---
name: writing-th
description: >
  v6.0.0 L-SKLL | Draft, revise, and quality-gate Thai institutional writing.
  Use for Thai policy reports, executive summaries, articles, and formal letters
  when source fidelity, audience fit, and explicit merge approval matter.
metadata:
  origin: project-local/arun-creagy-oracles
  installer: project
---

# /writing-th — Thai Institutional Writing Harness v6.0

Turn technical evidence into decision-ready Thai prose without confusing a
mechanical lint pass with editorial quality — and without asking one context
to formulate arguments, retrieve facts, invent connective reasoning, and draft
formal Thai prose all at once. That overload is what v5.0 got wrong: it went
straight from a metadata contract to a one-shot prose pass, with no argument
artifact in between, and the result was knowledge-telling — facts stitched
together with no rhetorical tension, findings with no "so what."

v6.0's core move: insert `argument-map.json` between scope and prose, and
enforce it as a **context boundary**, not just an added file. Argument
construction gets sources and no style material. Verbalization gets the
approved map and a style kernel, never the raw sources. The parent session
holds only paths, hashes, and gate verdicts — never content.

## Non-negotiable invariants

1. **Draft isolation** — write only to `ψ/incubate/drafts/`, another approved
   scratch location, or the chat. Never overwrite the destination before the
   human explicitly says `Approve`, `Merge`, or `Execute`.
2. **One scoped unit at a time** — do not batch unrelated sections.
3. **No prose before an approved argument map** — physically enforced by the
   `PreToolUse` hook on `Write|Edit`: a write to `ψ/incubate/drafts/**/*draft*.md`
   is denied when the sibling `argument-map.json` is missing or its
   `approval.status` is not `approved`. This is not a convention to remember;
   it cannot be skipped.
4. **Source fidelity** — preserve required evidence, distinctions, tables,
   equations, and frameworks. Compression is governed by the transformation
   mode, not by a universal character ratio.
5. **Three different assurances** — mechanical checks detect encoded
   patterns; Tier 1 review judges whether the argument map's reasoning
   actually holds; Tier 2 review judges whether the prose faithfully
   verbalizes that map. Never call a mechanical pass an editorial approval,
   and never let a Tier 2 pass stand in for Tier 1.
6. **No ledger writes** — do not modify style memory, retrospectives, or the miss
   register except through their own explicitly invoked maintenance skill. The
   ordinary linter may log runs only when repository policy permits it.

## Stage → agent → context map

See [references/subagent-prompts.md](references/subagent-prompts.md) for canonical prompts, model tiers, and invocation snippets.

| Stage | Runs as | Loads | Must never load |
|---|---|---|---|
| 0 Contract | Parent + `AskUserQuestion` / `ask_question` | plan index, source paths, writing plan (if any) | sources, full style pack |
| 1 Argument map | `th-argument-mapper` (`invoke_subagent` / `Agent`) | sources, writing plan (if any), argument schema, contract `target_altitude` | style pack, lexicon, rubric |
| 2 Blueprint gate | Parent (Plan Mode / Markdown Artifact + `ask_question`) | rendered map summary | everything else |
| 3 Verbalization | `th-verbalizer` (`invoke_subagent` / `Agent`) | `argument-map.json`, prose kernel, contract `report_specific_rules` & `target_altitude` | raw sources, full pack, rubric |
| 4 Mechanical gate | CLI only | — | nothing enters a model context |
| 5 Editorial review | `th-editorial-reviewer` (`invoke_subagent` / `Agent`) | draft, argument map, contract, rubric | sources, style pack |
| 6 Merge | CLI + parent | hashes, verdicts | — |

`LEXICON_TH.json` should never enter a model context at any stage —
`lint_thai_writing.py` reads it; only violations need to reach a model.

### Cross-Agent Runtime Mapping

| Primitive | Google Antigravity (AGY) | Claude Code | Codex / Headless CLI |
|---|---|---|---|
| **Human Decision Gates** | `ask_question` modal + Markdown Artifact | `AskUserQuestion` / `ExitPlanMode` | Interactive stdin / prompt |
| **Subagent Spawning** | `invoke_subagent(Role=..., Model="pro"|"flash")` | `Agent(subagent_type="...")` | Isolated prompt session |
| **PreToolUse Hook Gate** | Tool-Execution Reflection Lock + Pre-check script | `PreToolUse` hook (`settings.local.json`) | Shell wrapper / pre-commit |

