---
description: "Check if focused repositories are up to date with the remote. Fetches latest changes and warns about repos that are behind or have uncommitted changes."
---

# repo-sync

Follow the [repo-sync skill](../../skills/repo-sync/SKILL.md) for this workflow.
Resolve the skill from this command's workspace location, even when the
working directory is inside a focused repository. Read its SKILL.md
directly if the host has no skill-invocation tool.

Treat the user's text after the command as the invocation arguments,
including any repository path, range, mode, or style. In Codex CLI,
invoke the same workflow explicitly as `$repo-sync`.
