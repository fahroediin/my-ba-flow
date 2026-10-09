# Skill us-ac-writer Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Skill `us-ac-writer` di `my-ba-flow` yang menulis User Story dan Acceptance Criteria mengikuti `SysFunc_US_AC_Guide` handbook, dengan keluaran per US di `docs/ba/us-ac.md` dan TSV siap tempel ke xlsx.

**Architecture:** Aturan disalin utuh ke `us-ac-writer/references/` dan dijaga sama dengan handbook oleh `tools/sync_handbook.py`. `SKILL.md` memuat alur, format, dan checklist; LLM menulis `us-ac.md`, lalu `scripts/us_ac_to_tsv.py` (stdlib) mengubahnya menjadi `us.tsv`, `ac.tsv`, `mrtm-<modul>.tsv`. `tools/build_plugin.py` merakit `my-ba-flow.plugin` versi 1.2.0.

**Tech Stack:** Python 3 (stdlib), pytest, Markdown.

**Spec:** `docs/superpowers/specs/2026-10-09-us-ac-writer-design.md`

## Global Constraints

- Skrip hanya memakai pustaka standar Python.
- TSV: UTF-8 dengan BOM, pemisah tab, baris CRLF; sel yang memuat baris baru, tab, atau `"` dibungkus `"` dengan `"` di dalamnya digandakan; `<br>`, `<br/>`, `<br />` menjadi baris baru (LF) di dalam sel.
- Kolom `us.tsv`: `US-ID, Judul, Persona, Aksi yang dilakukan, Hasil nilai bisnis`. Kolom `ac.tsv`: `AC-ID, US-ID, Skenario, GIVEN, WHEN, THEN, Status`.
- ID: `US-XX`, `AC-XX.YY` (XX = nomor US-nya), `TRM_[MODUL]_XXX`.
- Status AC baru `Draft`.
- Judul kelompok US di `us-ac.md`: `## US-XX: <Judul>` (titik dua; konvensi repo melarang em-dash di prosa).
- Keluaran skill tanpa emoji; salinan di `references/` tetap byte-per-byte (boleh berisi emoji).
- Folder handbook: `BA_HANDBOOK_DIR`, default `C:\Users\User\OneDrive\Documents\Work\ba-handbook`.
- Plugin `.claude-plugin/plugin.json` versi `1.2.0`; isi plugin = 18 skill yang sekarang ada di zip + `us-ac-writer` (19 skill).
- Commit kecil per task; pesan commit dalam bahasa Inggris, imperatif.

## Review Focus

1. Teks sel yang memuat `|` literal (ditulis `\|` di Markdown) harus tetap utuh di TSV → `test_escaped_pipe_stays_in_cell` (Task 1).
2. AC untuk US-07 yang tertulis di bawah judul US-06 harus ditolak, bukan diam-diam salah kelompok → `test_ac_number_must_match_its_us` (Task 1).
3. MRTM dari dua modul dalam satu dokumen harus menjadi dua file → `test_mrtm_split_per_module` (Task 1).
4. Salinan aturan yang hanya berbeda CRLF/LF tidak boleh dilaporkan berbeda → `test_crlf_difference_is_ignored` (Task 2).
5. Plugin hasil build harus memuat `references/` dan `scripts/` skill baru, bukan hanya `SKILL.md` → `test_plugin_contains_us_ac_writer_files` (Task 4).

---

## File Structure

| File | Tanggung jawab | Task |
|---|---|---|
| `us-ac-writer/scripts/us_ac_to_tsv.py` | Parse `us-ac.md` → TSV | 1 |
| `tests/conftest.py` | Path import untuk skrip | 1 |
| `tests/test_us_ac_to_tsv.py` | Test konverter | 1 |
| `tools/sync_handbook.py` | Cek/perbarui salinan aturan | 2 |
| `us-ac-writer/references/sysfunc-us-ac-guide.md` | Salinan guide | 2 |
| `us-ac-writer/references/appendix-d-us-ac.md` | Salinan Lampiran D | 2 |
| `tests/test_handbook_sync.py` | Test sinkron | 2 |
| `us-ac-writer/SKILL.md` | Instruksi skill | 3 |
| `tests/test_skill_md.py` | Test struktur SKILL.md | 3 |
| `README.md`, `product-discovery/SKILL.md`, `ba-grooming/SKILL.md` | Integrasi | 4 |
| `.claude-plugin/plugin.json`, `tools/build_plugin.py`, `my-ba-flow.plugin` | Plugin | 4 |
| `tests/test_build_plugin.py` | Test build | 4 |

