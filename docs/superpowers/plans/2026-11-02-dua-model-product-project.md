# Dua Model Kerja BA (Product Based + Project Based) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Tambah jalur product based ke plugin `my-ba-flow` (pintu masuk `ba-start`, `product-onboarding`, `fit-gap`, perluasan `discovery-meeting-prep`, skill `demo-terpandu-fgd` dipindah ke plugin) yang bermuara ke pipeline Handbook project based, lalu rilis plugin 1.4.0.

**Architecture:** Setiap skill adalah folder di akar repo berisi `SKILL.md` (+ `references/`, `assets/`, `scripts/` bila perlu). `tools/build_plugin.py` mengemas daftar `SKILLS` menjadi `my-ba-flow.plugin`. Tes pytest memeriksa isi teks SKILL.md (frontmatter, frasa pemicu, rujukan file, konvensi tulisan) dan isi paket.

**Tech Stack:** Markdown (SKILL.md), Python 3 + pytest (tes, build), Node.js (aset skill demo; hanya `node --check`).

**Spec:** `docs/superpowers/specs/2026-11-02-dua-model-product-project-design.md`

## Global Constraints

- Repo: `C:\Users\User\Documents\Github_Fahrudin\SERVICES\my-ba-flow`, kerja di branch `dua-model` (bukan `main`).
- Nama skill baru persis: `ba-start`, `product-onboarding`, `fit-gap`, `demo-terpandu-fgd`.
- Instruksi SKILL.md skill baru dalam bahasa Inggris; contoh output, template dokumen dan bank pertanyaan dalam bahasa Indonesia. `demo-terpandu-fgd` tetap berbahasa Indonesia.
- SKILL.md dan semua `references/*.md` skill baru/diubah: tanpa emoji, tanpa em dash (`—`), tanpa `--` di prosa (boleh di blok kode/flag CLI).
- Setiap SKILL.md skill yang menghasilkan dokumen diakhiri bagian `## Writing conventions (enforced in all output)` meniru `reverse-engineering/SKILL.md`, dengan penyesuaian format ringan (§6 spec) untuk product based.
- Folder output product based: `docs/ba/product/<produk>-<versi>/`; sesi: `docs/ba/product/<produk>-<versi>/sessions/<klien>-<tanggal>/`; demo project based: `docs/ba/demo-sessions/<tanggal>/`; masukan proyek di folder proyek baru: `docs/ba/product-input/`.
- Format ringan: header `**Produk:**`, `**Versi:**`, `**Tanggal:**`, `**Disusun:**` (dua spasi di akhir baris) dan baris `Disusun dengan bantuan AI, ditinjau oleh BA: (nama)`; tanpa template Handbook dan tanpa sign-off.
- Label aturan bisnis product based persis `Terbukti` / `Asumsi`. Status fit-gap persis: `Fit`, `Fit dengan konfigurasi`, `Gap kecil`, `Gap besar`, `Tidak dibutuhkan`. Status asumsi persis: `dikonfirmasi`, `dibantah`, `belum`.
- Skill lama: hanya boleh mengubah baris `description` `product-discovery` dan `reverse-engineering`, menambah bagian "Input from product based" di `reverse-engineering`, tipe sesi + bank pertanyaan di `discovery-meeting-prep`, satu baris Handoff di `wireframe-spec`. Langkah lain tidak diubah.
- Versi plugin: `1.4.0`.

## Review Focus

