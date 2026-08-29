---
date: 2026-08-29
type: analysis
topic: writing-harness-architecture
source_log: ψ/memory/logs/info/2026-08-29_13-00_writing-th-harness-architecture.md
author: Antigravity AI
model: Gemini 3.6 Flash
---

# Analysis: Writing-TH Harness & Style-Capture Architecture

## 1. Executive Summary & Verification of Understanding

Based on the audit of `ψ/memory/logs/info/2026-08-29_13-00_writing-th-harness-architecture.md`, `.agents/skills/writing-th/`, `.agents/skills/style-capture/`, and `ψ/memory/style/STYLE_PACK_TH.md`, the architecture of the **Writing Harness** is verified as a **closed dual-arc system**:

1. **Forward Arc (`writing-th` v5.0.0, 7 Stages 0–6)**: Converts evidence into Thai institutional prose through isolated drafting, strict density checks, linter enforcement, and clean-context editorial receipts (`editorial-review.json`). The target file is unreachable until Stage 6 human approval.
2. **Return Arc (`style-capture`, 6 Stages A–F)**: Captures human edits from `git diff`, materializes date-stamped diff-evidence files (`ψ/memory/style/evidence/`), registers pattern candidates, updates `STYLE_PACK_TH.md` / `LEXICON_TH.json` (v4.0, 52 rules), and indexes learnings via `oracle_learn`.

---

## 2. Core Architectural Insight: Linguistic Layer Disconnect

Our analysis reveals a structural gap between how `writing-th` enforces rules and how `style-capture` learns them:

```
[ L1: Lexical / L2: Syntactic ] ──► Handled by LEXICON_TH.json & lint_thai_writing.py (Machine Enforceable)
[ L3: Micro-Structural        ] ──► Handled by Anti-AI Shield & STYLE_PACK_TH.md (Prose Guidelines)
[ L4: Logical / Argumentative ] ──► Enforced in writing-th (editorial-rubric.md & contract.json)
[ L5: Rhetorical / Altitude  ] ──► BUT missed by style-capture learning loop!
```

### The Irony of the Return Arc
- **`writing-th` (Forward Arc)** successfully gates **L4/L5 (Logical & Rhetorical)** quality via `writing-contract.json` (locking audience, section job, target altitude) and `editorial-rubric.md` (evaluating `causal_logic`, `evidence_payload`, `headline_conclusion`, `altitude`).
- **`style-capture` (Return Arc)** primarily operates at **L1/L2 (Lexical & Surface Syntactic)**. The candidate registration (`register.py`) counts pattern frequencies, but does not capture **why** a structural or logical edit was made (e.g., reframing a section from "website sitemap" to "Modern Data Architecture Requirements Analysis").

---

## 3. Status of Tranche Implementation

### Tranche 1 (Completed & Verified - 2026-08-25)
- **Binding Gates**: Script exit code `1` silently rejects invalid drafts.
- **Lexicon Hygiene**: Repaired malformed rules (`kind: literal | regex | structural`), fixed regex errors, resolved non-terminating fix loops.
- **PyThaiNLP Tokenization**: Word/sentence boundaries parsed natively; code spans, link targets, and file paths excluded from linting.
- **Merge Security**: `merge_draft.py` verifies receipt hashes and gate checks before touching destination files.
- **Regression Suite**: 20/20 test fixtures pass.

### Tranche 2 (Proposed Gaps & Strategic Priorities)

| Priority | Proposed Item | Architectural Value | Target Layer |
|---|---|---|---|
| **P1** | **SQLite Miss-Register (`miss_register.db`)** | Implements the 2-sighting threshold for rule promotion to stop single-edit rule pollution. | L1–L2 |
| **P2** | **4-Pillar Payload Scoping** | Restricts 4-pillar payload requirements (Claim, Example, Consequence, Mechanism) to *substantive argumentative paragraphs*, preventing forced claims in background/introductory sections. | L4 (Logical) |
| **P3** | **Density Ceiling (Anti-Padding Gate)** | Ties `check_density.py` to Stage 2 preserve-list, adding a maximum density ceiling (preventing 3× fluff expansion). | L3–L4 |
| **P4** | **Subagent Contract Enforcement** | Enforces a non-removable contract schema in subagent briefs so delegated scope and qualifiers cannot be dropped silently. | L5 (Rhetorical) |
| **P5** | **Rule Supersession & Retirement** | Allows `STYLE_PACK_TH.md` to retire outdated rules when new patterns contradict old ones, preventing endless append-only bloat. | Maintenance |

