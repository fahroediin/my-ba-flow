---
name: ba-handoff
description: Compile all BA artifacts into a structured handoff package for the engineering team, including a traceability matrix (requirement to user story to AC to screen), an open questions log, and a sign-off checklist. Use when the user wants to hand off requirements to engineering, says "package this for the dev team", "we're ready for handoff", "create the handoff document", "traceability matrix", or needs to ensure nothing is lost in the transition from analysis to implementation.
---

# BA Handoff

The final step in the BA pipeline. Compiles all BA artifacts into a single package that engineering can consume, verifies completeness and consistency, and produces the traceability matrix that proves every requirement has a path to delivery.

Aligned with BA Handbook Bab 4.6 (Approval), Bab 4.7 (Handoff), Bab 4.11.3 (Three Amigos), and Rules P5-02, P6-01, P6-03.

Three deliverables: **handoff package, traceability matrix, and sign-off checklist.**

## Pre-flight check

Before building the handoff, read every BA artifact that exists under `docs/ba/` and assess completeness:

| Artifact | Path | Status |
| --- | --- | --- |
| Stakeholder map | `docs/ba/stakeholder-map.md` | Found / Missing |
| Interview notes | `docs/ba/interview-notes.md` | Found / Missing |
| Pain points register | `docs/ba/pain-points-register.md` | Found / Missing |
| BRD | `docs/ba/brd.md` | Found / Missing |
| Business rules | `docs/ba/business-rules.md` | Found / Missing |
| AS-IS process map | `docs/ba/process-map-as-is.md` | Found / Missing |
| TO-BE process map | `docs/ba/process-map-to-be.md` | Found / Missing |
| Gap analysis | `docs/ba/gap-analysis.md` | Found / Missing |
| Impact assessment | `docs/ba/impact-assessment.md` | Found / Missing |
| Risk register | `docs/ba/risk-register.md` | Found / Missing |
| Change readiness | `docs/ba/change-readiness.md` | Found / Missing |
| Screen inventory | `docs/ba/screen-inventory.md` | Found / Missing |
| Navigation flow | `docs/ba/navigation-flow.md` | Found / Missing |
| Field specs | `docs/ba/field-specs/*.md` | Found / Missing |
| Data dictionary | `docs/ba/data-dictionary.md` | Found / Missing |
| Glossary | `docs/ba/glossary.md` | Found / Missing |
| Data lineage | `docs/ba/data-lineage.md` | Found / Missing |
| Assumptions log | `docs/ba/assumptions-log.md` | Found / Missing |

Also check `docs/business/` for any user stories and AC that already exist.

### MRTM pre-flight (Bab 14)

For every story with more than 3 logic branches: verify that an MRTM table exists and every row has a non-empty Expected Result. Stories without MRTM coverage for complex logic are flagged as Not Ready.

Report what is found and what is missing. Not every artifact is required for every project, but flag significant gaps (e.g. no BRD, no process maps) and ask the user whether to proceed or fill them first.

## Artifact 1: Handoff Package (`handoff-package.md`)

A structured summary document for the engineering team. Not a copy of every artifact, but a navigational guide with key decisions and pointers.

```markdown
# BA Handoff Package

**Version:** 1.0  
**Date:** (date)  
**Author:** (BA name)  
**Status:** Ready for Engineering Review  

## 1. Project Summary

(2-3 paragraphs: the problem, the solution, the scope, the key stakeholders)

## 2. Key Business Decisions

| Decision | Rationale | Decided By | Date | Artifact |
| --- | --- | --- | --- | --- |
| (decision) | (why) | (stakeholder) | (when) | (link to source) |

## 3. Scope Summary

### In Scope
(bullet list of what is being built, traced to BR-XX)

### Out of Scope
(bullet list of what is explicitly excluded)

### Deferred
(bullet list of what is planned for future phases)

## 4. Artifact Index

| Artifact | Path | Description | Status |
| --- | --- | --- | --- |
| (name) | (path) | (one-line description) | Complete / Draft / Missing |

## 5. Known Risks and Mitigations

(Top 5 risks from the risk register, with current mitigation status)

## 6. Open Questions

| ID | Question | Context | Impact if Unresolved | Owner | Due |
| --- | --- | --- | --- | --- | --- |
| OQ-01 | (question) | (why it matters) | (what breaks) | (who answers) | (deadline) |

## 7. Assumptions

(Assumptions that engineering should be aware of; any that prove false require re-analysis)

## 8. Recommended Next Steps

1. Hold a **Requirement Walkthrough** session (Rule P6-01): BA presents the handoff package to engineering, walking through key decisions, process maps, and complex business rules
2. For complex stories, conduct a **Three Amigos Sync** (BA + QA + Dev, max 15 minutes per story) to align on MRTM logic and expected behavior (Bab 4.11.3)
3. Engineering reviews this package and the linked artifacts
4. Engineering designs the solution architecture and plans sprints
```

