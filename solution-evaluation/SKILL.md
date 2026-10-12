---
name: solution-evaluation
description: Evaluate a delivered solution against the business need and close the project out — support UAT sign-off, analyze user feedback, report expected-vs-actual gaps, and run the Lesson Learned session. Use after go-live or at the end of a release, when the user says "did the solution meet the need", "run UAT sign-off", "gather feedback", "post-mortem", "lesson learned", "retrospective on the project", or "wrap up the project". This is the final phase of the BA lifecycle (Phase 8).
---

# Solution Evaluation

The last step of the BA pipeline (Phase 8). After the solution is built and released, the BA evaluates whether it actually met the business need, supports the UAT sign-off, and captures what was learned so the next project benefits.

Aligned with BA Handbook Bab 4.9 (Phase 8: Solution Evaluation), Bab 4.11.7 (UAT) and 4.11.8 (Lesson Learned), and Rules P8-01, P8-02, RM-05.

## Inputs

Read what exists under `docs/ba/`: `brd.md` (objectives and measures), `traceability-matrix.md`, `risk-register.md`, `impact-assessment.md`, and any user stories / MRTM. The BRD business objectives and their target measures are the yardstick for success.

## Artifact 1: UAT Support and Sign-off (`uat-signoff.md`)

Support UAT (Bab 4.11.7): prepare high-level business scenarios from the user stories, coordinate sample data and environment readiness with QA, accompany users, and triage findings with QA as **Requirement Defect** (ambiguous/incorrect requirement) vs **Implementation Defect** (build does not match a correct requirement).

```markdown
# UAT Sign-off Record

**Release:** (version)  
**Date:** (date)  

## UAT Scenarios
| Scenario | Related US / AC | Result (Pass/Fail) | Defect Type | Notes |
| --- | --- | --- | --- | --- |

## Defect Triage
| Defect | Requirement vs Implementation | Owner | Resolution |
| --- | --- | --- | --- |

## Sign-off
| Role | Name | Decision | Date | Signature |
| --- | --- | --- | --- | --- |
| Product Owner | | Accept / Reject | | |
| End-User Representative | | | | |
```

## Artifact 2: Solution Evaluation Report (`solution-evaluation.md`)

Compare expected vs actual against the BRD objectives (Bab 4.9).

```markdown
# Solution Evaluation Report

**Version:** 1.0  
**Date:** (date)  
**Author:** (BA name)  
**Status:** Draft  

## 1. Objectives vs Outcomes
| Objective (BR) | Target Measure | Actual Result | Met? | Notes |
| --- | --- | --- | --- | --- |

## 2. Feedback Analysis
(themes from user feedback, grouped and ranked by frequency and impact)

## 3. Expected vs Actual Gaps
| Gap | Expected | Actual | Severity | Recommended Action |
| --- | --- | --- | --- | --- |

## 4. Improvement Recommendations
| ID | Recommendation | Owner | Priority | Feeds Into |
| --- | --- | --- | --- | --- |
(recommendations that imply requirement changes become Change Requests; those that are new needs feed the Idea Pool)
```

## Artifact 3: Lesson Learned (`lesson-learned.md`)

Run within **2 weeks of go-live** (Rule P8-01) and store the result in the BA Knowledge Base (Rule P8-02). The report must include the risk retrospective section required by Rule RM-05.

```markdown
# Lesson Learned

**Project:** (name)  
**Date:** (date, within 2 weeks of go-live)  
**Facilitator:** (BA name)  

## What Went Well
## What Did Not Go Well
## Root Causes

## Risiko yang Terjadi vs Risiko yang Dimitigasi (Rule RM-05)
| Risk (from register) | Materialized? | Mitigation Worked? | Lesson |
| --- | --- | --- | --- |

## BA Process Review (Bab 4.11.6)
- Were any requirements missed during the project?
- Did any requirement change after baseline without a CR?
- Was there BA-Dev or BA-QA miscommunication?
- Were defects caused by ambiguous requirements?
- Were handbook rules followed consistently?

## Actions for Next Project
| Action | Owner | Due |
| --- | --- | --- |

## Knowledge Base
(link where this is stored — Rule P8-02)
```

## Output

| Artifact | Path |
| --- | --- |
| UAT sign-off | `docs/ba/uat-signoff.md` |
| Solution evaluation | `docs/ba/solution-evaluation.md` |
| Lesson learned | `docs/ba/lesson-learned.md` |

## Handoff

- Improvement recommendations that change baselined requirements go through `change-request`.
- New needs that are out of this release feed the stakeholder Idea Pool for prioritization (Bab 13).

## Writing conventions (enforced in all output)

- No AI slop: no filler or hedging; every sentence informs.
- No em-dashes, no double-dashes (`--`) in prose; dashes only as Markdown syntax (list bullets, table rules) or in literal code/CLI flags (e.g. `--no-deps`).
- No emoji. Professional, declarative tone.
- Governance (Rule AI-01, AI-03): AI-drafted artifacts must be reviewed by the responsible BA before becoming official deliverables; record AI assistance in the Revision History.
- Every deliverable carries a Revision History and version control (Rule DL-02).
- If a document carries a metadata header (`**Version:**`, `**Date:**`, `**Author:**`, `**Status:**`, `**Phase:**`), each such line ends with two trailing spaces so Markdown renders them on separate lines.
