---
name: ba-grooming
description: Review user stories and acceptance criteria from the Business Analyst's perspective, focusing on business value clarity, persona accuracy, testability by business users, and traceability to business requirements. Use when the user wants a BA review of stories, says "review these stories from a business perspective", "are these stories ready for the business", "check the business value", "validate the AC from the user's perspective", or needs to ensure stories are complete before handing off to engineering.
---

# BA Grooming

The fifth step in the BA pipeline. This skill reviews stories from the **business perspective**: does the story deliver clear value, is the persona right, can a business user validate the acceptance criteria, and do the stories trace back to documented requirements?

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
- Are the unhappy paths covered from the user's perspective? (What does the user see when something goes wrong, not what the system does internally.)
- Are boundary values stated in business terms? ("maximum 50 items per order" not "array length <= 50")
- Is the AC testable with a manual walkthrough by a business user during UAT?

#### Traceability

- Does every story trace to at least one business requirement (BR-XX) or pain point (PP-XX)?
- Are there documented requirements that no story covers (missing stories)?
- Are there stories that don't trace to any documented requirement (scope creep)?

#### Process Alignment

- Does the story's workflow match the TO-BE process map?
- Are there steps in the process map that no story covers?
- Does the story skip steps or combine steps that the process map separates?

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
  - Unhappy paths cover user-facing scenarios
  - Story traces to a documented requirement
  - Story aligns with TO-BE process
- **Ready / Not ready for engineering handoff**: with the single biggest gap if not ready.

#### 3. Suggestions

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
- If a document carries a metadata header (`**Version:**`, `**Date:**`, `**Author:**`, `**Status:**`, `**Phase:**`), each such line ends with two trailing spaces so Markdown renders them on separate lines.