1. Arsip yang tidak bisa diekstrak (rar berpassword, rusak, bukan zip/rar): `product-onboarding` berhenti dan meminta pengguna mengekstrak sendiri, tidak menebak isi. Tes: Task 3 `test_product_onboarding_handles_extract_failure`.
2. Aplikasi tidak bisa dijalankan lokal (dependensi cloud, build gagal): ringkasan tetap dibuat dari kode, `product-brief.md` mencatat "Tidak dijalankan: <alasan>" dan semua aturan dari kode saja tetap `Asumsi`. Tes: Task 3 `test_product_onboarding_handles_app_not_running`.
3. `fit-gap` dipanggil tanpa debrief atau catatan sesi klien: skill menolak membuat matriks dan mengarahkan ke `discovery-meeting-prep`/`demo-terpandu-fgd`. Tes: Task 4 `test_fit_gap_requires_session_evidence`.
4. Versi produk baru datang saat fit-gap versi lama sudah ada: folder versi baru, dokumen lama tidak ditimpa, ringkas perubahan. Tes: Task 3 `test_product_onboarding_versions_do_not_overwrite`.
5. `ba-start` di folder yang sudah berisi dokumen: menunjukkan posisi dan langkah berikutnya, tidak mengulang dari awal. Tes: Task 5 `test_ba_start_resumes_from_existing_docs`.

---

### Task 1: Branch, spec, dan pemeriksa skill bersama

**Files:**
- Create: `tests/skill_checks.py`
- Create: `tests/test_new_skills.py`
- Commit juga: `docs/superpowers/specs/2026-11-02-dua-model-product-project-design.md`, rencana ini

**Interfaces:**
- Produces: `skill_checks.read_skill(name: str) -> tuple[dict, str]` (frontmatter `{'name','description'}`, body teks); `skill_checks.prose_violations(text: str) -> list[str]` (emoji, `—`, `--` di luar blok kode/inline code); `skill_checks.missing_refs(name: str) -> list[str]` (path `references/`, `scripts/`, `assets/` yang disebut dalam backtick di SKILL.md tetapi tidak ada). `tests/test_new_skills.py` berisi `NEW_SKILLS: dict[str, list[str]]` (nama skill ke frasa pemicu wajib di description) dan tiga tes berparameter atasnya.

- [ ] **Step 1:** `git switch -c dua-model` di repo. Expected: `Switched to a new branch 'dua-model'`.
- [ ] **Step 2: Tulis tes untuk pemeriksa** di `tests/test_new_skills.py`:

```python
from skill_checks import prose_violations

def test_prose_violations_flags_dash_and_emoji_outside_code():
    assert prose_violations('a — b') and prose_violations('x -- y') and prose_violations('ok \U0001F600')
    assert prose_violations('`--format` and\n```\nnode a.mjs --x\n```') == []
```

Tambahkan juga `NEW_SKILLS = {}` dan tiga tes berparameter `@pytest.mark.parametrize('name', sorted(NEW_SKILLS))`: `test_frontmatter_and_triggers` (name == folder, setiap frasa ada di description, case-insensitive, description <= 1024 karakter), `test_refs_exist` (`missing_refs(name) == []`), `test_prose_rules` (`prose_violations` kosong untuk SKILL.md dan setiap `references/*.md`).
- [ ] **Step 3:** `python -m pytest tests/test_new_skills.py -q` → FAIL (`ModuleNotFoundError: skill_checks`).
- [ ] **Step 4:** Tulis `tests/skill_checks.py` dengan tiga fungsi di atas; tambahkan `'tests'` ke daftar `sys.path` di `tests/conftest.py` bila perlu. Hapus isi blok ```` ``` ```` dan `` `...` `` sebelum memeriksa `--`; emoji pakai regex yang sama dengan `tests/test_skill_md.py`.
- [ ] **Step 5:** `python -m pytest tests -q` → semua lulus (40 lama + baru).
- [ ] **Step 6: Commit** `git add tests docs/superpowers && git commit -m "Add the dual-model spec, plan, and shared skill checks"`

### Task 2: Pindahkan `demo-terpandu-fgd` ke plugin

**Files:**
- Create: `demo-terpandu-fgd/` (salin seluruh `C:\Users\User\.claude\skills\demo-terpandu-fgd\`: `SKILL.md`, `references/`, `assets/demo-proxy.mjs`, `assets/presenter-panel.js`, `scripts/build-script.mjs`, `scripts/import-questions.mjs`)
- Modify: `demo-terpandu-fgd/SKILL.md`, `demo-terpandu-fgd/references/desain-skenario.md` (satu `—`)
- Modify: `tools/build_plugin.py` (`SKILLS`), `tests/test_build_plugin.py` (`SKILLS`), `tests/test_new_skills.py`

**Interfaces:**
- Produces: skill `demo-terpandu-fgd` yang menyalin catatan sesi ke jalur §5.4 spec; dibaca Task 4 (`fit-gap`) dan Task 6 (`wireframe-spec` Handoff).

- [ ] **Step 1: Tes gagal.** Tambah ke `NEW_SKILLS`: `'demo-terpandu-fgd': ['panduan demo', 'FGD', 'prototype']`. Tambah tes:

```python
def test_demo_skill_covers_both_models():
    _, body = read_skill('demo-terpandu-fgd')
    for s in ('product based', 'project based', 'docs/ba/product/', '/sessions/', 'docs/ba/demo-sessions/', 'Figma'):
        assert s in body, s