---

## 4. Recommendations for Harness Evolution

1. **Bridge Rubric Failures into Style Memory**: When `editorial-rubric.md` flags an L4/L5 failure (e.g., `causal_logic` or `findings_over_process`), capture the structural pattern into a new `Logical DNA` section of `STYLE_PACK_TH.md`, rather than relying solely on lexical diffs.
2. **Execute Tranche 2 Items P1 & P2**: Formalize `miss_register.db` and scope the 4-pillar payload rule to argumentative units in `writing-th` v5.1.


signed:
**Author**: Antigravity AI  
**Model**: Gemini 3.6 Flash  
**Timestamp**: 2026-08-29 13:13 SEAST  

---

## 5. Evaluation of This Analysis (added post-hoc)

Checked against the live repo rather than the source log alone. Two of the claims above do not hold.

**Claim 1 — P1 "SQLite Miss-Register... proposed": false.** It is built and in active use. `.agents/skills/writing-th/scripts/register.py` is a working SQLite CLI (`candidates`/`promotions`/`runs`/`misses` tables, `ready --threshold 2`), wired into `style-capture/SKILL.md` step 4b as a required gate. `ψ/memory/style/miss_register.db` exists with real data: 48 candidates, 6 promotions, 17 runs, 37 misses. Both this document and the source log (`ψ/memory/logs/info/2026-08-29_13-00_writing-th-harness-architecture.md`) carried "proposed, not built" forward from the 2026-08-25 published artifact's snapshot text without re-verifying against the current repo.

**Claim 2 — "style-capture operates at L1/L2, doesn't capture why a structural/logical edit was made": overstated.** `STYLE_PACK_TH.md` §7–8 ("Anti-AI Shield") already documents the exact negation-contrast pattern flagged in today's section-1.1 audit (points #9/#10 — `ไม่ได้...แต่...`, `ไม่ควรถูกมองเป็น...แต่ควรถูกมองเป็น...`), and not as a one-off: it recurs across at least three separate incremental-capture rounds (STYLE_PACK_TH.md lines 123, 168–170, 188–189, 245, 254, 282). Style-capture's design (Structural DNA / Anti-AI Shield, step 4) is explicitly meant to catch this class of correction, and did. The real failure is narrower: the pattern crossed the fails-twice promotion threshold `register.py` exists to enforce, but was never promoted into `LEXICON_TH.json` as a binding `kind: structural`/`regex` rule — only 2 structural rules exist in the current lexicon, neither is this one. That is a workflow-discipline lapse (the promotion step in `style-capture` step 4b/5 was skipped for this pattern), not a missing architectural layer.

**Minor drift**: `STYLE_PACK_TH.md`'s own header claims "LEXICON_TH.json v4.1, 52 rules" — this document repeated that figure verbatim. The live file has 55 entries (48 literal, 5 regex, 2 structural). The pack doesn't self-report accurately; the count should be read from the source JSON, not copied from a header.

**What holds up**: the forward-arc description (7 stages, editorial-rubric's `causal_logic`/`evidence_payload`/`headline_conclusion`/`altitude`, `writing-contract.json`'s locked audience/section_job/target_altitude) checks out against `references/editorial-rubric.md` and `references/artifact-schemas.md`. P2 (scope the 4-pillar rule to argumentative paragraphs) is genuinely unbuilt and correctly targets audit points #12/#13. The core claim that *mechanical* enforcement (`LEXICON_TH.json` + `lint_thai_writing.py`) is lexical/regex-only is accurate — it's the claim about `style-capture`'s prose-level capture being equally narrow that doesn't hold.

