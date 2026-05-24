---
name: distill
description: >
  Use when the user has a long-form piece (article, blog post, essay, draft) and wants it broken into
  shorter standalone posts in one of two modes: **Micros** (≤280 chars, for X / Bluesky / Threads /
  Mastodon) or **LinkedIn shorts** (800–1,200 chars). Produces one mode or both depending on the request.
  Also use for cross-posting or repurposing a single long piece into distributable social content. Not for
  generating new post ideas from scratch (see ideate) or for shaping raw material into a full post (see
  create-post for 800–1,200 *word* posts, create-draft for 2,500–3,000 *word* articles).
---

# Distill

You take a long-form piece of writing and reframe its ideas into shorter standalone posts that work for someone who has never read the source. Two output modes:

- **Micros** — ≤280 characters. For X, Bluesky, Threads, Mastodon.
- **LinkedIn shorts** — 800–1,200 characters. The "gold-standard" length for LinkedIn feed posts.

This is the content distribution flywheel: write once at length, then break it into posts that each serve a specific reader in one of your content buckets. It's not a distillation or a summary — it's a reframed idea that's useful to the reader on its own terms.

## Setup

### Determine mode

Before drafting, decide which mode(s) to produce. Read the user's request:

- **Cues for Micros only:** "for X", "for Bluesky", "for Threads", "for Twitter", mentions of 280 chars, "tweet"-shaped requests
- **Cues for LinkedIn shorts only:** "for LinkedIn", "LinkedIn-length", "LinkedIn posts"
- **Cues for both:** "for cross-posting", "for X and LinkedIn", "all platforms", "social"
- **No cue:** ask one question — *"Which platforms? Micros (X / Bluesky, ≤280 chars), LinkedIn shorts (800–1,200 chars), or both?"*

Hold the chosen mode(s) as state. Each post belongs to exactly one mode.

### Load config

Load config per `../../CONFIG.md` ("Applying Config in Skills"). This skill uses **`purpose.md`**, **`buckets.md`**, **`tonality.md`** — every post must be positioned within a specific content bucket and written for that bucket's audience. The buckets are your distribution lens: they decide which angle an idea gets reframed from and who it's written for.

When `tonality.md` is populated, apply its format rules — match the user's voice in compressed form for Micros, match it at full breathing length for LinkedIn shorts. Compressed is not slogany: reasoning can be implicit but punchlines without substance are an anti-pattern.

Also read `../../references/tonality-guide.md`. It defines the four registers (descriptive, argumentative, instructional, referential) and the failure modes agents drift toward in each. **The source article's register carries through to the distilled posts.** If the source describes, the posts describe. If the source argues, the posts argue. Don't impose a register the source doesn't have — LinkedIn culture pushes argumentative-with-CTA-close regardless of source type, and that's the failure mode this rule prevents.

---

## Step 1 — Read, Map to Buckets, and Reframe for the Reader

Read the full piece. Your job is not to extract or distill — it's to **reframe the article's ideas so they're useful to a specific reader in one of your content buckets.** The article is raw material. The post is the product, and it's built for the reader, not summarised from the source.

For each section or key moment, ask two questions:

1. **Which bucket does this idea serve?** Map it to a specific content bucket from `buckets.md`. If an idea doesn't fit any bucket, it's not a candidate. If it could serve multiple buckets, pick the one where it's most actionable — or create separate posts, each reframed for its bucket's audience.
2. **What can the reader do, think, or change because of this idea?** The post exists to be useful — not to preserve the article's insight in compressed form. Frame it as something the reader walks away with: a decision they can make, a mental model they can apply, a question that changes how they see their own situation.

Identify candidates by looking for:

- **Applicable reframes** — flipped assumptions that change how the reader approaches their own work or life. "You're not a bad decision-maker — you're making decisions with broken equipment" works because the reader immediately applies it to themselves. The reframe must land in the reader's context, not the article's.
- **Actionable principles** — ideas the reader can use today. Not "energy management matters" (too abstract) but "Pick one decision per day — not a goal, a decision. The win is completing it." The reader knows what to do next.
- **Pattern recognition** — observations that help the reader see something in their own life they haven't named. The "I've always felt this but never heard anyone say it" effect. The value is in the naming, not the article it came from.
- **Self-contained story beats** — micro-stories where the setup and punchline don't require the article's context. "I asked for 2 sick days. My doctor gave me 18 months." works because it's a complete surprise in one sentence. "You made the phone call. Now it's 2pm and you're back in bed." doesn't — the reader doesn't know what phone call, or why bed.
- **Contrarian or counterintuitive takes** — these perform best on social platforms because they stop the scroll. But the contrarian point must be self-evident and useful on its own, not dependent on the article's argument to land.

Not every paragraph contains a post. A 1500-word article might yield 8–15 Micros candidates or 5–8 LinkedIn-shorts candidates. A thin article might yield 3 of either. Quality over quantity.

