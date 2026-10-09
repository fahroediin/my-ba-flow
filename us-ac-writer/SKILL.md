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
5. **Choose the AC format per US.** Input/output variables at most 3 and logic combinations at most 3: Given/When/Then. Otherwise write one AC whose THEN is `Refer to MRTM Rows: <first TCID> through <last TCID> for comprehensive logic combinations.` and build the MRTM table. That AC uses Skenario `Happy: <rule name> sesuai matriks`, a GIVEN that names the role and page, and a WHEN with the single user action that triggers the rule; the combinations, including the failing and boundary ones, live in the MRTM rows, not in extra narrative AC.
6. **Write the AC.** At least one Happy, one Negative, and one Boundary or Edge scenario per US; add State and Permission scenarios when relevant. GIVEN names the page. WHEN holds only user actions, never `OR`. THEN is observable and quotes text verbatim. A system result between actions splits the AC.
7. **Check before handing over.** Fix every violation, then show the result:
   - WHEN contains no system result ("aktif", "terbuka", "muncul", "berubah", "menampilkan", "sistem ...") and no `OR`.
   - Each AC has exactly one THEN (Rule P3-01).
   - Boundary values and edge cases are explicit (Rule RE-04).
   - Every US has Happy, Negative, and Boundary or Edge scenarios. For a story that uses MRTM, the category coverage is met by the MRTM rows: they must include at least one passing, one failing, and one boundary combination.
   - IDs follow `US-XX`, `AC-XX.YY` (XX is the story number; a split scenario may add a letter, `AC-XX.01a`, as in the guide), `TRM_[MODUL]_XXX`. No ID is used twice.
   - No "bisa/dapat" in actions, no "agar/untuk" in business value, no emoji.
8. **Hand over.** Show the blocks in chat, write them to `docs/ba/us-ac.md`, run `python <skill dir>/scripts/us_ac_to_tsv.py docs/ba/us-ac.md`, then list the IDs added in this run, open questions, and suggest `ba-grooming`. Tell the user to paste only the new rows into the xlsx: the TSV files always hold every row, and pasting them over the sheet would overwrite statuses already changed there (Reviewed, Approved).

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
