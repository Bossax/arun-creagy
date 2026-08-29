---
date: 2026-08-29
type: analysis
topic: writing-th-v6-codex-adaptation
status: ready-for-review
target: writing-th v6.0 on the shared Codex/Antigravity workspace
companions:
  - "[[2026-08-29_writing-harness-skill-architecture-analysis]]"
  - "[[2026-08-29_writing-th-v6-build-blueprint]]"
  - "[[2026-08-29_writing-th-v6-antigravity-adaptation]]"
author: Codex (GPT-5)
---

# Analysis: writing-th v6.0 — Codex Adaptation

## 1. Executive summary

The Antigravity adaptation identifies the right architectural invariants, but
its execution layer is runtime-specific. Codex and Antigravity share the same
`.agents/` skill tree, `AGENTS.md` governance, project files, Python scripts,
artifacts, and review rules. The Codex adaptation therefore changes the
orchestration and approval model without duplicating the skill architecture.

The shared v6.0 design remains:

1. `writing-contract.json` locks scope, audience, evidence, and authorization.
2. `argument-map.json` constructs the logical and rhetorical spine.
3. A human approves the argument map before prose is drafted.
4. A verbalizer renders only the approved map into Thai prose.
5. Mechanical scripts and an independent editorial review produce a quality
   receipt before merge.

The main Codex constraint is that a prompt-level instruction is not an
enforcement mechanism. Any invariant that must be non-bypassable needs either a
runtime hook that Codex actually supports, a deterministic wrapper script, or a
hard stop in the skill workflow plus explicit human approval. The design must
not import Antigravity primitives by analogy.

## 2. What stays shared

### Shared governance

`.agents/` and `AGENTS.md` are shared by Codex and Antigravity. The following
must remain common rather than forked:

- the `writing-th` skill and its references;
- project-local safety rules and the reflection lock;
- draft isolation and explicit merge approval;
- the prohibition on ordinary ledger writes;
- lexicon, style-pack, and miss-register maintenance boundaries;
- the artifact schemas and hash-binding conventions;
- deterministic Python validation scripts;
- the blind-test and regression-test expectations.

### Shared artifacts

Both runtimes should produce the same artifact contract:

```text
01_writing-contract.json
02_argument-map.json
03_th_draft.md
04_editorial-review.json
```

The artifacts must be portable across runtimes. A section started in
Antigravity should be reviewable or continued in Codex without translating the
logical content into a second schema.

### Shared context boundary

The argument map remains the compression boundary. Stage 1 needs sources and a
writing plan when one exists; it does not need the style pack. Stage 3 needs the
approved argument map and the compact prose kernel; it does not need the raw
sources. Stage 5 needs the draft, argument map, and editorial rubric; it does
not need the parent conversation or full style history.

## 3. What adapts for Codex

### 3.1 Skill invocation replaces runtime-specific orchestration

The shared `writing-th/SKILL.md` is the primary workflow contract. Codex must
follow its stages and read the required references before acting. The Codex
adaptation should not assume Antigravity's `invoke_subagent`, `ask_question`,
Markdown Artifacts, or `.agents/hooks.json` interfaces.

If the current Codex runtime exposes an approved delegation mechanism, it may
be used for the mapper, verbalizer, and reviewer. If not, the skill must
declare the fallback explicitly:

- use a separate clean Codex context/session for independent review when
  available; or
- perform a structured self-review and mark the receipt
  `reviewer_mode: self` and `assurance: degraded`.

The fallback must never be presented as equivalent to independent review.

### 3.2 Approval is a conversation checkpoint

Antigravity can expose `ask_question` and a right-hand Artifact panel. Codex
should render a compact approval surface in the conversation containing:

- governing thought;
- SCQA situation, complication, question, and answer;
- one line for each ordered argument unit;
- each unit's warrant and `application_to_design`;
- unresolved qualifiers or counter-arguments.

The workflow then stops and waits for an explicit human response such as
`Approve`, `Amend`, or `Reject`. Because `AGENTS.md` requires reflection before
state-changing actions, Codex must not create or modify the prose draft before
that response.

### 3.3 Shared filesystem, runtime-sensitive writes

Codex and Antigravity can inspect the same project state, so artifact paths and
hashes are shared. However, the existence of a shared filesystem increases the
risk of concurrent writes. The workflow should therefore:

- verify file state immediately before writing;
- preserve another runtime's edits when a file changed on disk;
- avoid editing a co-authored analysis in place without a clear attribution
  boundary;
- use a signed append or a new adaptation document when reconciling divergent
  runtime proposals.

The parent orchestration context should carry paths, hashes, gate verdicts, and
approval state—not entire source packs or historical style logs.

## 4. Codex stage map

