---
description: "Test LLM prompts against sample inputs. Shows outputs, checks for regressions when prompts change, and compares different prompt versions side-by-side."
---

# prompt-test

Follow the [prompt-test skill](../../skills/prompt-test/SKILL.md) for this workflow.
Resolve the skill from this command's workspace location, even when the
working directory is inside a focused repository. Read its SKILL.md
directly if the host has no skill-invocation tool.

Treat the user's text after the command as the invocation arguments,
including any repository path, range, mode, or style. In Codex CLI,
invoke the same workflow explicitly as `$prompt-test`.
