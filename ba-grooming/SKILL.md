---
name: ba-grooming
description: Review user stories and acceptance criteria from the Business Analyst's perspective, focusing on business value clarity, persona accuracy, testability by business users, and traceability to business requirements. Use when the user wants a BA review of stories, says "review these stories from a business perspective", "are these stories ready for the business", "check the business value", "validate the AC from the user's perspective", or needs to ensure stories are complete before handing off to engineering.
---

# BA Grooming

The fifth step in the BA pipeline. This skill reviews stories from the **business perspective**: does the story deliver clear value, is the persona right, can a business user validate the acceptance criteria, and do the stories trace back to documented requirements?

Aligned with BA Handbook Bab 4.5 (Design & Validation), Bab 4.7.1 (DoR), Bab 5.3.4 (AC Testability), Bab 14 (MRTM), and Rules P3-01, P4-01, RE-04, P6-03.

This skill asks "should we build this, and will the business know it's done?"

## What to do

The user gives you one or more user stories and their acceptance criteria. Review them through the BA lens, producing questions for the product owner or stakeholders and concrete suggestions for improvement.

### BA Review Lens

For each user story, evaluate against these criteria:

#### Business Value

- Is the business value statement specific and measurable, or is it vague ("so that I can be more efficient")?
- Can the stated value be traced to a business objective in the BRD (`docs/ba/brd.md`) or to a documented pain point (`docs/ba/pain-points-register.md`)?
- Is this the most valuable slice, or is value buried inside a larger story that should be split?
- Will a stakeholder recognize this value when they see the delivered feature?

#### Persona Accuracy

- Is the persona a real user role from the stakeholder map, or a made-up abstraction?
- Does this persona actually perform this action in the real workflow (reference `docs/ba/process-map-to-be.md` if available)?
- Are there other personas who need the same capability but with different permissions or views?
- Is the persona too broad ("as a user") or too narrow ("as a senior regional manager in Jakarta")?

#### Acceptance Criteria Quality (Business Perspective)

- Can a business user (not a developer) read this AC and determine whether it passes or fails?
- Does the AC describe observable behavior, not implementation details?
- **Rule P3-01**: does each AC have exactly **one THEN clause**? If there are multiple outcomes in a single AC, flag it for splitting.
- Are the unhappy paths covered from the user's perspective? (What does the user see when something goes wrong, not what the system does internally.)
- Are boundary values stated in business terms? ("maximum 50 items per order" not "array length <= 50")
- Is the AC testable with a manual walkthrough by a business user during UAT?

#### AC Testability (Rule RE-04, Bab 5.3.4)

- Does each AC include explicit **boundary values** (minimum, maximum) so QA can apply Boundary Value Analysis?
- Are **valid and invalid input ranges** clearly defined so QA can apply Equivalence Partitioning?
- Is the **expected result** for each condition definitive (not "shows an appropriate message" but "shows message: 'Saldo tidak mencukupi'")?
- Are **edge cases** considered (empty input, zero values, maximum length, concurrent access)?

#### MRTM Readiness (Bab 14)

- Does the story involve more than **3 input variables or decision branches**?
- If yes: AC must not be written as narrative prose. Flag that the AC should be converted to a tabular **MRTM (Master Requirement and Test Matrix)** and referenced as: *"Refer to MRTM rows TRM_XXX_001 through TRM_XXX_NNN."*
- If an MRTM already exists, verify that every row has a non-empty Expected Result column (no logic gaps).

#### Traceability

- Does every story trace to at least one business requirement (BR-XX) or pain point (PP-XX)?
- Are there documented requirements that no story covers (missing stories)?
- Are there stories that don't trace to any documented requirement (scope creep)?

#### Process Alignment

- Does the story's workflow match the TO-BE process map?
- Are there steps in the process map that no story covers?
- Does the story skip steps or combine steps that the process map separates?

### Requirements Validation (Bab 4.5)

Beyond the business-value lens, run each requirement and story through the BA Handbook Phase 4 validation checklist (Bab 4.5). This is the formal validation gate before stakeholder sign-off. Mark each criterion PASS / FAIL:

