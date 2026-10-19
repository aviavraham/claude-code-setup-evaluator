---
description: "Generate a changelog grouped by intent from git history. Reads commits since the last tag, classifies by purpose, and outputs Keep a Changelog format."
---

# changelog

Follow the [changelog skill](../../skills/changelog/SKILL.md) for this workflow.
Resolve the skill from this command's workspace location, even when the
working directory is inside a focused repository. Read its SKILL.md
directly if the host has no skill-invocation tool.

Treat the user's text after the command as the invocation arguments,
including any repository path, range, mode, or style. In Codex CLI,
invoke the same workflow explicitly as `$changelog`.
