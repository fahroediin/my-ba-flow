"""Shipped skills must match BA Handbook v2.1 (codes, templates, phase names)."""
import re

import build_plugin as B

OBSOLETE_TEMPLATES = re.compile(r'\bT-(01|02|03|10|13|15|17|20)\b')


def shipped_texts():
    paths = [B.REPO / 'README.md', B.REPO / '.claude-plugin' / 'plugin.json']
    for skill in B.SKILLS:
        paths += sorted((B.REPO / skill).rglob('*.md'))
    return {p.relative_to(B.REPO).as_posix(): p.read_text(encoding='utf-8') for p in paths}


def test_no_obsolete_template_codes():
    hits = {k: OBSOLETE_TEMPLATES.findall(t) for k, t in shipped_texts().items()}
    assert {k: v for k, v in hits.items() if v} == {}


def test_handbook_version_and_dead_url_gone():
    for name, text in shipped_texts().items():
        assert 'v1.13' not in text, name
        assert 'vercel.app' not in text, name


def test_phase_4_is_verification_and_validation():
    for name, text in shipped_texts().items():
        assert 'Design & Validation' not in text, name
    grooming = (B.REPO / 'ba-grooming' / 'SKILL.md').read_text(encoding='utf-8')
    assert 'Verification Checklist' in grooming and 'Validation Checklist' in grooming
    for item in ('Necessary', 'Singular', 'Unambiguous', 'Complete', 'Consistent', 'Feasible', 'Verifiable',
                 'Traceable', 'Prioritized'):
        assert f'**{item}**' in grooming, item


def test_reverse_engineering_uses_rv_codes_and_split_data_techniques():
    text = (B.REPO / 'reverse-engineering' / 'SKILL.md').read_text(encoding='utf-8')
    assert re.findall(r'\bRE-0\d', text) == []
    assert all(f'RV-0{n}' in text for n in range(1, 9))
    assert 'Data Modelling' in text and 'Data Mining' in text and 'Data Mining / Analysis' not in text


def test_requirement_classification_credits_babok():
    text = (B.REPO / 'requirement-elicitation' / 'SKILL.md').read_text(encoding='utf-8')
    assert 'ISO/IEC 29148 level' not in text
    assert 'BABOK v3 §2.3' in text
    assert 'confidentiality, integrity, non-repudiation, accountability, authenticity' in text


def test_change_request_approver_is_pm_and_sponsor():
    for skill in ('change-request', 'ba-handoff'):
        text = (B.REPO / skill / 'SKILL.md').read_text(encoding='utf-8')
        assert 'PM + Sponsor (Change Control Board)' in text, skill
        assert 'Change Advisory Board' not in text, skill
