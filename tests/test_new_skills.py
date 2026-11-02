import shutil
import subprocess

import pytest

from skill_checks import REPO, missing_refs, prose_violations, read_skill

# New skill name -> trigger phrases its description must contain.
NEW_SKILLS = {
    'demo-terpandu-fgd': ['panduan demo', 'FGD', 'prototype'],
    'product-onboarding': ['zip', 'rar', 'product based', 'aplikasi'],
}


def test_prose_violations_flags_dash_and_emoji_outside_code():
    assert prose_violations('a — b') and prose_violations('x -- y') and prose_violations('ok \U0001F600')
    assert prose_violations('`--format` and\n```\nnode a.mjs --x\n```') == []


@pytest.mark.parametrize('name', sorted(NEW_SKILLS))
def test_frontmatter_and_triggers(name):
    head, _ = read_skill(name)
    assert head['name'] == name
    assert len(head['description']) <= 1024
    for phrase in NEW_SKILLS[name]:
        assert phrase.lower() in head['description'].lower(), phrase


@pytest.mark.parametrize('name', sorted(NEW_SKILLS))
def test_refs_exist(name):
    assert missing_refs(name) == []


@pytest.mark.parametrize('name', sorted(NEW_SKILLS))
def test_prose_rules(name):
    _, body = read_skill(name)
    assert prose_violations(body) == []
    for ref in sorted((REPO / name / 'references').glob('*.md')):
        assert prose_violations(ref.read_text(encoding='utf-8')) == [], ref.name


def test_demo_skill_covers_both_models():
    _, body = read_skill('demo-terpandu-fgd')
    for s in ('product based', 'project based', 'docs/ba/product/', '/sessions/', 'docs/ba/demo-sessions/', 'Figma'):
        assert s in body, s


def test_demo_assets_parse_with_node():
    if not shutil.which('node'):
        pytest.skip('node not installed')
    for f in ('assets/demo-proxy.mjs', 'assets/presenter-panel.js', 'scripts/build-script.mjs', 'scripts/import-questions.mjs'):
        assert subprocess.run(['node', '--check', str(REPO / 'demo-terpandu-fgd' / f)]).returncode == 0, f


def test_product_onboarding_outputs_and_labels():
    _, body = read_skill('product-onboarding')
    for s in ('product-brief.md', 'feature-inventory.md', 'business-rules-found.md',
              'assumptions-to-confirm.md', 'demo-traps.md', 'docs/ba/product/', 'Terbukti', 'Asumsi',
              'tar -xf', '7z x', 'references/output-templates.md'):
        assert s in body, s


def test_product_onboarding_handles_extract_failure():
    _, body = read_skill('product-onboarding')
    assert 'password' in body.lower() and 'extract it themselves' in body


def test_product_onboarding_handles_app_not_running():
    _, body = read_skill('product-onboarding')
    assert 'Tidak dijalankan:' in body


def test_product_onboarding_versions_do_not_overwrite():
    _, body = read_skill('product-onboarding')
    assert 'never overwrite' in body and 'what changed' in body


def test_product_onboarding_is_not_bab_4a():
    _, body = read_skill('product-onboarding')
    assert 'RE Scope Statement' in body and 'reverse-engineering' in body
