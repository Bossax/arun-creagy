---
date: 2026-08-29
type: blueprint
topic: writing-th-v6-execution-architecture
status: ready-to-build
target: writing-th v6.0
companion: "[[2026-08-29_writing-harness-skill-architecture-analysis]]"
author: Claude Opus 5 (claude-opus-5), Claude Code
---

# Build Blueprint — writing-th v6.0 Execution Architecture

This is the implementation companion to the architecture analysis in
[[2026-08-29_writing-harness-skill-architecture-analysis]] (§6–§8). That
document defines **what the artifacts are**. This one defines **who runs each
stage, in what context, and what enforces the gates** — the part that decides
whether v6.0 costs more tokens than v5.0 or less.

Read §6 (writing-process science), §7 (v6.0 proposal), and §8 (artifact design)
first. This blueprint assumes them and does not restate them.

---

## 1. Governing principle

The `argument-map.json` artifact is a **compression boundary**, not just an
added file.

Today one context carries the writing plan, raw sources,
[[STYLE_PACK_TH]] (56,961 bytes), [[LEXICON_TH]] (22,993 bytes), and the
editorial rubric, then performs scope, argument, prose, and self-review inside
it. Thai content is token-expensive; call it 60–80K tokens of loaded material
before the first Thai sentence exists.

But the stages have disjoint needs:

- **Argument construction** needs sources and any writing plan. It needs no
  style material at all — it produces structured fields, not prose.
- **Verbalization** needs the approved map and a style kernel. It does not need
  the raw sources, because the grounds are already extracted into the map.

Neither stage needs both halves. v5.0 loads both into one context. Enforce the
split as a context boundary and per-stage load roughly halves, while the parent
carries neither.

**The parent session becomes an orchestrator holding artifact paths, gate
verdicts, and file hashes — never content.**

---

## 2. Correction to §7.3 Stage 0 — the writing plan is optional

§7.3 Stage 0 reads "Ingest existing hand-crafted writing plans." This is wrong
as an assumption. A writing plan may or may not exist when the skill is invoked.

Stage 0 must **ask**, not assume:

- Use `AskUserQuestion` to establish whether a prior writing plan or evidence
  base exists for this unit, and if so its path.
- If one exists: it is the primary input to Stage 1, and `oracle_search` /
  `oracle_trace` retrieve the relevant slice rather than loading the file whole.
- If none exists: Stage 1 builds the argument map directly from the approved
  sources. The map itself then becomes the writing plan for that unit, and
  should be preserved as such.

`writing-contract.json` records which path was taken in `input_assets`, with an
explicit `writing_plan: null` when none existed. A reviewer must be able to tell
whether the argument was derived from prior planning work or built fresh.

---

## 3. Stage → agent → context map

| Stage | Runs as | Loads | Must never load |
|---|---|---|---|
| 0 Contract | Parent + `AskUserQuestion` | plan index, source paths | sources, style material |
| 1 Argument map | subagent `th-argument-mapper` | sources, writing plan (if any), argument schema | style pack, lexicon, rubric |
| 2 Blueprint gate | Parent, plan mode | rendered map summary | everything else |
| 3 Verbalization | subagent `th-verbalizer` | `argument-map.json` (~3 KB), prose kernel (~5 KB) | raw sources, full pack, rubric |
| 4 Mechanical gate | CLI only | — | nothing enters a model context |
| 5 Editorial review | subagent `th-editorial-reviewer` | draft, argument map, rubric | sources, style pack |
| 6 Merge | CLI + parent | hashes, verdicts | — |

### Agent definitions to create

Follow the existing repo pattern in [[wp2-demand-scorer]] (frontmatter carries
`name`, `description`, `model`, `reasoning_effort`, `tools`).

Create three files in `.claude/agents/`:

**`th-argument-mapper.md`**
- `model`: strongest available; `reasoning_effort: high`
- `tools`: `Read, Grep, Glob, Write`
- Job: produce `argument-map.json` — governing thought, SCQA arc, Toulmin
  argument units with mandatory `warrant` and `application_to_design`.
- This is the stage where the thinking effort that v5.0 skipped must actually
  happen. Do not economize on model or effort here.

**`th-verbalizer.md`**
- `model`: strong model — Thai idiom quality matters
- `tools`: `Read, Write`
- Job: verbalize an approved argument map into Thai institutional prose.
  No argument formulation on the fly. If a warrant will not carry in prose,
  halt and propose a map amendment (see §5).

**`th-editorial-reviewer.md`**
- `model`: strong model; `reasoning_effort: high`
- `tools`: `Read, Write`
- Job: clean-context Tier 1 (map) and Tier 2 (prose fidelity) review.

