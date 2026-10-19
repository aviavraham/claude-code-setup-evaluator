---
description: "Find and update stale documentation after code changes. Scans all doc files in the focused repo, matches against the diff, and proposes targeted updates for review."
---

# update-docs

Follow the [update-docs skill](../../skills/update-docs/SKILL.md) for this workflow.
Resolve the skill from this command's workspace location, even when the
working directory is inside a focused repository. Read its SKILL.md
directly if the host has no skill-invocation tool.

Treat the user's text after the command as the invocation arguments,
including any repository path, range, mode, or style. In Codex CLI,
invoke the same workflow explicitly as `$update-docs`.
