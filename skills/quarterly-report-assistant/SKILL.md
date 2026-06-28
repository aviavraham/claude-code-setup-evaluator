---
name: quarterly-report-assistant
description: >-
  Use when the user mentions quarterly reviews, performance reviews, quarterly
  reports, Q1/Q2/Q3/Q4 summaries, "what did I accomplish", or wants to analyze
  work output for a specific time period. Automates report generation by
  aggregating Jira, GitHub, and GitLab data, analyzing cycle times, and
  creating polished performance review narratives.
  Activated by command: /quarterly-report
---

# Quarterly Report Assistant

Generate comprehensive quarterly achievement reports by aggregating data from
Jira, GitHub, and GitLab, analyzing cycle times, identifying top achievements,
and transforming technical descriptions into polished narratives.

## Reference Files

| Task | File |
|------|------|
| Writing achievement narratives | [narrative-frameworks.md](references/narrative-frameworks.md) |

## Overview

**Before:** 4-6 hours digging through Jira/GitHub, writing dry technical descriptions

**After:** 30 minutes of focused refinement using AI-powered analysis and narrative generation

## Prerequisites

### Required CLI Tools

**Required:**
- **acli (Atlassian CLI)**: `acli auth login`
- **GitHub CLI**: `gh auth login`

**Optional:**
- **GitLab CLI**: `glab auth login`

### Verify Installation

```bash
acli jira workitem search --jql "reporter = currentUser()" --limit 1
gh api user
glab api user  # optional
```

## Four-Phase Workflow

### Phase 1: Information Gathering

**Questions to ask:**
1. Which quarter and year? (e.g., Q1 2026)
2. What is your base username?
3. What is your Jira username? (often email: user@example.com)
4. What is your GitHub username? (handle)
5. What is your GitLab username? (optional)
6. Jira project filter? (e.g., WINC, optional)
7. GitHub organization filter? (e.g., openshift, optional)

**Why different usernames matter:**
- Jira typically uses email format (user@company.com)
- GitHub uses handle format (username)
- GitLab may differ from both

### Phase 2: Data Collection and Analysis

**Step 2.1: Fetch Jira Issues**

```bash
acli jira workitem search \
  --jql "reporter = currentUser() AND created >= '2026-01-01' AND created <= '2026-03-31' AND project = {PROJECT}" \
  --paginate --json
```

The `search` command does not return `created` or `resolutiondate` fields.
For each issue, fetch dates individually:

```bash
acli jira workitem view {ISSUE_KEY} --fields "key,summary,status,issuetype,created,resolutiondate,priority" --json
```

Extract: issue keys, summaries, types, statuses, created/resolved dates.
Calculate cycle time: (resolved_date - created_date) in days.

**Step 2.2: Fetch GitHub PRs**

```bash
gh api search/issues --method GET \
  -f q="author:{github_username} is:pr is:merged merged:2026-01-01..2026-03-31 org:{org}" \
  --paginate \
  --jq '.items[] | {number: .number, title: .title, repository: .repository_url, merged_at: .closed_at, html_url: .html_url}'
```

For each PR, fetch details for cycle time:

```bash
gh pr view {pr_number} --repo {owner/repo} --json number,title,createdAt,mergedAt,changedFiles,additions,deletions
```

Calculate cycle time: (merged_at - created_at) in days.

**Step 2.3: Analyze Cycle Times**

Calculate and present:

**Jira metrics:**
- Average cycle time, longest 10 issues, distribution by type

**GitHub metrics:**
- Average cycle time, longest 10 PRs, distribution by repo, total lines changed

**Step 2.4: Identify Top Achievements**

Apply THREE ranking strategies:

1. **By cycle time** — longest-running = likely strategic/foundational
2. **By impact** — boost scores for infrastructure keywords (infrastructure, framework, automation +50%; release, backport +30%; CI, test +20%)
3. **By complexity** — PRs: (files_changed * 0.5) + (lines_added / 100); Jira: cycle_days

Items appearing in top 10 of multiple rankings = top achievements.

### Phase 3: Achievement Narrative Refinement

For each top 5 achievement:

1. **Gather detailed context** — fetch PR details (`gh pr view --json body,labels,commits`), Jira details (`acli jira workitem view --fields "*all" --json`)
2. **Apply narrative frameworks** — write three versions (Business Impact, Technical Depth, Leadership) per the [narrative-frameworks.md](references/narrative-frameworks.md) reference
3. **Choose best style** — match framework to achievement type

### Phase 4: Report Generation

**Step 4.1: Compile Data Summary**

From CLI queries, compile:
- Jira: total filed, closed, closure rate, breakdown by status/type, avg cycle time
- GitHub: total merged, breakdown by repo, avg cycle time, total lines changed
- GitLab (if applicable): total MRs merged, breakdown by project

**Step 4.2: Create Enhanced Markdown Report**

Combine data summary with refined narratives into three sections:
1. **Top Accomplishments** — 2-4 paragraph narratives per achievement with WHAT/HOW/WHY
2. **By The Numbers** — summary table with key metrics
3. **How I Work** — patterns across achievements (strategic thinking, fast iteration, etc.)

**Step 4.3: Save Report**

Save as `~/Q{quarter}-{year}-Accomplishments-Enhanced.md`

Offer to:
1. Refine specific sections further
2. Add more achievements (beyond top 5)
3. Compare with previous quarter
4. Generate a shorter executive summary (for Workday text box)

## Edge Cases

**CLI tools not installed:**
```bash
command -v acli || echo "acli (Atlassian CLI) not installed"
command -v gh || echo "GitHub CLI not installed"
command -v glab || echo "GitLab CLI not installed (optional)"
```

**User doesn't know their usernames:**
- Jira: `acli jira workitem search --jql "reporter = currentUser()" --limit 1 --json`
- GitHub: `gh api user --jq .login`
- GitLab: `glab api user --jq .username`

**CLI authentication expired:**
- Jira: `acli auth login`
- GitHub: `gh auth refresh`
- GitLab: `glab auth login`

**No data returned:** Verify auth, check date format (YYYY-MM-DD), try without filters.

**Too many achievements (100+ PRs):** Focus on top 10 by cycle time, group related PRs into themes, prioritize infrastructure over bug fixes.

**Rate limits:** Check with `gh api rate_limit`.

## Success Criteria

1. User gets a comprehensive enhanced markdown report
2. Top 5 achievements have polished WHAT/HOW narratives
3. Report includes cycle time analysis and "By the Numbers" summary
4. Report is ready to copy into Workday with minimal editing
5. Process takes ~30 minutes instead of 4-6 hours

## After Report Generation

Offer: executive summary, quarter-over-quarter comparison, drill into specific items, next-quarter goal suggestions.

**Don't auto-submit anywhere** — the report is a DRAFT for user refinement.
