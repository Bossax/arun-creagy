---
type: trace
traceId: 05dcab3a-271e-44b3-bd5d-a8a5f5d38912
date: 2026-08-29
query: "investigate architecture of writing-th and style-capture: what each skill artifact and step does and what linguistic layer they address"
target: writing-th + style-capture skill system
mode: deep
timestamp: 2026-08-29 12:56
friction_score: 0.7
coverage: oracle, files, git
confidence: high
---

# Trace: writing-th & style-capture — Architecture & Linguistic Layer Map

**Target**: `writing-th` (v5) + `style-capture` skill system  
**Mode**: deep | **Friction**: 0.7 | **Confidence**: high  
**Time**: 2026-08-29 12:56 SEAST  
**Oracle Trace ID**: `05dcab3a-271e-44b3-bd5d-a8a5f5d38912`

---

## Oracle Results
Low-confidence pointer matches only — no direct Oracle memory on this topic. Oracle degraded to FTS5-only (no vector embedder).

## Files Found
- `.agents/skills/writing-th/SKILL.md`
- `.agents/skills/writing-th/references/editorial-rubric.md`
- `.agents/skills/writing-th/references/artifact-schemas.md`
- `.agents/skills/style-capture/SKILL.md`
- `ψ/memory/style/\`style-capture\` skill design.md` (internal design doc, most authoritative)
- `ψ/memory/style/STYLE_PACK_TH.md`
- `ψ/memory/style/LEXICON_TH.json`
- `ψ/memory/style/miss_register.db`
- `ψ/memory/style/evidence/` (7 diff-evidence files, 2026-07-01 to 2026-08-28)

## Git History
- `4737036` — upgrade writing-th v5
- `42fe840` — style-capture skill v1
- `85b4f42` — create writing-th skill and test it :pass
- `03d13e9` — rrr: writing-th-harness-tranche1
- `e85b989` — rrr: writing-th-foresight-style-pack-frustration (evidence of pain with the flat model)

---

## Architecture Analysis: Linguistic Layers & Artifact Mapping

### The Two-Skill System Design Intent
Per `ψ/memory/style/\`style-capture\` skill design.md` (the canonical design document):
> "In the redesigned architecture, `style-capture` is the **learning layer** of a staged writing loop. It should not behave like a flat style collector. It should identify which corrections belong to section architecture, paragraph payload, sentence agency, or lexicon cleanup, then feed those lessons back to the drafting engine."

The system is explicitly divided into **four scales** that map to distinct linguistic layers:

---

## Full Artifact × Step × Linguistic Layer Map

| Artifact / Step | Skill | Linguistic Layer | What It Does |
|---|---|---|---|
| **`writing-contract.json`** | `writing-th` Gate 2 | **L5 Rhetorical / Reader Contract** | Locks: audience, decision use, section job, target altitude, inclusions/exclusions, evidence policy, required concepts. This is the only explicit L5/L6 capture point in either skill. |
| **`editorial-rubric.md`** | `writing-th` Gate 5 | **L4 Logical/Argumentative + L5 Rhetorical** | 8 core dimensions: `section_job`, `audience_decision_value`, `evidence_payload`, `causal_logic`, `reader_facing_appropriateness`, `terminology_agency`, `source_fidelity`, `form_readability`. The exec-summary profile adds: `altitude`, `headline_conclusion`, `findings_over_process`. These are the deepest logical gates in the system. |
| **`editorial-review.json`** | `writing-th` Gate 5 | **L4 + L5** | Receipt of rubric evaluation. Records verdict per dimension. Invalidated on draft change. Enforces the gate is not rubber-stamped. |
| **`lint_thai_writing.py`** | `writing-th` Gate 4 | **L1 Lexical + L2 Surface Syntactic** | Runs LEXICON_TH.json patterns against draft. Detects banned phrases, structural patterns (if `kind: structural`), parenthetical overuse, AI-isms. Mechanical only — cannot detect meaning. |
| **`check_density.py`** | `writing-th` Gate 4 | **L1 + L2** | Compares source vs. draft character ratio (0.8 threshold). Detects over-compression or over-expansion. Purely surface/lexical. |
| **`editorial_gate.py`** | `writing-th` Gate 5 | **L4 + L5** | Prepares and verifies the editorial receipt. Checks SHA-256 hashes of draft and contract — invalidation on change. |
| **`merge_draft.py`** | `writing-th` Gate 6 | **L1–L5 (verification)** | Re-runs mechanical checks and verifies receipt hashes before allowing merge. The final gate. |
| **`STYLE_PACK_TH.md`** | `style-capture` | **L1 + L2 + L3 (some L4 aspiration)** | Cumulative guide. Structured by: Core Kernel, Stage/Scale Activation Map, Diction & Lexicon, Structural DNA, Anti-AI Shield, Implementation Prompt. The design doc specifies 4 scales (see below), but actual SKILL.md implementation is flatter. |
| **`LEXICON_TH.json`** | `style-capture` / `writing-th` | **L1 Lexical only** | Machine-readable banned/preferred term pairs. Fields: `banned`, `preferred`, `reason`, `kind` (literal/regex/structural), `scope`. The `structural` kind aspires to L2 but the 2026-08-05 retrospective notes 3 structural rules silently failed because they were written as English descriptions, not compiling patterns. |
| **`miss_register.db`** | `style-capture` Step 4b | **L1 + L2** | SQLite register. Each pattern observation logged via `register.py observe`. Promotion threshold: 2 sightings. Prevents single-sighting rules from polluting the pack. |
| **`evidence/*.diff-evidence.md`** | `style-capture` Step 3 | **L1 + L2 + emerging L3** | Date-stamped diff logs. Records: Metadata, Concrete Diff Log (word-for-word), Linguistic Shift (grammar/tone), Candidate Rules. This is the raw evidence vault — not synthesized. |
| **`register.py`** | `style-capture` Step 4b | **L1 + L2** | CLI: `observe`, `ready`, `promoted`. Enforces the 2-sighting threshold. Does not reason about why a correction was made — only counts frequency. |
| **`validate_lexicon.py`** | Maintenance | **L1** | Validates JSON schema of LEXICON_TH.json. Catches silent no-ops from structurally malformed entries. |

