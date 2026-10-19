---
name: changelog
description: Use when explicitly asked to draft release notes or a changelog from a Git tag, commit range, or recent history.
---

# Draft a Changelog

Work in the supplied repository or current focus using an absolute path.
Accept a starting tag, explicit range, or positive commit count from the
invocation. Validate refs before reading history.

Without a range, use the nearest reachable tag from
`git describe --tags --abbrev=0`, then inspect `<tag>..HEAD`. If there are no
tags, inspect the last 50 commits and explicitly label this bounded fallback:
it is not necessarily the full history or a complete release. Report shallow
or unavailable history when it limits coverage. An unborn repository has no
release history to summarize.

Read commit bodies and inspect relevant patches, including when the subject
looks clear. Include merge-result behavior: compare a merge with its first
parent, then avoid duplicating the same changes from constituent commits.
Do not filter all merges out. For a root commit use its initial patch.

Synthesize related commits into entries describing what users gain or must
change. Use the project's established changelog format; otherwise use the
Keep a Changelog categories Added, Changed, Fixed, Deprecated, Removed, and
Security. Give breaking changes and migration instructions a clear note.
Omit empty categories and routine internal/test-only work unless it affects
users; optionally summarize meaningful CI/infrastructure changes separately.

State the exact baseline/range and scope limitations. Draft an Unreleased
section unless a release version was supplied; do not invent a release date
or version. Present the draft in chat by default. Write it to a file only
when requested, preserving existing historical entries. Do not tag, commit,
or publish as part of drafting release notes.
