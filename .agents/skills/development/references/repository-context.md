# Repository context contract

Run shared workflows in the receiving repository, with paths resolved from its
root. Relative Markdown links within the shared skill tree resolve from the file
containing the link. Shared skills supply workflow; the repo supplies local facts
and policy. Follow the user's scope and the environment's governing instructions.

Start with the receiving repository's `AGENTS.md` and any applicable nested
instructions. Load only the context relevant to the task:

| Need | LearnUnlock convention | Repository owns |
| --- | --- | --- |
| Product and domain | `.agents/context/PRODUCT.md`, `CONTEXT.md` | Users, vocabulary, architecture, constraints |
| Implementation | `.agents/context/CODING_STANDARDS.md` | Language, package manager, boundaries, conventions |
| Verification | `.agents/context/TESTING.md` | Commands, environments, shared state, live checks |
| Design | Shared Impeccable or a repo-selected design skill, plus repo-owned design sources | Visual identity, components, UI workflow |
| Delivery | `.agents/context/DEPLOY.md` | Targets, deployment procedure, production acceptance |
| Workflow extensions | `.agents/context/WORKFLOW.md` or AGENTS.md pointers | Local skills, task-specific workflow and acceptance specializations |
| Coordination | `.agents/context/ISSUE_TRACKER.md` | Tracker, project, tools, labels, claims, dependencies |

These filenames are conventions, not required empty files. Where a workflow names
one of them, follow the equivalent source identified by the repo, including for historical hardcoded path mentions in these extracted skills. If none exists,
inspect the relevant configuration and ask only for material missing decisions.
A missing deployment document does not imply permission to deploy.

Resolve package tooling per active package from its manifest (`packageManager`,
engines, and scripts), current lockfile, and CI setup. Reconcile stale tool rules
in repo-owned instructions when authorized; a copied Bun rule does not govern a
pnpm app. Package-manager choice and a script's runtime are separate: preserve
intentional Bun runtimes when invoking existing scripts through pnpm. Keep
mixed-package repositories scoped rather than imposing one global tool rule.
Check the executable version before installs or lockfile changes: managed tool
shims may ignore manifest pins. Use supported version selection to honor the
project’s pin instead of silently regenerating locks with a different major.

Repository-specific skills extend this router through the repo's `AGENTS.md`;
keep them outside the shared folders. A local policy may specialize a shared
workflow without editing its shared copy. Shared updates should preserve that
separation. The [coding-harness adapter](../../coding-harness/SKILL.md) owns explicit
adoption and live resolution. Receiving repos route from AGENTS.md through the
resolver, keeping generic skills central. Optional thin entrypoints support tools
that need skill discovery. When following a shared workflow or resource, use its
repo-local counterpart if present; otherwise read it directly from the central
checkout.

Use tools actually available in the environment. `/skill-name` means load that
workflow; it does not assume a literal slash command exists. Delegate when the
workflow calls for it and delegation is supported and authorized; otherwise work
sequentially and state any material limit on independence or coverage.
