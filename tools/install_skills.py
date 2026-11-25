"""Pasang skill my-ba-flow ke folder skill agent lain (format Agent Skills, agentskills.io).

Pakai:
  python tools/install_skills.py --agent codex                     # project: ./.agents/skills
  python tools/install_skills.py --agent antigravity --scope user  # ~/.gemini/config/skills
  python tools/install_skills.py --agent cursor --project D:/kerja/klien-a
  python tools/install_skills.py --dir D:/skills                   # folder bebas
  python tools/install_skills.py --agent copilot --dry-run         # tampilkan tujuan saja
  python tools/install_skills.py --list                            # daftar agent dan foldernya

Skill yang sudah ada di tujuan ditimpa per file; file lain di folder tujuan tidak dihapus.
"""
import argparse
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_plugin as B  # noqa: E402

# agent -> (folder project relatif ke root project, folder user relatif ke home)
AGENTS = {
    'claude-code': ('.claude/skills', '.claude/skills'),
    'codex': ('.agents/skills', '.agents/skills'),
    'antigravity': ('.agents/skills', '.gemini/config/skills'),
    'gemini-cli': ('.agents/skills', '.gemini/skills'),
    'cursor': ('.agents/skills', '.cursor/skills'),
    'copilot': ('.github/skills', '.copilot/skills'),
}
SKIP = set(B.SKIP)


def target_dir(agent=None, scope='project', project=None, custom=None, home=None):
    if custom:
        return Path(custom)
    if agent not in AGENTS:
        raise SystemExit(f'Agent tidak dikenal: {agent}. Pilihan: {", ".join(AGENTS)}')
    proj_rel, user_rel = AGENTS[agent]
    if scope == 'user':
        return Path(home or Path.home()) / user_rel
    return Path(project or Path.cwd()) / proj_rel


def install(dest, skills=None, dry_run=False):
    """Salin setiap skill ke dest/<skill>/. Kembalikan daftar skill yang dipasang."""
    skills = skills or B.SKILLS
    for skill in skills:
        src = B.REPO / skill
        if not (src / 'SKILL.md').is_file():
            raise SystemExit(f'SKILL.md tidak ditemukan: {src}')
        if dry_run:
            continue
        for path in sorted(src.rglob('*')):
            if path.is_file() and not SKIP.intersection(path.parts):
                out = dest / skill / path.relative_to(src)
                out.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(path, out)
    return list(skills)


def main(argv=None):
    ap = argparse.ArgumentParser(description='Pasang skill my-ba-flow ke agent yang mendukung SKILL.md.')
    ap.add_argument('--agent', choices=sorted(AGENTS))
    ap.add_argument('--scope', choices=('project', 'user'), default='project')
    ap.add_argument('--project', help='Root project tujuan (bawaan: folder saat ini)')
    ap.add_argument('--dir', help='Folder tujuan bebas; mengabaikan --agent dan --scope')
    ap.add_argument('--skill', action='append', help='Pasang skill tertentu saja (boleh berulang)')
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--list', action='store_true', help='Tampilkan agent dan foldernya')
    a = ap.parse_args(argv)
    if a.list:
        for name, (proj, user) in AGENTS.items():
            print(f'{name:12} project: {proj:16} user: ~/{user}')
        return 0
    if not a.agent and not a.dir:
        ap.error('isi --agent atau --dir')
    unknown = sorted(set(a.skill or []) - set(B.SKILLS))
    if unknown:
        ap.error('skill tidak dikenal: ' + ', '.join(unknown))
    dest = target_dir(a.agent, a.scope, a.project, a.dir)
    done = install(dest, a.skill, a.dry_run)
    verb = 'Akan dipasang' if a.dry_run else 'Terpasang'
    print(f'{verb} {len(done)} skill ke {dest}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