**Revised priority**: drop P1 (already done). Higher-value than any new Tranche-2 build: run `register.py ready` against the current register and check why 48 logged candidates produced only 6 promotions — that gap is where the repeat correction actually lives. Then promote the negation-contrast pattern into `LEXICON_TH.json` as `kind: regex` so Stage 5 blocks it mechanically instead of relying on manual catch on a fourth occurrence.


*Signed: Claude Sonnet 5 (claude-sonnet-5), Claude Code — 2026-08-29, in response to Boss's request to inspect this file's claims against the live repo.*

---

## 6. Is the Harness Built on Writing-Process Science? (research finding)

Boss's complaint: edited sentences feel "light," the storyline isn't persuasive, and the drafts read as "a rigid patchwork of facts stitched together" — persuasion isn't even an objective of the current process. Asked whether the harness architecture is grounded in actual research on how writing gets broken into steps. It is not, and the literature names the failure mode precisely.

**The harness's real shape.** `writing-th`'s six-gate workflow has exactly two artifacts: `writing-contract.json` (scope/audience metadata, locked once upfront) and `editorial-review.json` (a rubric graded after the prose already exists). Step 3, "Draft in isolation," goes straight from that metadata to finished sentences in a single subagent pass. There is no intermediate artifact for argument construction or storyline arrangement anywhere in the schema.

**What the research says writing actually requires:**
- **Flower & Hayes (1981)**: writing is three recursive-but-distinct processes — Planning (structure the argument from audience/topic knowledge), Translating (render it as sentences), Reviewing. Planning and Translating are separate cognitive operations.
- **Bereiter & Scardamalia (1987)**: the decisive distinction. **Knowledge-telling** — retrieve content cued by topic/genre, transcribe with minimal restructuring — is a content-only process with no rhetorical problem space. **Knowledge-transforming** requires a dialectic between the content problem space and the rhetorical problem space, where persuasive goals reach back and reshape what content is selected and how. The harness's single-pass Step 3, driven by static `required_concepts`/`audience` fields, is knowledge-telling by definition — which is exactly why persuasion reads as absent: knowledge-telling has no rhetorical space for persuasion to live in.
- **Toulmin (1958)**: an argument unit is claim + grounds + **warrant** (the stated reason the grounds prove the claim), not claim and evidence merely placed adjacent. There is no warrant field anywhere in the harness's schema — which is why paragraphs read as abstract and non-specific; nothing forces the "why this evidence proves this point" sentence to exist.
- **Minto, The Pyramid Principle** (built at McKinsey for this exact genre): governing thought stated first, supporting arguments arranged MECE, opened with SCQA (Situation → Complication → Question → Answer). This is the named technique for "stitching individual arguments into a persuasive storyline" — the harness has no governing-thought field, no MECE check, no SCQA requirement.
- **Kellogg (1996)**: formulation, execution, and monitoring share finite working memory; under retrieval load, formulation crowds out monitoring, producing fluent-but-thin text. This explains mechanistically why a one-shot generate-and-word-simultaneously pass produces confident but hollow arguments, and why post-hoc editorial review (checking the same collapsed pass) tends to miss it — it's grading the wrong stage for a defect introduced earlier.

**Additional finding**: earlier, pre-skill writing plans already contain built evidence bases and argument work, done by hand outside the harness. That planning work is currently discarded — the schema has nowhere to store it, so Step 3 re-derives content from raw sources in one pass instead of consuming argument work that already exists.

**Recommended fix, grounded in the above**: insert a third required, gated artifact (`argument-map.json`) between the contract and the draft — Toulmin claim/grounds/warrant per argument unit, one governing thought per section, MECE-checked supporting arguments, and an explicit SCQA opening — reviewable on its own before Step 3 is allowed to run. This extends the same binding-gate discipline the harness already applies to lexicon and density to the one stage currently gated by nothing.

