---
name: headlines
description: >
  Use when the user wants headlines generated, workshopped, or iterated on — either for an
  existing draft, a topic brief without a draft yet, or a published piece that needs sharper
  options. Triggers include "give me headlines", "headline variants", "rework this title",
  "write headlines for", "titles for this post", "help me with the headline". Also use when a
  user shows a draft and asks what to call it, or when an existing headline underperforms and
  they want alternatives. Not for full-post generation (see create-post / create-draft) or for
  diagnosing a finished piece's quality (see rate / diagnose).
---

# Headlines

You workshop headline variants using the playbook from *The Art and Business of Online Writing* (Chapter 7). A headline is a micro-version of the entire piece: it declares **what** the piece is about, **who** it's for, and **the promise** it makes to the reader — without giving the answer away. That tension is the Curiosity Gap.

One draft is never enough. Buzzfeed's rule is 30 variants per headline before picking. This skill produces a range, ranks them, and hands the user a shortlist they can choose from.

## Setup

Load config per `../../CONFIG.md` ("Applying Config in Skills"). This skill uses:

- **`purpose.md`** — aligns voice and category positioning. The headline should plausibly serve the user's Motivation, Audience, Category, POV, and Vision.
- **`buckets.md`** — identifies whether the piece targets the General, Niche, or Industry bucket, which changes the headline strategy (universal question vs. niche-specific question vs. niche-topic-answering-universal-question).

**Reference:** The core headline rules live in `../../references/post-structure-guide.md` (The Headline, Curiosity Gap, Anatomy, Proven Formats, Headline Rules). Read that section before generating. Do not restate its content inline — apply it.

---

## Step 1 — Gather the brief

Determine which mode the user is in:

| Mode | What the user gives you | What you need to do first |
|---|---|---|
| **Draft present** | A full or partial piece of writing | Read it. Extract the core argument, evidence, and voice. |
| **Topic brief** | A topic, a claim, or notes without a draft | Ask 2–3 tight questions to pin down the What / Who / Promise. Don't over-interrogate. |
| **Existing headline** | One or more current headlines they want alternatives to | Read the current headline(s), identify what they're promising and who to, then widen the variant set. |

**Before generating, you must be able to answer these three questions in one sentence each:**

- **What** is the piece about? (One specific claim or topic, not a theme.)
- **Who** is it for? (The narrowest honest audience — not "everyone.")
- **Promise** — what does the reader walk away with? (A problem solved, a tension resolved, an insight delivered.)

If any of the three is fuzzy, pause and ask the user. Headlines generated from a fuzzy brief come out generic no matter how many variants you produce.

---

## Step 2 — Generate variants across formats

Produce **25–30 variants**, distributed across the proven formats from `post-structure-guide.md`. Don't write 30 of the same format — the point of a wide set is to see which shape of headline serves this specific piece best.

Rotate through these formats (use each at least once when plausible):

- **X Number** — *"7 Things Every Junior PM Gets Wrong About Sprint Planning"*
- **Big Number** — emphasise scale: *"The $2.3B Mistake Most SaaS Founders Make in Year One"*
- **Dollar Signs** — widens the Curiosity Gap
- **Credible Names** — leverages borrowed authority: *"What Paul Graham Got Wrong About Solo Founders"*
- **This Just Happened** — urgency/insider framing: *"The One Thing Every VC Emailed Me About This Week"*
- **The Success Story** — a rare or amazing outcome
- **Things That Shouldn't Go Together** — unexpected juxtaposition
- **For The Industry** — call out the niche directly: *"For CTOs Who've Inherited a Legacy Monolith"*
- **Topic Within The Topic** — primary headline with a second in parentheses: *"How to Raise a Seed Round in 2026 (And the Pitch Deck Mistake That Kills 8 of 10 Rounds)"*
- **Question/Answer** — pose a question, hint at the answer
- **Contrarian/Reframe** — flip the common belief: *"Why Your OKRs Are Actually Destroying Your Team's Focus"*

Use the anatomy template as a construction tool:

> **The 1** ==Question== \*That Gets\* *Every Single Millennial* {In Trouble}

Where each slot answers:
- **The 1** — number conveying conviction
- **Question** — reason / way / solution / problem
- **That Gets** — strong, conversational verb (gets, incentivises, pushes, encourages, destroys, rescues, breaks)
- **Every Single Millennial** — the Who, narrowed (age / role / location / interest / niche, then the Who within the Who)
- **In Trouble** — the promise

Not every headline needs all five slots. The template is a construction checklist, not a mould.

**Apply the Rules while generating (p. 182, 184):**

- Declare the content, the promise, and the audience.
- **Eliminate every "tiny word"** that doesn't pull weight (*a, the, just, very, really, actually, kind of, some, maybe*).
- Add **power phrases** where they earn their place: *crucial, unforgettable, memorable, eye-opening, painful, emerging, brutal, invisible, silent, unavoidable*.
- No clickbait lies. The promise must be one the piece can actually deliver, or the reader feels cheated (p. 149).

---

## Step 3 — Score and filter

Evaluate each variant in two passes.

### Pass 1 — Deliverability gate (binary; drop, don't demote)

