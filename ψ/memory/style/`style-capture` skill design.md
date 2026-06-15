# Skill Design: `style-capture` (Incremental Style Learning)

## Objective
To capture and refine a specific writing style (e.g., Thai Institutional Narrative) through incremental examples and feedback loops, maintaining a persistent "Style-Pack" that grows in fidelity over time.

## Internal Utility Artifacts
The skill manages a persistent folder at `ψ/memory/style/` containing:
1.  **`STYLE_PACK_<CONTEXT>.md`**: The master cumulative guide (Ranked Rules + Dos/Don'ts).
2.  **`LEXICON_DATABASE.json`**: A structured list of preferred terms, banned "AI-isms", and context-specific substitutions.
3.  **`EVIDENCE_VAULT/`**: A folder containing raw snippets or diffs that justify specific rules (for traceability).

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

3.  **Cumulative Merging (Update Phase)**
    *   Compare new patterns against the current `STYLE_PACK`.
    *   **Conflict Resolution**: If a new sample contradicts an old rule, flag it for the user or prioritize the latest input as "Evolution."
    *   **Ranking Update**: Re-evaluate the "Rank Order" of rules based on frequency of appearance.

4.  **Artifact Materialization (Write Phase)**
    *   Update the `STYLE_PACK.md` with new **Examples** and **Counter-examples**.
    *   Update the `LEXICON_DATABASE.json` with new term pairings.

5.  **Master Instruction Generation**
    *   Synthesize a concise "Implementation Prompt" that can be used by the agent in future writing tasks (Dual Curation Methodology).

---

## Cumulative State Structure (The "Style-Pack")

```markdown
# Style-Pack: [Context Name]
**Status**: Incremental (n=Samples) | **Last Updated**: YYYY-MM-DD

## 1. Fundamental Hierarchy (Ranked)
1. [Highest Priority Rule] - Why: [Evidence Link]
2. [Secondary Rule] ...

## 2. The Diction & Lexicon (Dos/Don'ts)
| Target Term | Preferred Substitution | Reason/Tone |
| :--- | :--- | :--- |
| "Data Hunt" | "การสืบค้นข้อมูลเชิงลึก" | Avoid consultant jargon |

## 3. Structural DNA
- Paragraph Flow: [e.g., Lead with Institutional Necessity]
- Hedging Style: [e.g., Use "อาจจะ" with specific evidence]

## 4. Anti-AI Shield (Counter-examples)
- **BAD**: "ในฐานะที่เป็นเครื่องมือที่สำคัญ..." (Tautology)
- **GOOD**: "ทำหน้าที่เป็นรากฐานในการ..." (Functional)

## 5. Dual Curation Protocol (The Implementation Prompt)
[A copy-pasteable prompt for the agent to start next tasks]
```