*Signed: Claude Sonnet 5 (claude-sonnet-5), Claude Code — 2026-08-29, writing-process research requested by Boss after reviewing the section-1.1 edit audit.*

---

## 7. Preliminary Architecture of Thai Writing Harness (v6.0 Grounded Proposal)

Based on the synthesis of writing process science (Flower & Hayes, Bereiter & Scardamalia, Toulmin, Minto, Kellogg) and state-of-the-art AI agent workflows (Stanford STORM, ArgLLM, DOC), this section outlines the preliminary architecture for the next evolution of `writing-th`.

### 7.1 Core Paradigm Shift: Decouple Argument Planning from Verbalization

The fundamental failure of v5.0 is forcing an LLM subagent to simultaneously formulate arguments, retrieve facts, invent connective logic (warrants), and draft formal Thai prose in a single pass. Under cognitive overload, the agent defaults to **Knowledge-Telling** (stitching facts without rhetorical tension).

**The v6.0 Mandate**: Treat writing as **Argument Planning first (Rhetorical Space)**, and **Linguistic Verbalization second (Translation Space)**.

```
[ Phase 1: Strategic Scope ]      [ Phase 2: Argument Construction ]      [ Phase 3: Verbalization & Gate ]
   writing-contract.json      ──►         argument-map.json           ──►              draft.md
   (Scope & Boundary Gate)                (Minto SCQA + Toulmin)                  (Isolated Prose Drafting)
                                                   ▲                                      │
                                                   │                                      ▼
                                        [Human Gate / Approval]                 editorial-review.json
                                                                                (Dual Quality Gate)
```

---

### 7.2 The 3-Artifact System

The harness moves from a 2-artifact system (`contract` + `review`) to a **3-artifact pipeline**:

#### Artifact 1: `writing-contract.json` (Scope & Boundary)
- **Job**: Locks the terms of engagement.
- **Fields**: `audience`, `target_altitude`, `section_job`, `inclusions`, `exclusions`, `source_paths`, `reference_samples`.
- **Gate**: Human approval stops scope creep before any work begins.

#### Artifact 2: `argument-map.json` (The Missing Argumentative Blueprint)
- **Job**: Builds the logical and narrative spine before drafting a single Thai sentence.
- **Components**:
  1. **Governing Thought (Minto)**: The single takeaway headline conclusion.
  2. **Narrative Arc (SCQA)**: 
     - **Situation**: Shared baseline reality.
     - **Complication**: Tension/blocker/institutional friction.
     - **Question**: Governing problem statement.
     - **Answer**: Proposed strategic direction.
  3. **Substantive Argument Units (Toulmin Model)**:
     - `unit_id` & `paragraph_job` (`define`, `diagnose`, `compare`, `mandate`)
     - `claim`: Core assertion.
     - `grounds`: Concrete empirical facts, cited benchmarks, or parameters.
     - `warrant`: **The mandatory connective reasoning** answering *"Why do these grounds prove this claim / compel this action?"* (Eliminates the "so what?" void).
     - `application_to_design`: Explicit mapping showing how this finding dictates NCAIF or system architecture (Prevents floating findings).
     - `counter_argument / qualifier`: Boundary conditions or recognized trade-offs.
- **Gate**: **Mandatory Human Sign-off**. The drafting agent cannot be spawned until the human approves the argument map.

#### Artifact 3: `editorial-review.json` (Dual-Layer Quality Receipt)
- **Layer A (Mechanical Lint)**: `lint_thai_writing.py` (Lexicon regex + PyThaiNLP boundary check) + `check_density.py` with both floor and ceiling limits.
- **Layer B (Argumentative Fidelity)**: Checks if the draft faithfully verbalizes the approved `argument-map.json` warrants without reverting to negative-framing crutches (`ไม่ได้...แต่...`) or dropping required mechanisms.

---

### 7.3 The 6-Stage Workflow (v6.0)

