---
name: update-docs
metadata:
  version: "1.0"
description: >-
  Use when implementing features, fixing bugs, or refactoring code that may
  invalidate existing docs. Detects stale documentation by matching the code
  diff against in-repo doc files and applies targeted updates. Relevant when
  code changes rename, remove, or add APIs, fields, config keys, or CLI flags.
  Also applies when the user says "update docs", "check docs", or "are the
  docs stale", or when reviewing a branch for documentation accuracy.
---

# Update Docs

Review code changes against current documentation, including documentation
already edited in the branch or working tree. Preserve the user's existing
edits and update only claims contradicted by the changed behavior.

## Scope and mode

Resolve the supplied repository or current focus to an absolute path. Accept
a documentation path to restrict candidates, and an explicit comparison base
when supplied. “Check docs”, “review docs”, or `--check` means report findings
and proposed corrections without writing files. An explicit request to update
or fix docs permits targeted edits. If invoked automatically while implementing
a change, follow the task's existing authorization for documentation edits.

## Collect the complete change evidence

1. Record Git status and distinguish committed branch changes, staged changes,
   unstaged changes, and relevant untracked source/docs. Inspect the actual
   patches and current file contents, not just filenames or commit subjects.
2. For committed branch changes, validate an explicit base if provided.
   Otherwise discover the default branch from available local remote-HEAD
   refs or trusted project/PR configuration. Use the actual remote, which
   need not be `origin`, and preserve the full branch name, including slashes.
   Verified local default-branch candidates can be used when unambiguous;
   a feature branch's upstream is not necessarily the comparison base.
3. Use the verified base's merge-base with HEAD for the committed branch diff.
   Separately inspect `git diff --cached` and `git diff` for local changes.
   Account for renames and deletions using both old and new identifiers.
   Compare documentation against the effective current code; explain any
   staging boundary that would leave a commit's documentation inconsistent.
4. If the base, history, or any required diff is unavailable, report the
   limitation and continue the checks that remain possible. Do not interpret
   a Git error as an empty diff or report a complete clean review. Ask for a
   base only when needed to finish the requested comparison.
5. If all inspected code diffs are empty, still review relevant documentation
   edits for accuracy. Skip untracked binaries, generated artifacts, and
   secret-bearing files; disclose exclusions affecting the review.

## Discover and evaluate documentation

Discover existing documentation within the selected repository: README/index
files, dedicated documentation trees, diagrams, and documented configuration
examples. Exclude vendored dependencies and generated output, not ordinary
docs changed in the PR. Review generated docs through their source when
relevant; do not edit generated output directly. Historical changelog/release
entries remain descriptions of their original release.

Build a per-file checklist of changed APIs, CLI flags, config keys, types,
and behavior. Search documentation for specific old and new identifiers with
literal matching (for example, `rg -n -F -- "$identifier"` over the selected
doc paths). Include every relevant changed source file; explain omissions.
Do not silently truncate discovery to the first 500 files or scan unrelated
repositories.

For each matched candidate, inspect the relevant context, then read the full
document before editing it. Mark claims stale only when the described
signature, behavior, or semantics contradict the code. A mention alone is not
a defect. Include docs already modified by the user: they can still be stale.

Also read the repository README and relevant documentation indexes/overviews,
even if identifier searches found no matches. Look for prose descriptions and
new behavior that cannot be found by searching exact code names.

## Apply or report

For an audit-only request, report stale passages with path/line, code evidence,
and proposed corrections. Leave all files unchanged.

For an authorized update, make narrow edits to existing documentation while
preserving format, unrelated content, and user changes. Do not create new docs
or rewrite history as part of this workflow. Recheck each corrected claim and
review the final diff for unintended changes. Follow the project's configured
documentation checks when applicable; report anything not verified.

Report scope/base, change states inspected, findings or edits, and limitations.
Use `DOCS_STALE` for confirmed audit-only findings, `DOCS_UPDATED` after edits,
`NO_DOCS_UPDATED` for a complete review needing no corrections, or
`NO_DOCS_FOUND` when complete discovery finds no applicable docs. Use
`INCOMPLETE_REVIEW` when missing evidence prevents a complete conclusion,
including partial findings when available. Do not stage, commit, or publish
documentation automatically.
