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