**Anti-pattern**: never use `subagent_type: "fork"` for Stage 5. A fork inherits
the parent's full context, which destroys the clean-context independence the
rubric requires. v5.0's `reviewer_mode: self, assurance: degraded` fallback
should become unreachable in practice — a genuinely independent reviewer is one
`Agent` call away.

---

## 4. Hooks — convert invariants into constraints

`.claude/settings.local.json` currently configures **no hooks**. This is the
highest-leverage unused capability in the stack.

Prose instructions get skipped under load. That is the demonstrated failure mode
behind the negation-contrast pattern recurring across sessions — the promotion
step in [[style-capture SKILL]] 4b/5 was skipped by a person following prose. A
hook cannot be skipped.

**Hook 1 — PreToolUse on `Write`** (blocking)
Reject any write to `ψ/incubate/drafts/**/*draft*.md` when the sibling
`argument-map.json` is absent or its `approval.status` is not `approved`.

This makes "no prose before the logic is approved" a physical property of the
harness rather than an instruction the drafting agent may ignore. It is the
single most important line of the whole design.

**Hook 2 — PostToolUse on `Write`** (advisory)
Auto-run [[lint_thai_writing]] on any written draft. Violations return as
feedback automatically; the model spends no tokens remembering to lint or
deciding when.

Use the `update-config` skill to author these rather than hand-editing settings.

---

## 5. Recursion — a bounded amendment path

§7.3 as written is a strict waterfall, which contradicts the science §6 cites.
Flower & Hayes's core finding is that planning, translating, and reviewing are
recursive under a monitor; Bereiter & Scardamalia's knowledge-transforming is
explicitly dialectical between the content and rhetorical problem spaces.

Once the map is approved and hash-locked at Stage 2, a strict pipeline leaves
Stage 3 two bad options when verbalization reveals a warrant that does not hold:
deviate silently, or faithfully render a bad argument. "Transcribe the approved
map" is still transcription — knowledge-telling one level up.

**Required**: Stage 3 may halt and emit a proposed amendment to
`argument-map.json` rather than papering over a failed warrant. The amendment
returns to the Stage 2 human gate, is logged, and re-locks the hash. One bounded
loop, not free revision. This preserves the dialectic without giving up the
gate.

---

## 6. Push deterministic work into CLI

The existing script pattern in `.agents/skills/writing-th/scripts/` is the right
instinct. Extend it. **Anything checkable by schema or string logic must never
reach a model context.**

**`argument_gate.py validate <map>`**
- every unit has non-empty `warrant` and `application_to_design`
- `governing_thought` present and non-empty
- unit `supports` values partition the governing thought — this is the MECE
  check made mechanical (see §7)
- no duplicate `unit_id`; every `paragraph_job` in the allowed enum
- exit 1 blocks, same convention as the existing gates

**`argument_gate.py prepare <contract>`**
- emit the map skeleton pre-filled from the contract so the model fills fields
  rather than inventing structure — mirrors [[editorial_gate]] `prepare`

**`warrant_trace.py <map> <draft>`**
- check each approved warrant has a corresponding claim present in the draft
- partial Tier 2 fidelity for free; genuine semantic judgment still goes to the
  Stage 5 reviewer

---

## 7. Schema corrections carried from the review

Three fixes to §7–§8 that must land in the build:

**Keep `kind: structural` in [[LEXICON_TH]].** §8.2 proposes eliminating it on
the grounds that structural rules caused silent no-ops and non-terminating
loops. This inverts the Tranche 1 history. The no-op bug was prose descriptions
written into `banned` on rules that were *not* marked structural; the
non-terminating loop was fixed *by moving* the offending rule to
`kind: structural`. [[lint_thai_writing]] line 10 documents structural as
"reported for human review, never blocks," and lines 234–238 print them as a
separate non-blocking channel. Removing the category also dead-ends the return
arc: a pattern that crosses the ≥2 promotion threshold but is not
regex-expressible would have nowhere to go, and the pressure becomes dropping
the rule or forcing a bad regex — exactly how the 2026-08-05 round produced
three dead rules. Instead, tighten the requirement that a structural entry state
a checkable condition rather than a paragraph of English.

**Give `argument_units` ordering and a `supports` field.** A flat array of
well-formed Toulmin units is a better-justified patchwork, still a patchwork.
Minto's pyramid is a hierarchy with load-bearing order, not a list. Tier 1 is
specified to check MECE compliance but the schema has no field to check it
against. Add per unit a `supports` value naming which part of the governing
thought it carries, plus an explicit ordering rationale. Without this the
storyline complaint is not actually addressed.