---

### Task 1: Konverter us-ac.md ke TSV

**Files:**
- Create: `us-ac-writer/scripts/us_ac_to_tsv.py`, `tests/conftest.py`, `tests/test_us_ac_to_tsv.py`

**Interfaces:**
- Produces: modul `us_ac_to_tsv` dengan `class ParseError(Exception)` (atribut `line: int`), `parse(text: str) -> dict` berkunci `us: list[list[str]]`, `ac: list[list[str]]`, `mrtm: dict[str, list[list[str]]]` (kunci = modul huruf kecil; baris pertama = header), `to_tsv(rows: list[list[str]]) -> str`, `convert(md_path: Path, out_dir: Path) -> list[Path]`, `main(argv: list[str]) -> int`.

- [ ] **Step 1: Tulis test yang gagal**

`tests/conftest.py`:

```python
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for sub in (os.path.join('us-ac-writer', 'scripts'), 'tools'):
    path = os.path.join(ROOT, sub)
    if path not in sys.path:
        sys.path.insert(0, path)
```

`tests/test_us_ac_to_tsv.py`:

```python
import csv
import io

import pytest

import us_ac_to_tsv as T

DOC = '''# User Story dan Acceptance Criteria

## US-06: Menambahkan Sertifikat Talent

| Persona | Aksi yang dilakukan | Hasil nilai bisnis |
|---|---|---|
| Manager | menambahkan data sertifikat baru ke profil talent | data kualifikasi talent selalu lengkap dan terbaru |

### Acceptance Criteria US-06

| AC-ID | Skenario | GIVEN | WHEN | THEN | Status |
|---|---|---|---|---|---|
| AC-06.01 | Happy: Menambahkan sertifikat dengan data valid | Saya seorang Manager<br>AND saya berada di halaman "Detail Talent" | Saya mengklik tombol "Tambah Sertifikat"<br/>AND saya menekan tombol "Simpan" | Sistem menampilkan notifikasi "Certificate added"<br />AND kartu baru muncul | Draft |
| AC-06.02 | Negative: Menyimpan tanpa nama | Saya seorang Manager | Saya menekan tombol "Simpan" | Field menampilkan teks "Name A \\| B is required" | Draft |

## US-07: Mengecek Kelayakan Order

| Persona | Aksi yang dilakukan | Hasil nilai bisnis |
|---|---|---|
| Customer | membuka halaman order | order hanya dibuat oleh pelanggan yang memenuhi syarat |

### Acceptance Criteria US-07

| AC-ID | Skenario | GIVEN | WHEN | THEN | Status |
|---|---|---|---|---|---|
| AC-07.01 | Happy: Kelayakan order sesuai matriks | Saya seorang Customer | Saya membuka halaman "Order" | Refer to MRTM Rows: TRM_ORD_001 through TRM_ORD_002 | Draft |

### MRTM US-07

| User Story ID | Acceptance Criteria ID | User | Test Case ID | Status User | Lokasi | Kondisi Khusus | HASIL (EXPECTED RESULT) |
|---|---|---|---|---|---|---|---|
| US_07 | AC_01 | Customer | TRM_ORD_001 | Aktif | Jakarta | [-] | Tombol Order aktif |
| US_07 | AC_01 | Customer | TRM_ORD_002 | Pasif | [ANY] | [-] | Tombol Order disembunyikan |
'''


def read_tsv(text):
    return list(csv.reader(io.StringIO(text, newline=''), delimiter='\t'))


def test_parse_groups_us_and_ac():
    d = T.parse(DOC)
    assert d['us'] == [
        ['US-06', 'Menambahkan Sertifikat Talent', 'Manager', 'menambahkan data sertifikat baru ke profil talent', 'data kualifikasi talent selalu lengkap dan terbaru'],
        ['US-07', 'Mengecek Kelayakan Order', 'Customer', 'membuka halaman order', 'order hanya dibuat oleh pelanggan yang memenuhi syarat'],
    ]
    assert [r[:2] for r in d['ac']] == [['AC-06.01', 'US-06'], ['AC-06.02', 'US-06'], ['AC-07.01', 'US-07']]
    assert all(r[6] == 'Draft' for r in d['ac'])


def test_br_variants_become_newlines_inside_one_cell():
    rows = read_tsv(T.to_tsv(T.parse(DOC)['ac']))
    assert rows[0][3] == 'Saya seorang Manager\nAND saya berada di halaman "Detail Talent"'
    assert rows[0][4] == 'Saya mengklik tombol "Tambah Sertifikat"\nAND saya menekan tombol "Simpan"'
    assert rows[0][5] == 'Sistem menampilkan notifikasi "Certificate added"\nAND kartu baru muncul'
    assert len(rows) == 3 and all(len(r) == 7 for r in rows)


def test_quotes_are_doubled_and_rows_end_with_crlf():
    text = T.to_tsv([['a', 'say "hi"'], ['b', 'plain']])
    assert text == 'a\t"say ""hi"""\r\nb\tplain\r\n'


def test_escaped_pipe_stays_in_cell():
    rows = T.parse(DOC)['ac']
    assert rows[1][5] == 'Field menampilkan teks "Name A | B is required"'


def test_mrtm_split_per_module():
    doc = DOC + '''
## US-08: Menghitung Diskon

| Persona | Aksi yang dilakukan | Hasil nilai bisnis |
|---|---|---|
| Customer | memasukkan kode promo | harga akhir sesuai aturan promo |

### Acceptance Criteria US-08

| AC-ID | Skenario | GIVEN | WHEN | THEN | Status |
|---|---|---|---|---|---|
| AC-08.01 | Happy: Diskon sesuai matriks | Saya seorang Customer | Saya mengetik kode promo | Refer to MRTM Rows: TRM_PRM_001 through TRM_PRM_001 | Draft |

### MRTM US-08

| User Story ID | Acceptance Criteria ID | User | Test Case ID | Kode | HASIL (EXPECTED RESULT) |
|---|---|---|---|---|---|
| US_08 | AC_01 | Customer | TRM_PRM_001 | HEMAT10 | Diskon 10% |
'''
    m = T.parse(doc)['mrtm']
    assert sorted(m) == ['ord', 'prm']
    assert m['ord'][0][3] == 'Test Case ID' and len(m['ord']) == 3
    assert len(m['prm']) == 2


def test_convert_writes_bom_files(tmp_path):
    src = tmp_path / 'us-ac.md'
    src.write_text(DOC, encoding='utf-8')
    written = T.convert(src, tmp_path)
    assert sorted(p.name for p in written) == ['ac.tsv', 'mrtm-ord.tsv', 'us.tsv']
    raw = (tmp_path / 'ac.tsv').read_bytes()
    assert raw.startswith(b'\xef\xbb\xbf')
    header = read_tsv(raw.decode('utf-8-sig'))[0]
    assert header == ['AC-ID', 'US-ID', 'Skenario', 'GIVEN', 'WHEN', 'THEN', 'Status']
    assert read_tsv((tmp_path / 'us.tsv').read_bytes().decode('utf-8-sig'))[0] == ['US-ID', 'Judul', 'Persona', 'Aksi yang dilakukan', 'Hasil nilai bisnis']


def test_ac_table_without_us_heading_fails_with_line():
    bad = '### Acceptance Criteria US-01\n\n| AC-ID | Skenario | GIVEN | WHEN | THEN | Status |\n|---|---|---|---|---|---|\n| AC-01.01 | x | g | w | t | Draft |\n'
    with pytest.raises(T.ParseError) as e:
        T.parse(bad)
    assert e.value.line == 5


def test_ac_number_must_match_its_us():
    bad = DOC.replace('| AC-06.02 |', '| AC-07.09 |')
    with pytest.raises(T.ParseError, match='AC-07.09'):
        T.parse(bad)


def test_wrong_column_count_fails():
    bad = DOC.replace('| Draft |\n| AC-06.02', '|\n| AC-06.02', 1)
    with pytest.raises(T.ParseError, match='kolom'):
        T.parse(bad)


def test_main_reports_error_and_exit_code(tmp_path, capsys):
    src = tmp_path / 'us-ac.md'
    src.write_text(DOC.replace('| AC-06.02 |', '| AC-6.2 |'), encoding='utf-8')
    assert T.main([str(src)]) == 1
    assert 'baris' in capsys.readouterr().err
    assert not (tmp_path / 'ac.tsv').exists()
```

