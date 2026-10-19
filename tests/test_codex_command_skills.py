"""Codex's invocation policy and local discovery for migrated commands."""

from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).parent.parent
COMMAND_SKILLS = ("repo-sync", "diff-explain", "changelog", "recap", "env-check", "prompt-test")


@pytest.mark.parametrize("name", COMMAND_SKILLS)
def test_command_skill_is_discoverable_and_explicit_only(name):
    source = ROOT / "skills" / name
    metadata = yaml.safe_load((source / "agents/openai.yaml").read_text())
    assert metadata["policy"]["allow_implicit_invocation"] is False
    discovered = ROOT / ".agents/skills" / name
    assert discovered.is_symlink()
    assert (discovered / "SKILL.md").samefile(source / "SKILL.md")