| Stage | Name | Description | Gate Type |
|---|---|---|---|
| **0** | **Source Ingestion & Contract** | Ingest existing hand-crafted writing plans (`แผนการเขียน...`) + build `writing-contract.json`. | **Stop Gate (Human)** |
| **1** | **Argument Blueprinting** | Construct `argument-map.json` using Minto SCQA and Toulmin argument units (Claims, Grounds, Warrants, Applications). | None (Agent Work) |
| **2** | **Argument Blueprint Gate** | Human inspects and approves the logical spine. No sentences are drafted until logic is verified. | **Stop Gate (Human)** |
| **3** | **Governed Verbalization** | Subagent translates the approved argument map into idiomatic, active-agency Thai institutional prose in `ψ/incubate/drafts/`. | Isolated Workspace |
| **4** | **Mechanical Gating** | Run `lint_thai_writing.py` and `check_density.py` (with anti-padding ceiling). Exit code 1 = automatic reject. | **Binding Script Gate** |
| **5** | **Independent Editorial Review** | Clean-context reviewer verifies draft against rubric and argument map; produces `editorial-review.json`. | **Binding Review Gate** |
| **6** | **Merge & Hash Lock** | `merge_draft.py` verifies all hashes and merges draft into destination. | **Binding + Stop Gate** |

---

### 7.4 Return Arc: Closing the Promotion Circuit

To prevent repeated human corrections (such as the negative-contrast structure `ไม่ได้...แต่...` occurring across multiple sessions):
1. **Miss Registration**: Human diff markers (`%%...%%`, `~~...~~`) are recorded into `miss_register.db`.
2. **Automated Promotion Trigger**: `register.py ready` flags patterns with $\ge 2$ sightings.
3. **Lexicon Compilation**: Promoted patterns are immediately compiled into `LEXICON_TH.json` as `kind: regex` and validated via `validate_lexicon.py`, ensuring Stage 4 blocks them mechanically in all future runs.

---

*Signed: Antigravity AI (Gemini 3.7 Flash) — 2026-08-29, in response to Boss's directive to formalize the preliminary architecture of Thai writing.*

---

## 8. Proposed Architecture & Artifacts Design (v6.0 Modular Blueprint)

Following the principle of **Separation of Concerns** (Scope Control, Logical Blueprinting, Prose Verbalization, Quality Gating, and Style Memory), this section defines the concrete artifact lifecycle: what is left off, compressed, and redesigned.

### 8.1 Artifact Lifecycle Matrix (v5.0 vs v6.0)

| Artifact | Role in v5.0 | Disposition in v6.0 | Role & Redesign in v6.0 |
|---|---|---|---|
| **`writing-contract.json`** | Mixed: Scope + loose topic checklist | **Redesign (Lean)** | Pure "Terms of Engagement": Audience, Decision Use, Altitude, Allowed Sources, Human Authorization. Argumentation moved out. |
| **`argument-map.json`** | *Non-existent (The Missing Link)* | **NEW (Core Engine)** | Logical & rhetorical blueprint: Minto Governing Thought, SCQA narrative tension, Toulmin argument units (Claim, Grounds, Warrant, Application to Design). |
| **`draft.md`** | Isolated prose from single-pass jump | **Redesign (Verbalization)** | Verbalization of approved argument map into idiomatic, active-agency Thai institutional prose. No argument formulation on the fly. |
| **`editorial-review.json`** | Post-hoc single-pass rubric receipt | **Redesign (Two-Tier)** | Two-tier gate: Tier 1 verifies argument map integrity; Tier 2 verifies prose fidelity to warrants and style rules. |
| **`STYLE_PACK_TH.md`** | 57 KB append-only historical log | **Compress (-70%)** | Active reference pack: Core Kernel (80/20), Anti-AI Shield (Counter-examples), and Diction Map. Historical session logs archived. |
| **`LEXICON_TH.json`** | Mixed: literal, regex, and dead structural prose | **Redesign (Machine-Only)** | Strictly machine-executable rules (`kind: literal` or compiled `kind: regex`). English descriptive prose eliminated. |
| **`miss_register.db`** | Active SQLite database | **Keep & Wire** | Retained as the promotion threshold engine ($\ge 2$ sightings) feeding regex rules into `LEXICON_TH.json`. |
| **`evidence/*.diff-evidence.md`** | Verbose narrative diff essays | **Compress** | Structured audit logs recording raw Before/After diffs and observation IDs. |

