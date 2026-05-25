---
name: impact-analysis
description: Analyze the impact of a proposed change on systems, processes, people, and data, producing an impact assessment matrix, a risk register, and a change readiness scorecard. Use when the user wants to understand what a change will affect, assess risks, evaluate readiness, says "what's the impact", "what could go wrong", "are we ready for this change", "risk assessment", or needs to present a structured impact case to stakeholders before committing to a project.
---

# Impact Analysis

The fourth step in the BA pipeline. Before a project proceeds, the BA must answer: what does this change break, who does it affect, and is the organization ready? This skill makes the blast radius of a change explicit and quantified so stakeholders can make informed go/no-go decisions.

Two phases: **assess impact across dimensions, then synthesize the risk and readiness picture.**

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

```markdown
# Risk Register

| ID | Risk | Category | Probability | Impact | Score | Owner | Mitigation | Contingency | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RISK-01 | (event) | Process/Tech/People/Data/External | High/Med/Low | High/Med/Low | (P x I) | SH-XX | (preventive action) | (reactive action) | Open |
```

Scoring guide:
- High x High = Critical (must mitigate before proceeding)
- High x Med or Med x High = Significant (mitigation plan required)
- Med x Med = Moderate (monitor with planned response)
- Low x any = Low (accept with monitoring)

### Artifact 3: Change Readiness Scorecard (`change-readiness.md`)

Assess readiness across five dimensions, each scored 1-5:

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
| Change readiness | `docs/ba/change-readiness.md` |

## Handoff

When the user is satisfied, point them at:
- `ba-grooming` to ensure user stories account for the risks and impacts identified
- `ba-handoff` to compile the full picture for engineering

## Writing conventions (enforced in all output)

- No AI slop: no filler or hedging; every sentence informs.
- No em-dashes, no double-dashes (`--`) in prose; dashes only as Markdown syntax (list bullets, table rules) or in literal code/CLI flags (e.g. `--no-deps`).
- No emoji. Professional, declarative tone.
- If a document carries a metadata header (`**Version:**`, `**Date:**`, `**Author:**`, `**Status:**`, `**Phase:**`), each such line ends with two trailing spaces so Markdown renders them on separate lines.
