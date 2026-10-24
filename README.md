# Coding-Agent-Harness

A shared backbone for large-scale coding work across repositories and tools.
Extracted from LearnUnlock, with reviewed local adoption and versioned updates.
The harness supplies workflows, not an agent runtime or product UI.

## What's here

- [Coding harness adapter](.agents/skills/coding-harness/SKILL.md): clone locally,
  adopt into a project, sync reviewed updates, or route through a global entrypoint.

- [Development router](.agents/skills/development/SKILL.md): discovery, specifications,
  dependency-aware tickets, implementation, debugging, reviews, research, and handoffs.
- [Wayfinder](.agents/skills/development/wayfinder/SKILL.md): large, uncertain efforts
  spanning multiple sessions, with durable decisions and dependency-aware claims.
- [Implement spec](.agents/skills/development/implement-spec/SKILL.md): coordinate
  dependent implementation tickets and integrate work on one branch.
- [Domain modeling](.agents/skills/development/domain-modeling/SKILL.md): maintain
  project terminology and significant architectural decisions.
- [Impeccable](.agents/skills/impeccable/SKILL.md): shared design principles and
  procedures; each repo owns its visual identity and product behavior.
- [Writing for agents](.agents/skills/writing-for-agents/SKILL.md): reusable guidance
  for maintaining agent instructions.
- [Repository context contract](.agents/skills/development/references/repository-context.md):
  how shared workflows use repo-owned context, policies, tools, and skills.

The shared workflow says how to approach the work. Each repo defines its product,
architecture, design/UI workflow, verification commands, and delivery requirements.
Codex and other tools consume the guidance through their own supported entrypoints.
The portable adapter uses ordinary files and local scripts; automatic discovery
must use each tool's supported entrypoint. Codex global use is described below.

## Give this to your agent

> Clone https://github.com/isaacwu2000/Coding-Agent-Harness.git into a local
> directory I can keep and edit. Read its `.agents/skills/coding-harness/SKILL.md`
> and follow the adoption guide for my project. Inspect existing instructions and
> local changes first; show the migration differences, preserve project-specific
> rules and tools, and install a versioned local copy. Never overwrite unreviewed
> edits or migrate another project. Follow my existing scope for commits/pushes.

Developers and agents use a local clone and ordinary project files. The adapter
provides workflow; each project retains its own context and local skills.

## Explicit updates

[The adoption guide](.agents/skills/coding-harness/references/adoption.md) describes
first-time migration and subsequent syncs. The tool previews changes before apply,
records an exact clean source commit in `.agents/harness.json`, and refuses local
conflicts. It manages only its listed shared skills and checker. Root AGENTS.md,
project context, application code, and local skills stay project-owned. Nothing
syncs on a schedule or at task startup.

For a previously adopted repo, from your local harness clone:

```sh
python3 .agents/skills/coding-harness/scripts/sync.py plan --source . --target /path/to/project
python3 .agents/skills/coding-harness/scripts/sync.py apply --source . --target /path/to/project --expect-plan <digest-from-plan>
```

Edit reusable workflows in your local clone or fork and commit them before sync.
Changes made directly to installed shared files remain protected as conflicts;
review them for promotion or move project-specific exceptions into local context.

## Global use in local Codex

Codex reads user skills from `~/.agents/skills` and follows symlinked skill folders.
[Official skill documentation](https://learn.chatgpt.com/docs/build-skills).
Link only the adapter, using the absolute path to your local clone:

```sh
mkdir -p ~/.agents/skills
ln -s /absolute/path/to/Coding-Agent-Harness/.agents/skills/coding-harness ~/.agents/skills/coding-harness
```

Preserve an existing destination rather than replacing it. Invoke `$coding-harness`
to use the workflows or request adoption/sync. The adapter prefers a project's
adopted copy and otherwise uses the clone's sibling skills while respecting the
project's own instructions. Do not globally install the same full skill folders
alongside repo copies: Codex may show duplicate names rather than merge them.
No global AGENTS.md edit is required. If the skill does not appear, restart Codex.

## Checks

Check local guidance links and required skill metadata with
`python3 .agents/skills/check_links.py`.

Check shared Impeccable context isolation and native-reference loading with
`node --test .agents/skills/impeccable/scripts/context.test.mjs`.

Check sync behavior in isolated temporary repositories with
`python3 -m unittest discover -s .agents/skills/coding-harness/scripts -p "test_*.py"`.
