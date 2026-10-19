---
description: "Audit project dependencies for unused packages, available updates, known vulnerabilities, and license metadata, reporting incomplete checks explicitly."
---

# dep-check

Follow the [dep-check skill](../../skills/dep-check/SKILL.md) for this workflow.
Resolve the skill from this command's workspace location, even when the
working directory is inside a focused repository. Read its SKILL.md
directly if the host has no skill-invocation tool.

Treat the user's text after the command as the invocation arguments,
including any repository path, range, mode, or style. In Codex CLI,
invoke the same workflow explicitly as `$dep-check`.
