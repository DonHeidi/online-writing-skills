---
name: analysiere-quelle
description: >
  Use when the user has raw material (English article, German article, brain dump in either language,
  transcript, mixed notes) and wants a German brief extracted from it as the planning artefact for a
  German article. Trigger on "analysiere quelle", "deutsche zusammenfassung", "brief auf deutsch",
  "extrahiere kern", or any explicit ask to prepare raw material for German long-form writing. Produces
  a German brief that schreibe-entwurf reads. Not for translation (the brief is in German but it is not
  a translation — it is an extraction).
---

# Analysiere Quelle

You extract a German brief from raw material. The brief is a planning artefact — a German argument map that captures the source's thesis, logical steps, evidence, target register, and any English/LinkedIn tells that the German version will drop. It is the input to `schreibe-entwurf`.

The problem this solves: when raw material is an English article, an LLM writing a German version unconsciously inherits English rhythms and platform tics from the source while writing prose. The brief breaks that grip. By the time prose-writing happens, the working artefact is German, in sober register, and the English source is two layers removed. This is the structural firewall against translation-drift.

The skill is language-agnostic on input, German-only on output.

## Setup

Load config (per `../../CONFIG.md` "Applying Config in Skills"):

- **`stil.md`** — when populated, the brief's "Zielregister" section reflects the user's defined German voice. If absent, fall back to `stil-guide.md` baselines.
- **`stil-guide.md`** — universal German register baselines and failure modes catalogue. Always loaded.
- **`purpose.md`** — when populated, the brief's "Adressat" reflects the user's defined audience.
- **`buckets.md`** — when populated, used to identify which content bucket the piece serves.

If `stil.md`, `purpose.md`, or `buckets.md` is missing or unpopulated, proceed without it. Do not fail. Always load `stil-guide.md` (it ships with the plugin).

Input is raw material. The user pastes it directly or provides a file path. If a file path is given, read it first.

---

## Step 1 — Identify the source character

Read the raw material and classify it:

- **English thought-leadership** — full of English-coded rhythms and LinkedIn tells. Most aggressive de-tell pass needed.
- **English Fachtext / sober writing** — fewer LinkedIn tells but still English rhythms. Moderate de-tell.
- **German Fachtext** — already in target register. Minimal de-tell, mostly anglicism check.
- **German LinkedIn / blog** — LinkedIn-coded structures even though German. Aggressive de-tell.
- **Brain dump (any language)** — fragmentary, unstructured. No source register to drop from; just extract.
- **Transcript** — spoken-word patterns, repetition, filler. Strip filler, keep argument.

See `../../references/stil-guide.md` "Source-Character Handling" for what to drop and preserve per type.

State the classification briefly to the user before proceeding: "Quelle: [type]. Ich extrahiere jetzt den Brief."

---

## Step 2 — Extract argument structure

Stay close to the source's actual claims. Do not elaborate, do not extend, do not invent specifics. Length grows from precision, not from new content.

- **These** — the single argument the text makes, in one German sentence. Not a hook, not a summary headline — the argument.
- **Argumentationsstruktur** — the logical steps as German bullets. Each bullet names one move in the argument. Sequence matters.
- **Belege und Beispiele** — data points, examples, third-party quotes. Third-party direct quotes stay in their original language; incidental claims are paraphrased to German. Numbers and proper nouns unchanged.

If the source's argument is unclear, mark "[?]" and ask the user during the surfacing step. Do not silently invent structure.

---

## Step 3 — Identify register and audience from config (not from source tone)

This is the critical step. The source's English LinkedIn-y tone does **not** become the brief's tone.

- **Zielregister** — pick from Beschreibend / Argumentativ / Anleitend / Referierend based on the source's *function* (does it describe, argue, instruct, or curate?), then layer the user's tendencies from `stil.md` if populated.
- **Adressat** — drawn from `purpose.md` if available. If not, infer from the source's evident audience but state the inference explicitly.

If the source's function is mixed (e.g., a Fallstudie with argument-tinted edges), name the primary register and note the secondary tilt.

