---
name: style-capture
description: Incrementally learns and refines writing styles from individual samples or draft/edit pairs. Maintains a persistent cumulative "Style-Pack" in project memory.
---

# /style-capture

> A cumulative learning engine for writing style mimicry. It extracts linguistic patterns, structural DNA, and lexicon preferences from single samples or "Draft vs. Edited" comparisons, merging them into a persistent context-specific **Style-Pack**.

## When to use this skill

- When you have a **single gold-standard sample** and want to start a new style context.
- When you have a **Draft vs. Edited pair** and want to capture "Corrective Patterns" (what to fix/avoid).
- When you want to **incrementally improve** an existing style guide as more examples become available.
- When you want to generate a **Master Implementation Prompt** for a specific writing style.

## When NOT to use this skill

- For general project retrospectives (use `/rrr`).
- For simple file editing without stylistic extraction goals.
- For learning technical facts or code patterns (use `oracle_learn` directly).

## Inputs required

1) **Context**: (e.g., `Thai-Institutional`, `Tech-Blog`, `Executive-Summary`). This determines which `Style-Pack` to update.
2) **Source Type**:
    - `Sample`: A single file path representing the target style.
    - `In-Place / Single File (Smart Diff Resolver)`: A single file path representing an edit. The agent automatically resolves the diff using the fallback ladder: working copy `git diff` → latest commit history (`git log -p -1` / `HEAD~1..HEAD`) → sibling baseline (`.pre-*.md`, `.draft.md`).
    - `Refinement (Two-File)`: An explicit pair of file paths (Draft vs. Edited) representing separate versions.
3) **Paths**:
    - For `Sample`: `sample_path`.
    - For `In-Place / Single File`: `file_path`.
    - For `Refinement`: `draft_path` and `edited_path`.
4) (Optional) **Focus**: Specific stylistic area to focus on (e.g., "Hedging," "Paragraph transitions").

---

## Workflow

1) **Initialization & Context Loading**
    - Check for existing artifacts in `ψ/memory/style/`:
        - `STYLE_PACK_<CONTEXT>.md`
        - `LEXICON_<CONTEXT>.json`
        - `STRUCTURAL_RULES_<CONTEXT>.json`
    - If they do not exist, initialize them using the "Cold Start" template.

2) **Reading & Pre-processing (Smart Diff Resolver)**
    - If `Sample` mode: Read the file.
    - If `In-Place / Single File` mode: Resolve the edit delta using this strict resolution ladder:
        1. **Working Copy**: Run `git diff <file_path>`. If non-empty, use deleted lines as draft and added lines as human edits.
        2. **Committed Revision**: If working copy diff is empty, inspect Git commit history: run `git log -p -1 <file_path>` or `git diff HEAD~1..HEAD -- <file_path>`. If changes were committed, extract the delta from that commit.
        3. **Sibling Baseline**: If git history shows no recent edit, search the sibling directory for baseline files (e.g. `*.pre-*.md`, `*.draft.md`, `02_th_draft.pre-1.1-revision.md`). If found, run `git diff --no-index <sibling_baseline> <file_path>`.
        4. **CRITICAL GUARD**: NEVER switch or wander off to an unrelated dirty file in `git status`. If no diff is found on the requested file across steps 1–3, halt and explicitly ask the user for the commit hash or baseline comparison path.
    - If `Refinement (Two-File)` mode: Read both files and perform a semantic comparison to identify specifically **what the human changed** (Word choice, re-ordering, tone shifts, structural restructuring).

3) **Intermediate Evidence Materialization (Diff Log)**
    - If `In-Place / Single File` or `Refinement` mode: Save a date-stamped diff evidence file to `ψ/memory/style/evidence/<YYYY-MM-DD>_<HH-MM>_<CONTEXT>_diff-evidence.md`.
    - This file records the specific delta of this run, preserving the project history for future statistical aggregation.
    - The file must document:
        - **Metadata**: Timestamp, session ID, source mode (In-Place Single File or Two-File Refinement), file paths, and context.
        - **Concrete Diff Log**: Direct line-by-line word-for-word changes, formatting transformations, and annotations (`%%...%%`).
        - **Linguistic Shift**: Specific grammar, tone, or structural changes observed.
        - **Candidate Rules**: Categorized by layer (`lexical`, `regex`, or `structural`).

4) **Pattern Extraction (Research Phase)**
    - Analyze the input across 3 layers:
        - **L1/L2 Lexical & Surface Regex**: Specific term replacements and negative-contrast scaffolding.
        - **L3 Micro-Structural / Tone**: Diction cleanup, Anti-AI Shield counter-examples.
        - **L4/L5 Structural & Rhetorical**: Document architecture, high-altitude tables, framework enumeration, finding-to-design bridges.

