#writing #online-writing #tonality #german

Universal German register and voice guidance for agents producing German text. Sibling to `tonality-guide.md` (which is language-agnostic at the voice layer). Loaded by `finde-stil`, `analysiere-quelle`, and `schreibe-entwurf`. This file is generic — it applies to every user of the plugin who writes in German, regardless of their personal voice profile in `stil.md`.

Per-user German register overrides live in `.online-writing/stil.md` under "Register by Writing Type." When that section is populated, its tendencies override the defaults described here. The failure modes in this file still apply.

---

## Why This File Exists

LLMs producing German text exhibit two stacked failure modes:

1. **English-coded rhythms.** The model carries the syntactic and rhetorical fingerprint of English thought-leadership into the German output: short-punchy sentence streaks, em-dash drama, punchline-first ordering, setup-reveal cadence. The German is grammatical but stylistically English.
2. **LinkedIn-coded register.** The model carries the genre fingerprint of platform writing into the output: hook-first reveals (*"Was viele nicht verstehen…"*, *"Die Wahrheit ist…"*), performative arcs (hook → lesson → takeaway), engagement-bait closings, marketing intensifiers (*grundlegend, fundamental, massiv*). The German reads as a translated LinkedIn post even when the source was a sober Fachtext.

This file names the patterns, gives concrete examples, and provides German-native register baselines that German content skills can point at. It is the single source of truth for "how German professional prose differs from translated English."

---

## Register Is Not The Same As Voice

A user's voice — the dimensions captured in `stil.md` (commitment, reasoning style, reader relationship, emotional register, density, plus Sachlichkeit ↔ Polemik) — is stable across pieces. The same writer sounds like themselves whether they're writing an opinion piece or a case study.

Register is what shifts. The same writer, writing an opinion piece, commits to a position and defends it. The same writer, writing a case study, describes the thing and lets the specifics carry the credibility.

Register maps roughly to writing type:

| Writing Type | Default German Register |
|---|---|
| Opinion / Essay / These | Argumentativ |
| Credible Talking Head / Fallstudie / Build-Log / Story | Beschreibend |
| Anleitung / Praxisleitfaden | Anleitend |
| Übersicht / Liste / Vergleich | Referierend |

Pieces blend types — a Fallstudie can have argument-tinted edges, an Opinion can have descriptive sequences. The piece's primary job sets the register; secondary tilts get room but don't take over.

---

## Universal Register Baselines

### Beschreibend (Descriptive)

**Sounds like:** Sober, specifics-led, claims earn their place through evidence. Sentences carry weight through subordinate clauses and connective tissue, not through punchy declaration. The author's authority is implicit in the precision of the description, not asserted.

**Failure modes the agent drifts toward:**
- Drifting into Argumentativ — turning a Fallstudie into an Opinion piece by stating a thesis up front and defending it.
- Importing English thought-leadership reveal cadence — *"Was sich auf den ersten Blick X zeigt, entpuppt sich bei näherer Betrachtung als Y."* This construction is a translation tell.
- Closing on a generalization or call to action when the piece's job was to describe the thing and stop.

**What to write instead:** Open with context or specifics, sequence the description, let the reader infer the implications. Close on the thing itself — the project, the system, the case — not on a moral.

### Argumentativ (Argumentative)

**Sounds like:** Committed, hedge-resistant, the thesis sits where the structural framework places it (early for declarative pieces, late for built-up essays). The argument is defended through reasoning and evidence, not through tone.

**Failure modes the agent drifts toward:**
- Collapsing into Sachtext-flat enumeration — listing positions without committing.
- Importing LinkedIn polemic energy — *"Hier ist die unbequeme Wahrheit…"*, *"Was niemand sagt…"*. These feel committed but are performance, not commitment.
- Over-hedging with *möglicherweise, eventuell, könnte, dürfte* stacked in a single sentence — German tolerates one Konjunktiv, not three.

**What to write instead:** State the position clearly. Let qualifications live in subordinate clauses (*sofern, insofern als, wobei*), not in adverb walls. Defend with evidence and reasoning that earns the conclusion.

