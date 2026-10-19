---
name: recap
description: Use when explicitly asked for a session recap, standup draft, handoff, or work summary for a specified time range or branch.
---

# Session Recap

Accept a time range, branch, repository, or technical/executive style from the
invocation. Default to the work performed in this conversation, organized by
repository. A requested history summary can have a wider scope than a session.

Use conversation history to establish the task, actual actions, decisions,
and known starting state. Check current Git status and the relevant diffs and
commits to corroborate it. Use absolute paths for each repository.

Do not treat "last eight hours" or "last ten commits" as proof of session
ownership. Separate other authors' work, earlier commits, and pre-existing
local changes from this session's changes. If the starting state or attribution
is unavailable, disclose that limitation instead of inventing a baseline or
precise file totals. Honor an explicit branch/time range when provided and
label history-derived results as such.

Include outcomes and why they matter, key decisions, problems resolved,
remaining work, and relevant commit hashes. Report test commands and results
only when supported by observed output, with their scope. Use **not run in
this session** when appropriate. An earlier passing run does not establish
that subsequent edits pass.

Finish with a brief, ready-to-share standup or handoff draft. Adjust detail to
the requested audience. Keep private data and secrets out of the draft; do not
send it to Slack, email, or another person without explicit instruction.
