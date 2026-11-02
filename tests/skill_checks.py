"""Shared text checks for SKILL.md files: frontmatter, referenced files, and the repo's writing rules."""
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
EMOJI = re.compile('[\U0001F300-\U0001FAFF☀-➿⬜⭐]')
FENCE = re.compile(r'^(```|~~~).*?^\1[^\n]*$', re.M | re.S)
INLINE = re.compile(r'`[^`\n]*`')
RULE_LINE = re.compile(r'^\s*\|?[\s:|-]*-{3,}[\s:|-]*\|?\s*$')
REF = re.compile(r'`[^`\n]*?\b((?:references|scripts|assets)/[\w.-]+(?:/[\w.-]+)*)')


def read_skill(name):
    """Return ({'name', 'description'}, body) for <repo>/<name>/SKILL.md; body excludes the frontmatter."""
    text = (REPO / name / 'SKILL.md').read_text(encoding='utf-8')
    _, head, body = text.split('---', 2)
    fields = {}
    for key in ('name', 'description'):
        m = re.search(rf'^{key}:\s*(.+)$', head, re.M)
        fields[key] = m.group(1).strip().strip('"\'') if m else ''
    return fields, body


def prose_violations(text):
    """Emoji, em dashes and '--' in prose; fenced code, inline code and table/rule lines are exempt."""
    prose = INLINE.sub('', FENCE.sub('', text))
    found = []
    for line in prose.splitlines():
        if RULE_LINE.match(line):
            continue
        if '—' in line or '--' in line or EMOJI.search(line):
            found.append(line.strip())
    return found


def missing_refs(name):
    """references/, scripts/ and assets/ paths named in backticks in SKILL.md that do not exist in the skill folder."""
    text = (REPO / name / 'SKILL.md').read_text(encoding='utf-8')
    return sorted({p for p in REF.findall(text) if not (REPO / name / p).exists()})