### Stage 0 — Contract: ask, don't assume

A writing plan may or may not already exist for this unit. Use
`AskUserQuestion` (Claude) or `ask_question` (Antigravity) to establish whether one does, and its path — never assume.

- **If a writing plan exists**: it is the primary input to Stage 1. Use `oracle_search` /
  `oracle_trace` to retrieve the relevant slice. **MANDATORY**: Explicitly scan the writing plan for a global/section rules block (such as Section 10 / "ข้อกำหนดรูปแบบการเขียน"), active actor identity (e.g. "คณะที่ปรึกษา" as the analytical subject), and altitude constraints. Extract and record them in `report_specific_rules`.
- **If none exists (or writing plan has no rules section)**: Use `ask_question` / `AskUserQuestion` to explicitly clarify:
  1. Actor convention (e.g., "คณะที่ปรึกษา" vs "กรมฯ" as subject)
  2. Tone & Persona (authoritative institutional vs technical brief)
  3. Altitude / Acronym policy (e.g. executive summary: ban internal acronym clutter)
  Record these under `report_specific_rules`.

Read [references/artifact-schemas.md](references/artifact-schemas.md) before
creating `writing-contract.json`. It must lock the audience, decision use,
section job, target altitude, report-specific rules, inclusions, exclusions, evidence policy, source
paths, and reference samples. Record which writing-plan path was taken in
`input_assets`, with an explicit `writing_plan: null` when none existed.

Present a compact contract summary and stop for human approval. Record that
approval in the contract.

### Stage 1 — Argument map

Spawn `th-argument-mapper` (Claude Code `Agent("th-argument-mapper")` or Antigravity `invoke_subagent(Role="TH Argument Mapper", Model="pro")`) with the approved contract, the source paths, and
the writing plan if one exists. It produces `argument-map.json`: a Minto
governing thought, an SCQA narrative arc, and ordered Toulmin argument units
— each with `claim`, `grounds`, `warrant`, `application_to_design`, and a
`supports` value that must partition `governing_thought_components`.

**Altitude filter**: When `target_altitude` is `executive-summary`, grounds must prioritize synthesized findings and operational impacts over raw internal acronyms or micro-activity lists.

The subagent validates its own output with
`argument_gate.py validate <map>` before reporting done. Do not accept a map
that hasn't passed this check.

Do not economize on model or effort here — this is the stage where the
thinking v5.0 skipped must actually happen.

### Stage 2 — Blueprint gate (human)

- **In Claude Code**: Use plan mode: present the governing thought, the SCQA arc, and one line per
  argument unit, then `ExitPlanMode` for approval via `AskUserQuestion`.
- **In Antigravity**: Render the governing thought, SCQA arc, and argument units as a formatted Markdown Artifact in the workspace, then call `ask_question` with options:
  1. "(Recommended) Approve argument map — proceed to Stage 3 verbalization"
  2. "Amend argument map — request structural revision of warrants"
  3. "Reject argument map — restart Stage 1 with new perspective"

Only once approved does `approval.status` become `"approved"` in
`argument-map.json`. This is the field the `PreToolUse` hook / reflection lock checks; nothing
else unlocks Stage 3.

### Stage 3 — Verbalization

Spawn `th-verbalizer` (Claude Code `Agent("th-verbalizer")` or Antigravity `invoke_subagent(Role="TH Verbalizer", Model="flash")`) with the approved `argument-map.json`,
[references/prose-kernel.md](references/prose-kernel.md), and the contract's `report_specific_rules`, `target_altitude`, and `terminology` — never the
raw sources, never the full `STYLE_PACK_TH.md`. Treat each argument unit's
`claim` / `grounds` / `warrant` / `application_to_design` as the paragraph's
payload; enforce the contract's active actor identity and report rules. Do not force a four-part structure onto paragraphs the map does not
call for. One dominant job per paragraph, matching the unit's `paragraph_job`.

**Bounded amendment path**: if verbalizing a unit reveals its `warrant`
doesn't actually hold in real prose, the subagent halts and proposes an
amendment rather than papering over it or silently deviating. The amendment
returns to the Stage 2 human gate, gets logged, and the map is re-approved.
One bounded loop, not free revision — "transcribe the approved map" is still
transcription if a broken warrant just gets rendered faithfully.

