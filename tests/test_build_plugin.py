import json
import zipfile

import build_plugin as B

SKILLS = ['ba-grooming', 'ba-handoff', 'ba-planning', 'change-request', 'data-dictionary', 'discovery-meeting-prep',
          'grill-with-docs',
          'impact-analysis', 'process-mapping', 'product-discovery', 'requirement-elicitation', 'reverse-engineering',
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
                 'skills/discovery-meeting-prep/references/question-bank.md', 'README.md', '.claude-plugin/plugin.json'):
        assert name in names, name
    assert not any('__pycache__' in n or n.startswith('skills/skill-creator') for n in names)
    with zipfile.ZipFile(out) as z:
        assert json.loads(z.read('.claude-plugin/plugin.json'))['version'] == '1.3.0'
