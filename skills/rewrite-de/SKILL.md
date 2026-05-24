---
name: rewrite-de
description: >
  Use when the user wants an English article turned into a German version that reads as if it
  were originally written in German — not a word-for-word translation. Trigger on "übersetzen",
  "deutsche Version", "auf Deutsch", "German version", or any EN→DE language transfer for
  articles, blog posts, essays, or thought-leadership content. Also trigger when the user
  pastes or links an English markdown article and asks for it in German. Not for DE→EN
  (reverse direction) or for word-for-word translation — this skill produces native German
  prose that preserves the argument but rebuilds the sentences.
---

# Rewrite EN→DE

You take an English article and produce a German version that reads as native German — not translated. English and German professional writing follow fundamentally different textual cultures. A direct translation produces text that is grammatically German but stylistically English: clipped, thin, cold ("hart und dünn"). The English source is a content brief, not a source to translate.

The output conveys the same arguments, evidence, and conclusions, follows German conventions for professional and technical writing, and reads as if it had been conceived in German from the start.

## Setup

Load config per `../../CONFIG.md` ("Applying Config in Skills"). This skill uses:

- **`purpose.md`** — when populated, informs the register and voice of the German output. The source text's own voice still leads; `purpose.md` resolves ambiguity (formal vs. conversational, authoritative vs. exploratory).
- **`settings.md`** — the `## rewrite-de` section holds stylistic choices the skill cannot default safely. Read this section before starting. If the file, the section, or a required field is missing, prompt the user **once** with the options below, save their answers under `## rewrite-de` in `.online-writing/settings.md` (creating file and section as needed, per CONFIG.md writing rules), then proceed. Don't re-prompt on later invocations — the user can edit `settings.md` directly. **Preserve the field format from the CONFIG.md template exactly** — bold label followed by value, e.g. `**Gender style:** Gender colon` — so the file stays machine-readable on subsequent reads.
- **`tonality.md`** — when populated, the German output should reflect the user's defined voice character. The dimension tendencies (commitment, reasoning style, density) apply to the German version — a user who builds toward their point in English should build toward their point in German, not get compressed into declarative statements by the translation process.

### Required settings (prompt if unset)

- **`Gender style:`** how to handle German gendered forms. Offer the full option list from CONFIG.md (Generic masculine, Paired forms, Gender colon *Entwickler:innen*, Gender star *Entwickler\*innen*, Gender gap, Binnen-I, Neutral forms, Mirror source, Ask each time). Give a one-line description of each; let the user pick by name.

### Defaulted settings (use silently unless user overrides in `settings.md`)

- **`Address form:`** default to **Mirror source** — use *Sie* or *du* according to the register of the English source (formal thought leadership → *Sie*; conversational personal essay → consider *du* only if the source uses first-person-you informally). Don't prompt unless the user has explicitly asked to be asked.

Input is a markdown article in English. The user either pastes it directly or provides a file path. If a file path is given, read it first.

---

## Step 1 — Analyse the Source

Before writing anything, internalise:

- **Core thesis** — the single argument the text makes
- **Evidence structure** — what data, examples, or cases support it
- **Rhetorical moves** — how the author builds credibility, creates tension, delivers the payoff
- **Audience assumptions** — what the reader is expected to already know
- **Voice register** — formal Fachtext, conversational thought leadership, polemic, personal essay

You are not about to translate sentences. You are about to rebuild the argument in German prose.

---

## Step 2 — Rewrite in German

Close the English text mentally. Write the German text as if explaining this argument to a sharp, skeptical German reader who has not seen the English version. Apply the **Textkultur rules** below as you write, not as a post-edit pass.

**No elaboration.** Rebuild the argument — do not extend it. Do not introduce claims, examples, specifics, numbers, or parenthetical detail that are not in the source. Length should grow from clause structure (subordination, connective tissue), never from new content. If the German text says something the English text did not, cut it.

---

## German Textkultur Rules

These rules encode the key differences between English and German professional writing. They are the heart of this skill.

### Sentence Architecture

English favours short, punchy sentences. German carries more argumentative weight per sentence through embedded subordinate clauses.

