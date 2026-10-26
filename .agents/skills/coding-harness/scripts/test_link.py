"""Live resolver behavior through local and shared workflow boundaries."""

import tempfile
import unittest
from pathlib import Path

import link


class LinkTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / "project"
        self.source = Path(self.tmp.name) / "source"
        for root in [self.root, self.source]:
            (root / ".agents/skills/development").mkdir(parents=True)
        self.shared = self.source / ".agents/skills/development/SKILL.md"
        self.shared.write_text("Shared")

    def test_live_source_changes_are_visible_without_copying_or_committing(self):
        result = link.resolve(self.root, self.source, "development")
        self.shared.write_text("Edited shared workflow")
        self.assertEqual(
            Path(result["skillPath"]).read_text(), "Edited shared workflow"
        )
        self.assertEqual(result["scope"], "shared")
        self.assertEqual(list((self.root / ".agents/skills/development").iterdir()), [])

    def test_local_override_wins_and_thin_entrypoint_does_not_override(self):
        local = self.root / ".agents/skills/development/SKILL.md"
        local.write_text("Local")
        self.assertEqual(
            link.resolve(self.root, self.source, "development")["scope"], "local"
        )
        local.write_text("<!-- coding-harness:entrypoint -->")
        self.assertEqual(
            link.resolve(self.root, self.source, "development")["scope"], "shared"
        )

    def test_child_workflow_and_resource_can_be_overridden_individually(self):
        for root in [self.root, self.source]:
            p = root / ".agents/skills/development/implement/SKILL.md"
            p.parent.mkdir()
            p.write_text(str(root))
        result = link.resolve(self.root, self.source, "development/implement")
        self.assertEqual(result["scope"], "local")
        (self.root / ".agents/skills/development/implement/SKILL.md").unlink()
        self.assertEqual(
            link.resolve(self.root, self.source, "development/implement")["scope"],
            "shared",
        )

    def test_bootstrap_finds_the_configured_clone_without_copying_workflows(self):
        import json
        import os
        import subprocess

        helper = self.source / ".agents/skills/coding-harness/scripts/link.py"
        helper.parent.mkdir(parents=True)
        helper.write_bytes(Path(link.__file__).read_bytes())
        bootstrap = self.root / ".agents/harness.py"
        bootstrap.write_bytes(
            (Path(link.__file__).parents[1] / "assets/harness.py").read_bytes()
        )
        result = subprocess.run(
            ["python3", str(bootstrap), "--skill", "development"],
            env={**os.environ, "CODING_HARNESS_HOME": str(self.source)},
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertEqual(json.loads(result.stdout)["skillPath"], str(self.shared.resolve()))

    def test_missing_or_escaping_workflow_fails(self):
        for name in ["../secret", "/absolute", "development/missing"]:
            with self.assertRaises(ValueError):
                link.resolve(self.root, self.source, name)


if __name__ == "__main__":
    unittest.main()