---

## Step 4 — List dropped tells

Explicit catalogue of patterns from the source that the German version will not carry over. Reference `stil-guide.md`'s failure modes catalogue.

For each dropped tell:
- Quote or paraphrase the pattern in the source.
- State what the German version will do instead.

Examples:
- Quelle nutzt *"Most people think X, they're wrong"*-Setup → deutsche Version beginnt direkt mit dem Argument.
- Quelle nutzt Em-Dash-Drama für Reveals → deutsche Version ersetzt durch explizite Subordination.
- Quelle nutzt Marketing-Intensifier (*massiv, fundamental*) → deutsche Version benennt die spezifische Veränderung.
- Quelle nutzt Anglicism-Splices (*delivern, performen*) → deutsche Version nutzt deutsche Verben.

If the source is a brain dump or already-sober German Fachtext, this section is empty or near-empty. State that explicitly: "Keine Quellen-Muster zu verwerfen."

---

## Step 5 — Surface the brief to the user

Present the brief in conversation. **Do not save to file until the user has reviewed it.**

Walk through each section in German. Ask: "Stimmt die These? Stimmt die Struktur? Fehlt etwas? Soll etwas raus?"

This checkpoint is mandatory. Skipping it makes the skill redundant — the whole point is to catch a register or thesis misreading before 2,500 words of prose are written from it. A 200-word brief is the cheapest place to fix that.

Iterate on the user's feedback. Re-present changed sections.

---

## Step 6 — Save (soft prompt)

After the user approves the brief, offer to save it.

**Suggestion:** `.online-writing/briefs/<slug>.md` — same parent folder as the other plugin artefacts, briefs as a sub-folder. Folder created on first save.

The user can:
- Accept the suggestion (use the suggested slug or rename).
- Pick a different location.
- Skip saving entirely (the brief lives only in the conversation).

If the user accepts the suggestion, create `.online-writing/briefs/` if it doesn't exist, then write the brief.

---

## Brief Template

Use this structure:

```markdown
# Brief — [working title in German]

**Quelle:** [filename, URL, or first line of raw material]
**Charakter der Quelle:** [English-thought-leadership / English-Fachtext / German-Fachtext / German-LinkedIn / brain dump / transcript / mixed]
**Datum:** [YYYY-MM-DD]

## These

[One German sentence — the single argument]

## Argumentationsstruktur

- [Logical step 1]
- [Logical step 2]
- [Logical step 3]
- ...

## Belege und Beispiele

- [Data point, example, or quote — verbatim where it's a third-party direct quote, paraphrased to German for incidental claims. Numbers and proper nouns unchanged.]
- ...

## Zielregister

**Primär:** [Beschreibend / Argumentativ / Anleitend / Referierend]
**Sekundäre Färbung:** [if any, otherwise "keine"]
**Voice-Notes aus stil.md:** [user-specific tendencies that apply to this register, if stil.md is populated]

## Adressat

[Who the piece addresses — drawn from purpose.md if available; otherwise inferred from source]

## Verworfene Muster aus der Quelle

[Explicit list of English/LinkedIn tells the German version will NOT carry over. Empty if source is already sober German or a brain dump.]

- Quelle nutzt [pattern] → deutsche Version macht [alternative]
- ...

## Offene Fragen

[Anything the agent could not extract cleanly. User fills in or marks "skip".]

- [?]
```

---

## Edge Cases

- **Code blocks** — if the source contains code, list the code blocks under "Belege und Beispiele" with a short German description of what each one demonstrates. The actual code stays in English.
- **Third-party direct quotes** — keep in their original language under "Belege und Beispiele". Note "(Direktzitat, Original belassen)".
- **Data and statistics** — keep numbers, percentages, proper nouns unchanged.
- **Multiple sources** — if raw material is several articles or a mixed brief, list all under "Quelle" and note "Mischmaterial: Argument synthetisiert aus mehreren Texten".
- **Genuinely uncertain extractions** — mark with `[?]` under "Offene Fragen". Do not silently guess.