- A good German sentence often runs 20–35 words.
- Three or more sentences under 10 words in sequence signal translated text.
- Use subordinate clauses (*weil, obwohl, wobei, sofern, insofern als, was dazu führt, dass*) to pack context into one sentence instead of spreading it across three.
- Vary length. The goal is rhythm, not uniformity — alternate between shorter and longer sentences.

**Carve-out — deliberate rhetorical parallelism.** Short-sentence streaks are *only* a problem when they come from translated flatness. When the source uses anaphora, tricolon, or parallel fragments as a rhetorical device (*"What to build. What to cut. What to ship."*), the repetition is the device — preserve it in German (*"Was gebaut wird. Was gestrichen wird. Was ausgeliefert wird."*). The test: if you rewrite the fragments into one long sentence, does the argumentative force **increase** (translation smell, rewrite it) or **collapse** (rhetorical device, keep it)?

**What to avoid:**
> KI-Agents automatisieren Aufgaben. Das verändert Organisationen. Manager werden überflüssig.

**What to produce:**
> Indem KI-Agents operative Aufgaben übernehmen, die bislang menschliche Koordination erforderten, verändert sich die Organisationsstruktur grundlegend — mit der Konsequenz, dass klassische Management-Ebenen zunehmend an Daseinsberechtigung verlieren.

### Connective Tissue

German readers expect explicit logical connectors between ideas: *daraus folgt, dies bedeutet konkret, der entscheidende Punkt ist, was auf den ersten Blick widersinnig erscheint, bei genauerer Betrachtung.*

- Avoid the English pattern of juxtaposition (placing two ideas next to each other and letting the reader infer the connection). Spell out the relationship.
- Paragraph transitions should be argumentative, not additive. Instead of *Außerdem…* (which feels like a list), use *Was diese Entwicklung besonders relevant macht, ist…* or *Daraus ergibt sich eine zweite, weniger offensichtliche Konsequenz:*.

**What to avoid (juxtaposition):**
> Viele Unternehmen starten KI-Pilotprojekte. Nur wenige skalieren sie. Die Gründe sind organisatorisch, nicht technisch.

**What to produce (spelled-out relationship):**
> Während zahlreiche Unternehmen KI-Pilotprojekte aufsetzen, gelingt nur einem Bruchteil die Skalierung — und zwar aus Gründen, die sich bei genauerer Betrachtung nicht als technische, sondern als organisatorische Hürden erweisen.

### Tone and Register

- German Fachtexte carry a slightly more formal register than English thought leadership — but they should not sound bureaucratic.
- Avoid the Anglo-Saxon conversational "you" unless the source is explicitly informal. In German professional writing, the reader is addressed implicitly through the argument, not directly.
- Use *wir* sparingly. It works for shared professional context (*als Branche stehen wir vor…*) but rings false when overused.
- The German text should feel **authoritative but not cold, dense but not academic, precise but not stiff**.

### Vocabulary and Phrasing

- Compound nouns are a feature, not a bug: *Koordinationsebene, Entscheidungsautonomie, Wertschöpfungskette*. They signal precision.
- Nominalization is acceptable in moderation. German tolerates it more than English style guides suggest — but overuse makes text feel bureaucratic.

**Loanword vs. anglicism — decision heuristic:**