| Stage | Codex responsibility | Context | Gate |
|---|---|---|---|
| 0 | Inspect sources, ask whether a writing plan exists, create contract | plan index and paths | Human approval |
| 1 | Build argument map | sources, plan if present, argument schema | Mechanical schema check |
| 2 | Present map and stop | rendered map summary only | Human Approve/Amend/Reject |
| 3 | Verbalize approved map | map and prose kernel | Draft isolation |
| 4 | Run lint, density, and argument checks | CLI inputs only | Exit-code gate |
| 5 | Perform clean-context editorial review if available | draft, map, rubric | Review receipt |
| 6 | Verify hashes and await merge approval | artifact paths and verdicts | Human merge approval |

Stage 0 must ask whether a writing plan exists. It must not assume that the
plan described by the earlier architecture is present. The contract should
record `writing_plan: null` when the argument map is built directly from
approved sources.

## 5. Codex-specific enforcement strategy

The Antigravity blueprint proposes lifecycle hooks in `.agents/hooks.json`.
That configuration must not be copied into the shared tree unless both runtimes
recognize it. A shared file that only one runtime understands would create a
false sense of enforcement for the other.

For Codex, enforcement should be layered:

1. **Skill-level stop**: `writing-th/SKILL.md` requires reflection and explicit
   approval before draft writes.
2. **Deterministic precondition script**: a script checks the target path,
   existence of `argument-map.json`, and `approval.status` before a draft write.
3. **Runtime hook, if verified**: configure only a Codex-supported hook or tool
   wrapper after testing its exact event and payload contract.
4. **Post-write lint**: run `lint_thai_writing.py` and record findings in the
   editorial receipt.

The precondition script should fail closed for an unknown payload or an
unapproved map. It should not infer approval from a natural-language sentence
inside a draft or from a prior session summary.

## 6. Schema and implementation corrections

The Codex build must carry forward the corrections already identified in the
shared blueprint:

- retain `kind: structural` in `LEXICON_TH.json`; the live linter reports these
  as non-blocking human-review items;
- add explicit argument-unit ordering and a `supports` field so the governing
  thought's MECE structure is inspectable;
- make `paragraph_job` use one authoritative enum, aligned with the style pack;
- keep `warrant` and `application_to_design` mandatory for substantive units;
- support one bounded amendment loop from verbalization back to the approved
  map gate;
- split references by consumer and extract a compact prose kernel;
- archive historical capture material rather than loading it into every stage.

## 7. Risks specific to the shared Codex/Antigravity workspace

### Runtime drift

A shared skill can silently accumulate instructions valid in one runtime but
ignored by the other. Every runtime-specific instruction should be labelled in
the skill or placed in a clearly named adaptation document.

### Concurrent modification

Both agents can modify the same inbox and draft files. A file-change warning is
helpful but not a coordination protocol. Build and review steps should use
small, hash-visible artifacts and avoid simultaneous edits to the same file.

### False hook confidence

The presence of a hook-looking JSON file does not prove Codex enforces it. The
hook must be tested with a deliberately failing draft write and the observed
runtime response recorded before it is described as binding.

### Review contamination

A reviewer operating in the parent context may inherit the drafting model's
assumptions. Codex should prefer a genuinely new context. If that is not
available, the degraded-review status must be explicit in the receipt.

## 8. Codex build order

1. Reconcile this analysis with the shared Antigravity adaptation and blueprint.
2. Define the portable artifact schemas, including ordering and `supports`.
3. Implement and test `argument_gate.py prepare` and `validate`.
4. Implement the precondition check and determine whether Codex supports a
   verified blocking hook or wrapper.
5. Split references and extract `prose-kernel.md`; archive style-capture history
   through the appropriate maintenance workflow.
6. Rewrite the shared `writing-th/SKILL.md` for v6.0, marking runtime-specific
   execution notes clearly.
7. Add the bounded amendment path and optional `warrant_trace.py`.
8. Run a blind end-to-end test separately in Codex and Antigravity, then run
   the shared test suite.

The lexicon promotion for the recurring negation-contrast pattern remains a
separate maintenance task and should use the style-capture workflow rather
than being folded into ordinary writing execution.

## 9. Decision summary

The correct relationship is one shared writing harness with runtime adapters,
not two independent writing skills. `.agents/` and `AGENTS.md` remain the
common control plane. The artifacts, schemas, scripts, style rules, and quality
criteria remain common. Only the orchestration surface, delegation availability,
approval presentation, and write-enforcement mechanism vary by runtime.

Codex's implementation should therefore be conservative about claiming
automation: where a mechanism has not been verified in the live Codex runtime,
the workflow must expose the limitation and preserve the human gate.

*Signed: Codex (GPT-5) — 2026-08-29, Codex adaptation analysis.*