def test_demo_assets_parse_with_node():
    for f in ('assets/demo-proxy.mjs', 'assets/presenter-panel.js', 'scripts/build-script.mjs', 'scripts/import-questions.mjs'):
        assert subprocess.run(['node', '--check', str(REPO / 'demo-terpandu-fgd' / f)]).returncode == 0, f
```

(lewati `test_demo_assets_parse_with_node` dengan `pytest.skip` bila `shutil.which('node')` kosong). Tambah `'demo-terpandu-fgd'` ke `SKILLS` di `tests/test_build_plugin.py`.
- [ ] **Step 2:** `python -m pytest tests -q` → FAIL (folder belum ada).
- [ ] **Step 3:** Salin folder skill; ganti `—` di `references/desain-skenario.md`; tambah bagian `## Dipakai di dua model` di SKILL.md: bahan product based (`product-brief.md`, `feature-inventory.md`, `demo-traps.md`, prep sheet `discovery-meeting-prep`), project based (prototype web; Figma hanya rundown cetak + lembar catatan tanpa panel), salin catatan ke `docs/ba/product/<produk>-<versi>/sessions/<klien>-<tanggal>/` atau `docs/ba/demo-sessions/<tanggal>/`, dan siapa pembacanya (`fit-gap`; `ba-grooming`/`change-request`). Tambah `description` frasa "prototype". Tambah `'demo-terpandu-fgd'` ke `SKILLS` di `tools/build_plugin.py`.
- [ ] **Step 4:** `python -m pytest tests -q` → lulus.
- [ ] **Step 5: Commit** `git commit -am "Ship demo-terpandu-fgd in the plugin for both work models"` (sertakan `git add demo-terpandu-fgd`).

### Task 3: `product-onboarding`

**Files:**
- Create: `product-onboarding/SKILL.md`, `product-onboarding/references/output-templates.md`
- Modify: `tools/build_plugin.py`, `tests/test_build_plugin.py`, `tests/test_new_skills.py`

**Interfaces:**
- Produces: lima file di `docs/ba/product/<produk>-<versi>/` dengan nama persis `product-brief.md`, `feature-inventory.md`, `business-rules-found.md`, `assumptions-to-confirm.md`, `demo-traps.md`. Dibaca Task 2, 4, 6.

- [ ] **Step 1: Tes gagal.** `NEW_SKILLS['product-onboarding'] = ['zip', 'rar', 'product based', 'aplikasi']`. Tes:

