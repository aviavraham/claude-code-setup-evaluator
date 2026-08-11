#!/usr/bin/env bash
# PreToolUse hook: block edits on default branch and ask user to decide.
# Extracts the file path from CLAUDE_TOOL_INPUT, checks if it's inside
# repositories/, and blocks if that repo is on main/master.

FILE=$(echo "$CLAUDE_TOOL_INPUT" | grep -oP '"file_path"\s*:\s*"\K[^"]+' 2>/dev/null)
[ -z "$FILE" ] && exit 0

# Only care about files under repositories/
echo "$FILE" | grep -q "repositories/" || exit 0

# Extract the repo directory (repositories/<name>)
REPO_DIR=$(echo "$FILE" | grep -oP 'repositories/[^/]+')
[ -z "$REPO_DIR" ] && exit 0
[ -d "$REPO_DIR/.git" ] || exit 0

BRANCH=$(git -C "$REPO_DIR" rev-parse --abbrev-ref HEAD 2>/dev/null)
[ -z "$BRANCH" ] && exit 0

if [ "$BRANCH" = "main" ] || [ "$BRANCH" = "master" ]; then
  echo "BLOCKED: $REPO_DIR is on '$BRANCH'."
  echo "Ask the user whether to continue on '$BRANCH' or create a new feature branch."
  echo "  To create a branch: git -C $REPO_DIR checkout -b <branch-name>"
  exit 2
fi

exit 0