Keep the English term when **all three** apply:
1. It appears in serious German trade press (Handelsblatt, c't, iX, Süddeutsche Wirtschaft) without translation.
2. It names a specific technical artifact or role, not a generic action (*Pipeline, Agent, Framework, Deployment, Commit, Stakeholder*).
3. The German alternative would be either a stiff coinage (*Rechner* for *Computer*) or ambiguous (*Anbieter* for *Vendor* loses specificity).

Replace with German when **any** applies:
1. It's an English verb spliced with a German ending (*performen, delivern, leveragen, impacten, committen, pushen*). These almost always have a native equivalent.
2. A widely-used German verb or noun fits cleanly (*leisten, liefern, nutzen, beeinflussen, bewirken*).
3. The English reads as corporate jargon rather than professional precision.

**What to avoid:**
> Das Team muss besser performen und Ergebnisse schneller delivern, um den Impact zu maximieren.

**What to produce:**
> Das Team muss schlagkräftiger arbeiten und Ergebnisse schneller liefern, um eine messbare Wirkung zu erzielen.

### Paragraph Structure

- German paragraphs are typically longer than English ones. A paragraph should develop one thought fully.
- "One idea, one paragraph" still applies — but the paragraph earns its length through argument development, not padding.
- Opening a paragraph with context or qualification before the main claim is natural in German (unlike English, which often leads with the punchline).

### Headlines and Subheadings

- German article headlines can be longer and more descriptive than English ones. A German headline often **previews** the argument; an English headline **teases** it.
- Subheadings should be informative, not clever. *Warum Koordination das eigentliche Problem ist* works better than a punchy two-word phrase.

---

## Step 3 — Preserve Metadata

Keep the following from the source unchanged:

- **YAML frontmatter** — translate the `title`, `description`, and `excerpt` fields. Keep `slug`, `tags`, `dates`, and similar identifiers as-is unless the user says otherwise.
- **Markdown structure** — heading levels, code blocks, blockquotes, lists, tables.
- **Links, references, data points, proper nouns** — do not localise.
- **Established tech loanwords** — keep in their English form where they are standard in German tech discourse.

---

## Step 4 — Self-Review

Run these **countable checks** before delivering. Each has a concrete trigger and a concrete action.

| Check | How to run it | Trigger to rewrite |
|---|---|---|
| Short-sentence streak | Scan the text. Flag any stretch of 3+ consecutive sentences under 10 words. | If the streak is deliberate rhetorical parallelism (anaphora, tricolon, parallel fragments mirroring a device in the source) → keep it. Otherwise → merge into subordinate-clause structure. Apply the collapse test from the Sentence Architecture section when unsure. |
| Subordinate-clause density | In any 300-word stretch, count occurrences of *weil, obwohl, wobei, dass, sofern, indem, während*, plus relative pronouns *der / die / das* used subordinately. | Fewer than ~5 across 300 words → the prose is too flat. Rewrite 1–2 paragraphs to add argumentative depth. |
| Additive transitions | Scan paragraph openings. List the connectors used. | If more than one paragraph starts with *Außerdem, Auch, Zusätzlich, Und* (or similar purely additive words), replace with argumentative connectors (*Was diese Entwicklung besonders relevant macht…*, *Daraus ergibt sich…*, *Bei genauerer Betrachtung…*). |
| Anglicism sweep | Search for: *performen, delivern, leveragen, impacten, committen, pushen, aligned, next-level, gemeinsam alignen*. | Any hit → apply the Vocabulary heuristic above. |
| Frontmatter integrity | Re-read the YAML block. | `title / description / excerpt` translated, AND `slug / tags / dates / IDs` untouched? If not, fix. |
| Code and quotes | Check each code block and each direct quote. | Code comments only translated if explanatory; direct third-party quotes untouched with German context around them. |

If any check triggers, **rewrite the affected passage — don't patch it**. A translated sentence cannot be repaired word by word; it has to be rebuilt.

---

## Edge Cases

- **Code blocks** — keep code in English. Comments inside code blocks may be translated if purely explanatory; leave them in English if they are functional (identifiers, API strings, example values referenced elsewhere).
- **Third-party quotes** — keep direct quotes in their original English. Add a German paraphrase or context sentence around them; do not translate someone else's direct words.
- **Data and statistics** — keep numbers, percentages, and data points unchanged. Adjust number formatting to German conventions (comma as decimal separator, period as thousands separator) only if the piece is clearly for a German-only audience.
- **Acronyms** — spell out on first use if not universally known in the German tech community. *LLM* and *API* need no explanation; niche acronyms do.
- **Genuinely uncertain domain terms** — mark inline with `[?]` so the user can review. Do not silently guess.

---

## Output Format

- Deliver the finished German text as markdown.
- Preserve the heading hierarchy from the source.
- Translate the relevant YAML frontmatter fields as noted above.
- Do **not** add translator's notes, commentary, or meta-discussion — only the finished text.

---

## After delivery — soft prompt

After producing the German text, offer one optional next step. Keep it brief and non-blocking — the user decides.

- **Save to a file?** Ask whether to write the output to a file. If yes, ask the user where and what to name it (defer to whatever conventions apply in their environment — don't assume a specific folder layout or naming scheme).

For structural diagnostics on the German version, the user can run `diagnose` against it — the post-structure playbook is language-agnostic for the most part, though German-specific rhythm issues are this skill's responsibility, not `diagnose`'s.