## Artifact 2: Traceability Matrix (`traceability-matrix.md`)

The proof that every business requirement has a path to delivery, and every deliverable traces back to a requirement.

```markdown
# Requirements Traceability Matrix

| BR ID | Requirement | US ID | User Story | AC IDs | Screen(s) | Process Step | Test Approach | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BR-01 | (requirement text) | US-01 | (story text) | AC-01.01, AC-01.02 | SCR-01, SCR-02 | TO-BE step 3 | (UAT scenario) | Mapped / Partial / Unmapped |
```

Flag three failure modes:
- **Unmapped requirements**: BR-XX exists but no US covers it (missing story)
- **Untraceable stories**: US-XX exists but traces to no BR (scope creep or undocumented requirement)
- **Missing test coverage**: an AC exists but has no UAT scenario

## Artifact 3: Sign-off Checklist (`sign-off-checklist.md`)

```markdown
# BA Handoff Sign-off Checklist

## Business Sign-off

| # | Check | Status | Signed By | Date |
| --- | --- | --- | --- | --- |
| 1 | All business requirements documented and prioritized | [ ] | | |
| 2 | User stories cover all in-scope requirements | [ ] | | |
| 3 | Acceptance criteria are testable by business users | [ ] | | |
| 4 | Process maps reviewed and approved by process owners | [ ] | | |
| 5 | Data dictionary reviewed by data owners | [ ] | | |
| 6 | Risk register reviewed by project sponsor | [ ] | | |
| 7 | Open questions assigned and time-boxed | [ ] | | |
| 8 | Screen specifications reviewed by end-user representatives | [ ] | | |
| 9 | Business rules validated by subject matter experts | [ ] | | |
| 10 | Traceability matrix shows full coverage | [ ] | | |

## Engineering Readiness

| # | Check | Status | Notes |
| --- | --- | --- | --- |
| 1 | Engineering team has read the handoff package | [ ] | |
| 2 | Engineering review of handoff package completed | [ ] | |
| 3 | Open questions that block architecture are escalated | [ ] | |
| 4 | Data dictionary sufficient for schema design | [ ] | |
| 5 | Business rules clear enough for implementation | [ ] | |

## Definition of Ready Compliance (Bab 4.7.1)

Every story in the handoff must pass the DoR gate before entering a sprint (Rule P6-03):

| # | DoR Criterion | Status | Notes |
| --- | --- | --- | --- |
| 1 | US in standard format with unique ID | [ ] | |
| 2 | AC complete (Given-When-Then, max 1 THEN per AC) | [ ] | |
| 3 | MRTM prepared for features with >3 logic branches | [ ] | |
| 4 | Story Mindmap available for complex features | [ ] | |
| 5 | Process Model (BPMN / Mermaid) available | [ ] | |
| 6 | QA validated logic (status: Pass) | [ ] | |
| 7 | Three Amigos Sync completed (BA + QA + Dev) | [ ] | |
| 8 | Sample Data Requirements identified | [ ] | |
| 9 | No open logic gaps (MRTM Expected Results all filled) | [ ] | |
| 10 | Peer review completed (min. 1 reviewer) | [ ] | |
```

## Output

| Artifact | Path |
| --- | --- |
| Handoff package | `docs/ba/handoff-package.md` |
| Traceability matrix | `docs/ba/traceability-matrix.md` |
| Sign-off checklist | `docs/ba/sign-off-checklist.md` |

## Downstream Usage

The handoff package is designed to be fully ready for the engineering team:

- **User stories and AC** in `docs/business/` serve as the source of truth for developer task breakdown and QA test cases.
- **Data dictionary** provides the exact domain terminology and data relationships for database schema design.
- **Business rules** guide developers on backend validations, calculations, and exceptions.
- **Screen specs** guide frontend developers and UI/UX designers on layout, fields, transitions, and states.
- **Risk register** feeds into project management, risk tracking, and release planning.
- **Glossary** establishes the ubiquitous language (Domain-Driven Design) for the entire product and codebase.

If the user has not yet created `docs/business/` artifacts (user stories, AC), offer to run `product-discovery` to generate them from the BRD and the pain points register.

## Writing conventions (enforced in all output)

- No AI slop: no filler or hedging; every sentence informs.
- No em-dashes, no double-dashes (`--`) in prose; dashes only as Markdown syntax (list bullets, table rules) or in literal code/CLI flags (e.g. `--no-deps`).
- No emoji. Professional, declarative tone.
- If a document carries a metadata header (`**Version:**`, `**Date:**`, `**Author:**`, `**Status:**`, `**Phase:**`), each such line ends with two trailing spaces so Markdown renders them on separate lines.
