---
name: diff-explain
description: Use when explicitly asked to explain uncommitted changes, a branch comparison, a commit, a commit range, or a pull request by purpose and impact.
---

# Explain Changes

Use the repository path supplied in the invocation, the conversation's focus,
or the current repository. Resolve it to an absolute path and run Git there.
Read changes without editing files or switching the user's checkout.

Choose the evidence matching the request:

- No comparison supplied: inspect **both** `git diff` and `git diff --cached`,
  plus status. Keep staged and unstaged changes distinguishable even when
  grouping them by purpose. List untracked paths separately; inspect relevant
  text files before describing their contents, avoiding secrets and binaries.
- Branch: validate the requested ref and inspect the merge-base comparison
  (`git diff <branch>...HEAD`) and relevant commit messages. Do not substitute
  `main` for a supplied branch.
- Range such as `A..B`: inspect the commit messages and actual patches in the
  range. Use `git diff A B` for the net endpoint change; distinguish that from
  per-commit history when changes were reverted within the range.
- Single commit: inspect `git show <commit>` and its parent comparison. For
  merges inspect the first-parent diff so merge-result changes are visible.
- PR/MR: use the available authenticated provider tooling to read its metadata
  and diff. Report unavailable access without claiming the review is complete.

Group related changes by purpose. Explain what changed, the user-visible
impact, affected paths, compatibility implications, and useful verification.
Support conclusions with code or commit evidence. Label a guessed motivation
as an inference; do not attribute unsupported intent to the author. Summarize
large changes with disclosed scope limits rather than silently omitting them.
