# SOP: NCAIF Executive Summary Generation (Chapters 5.2 & 5.3)

## 1. Output Deliverables
The execution pipeline will produce exactly **3 distinct documents** to ensure technical depth hierarchy and prevent lossy compression:
1.  **Chapter 5.2 Executive Summary**: Focused on the Platform Architecture & Governance Engine.
2.  **Chapter 5.3 Executive Summary**: Focused on Strategic Impact, Services, Gaps, and the Roadmap.
3.  **The Report-Level Executive Summary (4-5 Pages)**: The overarching narrative synthesized *exclusively* from the locked 5.2 and 5.3 summaries.

## 2. Strategic Framing & Narrative Logic
*   **The 5.2 Frame (The Engine):** Chapter 5.2 provides the required governance standards, architectural artifacts (CDM, Glossary), and role assignments necessary to build and keep the platform running.
*   **The 5.3 Frame (The Impact):** Chapter 5.3 focuses on the strategic, long-term development of climate information products and services, bridging architecture to institutional value.

**Narrative Sequence for the Final Synthesis:**
*   **Part 1: The Baseline Reality**: Global standards vs. current data landscape (5.2.1, 5.2.2, 5.3.1, 5.3.2, 5.3.11).
*   **Part 2: Platform Architecture & Governance**: Final design (5.2.9) and governance components (CDM, Glossary, Roles from 5.2.3, 5.2.5, 5.2.7).
*   **Part 3: Strategic Services & Models**: 8 Key Services (5.3.3) and the Loss & Damage logical data model (5.3.6, 5.3.7).
*   **Part 4: The Roadmap**: Institutional gaps (5.3.8) and the Data Governance Implementation Roadmap (5.3.9).

---

## 3. The 6-Stage Execution Pipeline (via `/writing-th` v3.0.0)

This pipeline mandates the **Harness Architecture**, strictly enforcing Causal Chaining and 1-to-1 Micro-Scoping.

### Stage 0: Calibration (Feedforward Control)
*   **Action**: Main Agent loads `STYLE_PACK_NCAIF-Institutional.md` and `LEXICON_NCAIF-Institutional.json`.
*   **Constraint**: Activate the Jargon Ban. No "เชิงบูรณาการ", no English concepts in parentheses unless technical fields.

### Stage 1: Strategy (The Mandates)
*   **Action**: Define the Stance (The Executive View) for the 3 target deliverables. The focus must be on actionable architectures and long-term service products.

### Stage 2: Foraging (Raw Anchor Injection)
*   **Action**: Main Agent extracts exact literal texts from the finalized `.md` reports in `ψ/incubate/DCCE/CRDB/output/final_report/`. 
*   **Constraint (Raw Anchor)**: Never summarize the source before feeding it to subagents.

### Stage 3: The Payload Gate (4-Pillars)
*   **Action**: Forced constraint on all subagents. Before writing Thai prose, they MUST output a `<thought>` block extracting:
    1. **Claim**: The core argument.
    2. **Concrete Example**: Specific evidence (e.g., Service 3, or the Glossary artifact).
    3. **Consequence**: Why it matters.
    4. **Mechanism**: The technical or institutional solution.

### Stage 4: Governed Execution (1-to-1 Micro-Scoping)
*   **Action**: Main Agent spawns subagents. 
*   **Anti-Batching Law**: Subagents are assigned to specific sections of 5.2 or 5.3 individually. No subagent writes an entire chapter. 
*   **Preservation-First Rule**: Subagents are strictly forbidden from cutting concrete examples or practical evidence.

### Stage 5: Deterministic Validation (Feedback Control)
*   **Action**: Main Agent acts as the Auditor on the returning drafts.
*   **Checklist (The Warden's Audit)**:
    - [ ] **Payload Check**: Did the subagent output the 4-Pillar thought block?
    - [ ] **Preservation Check**: Are the technical models and specific 8 services retained?
    - [ ] **Active Voice Check**: Is passive voice ("ถูก...") eliminated?
    - [ ] **Lexicon Check**: Is the text completely free of forbidden words and English crutches? Is `DCCE` replaced by `กรมฯ`?
    - [ ] **Pro-Drop & Rhythm Check (Anti-Robot Rule)**: Does the draft repeat the subject ("กรมฯ") mechanically at the start of every sentence? Thai is a pro-drop language; once the subject is established, it MUST be naturally omitted in subsequent sentences. Does the text use formulaic LLM numbering ("ประการแรก", "ประการที่สอง")?
*   **Rule (Silent Rejection & Mandatory Native Edit)**: The audit is NOT just a boolean checklist. If the draft passes the lexicon rules but sounds like a robotic staccato (e.g., the "กรมฯ" Gatling gun), the Main Agent MUST perform a surgical native edit to drop redundant subjects, restore artifact agency, and ensure natural Thai institutional flow before exposing it to the human.

---

## 4. Subagent Master Prompt Template (For Stage 4)

```markdown
# IDENTITY & LENS
You are a Strategy Consultant and Harness Warden writing an executive summary section for the Department of Climate Change and Environment (DCCE). You operate under the strict mandates of `/writing-th` (v3.0.0).

# THE HARNESS CONSTRAINTS (ABSOLUTE LAWS)
1. **Preservation-First Rule:** Do not use lossy compression. Retain specific technical models and stakeholder evidence.
2. **Jargon & Language Ban:** NO conceptual English terms in parentheses. NO standard AI filler words (e.g., "อย่างไรก็ตาม", "เชิงบูรณาการ", "ในมิติ").
3. **Mandatory Lexicon:** Use `กรมฯ` (not DCCE), `กรณีการใช้งาน` (not use case), `ขั้นตอนการทำงาน` (not workflow).
4. **Active Voice Only:** Do NOT use passive voice constructs. Rewrite to state the actor clearly.

# THE PAYLOAD GATE (MANDATORY)
Before generating the final Thai text, you MUST output a `<thought>` block extracting the **4 Pillars** from your raw evidence packet: (1) Claim, (2) Concrete Example, (3) Consequence, (4) Mechanism.

# OUTPUT
After your `<thought>` block, output the drafted Thai markdown. Must be EXACTLY [Word Count Boundary].
```
