# One shared checkout, local overrides

Clone `https://github.com/isaacwu2000/Coding-Agent-Harness.git` into the developer's
normal checkout area. They can edit it or use their own fork. Preserve attribution
and licenses. Use local files and scripts rather than remote shell piping.

## Local Codex setup

Link only the adapter into `~/.agents/skills/coding-harness`, preserving an existing
destination. Use an absolute path to this clone's `.agents/skills/coding-harness`.
Verify the link and readable SKILL.md. Invoke `$coding-harness` on a subsequent
turn; restart Codex if discovery has not refreshed. Other agents use their own
supported entrypoints; no global AGENTS.md change is required.

## Adopt or migrate a repo

1. Read local AGENTS.md, relevant context, skill files, and current Git changes.
   Check each package's actual manifest, lockfile, and CI tooling. Preserve
   unrelated work and correct stale package-manager rules within authorized scope.
2. Review copied shared workflows. Keep specialized local skills, context, and
   genuinely different behavior. Move small product-specific rules into local
   workflow context. Preserve coupled local packages with capabilities absent
   centrally, rather than mixing their engine files with shared ones.
3. Remove reviewed shared copies and route coding, design, and guidance work
   from AGENTS.md to `python3 .agents/harness.py --skill <name>`. Instruct agents
   to read the returned `skillPath` alongside local context. Keep generic skills
   in the central clone. Add thin skill entrypoints only when a tool needs them
   for discovery; mark those with `<!-- coding-harness:entrypoint -->` so they
   dispatch rather than override. Existing local overrides keep their normal paths.
4. Copy [the bootstrap](../assets/harness.py) to `.agents/harness.py`. Write a
   small `.agents/harness.json` with `schemaVersion: 2`, `mode: linked`, and
   `sourceRepository` identifying the clone's public origin (without credentials).
   Document local exceptions in repo-owned context. Set this machine's source:

   ```sh
   git config --local harness.source /absolute/path/to/Coding-Agent-Harness
   ```

   The bootstrap also supports `CODING_HARNESS_HOME`, a sibling harness clone,
   and the global adapter symlink. Keep machine paths out of tracked files.
5. Replace old copy/sync instructions and dangling child-file links with
   explicit resolver commands. Read the repo's local context alongside
   shared workflows. Test root and child resolution, verify local priority, and
   run guidance checks. Inspect the diff and preserve unrelated work. Commit or
   push only within the user's scope and local delivery rules.

A fresh developer clones the library locally and sets the checkout path. The
repo never needs a second full copy of the shared skill tree. New shared edits
are visible on the next read, without a commit or sync. Existing agent context
must be reread. GitHub updates arrive when the developer updates their clone.

## Ownership

General improvements go in the central clone; project-specific changes stay in
local context or skills. Local versions always win. A whole local Impeccable
installation may remain intentional when its engine has additional capabilities.
Updating or replacing it requires a reviewed migration preserving those features.

Legacy schema-1 copied installations may still use `scripts/sync.py` until they
are migrated; the copy utility is retained for compatibility, not the new default.
