---
name: ba-start
description: Entry point of the my-ba-flow pipeline. Asks which work model applies, product based (a finished app, e.g. built by the CEO Pak Tan or by the BA, handed over as a zip or rar, to be explained to prospective clients) or project based (a client need, built from scratch by the team), shows the route for that model and the next step, and picks up where the BA left off when docs/ba already has work in it. Use when the user starts BA work, says "mulai", "mulai dari mana", "ada aplikasi baru dari Pak Tan", "ada proyek baru", "langkah selanjutnya apa", "sudah sampai mana", or hands over an app archive without saying what to do with it.
---

# BA Start

Routes BA work into one of two models and keeps the BA oriented. This skill does not write documents; it asks, shows the route, and hands over to the skill that does the work.

## Step 1: Find where the work stands

Look at the working folder first. Files that exist already tell the model (anything under `docs/ba/product/` is product based); ask only when nothing is found. If any of these exist, report the current position and the next step; do not restart from the beginning. With several products, versions or clients, report one line per product, version and client (for example: client A has a fit-gap, client B only a meeting prep), then ask which one to continue.

| Found | Position | Next step |
| --- | --- | --- |
| Nothing under `docs/ba/` | Start | First step of the chosen model |
| `docs/ba/product/<produk>-<versi>/product-brief.md` | Product understood | `discovery-meeting-prep` (Product demo to a prospect) |
| `.../sessions/<klien>-<tanggal>/meeting-prep.md` without `debrief.md` | Meeting prepared | Run the meeting, demo with `demo-terpandu-fgd`, then the debrief |
| `.../sessions/<klien>-<tanggal>/debrief.md` | Client met | `fit-gap` |
| `.../fit-gap-<klien>.md` | Fit-gap done | If the client proceeds: project entry in `fit-gap` Step 5 |
| `docs/ba/product-input/` or `docs/ba/ba-work-plan.md` | Project started | Continue the Handbook pipeline from the latest existing deliverable |

When a newer product version arrives while an older version folder exists, the next step is `product-onboarding` for the new version.

## Step 2: Ask the model

Ask only when nothing was found in Step 1, or when the user starts something new. Ask with AskUserQuestion when available, otherwise as a plain question. Never pick for the user.

| Model | Signals |
| --- | --- |
| Product based | The application already exists before any client: built by Pak Tan (CEO) or by the BA (e.g. tester-lab), delivered as a zip or rar of source code, to be explained to prospective clients |
| Project based | A client need comes first; the team builds from scratch and may show mockups, Figma with user flow, or a prototype when the client needs speed |

For product based, also ask who built it: Pak Tan, the BA, or someone else. If the BA built it, the BA can answer intent questions directly. If Pak Tan or an AI-assisted build produced it, nobody has checked its rules with real users yet; the client conversation settles them.

## Step 3: Show the route

Show only the route for the chosen model, mark the current step, and name the next skill.

**Product based** (light format until the client proceeds):

1. `product-onboarding`: extract the zip or rar, run the app, write the product brief.
2. `discovery-meeting-prep`: session type "Product demo to a prospect".
3. `demo-terpandu-fgd`: guided demo or FGD of the product.
4. `fit-gap`: client needs against the product.
5. Client proceeds: separate project folder, then the BA Handbook pipeline: `ba-planning` (Rule P1-01), `reverse-engineering`, `requirement-elicitation`, and onwards.

**Project based** (BA Handbook from the start):

1. `discovery-meeting-prep`, then `ba-planning` and `stakeholder-interview`.
2. `requirement-elicitation`, `process-mapping`, `impact-analysis`.
3. `wireframe-spec` and `data-dictionary`; mockup, Figma or prototype by the team.
4. `demo-terpandu-fgd`: validate the mockup or prototype with the client.
5. `us-ac-writer`, `ba-grooming`, `ba-handoff`, then `change-request` and `solution-evaluation` as needed.

## Step 4: Hand over

Name the next skill and the inputs it needs, then let that skill take over. If the user asks for something outside the chosen route, say which model it belongs to and continue.
