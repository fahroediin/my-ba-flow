---
name: requirement-elicitation
description: Elicit and document business requirements into a Business Requirements Document (BRD) and a business rules catalog. Reads stakeholder interview artifacts if they exist, then interviews the user to fill gaps. Use when the user wants to gather requirements, write a BRD, document business rules, says "what are the requirements", "help me write a BRD", "let's capture the business needs", "document the rules", or needs to formalize what the business wants before user stories are written.
---

# Requirement Elicitation

The second step in the BA pipeline. Turns stakeholder pain points and organizational goals into formal, traceable business requirements. This skill produces the BRD that feeds into every downstream artifact: user stories, process maps, and the eventual handoff to engineering.

Two phases: **elicit through structured interview, then synthesize the BRD and business rules.**

Aligned with BA Handbook Bab 4.4 (Analysis & Documentation), Bab 5 (Requirements Engineering), and Rules P3-01, P3-04, RE-04.

## Phase 1 — Elicit

Read existing artifacts first: if `docs/ba/stakeholder-map.md`, `docs/ba/interview-notes.md`, or `docs/ba/pain-points-register.md` exist, load them and use them as context. Do not re-ask questions that are already answered.

Then interview the user one topic at a time, recommending an answer for each. Cover:

- **Business objectives.** What business outcomes does the project target? State each as a measurable goal (increase X by Y%, reduce Z from A to B). Tie each to a stakeholder from the stakeholder map if available.
- **Scope boundaries.** What is in scope for this initiative and what is explicitly excluded? If the user is vague, push for concrete boundaries: which departments, which products, which geographies, which user segments.
- **Functional requirements.** For each business objective, what capabilities must the solution provide? Organize by business process or functional area. For each requirement:
  - A unique ID (`BR-XX`)
  - A clear statement in the form: "The system shall [verb] [object] [condition]"
  - Priority (Must/Should/Could/Won't, MoSCoW)
  - Source stakeholder(s)
  - Acceptance measure: how do you know this requirement is met?
- **Business rules.** The policies, constraints, and logic the business enforces regardless of any system. These are not features; they are facts about how the business operates. Examples: "An order above $10,000 requires manager approval", "Customers in region X are exempt from tax Y". For each rule:
  - A unique ID (`RULE-XX`)
  - The rule statement
  - Source (regulation, policy, convention)
  - Exception handling: what happens when the rule cannot be met?
- **Non-functional requirements (business perspective).** Business-side expectations about system quality. Each NFR must be categorized under one of the **ISO/IEC 25010** characteristics (Rule P3-04):
  - **Functional Suitability**: completeness, correctness, appropriateness
  - **Performance Efficiency**: time behaviour, resource utilization, capacity
  - **Compatibility**: co-existence, interoperability
  - **Usability**: learnability, operability, accessibility
  - **Reliability**: maturity, availability, fault tolerance, recoverability
  - **Security**: confidentiality, integrity, non-repudiation, authentication, authorization
  - **Maintainability**: modularity, reusability, analysability, modifiability, testability
  - **Portability**: adaptability, installability, replaceability
  Every NFR must have a measurable target, not subjective descriptions.
- **Constraints and assumptions.** Budget limits, timeline, regulatory deadlines, technology mandates from IT, integration requirements with existing systems. Separate hard constraints (non-negotiable) from assumptions (believed true but unverified).
- **Dependencies.** Other projects, systems, teams, or decisions this initiative depends on. For each, note the dependency type (blocks, informs, shares resources) and current status.

Surface contradictions between stakeholder needs as you go. When two requirements conflict, present both sides and ask the user to resolve or escalate.

### Acceptance Criteria rules

When eliciting or writing acceptance criteria for any requirement:

- **Rule P3-01**: each AC must have exactly **one THEN clause**. If there are multiple outcomes, split into separate ACs.
- **Rule RE-04**: each AC must include **boundary values** and **edge cases** so QA can derive test cases using Equivalence Partitioning and Boundary Value Analysis without further clarification.
- **MRTM rule (Bab 14)**: if a feature's logic involves more than **3 input variables or decision branches**, do not write AC as narrative prose. Instead, reference a tabular MRTM (Master Requirement and Test Matrix). Write the AC as: *"Refer to MRTM rows TRM_XXX_001 through TRM_XXX_NNN for comprehensive logic combinations."*

## Phase 2 — Synthesize

### Artifact 1: Business Requirements Document (`brd.md`)

Structure:

```markdown
# Business Requirements Document

**Version:** 1.0  
**Date:** (date)  
**Author:** (BA name)  
**Status:** Draft  

## 1. Executive Summary
(one paragraph: the problem, the proposed solution, the expected outcome)

## 2. Business Objectives
| ID | Objective | Measure | Target | Stakeholder |
| --- | --- | --- | --- | --- |

## 3. Scope
### 3.1 In Scope
### 3.2 Out of Scope

## 4. Functional Requirements
### 4.1 (Functional Area)
| ID | Requirement | Priority | Source | Acceptance Measure |
| --- | --- | --- | --- | --- |

## 5. Non-Functional Requirements (Business)
| ID | Requirement | Category (ISO 25010) | Priority | Measurement | Source |
| --- | --- | --- | --- | --- | --- |

## 6. Constraints and Assumptions
### 6.1 Constraints
| ID | Constraint | Type | Impact | Flexibility |
| --- | --- | --- | --- | --- |
| CON-001 | | Budget/Timeline/Resource/Regulatory/Technical | | Fixed/Flexible |

### 6.2 Assumptions
| ID | Assumption | Raised By | Date | Status | Risk if Wrong |
| --- | --- | --- | --- | --- | --- |
| ASM-001 | | | | Unconfirmed/Confirmed/Invalid | |

## 7. Dependencies
| ID | Dependency | Type | Status | Impact if Delayed |
| --- | --- | --- | --- | --- |

## 8. Risks
| ID | Risk | Probability | Impact | Mitigation |
| --- | --- | --- | --- | --- |

## 9. Approval
| Role | Name | Date | Signature |
| --- | --- | --- | --- |
```

### Artifact 2: Business Rules Catalog (`business-rules.md`)

```markdown
# Business Rules Catalog

| ID | Rule | Category | Source | Exceptions | Related BR |
| --- | --- | --- | --- | --- | --- |
| RULE-01 | (statement) | (validation/authorization/calculation/workflow) | (source) | (exception handling) | BR-XX |
```

Group rules by category. Each rule traces back to the BR it supports.

## Output and handoff

Present both artifacts for review. Offer to save them to `docs/ba/`. When the user is satisfied, point them at:
- `process-mapping` to visualize the workflows these requirements describe
- `ba-grooming` to validate user stories against these requirements
- `impact-analysis` to assess the change these requirements imply

## Writing conventions (enforced in all output)

- No AI slop: no filler or hedging; every sentence informs.
- No em-dashes, no double-dashes (`--`) in prose; dashes only as Markdown syntax (list bullets, table rules) or in literal code/CLI flags (e.g. `--no-deps`).
- No emoji. Professional, declarative tone.
- If a document carries a metadata header (`**Version:**`, `**Date:**`, `**Author:**`, `**Status:**`, `**Phase:**`), each such line ends with two trailing spaces so Markdown renders them on separate lines.
