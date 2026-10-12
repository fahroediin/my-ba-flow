---
name: impact-analysis
description: Analyze the impact of a proposed change on systems, processes, people, and data, then quantify risk and issues using the BA Handbook's ISO 31000 model, producing an impact assessment matrix, a risk register (4x4 numeric scoring), an issue register, and a change readiness scorecard. Use when the user wants to understand what a change will affect, assess risks, evaluate readiness, says "what's the impact", "what could go wrong", "are we ready for this change", "risk assessment", or needs to present a structured impact case to stakeholders before committing to a project.
---

# Impact Analysis

The fourth step in the BA pipeline. Before a project proceeds, the BA must answer: what does this change break, who does it affect, and is the organization ready? This skill makes the blast radius of a change explicit and quantified so stakeholders can make informed go/no-go decisions.

Aligned with BA Handbook Bab 7 (Mitigasi Risiko & Manajemen Isu, ISO 31000:2018), Bab 4.8 (Phase 7: Support & Change Management), and Rules RM-01, RM-02, RM-03, RM-04, RM-06, SM-01.

Two phases: **assess impact across dimensions, then synthesize the risk, issue, and readiness picture.**

## Phase 1 — Impact Assessment

Read existing artifacts: `docs/ba/brd.md`, `docs/ba/gap-analysis.md`, `docs/ba/stakeholder-map.md`, `docs/ba/process-map-as-is.md`, `docs/ba/process-map-to-be.md` if they exist. Use the gap analysis as the primary driver: each gap implies an impact.

Interview the user to assess impact across four dimensions. For each dimension, walk through every affected area one at a time.

### 1. Process Impact

For each business process that changes:

- What changes in the workflow? (reference the gap analysis)
- Which roles are affected and how?
- What training or documentation is needed?
- What happens during the transition period (dual-run, phased rollout, big bang)?
- What is the rollback plan if the new process fails?

### 2. System/Technology Impact

For each system or tool that is introduced, modified, or retired:

- What integrations does this system have today?
- What data flows through it?
- What downstream systems depend on its output?
- What is the migration path for existing data?
- What is the expected downtime during cutover?

If a codebase is available, explore it to identify integration points, shared data stores, and API contracts that the change touches.

### 3. People/Organization Impact

For each stakeholder group:

- How does their daily workflow change?
- What new skills do they need?
- How many people are affected?
- What is their likely reaction (reference attitude from stakeholder map)?
- What change management activities are needed (training, communication, support)?

### 4. Data Impact

For each data entity that is created, modified, migrated, or retired:

- What is the current data volume?
- What is the data quality today (complete, accurate, timely)?
- What transformation is needed?
- What is the data migration strategy?
- What validation will confirm the migration succeeded?
- Are there regulatory or compliance implications (data retention, privacy, audit trail)?

## Phase 2 — Synthesize

### Artifact 1: Impact Assessment Matrix (`impact-assessment.md`)

```markdown
# Impact Assessment

**Version:** 1.0  
**Date:** (date)  
**Author:** (BA name)  
**Status:** Draft  

## Impact Matrix

| ID | Area | Dimension | Description | Severity | Stakeholders Affected | Mitigation | Related Gap |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IMP-01 | (area) | Process/System/People/Data | (what changes) | High/Med/Low | SH-XX, SH-YY | (action) | GAP-XX |

## Transition Plan Considerations

### Phasing Strategy
(recommended approach: big bang vs phased vs parallel run, with rationale)

### Critical Path Items
(impacts that must be resolved before go-live, sequenced)

### Rollback Triggers
(conditions under which the change should be reversed)
```

### Artifact 2: Risk Register (`risk-register.md`)

Use the BA Handbook risk model exactly (Bab 7.5). Probability and Impact are scored on a **1-4 numeric scale**, and the Risk Score is their product (range 1-16). Do not use a 3-level High/Med/Low product; the numeric score drives the response and escalation thresholds below.

**Probability scale (Bab 7.5.1):** 1 = Sangat Rendah, 2 = Rendah, 3 = Sedang, 4 = Tinggi.
**Impact scale:** 1 = Rendah, 2 = Sedang, 3 = Tinggi, 4 = Kritis.

**Risk category (Bab 7.4.1) — use these codes:**
- **RQ** Requirement Quality (ambiguous/incomplete/untestable requirements, gold plating, missing NFR)
- **SK** Stakeholder (key stakeholder unavailable, disengaged, changing, political conflict)
- **PR** Process (scope creep without CR, bypassed approval, inconsistent docs, knowledge loss)
- **CM** Communication (BA-Dev miscommunication, lost in translation, uneven information)
- **TC** Technical (infeasible requirement, complex integration, complex data migration)