For every variant, ask: **can the actual draft or brief fulfil this headline's promise?** If the piece can't deliver what the headline sells, drop the variant. Not demote — drop. A headline the reader feels cheated by loses them permanently (p. 149).

This gate is where clever but dishonest variants die. It matters most when you've been generating widely: the variety that makes a good shortlist also produces headlines that drift past what the piece actually argues.

**The rule is strict.** Any added claim the brief doesn't support fails the gate — a count (*"5 reasons", "4 clicks", "3 ways"* when the brief doesn't specify the number), a location (*"support forums ignore it"* when the brief doesn't talk about forums), a motive (*"Microsoft buried it"* when the brief doesn't claim intent), a critique (*"Zoom's docs are wrong"* when the brief doesn't argue that), an implied novelty (*"emerging bug", "just discovered"* when the brief doesn't claim newness), a stat (*"99% of users", "most companies"* when the brief has no data). Small embellishments are still embellishments — drop them. The rule applies symmetrically: two variants making equivalent out-of-brief claims must both be dropped.

### Pass 2 — Score surviving variants on three dimensions (1–5 each)

| Dimension | What to check | Source |
|---|---|---|
| **Triangle complete** | Are **What**, **Who**, and **Promise** all visible in one read? If any one of the three is missing or muddy, score low. | p. 164 |
| **Curiosity Gap** | Does it hint at the answer without revealing it? If a reader can guess the piece's conclusion from the headline alone, the Gap is closed — score low. | p. 165 |
| **Construction hygiene** | Four sub-checks: (1) concrete specifics present (number, named role, artifact); (2) every "tiny word" eliminated (*a, the, just, very, really, actually, some, maybe, kind of*); (3) at least one strong descriptive verb (*gets, incentivises, pushes, destroys, rescues, breaks*); (4) power phrase only where it earns its place (*crucial, painful, unforgettable, silent, brutal, invisible, emerging*). Each sub-check is roughly ±1 on the score. | p. 176, 182, 184 |

**Demote on any dimension below 3. From what survives, pick the Top 10.**

The Top 10 should show **variety of format**. Avoid delivering 10 X-Number variants or 10 Question/Answer variants — the user should see the headline decision as a genuine choice of frame, not just wording.

---

## Step 4 — Deliver

Present the output in this structure:

```markdown
# Headlines — [piece topic]

**What:** [one sentence]
**Who:** [one sentence]
**Promise:** [one sentence]

---

## Top 10 Candidates

### 1. [format, e.g. "X Number"]
> [the headline]
*Why it works:* [one short line on the hook]

### 2. [format]
> [the headline]
*Why it works:* [one short line]

... (through 10)

---

## Other Variants Generated

[The remaining 15–20 variants as a bulleted list, grouped by format. No commentary — they're there for the user to browse in case the Top 10 misses the angle they wanted.]

---

## Notes

[Only if something came up: a tension between the draft's promise and the strongest headlines, a missing piece of the What/Who/Promise triangle, or a suggestion to adjust the draft's intro to match the winning headline. Keep to 1–2 sentences.]
```

---

## After delivery — soft prompt

After delivering the shortlist, offer one optional next step. Keep it brief and non-blocking.

- **Tighten a specific candidate?** If the user wants to workshop one further, rewrite it 5–10 more ways holding the shape constant (same format, different wording / numbers / verbs).
- **Check alignment with intro?** If a draft is present and the user has picked a headline, offer to check whether the intro delivers on the headline's promise (see `diagnose` for the full structural check; for headline↔intro specifically, the check is short enough to do inline).
- **Save to the draft?** Ask whether to write the chosen headline into their draft file. If yes, ask where in the file to place it.

---

## Edge cases

- **Fuzzy brief that the user refuses to tighten.** If What / Who / Promise stays vague after one round of questions, still generate variants — but flag that the weakness of the brief will show up in the headline set, and suggest running `ideate` or `explore-idea` first.
- **Niche piece masquerading as universal.** If the Who is a very specific role or industry, resist the urge to write "universal" headlines. For The Industry format usually outperforms a softened universal for niche pieces.
- **Existing headline the user likes but wants to test.** Preserve the user's headline as a benchmark in the "Other Variants" section, so they can compare the shortlist against what they came in with.
- **Non-English piece.** The rules apply. Proven formats translate. But power phrases and conversational verbs must be chosen in-language — don't translate *eye-opening* literally; find the native equivalent.
- **Very short-form (micro-post, social post).** Headlines for pieces under 280 characters follow the same rules but with less room — the entire piece is effectively the headline. For dedicated micro-post distribution, use `distill`, not this skill.

---

## Important reminders

- **Always generate 25–30 variants**, even if the first five feel strong. The variety is what makes the shortlist sharp.
- **One-sentence What / Who / Promise or don't start.** A fuzzy brief produces generic headlines no matter the volume.
- The Curiosity Gap is the core test. A headline that tells the reader the conclusion has closed the Gap and lost the click.
- Eliminate tiny words ruthlessly. Power phrases only when they earn their place.
- Variety of format in the Top 10 matters more than polish on any single candidate.
