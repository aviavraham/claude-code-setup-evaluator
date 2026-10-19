---
name: env-check
description: Use when explicitly asked to diagnose a repository's development environment, runtime, dependencies, configuration, or local Git hooks.
---

# Diagnose the Development Environment

Resolve the supplied path, focused repository, or current repository to an
absolute path. Check that project, not the enclosing multi-repository workspace.
Detect its stack and package manager from manifests, lockfiles, runtime files,
and setup documentation before choosing checks. Support mixed-stack projects
without running Python checks against unrelated stacks.

This is diagnosis: do not install packages, synchronize environments, rewrite
lockfiles, run migrations, or repair configuration. In particular, `go mod tidy`
is not a diagnostic check. Avoid checks that download dependencies or import
application code merely to discover configuration. Use existing local tooling
and mark checks requiring unavailable tools as blocked or skipped.

Check the relevant areas:

- **Runtime:** compare the installed version against the project's actual
  requirement, including ranges. Report missing runtimes explicitly.
- **Dependencies:** inspect the selected environment and lockfile using
  available nonmutating package-manager checks. A global environment does not
  prove the project environment is healthy. Do not report outdated versions
  without current evidence.
- **Configuration:** compare expected variable names with configured names,
  reporting only missing/empty status. Parse sensitive files locally without
  printing their contents, values, or secret-bearing error output. Do not
  `source` dotenv files or execute configuration. Distinguish placeholders
  from demonstrated requirements.
- **Hooks:** inspect `core.hooksPath` when set; otherwise resolve the hooks
  location through `git rev-parse --git-path hooks`, in that repository.
  Account for relative configured paths and `.git` files in worktrees and
  submodules. Check relevant hook presence without executing it.
- **Migrations:** if the project documents a nonmutating pending-migrations
  check and the required services are available, report its result. Otherwise
  mark migration status unknown; never apply migrations during diagnosis.

Continue independent checks after a failure. Mark dependent checks blocked
instead of interpreting a missing tool as success. Report PASS, FAIL, WARN,
or SKIPPED per area with observed evidence and concrete suggested fixes.
Leave repairs for a separately requested action.