- [ ] **Step 2: Jalankan, pastikan gagal**

Run: `python -m pytest tests -q`
Expected: FAIL, `ModuleNotFoundError: No module named 'us_ac_to_tsv'`

- [ ] **Step 3: Implementasi** `us-ac-writer/scripts/us_ac_to_tsv.py`

```python
"""Ubah docs/ba/us-ac.md menjadi us.tsv, ac.tsv, dan mrtm-<modul>.tsv untuk ditempel ke xlsx.

Pakai: python us_ac_to_tsv.py <path us-ac.md> [--out <folder>]
"""
import re
import sys
from pathlib import Path

US_HEAD = re.compile(r'^## (US-(\d{2,})): (.+?)\s*$')
AC_HEAD = re.compile(r'^### Acceptance Criteria (US-\d{2,})\s*$')
MRTM_HEAD = re.compile(r'^### MRTM (US-\d{2,})\s*$')
AC_ID = re.compile(r'^AC-(\d{2,})\.(\d{2,})$')
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
    current = None  # (US-ID, nomor US, judul)
    us_heads = {}
    for n, line in enumerate(lines, 1):
        m = US_HEAD.match(line)
        if m:
            us_heads[n] = (m.group(1), m.group(2), m.group(3))
    for head_line, heading, rows in tables(lines):
        last_us = max((k for k in us_heads if k <= head_line), default=None)
        current = us_heads[last_us] if last_us else None
        header = rows[0][1]
        body = [(n, r) for n, r in rows[1:] if not is_rule(r)]
        first_line = body[0][0] if body else rows[0][0]
        if heading.startswith('## US-'):
            if header != US_COLS:
                raise ParseError(rows[0][0], f'header tabel US harus {US_COLS}')
            if len(body) != 1:
                raise ParseError(first_line, f'{current[0]} harus punya tepat satu baris US')
            n, r = body[0]
            if len(r) != len(US_COLS):
                raise ParseError(n, f'jumlah kolom US {len(r)}, seharusnya {len(US_COLS)}')
            us.append([current[0], current[2]] + r)
        elif AC_HEAD.match(heading) or MRTM_HEAD.match(heading):
            if current is None:
                raise ParseError(first_line, 'tabel di luar kelompok US (tidak ada judul "## US-XX: ..." di atasnya)')
            if AC_HEAD.match(heading):
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
                    table.append(r)
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
```

