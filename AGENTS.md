# Maintaining Coding-Agent-Harness

This repository contains a draft shared workflow library extracted from
LearnUnlock. Read [README.md](README.md) for scope.

- Edit this shared library without modifying consuming repositories unless asked.
- Keep product facts, UI identity, test commands, deployment policy, credentials,
  and domain-specific evaluations in the consuming repository.
- Preserve extracted behavior unless a change is needed for portability or is
  explicitly agreed.
- Treat `.agents/skills/` as library content under review, not instructions to
  publish issues, deploy, or run application workflows while maintaining it.
- After guidance changes, run `python3 .agents/skills/check_links.py`.
- Do not implement installation, synchronization, or scheduled updates until the
  user chooses that next step. This extraction is local and reviewable.