### The reader-utility test

Before adding any idea to your candidate list, ask: **Does this give the reader something they can use — a decision, a lens, a shift — without ever reading the source article?** If the answer is "it's interesting but not actionable," reframe it until it is. If it can't be made useful, drop it.

Example of distillation (what NOT to do):
> "A bad day isn't a failed day. If you spent all your energy on the one thing that mattered, that's enough."

Nice thought, but it's a compressed version of the article's wisdom — the reader walks away with nothing to do or apply.

Example of reader-useful reframing (what TO do):
> "Tomorrow, pick one thing. Not a to-do list — one thing. Spend whatever energy you have on that. If it's done by noon and you're empty, that's a full day."

Same underlying idea, but reframed as something the reader can act on. It meets them where they are and gives them a next step.

---

## Step 2 — Draft Posts

For each candidate idea, write a post that:

1. **Serves the reader, not the article.** The post exists to be useful to the person reading it — not to preserve the article's insight in compressed form. Reframe the idea so the reader walks away with something they can apply.
2. **Belongs to a bucket.** Every post is written for a specific audience from your content buckets. The bucket determines the angle: the same underlying idea reframed for an industry audience sounds different than for a general audience. Tag each post with its bucket.
3. **Stands completely alone.** A reader with zero context should understand the point and find it valuable. No "as I wrote in my latest article" framing.
4. **Fits its mode's character limit** (see Step 3).
5. **Leads with the sharpest version of the idea.** No warm-up. The first words should hook. On social platforms, you're competing with the next post in the feed.
6. **Preserves the author's voice and the source's register.** If the original is conversational, the post is conversational. If it's authoritative, keep that. If the source describes, the post describes. If the source argues, the post argues. Don't make everything sound like generic LinkedIn advice. The source's register beats LinkedIn's default register every time.
7. **Has a complete arc.** Setup and a payoff. "X is not Y — it's Z" reframes work well. Mini-stories where the punchline doesn't need context work well. Bare assertions without a payoff don't.

### Types of posts to generate

Vary the types across your set — don't produce 10 posts that all follow the same formula. The 7 types apply to both modes; what differs is how much room each gets to breathe.

- **The reframe** — Take a common belief and flip it so the reader sees their own situation differently. "Specificity isn't limiting. It's liberating." The reader should think "wait, I've been approaching this wrong."
- **The lens** — Give the reader a mental model they can apply immediately. "Your brain rewires based on what you repeatedly do, not what you want to do."
- **The next step** — One concrete, actionable piece of advice the reader can use today. "Pick one decision per day. Not a goal — a decision. Something small you can do and finish."
- **The question** — A provocative question that makes readers interrogate their own assumptions. Works best when the implied answer is counterintuitive.
- **The naming** — Articulate something the reader has felt but never had words for. The "I've always known this but never heard anyone say it" effect.
- **The micro-story** — Setup and punchline where both are self-contained. "I asked my doctor for 2 sick days. She kept asking. We settled on two weeks. That turned into 18 months."
- **The contrast** — Two things that shouldn't go together, or a before/after that speaks for itself.

### Mode-specific rules

**Micros (≤280 chars):** Compress hard. Reasoning is implicit; only the payoff and the minimum setup needed to land it survive. The opening line is half the post — make it work.

**LinkedIn shorts (800–1,200 chars):** You have room for setup + payoff + a beat of landing. Use it — but don't pad. Three failure modes to actively resist:

1. **LinkedIn-voice drift.** Don't reach for generic LinkedIn templates: *"Here's something most people miss about X:"*, *"3 lessons I learned the hard way:"*, *"I used to think X. Now I think Y. Here's what changed."*, numbered-step scaffolding, emoji-bullet lists. If the post you're drafting could be by anyone in your industry, it's not yours. Pull voice cues from the source article, not from LinkedIn convention.

2. **Engagement-bait closes.** Don't end with *"What's your take?"*, *"Drop a comment."*, *"Agree?"*, *"DM me if interested."* The post lands on its own substance — a directive, a frame, a question that interrogates the reader's own thinking. Not a request for response. (Final pass below catches these too.)

3. **Register imposition.** LinkedIn culture pushes everything toward thesis-forward / argumentative posts with closing punchlines. **Don't impose that register on a source that doesn't have it.** A case-study source stays descriptive at LinkedIn length — specifics-first, reasoning woven in, closes on observation or what the setup produces. A how-to source stays instructional. A curated-list source stays referential. Only an Opinion source is naturally argumentative. See `../../references/tonality-guide.md` for register-by-writing-type defaults.

### Final pass — strip empty closers

After drafting each post, re-read its last line specifically. Does the closer deliver a payoff the reader can carry — a decision, a lens, a shift, a question they'll keep thinking about? Or is it empty?

Two empty-closer patterns to watch for:

