---
name: schreibe-entwurf
description: >
  Use when the user has a German brief (produced by analysiere-quelle, or hand-written) and wants a
  long-form German article in the 2,500–3,000 word range — full Blog-Beitrag, Fachartikel, Essay, or
  Tiefenbeitrag. Trigger on "schreibe entwurf", "deutscher entwurf", "langform auf deutsch", or any
  explicit ask to draft a long-form German piece from a brief. Requires a German brief as input — if
  the user hands raw material instead, ask whether to run analysiere-quelle first. For short-form
  posts (800–1,200 words) use the (future) schreibe-post skill. For platform micro-posts use
  destilliere (future).
---

# Schreibe Entwurf

You write a 2,500–3,000 word German article from a German brief. The brief is the source-of-truth during prose-writing. The original raw material is consulted only for fact-check (numbers, names, direct quotes), never for sentence-level guidance.

This is the structural firewall against translation-drift: by the time this skill runs, the English source (if any) is two layers removed from the prose-writing context. The brief is in German, in sober register, and represents the argument the German article will make.

## Setup

Load config (per `../../CONFIG.md` "Applying Config in Skills"):

- **`stil.md`** — when populated, voice tendencies, Sachlichkeit/Polemik position, anglicism stance, register tendencies, and reference samples shape the prose. If absent, fall back to `stil-guide.md` baselines.
- **`stil-guide.md`** — universal German register baselines, cross-cutting LLM failure modes catalogue, German Textkultur rules. Always loaded.
- **`purpose.md`** — when populated, audience framing and category positioning.
- **`buckets.md`** — when populated, identify which bucket this piece serves; tag the output.
- **`settings.md`** `## schreibe-entwurf` section — gender style and address form. See "Required settings" below.

If `stil.md`, `purpose.md`, or `buckets.md` is missing or unpopulated, proceed without it. Always load `stil-guide.md`.

### Required settings (prompt if unset)

The `## schreibe-entwurf` section in `.online-writing/settings.md` holds stylistic choices the skill cannot default safely. If the file, the section, or a required field is missing, prompt the user **once** with the options below, save their answers under `## schreibe-entwurf` in `.online-writing/settings.md` (creating file and section as needed, per CONFIG.md writing rules), then proceed. **Preserve the field format from CONFIG.md exactly** — bold label followed by value, e.g. `**Gender style:** Gender colon`.

- **`Gender style:`** how to handle German gendered forms. Offer the full option list:
  - `Generic masculine` — *Entwickler, Mitarbeiter, Nutzer*
  - `Paired forms` — *Entwicklerinnen und Entwickler, Mitarbeiterinnen und Mitarbeiter*
  - `Gender colon` — *Entwickler:innen, Mitarbeiter:innen, Nutzer:innen*
  - `Gender star` — *Entwickler\*innen, Mitarbeiter\*innen, Nutzer\*innen*
  - `Gender gap` — *Entwickler_innen, Mitarbeiter_innen*
  - `Binnen-I` — *EntwicklerInnen, MitarbeiterInnen*
  - `Neutral forms` — participles and neutral nouns (*Entwickelnde, Studierende, Fachkraft, Person*)
  - `Ask each time` — prompt per draft

### Defaulted settings (use silently unless user overrides in `settings.md`)

- **`Address form:`** default to **`Sie`** unconditionally. *Mirror source* is not offered as a default because raw material may be a brain dump with no source register to mirror, and Sie is the safer default for German thought leadership.

---

## Step 1 — Require a German brief

Input is a German brief — either pasted directly or via a file path under `.online-writing/briefs/<slug>.md` (or anywhere else the user saved it).

**If the user hands raw material instead of a brief**, ask:

> "Du hast Rohmaterial übergeben, keinen Brief. Soll ich zuerst `analysiere-quelle` laufen lassen, um einen Brief zu erstellen? Oder hast du den Brief bereits anderswo?"

Do not silently dispatch to `analysiere-quelle`. The user controls the handoff. If they want to proceed without a brief, refuse — explain that the brief is the firewall against translation-drift and the skill cannot bypass it.

If they pass raw material *and* a brief, the brief is primary. The raw material is reference for fact-check only.

---

## Step 2 — Internalise the brief

Before writing prose:

- The brief's **These** is the single argument the article will make.
- The brief's **Argumentationsstruktur** is the article's spine. Each step becomes a section or sequence of paragraphs.
- The brief's **Belege und Beispiele** are the evidence to weave in.
- The brief's **Zielregister** sets the register (Beschreibend / Argumentativ / Anleitend / Referierend), with secondary tilts noted.
- The brief's **Verworfene Muster** is the explicit no-fly list — patterns that must not appear in the prose.

Read `stil-guide.md` "Universal Register Baselines" for the brief's primary register. Read `stil.md` (if populated) for the user's tendencies in that register. Read `stil-guide.md` "Cross-Cutting German LLM Failure Modes" — this is the failure catalogue you will check against.

You are not about to translate or expand the brief. You are about to write a German article whose argument the brief describes.

---

## Step 3 — Write the draft (2,500–3,000 words)

Apply the German Textkultur rules from `stil-guide.md` *as you write*, not as a post-edit pass. The rules:

