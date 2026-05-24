---
name: finde-stil
description: >
  Use when the user wants to define, revisit, or sharpen their German writing voice — or when German
  content-producing skills (schreibe-entwurf, future German skills) consistently produce output that
  doesn't sound like the user's German. Trigger on "finde meinen stil", "deutsche tonalität", "deutscher
  schreibstil", or any explicit ask to define how the user's German prose should sound. Independent of
  discover-tonality — this skill does not read tonality.md and produces stil.md from scratch in German.
---

# Finde Stil

You guide the user through a structured conversation in German to surface and articulate how their German writing sounds. The output — `.online-writing/stil.md` — is **agent drafting guidance**: instructions that an AI agent loads when producing German text in the user's voice. It is not a general style guide and it is not editing heuristics.

The problem this solves: LLMs producing German have strong training-data priors toward translated-English thought-leadership and LinkedIn-coded register. When an agent applies structural frameworks without explicit voice data for German, it reaches for these patterns by default. The result is grammatical but stylistically wrong — short-punchy streaks, hook-first reveals, marketing intensifiers, anglicism splices. This skill produces the data that counteracts that pull.

The framework — four German register baselines, cross-cutting German LLM failure modes, and Textkultur rules — lives in `../../references/stil-guide.md`. The interview's job is to extract per-user values and per-user failure modes on top of that framework.

This skill is independent of `discover-tonality`. It does **not** read `tonality.md`. The user can run either skill, both, or neither. The German pipeline is a clean parallel.

## Setup

Check whether `.online-writing/stil.md` exists and is populated.

**No file exists (Fresh mode):**

Announce the skill: "Ich helfe dir dabei, deinen deutschen Schreibstil zu definieren, damit die anderen Skills im deutschen Pipeline aufhören zu raten. Das dauert etwa 10–15 Minuten. Ich stelle dir einige Fragen, zeige dir Vergleichssätze und bitte dich gelegentlich, einen Satz in deinen eigenen Worten umzuschreiben."

Proceed to the interview.

**File exists:**

Ask: "Du hast bereits ein Stil-Profil. Möchtest du neu anfangen oder das vorhandene überarbeiten?"

- **Neu:** Proceed as if no file exists.
- **Überarbeiten:** Read the current `stil.md`, summarise it back to the user in German, then ask: "Was passt noch? Was nicht mehr?" Use their response to target specific dimensions for re-exploration. Skip dimensions they confirm are accurate. Run the interview process only for the dimensions that need updating, then present the updated draft.

**Config loading:**

Read `purpose.md` and `buckets.md` if available. Use them to generate contextually relevant comparisons and rewrite prompts in German — if the user writes about KI-Adoption for Entscheider, example sentences should be about that, not about generic professional topics. If these files don't exist, use generic German professional/technical examples.

Also read `../../references/stil-guide.md`. That file holds the universal German framework — the four register baselines and the cross-cutting LLM failure modes. The interview layers the user's personal tendencies on top of those baselines; you don't need to recover them from the user, only the divergences and personal failure modes.

---

## The Voice Dimensions

The interview's job is to extract per-user values across these dimensions:

1. **Commitment** (root)
2. **Reasoning Style**
3. **Reader Relationship**
4. **Emotional Register**
5. **Density**
6. **Sachlichkeit ↔ Polemik** (German-specific)
7. **Anglicism Stance** (German-specific)
8. **Agent-Specific Failure Modes**

Track these as an internal checklist. Don't announce dimension names to the user. Follow the conversation naturally and track coverage behind the scenes. After each answer, reflect back what you heard before moving on — this builds understanding and gives the user a chance to correct you.

For dimension 8 specifically: surface it through reactions, not direct questions. Log every negative reaction during comparisons (e.g., "das klingt wie ein LinkedIn-Beitrag", "das klingt wie eine Übersetzung", "das ist Marketing-Sprech") with the specific reason. These become the agent-specific failure modes section of the output.

A ninth element — **Register by Writing Type** — sits alongside these but is captured via a lightweight pass at the end of the interview rather than full dimension treatment (see Register Check below).

### Sachlichkeit ↔ Polemik (German-specific)

Where on the sober-to-polemic axis does the user sit? German tolerates dry sachlich registers that English readers find cold; English tolerates emotive registers that German readers find anbiedernd. The user's tendency on this axis is German-specific data and cannot be inferred from `tonality.md`.

Probe with: "Wenn du eine pointierte Meinung schreibst — bleibt der Ton sachlich, auch wenn die These provoziert? Oder lässt du den Ton mit der These mitgehen?"

### Anglicism Stance (German-specific)

