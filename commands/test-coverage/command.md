---
description: "Analyze test coverage, identify gaps, and generate focused missing tests. Respects the project's configured coverage target when one exists."
---

# test-coverage

Follow the [test-coverage skill](../../skills/test-coverage/SKILL.md) for this workflow.
Resolve the skill from this command's workspace location, even when the
working directory is inside a focused repository. Read its SKILL.md
directly if the host has no skill-invocation tool.

Treat the user's text after the command as the invocation arguments,
including any repository path, range, mode, or style. In Codex CLI,
invoke the same workflow explicitly as `$test-coverage`.
