---
description: "Explain a git diff or branch comparison in plain language. Describes the intent behind changes, not just what files were modified. Useful for MR reviews and catching up."
---

# diff-explain

Follow the [diff-explain skill](../../skills/diff-explain/SKILL.md) for this workflow.
Resolve the skill from this command's workspace location, even when the
working directory is inside a focused repository. Read its SKILL.md
directly if the host has no skill-invocation tool.

Treat the user's text after the command as the invocation arguments,
including any repository path, range, mode, or style. In Codex CLI,
invoke the same workflow explicitly as `$diff-explain`.