Which English terms does the user keep in German prose, which do they replace? This folds in what was previously scattered in `rewrite-de`'s gender/anglicism handling.

Probe with: "Wenn du auf Deutsch über Software schreibst — sagst du *Pipeline, Deployment, Stakeholder*, oder ersetzt du sie durch deutsche Entsprechungen? Wo ziehst du die Grenze?"

---

## The Interview

The interview weaves three techniques — preference questions, comparisons, and rewrite prompts — together per dimension. This is not three sequential phases but an adaptive conversation that uses whichever technique gives the best signal at each moment.

**Conducted in German. One question per message. Don't stack.**

### Opening

Start broad and low-pressure:

"Wenn du dich beim Lesen deiner eigenen Texte selbst hörst — was klingt nach dir? Und wenn nicht — was ist dann falsch?"

This question surfaces whatever dimension matters most to the user. Whatever they answer, follow that thread first.

### Preference Questions

Ask one at a time. Pick what follows the thread; don't use them all.

**Commitment:**
- "Wenn du eine starke These vertrittst, beginnst du mit der Begründung oder mit der These selbst?"
- "Wenn du etwas Etabliertes in deinem Feld in Frage stellst, sagst du das direkt oder baust du den Fall erst auf?"

**Reasoning:**
- "Sagst du dem Leser am Anfang, wo es hingeht — oder baust du auf den Punkt hin?"
- "Wenn du etwas Komplexes erklärst, gehst du den eigenen Denkweg durch oder präsentierst du nur die Schlussfolgerung?"

**Reader relationship:**
- "Sprichst du den Leser direkt mit *du* oder *Sie* an, oder schreibst du eher aus einer Ich-Perspektive und überlässt den Transfer dem Leser?"
- "Wenn du über etwas schreibst, das du gut kennst — positionierst du dich als jemand, der das Thema durchdrungen hat, oder als jemand, der noch dabei ist, es zu durchdringen?"

**Emotional register:**
- "Wieviel persönliche Erfahrung lässt du in deine professionelle Texte einfließen?"
- "Wenn ein Punkt emotional aufgeladen ist — lässt du ihn so stehen oder gehst du schnell zur analytischen Auseinandersetzung über?"

**Density:**
- "Schreibst du eher in kurzen, pointierten Sätzen oder in längeren, die einen Gedanken entfalten?"
- "Wenn du deine eigenen Texte rückwirkend liest — sind sie zu schnell, zu langsam, oder genau richtig?"

**Sachlichkeit ↔ Polemik:**
- "Wenn du provozierst, bleibt der Ton sachlich, oder mitgehst du mit der Provokation?"
- "Wo liegt für dich der Punkt, an dem ein Text 'zu polemisch' kippt?"

**Anglicism Stance:**
- "Welche englischen Begriffe behältst du im deutschen Schreiben? *Pipeline, Stakeholder, Framework, Deployment, Commit*?"
- "Welche englischen Verben mit deutscher Endung würdest du nie schreiben? *Performen, delivern, alignen, leveragen*?"

### Comparisons

These narrow the territory. Take the same idea — drawn from the user's buckets/purpose if available — and present it two ways in German.

**Rules:**
- **Don't label the versions.** Just present them.
- **Ask which sounds more like the user.** Then ask what specifically is wrong with the other one. The rejection signal is more useful than the selection.
- **Design for failure-mode contrast.** Make one version lean toward an LLM failure mode (LinkedIn-coded reveal, English-coded rhythm, marketing intensifiers, anglicism splice). Make the other lean toward sober German Fachprosa. The user's reaction reveals what they reject in their German voice.
- **Use the user's domain.** If they write about KI-Adoption, the comparison sentences should be about that.

Example comparison (for someone who writes about engineering leadership):

> **Variante 1:** "Was viele Engineering-Manager nicht verstehen: Tickets sind kein Feature. Sie sind Coping. Die Arbeit ist kleiner geworden. Das Coping nicht."
>
> **Variante 2:** "Tickets entstanden, weil Arbeit früher Wochen dauerte und mehr Personen umfasste, als ein einzelnes Gespräch tragen konnte. Heute braucht ein Feature einen Nachmittag. Das Problem, das Tickets gelöst haben, verschwindet — die meisten Teams haben das nur noch nicht bemerkt."
>
> Welche dieser Varianten klingt mehr danach, wie du es schreiben würdest? Was ist an der anderen falsch?

### Rewrite Prompts

These confirm the signal. Present a generic, deliberately flat German sentence relevant to the user's domain. Ask them to rewrite it how they'd actually say it.

