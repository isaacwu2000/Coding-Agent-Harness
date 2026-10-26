"""Resolve live shared workflows with repository-local overrides."""

import argparse
import json
import os
import subprocess
from pathlib import Path, PurePosixPath

SOURCE_URL = "https://github.com/isaacwu2000/Coding-Agent-Harness.git"


def checkout(project):
    project = Path(project).resolve()
    result = subprocess.run(
        ["git", "-C", str(project), "rev-parse", "--show-toplevel"],
        capture_output=True,
        text=True,
        check=False,
    )
    return Path(result.stdout.strip()).resolve() if result.returncode == 0 else project


def source_for(project, explicit=None):
    root = checkout(project)
    config = subprocess.run(
        ["git", "-C", str(root), "config", "--local", "--get", "harness.source"],
        capture_output=True,
        text=True,
        check=False,
    )
    candidates = [
        explicit,
        os.environ.get("CODING_HARNESS_HOME"),
        config.stdout.strip() if config.returncode == 0 else None,
        root.parent / "Coding-Agent-Harness",
    ]
    # The global adapter may itself be a symlink into a clone at any location.
    global_adapter = Path.home() / ".agents/skills/coding-harness"
    if global_adapter.exists():
        candidates.insert(3, global_adapter.resolve().parents[2])
    for candidate in candidates:
        if candidate:
            path = Path(candidate).expanduser().resolve()
            if (path / ".agents/skills/coding-harness/scripts/link.py").is_file():
                return path
            if explicit:
                break
    raise ValueError(
        f"Clone {SOURCE_URL} locally and set CODING_HARNESS_HOME or git config --local harness.source /absolute/clone/path"
    )


def resolve(project, source, skill=None):
    root, source = checkout(project), Path(source).resolve()
    result = {
        "mode": "linked",
        "project": str(root),
        "sharedSkillsPath": str(source / ".agents/skills"),
        "localSkillsPath": str(root / ".agents/skills"),
    }
    if skill:
        name = PurePosixPath(skill)
        if name.is_absolute() or ".." in name.parts or str(name) != skill:
            raise ValueError("Skill must be a relative workflow path")
        relative = name if name.suffix else name / "SKILL.md"
        manifest = root / ".agents/harness.json"
        local_packages = (
            json.loads(manifest.read_text()).get("localPackages", [])
            if manifest.is_file()
            else []
        )
        if not isinstance(local_packages, list) or not all(
            isinstance(name, str) for name in local_packages
        ):
            raise ValueError("Manifest localPackages must be a list of package names")
        coupled_local = relative.parts[0] in local_packages
        local = root / ".agents/skills" / relative
        shared = source / ".agents/skills" / relative
        # Thin entrypoints dispatch to the shared workflow rather than to themselves.
        entrypoint = (
            local.is_file()
            and b"<!-- coding-harness:entrypoint -->" in local.read_bytes()
        )
        selected = (
            local if coupled_local or (local.is_file() and not entrypoint) else shared
        )
        if not selected.is_file():
            raise ValueError(f"Workflow not found: {skill}")
        result.update(
            skillPath=str(selected), scope="local" if selected == local else "shared"
        )
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", default=".")
    parser.add_argument("--source")
    parser.add_argument("--skill")
    args = parser.parse_args()
    try:
        print(
            json.dumps(
                resolve(args.target, source_for(args.target, args.source), args.skill)
            )
        )
    except (ValueError, OSError) as error:
        parser.exit(1, str(error) + "\n")


if __name__ == "__main__":
    main()