Catatan desain: `convert` memanggil `parse` lebih dulu, sehingga bila parse gagal tidak ada file yang ditulis (`test_main_reports_error_and_exit_code`).

- [ ] **Step 4: Jalankan, pastikan lulus**

Run: `python -m pytest tests -q`
Expected: PASS, 10 test

- [ ] **Step 5: Commit**

```bash
git add us-ac-writer/scripts/us_ac_to_tsv.py tests/conftest.py tests/test_us_ac_to_tsv.py
git commit -m "Add the us-ac.md to TSV converter for pasting into Excel"
```

---

### Task 2: Salinan aturan dan cek sinkron

**Files:**
- Create: `tools/sync_handbook.py`, `tests/test_handbook_sync.py`, `us-ac-writer/references/sysfunc-us-ac-guide.md`, `us-ac-writer/references/appendix-d-us-ac.md`

**Interfaces:**
- Produces: modul `sync_handbook` dengan `PAIRS: list[tuple[str, str]]` (path relatif handbook, path relatif repo), `handbook_dir() -> Path`, `differences(hb: Path, repo: Path) -> list[str]` (path repo yang berbeda atau hilang), `update(hb: Path, repo: Path) -> list[str]`, `main(argv) -> int` (0 sinkron/terupdate, 1 berbeda, 2 folder handbook tidak ada).