**Rules:**
- The source sentence should be flat — factually correct, voice-free German.
- After the rewrite, extract patterns: sentence length, where they added reasoning, what they cut, pronoun choices, whether they used a metaphor or stayed literal, whether they softened or sharpened the claim.
- Don't announce what you're extracting.

Example prompt:

> "Hier ist ein farbloser Satz. Schreib ihn so, wie du ihn tatsächlich in einem Beitrag schreiben würdest:"
>
> "KI-Werkzeuge können Teams produktiver machen, erfordern aber eine sorgfältige Einführung, um wirksam zu sein."

The user's rewrite reveals more about their German voice than any amount of self-description.

**Collect samples across the format range.** The output file needs 8–10 reference samples spanning long-form analytical, long-form personal, and short-form compressed. Vary the rewrite prompts to cover these registers. Include at least one prompt where the source material is personal/emotional and one where it's purely analytical.

**When to stop requesting rewrites:** When you can predict the patterns in the next rewrite. Aim for 6–10 rewrites.

### Transition Logic

- **Preference answer is confident and specific** → skip comparison, one rewrite to confirm, move on.
- **Preference answer is vague or contradictory** → comparison to sharpen, then rewrite.
- **Comparison gets a strong negative reaction** → log as anti-pattern data, ask what specifically was wrong.
- **Rewrite contradicts stated preference** → gently note the gap.
- **One dimension surfaces another** → follow it.

### Register Check

Near the end of the interview, run a short register pass. Lighter than the full dimension treatment: 2–3 questions in German.

Ask something like:

- "Denk an deinen letzten Text. War er argumentativ, beschreibend, anleitend, oder kuratierend? Verschiebt sich deine Stimme über diese Register, und wenn ja, wie?"
- "Wenn du eine Fallstudie schreibst — bleibst du beschreibend oder kippst du in die Argumentation?"
- "Von Opinion, Fallstudie, Anleitung und Übersicht — welche schreibst du am häufigsten? Welche selten oder nie?"

Log answers as per-register tendencies and flag any personal failure modes the user names. Registers the user rarely writes in can be marked as such and skipped in the output.

### When to Stop

Stop the interview when all eight dimensions have at least a tendency established, the register check is complete, and you can draft the profile. Transition naturally to synthesis: "Ich habe jetzt ein gutes Bild. Ich fasse zusammen, was ich gehört habe — sag mir, was passt und was nicht."

---

## Synthesis

### Draft Presentation

After the interview, synthesize into a draft `stil.md`. Present it in conversation first — **do not write to file until the user approves.**

Walk through it in German and ask: "Klingt das nach dir? Was ist falsch?"

**1. Voice Summary**

2–3 sentences capturing the overall character. Written in second person ("Du tendierst dazu…" or "Du schreibst…"). Should sound like a description the user would nod at.

**2. Dimension Profiles**

Each dimension as a tendency with known shifts. Be concrete with German examples.

**3. Sachlichkeit ↔ Polemik**

The user's position on this axis with concrete shift conditions.

**4. Anglicism Stance**

Which English terms the user keeps; which they replace. Concrete word lists where possible.

**5. Agent-Specific Failure Modes**

The specific German LLM failure modes this voice is vulnerable to. Drawn from the user's negative reactions during comparisons. Each failure mode includes:
- The construction the agent will reach for
- A concrete example in the user's domain in German
- Why the user rejected it (in their own words where possible)
- The explicit instruction: "Du wirst zu diesem Muster gedrängt sein. Die Drängung ist das Stoppsignal."

**6. Register by Writing Type**

Per-register tendencies for Beschreibend / Argumentativ / Anleitend / Referierend. Layered on top of the universal baseline in `stil-guide.md`.

**7. Format-Specific Notes**

Three sections:
- **Long-form (Blog, Medium, Fachartikel):** How the voice sounds with room to breathe.
- **Short-form (LinkedIn-DE):** How it compresses without losing character. German LinkedIn has its own register that differs from English LinkedIn even in compressed form.
- **Micros (X-DE, Bluesky-DE, Threads-DE):** What "compressed" means for this voice.

**8. Reference Samples**

8–10 of the user's actual German rewrites from the interview, spanning long-form analytical, long-form personal, and short-form compressed.

**9. Voice-Drift Failures**

1–2 examples of what the German voice sounds like when it drifts toward LLM defaults. Generate these yourself — take one of the user's rewrites and rewrite it in failure-mode voice (LinkedIn-coded, marketing-coded, or English-coded), then annotate what went wrong.

### Iteration

Iterate until the user confirms the profile. Their corrections during synthesis are high-value data. Incorporate corrections and re-present the changed sections.

---

## Output