```markdown
# Risk Register

**Version:** 1.0  
**Date:** (date)  
**Author:** (BA name)  
**Status:** Draft  

| ID | Risk | Category | Probability (1-4) | Impact (1-4) | Score (PxI) | Level | Owner | Mitigation | Contingency | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RISK-01 | (event) | RQ/SK/PR/CM/TC | 3 | 4 | 12 | Critical | SH-XX | (preventive action) | (reactive action) | Open |
```

**Score to Level, Response, and Escalation (Bab 7.5.2):**

| Level | Score | Response | Escalation |
| --- | --- | --- | --- |
| Low | 1-3 | Accept & Monitor | None |
| Medium | 4-6 | Mitigate — build an action plan | BA Lead |
| High | 8-9 | Mitigate aggressively — prioritize action | Head of BA + PM |
| Critical | 12-16 | Immediate action — escalate to Steering Committee | Steering Committee |

Rules to enforce while producing and maintaining this register:
- **Rule RM-01:** the Risk Register must be updated at least every 2 weeks (or every sprint in Agile).
- **Rule RM-02:** Critical and High risks must be escalated without delay — no Critical risk may sit without an action plan for more than 24 hours, no High risk for more than 3 working days.
- **Rule RM-03:** every unconfirmed assumption older than 2 weeks becomes an active risk; pull open items from `docs/ba/assumptions-log.md` and add them here.
- **Rule RM-04:** a risk review is mandatory in every sprint retrospective or status meeting.

### Artifact 3: Issue Register (`issue-register.md`)

An **issue** is an event that has **already happened** and needs resolution (Bab 7.2), as opposed to a risk (which might happen). Every requirement conflict surfaced during analysis must be logged here (Rule SM-01). Use the handbook Issue Register template (Bab 7.7.2) and severity SLAs (Bab 7.7.3).

```markdown
# Issue Register

| Issue ID | Date | Description | Category | Severity | PIC | Target Date | Status | Resolution |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ISS-01 | (date) | (description) | Req Quality / Stakeholder / Process / Comm / Technical | Critical/High/Med/Low | SH-XX | (date) | Open/In Progress/Resolved/Closed | (resolution) |
```

**Severity SLA (Bab 7.7.3):**

| Severity | Definition | Resolution SLA |
| --- | --- | --- |
| Critical | Halts overall progress | 24 hours |
| High | Significantly blocks progress | 3 working days |
| Medium | Disrupts progress | 5 working days |
| Low | Minor, does not block progress | 10 working days |

**Rule RM-06:** any issue that passes its SLA without progress must be escalated automatically to the next level.

### Artifact 4: Change Readiness Scorecard (`change-readiness.md`)

Supplementary to the handbook (not a mandated template): a fast go/no-go readiness view for the sponsor. Assess readiness across five dimensions, each scored 1-5:

```markdown
# Change Readiness Scorecard

| Dimension | Score (1-5) | Evidence | Gaps | Actions Needed |
| --- | --- | --- | --- | --- |
| Leadership Sponsorship | | (what supports this score) | | |
| Stakeholder Alignment | | | | |
| Process Readiness | | | | |
| Technical Readiness | | | | |
| People Readiness | | | | |

**Overall Readiness: X/25**

## Readiness Verdict

- 20-25: Ready to proceed
- 15-19: Proceed with targeted interventions
- 10-14: Significant gaps; address before proceeding
- Below 10: Not ready; major intervention needed
```

## Output

Write to `docs/ba/`:

| Artifact | Path |
| --- | --- |
| Impact assessment | `docs/ba/impact-assessment.md` |
| Risk register | `docs/ba/risk-register.md` |
| Issue register | `docs/ba/issue-register.md` |
| Change readiness | `docs/ba/change-readiness.md` |

## Handoff

When the user is satisfied, point them at:
- `ba-grooming` to ensure user stories account for the risks and impacts identified
- `ba-handoff` to compile the full picture for engineering
- `change-request` (BA-9) when any of these impacts or risks later triggers a change to a baselined requirement

## Writing conventions (enforced in all output)

- No AI slop: no filler or hedging; every sentence informs.
- No em-dashes, no double-dashes (`--`) in prose; dashes only as Markdown syntax (list bullets, table rules) or in literal code/CLI flags (e.g. `--no-deps`).
- No emoji. Professional, declarative tone.
- Governance (Rule AI-01, AI-03): every artifact this skill drafts is AI-generated and must be reviewed by the responsible BA before it becomes an official deliverable; record that AI assisted in the document's Revision History.
- Every deliverable carries a Revision History and version control (Rule DL-02).
- If a document carries a metadata header (`**Version:**`, `**Date:**`, `**Author:**`, `**Status:**`, `**Phase:**`), each such line ends with two trailing spaces so Markdown renders them on separate lines.
