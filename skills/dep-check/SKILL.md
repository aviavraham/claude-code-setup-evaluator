---
name: dep-check
description: Use when explicitly asked to audit project dependencies for unused packages, available updates, vulnerabilities, or license metadata.
---

# Audit Project Dependencies

Accept a repository path, `--unused`, or `--security` from the invocation.
Otherwise use the current focus or project and run the relevant audit areas.
Use absolute paths and identify the project's package manager, manifests,
lockfiles, dependency groups, and installed environment before choosing tools.
Support multiple stacks and monorepo manifests within the requested scope.

Keep the audit diagnostic: do not install tools, update packages, rewrite
lockfiles, remove dependencies, or run automatic fixes. State when an audit
requires network access; do not upload private manifests, registry credentials,
or source to an external service without authorization for that disclosure.

## Inventory and unused packages

Read declared dependencies and resolved versions from project lockfiles such
as `uv.lock`, package-manager locks, `go.sum`, or `Cargo.lock`, accounting for
their different semantics. Distinguish declared constraints, locked resolution,
and observed installed versions. A global `pip list` does not describe the
project environment. If the environment is absent, say so and use lockfile
evidence where the audit tool supports it without installing dependencies.

For unused candidates, check source, configuration, entry points, scripts,
plugins, optional features, and test tooling. Account for package/import-name
differences and dynamic loading. A pytest plugin or CLI dependency need not
appear in an import. Label candidates with evidence and uncertainty; do not
recommend removal solely because no direct import was found.

## Updates, vulnerabilities, and licenses

Use available ecosystem tools against the target environment or lockfile.
Check installed tool help/version when needed to select supported options.
Capture diagnostics and exit status: a nonzero audit result may contain real
findings rather than an execution failure. Preserve findings before deciding
whether a fallback is needed; do not hide failures with `2>/dev/null` or an
unconditional alternative command.

Locked versions alone cannot establish current releases or vulnerability
status. If network access, advisory data, tools, or supported input formats
are unavailable, report the affected check as skipped/incomplete with the
reason and data age if known. Never report "no vulnerabilities" for a check
that did not complete. Identify advisory IDs, affected locked/installed
versions, and verified remediation information when available; an available
upgrade is not automatically compatible or safe to apply.

Read license metadata for the actual dependency versions. Flag missing or
potentially relevant obligations for review, with source/provenance. Do not
declare legal compatibility from a license name alone.

Report each area's scope, environment/lockfile used, tool/data provenance,
findings, skipped checks, and suggested next actions. Redact credentials in
registry URLs and diagnostics. Make no changes during this audit.
