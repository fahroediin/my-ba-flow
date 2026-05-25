# Claude Code Skills — Business Analyst Pipeline

Personal skill library for Claude Code. This repository contains a **business
analyst pipeline** that takes a raw business need from stakeholder interviews all
the way to a structured handoff package ready for engineering consumption. Each
stage is a skill that reads the artifacts produced by the previous stage and
writes the next one, so the project documentation stays consistent and every
decision is traceable from business objective to final handoff deliverable.

## The business analyst pipeline

The BA pipeline takes a raw project idea or business need and produces the
structured requirements, process maps, and specifications that an engineering
team can consume. All BA artifacts live in `docs/ba/`.

| Step | Stage | Skill | Produces |
| ---- | ----- | ----- | -------- |
| BA-0 | Discover (optional) | `product-discovery` | The step-1 requirements table, elicited by interview, when no user stories or AC exist yet |
| BA-1 | Stakeholder interview | `stakeholder-interview` | `docs/ba/stakeholder-map.md`, `interview-notes.md`, `pain-points-register.md` |
| BA-2 | Requirement elicitation | `requirement-elicitation` | `docs/ba/brd.md`, `business-rules.md` |
| BA-3 | Process mapping | `process-mapping` | `docs/ba/process-map-as-is.md`, `process-map-to-be.md`, `gap-analysis.md` |
| BA-4 | Impact analysis | `impact-analysis` | `docs/ba/impact-assessment.md`, `risk-register.md`, `change-readiness.md` |
| BA-5 | BA grooming | `ba-grooming` | Business-perspective review of user stories: value clarity, persona accuracy, testability by business users |
| BA-6 | Wireframe spec | `wireframe-spec` | `docs/ba/screen-inventory.md`, `navigation-flow.md`, `field-specs/*.md` |
| BA-7 | Data dictionary | `data-dictionary` | `docs/ba/data-dictionary.md`, `glossary.md`, `data-lineage.md` |
| BA-8 | BA handoff | `ba-handoff` | `docs/ba/handoff-package.md`, `traceability-matrix.md`, `sign-off-checklist.md` |

### How the BA stages connect

- `product-discovery` (BA-0) is the optional on-ramp when no requirements exist
  yet: it interviews stakeholders and emits a requirements table that
  `stakeholder-interview` and `requirement-elicitation` can build on.
- `stakeholder-interview` (BA-1) is the primary entry point: it maps the
  stakeholder landscape and surfaces pain points that `requirement-elicitation`
  formalizes.
- `requirement-elicitation` (BA-2) produces the BRD that drives everything
  downstream: process maps, impact analysis, screen specs, and data dictionary
  all trace back to business requirements.
- `process-mapping` (BA-3) and `impact-analysis` (BA-4) can run in parallel
  after the BRD exists. Process maps show what changes; impact analysis shows
  what the change costs.
- `ba-grooming` (BA-5) reviews user stories from the business perspective,
  ensuring value clarity and testability before handoff.
- `wireframe-spec` (BA-6) and `data-dictionary` (BA-7) can run in parallel.
  Screen specs define the UI contract; the data dictionary defines the data
  contract.
- `ba-handoff` (BA-8) compiles everything into a package the engineering team
  can consume, with a traceability matrix proving coverage.

## Supporting skills

General-purpose skills that assist the pipeline at any stage:

- `grill-me`, `grill-with-docs`: stress-test a plan or design before finalizing.
- `stop-slop`: remove AI writing patterns from prose.
- `handoff`, `caveman`.
- `skill-creator`, `write-a-skill`: create and extend skills for the pipeline.