- **Sentence Architecture** — working sentences run 20–35 words. Three or more sentences under 10 words signal translated text (carve-out: deliberate rhetorical parallelism). Use subordinate clauses to pack context.
- **Connective Tissue** — explicit logical connectors between ideas. Argumentative connectives, not additive. Avoid the *Außerdem* trap.
- **Compound Nouns and Nominalization** — feature, not bug, in moderation. Three nominalizations and no concrete verbs in one sentence → rewrite.
- **Loanword vs. Anglicism** — apply the three-condition heuristic from `stil-guide.md`. Specifically forbidden: *performen, alignen, delivern, leveragen, impacten, committen, pushen, sich aligned, gemeinsam alignen*.
- **Paragraph Structure** — German paragraphs are typically longer than English. Develop one thought fully. Context-before-claim is natural.
- **Headlines and Subheadings** — German headlines preview, English ones tease. Subheadings should be informative, not clever.

**Source firewall:** the brief is the source-of-truth. The original raw material is consulted **only** for fact-check (numbers, names, direct quotes). If you find yourself reaching for the source while writing prose, stop — the brief is what you write from.

**Length target:** 2,500–3,000 words. Length grows from clause structure (subordination, connective tissue), never from new content. If the German says something the brief did not, cut it.

**Voice and register:**
- If `stil.md` is populated, match dimension tendencies for long-form, match register tendencies for the brief's primary register, check output against the user's agent-specific failure modes, pattern-match against reference samples.
- If `stil.md` is absent, apply `stil-guide.md` register baselines.

---

## Step 4 — Self-review

Run these countable checks before delivering. Each has a concrete trigger and a concrete action.

| Check | How to run it | Trigger to rewrite |
|---|---|---|
| Short-sentence streak | Scan the text. Flag any stretch of 3+ consecutive sentences under 10 words. | If deliberate rhetorical parallelism (anaphora, tricolon mirroring a device in the brief) → keep. Otherwise → merge into subordinate-clause structure. |
| Subordinate-clause density | In any 300-word stretch, count *weil, obwohl, wobei, dass, sofern, indem, während*, plus relative pronouns *der/die/das* used subordinately. | Fewer than ~5 across 300 words → too flat. Rewrite 1–2 paragraphs to add argumentative depth. |
| Additive transitions | Scan paragraph openings. List the connectors. | If more than one paragraph starts with *Außerdem, Auch, Zusätzlich, Und, Darüber hinaus*, replace with argumentative connectors. |
| Anglicism sweep | Search for: *performen, delivern, leveragen, impacten, committen, pushen, aligned, next-level, gemeinsam alignen*. | Any hit → apply the Loanword heuristic. |
| Marketing-vocabulary sweep | Search for: *grundlegend, fundamental, massiv, exponentiell, krass, einfach nur, völlig, komplett, total* used as intensifiers; *Game-Changer, Revolution, Disruption, Paradigmenwechsel, neu definieren, transformieren, revolutionieren*. | Any hit → name the specific change instead. |
| LinkedIn-coded structure scan | Search for: *"Was viele nicht verstehen…"*, *"Die Wahrheit ist…"*, *"Hier kommt der Punkt…"*, *"Was Ihnen niemand sagt…"*, *"Eine unbequeme Erkenntnis…"*. | Any hit → cut the hook, start with the substance. |
| Stock translation patterns | Search for: *"Was auf den ersten Blick X erscheint, entpuppt sich bei näherer Betrachtung als Y"*, *"und zwar…"*, *"in der Tat"*, *"letztendlich"*, *"in der heutigen Welt"*, *"Es ist wichtig zu erwähnen, dass"*. | Any hit → rewrite the sentence with direct German constructions. |
| Frontmatter integrity | Re-read the YAML block. | `title / description / excerpt` translated AND `slug / tags / dates / IDs` untouched? If not, fix. |
| Code and quotes | Check each code block and each direct third-party quote. | Code in English; comments translated only if explanatory; direct third-party quotes untouched with German context around them. |
| Brief-no-fly compliance | Re-read the brief's "Verworfene Muster" section. | Any no-fly pattern appearing in the draft → rewrite that passage. |

If any check triggers, **rewrite the affected passage — don't patch it**. A translated or LinkedIn-coded sentence cannot be repaired word by word; it has to be rebuilt.

---

## Step 5 — Deliver

- Deliver the finished German text as markdown.
- Preserve the heading hierarchy implied by the brief's argument structure.
- Translate the relevant YAML frontmatter fields if the brief or raw material had them. Keep `slug`, `tags`, `dates`, IDs as-is unless the user says otherwise.
- Do **not** add translator's notes, commentary, or meta-discussion — only the finished text.

After delivery, offer one optional next step. Keep it brief and non-blocking.

- **Save to a file?** Ask whether to write the output to a file. If yes, ask the user where and what to name it (defer to whatever conventions apply in their environment — don't assume a specific folder layout or naming scheme).

For structural diagnostics on the German output, the user can run `diagnose` against it — the post-structure playbook is largely language-agnostic, though German-specific rhythm and register issues are this skill's responsibility, not `diagnose`'s.

---

## Edge Cases

- **Code blocks** — keep code in English. Comments inside code blocks may be translated if purely explanatory; leave them in English if functional.
- **Third-party direct quotes** — keep direct quotes in their original language. Add a German paraphrase or context sentence around them; do not translate someone else's direct words.
- **Data and statistics** — keep numbers, percentages, and data points unchanged. Adjust number formatting to German conventions (comma as decimal separator, period as thousands separator) only if the piece is clearly for a German-only audience.
- **Acronyms** — spell out on first use if not universally known in the German tech community. *LLM* and *API* need no explanation; niche acronyms do.
- **Genuinely uncertain domain terms** — mark inline with `[?]` so the user can review. Do not silently guess.
