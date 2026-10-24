# Coding-Agent-Harness

A shared backbone for large-scale coding work across repositories and tools.
Initial draft extracted from LearnUnlock; no agent runtime or product UI.

## What's here

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
No cross-tool installation has been configured or tested yet.

## Updates — direction for discussion

Keep shared files centrally maintained and repo-specific files separate. A future
sync should record the shared revision, show changes, and preserve local work.
Improvements discovered in a project can be proposed back here; product-specific
exceptions stay in that project. Choosing the sync mechanism comes after reviewing
this extraction. Nothing currently syncs or changes LearnUnlock automatically.

Check local guidance links and required skill metadata with
`python3 .agents/skills/check_links.py`.

Check shared Impeccable context isolation and native-reference loading with
`node --test .agents/skills/impeccable/scripts/context.test.mjs`.
