---
name: test-coverage
description: Use when explicitly asked to measure test coverage, identify important untested behavior, or add focused tests for coverage gaps.
---

# Measure Coverage and Close Meaningful Gaps

Resolve the supplied repository/module/file or current focus to an absolute
path. Honor analysis-only requests without editing tests. When asked to add
tests, limit changes to the requested area and its important behaviors.

## Establish the baseline

Detect the actual test runner, environment, coverage tool, source selection,
and commands from project configuration, package scripts, documentation, and
CI. Include CLI flags and configured test-runner options when determining the
effective threshold. A `pyproject.toml` alone does not establish pytest as
the runner. If the runner remains ambiguous, ask rather than inventing one.

Use the project's existing coverage command and preserve its exit status.
Distinguish test failures, threshold failures, and unavailable tooling. Do not
install dependencies or rewrite configuration simply to collect a report.
Avoid truncating away failure details or letting a pipeline hide the status.

Use numeric thresholds only when configured or requested. State whether the
threshold is aggregate, branch, per-file, or a CI-specific ratchet. A 20%
aggregate floor does not make every file below 20% a failing file. If there
is no target, report measured coverage without imposing 80% or another goal.
Disclose conflicting local/CI settings and which command produced the result.

If coverage cannot be measured, report **coverage unavailable** and perform
a static review of tests and source. Treat suspected gaps as hypotheses:
integration tests may exercise modules with no matching test filename. Do
not estimate percentages from function/file counts or label modules 0%
without measurement. Line coverage alone does not establish branch coverage.

## Add tests when requested

Prioritize meaningful behavior: security and business rules, public contracts,
error handling, boundaries, and complex branches. Identify the concrete
behavior and failure each new test should detect. Follow project fixtures,
assertion style, and runner conventions; avoid tests of implementation details
or changes made only to increase a percentage. Use temporary resources and
mock external services when appropriate, while exercising real target logic.

Establish the baseline test result first. Add focused tests, run them, then
run the project's full applicable suite and remeasure coverage with the same
scope/settings. Report pre-existing failures separately; do not claim full
verification if the suite could not run. Stop after the requested meaningful
gaps are addressed; report any unmet configured threshold and remaining gaps
instead of expanding into unrelated code or weakening the threshold.

Report baseline/final measured coverage, line versus branch scope, applicable
thresholds, tests added, commands and exit statuses, limitations, and the next
highest-value gaps. Keep static observations separate from measured results.
