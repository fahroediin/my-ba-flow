---
name: stakeholder-interview
description: Conduct a structured stakeholder interview for a project or initiative, producing a stakeholder map (power/interest grid), interview notes, and a pain-points register. Use when the user wants to interview stakeholders, identify key players, understand who is affected by a change, map decision-makers, says "who are the stakeholders", "let's do stakeholder analysis", "help me prepare for stakeholder interviews", or needs to understand the organizational landscape before gathering requirements.
---

# Stakeholder Interview

The entry point of the BA pipeline. Before gathering requirements, a BA must understand *who* cares, *how much* they care, and *what* they need. This skill interviews the user (acting as the domain expert or project sponsor) to build a complete picture of the stakeholder landscape.

Aligned with BA Handbook Bab 4.2 (Planning & Scoping), Bab 6 (Stakeholder Management), and Rules P1-02, P2-01, P2-03.

Two phases: **interview to map the landscape, then synthesize the artifacts.**

## Phase 1 — Interview

Elicit the stakeholder landscape one question at a time, recommend an answer for each, and do not move on until the user confirms. The goal is to identify every person or group who influences, is affected by, or has authority over the project.

Cover, adapting to the project:

- **Project context.** What is the project or initiative about? What triggered it (a problem, an opportunity, a regulation)? What does the organization look like today?
- **Stakeholder identification.** Who are the people and groups involved? Walk through each organizational layer and classify each stakeholder into one of these categories (per BA Handbook Bab 6.2.1):
  - **Sponsor**: C-Level, VP, Director (approval and funding)
  - **Domain SME**: Department Head, Senior Staff (primary source of requirements)
  - **End User**: Operator, Staff (daily usage and feedback)
  - **Regulator**: Compliance Officer, Auditor (regulatory constraints)
  - **Technical**: Architect, Dev Lead, DBA (technical feasibility)
  - **Support**: Helpdesk, Trainer (transition and adoption)
  - **External**: Customer, Vendor, Partner (external requirements)
  For each stakeholder, capture: name or role title, department, and their relationship to the project.
- **Power and interest.** For each stakeholder, assess:
  - **Power**: their ability to influence the project's direction or outcome (High/Medium/Low)
  - **Interest**: how much the project affects their daily work or goals (High/Medium/Low)
  - **Attitude**: Supportive, Neutral, or Resistant to the change
  - **Engagement level**: Unaware, Resistant, Neutral, Supportive, or Committed (per Handbook Bab 6.4.2). Note the *current* level and the *desired* level; the gap drives the engagement strategy.
- **Communication needs.** For key stakeholders: preferred communication channel, frequency (Daily/Weekly/Bi-weekly/Monthly), and level of detail (executive summary vs. working-level detail).
- **Pain points.** What frustrates each stakeholder group today? What do they complain about? What workarounds do they use? These become requirement candidates later.
- **Success criteria.** How will each stakeholder group judge whether the project succeeded? Pin concrete, observable measures where possible.
- **Risks and politics.** Any known conflicts between stakeholder groups? Competing priorities? Historical context that could derail the project?
- **Assumptions.** Record every assumption that emerges during the interview. An assumption is something believed true but not yet confirmed. For each, note what risk materializes if the assumption proves false. (Rule P2-03: BA must not make assumptions without confirmation.)

Surface contradictions and coverage gaps as you go. When the picture is complete, summarize it back and confirm before writing.

Note on timing (Rule P2-01): if this skill is used during a live interview session, the resulting artifacts serve as the structured meeting minutes and must be finalized within 24 hours of the session.

## Phase 2 — Synthesize the artifacts

Turn the interview into structured documents the rest of the BA pipeline can consume.

### Artifact 1: Stakeholder Map (`stakeholder-map.md`)

A power/interest grid with every identified stakeholder placed in one of four quadrants:

```
| Quadrant | Strategy | Stakeholders |
| --- | --- | --- |
| High Power, High Interest | Manage Closely | (names/roles) |
| High Power, Low Interest | Keep Satisfied | (names/roles) |
| Low Power, High Interest | Keep Informed | (names/roles) |
| Low Power, Low Interest | Monitor | (names/roles) |
```

Below the grid, a detailed stakeholder register table (aligned with BA Handbook template T-02 and Bab 6.2.2):

```
| ID | Name/Role | Department | Category | Power | Interest | Attitude | Current Engagement | Desired Engagement | Communication Pref | Frequency | Success Criteria |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SH-01 | (name/role) | (dept) | Sponsor/Domain SME/End User/Regulator/Technical/Support/External | H/M/L | H/M/L | Supportive/Neutral/Resistant | (current level) | (desired level) | (channel) | Weekly/Bi-weekly/Monthly | (measure) |
```

### Artifact 2: Interview Notes (`interview-notes.md`)

Structured notes from the interview, organized by topic area. Each note traces back to a stakeholder ID. Include direct quotes or paraphrased statements that capture the stakeholder's voice, these become evidence for requirements later.

### Artifact 3: Pain Points Register (`pain-points-register.md`)

```
| ID | Stakeholder(s) | Pain Point | Current Workaround | Severity | Frequency | Requirement Candidate |
| --- | --- | --- | --- | --- | --- | --- |
| PP-01 | SH-01, SH-03 | (description) | (what they do today) | High/Med/Low | Daily/Weekly/Monthly | Yes/No |
```

### Artifact 4: Assumptions Log (`assumptions-log.md`)

Every assumption surfaced during the interview must be recorded (Rule P2-03). Assumptions left unconfirmed for more than 2 weeks become active risks (Rule RM-03).

```
| ID | Assumption | Raised By | Date | Status | Confirmed By | Confirmation Date | Risk if Wrong |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ASM-001 | (assumption) | (stakeholder) | (date) | Unconfirmed/Confirmed/Invalid | (name) | (date) | (consequence) |
```

## Output and handoff

Present the artifacts for the user to review and edit. Offer to save them to `docs/ba/`. When the user is happy, point them at the next step: `requirement-elicitation` to turn pain points into a formal BRD, or `process-mapping` to visualize the current and future workflows.

| Artifact | Path |
| --- | --- |
| Stakeholder Map | `docs/ba/stakeholder-map.md` |
| Interview Notes | `docs/ba/interview-notes.md` |
| Pain Points Register | `docs/ba/pain-points-register.md` |
| Assumptions Log | `docs/ba/assumptions-log.md` |

## Writing conventions (enforced in all output)

- No AI slop: no filler or hedging; every sentence informs.
- No em-dashes, no double-dashes (`--`) in prose; dashes only as Markdown syntax (list bullets, table rules) or in literal code/CLI flags (e.g. `--no-deps`).
- No emoji. Professional, declarative tone.
- If a document carries a metadata header (`**Version:**`, `**Date:**`, `**Author:**`, `**Status:**`, `**Phase:**`), each such line ends with two trailing spaces so Markdown renders them on separate lines.
