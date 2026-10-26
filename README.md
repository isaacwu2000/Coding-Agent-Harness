# Coding-Agent-Harness

One shared coding and design workflow library for large-scale work across repos
and agents. Extracted from LearnUnlock; each product keeps its own facts,
identity, tools, testing, and delivery rules.

## Use it

Give this to your agent:

> Clone https://github.com/isaacwu2000/Coding-Agent-Harness.git into a local
> directory I can keep and edit. Read `.agents/skills/coding-harness/SKILL.md` and
> its adoption guide. Register only the adapter globally for local Codex,
> preserving any existing destination. For the repos I name, replace reviewed
> shared copies with thin entrypoints into this checkout. Preserve local context,
> specialized skills, local overrides, and concurrent work. General improvements
> go in this shared clone; project-specific improvements stay local. Follow my
> existing publication scope.

The [adoption guide](.agents/skills/coding-harness/references/adoption.md) describes
setup and migration. Adopted repos resolve workflows through a small bootstrap:

```sh
python3 .agents/harness.py --skill development
python3 .agents/harness.py --skill development/implement
python3 .agents/harness.py --skill impeccable
```

Read the returned `skillPath`. A local workflow or resource takes priority over
the central version. Shared edits are available directly from this local clone,
including uncommitted changes; existing tasks must reread updated guidance.
There is no copied development set, automatic GitHub pull, or background sync.
Keep machine paths in local Git configuration or `CODING_HARNESS_HOME`.

## What's shared

- [Development](.agents/skills/development/SKILL.md): discovery, specifications,
  tickets, implementation, tests, diagnosis, review, research, and handoffs.
- [Wayfinder](.agents/skills/development/wayfinder/SKILL.md): large uncertain work
  spanning sessions, with durable decisions and dependencies.
- [Implement spec](.agents/skills/development/implement-spec/SKILL.md): coordinate
  an agreed ticketed effort.
- [Domain modeling](.agents/skills/development/domain-modeling/SKILL.md): vocabulary
  and architectural decisions.
- [Impeccable](.agents/skills/impeccable/SKILL.md): design principles and procedures;
  each repo retains its own identity and product behavior.
- [Writing for agents](.agents/skills/writing-for-agents/SKILL.md): agent guidance.
- [Repository context contract](.agents/skills/development/references/repository-context.md):
  how shared workflows use repo-owned policies and extensions.

General improvement → central clone. Project-specific improvement → local repo.
Intentional local packages with additional capabilities remain local overrides.
The old copy/sync helper remains only for existing installations awaiting migration.

## Local Codex discovery

Link the adapter using your clone's absolute path:

```sh
mkdir -p ~/.agents/skills
ln -s /absolute/path/to/Coding-Agent-Harness/.agents/skills/coding-harness ~/.agents/skills/coding-harness
```

Keep an existing destination; do not force-replace it. Invoke `$coding-harness`.
No global AGENTS.md edit is needed. Other tools use their own supported discovery
paths. If Codex hasn't discovered the new skill, restart it.

## Checks

```sh
python3 .agents/skills/check_links.py
python3 -m unittest discover -s .agents/skills/coding-harness/scripts -p 'test_*.py'
node --test .agents/skills/impeccable/scripts/context.test.mjs
```