---

## The 4-Scale Design (per Design Doc) vs. Actual Implementation

The `style-capture` skill design doc defined this 4-scale architecture:

| Scale | Layer Name | Linguistic Layer | Targets |
|---|---|---|---|
| **Scale 1** | Section architecture | **L4 + L5 Logical/Rhetorical** | Section job, argument spine, service-package sequence |
| **Scale 2** | Paragraph payload & structural revision | **L4 Logical/Argumentative** | One paragraph one job, evidence payload, sequence/decomposition clarity |
| **Scale 3** | Sentence agency and voice | **L2 + L3 Surface Syntactic + Micro-Structural** | Subject-first phrasing, active institutional agency, anti-AI phrasing |
| **Scale 4** | Lexicon and consistency cleanup | **L1 Lexical** | Banned phrases, preferred substitutions, technical anchor consistency |

**Key design mandate**: *"A lexical correction must not outrank a section-architecture rule unless repeated evidence proves it is more generative."*

---

## Critical Gap: What the System Actually Captures vs. What It Aspires To

| What the Design Doc Envisions | What the Current SKILL.md + Scripts Actually Implement |
|---|---|
| 4-scale learning (Section → Paragraph → Sentence → Lexicon) | Primarily Scale 3–4. `STYLE_PACK_TH.md` has a Scale/Stage Activation Map section but it's not enforced programmatically |
| `style-capture` assigns each pattern a Scale and Stage | The SKILL.md workflow (Steps 1–8) does this analytically in prose, but `register.py` only counts frequency — it does not tag Scale or Stage |
| Section-architecture rules (L4/L5) should outrank lexical rules | The `writing-contract.json` + `editorial-rubric.md` in `writing-th` hold L4/L5, but `style-capture` has no formal path to feed patterns back into the rubric dimensions |
| Evidence-to-design-decision chain (L4/L5 reasoning) | Not captured. The diff-evidence files log what changed, not why at the logical or epistemic level. |

---

## Friction Analysis

**Score**: 0.7 — Present in files but architecture partially aspirational vs. implemented  
**Coverage**: Oracle (low-confidence), files (high-confidence), git history (confirmed)  
**Goal check**: Answered. The system architecture is clear. The key finding is that `writing-th` holds L4/L5 through the `writing-contract.json` + `editorial-rubric.md` gates, but `style-capture` currently operates primarily at L1–L3 and has no formal pipeline to capture or feed back L4/L5 (logical, argumentative, rhetorical) patterns even though the design doc explicitly envisions it.

---

### Potential Ledger Yields (T-E-D-A Hypothesis)

- **[T] Potential Trigger**: The `style-capture` skill is architecturally designed for L1–L4 capture (4-Scale model), but only L1–L3 is implemented programmatically. L4/L5 reasoning (why edits are made at the logical and rhetorical level) exists only in the `writing-contract.json` and `editorial-rubric.md` — both of which live in `writing-th` and are not fed back into `style-capture`'s learning loop.

- **[E] Supporting Evidence**:  
  - [`style-capture skill design.md`](C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/memory/style/`style-capture` skill design.md) — design intent for 4-scale architecture  
  - [`editorial-rubric.md`](C:/Users/sitth/OracleWorkspace/Arun_Creagy/.agents/skills/writing-th/references/editorial-rubric.md) — L4/L5 dimensions: `evidence_payload`, `causal_logic`, `audience_decision_value`, `headline_conclusion`  
  - [`register.py`](C:/Users/sitth/OracleWorkspace/Arun_Creagy/.agents/skills/writing-th/scripts/register.py) — counts only, does not tag Scale/Stage  
  - `git log` commit `e85b989` — "writing-th-foresight-style-pack-frustration" — historical evidence of pain with the flat model

- **[D] Potential Decision**: If the goal is to capture Boss's L4/L5 logical edits (as in today's `02_th_draft.md` session), a new mechanism is needed — either an extension to `style-capture` that formally captures Scale 1 (Section Architecture) patterns with logical reasoning, or a separate `/logic-capture` or `reasoning-rubric` learning artifact that feeds into `writing-contract.json` templates for future sessions.

- **[A] Target Asset**: [`ψ/memory/style/STYLE_PACK_TH.md`](C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/memory/style/STYLE_PACK_TH.md) + the `style-capture` SKILL.md itself.
