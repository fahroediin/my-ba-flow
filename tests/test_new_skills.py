import re
import shutil
import subprocess

import pytest

from skill_checks import REPO, missing_refs, prose_violations, read_skill

# New skill name -> trigger phrases its description must contain.
NEW_SKILLS = {
    'ba-start': ['mulai', 'product based', 'project based', 'zip'],
    'demo-terpandu-fgd': ['panduan demo', 'FGD', 'prototype'],
    'product-onboarding': ['zip', 'rar', 'product based', 'aplikasi'],
    'fit-gap': ['fit-gap', 'calon klien', 'product based'],
    'meeting-live-assist': ['meeting sedang berjalan', 'potongan transkrip', 'Live Captions', 'replay'],
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


def test_fit_gap_statuses_and_handoff():
    _, body = read_skill('fit-gap')
    for s in ('Fit', 'Fit dengan konfigurasi', 'Gap kecil', 'Gap besar', 'Tidak dibutuhkan',
              'dikonfirmasi', 'dibantah', 'belum', 'fit-gap-<klien>.md', 'docs/ba/product-input/',
              'ba-planning', 'reverse-engineering', 'requirement-elicitation', 'P1-01', 'gap-analysis.md'):
        assert s in body, s


def test_fit_gap_requires_session_evidence():
    _, body = read_skill('fit-gap')
    assert 'no debrief' in body.lower() and 'discovery-meeting-prep' in body


def test_fit_gap_is_product_based_only():
    _, body = read_skill('fit-gap')
    assert 'project based' in body and 'ba-grooming' in body


def test_ba_start_routes_both_models():
    _, body = read_skill('ba-start')
    for s in ('AskUserQuestion', 'Pak Tan', 'product-onboarding', 'discovery-meeting-prep',
              'demo-terpandu-fgd', 'fit-gap', 'ba-planning', 'wireframe-spec', 'ba-grooming'):
        assert s in body, s
    assert 'does not write documents' in body


def test_ba_start_resumes_from_existing_docs():
    _, body = read_skill('ba-start')
    assert 'docs/ba/product/' in body and 'next step' in body and 'do not restart' in body.lower()


def test_discovery_has_product_demo_session():
    _, body = read_skill('discovery-meeting-prep')
    for s in ('Product demo to a prospect', 'product-brief.md', 'assumptions-to-confirm.md',
              'sessions/<klien>-<tanggal>/', 'meeting-prep.md', 'debrief.md', 'Module E'):
        assert s in body, s
    bank = (REPO / 'discovery-meeting-prep/references/question-bank.md').read_text(encoding='utf-8')
    assert '## Bagian E: Demo produk ke calon klien' in bank and '| E-01 |' in bank


def test_live_assist_chunk_format_matches_mom_template():
    _, body = read_skill('meeting-live-assist')
    for s in ('Tanyakan sekarang', 'Baru dibahas', 'Terjawab',
              '| No | Pertanyaan | Perlu Jawaban Dari | Deadline Jawaban |',
              '| No | Asumsi Logika Bisnis / Teknis | Konfirmasi Diperlukan Dari |',
              'T-04', 'Template_MoM.md'):
        assert s in body, s
    assert 'at most 3' in body


def test_live_assist_setup_close_and_replay():
    _, body = read_skill('meeting-live-assist')
    for s in ('meeting-prep', 'selesai', 'P2-01', 'P2-03', 'risk if wrong',
              'docs/ba/meeting-live-', 'Replay mode', 'Hollyland', 'NDA'):
        assert s in body, s
    assert 'never invent' in body.lower()


def test_discovery_points_to_live_assist():
    _, body = read_skill('discovery-meeting-prep')
    assert 'meeting-live-assist' in body


def test_reverse_engineering_accepts_product_input():
    head, body = read_skill('reverse-engineering')
    assert '## Input from product based' in body
    section = body.split('## Input from product based')[1].split('\n## ')[0]
    for s in ('High', 'Medium', 'Low', 'dibantah', 'fit-gap', 'gap-analysis.md'):
        assert s in section, s
    assert 'document what this app already does' not in head['description']


def test_product_discovery_does_not_claim_existing_apps():
    head, _ = read_skill('product-discovery')
    assert 'zip' not in head['description'].lower() and 'existing app' not in head['description'].lower()


def test_wireframe_spec_points_to_demo_guide():
    _, body = read_skill('wireframe-spec')
    assert 'demo-terpandu-fgd' in body.split('## Handoff')[1]


def _quoted_triggers(name):
    head, _ = read_skill(name)
    return [p.lower() for p in re.findall(r'"([^"]+)"', head['description'])]


def test_no_trigger_collisions_with_new_skills():
    names = ['ba-start', 'product-onboarding', 'fit-gap', 'demo-terpandu-fgd', 'product-discovery',
             'reverse-engineering', 'discovery-meeting-prep', 'meeting-live-assist']
    for a in names:
        for b in names:
            if a == b:
                continue
            for pa in _quoted_triggers(a):
                for pb in _quoted_triggers(b):
                    assert pa not in pb, (a, pa, b, pb)
    head, _ = read_skill('product-discovery')
    assert 'where to begin' not in head['description'] and 'from scratch' not in head['description']


def test_terbukti_and_asumsi_have_one_meaning():
    _, onboarding = read_skill('product-onboarding')
    _, start = read_skill('ba-start')
    for text in (onboarding, start):
        assert 'not confirmed by real users' not in text
    assert 'client status' in onboarding
    tmpl = (REPO / 'product-onboarding/references/output-templates.md').read_text(encoding='utf-8')
    section = tmpl.split('## assumptions-to-confirm.md')[1]
    assert '| Label |' in section or '| Label' in section


def test_ba_start_detects_position_before_asking():
    _, body = read_skill('ba-start')
    assert body.index('Find where the work stands') < body.index('Ask the model')
    assert 'one line per' in body and 'only when nothing' in body
