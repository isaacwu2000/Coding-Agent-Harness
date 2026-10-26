---
name: coding-harness
description: Set up or use the central coding and design harness from a local clone. Resolve shared workflows with repo-local overrides; improve general guidance centrally and project-specific guidance locally.
---

# Coding Harness

Keep one editable local clone of the shared library. Receiving repos retain thin
entrypoints, project context, and specialized skills. Read the receiving repo's
AGENTS.md and relevant local context first; this clone's maintenance instructions
do not become application policy.

For setup or migration, read [adoption](references/adoption.md). Existing copied
installations need a reviewed migration; do not automatically delete local work.

## Use a workflow

From an adopted repo, run:

```sh
python3 .agents/harness.py --skill development
python3 .agents/harness.py --skill impeccable
```

Otherwise use this adapter's real directory (resolve symlinks):

```sh
python3 <adapter>/scripts/link.py --target <project> --skill development
```

Read the returned `skillPath`. Every shared workflow or resource may have a local
counterpart under the receiving repo's `.agents/skills/`; that counterpart wins.
For child workflows, use e.g. `--skill development/implement`. A thin entrypoint
marked `coding-harness:entrypoint` dispatches to the central copy rather than
overriding it. Resolve relative references from the actual selected file, keeping
commands' working directory in the receiving repo. Follow that repo's tooling,
product/design sources, acceptance, and publication policy.

Shared guidance is read directly from the clone, including uncommitted edits.
There is no file copying, background sync, or automatic GitHub pull. Reread a
changed workflow before relying on it in an existing task. A missing clone needs
local setup; report that instead of silently reading stale copied guidance.

## Where improvements belong

General workflow/design improvements: edit and validate the central local clone.
Project-specific behavior, identity, commands, evaluations, and exceptions: edit
the receiving repo's context or specialized skills. Prefer a small context
extension to duplicating an entire workflow. An intentional local workflow or
package override always takes priority. Publish only within the user's scope;
keep private project facts out of the public shared library.
