"""Ubah docs/ba/us-ac.md menjadi us.tsv, ac.tsv, dan mrtm-<modul>.tsv untuk ditempel ke xlsx.

Pakai: python us_ac_to_tsv.py <path us-ac.md> [--out <folder>]
"""
import re
import sys
from pathlib import Path

US_HEAD = re.compile(r'^## (US-(\d{2,})): (.+?)\s*$')
AC_HEAD = re.compile(r'^### Acceptance Criteria (US-\d{2,})\s*$')
MRTM_HEAD = re.compile(r'^### MRTM (US-\d{2,})\s*$')
# Akhiran huruf mengikuti contoh pemecahan skenario di guide (AC-XX.01a, AC-XX.01b).
AC_ID = re.compile(r'^AC-(\d{2,})\.(\d{2,})([a-z])?$')
TCID = re.compile(r'^TRM_([A-Z0-9]+)_\d{3}$')
BR = re.compile(r'<br\s*/?>', re.I)
US_COLS = ['Persona', 'Aksi yang dilakukan', 'Hasil nilai bisnis']
AC_COLS = ['AC-ID', 'Skenario', 'GIVEN', 'WHEN', 'THEN', 'Status']
US_OUT = ['US-ID', 'Judul', 'Persona', 'Aksi yang dilakukan', 'Hasil nilai bisnis']
AC_OUT = ['AC-ID', 'US-ID', 'Skenario', 'GIVEN', 'WHEN', 'THEN', 'Status']
PIPE = '\x00'


class ParseError(Exception):
    def __init__(self, line, message):
        super().__init__(f'baris {line}: {message}')
        self.line = line


def cells(line):
    inner = line.strip().replace('\\|', PIPE)
    if inner.startswith('|'):
        inner = inner[1:]
    if inner.endswith('|'):
        inner = inner[:-1]
    return [BR.sub('\n', c.strip().replace(PIPE, '|')) for c in inner.split('|')]


def is_rule(row):
    return all(re.fullmatch(r':?-{3,}:?', c) for c in row)


def tables(lines):
    """Hasilkan (nomor baris heading terakhir, heading, [(nomor baris, sel)]) per tabel."""
    heading, heading_line, i = '', 0, 0
    while i < len(lines):
        line = lines[i]
        if line.startswith('#'):
            heading, heading_line = line.strip(), i + 1
        if line.lstrip().startswith('|'):
            rows = []
            while i < len(lines) and lines[i].lstrip().startswith('|'):
                rows.append((i + 1, cells(lines[i])))
                i += 1
            yield heading_line, heading, rows
            continue
        i += 1


