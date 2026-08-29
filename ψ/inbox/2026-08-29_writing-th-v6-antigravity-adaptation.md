---
date: 2026-08-29
type: blueprint
topic: writing-th-v6-antigravity-adaptation
status: ready-to-build
target: writing-th v6.0 on Google Antigravity (AGY)
companions:
  - "[[2026-08-29_writing-harness-skill-architecture-analysis]]"
  - "[[2026-08-29_writing-th-v6-build-blueprint]]"
author: Antigravity AI (Gemini 3.7 Flash)
---

# Blueprint: writing-th v6.0 Execution Architecture — Antigravity Adaptation

This document is the **Google Antigravity (AGY) implementation blueprint** translating the execution architecture defined in [[2026-08-29_writing-th-v6-build-blueprint]] and the theoretical foundations in [[2026-08-29_writing-harness-skill-architecture-analysis]] (§6–§8) into production reality within the Antigravity runtime.

---

## 1. Executive Summary: What Stays vs. What Adapts

The core architectural breakthroughs of v6.0 remain identical:
1. **The 3-Artifact System**: `writing-contract.json` (Scope) → `argument-map.json` (Logic Blueprint) → `editorial-review.json` (Quality Receipt).
2. **Argument Map as a Compression Boundary**: Decoupling argument construction (sources loaded, no style loaded) from prose verbalization (map + prose kernel loaded, no sources loaded).
3. **Non-Bypassable Lifecycle Hooks**: Rejecting unapproved drafting via system constraints rather than easily skipped prompt instructions.
4. **Clean Independent Review**: Eliminating degraded self-reviews by invoking clean-context subagents.

What adapts is **the runtime machinery**: translating Claude Code specific files (`.claude/settings.local.json`, `.claude/agents/*.md`, `ExitPlanMode`) into native Antigravity primitives (`.agents/hooks.json`, `invoke_subagent`, `ask_question`, and Antigravity Markdown Artifacts).

---

## 2. The 5 Antigravity Core Adaptations

### Adaptation 1: Lifecycle Hooks (`.agents/hooks.json`)
Antigravity provides full lifecycle hook support via `.agents/hooks.json`. Commands run synchronously via `cmd /c` (Windows) receiving JSON on `stdin` and outputting JSON on `stdout`.

```json
{
  "writing-th-guard": {
    "PreToolUse": [
      {
        "matcher": "write_to_file|replace_file_content",
        "hooks": [
          {
            "type": "command",
            "command": "python .agents/skills/writing-th/scripts/check_draft_preconditions.py",
            "timeout": 15
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "write_to_file|replace_file_content",
        "hooks": [
          {
            "type": "command",
            "command": "python .agents/skills/writing-th/scripts/lint_thai_writing.py",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

* **Hook 1 (PreToolUse - Blocking Gate)**:
  - Intercepts calls to `write_to_file` and `replace_file_content`.
  - Checks if the target path matches `ψ/incubate/drafts/**/*draft*.md`.
  - If `argument-map.json` is missing or `approval.status != "approved"`, it emits:
    ```json
    {
      "decision": "deny",
      "reason": "CRITICAL GATE FAILURE: Cannot draft Thai prose before argument-map.json is approved by human sign-off!"
    }
    ```
* **Hook 2 (PostToolUse - Automated Linter)**:
  - Runs automatically on any draft edit, injecting linter findings directly as environment feedback without consuming model memory on deciding when to lint.

---

### Adaptation 2: Subagent Orchestration via Antigravity API
In Antigravity, subagents are spawned with isolated context and distinct model tiers using `invoke_subagent`:

| Stage | Subagent Role | Model Tier in Antigravity | Context Ingestion | Prohibited Ingestion |
|---|---|---|---|---|
| **Stage 1** | `TH Argument Mapper` | `Model: "pro"` (High reasoning) | Raw sources, writing plan, `references/argument-schema.md` | `STYLE_PACK_TH.md`, `LEXICON_TH.json`, rubric |
| **Stage 3** | `TH Verbalizer` | `Model: "flash"` (Fast, strong Thai idiom) | Approved `argument-map.json`, `references/prose-kernel.md` | Raw sources, full style pack, rubric |
| **Stage 5** | `TH Editorial Reviewer` | `Model: "pro"` (Independent context) | `draft.md`, `argument-map.json`, `references/editorial-rubric.md` | Raw sources, style pack, parent history |

*Antigravity automatically provides fresh conversation threads for invoked subagents, guaranteeing 100% clean-context review without "fork" contamination.*

---

### Adaptation 3: Human Gate Surface (`ask_question` + Artifacts)
Claude Code’s `ExitPlanMode` is replaced with Antigravity’s native UI capabilities:
1. **Interactive Plan Presentation**: The parent agent renders the Minto Governing Thought, SCQA narrative tension, and Toulmin units as a formatted Markdown Artifact in the right-hand panel.
2. **Interactive Decision Gate**: The parent calls `ask_question`:
   - `question`: "Do you approve the argument map for [Section Name]?"
   - `options`:
     - "(Recommended) Approve argument map — proceed to Stage 3 verbalization"
     - "Amend argument map — request structural revision of warrants"
     - "Reject argument map — restart Stage 1 with new perspective"

---

### Adaptation 4: Token & Context Optimization
1. **Archive Section 9**: Move `STYLE_PACK_TH.md` Section 9 (35.8 KB of historical narrative logs) to `ψ/archive/style/capture_history/`. The active pack shrinks from 57 KB to ~12 KB.
2. **Extract `references/prose-kernel.md` (~5 KB)**: Stage 3 loads only the Core Kernel (80/20) and Anti-AI Shield.
3. **Lexicon Isolation**: `LEXICON_TH.json` is consumed solely by CLI tools (`lint_thai_writing.py`), never entering LLM context.

---

### Adaptation 5: Deterministic Python Scripts (Windows & Cross-Platform)
All scripts in `.agents/skills/writing-th/scripts/` run natively in Windows (`pwsh` / `cmd /c`):
- `argument_gate.py prepare <contract>`: Emits skeleton map.
- `argument_gate.py validate <map>`: Mechanical MECE, warrant, and enum check (exit code 1 blocks).
- `check_draft_preconditions.py`: Hook script inspecting stdin JSON payload.

---

## 3. Seven-Step Build Order for Antigravity

1. **Step 1 — Create Precondition Script & Hook**: Build `check_draft_preconditions.py` and register in `.agents/hooks.json`.
2. **Step 2 — Implement `argument_gate.py`**: Build `prepare` and `validate` commands with strict schema checks.
3. **Step 3 — Archive Style History & Extract Prose Kernel**: Move `STYLE_PACK_TH.md` §9 to archive; extract `references/prose-kernel.md`.
4. **Step 4 — Wire Subagent Prompts into `writing-th/SKILL.md`**: Update SKILL.md with Antigravity `invoke_subagent` specifications and Stage 0 `ask_question` writing-plan check.
5. **Step 5 — Add Bounded Amendment Path (Stage 3 -> Stage 2)**: Allow verbalizer to emit amendment proposals instead of silent deviation.
6. **Step 6 — Promote Negation-Contrast Regex to `LEXICON_TH.json`**: Add compiling regex for `ไม่ได้...แต่...` and validate via `validate_lexicon.py`.
7. **Step 7 — Execute Blind Test**: Test end-to-end on a pilot chapter section in `ψ/incubate/drafts/`.

---

*Signed: Antigravity AI (Gemini 3.7 Flash) — 2026-08-29, Antigravity Adaptation Blueprint.*