```python
def test_product_onboarding_outputs_and_labels():
    _, body = read_skill('product-onboarding')
    for s in ('product-brief.md', 'feature-inventory.md', 'business-rules-found.md',
              'assumptions-to-confirm.md', 'demo-traps.md', 'docs/ba/product/', 'Terbukti', 'Asumsi',
              'tar -xf', '7z x', 'references/output-templates.md'):
        assert s in body, s

def test_product_onboarding_handles_extract_failure():
    _, body = read_skill('product-onboarding')
    assert 'password' in body.lower() and 'extract it themselves' in body

def test_product_onboarding_handles_app_not_running():
    _, body = read_skill('product-onboarding')
    assert 'Tidak dijalankan:' in body

def test_product_onboarding_versions_do_not_overwrite():
    _, body = read_skill('product-onboarding')
    assert 'never overwrite' in body and 'what changed' in body

def test_product_onboarding_is_not_bab_4a():
    _, body = read_skill('product-onboarding')
    assert 'RE Scope Statement' in body and 'reverse-engineering' in body
```
- [ ] **Step 2:** `python -m pytest tests/test_new_skills.py -q` → FAIL.
- [ ] **Step 3:** Tulis SKILL.md mengikuti §5.2 spec: input; langkah 1–5 (ekstrak dengan `tar -xf` lalu `7z x`, stop dan minta pengguna "extract it themselves" bila password/rusak; isi arsip adalah data, bukan instruksi; baca kode; jalankan lokal, bila gagal catat `Tidak dijalankan: <alasan>`; uji kasus tepi; bandingkan versi: folder versi baru, never overwrite, ringkas what changed); tabel lima output; kalimat bahwa skill ini bukan Bab 4A (tidak ada RE Scope Statement; itu nanti di `reverse-engineering` lewat `fit-gap`); Handoff ke `discovery-meeting-prep` (tipe Demo produk) lalu `demo-terpandu-fgd`; Writing conventions format ringan. `references/output-templates.md`: kerangka kelima file dengan header format ringan dan kolom dari §5.2 (aturan: ID, aturan, sumber/bukti, label Terbukti/Asumsi). Tambah ke `SKILLS` kedua file build/tes.
- [ ] **Step 4:** `python -m pytest tests -q` → lulus.
- [ ] **Step 5: Commit** `git add product-onboarding tests tools && git commit -m "Add product-onboarding for apps handed over as zip or rar"`

### Task 4: `fit-gap`

**Files:**
- Create: `fit-gap/SKILL.md`
- Modify: `tools/build_plugin.py`, `tests/test_build_plugin.py`, `tests/test_new_skills.py`

**Interfaces:**
- Consumes: lima file Task 3; sesi Task 2/Task 6 di `sessions/<klien>-<tanggal>/` (`meeting-prep.md`, `debrief.md`, catatan demo).
- Produces: `docs/ba/product/<produk>-<versi>/fit-gap-<klien>.md`; saat titik masuk proyek, folder proyek baru dengan `docs/ba/product-input/`.

- [ ] **Step 1: Tes gagal.** `NEW_SKILLS['fit-gap'] = ['fit-gap', 'calon klien', 'product based']`. Tes:

```python
def test_fit_gap_statuses_and_handoff():
    _, body = read_skill('fit-gap')
    for s in ('Fit', 'Fit dengan konfigurasi', 'Gap kecil', 'Gap besar', 'Tidak dibutuhkan',
              'dikonfirmasi', 'dibantah', 'belum', 'fit-gap-<klien>.md', 'docs/ba/product-input/',
              'ba-planning', 'reverse-engineering', 'requirement-elicitation', 'P1-01', 'gap-analysis.md'):
        assert s in body, s

def test_fit_gap_requires_session_evidence():
    _, body = read_skill('fit-gap')
    assert 'no debrief' in body.lower() and 'discovery-meeting-prep' in body

def test_fit_gap_is_product_based_only():
    _, body = read_skill('fit-gap')
    assert 'project based' in body and 'ba-grooming' in body
```
- [ ] **Step 2:** pytest → FAIL.
- [ ] **Step 3:** Tulis SKILL.md mengikuti §5.5 spec: input; tolak bila no debrief/catatan sesi; tabel matriks (kolom persis dari spec) dan lima status; status akhir asumsi; ringkasan + rekomendasi; titik masuk proyek: tawarkan membuat folder proyek per klien, salin fit-gap + folder sesi klien + lima file onboarding ke `docs/ba/product-input/`, lalu urutan `ba-planning` (P1-01) → `reverse-engineering` (penuh, fit-gap jadi masukan `gap-analysis.md`) → `requirement-elicitation`; catatan bahwa project based tidak memakai skill ini (masukan prototype ke `ba-grooming`); Writing conventions format ringan. Tambah ke `SKILLS`.
- [ ] **Step 4:** pytest → lulus.
- [ ] **Step 5: Commit** `git add fit-gap tests tools && git commit -m "Add fit-gap as the entry point from product demo to project"`