Evidence-traceability notes, slide/page locators, prompt scaffolding, and
report roadmaps belong outside audience-facing prose. A requested diagram
becomes a figure placeholder or actual figure, never an inline arrow chain.

### Stage 4 — Mechanical checks

For report prose, run:

```text
python .agents/skills/writing-th/scripts/lint_thai_writing.py <draft> ψ/memory/style/LEXICON_TH.json --scope report
```

For `rewrite` mode only, also run:

```text
python .agents/skills/writing-th/scripts/check_density.py <source> <draft>
```

`check_density.py` now enforces both a floor (0.8, catches under-preservation)
and a ceiling (1.6, catches padding that hides a thin argument). Override
either with positional args if a section's transformation genuinely warrants
it — that is a deliberate exception, not a default.

Fix blocking failures. Carry every non-blocking `[STRUCTURAL]`,
`[PARENTHETICAL]`, `[ARTIFACT]`, or `[META]` review item into the editorial
receipt with a disposition. A green result here means only **mechanical pass**.

### Stage 5 — Editorial review

Default to `th-editorial-reviewer` run as an independent clean-context subagent call (Claude Code `Agent("th-editorial-reviewer")` or Antigravity `invoke_subagent(Role="TH Editorial Reviewer", Model="pro")`) — never
a shared/forked context that inherits the parent's drafting history, which
destroys the clean-context independence the rubric depends on. A genuinely
independent reviewer is one subagent call away; the v5.0
`reviewer_mode: self, assurance: degraded` fallback should be unreachable in
practice.

Give the reviewer only the approved contract, the approved argument map, the
draft, the selected profile rubric, and a reference sample if one exists. Do
not provide the intended verdict or the drafting agent's self-justification.

Read [references/editorial-rubric.md](references/editorial-rubric.md)
beforehand. Review runs in two tiers: **Tier 1** judges the argument map's
own reasoning (does each `warrant` actually connect its `grounds` to its
`claim`? does `governing_thought_components` genuinely partition the
governing thought, not just satisfy the mechanical MECE check?) — this must
pass before Tier 2 proceeds, or a passing editorial receipt ends up
certifying a causal bridge that was never actually established. **Tier 2** is
the familiar per-draft rubric, now including `argument_fidelity`: every
approved unit's claim and warrant should appear in the draft, and no claim in
the draft should be absent from the map.

Create a receipt scaffold with:

```text
python .agents/skills/writing-th/scripts/editorial_gate.py prepare <draft> <contract> --out <review> --reviewer-mode independent
```

Complete every required rubric dimension and record located findings. A
receipt passes only when its verdict is `pass`, all required dimensions pass
(or `source_fidelity` is legitimately `not_applicable` in `new` mode), and no
critical or major finding remains unresolved.

Optionally, run `warrant_trace.py <map> <draft>` first for partial mechanical
Tier 2 coverage — it checks that each approved warrant has a corresponding
claim present in the draft. Genuine semantic judgment still belongs to the
reviewer.

Verify it with:

```text
python .agents/skills/writing-th/scripts/editorial_gate.py verify <draft> <contract> <review>
```

Any draft or contract change invalidates the receipt. Review the new hashes.

### Stage 6 — Human bridge and merge

Present the draft with its editorial assurance and unresolved minor findings.
Merge only after explicit human approval:

```text
python .agents/skills/writing-th/scripts/merge_draft.py <draft> <dest> --lexicon ψ/memory/style/LEXICON_TH.json --contract <contract> --review <review> [--source <source>]
```

Merge reruns mechanical checks, verifies the exact receipt hashes, and
confirms that all emitted review items have dispositions. `--skip-gates`
remains a loud, deliberate override; never infer permission to use it.

## Maintenance

- After a style-capture round, validate the lexicon with
  `validate_lexicon.py`; do not edit style memory from this skill.
- After changing canonical `SKILL.md` or `references/`, run
  `check_skill_drift.py --sync`.
- Run `tests/run_tests.py` after any harness change.
- A behaviorally significant revision requires a blind forward test in an
  isolated temporary workspace. Use an independent reviewer when delegation is
  available; otherwise document that the test used degraded self-review.