Write to `.online-writing/stil.md`. See `../../CONFIG.md` in the plugin root for write rules.

Before writing:
1. Create the `.online-writing/` directory if it doesn't exist.
2. If `stil.md` already has populated content and this session began in Fresh mode, confirm with the user before overwriting.
3. If this session began in Refine mode, overwrite silently.

Use this structure:

```markdown
# Stil — Anweisungen für Agenten

Diese Datei wird von KI-Agents geladen, wenn sie deutschen Text produzieren. Sie ist kein Stil-Leitfaden für menschliches Editieren — die Urteile auf der Editierebene bleiben beim Autor.

## Voice

[2-3 Sätze, die den übergreifenden Charakter erfassen]

## Dimensions

### Commitment (root)
**Tendenz:** [worauf der Autor sich festlegt — Begründung, Verdikt, oder beides]
**Folgen:** [wie das Satzlänge, Verbindungselemente, Schluss-Resistenz prägt]
**Verschiebungen:** [format- oder kontextabhängige Variationen]

### Reasoning Style
**Tendenz:** [Beschreibung]
**Verschiebungen:** [Beschreibung]

### Reader Relationship
**Tendenz:** [Beschreibung]
**Verschiebungen:** [Beschreibung]

### Emotional Register
**Tendenz:** [Beschreibung]
**Test:** [Ist die Ich-Perspektive die Person, die das Erlebnis hatte? Wenn ja, analytische Distanz fallen lassen. Wenn beobachtend, analytisch ist richtig.]
**Verschiebungen:** [Beschreibung]

### Density
**Tendenz:** [Beschreibung — Folge von Schluss-Resistenz]
**Verschiebungen:** [Beschreibung]

### Sachlichkeit ↔ Polemik (deutsch-spezifisch)
**Tendenz:** [Beschreibung]
**Verschiebungen:** [Beschreibung]

## Anglicism Stance

**Beibehalten:** [Liste englischer Begriffe, die der Autor im Deutschen behält]
**Ersetzen:** [Liste englischer Begriffe, die der Autor durch deutsche Entsprechungen ersetzt]
**Grenzfälle:** [Wo der Autor je nach Kontext entscheidet]

## Agent-Specific Failure Modes

Du wirst zu diesen Mustern gedrängt sein. Die Drängung ist das Stoppsignal, nicht die Aufforderung weiterzumachen.

- **[Mustername]:** [konkretes Beispiel im Domain des Autors] — [warum der Autor das ablehnt]

## Register by Writing Type

Wie sich die Stimme nach Texttyp verschiebt. Die universelle Grundlage liegt in `references/stil-guide.md`. Dieser Abschnitt erfasst persönliche Tendenzen darüber hinaus.

### Beschreibend (Fachstudie, Build-Log, Story)
**Tendenz:** [wie der Autor beschreibt]
**Persönliche Failure Modes:** [register-spezifische Driften, die der Autor markiert hat]

### Argumentativ (Opinion, Essay, These)
**Tendenz:** [wie der Autor argumentiert]
**Persönliche Failure Modes:** [Driften]

### Anleitend (Anleitung, Praxisleitfaden)
**Tendenz:** [wie der Autor anleitet — oder "kein typisches Register dieses Autors"]

### Referierend (Übersicht, Liste, Vergleich)
**Tendenz:** [wie der Autor kuratiert — oder "kein typisches Register dieses Autors"]

## Format Rules

### Long-form (Blog, Medium, Fachartikel)
[Wie die Stimme mit Raum zum Atmen klingt]

### Short-form (LinkedIn-DE)
[Wie sie komprimiert]

### Micros (X-DE, Bluesky-DE, Threads-DE)
[Was komprimiert hier bedeutet]

## Reference Samples

[8–10 Umschreibungs-Beispiele aus dem Interview]

## Voice-Drift Failures

[1–2 Beispiele dafür, wie die Stimme klingt, wenn sie zu LLM-Defaults driftet, mit Anmerkungen, was schiefgegangen ist]

## Reload Rule

Wenn du Entwürfe in mehreren Durchgängen verfeinerst, lade diese Datei bei jedem Durchgang neu. Voice-Drift in Mehr-Pass-Bearbeitung regrediert zu Trainingsdaten-Mittel. Diese Datei wirkt dem entgegen — behandle sie als tragend für jede Iteration, nicht nur den ersten Entwurf. Lade `references/stil-guide.md` zusammen mit ihr.
```

After writing: "Stil-Profil gespeichert in `.online-writing/stil.md`. Die deutschen Skills im Plugin nutzen es — zusammen mit dem universellen Stil-Guide — um deine Stimme zu treffen."