- [ ] **Complete** — no missing information
- [ ] **Consistent** — no conflict with another requirement
- [ ] **Correct** — accurately reflects the stakeholder need
- [ ] **Feasible** — technically implementable
- [ ] **Modifiable** — can change without excessive impact
- [ ] **Unambiguous** — exactly one interpretation
- [ ] **Testable** — verifiable through testing
- [ ] **Traceable** — traces to a business need
- [ ] **Verifiable** — implementation can be proven

**Rule P4-01:** every requirements document must pass at least one peer review by another BA before it is presented to stakeholders. Record the reviewer and date. **Rule P4-02:** requirements not yet validated by the stakeholder must not be treated as "approved" or handed off to development.

Record the validation and peer-review results as a **Review Checklist (T-15)** at `docs/ba/review-checklist.md` so Phase 4 has its mandated deliverable.

### Output Structure

#### 1. Business Review Questions

Group questions under these headings. For each question, note why it matters to the business:

- **Value and priority**: Is this worth building now?
- **Persona and workflow**: Does this match how the business actually works?
- **Completeness**: What is missing from the business perspective?
- **Testability**: Can the business validate this?

#### 2. Readiness Verdict

- **Business Readiness Checklist**: each criterion marked PASS / WARN / FAIL
  - Business value is specific and traceable
  - Persona matches a documented stakeholder role
  - AC are testable by a business user
  - Each AC has exactly one THEN clause (Rule P3-01)
  - Boundary values and edge cases are explicit (Rule RE-04)
  - MRTM exists for stories with >3 decision branches (Bab 14)
  - Unhappy paths cover user-facing scenarios
  - Story traces to a documented requirement
  - Story aligns with TO-BE process
- **Ready / Not ready for engineering handoff**: with the single biggest gap if not ready.

#### 3. DoR Pre-check (Bab 4.7.1)

For each story, run through the **Definition of Ready** checklist from the BA Handbook. Mark each item PASS / FAIL:

| # | DoR Criterion | Status |
| --- | --- | --- |
| 1 | User Story written in standard format (As a / I want / So that) with unique ID | |
| 2 | Acceptance Criteria complete (Given-When-Then, max 1 THEN per AC) | |
| 3 | MRTM prepared for features with >3 logic branches | |
| 4 | Story Mindmap available for complex features | |
| 5 | Process Model (BPMN / Mermaid) available for main business flows | |
| 6 | QA has validated logic and given status "Pass" | |
| 7 | Three Amigos Sync completed (BA + QA + Dev, max 15 min) | |
| 8 | Sample Data Requirements identified | |
| 9 | No open logic gaps (all Expected Results in MRTM filled) | |
| 10 | Peer review of requirement document completed (min. 1 reviewer) | |

Stories that do not pass all DoR criteria must not enter a sprint (Rule P6-03).

#### 4. Suggestions

Three change types to structure the feedback:

- **Add**: missing stories or AC the business needs (gaps in requirement coverage, missing personas, missing unhappy paths from the user's perspective)
- **Remove**: stories or AC that are out of scope per the BRD, duplicated, or untestable by business users
- **Edit**: reword to make business value concrete, AC testable by business users, or personas accurate

Rules:
- Match the project's existing US/AC format and IDs.
- Show the change concretely: write out the proposed text, not just "clarify this".
- Tie each suggestion to the review criterion that exposed it.
- These are proposals, not edits you apply. Only write changes into source docs if the user explicitly asks.

## Handoff

When the user is satisfied with the review:
- If stories need business-side fixes: the user edits them, then re-runs `ba-grooming`
- If stories are business-ready: proceed to `wireframe-spec` (BA-6) or `ba-handoff` (BA-8)

## Writing conventions (enforced in all output)

- No AI slop: no filler or hedging; every sentence informs.
- No em-dashes, no double-dashes (`--`) in prose; dashes only as Markdown syntax (list bullets, table rules) or in literal code/CLI flags (e.g. `--no-deps`).
- No emoji. Professional, declarative tone.
- - If a document carries a metadata header (`**Version:**`, `**Date:**`, `**Author:**`, `**Status:**`, `**Phase:**`), each such line ends with two trailing spaces so Markdown renders them on separate lines.
