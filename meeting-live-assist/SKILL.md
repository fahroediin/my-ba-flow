---
name: meeting-live-assist
description: Assist a BA while a client meeting is in progress by processing the transcript in chunks of 5 to 10 minutes and returning, for each chunk, what is new, at most three questions to ask right now, and rows for the Open Questions and Assumptions sections of the MoM template (T-04). Closes with a consolidated list ready to merge into the MoM. Also replays a saved transcript or recording in chunks to test the approach after the fact. Use when the user says "meeting sedang berjalan", "bantu saya saat meeting", "ini potongan transkrip", "live meeting", "transkrip live", pastes text from Windows Live Captions, Google Meet or Teams captions during a session, or asks to replay an old transcript chunk by chunk.
---

# Meeting Live Assist

Companion for the meeting itself. `discovery-meeting-prep` prepares the questions before the session and runs the debrief after it; this skill sits in between, so gaps surface while the client is still in the room instead of becoming follow-up emails.

Aligned with BA Handbook Bab 6 (Stakeholder Management), the MoM template T-04 (`Template/Template_MoM.md`), and Rules P2-01, P2-02, P2-03. Golden rule applied throughout: As-Is before To-Be.

Claude cannot hear the meeting. It works only on text the user pastes. Every answer must be readable in 30 seconds, because the user reads it while listening.

## Step 1: Setup (before the meeting starts)

Ask once, in one message, and accept short answers:

- Client, project, and the session goal in one sentence.
- Meeting type: with the client, or internal preparation. In an internal meeting, "Tanyakan sekarang" targets what the team must settle before contacting the client (owner, deadline, positioning, who decides), and Pertanyaan Terbuka collects what only the client can answer.
- Participants and roles, so questions can be addressed to the right person.
- Names and terms likely to be misheard: people, the client, products, modules. Use them to read the transcript correctly.
- Agenda topics.
- An existing prep sheet: `docs/ba/meeting-prep-<client>-<YYYY-MM-DD>.md` or `docs/ba/product/<produk>-<versi>/sessions/<klien>-<tanggal>/meeting-prep.md`. If one exists, load its must-ask list and track each question as answered or not.

If the user skips setup and pastes a chunk directly, infer what you can from the chunk and continue. Do not block on missing context.

Remind the user once: ask the client for permission to record, and check the NDA before transcript text goes to a cloud service.

### Getting live text

Tell the user the option that fits their setup, only if they ask or have no text source yet:

| Meeting | Source |
| --- | --- |
| Offline (in a room) | Hollyland Lark receiver plugged into the laptop as the microphone, then Windows Live Captions (Win + Ctrl + L) |
| Online | Windows Live Captions on system audio with microphone audio included, or the built-in transcript of Google Meet or Teams |

The user copies the newest part every 5 to 10 minutes. Overlap with the previous chunk is fine; ignore lines already processed.

## Step 2: Process each chunk

Use this exact format. Number questions and assumptions continuously across chunks (Q-01, Q-02, A-01) so the user can refer to them aloud.

```markdown
## Potongan <n> (<mm:ss> s.d. <mm:ss>)

**Baru dibahas:** 2 to 4 bullets, facts only, with numbers when said.

**Tanyakan sekarang:**
1. Q-07 (ke <role>) <question>. Alasan: <one short clause>.

**Terjawab:** Q-03: <answer in a few words>.

**Pertanyaan Terbuka (T-04 bagian 5):**
| No | Pertanyaan | Perlu Jawaban Dari | Deadline Jawaban |
| --- | --- | --- | --- |

**Asumsi (T-04 bagian 6):**
| No | Asumsi Logika Bisnis / Teknis | Konfirmasi Diperlukan Dari |
| --- | --- | --- |

**Keputusan / action item terdengar:** short list, or "tidak ada".
**Must-ask prep belum terjawab:** IDs from the prep sheet, or omit when there is no prep sheet.
```