- [ ] **Step 1: Tulis test yang gagal** `tests/test_handbook_sync.py`

```python
from pathlib import Path

import pytest

import sync_handbook as S

REPO = Path(__file__).resolve().parents[1]


def make(tmp_path, hb_text, repo_text, crlf=False):
    hb, repo = tmp_path / 'hb', tmp_path / 'repo'
    for src, dst in S.PAIRS:
        (hb / src).parent.mkdir(parents=True, exist_ok=True)
        (hb / src).write_bytes((hb_text.replace('\n', '\r\n') if crlf else hb_text).encode('utf-8'))
        if repo_text is not None:
            (repo / dst).parent.mkdir(parents=True, exist_ok=True)
            (repo / dst).write_bytes(repo_text.encode('utf-8'))
    return hb, repo


def test_pairs_cover_guide_and_appendix_d():
    assert dict(S.PAIRS) == {
        'Template/SysFunc_US_AC_Guide.md': 'us-ac-writer/references/sysfunc-us-ac-guide.md',
        'Appendix_D_Panduan_Praktik_US_AC.md': 'us-ac-writer/references/appendix-d-us-ac.md',
    }


def test_identical_copies_have_no_differences(tmp_path):
    hb, repo = make(tmp_path, 'aturan\n', 'aturan\n')
    assert S.differences(hb, repo) == []


def test_crlf_difference_is_ignored(tmp_path):
    hb, repo = make(tmp_path, 'aturan\nbaris dua\n', 'aturan\nbaris dua\n', crlf=True)
    assert S.differences(hb, repo) == []


def test_changed_and_missing_copies_are_reported(tmp_path):
    hb, repo = make(tmp_path, 'baru\n', 'lama\n')
    assert S.differences(hb, repo) == [dst for _, dst in S.PAIRS]
    hb2, repo2 = make(tmp_path / 'b', 'baru\n', None)
    assert S.differences(hb2, repo2) == [dst for _, dst in S.PAIRS]


def test_update_copies_bytes(tmp_path):
    hb, repo = make(tmp_path, 'baru\n', 'lama\n')
    S.update(hb, repo)
    assert S.differences(hb, repo) == []


def test_missing_handbook_exits_2(tmp_path, monkeypatch, capsys):
    monkeypatch.setenv('BA_HANDBOOK_DIR', str(tmp_path / 'tidak-ada'))
    assert S.main([]) == 2
    assert 'BA_HANDBOOK_DIR' in capsys.readouterr().err


def test_committed_copies_match_handbook():
    hb = S.handbook_dir()
    if not hb.is_dir():
        pytest.skip(f'folder handbook tidak ada: {hb}')
    assert S.differences(hb, REPO) == [], 'Jalankan: python tools/sync_handbook.py --update'
```

- [ ] **Step 2: Jalankan, pastikan gagal**

Run: `python -m pytest tests -q`
Expected: FAIL, `ModuleNotFoundError: No module named 'sync_handbook'`

- [ ] **Step 3: Implementasi** `tools/sync_handbook.py`

```python
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
```

- [ ] **Step 4: Buat salinan aturan**

Run: `python tools/sync_handbook.py --update`
Expected: `diperbarui: us-ac-writer/references/sysfunc-us-ac-guide.md, us-ac-writer/references/appendix-d-us-ac.md`
Lalu: `python tools/sync_handbook.py` → `sinkron`.

- [ ] **Step 5: Jalankan, pastikan lulus**

Run: `python -m pytest tests -q`
Expected: PASS, 17 test

- [ ] **Step 6: Commit**

```bash
git add tools/sync_handbook.py tests/test_handbook_sync.py us-ac-writer/references
git commit -m "Copy the handbook US/AC rules into the skill and check they stay in sync"
```

---

### Task 3: SKILL.md

**Files:**
- Create: `us-ac-writer/SKILL.md`, `tests/test_skill_md.py`

