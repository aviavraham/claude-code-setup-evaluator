---
description: "Generate a quarterly achievement report by aggregating Jira, GitHub, and GitLab data, analyzing cycle times, and creating polished performance review narratives."
---

# Quarterly Report Command

Use the Skill tool to invoke `quarterly-report-assistant`, then follow its four-phase workflow:

1. **Information Gathering** — Ask for quarter/year, usernames, project filters
2. **Data Collection** — Fetch Jira issues (via `acli`), GitHub PRs (via `gh`), GitLab MRs (via `glab`), analyze cycle times
3. **Narrative Refinement** — Transform top achievements into polished narratives
4. **Report Generation** — Save enhanced markdown report

If the Skill tool is not available or the skill is not found, read `skills/quarterly-report-assistant/SKILL.md` directly and follow it.

## Arguments

$ARGUMENTS can be:
- A quarter/year like `Q2 2026` to skip the quarter question
- Empty to start the full interactive workflow
