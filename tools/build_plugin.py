"""Rakit my-ba-flow.plugin (zip) dari folder skill di repo.

Pakai: python tools/build_plugin.py [--out <path>]
"""
import sys
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SKILLS = ['ba-grooming', 'ba-handoff', 'ba-planning', 'change-request', 'data-dictionary', 'discovery-meeting-prep',
          'grill-with-docs',
          'impact-analysis', 'process-mapping', 'product-discovery', 'requirement-elicitation', 'reverse-engineering',
          'solution-evaluation', 'stakeholder-interview', 'stop-slop', 'us-ac-writer', 'wireframe-spec']
SKIP = {'__pycache__', '.pytest_cache'}


def build(out):
    names = []
    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
        for rel in ('README.md', '.claude-plugin/plugin.json'):
            z.write(REPO / rel, rel)
            names.append(rel)
        for skill in SKILLS:
            for path in sorted((REPO / skill).rglob('*')):
                if path.is_file() and not SKIP.intersection(path.parts):
                    name = f'skills/{skill}/' + path.relative_to(REPO / skill).as_posix()
                    z.write(path, name)
                    names.append(name)
    return names


def main(argv):
    out = Path(argv[argv.index('--out') + 1]) if '--out' in argv else REPO / 'my-ba-flow.plugin'
    names = build(out)
    print(f'{out.name}: {len(names)} file')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