**Interfaces:**
- Consumes: `us-ac-writer/references/*.md` (Task 2), `us-ac-writer/scripts/us_ac_to_tsv.py` (Task 1).

- [ ] **Step 1: Tulis test yang gagal** `tests/test_skill_md.py`

```python
import re
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1] / 'us-ac-writer' / 'SKILL.md'
EMOJI = re.compile('[\U0001F300-\U0001FAFF\u2600-\u27BF\u2B1C\u2B50]')


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
    assert '\u2014' not in text
```

- [ ] **Step 2: Jalankan, pastikan gagal**

Run: `python -m pytest tests/test_skill_md.py -q`
Expected: FAIL, `FileNotFoundError` untuk `us-ac-writer/SKILL.md`

- [ ] **Step 3: Implementasi** `us-ac-writer/SKILL.md`

````markdown
---
name: us-ac-writer
description: Write User Stories and Acceptance Criteria that follow the BA Handbook system prompt (SysFunc_US_AC_Guide and Appendix D) without being reminded. Use when the user says "buatkan US AC", "tulis user story", "buat acceptance criteria", "lengkapi Given/When/Then", "ikuti aturan system prompt US AC", asks for MRTM rows, or hands over MoM notes, a narrative, screenshots, a BRD, a process map, or a product-discovery draft and wants user stories with acceptance criteria. Outputs one block per user story (story first, its AC below) in docs/ba/us-ac.md plus us.tsv and ac.tsv ready to paste into the xlsx.
---

# US AC Writer

Writes User Stories (US) and Acceptance Criteria (AC) for the Analysis phase (BA Handbook Bab 4.4) and hands them to `ba-grooming` for review.

## Rules are mandatory and live in references

Before writing anything, read both files completely and follow every rule in them:

- `references/sysfunc-us-ac-guide.md`: the system prompt (Tahap 1 to 4: context and persona, US generation with INVEST, AC generation with Given/When/Then, MRTM).
- `references/appendix-d-us-ac.md`: Appendix D practice guide (anatomy of a US, vertical slicing, bloated versus standard AC).

These copies match the handbook (checked by `tools/sync_handbook.py`). Where this file and the references disagree, the references win. Do not ask the user to restate the rules; applying them is the point of this skill.

## Inputs

Use whatever the user provides, in any combination: MoM, a narrative, screenshots or mockups, and documents in `docs/ba/` (`brd.md`, `business-rules.md`, `process-map-to-be.md`, a `product-discovery` draft). If `docs/ba/us-ac.md` exists, read it first.

## Workflow

1. **Collect context.** Fill the four Tahap 1 inputs: feature or module name, business goal, primary persona, key actions. Ask only for what is still missing, one question at a time, each with a recommended answer. Also ask once which language the app's UI text uses if it is not evident; quote UI labels and messages verbatim in that language.
2. **Check existing stories.** If `docs/ba/us-ac.md` or a pasted list exists, decide whether each key action is already covered by an existing US. If it is, add AC under that US instead of creating a new one. Continue numbering from the highest existing US and AC numbers.
3. **Vertical slicing.** If a US covers more than 3 CRUD actions or more than 1 sprint, propose a split and wait for the user's agreement.
4. **Write the US.** Action without "bisa" or "dapat"; business value without "agar" or "untuk". Title in the form verb + object. Validate each US against INVEST and fix failures before writing AC.
5. **Choose the AC format per US.** Input/output variables at most 3 and logic combinations at most 3: Given/When/Then. Otherwise write one AC whose THEN is `Refer to MRTM Rows: <first TCID> through <last TCID> for comprehensive logic combinations.` and build the MRTM table.
6. **Write the AC.** At least one Happy, one Negative, and one Boundary or Edge scenario per US; add State and Permission scenarios when relevant. GIVEN names the page. WHEN holds only user actions, never `OR`. THEN is observable and quotes text verbatim. A system result between actions splits the AC.
7. **Check before handing over.** Fix every violation, then show the result:
   - WHEN contains no system result ("aktif", "terbuka", "muncul", "berubah", "menampilkan", "sistem ...") and no `OR`.
   - Each AC has exactly one THEN (Rule P3-01).
   - Boundary values and edge cases are explicit (Rule RE-04).
   - Every US has Happy, Negative, and Boundary or Edge scenarios.
   - IDs follow `US-XX`, `AC-XX.YY` (XX is the story number), `TRM_[MODUL]_XXX`.
   - No "bisa/dapat" in actions, no "agar/untuk" in business value, no emoji.
