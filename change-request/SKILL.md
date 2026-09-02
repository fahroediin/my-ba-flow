---
name: change-request
description: Handle a change to a baselined requirement through the formal Change Request process, producing a Change Request Form with a mandatory impact analysis and routing it for approval, and logging the change. Use after requirements are approved/baselined and something must change — the user says "we need to change a requirement", "raise a change request", "the scope changed", "CR", "the stakeholder wants something different now", or a new need appears after sign-off. Any post-baseline change must go through this (Rules P7-01, DL-04).
---

# Change Request

The Support and Change Management step of the BA pipeline (Phase 7). Once requirements are Baselined (Rule P5-01), every change must go through a formal Change Request; a change made without a CR is a governance violation (Rule P7-01). This skill produces the Change Request Form, forces the mandatory impact analysis, and records the change.

Aligned with BA Handbook Bab 4.8 (Phase 7: Support & Change Management), Bab 8 (template T-18), and Rules R-03, P7-01, P7-02, DL-04.

## When this applies

Use this only for changes to something already **approved / baselined**. If requirements are still in Draft, edit them directly through `requirement-elicitation` instead. If a conflict or defect is raised but not yet a requirement change, log it via the Issue Register in `impact-analysis`.

## Pre-flight

Read the affected artifacts under `docs/ba/`: `brd.md`, `business-rules.md`, `traceability-matrix.md`, and any user stories. Identify exactly which baselined requirements (BR / US / AC IDs) the change touches. Confirm the current baseline version.

## Artifact 1: Change Request Form (`change-requests/CR-XX.md`) — template T-18

```markdown
# Change Request Form

**CR ID:** CR-XX  
**Date:** (date)  
**Raised By:** (name / role)  
**Related Baseline:** (BRD version / sprint)  
**Status:** Draft / Under Review / Approved / Rejected / Implemented  

## Revision History
| Version | Date | Author | Change Summary | AI-Assisted |
| --- | --- | --- | --- | --- |
| 1.0 | (date) | (name) | Initial CR | Yes/No |

## 1. Change Description
(what is changing, concretely)

## 2. Reason for Change
(why: new business need, regulation, defect, corrected assumption, market shift)

## 3. Affected Requirements
| ID | Current State | Proposed State |
| --- | --- | --- |
| BR-XX / US-XX / AC-XX | (as baselined) | (after change) |

## 4. Impact Analysis (mandatory — Rule P7-02)
### Scope Impact
### Timeline Impact
### Cost Impact
### Quality Impact
### Risk Impact
(reference RISK-XX in the risk register; add new risks if the change introduces them)

## 5. Alternatives Considered
| Option | Description | Pros | Cons |
| --- | --- | --- | --- |

## 6. Recommendation
(BA's recommended option and rationale)

## 7. Approval
| Role | Name | Decision | Date | Signature |
| --- | --- | --- | --- | --- |
| BA Lead (Reviewer) | | | | |
| Change Advisory Board / Sponsor (Approver) | | | | |
```

## Mandatory rules to enforce

- **Rule P7-01:** no post-baseline change proceeds without an approved CR. State this to the user if they try to skip it.
- **Rule P7-02:** every CR must carry an Impact Analysis covering scope, timeline, cost, and quality. Do not mark a CR ready for approval with Section 4 empty.
- **Rule DL-04:** an Approved deliverable must not be edited until the CR is approved. Only after approval do you update the source artifacts.
- **Rule P5-02:** approval must be written evidence (email, digital signature, tool sign-off).

## After approval

Once the CR is approved:

1. Update every affected artifact (`brd.md`, `business-rules.md`, user stories, `traceability-matrix.md`), bumping each document's version and Revision History (Rule DL-02).
2. Increment the baseline version and note the CR ID in the changed rows of the RTM.
3. If the change affects complex logic (>3 branches), re-run the MRTM and a Three Amigos Sync before the change re-enters a sprint (DoR, Bab 4.7.1).
4. Record the CR in the CR Register.

## Artifact 2: CR Register (`change-requests/cr-register.md`)

```markdown
# Change Request Register

| CR ID | Date | Description | Affected Reqs | Decision | Approved By | Date | Baseline After |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CR-01 | (date) | (summary) | BR-XX, US-XX | Approved/Rejected | (name) | (date) | v1.1 |
```

## Output

| Artifact | Path |
| --- | --- |
| Change Request Form | `docs/ba/change-requests/CR-XX.md` |
| CR Register | `docs/ba/change-requests/cr-register.md` |

## Handoff

- Use `impact-analysis` for a deep impact/risk assessment when the change is large.
- After implementation, feed outcomes into `solution-evaluation` (BA-10) at the next Lesson Learned.

## Writing conventions (enforced in all output)

- No AI slop: no filler or hedging; every sentence informs.
- No em-dashes, no double-dashes (`--`) in prose; dashes only as Markdown syntax (list bullets, table rules) or in literal code/CLI flags (e.g. `--no-deps`).
- No emoji. Professional, declarative tone.
- Governance (Rule AI-01, AI-03): AI-drafted artifacts must be reviewed by the responsible BA before becoming official deliverables; record AI assistance in the Revision History.
- Every deliverable carries a Revision History and version control (Rule DL-02).
- If a document carries a metadata header (`**Version:**`, `**Date:**`, `**Author:**`, `**Status:**`, `**Phase:**`), each such line ends with two trailing spaces so Markdown renders them on separate lines.
