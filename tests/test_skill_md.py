import re
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1] / 'us-ac-writer' / 'SKILL.md'
EMOJI = re.compile('[\U0001F300-\U0001FAFF☀-➿⬜⭐]')


def body():
    return SKILL.read_text(encoding='utf-8')


def test_frontmatter_names_skill_and_triggers():
    text = body()
    head = text.split('---')[1]
    assert re.search(r'^name: us-ac-writer$', head, re.M)
    desc = re.search(r'^description: (.+)$', head, re.M).group(1)
    for phrase in ('user story', 'acceptance criteria', 'Given/When/Then', 'MRTM', 'US AC'):
        assert phrase.lower() in desc.lower(), phrase


def test_skill_points_at_files_that_exist():
    text = body()
    for rel in re.findall(r'`((?:references|scripts)/[\w./-]+)`', text):
        assert (SKILL.parent / rel).exists(), rel
    assert 'references/sysfunc-us-ac-guide.md' in text and 'references/appendix-d-us-ac.md' in text
    assert 'scripts/us_ac_to_tsv.py' in text


def test_output_format_matches_converter():
    text = body()
    assert '## US-XX: <Judul>' in text
    assert '| AC-ID | Skenario | GIVEN | WHEN | THEN | Status |' in text
    assert '### Acceptance Criteria US-XX' in text and '### MRTM US-XX' in text


def test_no_emoji_and_no_em_dash():
    text = body()
    assert EMOJI.findall(text) == []
    assert '—' not in text