### Task 5: `ba-start`

**Files:**
- Create: `ba-start/SKILL.md`
- Modify: `tools/build_plugin.py`, `tests/test_build_plugin.py`, `tests/test_new_skills.py`

**Interfaces:**
- Consumes: nama skill dari Task 2–4 dan skill lama.

- [ ] **Step 1: Tes gagal.** `NEW_SKILLS['ba-start'] = ['mulai', 'product based', 'project based', 'zip']`. Tes:

```python
def test_ba_start_routes_both_models():
    _, body = read_skill('ba-start')
    for s in ('AskUserQuestion', 'Pak Tan', 'product-onboarding', 'discovery-meeting-prep',
              'demo-terpandu-fgd', 'fit-gap', 'ba-planning', 'wireframe-spec', 'ba-grooming'):
        assert s in body, s
    assert 'does not write documents' in body

def test_ba_start_resumes_from_existing_docs():
    _, body = read_skill('ba-start')
    assert 'docs/ba/product/' in body and 'next step' in body and 'do not restart' in body.lower()
```
- [ ] **Step 2:** pytest → FAIL.
- [ ] **Step 3:** Tulis SKILL.md mengikuti §5.1 spec: tanya model via AskUserQuestion; untuk product based tanya pembuat (Pak Tan / BA sendiri / lainnya) dan artinya; peta langkah per model (diagram §4 spec, hanya jalur terpilih); deteksi posisi dari file yang ada (`docs/ba/product/...`, `fit-gap-*.md`, `docs/ba/ba-work-plan.md`, dst.) dan tampilkan next step, do not restart; skill ini does not write documents. Tambah ke `SKILLS`.
- [ ] **Step 4:** pytest → lulus.
- [ ] **Step 5: Commit** `git add ba-start tests tools && git commit -m "Add ba-start to route BA work into product or project based"`

### Task 6: Sambungkan skill lama

**Files:**
- Modify: `discovery-meeting-prep/SKILL.md` (Step 1 tabel tipe sesi, output, Handoff), `discovery-meeting-prep/references/question-bank.md` (bagian baru `## Bagian E: Demo produk ke calon klien` sebelum `## Teknik menggali`)
- Modify: `reverse-engineering/SKILL.md` (description; bagian baru `## Input from product based` sebelum `## Output`)
- Modify: `product-discovery/SKILL.md` (description saja)
- Modify: `wireframe-spec/SKILL.md` (satu butir Handoff)
- Test: `tests/test_new_skills.py`

**Interfaces:**
- Consumes: jalur dan nama file Task 2–4.

- [ ] **Step 1: Tes gagal.**