8. **Hand over.** Show the blocks in chat, write them to `docs/ba/us-ac.md`, run `python <skill dir>/scripts/us_ac_to_tsv.py docs/ba/us-ac.md`, then list open questions and suggest `ba-grooming`.

## Output format

One block per story, story first, its AC below. Write it exactly like this so `scripts/us_ac_to_tsv.py` can read it:

```markdown
## US-XX: <Judul>

| Persona | Aksi yang dilakukan | Hasil nilai bisnis |
|---|---|---|
| <persona> | <aksi> | <nilai bisnis> |

### Acceptance Criteria US-XX

| AC-ID | Skenario | GIVEN | WHEN | THEN | Status |
|---|---|---|---|---|---|
| AC-XX.01 | Happy: <skenario> | Saya seorang <role><br>AND saya berada di halaman "<halaman>" | Saya <aksi><br>AND saya <aksi> | Sistem menampilkan <hasil><br>AND <hasil lain> | Draft |

### MRTM US-XX

| User Story ID | Acceptance Criteria ID | User | Test Case ID | <Variabel 1> | <Variabel 2> | Kondisi Khusus | HASIL (EXPECTED RESULT) |
|---|---|---|---|---|---|---|---|
| US_XX | AC_01 | <persona> | TRM_<MODUL>_001 | <nilai> | [ANY] | [-] | <hasil> |
```

- Skenario starts with its category: `Happy:`, `Negative:`, `Boundary:`, `Edge:`, `State:`, `Permission:`.
- Status of every new AC is `Draft`.
- Separate AND lines inside a cell with `<br>`. Write a literal pipe as `\|`.
- Include the MRTM section only when the story uses it.
- Sentences in Indonesian following the guide's patterns; UI text verbatim in the app's language.

## Files

- `docs/ba/us-ac.md`: append new stories at the end; append new AC at the end of their story's AC table. Never edit existing rows unless the user explicitly asks.
- `docs/ba/us.tsv`, `docs/ba/ac.tsv`, `docs/ba/mrtm-<modul>.tsv`: always generated by `scripts/us_ac_to_tsv.py`, never written by hand. If the script reports an error with a line number, fix that line in `us-ac.md` and run it again.

## Handoff

Next step: `ba-grooming` reviews the stories from the business perspective, then `ba-handoff` builds the traceability matrix.

## Writing conventions (enforced in all output)

- No AI slop: no filler or hedging; every sentence informs. Use the `stop-slop` skill on prose when unsure.
- No em-dashes, no double-dashes in prose; dashes only as Markdown syntax.
- No emoji. Replace the guide's picture markers with the words Happy, Negative, Boundary, Edge, State, Permission.
- Governance (Rule AI-01, AI-03): every artifact this skill drafts is AI-generated and must be reviewed by the responsible BA before it becomes an official deliverable.
````

- [ ] **Step 4: Jalankan, pastikan lulus**

Run: `python -m pytest tests -q`
Expected: PASS, 21 test

- [ ] **Step 5: Commit**

```bash
git add us-ac-writer/SKILL.md tests/test_skill_md.py
git commit -m "Add the us-ac-writer skill instructions"
```

---

### Task 4: Integrasi pipeline dan build plugin

**Files:**
- Create: `.claude-plugin/plugin.json`, `tools/build_plugin.py`, `tests/test_build_plugin.py`
- Modify: `README.md`, `product-discovery/SKILL.md:37`, `ba-grooming/SKILL.md:16`, `my-ba-flow.plugin`

**Interfaces:**
- Consumes: semua file `us-ac-writer/` (Task 1 sampai 3).
- Produces: `build_plugin.SKILLS: list[str]`, `build_plugin.build(out: Path) -> list[str]` (daftar nama entri zip).

- [ ] **Step 1: Tulis test yang gagal** `tests/test_build_plugin.py`