4b) **Miss Register (Promotion Threshold)**
    - A single correction is a local edit. The same correction twice is a rule -- learning 2026-06-27 fixed that threshold at two, and the register is what counts to it.
    - For every candidate pattern found in step 4 that is **not already in the lexicon or structural rules**, record it:
      `python .agents/skills/writing-th/scripts/register.py observe "<pattern>" --source <file> --layer <lexical|regex|structural> --fix "<what you changed it to>"`
    - Then ask what has earned promotion:
      `python .agents/skills/writing-th/scripts/register.py ready [--layer <lexical|regex|structural>]`
    - Only patterns listed by `ready` should be promoted in step 5. A pattern seen once stays in the register and waits.
    - After writing a pattern into the pack, lexicon, or structural rules, close it out:
      `python .agents/skills/writing-th/scripts/register.py promoted "<pattern>" --layer <lexical|regex|structural>`
    - Nothing is deleted. A promoted pattern keeps its full observation history; it simply stops appearing in `ready`.

5) **Cumulative Merging (Update Phase)**
    - **Merge Strategy by Layer**:
        - **L1/L2 (Lexical & Regex)**: Update `LEXICON_<CONTEXT>.json`. Every entry needs `banned`, `preferred`, `reason`, `kind`, `scope`, and `pattern` (for regex). After write, run:
          `python .agents/skills/writing-th/scripts/validate_lexicon.py ψ/memory/style/LEXICON_TH.json`
        - **L4/L5 (Structural Rules)**: Update `STRUCTURAL_RULES_<CONTEXT>.json`. Every entry needs `id`, `name`, `scope`, `section_job`, `trigger_condition`, `mandatory_structure`, `counter_pattern`, and `status: "promoted"`. After write, run:
          `python .agents/skills/writing-th/scripts/validate_structural_rules.py ψ/memory/style/STRUCTURAL_RULES_TH.json`
        - **L3 (Anti-AI Shield)**: Append new **Examples** and **Counter-examples** to `STYLE_PACK_<CONTEXT>.md §7`.
6) **Artifact Materialization**
    - Write/Update the `STYLE_PACK_<CONTEXT>.md`.
    - Format (as of the 2026-08-29 v6.0 harness overhaul — `STYLE_PACK_TH.md`
      is the live example):
        - `## 1. Core Kernel (80/20)`
        - `## 2. Stage / Scale Activation Map`
        - `## 3. Secondary Pass Rules`
        - `## 4. Hierarchical Vetting Stack`
        - `## 5. Lexicon & Diction (Dos/Don'ts Table)`
        - `## 6. Structural DNA`
        - `## 7. Anti-AI Shield (Counter-examples)`
        - `## 8. Master Implementation Prompt`
        - `## 9. Incremental Capture Log` — **archived, not active**. This
          section grows unbounded and must never be loaded into a drafting or
          review model's context. Append new capture entries directly to
          `ψ/archive/style/capture_history/STYLE_PACK_TH_incremental-capture-log.md`,
          not to `STYLE_PACK_TH.md` itself; leave the short pointer note in
          §9 of the live pack undisturbed. Give every new entry its own
          heading level below `##` so a capture entry can never again collide
          with a real numbered section (this is what produced the stray
          duplicate `## 5.` heading fixed on 2026-08-29).
        - Sections 1–8 are what Stage 3 of `writing-th` v6.0 actually needs,
          and only a compressed extract of them —
          `.agents/skills/writing-th/references/prose-kernel.md` — is loaded
          during drafting. Do not assume a drafting agent has read this file.

7) **Master Prompt Synthesis**
    - Generate a concise, high-signal prompt that can be pasted into a new session to "activate" this style. It should include the Top 5 rules and a few critical Dos/Don'ts.

8) **oracle_learn Integration**
    - Call `oracle_learn` to index the new patterns.
    - Concepts: `writing-style`, `<CONTEXT>`, `style-capture`.
    - Pattern: A summary of the latest delta (e.g., "Added rule for formal Thai hedging using 'อาจพิจารณาได้ว่า'").

---

## Output Template: `STYLE_PACK_<CONTEXT>.md`

Follow the actual 9-section structure listed under step 6 above — this
template shows only the shape of the two sections a promotion round usually
touches, not the whole file:

```markdown
# Style-Pack: [Context]
**Samples Learnt**: [N] | **Last Updated**: [Date] | **Lexicon**: LEXICON_[CONTEXT].json v[X], [N] rules

## 5. Lexicon & Diction
| Banned/Common | Preferred | Reason |
| :--- | :--- | :--- |

## 7. Anti-AI Shield
- **DON'T**: [AI-sounding phrase]
- **DO**: [Human-sounding alternative]
```

A new capture entry belongs in the archived capture-history file (see step 6),
never appended to `## 9` of the live pack itself.
