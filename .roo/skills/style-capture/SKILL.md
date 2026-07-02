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
    - `In-Place (Git Diff)`: A single file path representing an in-place edit where the user modified the file directly in the workspace. The agent will compare the current dirty workspace copy against the latest committed version.
    - `Refinement (Two-File)`: A pair of file paths (Draft vs. Edited) representing separate versions.
3) **Paths**:
    - For `Sample`: `sample_path`.
    - For `In-Place (Git Diff)`: `file_path`.
    - For `Refinement`: `draft_path` and `edited_path`.
4) (Optional) **Focus**: Specific stylistic area to focus on (e.g., "Hedging," "Paragraph transitions").

---

## Workflow

1) **Initialization & Context Loading**
    - Check for existing artifacts in `ψ/memory/style/`:
        - `STYLE_PACK_<CONTEXT>.md`
        - `LEXICON_<CONTEXT>.json`
    - If they do not exist, initialize them using the "Cold Start" template.

2) **Reading & Pre-processing**
    - If `Sample` mode: Read the file.
    - If `In-Place (Git Diff)` mode: Run `git diff <file_path>` to extract the uncommitted changes. Analyze the deleted lines (acting as the draft) and the added lines (acting as the edits).
    - If `Refinement (Two-File)` mode: Read both files and perform a semantic comparison to identify specifically **what the human changed** (Word choice, re-ordering, tone shifts).

3) **Intermediate Evidence Materialization (Diff Log)**
    - If `In-Place (Git Diff)` or `Refinement` mode: Save a date-stamped diff evidence file to `ψ/memory/style/evidence/<YYYY-MM-DD>_<HH-MM>_<CONTEXT>_diff-evidence.md`.
    - This file records the specific delta of this run, preserving the project history for future statistical aggregation.
    - The file must document:
        - **Metadata**: Timestamp, session ID, source mode (In-Place Git Diff or Two-File Refinement), file paths, and context.
        - **Concrete Diff Log**: Direct word-for-word or phrase-for-phrase changes.
        - **Linguistic Shift**: Specific grammar, tone, or structural changes observed.
        - **Candidate Rules**: A list of suggested style rules hypothesized from this comparison.
    - Separate evidence logs enable bulk analysis later, making it possible to trace recurring correction patterns and verify their statistical significance before cementing them into the master `STYLE_PACK`.

4) **Pattern Extraction (Research Phase)**
    - Analyze the input for:
        - **Structural DNA**: How are sections introduced? How is evidence linked to claims?
        - **Linguistic Markers**: Sentence length, active/passive preference, use of connectors.
        - **The Anti-AI Shield**: Identify phrases or structures that were removed/replaced (Counter-examples).
        - **Lexicon**: Map specific terms to their preferred alternatives.

5) **Cumulative Merging (Update Phase)**
    - **Merge Strategy**:
        - Append new **Examples** and **Counter-examples** to the `STYLE_PACK`.
        - If a new pattern contradicts an existing rule, prioritize the new evidence as "Style Evolution" but keep a note of the change.
        - **Rank Order**: Re-evaluate the hierarchy. Rules appearing in multiple samples move to "Highest Priority."
    - Update the `LEXICON_<CONTEXT>.json` with new term pairings.

6) **Artifact Materialization**
    - Write/Update the `STYLE_PACK_<CONTEXT>.md`.
    - Format:
        - `## 1. Ranked Style Rules`
        - `## 2. Structural DNA`
        - `## 3. Lexicon & Diction (Dos/Don'ts Table)`
        - `## 4. Anti-AI Shield (Counter-examples)`
        - `## 5. Master Implementation Prompt`

7) **Master Prompt Synthesis**
    - Generate a concise, high-signal prompt that can be pasted into a new session to "activate" this style. It should include the Top 5 rules and a few critical Dos/Don'ts.

8) **oracle_learn Integration**
    - Call `oracle_learn` to index the new patterns.
    - Concepts: `writing-style`, `<CONTEXT>`, `style-capture`.
    - Pattern: A summary of the latest delta (e.g., "Added rule for formal Thai hedging using 'อาจพิจารณาได้ว่า'").

---

## Output Template: `STYLE_PACK_<CONTEXT>.md`

```markdown
# Style-Pack: [Context]
**Samples Learnt**: [N] | **Last Updated**: [Date]

## 1. Ranked Style Rules
1. [Rule] - [Example]
2. ...

## 2. Lexicon & Diction
| Banned/Common | Preferred | Reason |
| :--- | :--- | :--- |

## 3. Anti-AI Shield
- **DON'T**: [AI-sounding phrase]
- **DO**: [Human-sounding alternative]

## 4. Master Implementation Prompt
[Concise instructions for future sessions]
```
