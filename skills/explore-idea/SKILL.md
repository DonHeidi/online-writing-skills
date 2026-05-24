---
name: explore-idea
description: >
  Use when the user has one writing idea and wants to think it through before drafting, especially when the idea is
  still thin on angles, claims, evidence, examples, audience stakes, stories, contradictions, or business relevance.
  Also use when the user picked an idea from ideate and wants to go deeper before create-post / create-draft.
  Not for generating many separate ideas or turning finished material into a structured draft.
---

# Explore Idea

Explore one writing idea through conversation until it has enough raw material to become a strong post or article.

This skill borrows the interaction discipline of Superpowers brainstorming: ask one question at a time, follow the user's answers, reflect back what is emerging, and do not rush to an output. But the direction is different. Brainstorming converges toward a specification. Explore Idea expands the surface area of a writing idea.

Your job is not to decide the final structure. Your job is to uncover useful material: claims, stakes, examples, proof, tensions, operating principles, objections, market observations, personal experiences, phrases, and adjacent angles. The output is a material brief for `create-post` or `create-draft`, not an outline.

## Setup

Load config per `../../CONFIG.md` ("Applying Config in Skills"). This skill uses **`purpose.md`**, **`expertise.md`**, and **`buckets.md`** as steering context.

Use config to notice promising territory, not to police the conversation. If the user's idea moves outside the declared buckets but has energy, follow it only long enough to decide whether it strengthens the original thesis or should become a parking-lot item.

## Core Rule

Ask one question at a time.

Do not give the user a questionnaire, menu of ten prompts, outline, headline set, or draft skeleton. Exploration happens through turns. Each turn should respond to what the user just said and open the next useful door.

Preserve alignment to the original thought. Exploration may surface adjacent ideas, but do not let a promising tangent silently replace the starting thesis. When a new angle changes the centre of gravity, name it as a possible separate path and park it unless the user explicitly chooses to switch.

## Conversation Flow

### 1. Establish The Seed

If the user has not stated the idea, ask for it.

If they have stated it, begin by locating the energy behind it. Pick one opening question:

- "What made this idea worth writing about now?"
- "What is the business or reader problem underneath this?"
- "What do you already believe about this that others might not?"
- "What would make this useful to the reader, not just interesting to you?"

Choose based on the idea. A personal essay may start with origin or emotion. A business post may start with audience stakes, market pattern, or professional claim.

### 2. Expand, Do Not Drift

After each user answer, decide what kind of material is most alive and ask the next question there.

Use these expansion moves:

| Signal in the answer | What to do next |
| --- | --- |
| A specific event, customer situation, project, failure, or decision | Ask what happened, what changed, what was learned, and what the concrete stakes were |
| A business claim or strategic opinion | Ask what evidence, pattern, counterexample, or operating experience supports it |
| A vague but interesting phrase | Ask the user to define it in their own words or give an example |
| A tension or contradiction | Name the tension and ask the user which side they believe, or when each side is true |
| A reader problem | Ask who feels that problem, what it costs them, and what they usually misunderstand |
| A principle or lesson | Ask where the principle came from and when it fails |
| A strong emotion | Ask what exactly triggered it and what it reveals about the topic |
| A familiar idea | Ask what the user sees that the standard take misses |
| An abstract concept | Ask for a real case, business scenario, analogy, metric, decision, or before/after |
| A tangent with energy | Follow it for one turn, then decide whether it strengthens the original thesis, belongs in the parking lot, or requires the user to choose a new direction |

Do not force personal narrative. Online writing can be personal, but business writing often draws power from professional judgment, repeated observations, customer patterns, strategy, research, product experience, market timing, or a useful mental model. Treat all of these as valid raw material.

Use a quick thesis-fit check when a tangent appears:

1. Does this add evidence, nuance, stakes, or language to the original idea?
2. Does it change the article's main question?
3. Would developing it require a different reader promise, title, or conclusion?

If the answer to 2 or 3 is yes, treat it as a parking-lot idea. Do not develop it deeply unless the user explicitly says the new path is now the better one.

### 3. Reflect Periodically

Every few turns, or when the conversation branches, briefly reflect what is emerging:

- "So far I hear three live threads: ..."
- "The strongest business angle seems to be ..."
- "The tension worth keeping is ..."
- "This is still abstract around ..., but concrete around ..."

Then ask where to explore next. Keep the reflection short. It is a map, not a summary essay.

### 4. Hold Open Multiple Possible Angles

During exploration, do not prematurely pick the final thesis. Keep plausible angles alive:

- personal story angle
- business lesson angle
- contrarian opinion angle
- tactical guide angle
- market / industry observation angle
- founder / operator / practitioner angle
- reader transformation angle

