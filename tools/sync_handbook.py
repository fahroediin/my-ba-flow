"""Jaga salinan aturan di skill tetap sama dengan file di BA Handbook.

Pakai:
  python tools/sync_handbook.py            cek; exit 1 bila ada yang berbeda
  python tools/sync_handbook.py --update   salin versi handbook ke skill
Folder handbook: variabel BA_HANDBOOK_DIR, default DEFAULT_HANDBOOK.
"""
import difflib
import os
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DEFAULT_HANDBOOK = r'C:\Users\User\OneDrive\Documents\Work\ba-handbook'
PAIRS = [
    ('Template/SysFunc_US_AC_Guide.md', 'us-ac-writer/references/sysfunc-us-ac-guide.md'),
    ('Appendix_D_Panduan_Praktik_US_AC.md', 'us-ac-writer/references/appendix-d-us-ac.md'),
]


def handbook_dir():
    return Path(os.environ.get('BA_HANDBOOK_DIR', DEFAULT_HANDBOOK))


def text(path):
    return path.read_bytes().decode('utf-8').replace('\r\n', '\n')


def differences(hb, repo):
    out = []
    for src, dst in PAIRS:
        target = repo / dst
        if not target.exists() or text(hb / src) != text(target):
            out.append(dst)
    return out


def update(hb, repo):
    changed = differences(hb, repo)
    for src, dst in PAIRS:
        if dst in changed:
            (repo / dst).parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(hb / src, repo / dst)
    return changed


def main(argv):
    hb = handbook_dir()
    if not hb.is_dir():
        print(f'Folder handbook tidak ditemukan: {hb}. Setel BA_HANDBOOK_DIR.', file=sys.stderr)
        return 2
    if '--update' in argv:
        changed = update(hb, REPO)
        print('diperbarui: ' + ', '.join(changed) if changed else 'sinkron')
        return 0
    changed = differences(hb, REPO)
    if not changed:
        print('sinkron')
        return 0
    for src, dst in PAIRS:
        if dst in changed:
            old = text(REPO / dst).splitlines() if (REPO / dst).exists() else []
            diff = list(difflib.unified_diff(old, text(hb / src).splitlines(), dst, src, lineterm='', n=1))
            print('\n'.join(diff[:40]) or f'{dst}: belum ada')
    return 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
