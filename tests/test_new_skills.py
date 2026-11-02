import pytest

from skill_checks import REPO, missing_refs, prose_violations, read_skill

# New skill name -> trigger phrases its description must contain.
NEW_SKILLS = {}


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