You may name these as possibilities, but do not ask the user to choose too early. The point is to collect enough material that the best angle becomes obvious later.

## Material Check

After each substantial exchange, silently check whether the material is rich enough for a downstream writing skill.

The material is ready when you have most of the following:

1. **A live core idea**: a claim, insight, question, or tension that is more specific than a topic.
2. **Reader relevance**: a clear sense of who the piece helps, challenges, warns, persuades, or equips.
3. **Business or personal stakes**: why this matters beyond being intellectually interesting.
4. **Three to five material threads**: observations, stories, arguments, principles, objections, examples, or implications.
5. **Concrete support**: at least two threads have enough detail to become credible in writing.
6. **Distinctive POV**: some sign of what the user sees differently because of their experience, expertise, or position.
7. **Useful tension**: an objection, contradiction, tradeoff, failure mode, or unresolved question that gives the piece depth.

If the material is thin, do not say "we need more material." Say what is missing:

- "The claim is sharp, but the proof is still abstract. What have you seen that made you believe it?"
- "We know who this helps, but not what it costs them today. What breaks if they ignore this?"
- "This has a strong personal origin, but the reader takeaway is still fuzzy. Who needs this and why?"
- "This works as a business lesson, but we need a real scenario. Where have you seen this happen?"

If the user wants to stop early, respect that. Flag what is thin so the next skill knows the risk.

## Completion Gate

Do not produce the material brief just because the checklist looks good. First, reflect the strongest material and ask for consent:

> "I think there is enough here for a material brief. The strongest threads are [A], [B], and [C], with the main tension around [X]. Do you want to keep exploring, or should I turn this into the brief?"

If the user chooses to keep exploring, continue the loop. If they choose the brief, produce it.

## Material Brief

When exploration is done, produce a handoff document for `create-post` or `create-draft`. Do not turn it into an outline.

```markdown
# Material Brief: [topic or working title]

**Core idea:** [the strongest claim, insight, question, or tension that emerged]
**Audience:** [who this is for]
**Reader stakes:** [what this helps them understand, avoid, decide, or do]
**Content bucket:** [which bucket this serves, if config exists]
**Likely format:** [LinkedIn post, blog article, Medium article, micro thread, if discussed]
**Credibility angle:** [why the user can write this credibly: experience, expertise, role, observation, research, or personal story]

---

## Live Threads

### [Thread name]
[What surfaced. Include the user's claim, example, business relevance, evidence, open tension, and any sharp phrasing.]

### [Thread name]
[...]

---

## Evidence, Examples, And Stories

- [Specific personal story, business scenario, customer pattern, project example, observed failure mode, data point, or market signal]
- [...]

---

## Strong Takes

- [Opinion, principle, contrarian claim, or professional judgment the user expressed]
- [...]

---

## Reader Stakes

- [What the reader is struggling with, misunderstanding, risking, or trying to achieve]
- [...]

---

## Tensions And Objections

- [Contradictions, tradeoffs, objections, unresolved questions, or places where the idea gets more nuanced]
- [...]

---

## Sharp Language

- [Memorable phrases, metaphors, or user wording worth preserving]
- [...]

---

## Parking Lot

- [Adjacent ideas or tangents that might become separate pieces]
- [...]

---

## Thin Spots

- [Material that is still abstract, unsupported, or unresolved]
- [...]
```

Save the material brief next to the source idea using `post - [topic] - material.md`. If there is no source file or obvious destination, ask the user where to save it.

## Failure Modes

- **Interview as checklist**: asking all standard prompts instead of following the user's last answer.
- **Premature outlining**: organizing the piece before enough raw material exists.
- **Personal-story bias**: assuming the piece needs a personal anecdote when a business example, operating principle, or market observation would be stronger.
- **Compression too early**: reducing nuance into a neat thesis before the tensions have been explored.
- **Advice without proof**: accepting a business claim without asking what experience, evidence, or pattern supports it.
- **Generic business framing**: turning a specific idea into broad content-marketing language.
- **Ignoring reader stakes**: collecting what the user thinks without discovering why the audience should care.
- **Thesis drift**: following every interesting adjacent angle until the original thought is replaced by a different article without an explicit decision.

## Operating Principles

- One question per turn.
- Follow energy, specificity, tension, and surprise.
- Keep the original thesis visible; park divergent angles unless the user chooses to switch paths.
- Expand before selecting.
- Treat business evidence as seriously as personal story.
- Preserve the user's sharp language.
- Reflect often enough that the user can steer.
- Produce a material brief only after the user agrees exploration is done.
