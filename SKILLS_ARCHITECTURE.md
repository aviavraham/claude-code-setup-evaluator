# Skills Architecture

This document maps all skills, their purpose, activation triggers, and relationships.

## Skills Overview

### Core Verification & Review (always available)

**`verification-loop`** — Unified verification engine covering 7 phases: environment check, type check, lint, tests, code review, security scan, pre-push checks. Invoked by `/verify`, `/quality-gate`, and code-review commands. Core skill powering the entire QA workflow.

**`refactoring-patterns`** — Measurement-driven refactoring (profile → refactor → measure). Activates when user says "refactor", "clean up", "simplify", or when code has high complexity. Ensures changes improve metrics, not just code appearance.

**`update-docs`** — Reviews committed, staged, and unstaged changes against current docs, including already-edited docs. Check-only requests report findings without edits; update requests permit targeted corrections. Missing comparison evidence produces an incomplete review rather than a clean verdict.

**`security-check`** — Scans for credential leaks, secrets in code, insecure patterns, LLM API key exposure, PII leakage to external services, and `.env/.gitignore` misconfigurations. Runs automatically before commits and when editing credential-related code.

### Python Development (language-specific)

**`python-patterns`** — Unified conventions for team Python development:
- **Credentials:** dotenv loading, fail-fast on missing secrets, `.env.example` patterns
- **API clients:** timeouts (30s), transient retry logic, response validation, LLM response parsing
- **Testing:** TDD workflow, mock external APIs, set `random_state=42`, 80%+ coverage
- **Pipelines:** standard stage structure, JSON metadata, validation-before-processing, fail-fast, checkpointing

Replaces separate `python-conventions` and `data-pipeline-patterns` skills (merged for clarity).

### Design & Workflow

**`brainstorming`** — Design exploration before implementation. Activates when user asks "design", "how should i build", "what's the approach", "plan this out". Proposes 2-3 approaches with trade-offs, gets approval before coding.

**`cost-speed-meter`** — Tracks command execution times (tests, builds, lint) across sessions. Shows trends, detects regressions, suggests fast-path alternatives (unit tests vs integration). Measures if optimizations actually worked.

## Skill Activation Model

The nine migrated command skills described in [GUIDE.md](GUIDE.md#codex-cli-command-skills)
use explicit `$skill-name` invocation in Codex. Their `agents/openai.yaml` files
disable implicit invocation; the corresponding slash commands read the same
skill files. `architecture-docs` documents observed design, `dep-check` audits
the project environment/lockfiles, and `test-coverage` uses measured coverage
and configured thresholds without inventing percentages or per-file limits.

| Skill | Activation Type | Trigger |
|-------|-----------------|---------|
| `verification-loop` | Command-invoked | `/verify`, `/quality-gate`, code-review commands |
| `refactoring-patterns` | Declarative | User says "refactor", "simplify", "clean up", or high complexity detected |
| `update-docs` | Declarative | Code changes APIs/configs/CLI flags; user asks "update docs" |
| `security-check` | Declarative | Editing credential/secret handling code; before commits |
| `python-patterns` | Declarative | Editing Python code files (any `.py` file in context) |
| `brainstorming` | Declarative | User explicitly asks for design, planning, or approach exploration |
| `cost-speed-meter` | Automatic | Tracks all bash command execution; invoked via `/metrics` or `/metrics-report` |

## Command Dependencies

Commands that rely on specific skills:

| Command | Requires | Notes |
|---------|----------|-------|
| `/verify` | `verification-loop` | Runs phases 1-4: environment, types, lint, tests |
| `/quality-gate` | `verification-loop` | Runs phases 1-4 + phase 6: plus pre-push security |
| `/refactor-safe` | `verification-loop`, `refactoring-patterns` | Verify code works before refactoring, then measure |
| `/test-coverage` | `test-coverage` | Measures coverage and addresses requested meaningful gaps |
| `/update-docs` | `update-docs` | Standalone; detects stale docs from code changes |
| `/diff-explain` | `diff-explain` | Explains staged/unstaged changes and Git comparisons |
| `/explain-code` | None | Standalone; layered explanation by complexity |
| `/prompt-test` | `prompt-test` | Evaluates prompts using sanitized fixtures and explicit live-call scope |
| `/ai-engineer-review` | None | Standalone; architectural review |
| `/changelog` | `changelog` | Drafts release notes from a disclosed history baseline |
| `/dep-check` | `dep-check` | Audits project dependencies and discloses incomplete checks |
| `/env-check` | `env-check` | Diagnoses the project environment without repairs |
| `/architecture-docs` | `architecture-docs` | Documents existing architecture with optional quick Mermaid output |
| `/repo-sync` | `repo-sync` | Checks upstream freshness and local changes in focused repositories |
| `/recap` | `recap` | Summarizes observed session work or a requested history range |

## Removed Skills

**`redhat-writing`** — Deleted. This was user-specific (Red Hat brand voice/style). Does not belong in a generic meta-repo that others clone. Users who need it should add their own CLAUDE.md instructions locally.

**`python-conventions` (merged)** — Consolidated into `python-patterns` with `data-pipeline-patterns`. Both covered Python team conventions; one unified skill is clearer.

**`data-pipeline-patterns` (merged)** — Consolidated into `python-patterns`. Pipeline structure is a specific application of Python conventions, not separate.

## Token Budget

Always-loaded skills (loaded once per session):
- `verification-loop` — ~3KB (core engine)
- `refactoring-patterns` — ~2KB
- `security-check` — ~2KB
- `python-patterns` — ~4KB (credentials, APIs, testing, pipelines)
- `brainstorming` — ~2KB
- `cost-speed-meter` — ~4KB

**Total always-loaded: ~17KB** — under 5% of typical conversation context.

On-demand skills (load only when invoked):
- `update-docs` — reads relevant docs and change evidence when selected

## Design Rationale

1. **Merged python-conventions + data-pipeline-patterns** — Both were "team conventions for Python code." Keeping them separate created confusion about scope. One unified `python-patterns` skill is clearer and avoids redundancy.

2. **Explicit activation in ai-workspace.toml** — Skills can now be tracked as dependencies. Commands that require a skill have it documented. Future refactoring is safer.

3. **Removed redhat-writing from repo** — Generic meta-repo should not include user-specific or organization-specific content. Red Hat employees can add this locally to `~/.claude/CLAUDE.md`.

4. **Clarified brainstorming and cost-speed-meter** — Both had vague triggers ("when to activate"). Rewritten with explicit user-facing conditions (what the user asks for, not implicit context).

5. **Consolidated core verification** — Multiple commands (`/verify`, `/quality-gate`, `/refactor-safe`) all use `verification-loop`. Having them as separate commands is fine; they invoke the same skill with different phase subsets.
