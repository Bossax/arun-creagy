---
name: writing-th
description: >
  v5.0.0 L-SKLL | Draft, revise, and quality-gate Thai institutional writing.
  Use for Thai policy reports, executive summaries, articles, and formal letters
  when source fidelity, audience fit, and explicit merge approval matter.
metadata:
  origin: project-local/arun-creagy-oracles
  installer: project
---

# /writing-th — Thai Institutional Writing Harness v5

Turn technical evidence into decision-ready Thai prose without confusing a
mechanical lint pass with editorial quality.

## Non-negotiable invariants

1. **Draft isolation** — write only to `ψ/incubate/drafts/`, another approved
   scratch location, or the chat. Never overwrite the destination before the
   human explicitly says `Approve`, `Merge`, or `Execute`.
2. **One scoped unit at a time** — do not batch unrelated sections.
3. **Source fidelity** — preserve required evidence, distinctions, tables,
   equations, and frameworks. Compression is governed by the transformation
   mode, not by a universal character ratio.
4. **Two different assurances** — mechanical checks detect encoded patterns;
   editorial review judges meaning, altitude, reader value, and form. Never call
   a mechanical pass an editorial approval.
5. **No ledger writes** — do not modify style memory, retrospectives, or the miss
   register except through their own explicitly invoked maintenance skill. The
   ordinary linter may log runs only when repository policy permits it.

## Required references

- Read [references/editorial-rubric.md](references/editorial-rubric.md) before
  creating the content contract or reviewing a draft. Apply the core rubric and
  only the selected deliverable profile.
- Read [references/artifact-schemas.md](references/artifact-schemas.md) before
  creating `writing-contract.json` or `editorial-review.json`.
- Load the writing plan and the style pack it names. If none is named, use
  `ψ/memory/style/STYLE_PACK_TH.md` and `ψ/memory/style/LEXICON_TH.json`.

## Six-gate workflow

### 1. Inspect sources and classify the transformation

Read the brief, source evidence, target section, applicable style material, and
any approved sample. Select exactly one mode:

- `rewrite`: the source and draft are comparable in scope; preservation and the
  size heuristic apply.
- `synthesis`: the draft intentionally compresses or combines sources; the size
  heuristic must not run.
- `new`: no source text is being rewritten; the size heuristic must not run.

Do not draft yet.

### 2. Build one content contract and stop

Create `writing-contract.json` beside the future isolated draft. It must lock the
audience, decision use, section job, target altitude, inclusions, exclusions,
evidence policy, required concepts, terminology, required structures, source
paths, and reference samples.

Present a compact contract summary and stop for human approval. Record that
approval in the contract. This replaces separate persona and density stops.

### 3. Draft in isolation

Draft only the approved unit. Treat finding, concrete evidence, consequence,
and mechanism as the payload of each **substantive argument unit**; do not force
all four into every paragraph. Keep one dominant job per paragraph.

Evidence-traceability notes, slide/page locators, prompt scaffolding, and report
roadmaps belong outside audience-facing prose. A requested diagram becomes a
figure placeholder or actual figure, never an inline arrow chain.

### 4. Run mechanical checks

For report prose, run:

```text
python .agents/skills/writing-th/scripts/lint_thai_writing.py <draft> ψ/memory/style/LEXICON_TH.json --scope report
```

For `rewrite` mode only, also run:

```text
python .agents/skills/writing-th/scripts/check_density.py <source> <draft> 0.8
```

Fix blocking failures. Carry every non-blocking `[STRUCTURAL]`,
`[PARENTHETICAL]`, `[ARTIFACT]`, or `[META]` review item into the editorial
receipt with a disposition. A green result here means only **mechanical pass**.

### 5. Obtain editorial review

Default to an independent clean-context reviewer. Give the reviewer only the
approved contract, draft, necessary sources or traceability sidecar, selected
profile rubric, and reference sample. Do not provide the intended verdict or
the drafting agent's self-justification.

If an independent reviewer is unavailable, perform a structured self-review and
mark it `reviewer_mode: self`, `assurance: degraded`. Degraded review may pass,
but must be disclosed prominently.

Create a receipt scaffold with:

```text
python .agents/skills/writing-th/scripts/editorial_gate.py prepare <draft> <contract> --out <review> --reviewer-mode independent
```

Complete every required rubric dimension and record located findings. A receipt
passes only when its verdict is `pass`, all required dimensions pass (or source
fidelity is legitimately `not_applicable` in `new` mode), and no critical or
major finding remains unresolved.

Verify it with:

```text
python .agents/skills/writing-th/scripts/editorial_gate.py verify <draft> <contract> <review>
```

Any draft or contract change invalidates the receipt. Review the new hashes.

### 6. Human bridge and merge

Present the draft with its editorial assurance and unresolved minor findings.
Merge only after explicit human approval:

```text
python .agents/skills/writing-th/scripts/merge_draft.py <draft> <dest> --lexicon ψ/memory/style/LEXICON_TH.json --contract <contract> --review <review> [--source <source>]
```

Merge reruns mechanical checks, verifies the exact receipt hashes, and confirms
that all emitted review items have dispositions. `--skip-gates` remains a loud,
deliberate override; never infer permission to use it.

## Maintenance

- After a style-capture round, validate the lexicon with
  `validate_lexicon.py`; do not edit style memory from this skill.
- After changing canonical `SKILL.md`, run `check_skill_drift.py --sync`.
- Run `tests/run_tests.py` after any harness change.
- A behaviorally significant revision requires a blind forward test in an
  isolated temporary workspace. Use an independent reviewer when delegation is
  available; otherwise document that the test used degraded self-review.