def parse(text):
    lines = text.replace('\r\n', '\n').split('\n')
    us, ac, mrtm = [], [], {}
    us_heads, seen = {}, set()
    for n, line in enumerate(lines, 1):
        if line.startswith('## US-'):
            m = US_HEAD.match(line)
            if not m:
                raise ParseError(n, 'judul US harus berformat "## US-XX: <Judul>"')
            if m.group(1) in seen:
                raise ParseError(n, f'{m.group(1)} sudah dipakai')
            seen.add(m.group(1))
            us_heads[n] = (m.group(1), m.group(2), m.group(3))
    us_with_row = set()
    for head_line, heading, rows in tables(lines):
        last_us = max((k for k in us_heads if k <= head_line), default=None)
        current = us_heads[last_us] if last_us else None
        header = rows[0][1]
        body = [(n, r) for n, r in rows[1:] if not is_rule(r)]
        first_line = body[0][0] if body else rows[0][0]
        ac_head, mrtm_head = AC_HEAD.match(heading), MRTM_HEAD.match(heading)
        if heading.startswith('## US-'):
            if header != US_COLS:
                raise ParseError(rows[0][0], f'header tabel US harus {US_COLS}')
            if len(body) != 1:
                raise ParseError(first_line, f'{current[0]} harus punya tepat satu baris US')
            n, r = body[0]
            if len(r) != len(US_COLS):
                raise ParseError(n, f'jumlah kolom US {len(r)}, seharusnya {len(US_COLS)}')
            us.append([current[0], current[2]] + r)
            us_with_row.add(current[0])
        elif ac_head or mrtm_head:
            if current is None:
                raise ParseError(first_line, 'tabel di luar kelompok US (tidak ada judul "## US-XX: ..." di atasnya)')
            if (ac_head or mrtm_head).group(1) != current[0]:
                raise ParseError(head_line, f'judul "{heading}" berada di bawah {current[0]}')
            if ac_head:
                if header != AC_COLS:
                    raise ParseError(rows[0][0], f'header tabel AC harus {AC_COLS}')
                for n, r in body:
                    if len(r) != len(AC_COLS):
                        raise ParseError(n, f'jumlah kolom AC {len(r)}, seharusnya {len(AC_COLS)}')
                    m = AC_ID.match(r[0])
                    if not m:
                        raise ParseError(n, f'AC-ID "{r[0]}" harus berformat AC-XX.YY')
                    if m.group(1) != current[1]:
                        raise ParseError(n, f'{r[0]} tidak milik {current[0]}')
                    if r[0] in seen:
                        raise ParseError(n, f'{r[0]} sudah dipakai')
                    seen.add(r[0])
                    ac.append([r[0], current[0]] + r[1:])
            else:
                if 'Test Case ID' not in header:
                    raise ParseError(rows[0][0], 'header MRTM harus memuat kolom "Test Case ID"')
                col = header.index('Test Case ID')
                for n, r in body:
                    if len(r) != len(header):
                        raise ParseError(n, f'jumlah kolom MRTM {len(r)}, seharusnya {len(header)}')
                    m = TCID.match(r[col])
                    if not m:
                        raise ParseError(n, f'Test Case ID "{r[col]}" harus berformat TRM_MODUL_XXX')
                    table = mrtm.setdefault(m.group(1).lower(), [header])
                    if table[0] != header:
                        raise ParseError(rows[0][0], f'MRTM modul {m.group(1)} sudah memakai kolom lain; samakan kolomnya atau pakai modul berbeda')
                    table.append(r)
        elif header in (US_COLS, AC_COLS) or 'Test Case ID' in header:
            raise ParseError(head_line or rows[0][0], f'tabel US/AC/MRTM di bawah judul "{heading}" yang tidak dikenali')
    for n, (us_id, _, _) in us_heads.items():
        if us_id not in us_with_row:
            raise ParseError(n, f'{us_id} tidak punya tabel US (Persona, Aksi, Hasil nilai bisnis) tepat di bawah judulnya')
    return {'us': us, 'ac': ac, 'mrtm': mrtm}


def tsv_cell(value):
    if any(ch in value for ch in '\n\t"'):
        return '"' + value.replace('"', '""') + '"'
    return value


def to_tsv(rows):
    return ''.join('\t'.join(tsv_cell(c) for c in row) + '\r\n' for row in rows)


def convert(md_path, out_dir):
    doc = parse(Path(md_path).read_text(encoding='utf-8'))
    out = Path(out_dir)
    files = {'us.tsv': [US_OUT] + doc['us'], 'ac.tsv': [AC_OUT] + doc['ac']}
    for module, rows in doc['mrtm'].items():
        files[f'mrtm-{module}.tsv'] = rows
    written = []
    for name, rows in files.items():
        path = out / name
        path.write_text(to_tsv(rows), encoding='utf-8-sig', newline='')
        written.append(path)
    return written


def main(argv):
    args = list(argv)
    out = None
    if '--out' in args:
        i = args.index('--out')
        out = args[i + 1]
        del args[i:i + 2]
    if len(args) != 1:
        print('Pakai: python us_ac_to_tsv.py <path us-ac.md> [--out <folder>]', file=sys.stderr)
        return 2
    src = Path(args[0])
    try:
        written = convert(src, Path(out) if out else src.parent)
    except ParseError as e:
        print(f'{src.name} {e}', file=sys.stderr)
        return 1
    for path in written:
        print(f'ditulis: {path}')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
