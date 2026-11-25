# my-ba-flow: Business Analyst Pipeline (Agent Skills)

A personal skill library that turns the internal **BA Handbook v2.1** (https://ba.learning.my.id, login required) into an agent skill pipeline. Every skill follows the open [Agent Skills](https://agentskills.io) format, so it runs in Claude Code, Codex, Antigravity, Gemini CLI, Cursor, GitHub Copilot and other agents that read `SKILL.md`. You start with a business need at project kickoff and finish with a solution evaluation. Along the way the skills write the planning, requirements, process, impact, validation and handoff artifacts the handbook requires. Each skill reads what the previous one wrote, so you can trace any decision from business objective to delivered solution.

All BA artifacts live in `docs/ba/`. When a skill and the handbook disagree, follow the handbook.

## Install

**Claude Code and Claude apps.** Install `my-ba-flow.plugin`. Rebuild it after any change with `python tools/build_plugin.py`.

**Other agents.** Copy the skills into the folder your agent reads with `tools/install_skills.py`:

| Agent | Command | Installs to |
| --- | --- | --- |
| Codex | `python tools/install_skills.py --agent codex` | `.agents/skills/` in the current project |
| Antigravity | `python tools/install_skills.py --agent antigravity --scope user` | `~/.gemini/config/skills/`, all workspaces |
| Gemini CLI | `python tools/install_skills.py --agent gemini-cli` | `.agents/skills/` in the current project |
| Cursor | `python tools/install_skills.py --agent cursor` | `.agents/skills/` in the current project |
| GitHub Copilot / VS Code | `python tools/install_skills.py --agent copilot` | `.github/skills/` in the current project |
| Any folder | `python tools/install_skills.py --dir <folder>` | `<folder>/<skill>/` |

Add `--scope user` to install for every project on your machine, `--project <path>` to target another project, `--skill <name>` to install one skill, and `--dry-run` to see the destination first. `--list` prints every agent and its folders. The script overwrites files of skills it installs and leaves everything else in the folder alone.

Notes for non-Claude agents:

- Skills call each other by name (`fit-gap` hands over to `ba-planning`), so install the whole set.
- `demo-terpandu-fgd` needs Node.js; `us-ac-writer` needs Python. Both run the same in any agent.
- Where a skill asks a multiple-choice question, agents without such a tool ask it as plain text.

## Two work models

`ba-start` asks which model applies, shows the route and picks up where you left off.

| | Project based | Product based |
| --- | --- | --- |
| Starting point | A client need; no application yet | A finished application (built by the CEO or by the BA), handed over as a zip or rar of source code |
| First BA work | Elicit needs, then mockup, Figma or prototype | Understand the product, then demo it to a prospective client |
| Documents | BA Handbook from the start | Light format until the client proceeds |
| Meeting point | Documented client needs | `fit-gap`: client needs against the product |
| Afterwards | The Handbook pipeline below | A separate project folder per client, then the same Handbook pipeline |

The product based route runs in this order:

1. `product-onboarding`: extract and run the app, then write a product brief with rules labelled Terbukti or Asumsi and a commercial value section.
2. `discovery-meeting-prep`: session type "Product demo to a prospect". The debrief ends with a deal qualification summary.
3. `demo-terpandu-fgd`: a guided demo or FGD that opens with the value moment.
4. `fit-gap`: deal impact and gap nature per need, then an update to the product's shared file of recurring gaps.
5. `ba-planning` and `reverse-engineering` in a new project folder, once the client proceeds.

The product based path is **revenue-first**. The product earns money when the same product sells to many clients with little custom work. At each step you ask who pays, for which money problem, whether the deal is worth pursuing, and which gaps would sell again as product features. You hand that evidence to BD. You do not set or promise price, discount or timeline.

`demo-terpandu-fgd` serves both models. In product based work it demos the finished product; in project based work it demos the team's prototype.

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

### Entry points and on-ramps

- `ba-start`: asks product based or project based and routes the work.
- `discovery-meeting-prep`: use it before the first client contact. It classifies the session (new system from scratch, vendor switch or troubled project, tender aanwijzing, product demo), builds a prioritized question list and red-flag watchlist from the team question bank, and runs the debrief that feeds `ba-planning` and `stakeholder-interview`.
- `meeting-live-assist`: use it during the meeting. Paste the transcript in 5 to 10 minute chunks; you get at most three questions to ask now, plus Open Questions and Assumptions rows in the MoM template (T-04) format. It also replays saved transcripts.
- `product-discovery`: use it when you have a raw idea and no requirements. It interviews you and writes a first-draft user story, AC and sprint table for `stakeholder-interview` and `requirement-elicitation`.
- `reverse-engineering`: use it on an existing system with no documentation (Bab 4A). It recovers the As-Is, business rules and data dictionary with confidence levels, then feeds the normal pipeline.
- `product-onboarding` (product based): turns a zip or rar of a finished app into a light product brief.
- `fit-gap` (product based): compares the client's needs with the product after the demo and opens the client project.

### How the stages connect

1. `ba-planning` is the first gate. The BA Work Plan must exist before any elicitation (Rule P1-01).
2. `stakeholder-interview` maps who matters and records their pain points.
3. `requirement-elicitation` turns those into a baselined BRD and business rules.
4. `process-mapping` and `impact-analysis` both start from the BRD. Process maps show what changes; impact analysis scores risk (ISO 31000, 4x4) and logs issues.
5. `wireframe-spec` and `data-dictionary` run side by side: one sets the UI contract, the other the data contract.
6. `ba-grooming` reviews stories from the business side and runs the Phase-4 validation gate (peer review, Rule P4-01).
7. `ba-handoff` packages everything with a Bab 5.4.2 traceability matrix, Approval Authority and the DoR gate.
8. After baseline, every change goes through `change-request` (Rule P7-01). After go-live, `solution-evaluation` runs UAT sign-off and Lesson Learned (Rule P8-01).

## Rules every deliverable follows

- Outputs use the handbook's official templates in Bab 8 (T-04, T-07, T-09, T-18, T-App-BA/UIUX/Eng, T-PRD, T-FSD, T-RES), not ad-hoc formats (Rules DL-01, P3-03).
- Each deliverable carries a Revision History and version control (Rule DL-02).
- The responsible BA reviews AI-drafted content before it becomes an official deliverable, and logs the AI assistance in the Revision History (Rules AI-01, AI-03).
- Traceability runs both ways: Business Need to Requirement to Test Case (Rule R-04).

## Supporting skills

You can use these at any stage:

- `grill-with-docs`: test a plan against the project's domain language and docs before you finalize it.
- `stop-slop`: strip AI writing patterns from prose.
- `demo-terpandu-fgd`: a guided demo (Panduan Demo) or FGD (Panduan FGD FIF format) panel over a locally running app or prototype, with notes and a printable rundown.

Each skill does one job. Version 1.3.0 dropped `grill-me`, `handoff` and `caveman`: `grill-with-docs`, the app's own session handoff and plain writing rules cover them. `skill-creator/` and `write-a-skill/` stay in the repo as authoring notes; neither the plugin nor `tools/install_skills.py` ships them.

## Keeping handbook copies in sync

`us-ac-writer/references/` holds exact copies of the handbook's `Template/SysFunc_US_AC_Guide.md` and `Appendix_D_Panduan_Praktik_US_AC.md`. After the handbook changes:

1. Run `python tools/sync_handbook.py --update`. Set `BA_HANDBOOK_DIR` if the handbook is not at the default path.
2. Run `python -m pytest tests -q`.
3. Rebuild the plugin with `python tools/build_plugin.py` and reinstall it, or rerun `tools/install_skills.py` for other agents.
