---
description: "Diagnose the project's runtime, dependencies, configuration, Git hooks, and migration status without changing the development environment."
---

# env-check

Follow the [env-check skill](../../skills/env-check/SKILL.md) for this workflow.
Resolve the skill from this command's workspace location, even when the
working directory is inside a focused repository. Read its SKILL.md
directly if the host has no skill-invocation tool.

Treat the user's text after the command as the invocation arguments,
including any repository path, range, mode, or style. In Codex CLI,
invoke the same workflow explicitly as `$env-check`.
