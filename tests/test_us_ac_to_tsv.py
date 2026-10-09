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


@pytest.mark.parametrize('heading', ['### Acceptance Criteria (US-06)', '### Acceptance Criteria', '### Acceptance Criteria US-07'])
def test_ac_table_under_wrong_heading_fails(heading):
    bad = DOC.replace('### Acceptance Criteria US-06', heading, 1)
    with pytest.raises(T.ParseError):
        T.parse(bad)


def test_us_heading_without_us_table_fails():
    bad = DOC.replace('| Persona | Aksi yang dilakukan | Hasil nilai bisnis |\n|---|---|---|\n| Customer | membuka halaman order | order hanya dibuat oleh pelanggan yang memenuhi syarat |\n', '', 1)
    with pytest.raises(T.ParseError, match='US-07'):
        T.parse(bad)


@pytest.mark.parametrize('heading', ['## US-07 - Mengecek Kelayakan Order', '## US-7: Mengecek Kelayakan Order'])
def test_malformed_us_heading_fails_with_line(heading):
    bad = DOC.replace('## US-07: Mengecek Kelayakan Order', heading, 1)
    with pytest.raises(T.ParseError, match='US-XX'):
        T.parse(bad)


def test_duplicate_ids_fail():
    with pytest.raises(T.ParseError, match='AC-06.01'):
        T.parse(DOC.replace('| AC-06.02 |', '| AC-06.01 |', 1))
    dup_us = DOC + '\n## US-06: Lagi\n\n| Persona | Aksi yang dilakukan | Hasil nilai bisnis |\n|---|---|---|\n| A | b | c |\n'
    with pytest.raises(T.ParseError, match='US-06'):
        T.parse(dup_us)


def test_same_module_mrtm_with_different_columns_fails():
    extra = '''
## US-08: Order Lain

| Persona | Aksi yang dilakukan | Hasil nilai bisnis |
|---|---|---|
| Customer | membuka order lain | order sesuai aturan |

### Acceptance Criteria US-08

| AC-ID | Skenario | GIVEN | WHEN | THEN | Status |
|---|---|---|---|---|---|
| AC-08.01 | Happy: Matriks | g | w | Refer to MRTM Rows: TRM_ORD_003 through TRM_ORD_003 | Draft |

### MRTM US-08

| User Story ID | Acceptance Criteria ID | User | Test Case ID | Kode | HASIL (EXPECTED RESULT) |
|---|---|---|---|---|---|
| US_08 | AC_01 | Customer | TRM_ORD_003 | X | Y |
'''
    with pytest.raises(T.ParseError, match='ORD'):
        T.parse(DOC + extra)


def test_guide_split_suffix_ids_are_accepted():
    ok = DOC.replace('| AC-06.02 |', '| AC-06.01b |', 1)
    assert [r[0] for r in T.parse(ok)['ac']][:2] == ['AC-06.01', 'AC-06.01b']
