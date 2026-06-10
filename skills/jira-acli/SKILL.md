---
name: jira-acli
description: Use when interacting with Jira — reading tickets, creating work items, updating descriptions, searching with JQL, adding comments, transitioning status, or linking issues. Triggers on Jira URLs, ticket IDs (e.g. AIPCC-XXXXX), or requests to check/update/create Jira tickets.
---

# Jira via acli

CLI tool for Jira Cloud. Authenticated to `redhat.atlassian.net` as `aavraham@redhat.com`. Config stored in `~/.config/acli/jira_config.yaml`.

## Quick Reference

| Action | Command |
|--------|---------|
| View ticket | `acli jira workitem view KEY-123` |
| View as JSON | `acli jira workitem view KEY-123 --json` |
| View specific fields | `acli jira workitem view KEY-123 --fields "summary,status,description"` |
| Search (JQL) | `acli jira workitem search --jql "project = PROJ AND status = 'In Progress'"` |
| Search (count only) | `acli jira workitem search --jql "..." --count` |
| Search (all results) | `acli jira workitem search --jql "..." --paginate` |
| Search (CSV export) | `acli jira workitem search --jql "..." --csv` |
| Find children | `acli jira workitem search --jql "parent = KEY-123"` |
| Create ticket | `acli jira workitem create --project "PROJ" --type "Task" --summary "Title" --description "Body"` |
| Create with parent | `acli jira workitem create --project "PROJ" --type "Task" --summary "Title" --parent "KEY-123"` |
| Create from file | `acli jira workitem create --project "PROJ" --type "Task" --summary "Title" --description-file desc.txt` |
| Edit description | `acli jira workitem edit --key KEY-123 --description "New text" --yes` |
| Edit from file | `acli jira workitem edit --key KEY-123 --description-file desc.txt --yes` |
| Edit summary | `acli jira workitem edit --key KEY-123 --summary "New title" --yes` |
| Add labels | `acli jira workitem edit --key KEY-123 --labels "label1,label2" --yes` |
| Assign | `acli jira workitem edit --key KEY-123 --assignee "user@redhat.com" --yes` |
| Self-assign | `acli jira workitem edit --key KEY-123 --assignee "@me" --yes` |
| Transition status | `acli jira workitem transition --key KEY-123 --status "In Progress" --yes` |
| Add comment | `acli jira workitem comment create --key KEY-123 --body "Comment text"` |
| Comment from file | `acli jira workitem comment create --key KEY-123 --body-file comment.txt` |
| List comments | `acli jira workitem comment list KEY-123` |
| Link issues | `acli jira workitem link create --out KEY-1 --in KEY-2 --type "Blocks"` |
| List links | `acli jira workitem link list KEY-123` |
| List projects | `acli jira project list` |

## Long Descriptions

Jira descriptions support plain text. For multi-line or formatted content, write to a file first and use `--description-file`:

```bash
cat > /tmp/desc.txt << 'EOF'
h2. Section Title

* Bullet one
* Bullet two

h3. Subsection

Paragraph text here.
EOF

acli jira workitem edit --key KEY-123 --description-file /tmp/desc.txt --yes
```

Jira wiki markup: `h2.` for headings, `*` for bullets, `#` for numbered lists, `{code}...{code}` for code blocks.

## Common JQL Patterns

```bash
# My open tickets
--jql "assignee = currentUser() AND status != Done"

# Sprint tickets
--jql "project = PROJ AND sprint in openSprints()"

# Recently updated
--jql "project = PROJ AND updated >= -7d ORDER BY updated DESC"

# Epics in a project
--jql "project = PROJ AND issuetype = Epic"

# By label
--jql "labels = 'my-label'"

# Text search
--jql "project = PROJ AND text ~ 'search term'"
```

## Work Item Types

Common types: `Epic`, `Story`, `Task`, `Bug`, `Sub-task`, `Initiative`

## Auth

Already configured. If auth expires:
```bash
echo "TOKEN" | acli jira auth login --site "redhat.atlassian.net" --email "aavraham@redhat.com" --token
acli jira auth status
```
