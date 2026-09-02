---
name: reverse-engineering
description: Recover requirements from an existing, running system that lacks documentation — reconstruct the As-Is model, business rules, and data dictionary from source code, database, UI, logs, and SMEs, each tagged with a confidence level. Use when the user must modernize, replace, or enhance a legacy system and says "there's no documentation", "reverse engineer this system", "recover the requirements", "document what this app already does", or "we don't know how the old system works". Read-only activity; never changes the target system.
---

# Reverse Engineering and Requirements Recovery

An optional, parallel on-ramp to the BA pipeline for existing systems. Instead of eliciting requirements from scratch, it works backward from a running solution to reconstruct the requirements that underlie it, then feeds the recovered As-Is into the normal pipeline (process mapping, requirement elicitation).

Aligned with BA Handbook Bab 4A (Reverse Engineering & Requirements Recovery), and Rules RE-01 through RE-08 (Bab 4A). Note: RE-01..RE-08 in Bab 4A are the Reverse Engineering rules, distinct from the Requirements Engineering rules of the same code in Bab 5.

## When to use (Bab 4A.3)

Triggers: modernization or replacement of a legacy system, missing or outdated documentation, onboarding onto an unfamiliar system, or an enhancement whose current behavior nobody can fully describe. If a system does not yet exist, use `ba-planning` and `stakeholder-interview` instead.

> **Rule RE-04 (Bab 4A):** reverse engineering is strictly **read-only**. Never change the production system or database during RE. Use a staging or sandbox environment for any testing.

## The RE Lifecycle (Bab 4A.4 — 6 phases)

Walk the user through each phase, one at a time.

### Phase 1 — Discovery and Scoping
- Identify remaining stakeholders and SMEs.
- Inventory existing artifacts (documents, source code, database, logs) into an **Asset Inventory**.
- Define the **RE Scope Statement** (target system, target modules, expected deliverables, timeline) and get BA Lead approval.

> **Rule RE-01 (Bab 4A):** every RE activity must start with an RE Scope Statement approved by the BA Lead.

**Entry criteria:** target system identified; access to system/source code granted; at least one SME/user available.

### Phase 2 — System Analysis and Extraction
Apply the core BABOK techniques (Bab 4A.5) to pull information from each source:

| Technique | Applied to | Output |
| --- | --- | --- |
| Document Analysis | old SOPs, manuals, legacy SRS | extracted requirements list |
| Interface Analysis | APIs, file transfers, message brokers | interface specification |
| Observation / Job Shadowing | users running the system | actual workflow notes |
| Data Mining / Analysis | DB schema, data patterns, stored procedures | data model, business rules |
| Prototyping | mockups of current understanding | validated understanding |
| Workshops / Focus Groups | multiple SMEs | consolidated knowledge |

Supporting techniques: code-review collaboration, screen-recording analysis, ERD generation from the database, API doc generation (Swagger/Postman), log analysis.

### Phase 3 — Documentation and Modeling
Transform raw findings into formal models: As-Is process model, business rules catalog, and a data dictionary. Tag every extracted item with a **Confidence Level** (Phase below).

### Phase 4 — Validation and Verification
Cross-validate each finding against multiple sources.

> **Rule RE-03 (Bab 4A):** a business rule may be marked "verified" only after cross-validation from at least **2 different sources** (source code, database, SME/user confirmation, system logs).

### Phase 5 — Baseline and Sign-off
Get formal sign-off from the Process Owner, and produce a **Gap Report** (what the system does vs what the business now needs).

> **Rule RE-06 (Bab 4A):** RE results must be baselined and formally signed off by the Process Owner before they drive a modernization/enhancement project.

### Phase 6 — Maintenance and Updates
Keep the recovered documentation current as the system changes.

## Confidence Level Framework (Bab 4A.7)

Tag every recovered item:

| Level | Criteria | Action |
| --- | --- | --- |
| High | found in source code AND confirmed by SME/user (>=2 sources) | usable as baseline directly |
| Medium | found in one reliable source (code only, or SME only) | needs additional validation |
| Low | only in old documents or based on BA assumption | must be verified before baseline |

> **Rule RE-05 (Bab 4A):** Low-confidence information must not become baseline requirements without additional verification from at least one other source.

## Business Rules Extraction template (Bab 4A.6)

```markdown
| Rule ID | Description | Source (where found) | Confidence | Validated By |
| --- | --- | --- | --- | --- |
| RRULE-01 | (extracted rule) | source code / DB / SME / logs | High/Medium/Low | (name) |
```

> **Rule RE-02 (Bab 4A):** every extracted business rule must record Rule ID, Description, Source, Confidence Level, and Validated By.

## Governance

- **Rule RE-07 (Bab 4A):** respect intellectual property and licensing; ensure RE does not violate third-party software license agreements.
- **Rule RE-08 (Bab 4A):** store all RE deliverables in the BA Knowledge Base and integrate them into the RTM if they will be reused.

## Output

| Artifact | Path |
| --- | --- |
| RE Scope Statement + Asset Inventory | `docs/ba/re-scope.md` |
| As-Is model (recovered) | `docs/ba/process-map-as-is.md` |
| Recovered business rules (with confidence) | `docs/ba/business-rules.md` |
| Recovered data dictionary | `docs/ba/data-dictionary.md` |
| Gap Report | `docs/ba/gap-analysis.md` |

## Handoff

The recovered As-Is feeds straight into the normal pipeline: `process-mapping` (design the To-Be), `requirement-elicitation` (formalize forward requirements), and `impact-analysis` (assess the modernization).

## Writing conventions (enforced in all output)

- No AI slop: no filler or hedging; every sentence informs.
- No em-dashes, no double-dashes (`--`) in prose; dashes only as Markdown syntax (list bullets, table rules) or in literal code/CLI flags (e.g. `--no-deps`).
- No emoji. Professional, declarative tone.
- Governance (Rule AI-01, AI-03): AI-drafted artifacts must be reviewed by the responsible BA before becoming official deliverables; record AI assistance in the Revision History.
- Every deliverable carries a Revision History and version control (Rule DL-02).
- If a document carries a metadata header (`**Version:**`, `**Date:**`, `**Author:**`, `**Status:**`, `**Phase:**`), each such line ends with two trailing spaces so Markdown renders them on separate lines.