---

### 8.2 What is Left Off (Dead Weight Removed)

1. **Argumentative Micro-Fields in `writing-contract.json`**:
   - `required_concepts`, `required_structures`, and `inclusions` treated as a flat bucket are removed. Argument structure belongs in `argument-map.json`, not in the scope contract.
2. **Descriptive English Rules (`kind: structural`) in `LEXICON_TH.json`**:
   - English prose descriptions compiled as regex caused silent no-ops and non-terminating loops. Lexicon is restricted to computable strings and compiling regex. Interpretive evaluation is handled by the Editorial Rubric.
3. **Blanket 4-Pillar Checklist across Every Paragraph**:
   - Forcing Claim, Example, Consequence, and Mechanism onto every paragraph produced artificial claims in introductory and transitional text. The 4-pillar rule is scoped exclusively to `substantive_argument` units in the argument map.

---

### 8.3 What is Compressed (Token Bloat Eliminated)

1. **`STYLE_PACK_TH.md` Compressed from 57 KB to ~12 KB**:
   - **Current Flaw**: Section 9 (Incremental Capture Log) contains 9 historical session retrospectives dating back to June 2026, consuming over 60% of file tokens whenever loaded into agent context.
   - **Resolution**: Move Section 9 history to `ψ/archive/style/capture_history/`. Keep only the active **Core Kernel (80/20)**, **Anti-AI Shield (Good vs Bad pairs)**, and **Diction Map**.
2. **`diff-evidence.md` Files**:
   - Compressed from repetitive linguistic essays into concise, structured diff tables linked to Git commit hashes and `miss_register.db` observation IDs.

---

### 8.4 What is Redesigned (The Modular Engine)

#### A. Core Innovation: `argument-map.json`
Mandatory intermediate blueprint bridging the gap between scope and prose:
```json
{
  "schema_version": "1.0",
  "section_id": "crdb-exec-summary-1.1",
  "governing_thought": "Primary takeaway conclusion answering the governing policy question (Minto Top)",
  "narrative_scqa": {
    "situation": "Shared baseline context and institutional mandate",
    "complication": "Systemic failure, data gap, or operational blocker creating urgency",
    "question": "Governing technical/policy question",
    "answer": "Strategic response and architecture"
  },
  "argument_units": [
    {
      "unit_id": "arg-01",
      "paragraph_job": "diagnose",
      "claim": "Central assertion of this unit",
      "grounds": "Empirical evidence, benchmarks, or cited parameters",
      "warrant": "Connective reasoning explaining why grounds necessitate the claim (Answers 'So what?')",
      "application_to_design": "Explicit mapping showing how this finding dictates system or deliverable design",
      "boundary_qualifier": "Scope limitation or operational caveat"
    }
  ]
}
```

#### B. Lean `writing-contract.json`
Focuses strictly on policy, boundary, and authorization:
- `audience`: Intended decision-maker level (Executive vs Technical).
- `target_altitude`: Reading depth constraint (e.g. 5-minute executive read).
- `input_assets`: Direct ingestion of existing hand-crafted writing plans (`แผนการเขียนบทที่...`).
- `human_signoff`: Mandatory gate before argument mapping commences.

#### C. Two-Tier `editorial-review.json`
- **Tier 1 (Logical Blueprint Audit)**: Evaluates `argument-map.json` before drafting begins (Checks for missing warrants, MECE compliance, and explicit design applications).
- **Tier 2 (Prose Verbalization Audit)**: Evaluates `draft.md` after drafting (Checks warrant preservation, active institutional agency, and absence of negative-framing crutches).

---

### 8.5 Directory Layout (v6.0 Standard)