```python
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
```

Catatan: `OLD_SKILLS` adalah 18 folder skill yang ada di `my-ba-flow.plugin` saat ini (tanpa `skill-creator` dan `write-a-skill`).

- [ ] **Step 2: Jalankan, pastikan gagal**

Run: `python -m pytest tests/test_build_plugin.py -q`
Expected: FAIL, `ModuleNotFoundError: No module named 'build_plugin'`

- [ ] **Step 3: Simpan plugin.json di repo**

```bash
python -c "import zipfile,pathlib;p=pathlib.Path('.claude-plugin');p.mkdir(exist_ok=True);(p/'plugin.json').write_bytes(zipfile.ZipFile('my-ba-flow.plugin').read('.claude-plugin/plugin.json'))"
```

Lalu ubah `"version": "1.1.0"` menjadi `"version": "1.2.0"` di `.claude-plugin/plugin.json`. Deskripsi (yang masih menyebut v1.13) tidak diubah di sini; itu bagian pekerjaan penyelarasan v2.1 yang terpisah.

- [ ] **Step 4: Implementasi** `tools/build_plugin.py`

```python
"""Rakit my-ba-flow.plugin (zip) dari folder skill di repo.

Pakai: python tools/build_plugin.py [--out <path>]
"""
import sys
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SKILLS = ['ba-grooming', 'ba-handoff', 'ba-planning', 'caveman', 'change-request', 'data-dictionary', 'grill-me',
          'grill-with-docs', 'handoff', 'impact-analysis', 'process-mapping', 'product-discovery',
          'requirement-elicitation', 'reverse-engineering', 'solution-evaluation', 'stakeholder-interview',
          'stop-slop', 'us-ac-writer', 'wireframe-spec']
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
```

- [ ] **Step 5: Integrasi skill lain**

`README.md`: sisipkan baris berikut tepat sebelum baris `| 4. Design & Validation | \`ba-grooming\` | ...`:

```markdown
| 3. Analysis (US & AC) | `us-ac-writer` | `us-ac.md` (per story: US, then its AC and MRTM), `us.tsv`, `ac.tsv`, `mrtm-*.tsv`; rules from SysFunc_US_AC_Guide and Appendix D |
```

Lalu tambahkan bagian ini di akhir `README.md`:

```markdown
## Keeping handbook copies in sync

`us-ac-writer/references/` holds exact copies of the handbook's `Template/SysFunc_US_AC_Guide.md` and `Appendix_D_Panduan_Praktik_US_AC.md`. After the handbook changes, run `python tools/sync_handbook.py --update` (set `BA_HANDBOOK_DIR` if the handbook is not at the default path), run `python -m pytest tests -q`, then rebuild the plugin with `python tools/build_plugin.py` and reinstall it.
```

`product-discovery/SKILL.md` baris 37: ganti `the pipeline refines the full Given/When/Then later` dengan `` `us-ac-writer` turns these into full Given/When/Then later``.

`ba-grooming/SKILL.md`: setelah kalimat `The user gives you one or more user stories and their acceptance criteria.` tambahkan kalimat baru dalam paragraf yang sama: `` If they are not pasted, read `docs/ba/us-ac.md` written by `us-ac-writer`.``

- [ ] **Step 6: Build dan jalankan semua test**

```bash
python tools/build_plugin.py
python -m pytest tests -q
```

Expected: `my-ba-flow.plugin: 29 file` (25 entri lama + `SKILL.md`, 2 file `references/`, 1 skrip), lalu PASS, 23 test.

- [ ] **Step 7: Commit**

```bash
git add .claude-plugin/plugin.json tools/build_plugin.py tests/test_build_plugin.py README.md product-discovery/SKILL.md ba-grooming/SKILL.md my-ba-flow.plugin
git commit -m "Wire us-ac-writer into the pipeline and rebuild the plugin as 1.2.0"
```

- [ ] **Step 8: Serahkan**

Beri tahu pengguna: pasang ulang `my-ba-flow.plugin` (versi 1.2.0), lalu uji dengan meminta US/AC untuk satu fitur nyata dan menempel `us.tsv`/`ac.tsv` ke xlsx.