Rules for the chunk answer:

- "Tanyakan sekarang" holds at most 3 questions, the ones that lose value if not asked before the topic moves on. Everything else goes to Pertanyaan Terbuka.
- Never repeat a question already listed. When a later chunk answers it, move it to Terjawab.
- Omit an empty section instead of printing an empty table.
- Questions are in Bahasa Indonesia, short enough to say in one breath, and use the client's own terms.
- Leave Deadline Jawaban as "TBD" unless a date was said.

### What makes a good question here

Look for these signals in the chunk:

| Signal in the transcript | Question to raise |
| --- | --- |
| "biasanya", "kadang", "tergantung", "kalau perlu" | The exact condition and who decides |
| A To-Be wish with no As-Is described | How it is done today, by whom, with what tool |
| A pain point with no number | Frequency, volume, time lost, or money lost |
| A rule with no exception mentioned | What happens when it fails, is late, or is rejected |
| An approval step with no named role | Who approves, and what happens above a limit |
| A client term not defined | What the term means; note it for `data-dictionary` |
| Two speakers saying different things | Which version is correct, addressed to the owner |
| A sentence that reads two ways, for example a product feature or a task for the team | Which one was meant |
| Data moving between systems or units | Source, format, frequency, and who owns it |

Never promise a solution, price, or timeline in a suggested question.

### Transcript quality

Speech recognition mangles names, numbers, and domain terms. Never invent what was not said. When a word looks misheard and it matters, write it as `[tidak jelas: <word>]` and ask the user to confirm it instead of guessing. Do not turn a misheard number into an assumption.

## Step 3: Close (when the user says "selesai" or "tutup meeting")

Produce one consolidated block in T-04 order so it can be merged with the MoM the user drafts from the recording:

1. Poin Diskusi & Keputusan Bisnis: topics and decisions heard, with PIC when named.
2. Tindak Lanjut: action items with PIC and deadline when said.
3. Pertanyaan Terbuka: every open question still unanswered, deduplicated.
4. Asumsi & Batasan: every assumption, each with a "risk if wrong" (Rule P2-03).
5. Must-ask prep belum terjawab, when a prep sheet was loaded.

If the project has a `docs/ba/` folder, write it to `docs/ba/meeting-live-<client>-<YYYY-MM-DD>.md`; otherwise return it in chat. Remind the user that the MoM must be final within 24 hours (Rule P2-01) and confirmed by participants (Rule P2-02).

## Replay mode

For a saved transcript or recording, used to test this skill or to catch what a past meeting missed:

1. If given audio or video, transcribe it locally first (for example faster-whisper with timestamps, passing the names and terms from setup as the initial prompt), and tell the user the transcript is machine output.
2. Split the transcript into chunks of about 5 minutes by timestamp.
3. Run Step 2 on each chunk in order, using only what was said up to that chunk. Do not use later chunks to sharpen earlier questions; the point is to show what was knowable at that moment.
4. Run Step 3, then, if the user has the MoM of that meeting, compare its Open Questions and Assumptions with the replay result: which were caught live, which only the replay found, which only the MoM has. Also report T-04 sections the MoM is missing, and names, PICs, times, or reasons in the MoM that the transcript does not contain, so the user can verify them before distribution.

## Handoff

| Situation | Next skill |
| --- | --- |
| After the meeting, prep sheet existed | `discovery-meeting-prep` Step 5 (debrief) |
| Pain points and stakeholder map to record | `stakeholder-interview` |
| Requirements and business rules surfaced | `requirement-elicitation` |
| Undefined client terms collected | `data-dictionary` |

## Writing conventions (enforced in all output)

- No AI slop: no filler or hedging; every sentence informs.
- No em dashes, no double hyphens in prose; dashes only as Markdown syntax.
- No emoji. Professional, declarative tone.
- Metadata header lines end with two trailing spaces so Markdown renders them on separate lines.