- **Wisdom-tics.** Slogans, aphorisms, sand-the-edges-off lines that sound profound but give the reader nothing to do or apply. *"…and that changes everything."* *"Everything else is just the coefficient."* *"Sand the edges off and you sand that out too."*
- **Engagement-bait.** Requests for response grafted onto the end. *"What's your take?"* *"Drop a comment."* *"Agree? DM me."* LinkedIn-specific but creeps into Micros too. The post should land on its own substance, not a request for engagement.

If the closer is empty: cut it. The post often ends stronger one line earlier. If the substance lives in the closer and the rest is setup, restructure to lead with the closer's substance and drop the wind-up.

---

## Step 3 — Verify Character Counts

After drafting, count the characters of every post. Hard limits:

- **Micros: 280 characters absolute.** No exceptions, including thread-starter openers.
- **LinkedIn shorts: 800–1,200 characters.** Posts under 800 are too short — fold extra context back in or merge with another post. Posts over 1,200 are too long — trim back. The range exists because LinkedIn rewards posts that fill the feed slot without pushing into "show more" fatigue.

Common trimming techniques:

- Replace "that is" with "that's", "do not" with "don't"
- Cut filler words: "actually", "really", "just", "very"
- Replace phrases with shorter equivalents: "in order to" → "to", "the reason why" → "why"
- Restructure to front-load the payoff and cut the setup

If a great Micro idea can't fit in 280 characters without losing its punch, flag it as a **thread starter** instead — a post that works alone but could open a 3–5 post thread. (Thread starters are a Micros-mode artifact; LinkedIn shorts have room to land as a single post and don't need this fallback.)

---

## Step 4 — Organise and Present

Output template — applied per mode. When both modes are produced, render them as two separate top-level documents (and save to two files — see *After delivery* below).

```
# [Micros / LinkedIn Shorts] from: [article title]

**Source:** [title or file name]
**Mode:** [Micros — ≤280 chars / LinkedIn Shorts — 800–1,200 chars]
**Posts generated:** [count]

---

## [Bucket name] — [bucket's target audience]

### 1. [type: reframe / lens / next step / question / naming / micro-story / contrast]
> [the post text]
[character count]

### 2. [type]
> [the post text]
[character count]

...

## [Next bucket name] — [bucket's target audience]

### 3. [type]
> [the post text]
[character count]

...

---

## Thread Starters (Micros mode only — ideas too rich for 280 characters)

### 1. [topic] — [bucket]
**Opening post:**
> [≤280-character opener]
[character count]

**Thread outline:** [2–3 bullet points for follow-up posts]

---

## Discarded Ideas

[Ideas from the article that didn't work as posts in this mode and why — too dependent on context, couldn't be made reader-useful when compressed, didn't fit any bucket, etc. Kept here in case the user wants to develop them differently or use them in the other mode.]
```

---

## After delivery — soft prompt

After producing the output above, offer one optional next step. Keep it brief and non-blocking — the user decides.

- **Save to file(s)?** Ask whether to write the post collection to disk. If yes, ask the user where and what to name them — defer to whatever conventions apply in their environment, don't assume a specific layout or naming scheme. **When both modes are produced, save them to two separate files** (one per mode), with names that distinguish the modes (e.g., suffix `-micros` and `-linkedin`, or whatever convention the user gives you).

(Structural diagnostics don't apply to standalone posts — each one is self-contained and length-bounded. For overall quality signal on the source article, use `rate`.)

---

## When the user provides multiple articles

If the user gives you several pieces to distill at once, process each separately but also look for cross-article patterns — recurring themes that could become a post series or a thread that ties multiple articles together.

---

## Important Reminders

- Character limits are absolute. Micros: 280. LinkedIn shorts: 800–1,200. Count every post. No exceptions, including thread-starter openers.
- Each post must stand alone. If you need to say "in my latest article" to make it work, it's not a post — it's a promo. Rewrite it so the idea speaks for itself.
- Every post must belong to a bucket. If an idea doesn't serve a specific audience from your content buckets, it's not a candidate — no matter how clever it sounds.
- Reader utility over distilled wisdom. The test is "can the reader do something with this?" not "does this capture the article's insight?" If a post is interesting but not useful, reframe it until it is or drop it.
- The source's register beats LinkedIn's default register. Descriptive sources stay descriptive at LinkedIn length. Don't drill a thesis into a piece that's just describing.
- No engagement-bait closes. Posts land on their own substance, not "What's your take?"
- Aim for at least 5 strong posts per article in each mode requested. A rich article might yield 15 Micros or 8 LinkedIn shorts. Don't pad — if the article only has 4 great moments in a mode, produce 4.
- Preserve the author's voice. The posts should sound like the person who wrote the original, not like a social media manager.
- Contrarian and counterintuitive posts outperform on social platforms. Prioritise ideas that challenge assumptions or flip common advice.
- The character count goes in the output so the user can verify at a glance. Trust but verify — if you're close to the limit, double-check.
