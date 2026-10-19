---
name: "source-command-focus"
description: "Switch which repository/repositories to focus on. Re-presents the repo selection menu and completely replaces the previous selection."
---

# source-command-focus

Use this skill when the user asks to run the migrated source command `focus`.

## Command Template

# Focus Command

Switch repository focus mid-session.

## Instructions

### Step 1: Scan Available Repositories

Locate the workspace containing this command, not just the current Git root
(a project under `repositories/` has its own Git root). The scan below searches
upward from the working directory. If working elsewhere, set `WORKSPACE_ROOT`
to the absolute workspace path derived from this command or skill's location.
Do not guess a path or silently scan a different workspace.

```bash
workspace_root="${WORKSPACE_ROOT:-$PWD}"
while [ ! -f "$workspace_root/ai-workspace.toml" ] || [ ! -f "$workspace_root/commands/focus/command.md" ]; do
  if [ "$workspace_root" = / ]; then
    echo "Workspace not found. Set WORKSPACE_ROOT to the workspace containing this command." >&2
    exit 1
  fi
  workspace_root=$(dirname "$workspace_root")
done

i=0
for dir in "$workspace_root"/repositories/*/; do
  # Clones have a .git directory; submodules and worktrees have a .git file.
  if [ -e "$dir/.git" ] && git -C "$dir" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    i=$((i + 1))
    name=$(basename "$dir")
    branch=$(git -C "$dir" symbolic-ref --short -q HEAD 2>/dev/null || git -C "$dir" rev-parse --short HEAD 2>/dev/null || echo "unknown")
    status=$(git -C "$dir" status --porcelain 2>/dev/null)
    if [ -n "$status" ]; then
      count=$(echo "$status" | wc -l | tr -d ' ')
      hint="$branch, $count uncommitted"
    else
      hint="$branch, clean"
    fi
    printf "  %s. %-30s (%s)\n" "$i" "$name" "$hint"
  fi
done
if [ "$i" -eq 0 ]; then
  echo "No repositories found in $workspace_root/repositories/."
fi
```

### Step 2: Present the Menu

Show the numbered list:

```
REPOSITORY FOCUS
================
  1. my-project                   (main, clean)
  2. backend-api                  (feature/add-retry, 3 uncommitted)
  3. frontend-app                 (main, clean)

Which repo(s)? (e.g. 1, 1-3, all, all except 2)
```

If there is a current focus, mark it:

```
  2. backend-api                  (feature/add-retry, 3 uncommitted)  [current]
```

### Step 3: Apply Selection

The user's response **completely replaces** the previous focus. Parse their selection:

- `2` → single repo
- `1 3` → multiple repos by number
- `1-3` → range
- `all` → all repos
- `all except 2` → all minus specific ones
- Repo names also work: `backend-api`

### Step 4: Confirm

```
Focused on: backend-api, frontend-app
```

Then continue working. Apply the same focus constraint: only read/modify files in the selected repo(s) unless the user explicitly asks otherwise.

Focus is a scope instruction for the current conversation. It does not change
filesystem permissions, create a sandbox, or change the working directory of
later tool calls. Use the selected repositories' absolute paths explicitly.
Workspace command/skill metadata may be read to operate `/focus` itself.

### Step 5: Update tmux Window Name

If running inside tmux, rename the current window to reflect the focused repo(s):

```bash
# Only if inside a tmux session
if [ -n "$TMUX" ]; then
  # Single repo: use repo name
  # Multiple repos: "first-repo+N" where N is the count of additional repos
  tmux rename-window "WINDOW_NAME"
fi
```

Examples:
- 1 repo selected → `tmux rename-window "backend-api"`
- 3 repos selected → `tmux rename-window "backend-api+2"`

If not inside tmux, skip this step silently.

## Important

- This command **replaces** the current focus — it does not add to it
- Always scan the actual `repositories/` directory — never use a cached list
- If only one repo exists, auto-select it and confirm without asking
- If no repositories are found, report that and preserve the current focus
- Reject unknown names or out-of-range numbers without replacing the current focus
