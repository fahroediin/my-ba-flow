---
name: discovery-meeting-prep
description: Prepare a BA for an initial client meeting or a tender aanwijzing session by classifying the session (new system from scratch, vendor switch or troubled project, tender aanwijzing), then producing a prioritized, client-specific question list, a red-flag watchlist, and a capture sheet from the team's question bank. Also runs the post-meeting debrief that turns notes into a pain points register, assumptions log, and open questions. Use when the user says "prep my client meeting", "what should I ask the client", "initial meeting", "discovery meeting", "kickoff with client", "aanwijzing", "pertanyaan untuk klien", "review this KAK/TOR/RKS", "client wants to switch vendor", or shares meeting context, a client profile, or tender documents before a session.
---

# Discovery Meeting Prep

Pre-pipeline on-ramp for the first contact with a client: initial discovery meetings and tender aanwijzing sessions. It replaces ad-hoc, spontaneous question lists with a consistent, prioritized checklist so every BA covers the same ground. Its output feeds `ba-planning` and `stakeholder-interview`.

Aligned with BA Handbook Bab 4.2 (Planning & Scoping), Bab 6 (Stakeholder Management), and Rules P2-01, P2-02, P2-03. Golden rule applied throughout: As-Is before To-Be.

The full question bank lives in [references/question-bank.md](references/question-bank.md). Read it before Step 3. Questions are in Bahasa Indonesia because sessions run in Bahasa Indonesia.

## Step 1 — Classify the session

Ask the user (or infer from what they shared, then confirm):

| Session type | Signals | Modules |
| --- | --- | --- |
| New system from scratch | No system yet, manual/Excel process, "we want an app like X" | Core A + Module B |
| Vendor switch / troubled project | Existing system or project with a previous vendor, unhappy with results | Core A + Module C |
| Tender aanwijzing | KAK/TOR/RKS exists, formal Q&A before bid submission | Module D first, then Core A as a gap filter on the KAK |

## Step 2 — Gather context

Collect what is known, one topic at a time. Do not re-ask what the user already gave.

- Client name, industry, size. If no profile exists, suggest running `company-profiling` first.
- Who will attend from the client side (names, roles) and from our side.
- Meeting duration and format (onsite, online).
- Anything already shared: emails, decks, screenshots, KAK/TOR, previous vendor documents.
- For tenders: read the full KAK/TOR/RKS. Break it into numbered requirements and label each Clear, Ambiguous, Not measurable, Contradictory, or Unrealistic for the timeline.

## Step 3 — Select and tailor questions

From the question bank:

1. Take every P1 question from the selected modules.
2. Drop questions already answered by the context gathered in Step 2. Note the answer instead.
3. Rewrite generic questions with client specifics (their module names, their terms, KAK clause numbers). Example: "Pada butir 4.2 KAK disebut 'integrasi dengan sistem eksisting'. Sistem apa saja yang dimaksud?"
4. Cap the must-ask list at 15 questions for a 60-minute session (scale proportionally). Move the rest to "if time allows".
5. For tenders, order questions by cost impact and remove any question that reveals our solution strategy to competitors.

## Step 4 — Produce the prep sheet

Write `docs/ba/meeting-prep-<client>-<YYYY-MM-DD>.md`:

```markdown
# Meeting Prep: (client), (session type)

**Date:** (date)  
**Attendees (client):** (names/roles)  
**Attendees (us):** (asker, note-taker)  
**Duration:** (minutes)  

## Session goal
(one sentence: what we must know when we walk out)

## Known context
(bullets; answers already known, with source)

## Must-ask (P1)
| # | Question | Source ID | Why it matters | Answer |
| --- | --- | --- | --- | --- |

## If time allows (P2)
| # | Question | Source ID | Answer |
| --- | --- | --- | --- |

## Red flags to watch
(3–5 most likely for this client, from the question bank)

## Capture during the meeting
- Pain points (with frequency and impact numbers)
- Assumptions to confirm
- Open questions (owner, due date)
- Documents promised by the client
```

Remind the user: one BA asks, one BA captures; ask permission to record at the start.

## Step 5 — Debrief (after the meeting)

When the user returns with notes or a transcript:

1. Fill the Answer column. Mark unanswered P1 questions as open questions with owner and due date.
2. Extract pain points into `docs/ba/pain-points-register.md` and assumptions into `docs/ba/assumptions-log.md`, using the formats in `stakeholder-interview`. Every assumption needs a "risk if wrong" (Rule P2-03).
3. List red flags observed and the action for each (report to BD / Head of BA).
4. Draft the Minutes of Meeting. It must be final within 24 hours (Rule P2-01) and confirmed by participants (Rule P2-02).
5. For tenders: list which answers appear in the Berita Acara Pemberian Penjelasan or addendum; oral answers are not binding. Unclear answers go to the risk register with their price impact.
6. Suggest new questions that proved important but are missing from the question bank, so the user can add them.

## Handoff

| Session type | Next skill |
| --- | --- |
| New system | `ba-planning`, then `stakeholder-interview` |
| Vendor switch | `reverse-engineering`, then `ba-planning` |
| Tender | proposal work; after award, `ba-planning` |
| Comparing fix vs rebuild | `impact-analysis` |

## Writing conventions (enforced in all output)

- No AI slop: no filler or hedging; every sentence informs.
- No em-dashes, no double-dashes (`--`) in prose; dashes only as Markdown syntax.
- No emoji. Professional, declarative tone.
- Never promise a solution, price, or timeline in prep notes or questions.
- Metadata header lines end with two trailing spaces so Markdown renders them on separate lines.
