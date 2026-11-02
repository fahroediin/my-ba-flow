---
name: fit-gap
description: Product based checkpoint after demoing a finished product to a prospective client (calon klien). Compares what the client needs with what the product already does, producing a fit-gap matrix (Fit, Fit dengan konfigurasi, Gap kecil, Gap besar, Tidak dibutuhkan), the final status of every product assumption, and a go or no-go recommendation. When the client proceeds, it opens a separate project folder and hands over to the BA Handbook pipeline (ba-planning, reverse-engineering, requirement-elicitation). Use after a product demo or FGD, or when the user says "fit-gap", "apa yang cocok dan apa yang kurang", "klien mau lanjut", "gap produk dengan kebutuhan klien", "kebutuhan klien vs fitur aplikasi".
---

# Fit-Gap

The meeting point of the two work models. In **product based** work the product already exists; after the client has seen it, this skill states exactly which needs the product meets, which need changes, and which product features the client does not need. The gaps become the scope of a project, and from that moment the BA Handbook applies.

This skill is for product based work only. In project based work there is no finished product to compare against; feedback from a prototype demo goes to `ba-grooming` instead.

Light format until the client proceeds (see Writing conventions).

## Inputs

From `docs/ba/product/<produk>-<versi>/`:

- `feature-inventory.md`, `business-rules-found.md`, `assumptions-to-confirm.md` (from `product-onboarding`)
- `sessions/<klien>-<tanggal>/`: `meeting-prep.md` and `debrief.md` (from `discovery-meeting-prep`), and the demo or FGD notes copied there by `demo-terpandu-fgd`

If there is no debrief and no session notes for this client, stop: a fit-gap without the client's own words is guesswork. Point the user to `discovery-meeting-prep` (session type "Product demo to a prospect") and `demo-terpandu-fgd`, and resume afterwards. If several sessions exist for the same client, read them all, newest last.

## Step 1: List the client's needs

From the debrief and session notes, list every need the client stated or confirmed, in the client's words, each with its source (debrief section, or "catatan langkah N" from the demo). Do not add needs the client never expressed.

## Step 2: Match each need to the product

| Kebutuhan klien | Sumber | Status | Bukti di produk | Catatan |
| --- | --- | --- | --- | --- |

Status, exactly one of:

| Status | Meaning |
| --- | --- |
| Fit | The product does it as is |
| Fit dengan konfigurasi | Settings or master data only, no code change |
| Gap kecil | Small change to an existing feature |
| Gap besar | New module, new flow, or a change to a core rule |
| Tidak dibutuhkan | A product feature the client does not need (list these too: they affect training and licensing talks) |

Evidence must point to `feature-inventory.md` IDs or `business-rules-found.md` IDs. A need matched only to an `Asumsi` rule that the client has not confirmed is at best `Gap kecil` until confirmed.

## Step 3: Close the assumptions

For every row in `assumptions-to-confirm.md`, record the final status: `dikonfirmasi`, `dibantah`, or `belum`. A `dibantah` assumption usually creates a gap; add it to the matrix. `belum` items go to the open questions list with an owner.

## Step 4: Summarise and recommend

- Count per status.
- The gaps that decide the deal (the ones the client called must-have).
- Recommendation: proceed, proceed with conditions, or do not proceed, with one sentence of reasoning. Never state price or timeline.

Write `docs/ba/product/<produk>-<versi>/fit-gap-<klien>.md`. Re-running after a later session updates the same file and notes what changed.

## Step 5: Entry into a project (when the client proceeds)

Only when the user says the client is moving forward:

1. Offer to create a separate folder (or repository) for the client project. Each client project lives on its own, so the Handbook documents of two clients never mix.
2. Copy into `<folder proyek>/docs/ba/product-input/`: `fit-gap-<klien>.md`, the client's `sessions/` folders, and the five `product-onboarding` files.
3. From here every deliverable follows the BA Handbook. Hand over in this order:
   1. `ba-planning`: the mandatory first gate (Rule P1-01), with the fit-gap as context and the gaps as candidate scope.
   2. `reverse-engineering`: run in full (Bab 4A) to formalise the product's As-Is, using its "Input from product based" section. The fit-gap feeds the RE Gap Report `docs/ba/gap-analysis.md`; it does not replace it.
   3. `requirement-elicitation`: the gaps become the project's requirements, then the normal pipeline continues.

## Writing conventions (enforced in all output)

- Light format until Step 5: header lines `**Produk:**`, `**Versi:**`, `**Tanggal:**`, `**Disusun:**`, each ending with two trailing spaces, then `Disusun dengan bantuan AI, ditinjau oleh BA: (nama)`. No Handbook template, no sign-off.
- Documents are in Bahasa Indonesia, in the client's terms.
- Never promise a solution, price, or timeline.
- No AI slop: no filler or hedging; every sentence informs.
- No em-dashes, no double-dashes in prose; dashes only as Markdown syntax.
- No emoji. Professional, declarative tone.
