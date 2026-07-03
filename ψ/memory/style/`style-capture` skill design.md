# Skill Design: `style-capture` (Incremental Style Learning)

## Objective
To capture and refine a specific writing style (e.g., Thai Institutional Narrative) through incremental examples and feedback loops, maintaining a persistent "Style-Pack" that grows in fidelity over time.

In the redesigned architecture, `style-capture` is the **learning layer** of a staged writing loop. It should not behave like a flat style collector. It should identify which corrections belong to section architecture, paragraph payload, sentence agency, or lexicon cleanup, then feed those lessons back to the drafting engine.

## Internal Utility Artifacts
The skill manages a persistent folder at `ψ/memory/style/` containing:
1.  **`STYLE_PACK_<CONTEXT>.md`**: The master cumulative guide, but organized by **stage / scale** rather than one flat rule list.
2.  **`LEXICON_DATABASE.json`**: A structured list of preferred terms, banned "AI-isms", and context-specific substitutions. This file should stay narrow and serve late-pass cleanup.
3.  **`EVIDENCE_VAULT/`**: A folder containing raw snippets or diffs that justify specific rules (for traceability).

## Stage-aware architecture

The writing system should be divided into four scales:

1. **Scale 1 — Section architecture**
   - section job
   - argument spine
   - service-package sequence

2. **Scale 2 — Paragraph payload and structural revision**
   - one paragraph one job
   - evidence payload
   - sequence / decomposition / adoption-test clarity

3. **Scale 3 — Sentence agency and voice**
   - subject-first phrasing
   - active institutional agency
   - anti-translation cleanup
   - anti-AI phrasing

4. **Scale 4 — Lexicon and consistency cleanup**
   - banned phrases
   - preferred substitutions
   - shorthand normalization
   - technical anchor consistency

`writing-th` should activate these scales by stage. `style-capture` should learn new rules into the correct scale, not flatten them.

---

## Command: `/style-capture`

### Inputs
*   **Source**: A single file path (new writing sample) OR a pair of paths (Draft vs. Edited).
*   **Context**: (e.g., `NCAIF-Institutional`, `Technical-Spec`).
*   **Learning Goal**: (e.g., "Refine hedging," "Fix word choice").

### Workflow (Incremental Loop)

1.  **Context Loading (Research Phase)**
    *   Find the existing `STYLE_PACK` for the given context.
    *   If none exists, initialize a new one using the "Cold Start" template.

2.  **Pattern Extraction (Analyze Phase)**
    *   If **Sample only**: Analyze the text for Sentence Structure, Vocabulary, and Tone. Extract "Positive Patterns."
    *   If **Draft vs. Edited**: Identify exactly what the human changed. Extract "Corrective Patterns" (Anti-AI rules).
    *   For every extracted pattern, assign:
        1.  **Scale**: Section / Paragraph / Sentence / Lexicon
        2.  **Stage**: Outline / First Draft / Structural Revision / Voice Revision / Cleanup
        3.  **Priority**: Core Kernel / Secondary Pass / Reference Only

3.  **Cumulative Merging (Update Phase)**
    *   Compare new patterns against the current `STYLE_PACK`.
    *   **Conflict Resolution**: If a new sample contradicts an old rule, flag it for the user or prioritize the latest input as "Evolution."
    *   **Ranking Update**: Re-evaluate the "Rank Order" of rules based on frequency of appearance.
    *   **Scale Discipline**: A lexical correction must not outrank a section-architecture rule unless repeated evidence proves it is more generative.

4.  **Artifact Materialization (Write Phase)**
    *   Update the `STYLE_PACK.md` with new **Examples** and **Counter-examples**.
    *   Update the `LEXICON_DATABASE.json` with new term pairings.
    *   Preserve an 80/20 distinction between:
        - **Core Kernel**: small set of highly generative rules
        - **Secondary Pass**: useful but stage-limited rules
        - **Reference Layer**: examples, banned phrases, edge cases

5.  **Master Instruction Generation**
    *   Synthesize a concise "Implementation Prompt" that can be used by the agent in future writing tasks (Dual Curation Methodology).

---

## Cumulative State Structure (The "Style-Pack")

```markdown
# Style-Pack: [Context Name]
**Status**: Incremental (n=Samples) | **Last Updated**: YYYY-MM-DD

## 1. Core Kernel (80/20)
1. [Highest Priority Rule] - Why: [Evidence Link]
2. [Secondary Rule] ...

## 2. Stage / Scale Activation Map
- Stage A / Scale 1 — Section architecture:
- Stage B / Scale 2 — First-draft content build:
- Stage C / Scale 2 — Structural revision:
- Stage D / Scale 3 — Sentence agency and voice:
- Stage E / Scale 4 — Lexicon and cleanup:

## 3. The Diction & Lexicon (Dos/Don'ts)
| Target Term | Preferred Substitution | Reason/Tone |
| :--- | :--- | :--- |
| "Data Hunt" | "การสืบค้นข้อมูลเชิงลึก" | Avoid consultant jargon |

## 4. Structural DNA
- Paragraph Flow: [e.g., Lead with Institutional Necessity]
- Hedging Style: [e.g., Use "อาจจะ" with specific evidence]

## 5. Anti-AI Shield (Counter-examples)
- **BAD**: "ในฐานะที่เป็นเครื่องมือที่สำคัญ..." (Tautology)
- **GOOD**: "ทำหน้าที่เป็นรากฐานในการ..." (Functional)

## 6. Dual Curation Protocol (The Implementation Prompt)
[A copy-pasteable prompt for the agent to start next tasks]
```
