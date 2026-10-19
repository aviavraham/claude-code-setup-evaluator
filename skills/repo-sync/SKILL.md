---
name: repo-sync
description: Use when explicitly asked to check focused repositories for upstream changes, local changes, or synchronization status.
---

# Repository Sync Check

Accept repository names or paths from the invocation. Otherwise use the current
conversation's focused repositories, then the current repository. Ask only if
the target is still ambiguous. Resolve names against the workspace containing
this skill; use absolute paths and `git -C "$repo"` for every command. A nested
project's Git root is not the workspace root.

For each repository:

1. Read branch, tracking configuration, and `git status --short`, including
   untracked files. Resolve the configured upstream rather than assuming
   `origin` or that local and remote branch names match.
2. Fetch the tracking remote with a bounded timeout. Capture its exit status
   and a redacted error summary. Fetching updates tracking refs; it does not
   authorize pulling, switching branches, stashing, committing, or pushing.
3. If fetching succeeds, run
   `git -C "$repo" rev-list --left-right --count 'HEAD...@{upstream}'`.
   The first count is ahead, the second behind. Report divergence when both
   counts are nonzero.
4. If fetch fails, report remote freshness as **unknown**. Cached counts may
   be shown as cached, but never establish that the repo is up to date.
   Missing upstream, detached HEAD, and unborn branches also need explicit
   statuses; do not invent a tracking branch. Continue checking other repos.

Report path, branch/upstream, ahead/behind status, and local changes for each
repo. When behind, suggest the next action. Only perform a pull or other
working-tree mutation if separately authorized; use the actual tracking
configuration and account for dirty files and divergence first.