```python
def test_discovery_has_product_demo_session():
    _, body = read_skill('discovery-meeting-prep')
    for s in ('Product demo to a prospect', 'product-brief.md', 'assumptions-to-confirm.md',
              'sessions/<klien>-<tanggal>/', 'meeting-prep.md', 'debrief.md', 'Module E'):
        assert s in body, s
    bank = (REPO / 'discovery-meeting-prep/references/question-bank.md').read_text(encoding='utf-8')
    assert '## Bagian E: Demo produk ke calon klien' in bank and '| E-01 |' in bank

def test_reverse_engineering_accepts_product_input():
    head, body = read_skill('reverse-engineering')
    assert '## Input from product based' in body
    for s in ('High', 'Medium', 'Low', 'dibantah', 'fit-gap', 'gap-analysis.md'):
        assert s in body.split('## Input from product based')[1].split('\n## ')[0], s
    assert 'document what this app already does' not in head['description']

def test_product_discovery_does_not_claim_existing_apps():
    head, _ = read_skill('product-discovery')
    assert 'zip' not in head['description'].lower() and 'existing app' not in head['description'].lower()

def test_wireframe_spec_points_to_demo_guide():
    _, body = read_skill('wireframe-spec')
    assert 'demo-terpandu-fgd' in body.split('## Handoff')[1]
```
- [ ] **Step 2:** pytest → FAIL.
- [ ] **Step 3:** Terapkan §5.3 spec ke `discovery-meeting-prep` (tipe sesi keempat "Product demo to a prospect", modul Core A + Module E, konteks wajib, jalur output sesi, red flag tambahan, Handoff ke `demo-terpandu-fgd` lalu `fit-gap`); tulis Bagian E (format tabel sama dengan Bagian A: `| ID | Pertanyaan | Prio | Yang dicari |`, ID `E-01`… minimal 8 pertanyaan, P1 untuk konfirmasi asumsi dan kecocokan proses). Tambah bagian `reverse-engineering` sesuai §5.5 spec butir 2 (dijalankan penuh, pemetaan empat baris Confidence Level, fit-gap sebagai masukan Gap Report). Ganti frasa "document what this app already does" di description `reverse-engineering` dengan frasa yang hanya untuk sistem lama yang akan dimodernisasi. Pastikan description `product-discovery` hanya untuk ide tanpa aplikasi. Tambah butir Handoff `wireframe-spec`: validasi mockup/prototype ke klien dengan `demo-terpandu-fgd`.
- [ ] **Step 4:** `python -m pytest tests -q` → lulus (termasuk tes lama `test_handbook_*`).
- [ ] **Step 5: Commit** `git commit -am "Connect discovery, reverse engineering, and wireframe spec to the product path"`

### Task 7: README, versi 1.4.0, kemas, pasang

**Files:**
- Modify: `README.md`, `.claude-plugin/plugin.json`, `tests/test_build_plugin.py`
- Build: `my-ba-flow.plugin`

- [ ] **Step 1: Tes gagal.** Di `tests/test_build_plugin.py` ubah versi yang diharapkan menjadi `'1.4.0'` dan tambahkan nama file wajib: `skills/ba-start/SKILL.md`, `skills/product-onboarding/references/output-templates.md`, `skills/fit-gap/SKILL.md`, `skills/demo-terpandu-fgd/assets/demo-proxy.mjs`, `skills/demo-terpandu-fgd/scripts/import-questions.mjs`. Tambah tes README berisi `## Two work models` dan keempat nama skill baru.
- [ ] **Step 2:** pytest → FAIL.
- [ ] **Step 3:** `plugin.json` versi `1.4.0`, description menyebut product based dan demo/FGD, keywords `product-based`, `demo`, `fgd`, `fit-gap`. README: bagian `## Two work models` (tabel dua model dan diagram §4 spec), tambah ketiga skill baru ke on-ramps dan `demo-terpandu-fgd` ke supporting skills.
- [ ] **Step 4:** `python -m pytest tests -q` → lulus; `python tools/build_plugin.py` → `my-ba-flow.plugin: N file` dengan N naik dari sebelumnya.
- [ ] **Step 5: Commit** `git commit -am "Release my-ba-flow 1.4.0 with the product based path"` (sertakan plugin hasil build bila repo memang melacaknya; cek `git ls-files my-ba-flow.plugin`).
- [ ] **Step 6:** Kirim `my-ba-flow.plugin` ke pengguna untuk dipasang. Setelah pengguna memastikan skill `my-ba-flow:demo-terpandu-fgd` muncul di daftar skill, hapus `C:\Users\User\.claude\skills\demo-terpandu-fgd` (disetujui pengguna; cadangan `.skill` ada di `C:\Users\User\Documents\Work\Egg Farm`). Push branch hanya bila pengguna meminta.
