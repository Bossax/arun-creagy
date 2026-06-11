---
name: style-capture
description: Incrementally learns and refines writing styles from individual samples or draft/edit pairs. Maintains a persistent cumulative Style-Pack in project-local memory artifacts.
---

# /style-capture

> A cumulative learning engine for writing style mimicry. It extracts linguistic patterns, structural DNA, and lexicon preferences from single samples or draft-vs-edited comparisons, merging them into a persistent context-specific **Style-Pack**.

## When to use this skill

- When you have a **single gold-standard sample** and want to start a new style context.
- When you have a **draft vs. edited pair** and want to capture corrective patterns: what to fix, avoid, or preserve.
- When you want to **incrementally improve** an existing style guide as more examples become available.
- When you want to generate a **Master Implementation Prompt** for a specific writing style.

## When NOT to use this skill

- For general project retrospectives (use `/rrr`).
- For simple file editing without stylistic extraction goals.
- For learning technical facts or code patterns (use the dedicated learning workflow instead of style capture).

## Inputs required

1. **Context**: For example, `Thai-Institutional`, `Tech-Blog`, or `Executive-Summary`. This determines which `Style-Pack` to update.
2. **Source type**:
   - `Sample`: a single file path representing the target style.
   - `Refinement`: a pair of file paths (`draft_path` and `edited_path`) representing an improvement.
3. **Paths**:
   - For `Sample`: `sample_path`.
   - For `Refinement`: `draft_path` and `edited_path`.
4. **Optional focus**: Specific stylistic area to focus on, such as hedging or paragraph transitions.

---

## Roo destination and artifact convention

- Primary skill home: [` .roo/skills/style-capture/SKILL.md`](.roo/skills/style-capture/SKILL.md)
- Style-Pack artifacts: prefer a project-local markdown ledger under `plans/` for session-scoped work, or `ψ/memory/` when the style needs to persist beyond one project.
- Lexicon artifacts: store alongside the Style-Pack as a companion JSON or markdown table when needed.
- Keep artifacts append-only where practical; do not overwrite prior evidence unless a new version is explicitly intended.

---

## Workflow

1. **Initialization and context loading**
   - Check for existing artifacts for the current context, such as:
     - `STYLE_PACK_<CONTEXT>.md`
     - `LEXICON_<CONTEXT>.json`
   - If they do not exist, initialize them from a cold-start template.

2. **Reading and pre-processing**
   - Read the input file(s).
   - If in refinement mode, compare draft vs. edited and identify specifically what changed: wording, ordering, tone, compression, or emphasis.

3. **Pattern extraction**
   - Analyze the input for:
     - **Structural DNA**: how sections are introduced and how evidence links to claims.
     - **Linguistic markers**: sentence length, active/passive preference, connective usage.
     - **Anti-AI shield**: phrases or structures removed or replaced.
     - **Lexicon**: preferred terms and rejected alternatives.

4. **Cumulative merging**
   - Append new examples and counter-examples to the Style-Pack.
   - If a new pattern contradicts an existing rule, treat it as style evolution and keep a note of the change.
   - Re-rank rules when a pattern appears in multiple samples.
   - Update the lexicon artifact with new term pairings.

5. **Artifact materialization**
   - Write or update `STYLE_PACK_<CONTEXT>.md`.
   - Use these sections:
     - `## 1. Ranked Style Rules`
     - `## 2. Structural DNA`
     - `## 3. Lexicon & Diction (Dos/Don'ts Table)`
     - `## 4. Anti-AI Shield (Counter-examples)`
     - `## 5. Master Implementation Prompt`

6. **Master prompt synthesis**
   - Generate a concise, high-signal prompt that can be pasted into a new session to activate the style.
   - Include the top rules plus a few critical dos and don'ts.

7. **Learning handoff alignment**
   - When a draft/edited pair is available, align the captured delta with the companion learning workflow used by [`writing-th-learn`](.roo/skills/writing-th-learn/SKILL.md).
   - Keep the style-capture output compatible with the Thai writing workflow in [`writing-th`](.roo/skills/writing-th/SKILL.md) when the context is Thai-first or report/article oriented.

---

## Output template: `STYLE_PACK_<CONTEXT>.md`

```markdown
# Style-Pack: [Context]
**Samples Learned**: [N] | **Last Updated**: [Date]

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

---

## Roo compatibility notes

- Prefer local file paths and repository artifacts over any runtime-only or hosted-state assumptions.
- Keep the skill usable outside Thai-first workflows, while still allowing direct reuse of the writing-th ecosystem where it fits.
- Preserve the learning loop: sample, refine, merge, and synthesize.
