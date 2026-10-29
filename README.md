# my-ba-flow — Business Analyst Pipeline (Claude Code Skills)

Personal skill library that operationalizes the internal **BA Handbook v2.1** (https://ba.learning.my.id, login required) as a
Claude Code / LLM skill pipeline. It takes a business need from project kickoff all the
way to solution evaluation, producing the planning, requirements, process, impact,
validation, and handoff artifacts the handbook mandates. Each stage reads the artifacts
produced by the previous stage and writes the next, so every decision stays traceable
from business objective to delivered solution.

All BA artifacts live in `docs/ba/`. The handbook is the single source of truth; where
a skill and the handbook disagree, the handbook wins.

## Pipeline mapped to the BA Handbook 8-phase lifecycle (Bab 4)

| Phase (Bab 4) | Skill | Produces |
| --- | --- | --- |
| 1. Planning & Scoping | `ba-planning` | `ba-work-plan.md`, `ba-approach.md`, `communication-plan.md`, `context-diagram.md` |
| 1. Planning (stakeholders) | `stakeholder-interview` | `stakeholder-map.md` (Bab 6.2.2), `interview-notes.md`, `pain-points-register.md`, `assumptions-log.md` |
| 2. Elicitation & Discovery | `requirement-elicitation` | `brd.md` (T-07), `business-rules.md` |
| 3. Analysis & Documentation | `process-mapping` | `process-map-as-is.md`, `process-map-to-be.md`, `gap-analysis.md` (Process Model) |
| 3. Analysis (impact/risk) | `impact-analysis` | `impact-assessment.md`, `risk-register.md` (4x4 model), `issue-register.md` (Issue Log, Bab 7.7.2), `change-readiness.md` |
| 3. Analysis (UI spec) | `wireframe-spec` | `screen-inventory.md`, `navigation-flow.md`, `field-specs/*.md` (FSD Section 8) |
| 3. Analysis (data) | `data-dictionary` | `data-dictionary.md`, `glossary.md`, `data-lineage.md` |
| 3. Analysis (US & AC) | `us-ac-writer` | `us-ac.md` (per story: US, then its AC and MRTM), `us.tsv`, `ac.tsv`, `mrtm-*.tsv`; rules from SysFunc_US_AC_Guide and Appendix D |
| 4. Verification & Validation | `ba-grooming` | Business review + Phase-4 verification and validation checklists; `review-checklist.md` (Bab 9.4) |
| 5. Approval & 6. Handoff | `ba-handoff` | `handoff-package.md`, `traceability-matrix.md` (Bab 5.4.2), `sign-off-checklist.md` (Approval Authority + DoR) |
| 7. Support & Change Mgmt | `change-request` | `change-requests/CR-XX.md` (T-18), `cr-register.md` |
| 8. Solution Evaluation | `solution-evaluation` | `uat-signoff.md`, `solution-evaluation.md`, `lesson-learned.md` |

### Optional on-ramps

- `product-discovery` — when starting from a raw idea with no requirements: interviews the
  user and emits a first-draft user-story / AC / sprint table that feeds
  `stakeholder-interview` and `requirement-elicitation`.
- `reverse-engineering` — when starting from an existing, undocumented system (Bab 4A):
  recovers the As-Is, business rules, and data dictionary (with confidence levels),
  then feeds the normal pipeline.

### How the stages connect

1. `ba-planning` is the mandatory first gate — the BA Work Plan must exist before any
   elicitation (Rule P1-01).
2. `stakeholder-interview` maps the landscape and surfaces pain points.
3. `requirement-elicitation` turns those into a baselined BRD and business rules.
4. `process-mapping` and `impact-analysis` run in parallel off the BRD: process maps show
   what changes; impact analysis quantifies risk (ISO 31000, 4x4) and logs issues.
5. `wireframe-spec` and `data-dictionary` run in parallel: the UI contract and the data
   contract.
6. `ba-grooming` validates stories from the business perspective and runs the Phase-4
   validation gate (peer review, Rule P4-01).
7. `ba-handoff` compiles everything with a Bab 5.4.2 traceability matrix, Approval Authority,
   and the DoR gate.
8. After baseline, `change-request` governs every change (Rule P7-01); after go-live,
   `solution-evaluation` runs UAT sign-off and Lesson Learned (Rule P8-01).

## Governance baked into every deliverable-producing skill

- Outputs target the handbook's official templates and formats in Bab 8 (T-04, T-07, T-09,
  T-18, T-App-BA/UIUX/Eng, T-PRD, T-FSD, T-RES) rather than ad-hoc formats (Rule DL-01, P3-03).
- Every deliverable carries a Revision History and version control (Rule DL-02).
- AI-drafted content must be reviewed by the responsible BA before it becomes an official
  deliverable, and AI assistance is logged in the Revision History (Rules AI-01, AI-03).
- Traceability is bidirectional: Business Need to Requirement to Test Case (Rule R-04).

## Supporting skills

General-purpose helpers usable at any stage:

- `grill-with-docs` — stress-test a plan against the project's domain language and docs before finalizing.
- `stop-slop` — remove AI writing patterns from prose.

One skill per job: `grill-me`, `handoff`, and `caveman` were dropped in 1.3.0 because
`grill-with-docs`, the app's own session handoff, and plain writing rules already cover
them. `skill-creator/` and `write-a-skill/` stay in the repo as authoring notes only and
are not shipped in the plugin.

## Keeping handbook copies in sync

`us-ac-writer/references/` holds exact copies of the handbook's `Template/SysFunc_US_AC_Guide.md` and `Appendix_D_Panduan_Praktik_US_AC.md`. After the handbook changes, run `python tools/sync_handbook.py --update` (set `BA_HANDBOOK_DIR` if the handbook is not at the default path), run `python -m pytest tests -q`, then rebuild the plugin with `python tools/build_plugin.py` and reinstall it.
