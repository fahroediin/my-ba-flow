import json
import zipfile

import build_plugin as B

SKILLS = ['ba-grooming', 'ba-start', 'ba-handoff', 'ba-planning', 'change-request', 'data-dictionary', 'demo-terpandu-fgd',
          'discovery-meeting-prep', 'fit-gap',
          'grill-with-docs',
          'impact-analysis', 'meeting-live-assist', 'process-mapping', 'product-discovery', 'product-onboarding', 'requirement-elicitation', 'reverse-engineering',
          'solution-evaluation', 'stakeholder-interview', 'stop-slop', 'us-ac-writer', 'wireframe-spec']
DROPPED = ['caveman', 'grill-me', 'handoff']


def test_skill_list_has_one_skill_per_job():
    assert sorted(B.SKILLS) == sorted(SKILLS)


def test_dropped_skills_are_gone_from_repo_and_plugin(tmp_path):
    names = B.build(tmp_path / 'my-ba-flow.plugin')
    for skill in DROPPED:
        assert not (B.REPO / skill).exists(), skill
        assert not any(n.startswith(f'skills/{skill}/') for n in names), skill


def test_plugin_contains_us_ac_writer_files(tmp_path):
    out = tmp_path / 'my-ba-flow.plugin'
    names = B.build(out)
    for name in ('skills/us-ac-writer/SKILL.md', 'skills/us-ac-writer/references/sysfunc-us-ac-guide.md',
                 'skills/us-ac-writer/references/appendix-d-us-ac.md', 'skills/us-ac-writer/scripts/us_ac_to_tsv.py',
                 'skills/stop-slop/references/phrases.md',
                 'skills/discovery-meeting-prep/references/question-bank.md', 'README.md', '.claude-plugin/plugin.json',
                 'skills/ba-start/SKILL.md', 'skills/product-onboarding/references/output-templates.md',
                 'skills/fit-gap/SKILL.md', 'skills/meeting-live-assist/SKILL.md','skills/demo-terpandu-fgd/assets/demo-proxy.mjs',
                 'skills/demo-terpandu-fgd/scripts/import-questions.mjs'):
        assert name in names, name
    assert not any('__pycache__' in n or n.startswith('skills/skill-creator') for n in names)
    with zipfile.ZipFile(out) as z:
        assert json.loads(z.read('.claude-plugin/plugin.json'))['version'] == '1.5.0'


def test_readme_explains_two_work_models():
    text = (B.REPO / 'README.md').read_text(encoding='utf-8')
    assert '## Two work models' in text
    for skill in ('ba-start', 'product-onboarding', 'fit-gap', 'demo-terpandu-fgd'):
        assert f'`{skill}`' in text, skill
