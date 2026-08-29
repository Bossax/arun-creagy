---
date: 2026-08-29 13:00 SEAST
type: info
status: raw
significance: important
---

# Writing-TH Harness Architecture

**Skill**: `writing-th` v5.0.0 (`.agents/skills/writing-th/`)
**Created**: 2026-03-13 (first committed as an Agy local skill)
**Upgraded to current v5 form**: 2026-08-28 (commit `4737036 updrade writing-th v5`; prior overhaul 2026-08-25, commit `6f70d93 writing skill overhual`)
**Architecture doc published**: 2026-08-25, as Artifact "Writing-TH Harness" — https://claude.ai/code/artifact/259a8a31-5d30-4e32-8bc5-bc7171b09cb3
**Companion skill**: `style-capture` (`.agents/skills/style-capture/`)

## Summary

A closed loop between two skills sharing one style pack (`ψ/memory/style/`, `STYLE_PACK_TH` + `LEXICON_TH` v4.0, 48 rules: 42 literal, 4 regex, 2 structural; 40 universal, 8 report-specific).

### Forward arc — `writing-th`, 7 stages (0–6)

| # | Stage | Gate |
|---|---|---|
| 0 | Calibration — loads style pack, builds jargon ban list, halts to confirm persona | **Stop** |
| 1 | Strategy — victory condition, evidence→analysis→solution shape | none |
| 2 | Density & Scope Validation — lists every table/equation/framework that must survive rewrite, halts for sign-off | **Stop** |
| 3 | Payload Gate — 4-Pillar Extraction (Claim, Concrete Example, Consequence, Mechanism), required before drafting | none |
| 4 | Governed Execution — one subagent per subsection, writes only to `ψ/incubate/drafts/`; target file unreachable by construction | none |
| 5 | Script Gates — lexicon lint + density, exit code 1 = silent rejection | **Binding** |
| 6 | Merge — human approves, `merge_draft.py` copies draft over the real file | **Binding + Stop** |

The draft never touches the destination file until stage 6.

### Return arc — `style-capture`, 6 stages (A–F)

| # | Stage | Gate |
|---|---|---|
| A | Read the delta — `git diff` on the hand-edited file | human-initiated |
| B | Materialize evidence — dated diff-evidence file of word-for-word changes + candidate rules | artifact |
| C | Validate before promoting — every rule declares `kind` (literal/regex/structural) + `scope`; `validate_lexicon.py` rejects malformed rules | **Binding** |
| D | Check the miss register — proposed, not built: SQLite append-only log, promotion fires once a pattern fails twice | proposed |
| E | Merge into the pack — appends examples/counter-examples, re-ranks rules | none |
| F | Index to Oracle — calls `oracle_learn` so the round becomes searchable memory | persisted |

## Tranche 1 — verified 2026-08-25 (every check run, not asserted)

- Gates made binding rather than advisory.
- Fixed 3 of 5 lexicon rules from the 2026-08-05 round that were silently dead — prose descriptions had been compiled as regex (e.g. `[ผลงาน/deliverable]` became a character class).
- Fixed a rule whose prescribed replacement contained its own banned string, which made the rerun-until-exit-0 loop non-terminating — reclassified as `kind: structural`.
- Word/sentence boundaries now come from PyThaiNLP; code spans, link targets, and file paths are excluded from prose linting.
- `merge_draft.py` used to only check the draft existed, then copy — never called the gates. It now runs the gates itself and exits 1 without touching the destination on failure. `--skip-gates` exists for deliberate override with a loud warning.
- Regression suite: 20/20 fixtures pass; 11/20 disagree with the old linter, including every defect case.

## Tranche 2 — proposed, not built

1. Move persona out of Stage 0 into a late voice pass (the pack itself places voice at stage D and lexicon at stage E — "a late-pass sweep, not a first-pass drafting engine").
2. Add the missing structural-revision stage.
3. Move evidence gathering ahead of any framing.
4. Fast/slow track split (Stage 0–2).
5. Restrict the 4-pillar payload rule to argumentative paragraphs only — it currently applies to every paragraph with no exception, forcing foundation paragraphs to invent a claim.
6. SQLite miss-register with fails-twice promotion trigger — the threshold was already fixed at two by a 2026-06-27 learning, but markdown files cannot aggregate, so nothing ever counts to two.
7. Density ceiling tied to the Stage 2 preserve-list — density is currently a floor with no ceiling; a draft at 3× source length passes silently, so padding is the cheapest way to clear the gate.
8. Subagent brief schema with a non-removable clause — subagents currently get a topic, not a contract, so delegated scope, examples, and qualifiers get silently dropped.
9. Lint the scaffolding, not just the final draft.
10. Supersession marking so the pack can shrink — across nine append-only rounds nothing is ever marked retired, so the pack only grows; when a new pattern contradicts an old rule the instruction is "prefer the new one and keep a note."
11. Parenthetical allowlist for verbatim TOR titles.

## Cross-references

- Source: `ψ/lab/writing-th-harness/` (published Artifact "Writing-TH Harness")
- Skill source: `.agents/skills/writing-th/`, `.agents/skills/style-capture/`, `ψ/memory/style/` (pack v5.0, lexicon TH v4.0)

Logged via /fyi