### Anleitend (Instructional)

**Sounds like:** Imperative, sequenced, no narrative drift. Steps are concrete, ordered, and complete. The reader can act on each step without inferring.

**Failure modes the agent drifts toward:**
- Meandering into essay register — framing the steps as a story, opening each with context the reader doesn't need yet.
- Drifting into Argumentativ when explaining *why* a step matters — replacing the step with an argument for it.
- Burying the action in subordinate clauses (*"Bevor man, sofern die Voraussetzungen erfüllt sind, mit dem Schritt beginnt, sollte…"*) when an imperative would do.

**What to write instead:** State the step. Add the *why* if it's load-bearing for getting the step right; otherwise keep the step terminal.

### Referierend (Referential)

**Sounds like:** Neutral, balanced, no favourite. Each entry gets equivalent treatment. The author's role is curation, not advocacy.

**Failure modes the agent drifts toward:**
- Arguing for one entry — breaking the curation contract by giving the agent's preferred option more space, more positive framing, or a closing recommendation.
- Importing listicle energy from English — *"Diese 5 Tools verändern…"*, *"Die ultimative Liste…"*. German Übersicht writing is sober, not promotional.

**What to write instead:** Give each entry the same shape (description, key trait, who it's for, when it fits). Vary content, not weight. Close on the comparison itself, not on a verdict.

---

## Cross-Cutting German LLM Failure Modes

These patterns leak into German output regardless of register. They are the residual fingerprint of training data that's heavy on translated English thought-leadership and German LinkedIn writing. Each entry: the pattern, an example, why it's wrong, what to write instead.

### English-Coded Rhythms

**Pattern:** Short-punchy sentence streaks (3+ consecutive sentences under 10 words) used outside deliberate rhetorical parallelism.

**Example to avoid:**
> KI-Agents automatisieren Aufgaben. Das verändert Organisationen. Manager werden überflüssig.

**Why it's wrong:** German argumentative weight lives in subordinate clauses, not in juxtaposition. This rhythm is English thought-leadership cadence transliterated.

**Write instead:**
> Indem KI-Agents operative Aufgaben übernehmen, die bislang menschliche Koordination erforderten, verschiebt sich das Gewicht klassischer Management-Ebenen — sie werden nicht abgeschafft, aber ihre bisherige Begründung trägt nicht mehr.

**Carve-out:** Deliberate rhetorical parallelism stays. *"Was gebaut wird. Was gestrichen wird. Was ausgeliefert wird."* — the repetition is the device, preserve it.

---

**Pattern:** Em-dash drama as a setup-reveal device.

**Example to avoid:**
> Die meisten Unternehmen scheitern an KI — nicht an der Technik, sondern an sich selbst.

**Why it's wrong:** This is English Atlantic-essay cadence. The em-dash setting up a punchy reversal is a translation tell.

**Write instead:**
> Die meisten Unternehmen scheitern an KI nicht an der Technik, sondern an organisatorischen Voraussetzungen, die sie vor dem Pilotprojekt hätten klären müssen.

---

**Pattern:** Punchline-first sentence ordering — putting the conclusion at the head of the sentence and following with the explanation.

**Example to avoid:**
> Skalierung ist ein Organisationsproblem, kein Technikproblem.

**Why it's wrong:** German tolerates and often prefers context-before-claim. The punchy lead-with-conclusion is an English structural import.

**Write instead:**
> Wer KI-Pilotprojekte skaliert, stößt nicht auf technische, sondern auf organisatorische Hürden — und scheitert nicht selten an der zweiten Kategorie, weil er sie für die erste hält.

### LinkedIn-Coded Structures

**Pattern:** Hook-first reveals.

**Examples to avoid:**
- *"Was viele nicht verstehen, ist…"*
- *"Die Wahrheit ist…"*
- *"Hier kommt der Punkt…"*
- *"Was Ihnen niemand sagt…"*
- *"Eine unbequeme Erkenntnis…"*

**Why they're wrong:** These are platform-writing devices designed to hook a scrolling reader. They signal performance, not argument. German Fachprosa addresses readers who are already committed to reading.

**Write instead:** Start with the substance. If a contrarian claim is being made, lead with the claim and defend it — don't tease that you're about to make it.

---

**Pattern:** Hook → lesson → takeaway arc.

**Why it's wrong:** This three-act structure is engagement architecture. It treats the reader as an audience to be entertained rather than as a peer to be argued with.

**Write instead:** Use the structural framework appropriate to the piece (Opinion, Fallstudie, Anleitung, Übersicht). The framework's structure is the architecture, not the platform's.

---

**Pattern:** Engagement-bait closings — rhetorical questions or calls to interaction at the end.

**Examples to avoid:**
- *"Was ist Ihre Meinung dazu?"*
- *"Teilen Sie diesen Beitrag, wenn…"*
- *"Schreiben Sie es in die Kommentare."*

**Why they're wrong:** Platform-native engagement signals don't belong in long-form prose. They break the implicit contract of professional writing.

**Write instead:** Close on the argument's natural endpoint. If the close calls for an action by the reader, embed it in the argument, not in a question.

### Marketing-Coded Vocabulary

**Pattern:** Intensifiers used as filler.

**Word list:** *grundlegend, fundamental, massiv, exponentiell, krass, einfach nur, völlig, komplett, total*

**Example to avoid:**
> KI verändert grundlegend, wie Unternehmen arbeiten.

**Why it's wrong:** *Grundlegend* is doing no work — every claim about KI in business writing is "grundlegend." It signals stake-claiming, not analysis.

**Write instead:**
> KI verschiebt, wie Unternehmen arbeiten — am sichtbarsten dort, wo Koordinationskosten bislang den Maßstab gesetzt haben.

---

**Pattern:** Marketing nouns and verbs.

**Word list:** *Game-Changer, Revolution, Disruption, Paradigmenwechsel, neu definieren, transformieren, revolutionieren*

**Why they're wrong:** These are decade-old keynote vocabulary. They claim significance instead of demonstrating it.

**Write instead:** Describe the specific change. If the change is genuinely paradigm-shifting, the description will carry the weight without the label.

### Anglicism Splices

**Pattern:** English verb stems with German conjugation endings.

**Word list:** *performen, alignen, delivern, leveragen, impacten, committen, pushen, sich aligned, gemeinsam alignen, next-level, mind-blowing*

**Example to avoid:**
> Das Team muss besser performen und Ergebnisse schneller delivern, um den Impact zu maximieren.

**Why it's wrong:** These are corporate Denglisch. Native German verbs cover every case more precisely.

**Write instead:**
> Das Team muss schlagkräftiger arbeiten und Ergebnisse schneller liefern, um eine messbare Wirkung zu erzielen.

### Stock Translation Patterns

**Pattern:** Constructions that betray a translation pass even when the words are German.

**Phrase list:**
- *"Was auf den ersten Blick X erscheint, entpuppt sich bei näherer Betrachtung als Y"* — overused as a reveal device
- *"und zwar…"* — punchy connector trying to dramatize
- *"in der Tat"* — filler, used where English would say *"indeed"*
- *"letztendlich"* — used as throat-clearing
- *"in der heutigen Welt"* / *"im heutigen Zeitalter"* — translated *"in today's world"*
- *"bei genauerer Betrachtung"* — fine once, but stock filler when repeated
- *"Es ist wichtig zu erwähnen, dass…"* — translated *"it's important to note"*

**Why they're wrong:** Each one signals "I was thinking in English while writing this." Collectively they make German prose feel translated even when it isn't.

**Write instead:** When the same logical move is needed, use direct German constructions: *"Was wie X aussieht, ist tatsächlich Y"* / *"konkret heißt das"* / *"genauer gesagt"* / *"freilich"* / *"allerdings"*. And use them sparingly.

### Conversational-You Overuse

**Pattern:** Direct *du* or *Sie* address used to address the reader where implicit reader-address is more native.

**Example to avoid:**
> Sie kennen das Problem: Sie starten ein Pilotprojekt, Sie sehen erste Ergebnisse, und dann passiert nichts mehr.

**Why it's wrong:** German Fachprosa addresses the reader implicitly through the argument, not directly. Repeated *Sie* feels like a presentation script.

**Write instead:**
> Das Muster ist bekannt: Ein Pilotprojekt zeigt erste Ergebnisse, doch danach versickert es. Skalierung scheitert nicht an der Technik, sondern an organisatorischen Voraussetzungen.

**Carve-out:** Personal essay register and conversational instructional register both tolerate direct address. The failure mode is direct address in argumentative or descriptive register where it doesn't belong.

---

## Universal German Textkultur Rules

These are language-level rules, distinct from register or voice. They apply to all German prose produced by the pipeline regardless of who is writing or what register they're writing in.

### Sentence Architecture

English favours short, punchy sentences. German carries argumentative weight per sentence through embedded subordinate clauses.

- A working German sentence often runs 20–35 words.
- Three or more sentences under 10 words in sequence signal translated text (carve-out: deliberate rhetorical parallelism).
- Subordinate clauses pack context into one sentence: *weil, obwohl, wobei, sofern, insofern als, was dazu führt, dass*.
- Vary length. The goal is rhythm, not uniformity.

### Connective Tissue

German readers expect explicit logical connectors between ideas. Avoid English juxtaposition (placing two ideas next to each other and letting the reader infer the connection).

- Argumentative connectors (use these): *daraus folgt, dies bedeutet konkret, der entscheidende Punkt ist, was diese Entwicklung besonders relevant macht, bei genauerer Betrachtung* (sparingly).
- Additive connectors (avoid as paragraph openers): *Außerdem, Auch, Zusätzlich, Und, Darüber hinaus*.
- The *Außerdem* trap: when paragraph openings stack additive connectors, the prose reads as a list. Replace with argumentative ones that name the relationship between paragraphs.

### Compound Nouns and Nominalization

Compound nouns are a feature: *Koordinationsebene, Entscheidungsautonomie, Wertschöpfungskette*. They signal precision.

Nominalization is acceptable in moderation. German tolerates it more than English style guides suggest, but overuse makes prose feel bureaucratic. The tip-over point: when a sentence has three or more nominalizations and no concrete verbs, rewrite at least one as a verb.

### Loanword vs. Anglicism Heuristic

**Keep the English term when all three apply:**
1. It appears in serious German trade press (Handelsblatt, c't, iX, Süddeutsche Wirtschaft) without translation.
2. It names a specific technical artefact or role, not a generic action (*Pipeline, Agent, Framework, Deployment, Commit, Stakeholder, Workflow*).
3. The German alternative would be either a stiff coinage or ambiguous (*Rechner* for *Computer*, *Anbieter* for *Vendor*).

**Replace with German when any applies:**
1. It's an English verb spliced with a German ending (*performen, delivern, leveragen, impacten*).
2. A widely-used German verb or noun fits cleanly (*leisten, liefern, nutzen, beeinflussen, bewirken*).
3. The English reads as corporate jargon rather than professional precision.

### Paragraph Structure

- German paragraphs are typically longer than English ones. A paragraph develops one thought fully.
- "One idea, one paragraph" still applies — but the paragraph earns its length through argument development, not padding.
- Opening a paragraph with context or qualification before the main claim is natural in German (unlike English, which often leads with the punchline).

### Headlines and Subheadings

- German article headlines can be longer and more descriptive than English ones. A German headline often previews the argument; an English headline teases it.
- Subheadings should be informative, not clever. *Warum Koordination das eigentliche Problem ist* works better than a punchy two-word phrase.

---

## Source-Character Handling

Guidance for `analysiere-quelle` on how to treat each source type when extracting a brief.

| Source character | What to expect | What to drop | What to preserve |
|---|---|---|---|
| English thought-leadership | Strong English-coded rhythms, LinkedIn structures, marketing vocab | Hook-first reveals, em-dash drama, punchline-first ordering, intensifier vocab | Argument structure, evidence, data, third-party quotes |
| English Fachtext / sober writing | Fewer LinkedIn tells, but still English rhythms | Punchline-first ordering, short-punchy streaks if not deliberate | Argument, evidence, technical specificity |
| German Fachtext | Already in target register | Anglicism splices if any, marketing intensifiers if any | Everything else |
| German LinkedIn / blog | LinkedIn-coded structures even though German | Hook-first reveals, engagement-bait closings, marketing vocab | Argument and evidence |
| Brain dump (any language) | Fragmentary, unstructured | N/A — no source register to drop from | Every load-bearing claim, every concrete example |
| Transcript | Spoken-word patterns, repetition, filler | Filler, false starts, repetition unless rhetorical | Argument, examples, the speaker's framing |

---

## Anti-Templates

Concrete bad-output examples paired with what to write instead. Drawn from the failure-mode catalogue above. Useful for `schreibe-entwurf`'s self-review pass — pattern-match against these, not just against rule descriptions.

### Anti-Template 1: LinkedIn-coded thought leadership

**What to avoid:**
> Was viele Manager nicht verstehen: KI verändert nicht ihre Werkzeuge — sie verändert ihre Daseinsberechtigung. Die meisten reagieren mit mehr Prozessen. Sie sollten weniger machen. Hier ist die unbequeme Wahrheit.

**What's wrong:**
- Hook-first reveal (*"Was viele Manager nicht verstehen…"*)
- Em-dash drama for setup-payoff
- Marketing intensifier (*Daseinsberechtigung* used as a punchy noun)
- Short-punchy streak in the middle
- Tease-the-reveal closing (*"Hier ist die unbequeme Wahrheit"*)

**What to produce:**
> Die Reaktion vieler Führungskräfte auf KI-Agents besteht darin, neue Steuerungsprozesse einzuziehen — eine Reaktion, die zur Lage des bisherigen Managements passt, aber nicht zur Lage, die KI-Agents tatsächlich erzeugen. Wenn operative Koordination zunehmend von Agents übernommen wird, verlagert sich die Aufgabe von Führung; das schmälert sie nicht, aber es verändert, woran sie sich messen lassen muss.

### Anti-Template 2: Translated tech press

**What to avoid:**
> Das Team konnte 30% schneller delivern, nachdem wir den neuen Workflow gepusht haben. Der Impact war massiv. Wir haben unsere KPIs grundlegend neu definiert.

**What's wrong:**
- Anglicism splices (*delivern, gepusht*)
- Marketing intensifiers (*massiv, grundlegend neu definiert*)
- Anglicism noun (*Impact* — *Wirkung* fits)
- *KPIs* is fine if the audience is a tech/product team; for a generalist audience, replace with *Kennzahlen*

**What to produce:**
> Das Team lieferte nach Einführung des neuen Workflows etwa 30% schneller. Die Wirkung war so deutlich, dass wir unsere Kennzahlen anpassen mussten — sie unterscheiden inzwischen zwischen Liefergeschwindigkeit und Lieferqualität, weil die alte Zusammenfassung beides verdeckt hätte.

### Anti-Template 3: Translated essay close

**What to avoid:**
> Letztendlich ist KI nichts weiter als ein Werkzeug. Es liegt an uns, was wir damit machen. Die Zukunft gehört denen, die jetzt handeln.

**What's wrong:**
- *Letztendlich* as filler-throat-clearing
- Truism close (*"nichts weiter als ein Werkzeug"*)
- Motivational-poster ending (*"Die Zukunft gehört…"*)

**What to produce:**
> Welche Wirkung KI auf eine konkrete Organisation hat, hängt weniger von der Technik ab als von den Voraussetzungen, unter denen sie eingeführt wird — und genau diese Voraussetzungen lassen sich, anders als die Technik, nicht einkaufen, sondern müssen erarbeitet werden.

---

## Reload Rule

When refining or rewriting German prose across multiple passes, reload this file on every pass alongside `stil.md`. Voice and register drift in multi-turn rewriting regresses toward training-data defaults — translated English thought-leadership and LinkedIn-coded register. Treat both files as load-bearing for every iteration, not just the first draft.