**Align `paragraph_job` with the style pack.** §8.4 uses
`define / diagnose / compare / mandate`; [[STYLE_PACK_TH]] rule 6 uses
`define / diagnose / compare / conclude`. Pick one and make the enum
authoritative in `argument_gate.py`.

---

## 8. Progressive disclosure in the skill

[[writing-th SKILL]] currently instructs whoever is running to read
[[editorial-rubric]] *before creating the contract* — so the drafting path loads
a review rubric it never uses. Split `references/` by consumer so each subagent
loads only its own:

- `references/argument-schema.md` → Stage 1 only
- `references/prose-kernel.md` → Stage 3 only
- [[editorial-rubric]] → Stage 5 only

The prose kernel is where §8.3's compression pays twice. The extracted Core
Kernel plus Anti-AI Shield is roughly 5 KB against the pack's 57 KB, and
[[STYLE_PACK_TH]] §9's Incremental Capture Log — 35,812 bytes, 62.9% of the
file, verified — never enters any model context again once archived to
`ψ/archive/style/capture_history/`.

---

## 9. Model tiering

`Agent` accepts a `model` override, and [[wp2-demand-scorer]] already pins
`claude-sonnet-5` with `reasoning_effort: high`. Apply deliberately:

| Work | Tier |
|---|---|
| Argument construction (Stage 1) | strongest model, high effort — this is where the missing thinking happens |
| Verbalization (Stage 3) | strong model — Thai idiom quality matters |
| Source scanning / grounds extraction | Haiku — it is retrieval |
| Mechanical disposition write-ups | Haiku |

---

## 10. Human gates

Reviewing raw `argument-map.json` is a poor review surface. Use plan mode for
Stage 2: present the governing thought, the SCQA arc, and one line per argument
unit, then `ExitPlanMode` for approval. Use `AskUserQuestion` for bounded
choices — writing plan present or not, profile, transformation mode,
approve / amend / reject. Both are cheaper than conversational negotiation and
give a better surface than JSON.

---

## 11. Oracle MCP

**`oracle_search` / `oracle_trace` at Stage 0** — retrieve the relevant slice of
any prior writing plan rather than loading whole files into context.

**`oracle_thread` per chapter section** — argument-map decisions and their
rationale survive across sessions instead of being re-derived each time.

**`oracle_learn` at return-arc Stage F** — unchanged from current behavior.

---

## 12. Build order

Cheapest first, and the early items are the ones that stop gates from being
skipped:

1. **Two hooks** (§4) — highest leverage, smallest diff. The PreToolUse block is
   what makes the whole architecture real rather than advisory.
2. **Three agent definitions** (§3) in `.claude/agents/`.
3. **`argument_gate.py`** validate + prepare (§6).
4. **Reference split** (§8) and prose-kernel extraction; archive
   [[STYLE_PACK_TH]] §9 to `ψ/archive/style/capture_history/`.
5. **[[writing-th SKILL]] v6.0 rewrite** wiring stages to agents, with the Stage
   0 writing-plan question (§2) and the Stage 3 amendment path (§5).
6. **`warrant_trace.py`** (§6) — last, it is the optional one.
7. **Blind forward test** in an isolated temporary workspace per the existing
   maintenance rule, then `tests/run_tests.py`.

---

## 13. Expected token profile

| | v5.0 | v6.0 |
|---|---|---|
| Parent context | full sources + style + rubric, ~60–80K | paths, verdicts, hashes — a few K |
| Argument work | fused into drafting pass | isolated, ~20–30K, no style loaded |
| Drafting | same context as everything else | ~10K — map + kernel only |
| Review | often degraded self-review, same context | ~15K, genuinely clean |
| Lexicon in model context | loaded | never — CLI consumes it, only violations surface |

The lexicon should not enter a model context at any stage. [[lint_thai_writing]]
reads it; only the violations need to reach a model. The same discipline applies
to the archived capture log.

---

## Related

- [[2026-08-29_writing-harness-skill-architecture-analysis]] — §6 science, §7 v6.0 proposal, §8 artifact design
- [[2026-08-29_12-46_crdb-exec-summary-editing-points-audit]] — the 14 edit points that triggered this
- [[2026-08-29_13-00_writing-th-harness-architecture]] — v5.0 architecture of record

---

*Signed: Claude Opus 5 (claude-opus-5), Claude Code — 2026-08-29. Companion to*
*§6–§8 of [[ψ/inbox/2026-08-29_writing-harness-skill-architecture-analysis|2026-08-29_writing-harness-skill-architecture-analysis]].*
*Built for execution in a following session; nothing here has been implemented.*
