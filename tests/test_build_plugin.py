import json
import zipfile

import build_plugin as B

OLD_SKILLS = ['ba-grooming', 'ba-handoff', 'ba-planning', 'caveman', 'change-request', 'data-dictionary', 'grill-me',
              'grill-with-docs', 'handoff', 'impact-analysis', 'process-mapping', 'product-discovery',
              'requirement-elicitation', 'reverse-engineering', 'solution-evaluation', 'stakeholder-interview',
              'stop-slop', 'wireframe-spec']


def test_skill_list_keeps_existing_and_adds_us_ac_writer():
    assert sorted(B.SKILLS) == sorted(OLD_SKILLS + ['us-ac-writer'])


def test_plugin_contains_us_ac_writer_files(tmp_path):
    out = tmp_path / 'my-ba-flow.plugin'
    names = B.build(out)
    for name in ('skills/us-ac-writer/SKILL.md', 'skills/us-ac-writer/references/sysfunc-us-ac-guide.md',
                 'skills/us-ac-writer/references/appendix-d-us-ac.md', 'skills/us-ac-writer/scripts/us_ac_to_tsv.py',
                 'skills/stop-slop/references/phrases.md', 'README.md', '.claude-plugin/plugin.json'):
        assert name in names, name
    assert not any('__pycache__' in n or n.startswith('skills/skill-creator') for n in names)
    with zipfile.ZipFile(out) as z:
        assert json.loads(z.read('.claude-plugin/plugin.json'))['version'] == '1.2.0'