```text
ψ/incubate/drafts/crdb-exec-summary-1.1/
├── 01_writing-contract.json      # [Redesigned] Lean scope & authorization contract
├── 02_argument-map.json          # [NEW] Logical blueprint (Minto SCQA + Toulmin Units)
├── 03_th_draft.md                # [Clean] Isolated Thai prose verbalized from argument map
└── 04_editorial-review.json      # [Redesigned] Two-tier quality receipt (Logic + Prose)

ψ/memory/style/
├── STYLE_PACK_TH.md              # [Compressed] Active Core Kernel & Anti-AI Shield (~12 KB)
├── LEXICON_TH.json               # [Redesigned] Strictly machine-executable literal/regex rules
├── miss_register.db              # [Database] SQLite tracking threshold (>= 2) for promotions
└── evidence/                     # [Lightweight] Structured diff audit trails
```

---

*Signed: Antigravity AI (Gemini 3.7 Flash) — 2026-08-29, in response to Boss's directive to formalize the proposed architecture design.*

---

## 9. Execution Architecture — see [[2026-08-29_writing-th-v6-build-blueprint]]

§7 and §8 define **what the artifacts are**. They do not say **who runs each
stage, in what context, or what enforces the gates** — and without that, adding
a third artifact genuinely does cost more tokens than v5.0. The full execution
design is in [[2026-08-29_writing-th-v6-build-blueprint]], written as the
build sheet for the next session. Summary of what it adds:

**The argument map is a compression boundary, not just an added file.** Argument
construction needs sources and no style material; verbalization needs the
approved map and a style kernel but not the raw sources. v5.0 loads both halves
into one context. Split as agent boundaries and per-stage load roughly halves,
while the parent holds only paths, verdicts, and hashes.

**Three subagent definitions** in `.claude/agents/` following the
[[wp2-demand-scorer]] pattern — `th-argument-mapper` (strongest model, high
effort; this is where the missing thinking happens), `th-verbalizer`, and
`th-editorial-reviewer`. Never `fork` for the reviewer — it inherits parent
context and destroys the clean-context independence the rubric requires. v5.0's
`assurance: degraded` fallback becomes unreachable in practice.

**Two hooks**, currently the largest unused capability —
`.claude/settings.local.json` configures none. A blocking PreToolUse on `Write`
rejects any draft file whose sibling `argument-map.json` is missing or
unapproved, making "no prose before the logic is approved" a property of the
harness rather than an instruction. A PostToolUse auto-runs
[[lint_thai_writing]]. Prose instructions get skipped under load — that is the
demonstrated cause of the negation-contrast pattern recurring across sessions.
Hooks cannot be skipped.

**A bounded amendment path**, because §7.3 as written is a waterfall that
contradicts the science §6 cites. Stage 3 must be able to halt and propose a map
amendment when a warrant will not carry in prose, rather than deviating silently
or faithfully rendering a bad argument. One loop back to the Stage 2 gate, not
free revision.

**Three schema corrections** carried from §5: keep `kind: structural` (§8.2
inverts the Tranche 1 history — structural was the fix for the non-terminating
loop, not its cause, and removing it dead-ends the return arc for
non-regex-expressible promoted patterns); give `argument_units` ordering and a
`supports` field so MECE is checkable and the storyline is represented rather
than assumed; align `paragraph_job` with [[STYLE_PACK_TH]] rule 6.

**Correction to Stage 0**: a writing plan may or may not exist when the skill is
invoked. Stage 0 asks with `AskUserQuestion` rather than assuming ingestion, and
`writing-contract.json` records `writing_plan: null` when none existed, so a
reviewer can tell whether the argument came from prior planning work or was
built fresh.

Also covered there: deterministic checks pushed into `argument_gate.py` and
`warrant_trace.py`, progressive disclosure splitting `references/` by consumer,
model tiering, plan mode and `AskUserQuestion` as the human-gate surface,
`oracle_thread` for cross-session continuity, and a seven-step build order.

*Signed: Claude Opus 5 (claude-opus-5), Claude Code — 2026-08-29.*
