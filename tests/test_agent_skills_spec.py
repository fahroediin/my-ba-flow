"""Shipped skills follow the Agent Skills spec (agentskills.io) so Codex, Antigravity, Gemini CLI, Cursor and Copilot can load them."""
import re

import pytest

import build_plugin as B
import install_skills as I

SPEC_KEYS = {'name', 'description', 'license', 'compatibility', 'metadata', 'allowed-tools'}
NAME = re.compile(r'^[a-z0-9]+(-[a-z0-9]+)*$')


def frontmatter(skill):
    text = (B.REPO / skill / 'SKILL.md').read_text(encoding='utf-8').replace('\r\n', '\n')
    assert text.startswith('---\n'), skill
    head = text.split('\n---', 1)[0][4:]
    top = {}
    for line in head.splitlines():
        m = re.match(r'^([A-Za-z][\w-]*):\s*(.*)$', line)
        if m:
            top[m.group(1)] = m.group(2).strip().strip('"\'')
    return top


@pytest.mark.parametrize('skill', B.SKILLS)
def test_frontmatter_matches_spec(skill):
    fm = frontmatter(skill)
    assert set(fm) <= SPEC_KEYS, set(fm) - SPEC_KEYS
    assert fm.get('name') == skill
    assert 1 <= len(skill) <= 64 and NAME.match(skill)
    assert 1 <= len(fm.get('description', '')) <= 1024


@pytest.mark.parametrize('skill', B.SKILLS)
def test_no_claude_only_wording(skill):
    text = (B.REPO / skill / 'SKILL.md').read_text(encoding='utf-8')
    assert not re.search(r'\bClaude (cannot|can|will|must|should)\b', text)
    assert 'plugin my-ba-flow' not in text


def test_install_copies_every_skill(tmp_path):
    dest = I.target_dir('codex', 'project', project=tmp_path)
    assert dest == tmp_path / '.agents' / 'skills'
    I.install(dest)
    for skill in B.SKILLS:
        assert (dest / skill / 'SKILL.md').is_file(), skill
    assert not list(dest.rglob('__pycache__'))
    assert (dest / 'demo-terpandu-fgd' / 'assets' / 'demo-proxy.mjs').is_file()


def test_install_user_scope_paths(tmp_path):
    assert I.target_dir('antigravity', 'user', home=tmp_path) == tmp_path / '.gemini' / 'config' / 'skills'
    assert I.target_dir('copilot', 'project', project=tmp_path) == tmp_path / '.github' / 'skills'
    assert I.target_dir(custom=tmp_path / 'x') == tmp_path / 'x'


def test_install_dry_run_writes_nothing(tmp_path):
    I.install(tmp_path / 's', dry_run=True)
    assert not (tmp_path / 's').exists()
