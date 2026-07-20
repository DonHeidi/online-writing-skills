# Rate-skill eval harness

The `rate` skill makes mechanically checkable claims: the content score must
equal a fixed weighted sum of the dimension scores and the VPM subscore, the
VPM must equal value instances divided by the unrounded duration from
`scripts/count-words`, the deduction ledger must cover all six dimensions,
recommendations must trace to ledger defects, and the readiness verdict must
follow the tier rules. This harness checks those claims — the judgment calls
(is an 8 in credibility right?) it deliberately does not.

## Files

- `fixtures/` — three sample drafts of known character:
  - `strong-draft.md` — dense, specific, single-thesis (should rate well)
  - `padded-draft.md` — generic truisms, repetition (should rate poorly on
    originality and VPM)
  - `off-thesis-draft.md` — competent prose, two competing theses (should
    lose clarity-of-thesis points)
- `validate_rating.py` — mechanical validator for one rating JSON
- `rate_eval.py` — headless runner + variance benchmark

## Validate a single rating

```sh
tests/validate_rating.py rating.json tests/fixtures/strong-draft.md
```

Omit the fixture path to skip the word-count/VPM checks (e.g. for ratings of
content you don't have on disk). Exit code 0 = pass.

## Run the skill and benchmark variance

```sh
tests/rate_eval.py --fixture tests/fixtures/strong-draft.md --runs 3
tests/rate_eval.py --fixture tests/fixtures/padded-draft.md --runs 3 --own-draft
```

Each run invokes `claude -p` in the repo root (requires the claude CLI,
consumes real tokens, roughly a minute per run), validates the JSON output,
and reports mean / standard deviation / range for the content score, each
dimension, and VPM across runs.

How to read the variance report:

- **Dimension sd ≲ 0.5 and content-score range within a few points** is the
  goal of the anchored rubric — the formula is deterministic, so all
  remaining spread comes from dimension judgment and value-instance
  extraction.
- **Rising spread after editing SKILL.md** means the anchors got vaguer —
  treat it as a regression even if single runs look fine.
- Fixture ordering is a sanity check, not an assertion: `strong-draft`
  should reliably outscore `padded-draft`. If it doesn't, the rubric (or the
  fixture) needs attention.

## Keeping the harness honest

`validate_rating.py` mirrors the weight profiles, VPM bands, and readiness
tiers from `skills/rate/SKILL.md`. **If you change those in the skill, change
them here in the same commit** — a green validator against a stale table is
worse than no validator.

The validator is itself tested by mutation: seed a known-good rating with a
specific defect and assert the check catches it (see the branch history for
the 14-mutation self-test).
