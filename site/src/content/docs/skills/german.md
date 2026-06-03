---
title: German Workflow
description: A dedicated pipeline for German writing — style, source analysis, briefs, drafting, and EN→DE rewriting.
---

The collection is English-first, but a focused subset supports German-language writing. These skills
form their own small pipeline and are independent of the English voice profile — they read and write
German artefacts.

## `finde-stil`

Define, revisit, or sharpen your **German** writing voice. Use it when German content skills
consistently produce output that doesn't sound like your German. Triggers: "finde meinen stil",
"deutsche tonalität", "deutscher schreibstil".

Independent of [`discover-tonality`](/online-writing-skills/skills/discovery/) — it does **not** read `tonality.md` and
produces `stil.md` from scratch in German.

## `analysiere-quelle`

Extract a **German brief** from raw material (an English or German article, a brain dump in either
language, a transcript, mixed notes) as the planning artefact for a German article. Triggers:
"analysiere quelle", "deutsche zusammenfassung", "brief auf deutsch", "extrahiere kern".

This is **extraction, not translation** — the brief is in German, but it captures the core rather
than translating the source. The brief feeds `schreibe-entwurf`.

## `schreibe-entwurf`

Draft a long-form German article (**2,500–3,000 words** — Blog-Beitrag, Fachartikel, Essay,
Tiefenbeitrag) from a German brief. Triggers: "schreibe entwurf", "deutscher entwurf", "langform auf
deutsch".

Requires a German brief as input. If you hand it raw material instead, it will ask whether to run
`analysiere-quelle` first.

## `rewrite-de`

Turn an English article into a German version that reads as if it were **originally written in
German** — not a word-for-word translation. Triggers: "übersetzen", "deutsche Version", "auf Deutsch",
or pasting/linking an English Markdown article and asking for it in German.

It preserves the argument but rebuilds the sentences as native German prose. For the reverse direction
(DE→EN) or literal translation, this is not the right skill.

## Typical German flow

```text
analysiere-quelle  →  schreibe-entwurf      (raw material → German brief → long-form draft)
rewrite-de                                   (existing English article → native German version)
finde-stil                                   (run once to calibrate German voice → stil.md)
```
