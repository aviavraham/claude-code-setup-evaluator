"""Exercise the actual repository-discovery example shipped in /focus."""

import os
import re
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent
COMMAND = ROOT / "commands/focus/command.md"


@pytest.fixture
def workspace(tmp_path):
    root = tmp_path / "workspace with spaces"
    (root / "commands/focus").mkdir(parents=True)
    (root / "commands/focus/command.md").write_text(COMMAND.read_text())
    (root / "ai-workspace.toml").touch()
    (root / "repositories").mkdir()
    return root


def git(*args):
    return subprocess.run(["git", *map(str, args)], check=True, capture_output=True, text=True)


def scan(cwd, **env):
    script = re.search(r"```bash\n(.*?)```", COMMAND.read_text(), re.DOTALL).group(1)
    environ = dict(os.environ)
    environ.pop("WORKSPACE_ROOT", None)
    environ.pop("i", None)
    environ.update(env)
    return subprocess.run(["bash", "-c", script], cwd=cwd, env=environ, capture_output=True, text=True)


def test_numbers_repositories_and_reports_dirty_state(workspace):
    for name in ("alpha", "beta"):
        git("init", "-q", "-b", "main", workspace / "repositories" / name)
    (workspace / "repositories/beta/new.txt").touch()
    result = scan(workspace)
    assert result.returncode == 0, result.stderr
    assert re.search(r"1\.\s+alpha\s+\(main, clean\)", result.stdout)
    assert re.search(r"2\.\s+beta\s+\(main, 1 uncommitted\)", result.stdout)


def test_discovers_from_inside_a_nested_repository(workspace):
    repo = workspace / "repositories/alpha"
    git("init", "-q", "-b", "main", repo)
    nested = repo / "src/package"
    nested.mkdir(parents=True)
    result = scan(nested)
    assert result.returncode == 0, result.stderr
    assert "alpha" in result.stdout


def test_includes_gitfile_worktrees(workspace, tmp_path):
    origin = tmp_path / "origin"
    git("init", "-q", "-b", "main", origin)
    git(
        "-C",
        origin,
        "-c",
        "user.name=Test",
        "-c",
        "user.email=test@example.com",
        "commit",
        "--allow-empty",
        "-qm",
        "initial",
    )
    git("-C", origin, "worktree", "add", "-qb", "feature", workspace / "repositories/linked")
    result = scan(workspace)
    assert result.returncode == 0, result.stderr
    assert re.search(r"1\.\s+linked\s+\(feature, clean\)", result.stdout)


def test_explicit_workspace_from_unrelated_directory(workspace, tmp_path):
    git("init", "-q", "-b", "main", workspace / "repositories/alpha")
    result = scan(tmp_path, WORKSPACE_ROOT=str(workspace))
    assert result.returncode == 0, result.stderr
    assert "alpha" in result.stdout


def test_empty_workspace_reports_no_repositories(workspace):
    result = scan(workspace)
    assert result.returncode == 0, result.stderr
    assert "No repositories found" in result.stdout
