# SOP: NCAIF Chapter 5.2 (5.2.3, 5.2.5, 5.2.7) Structural Rewrite

## 1. Objective and Stance
*   **Mission:** Redesign the high-level content structure of chapters 5.2.3, 5.2.5, and 5.2.7 to focus on the "Journey of Requirement Gathering." 
*   **The Problem:** The current chapters read like chronological progress logs, repeating and evolving the "Sitemap" structure, which causes reader confusion before the final reveal in 5.2.9.
*   **The Fix:** Remove the repetitive sitemap lists from 5.2.3, 5.2.5, and 5.2.7. Anchor each chapter to a specific layer of requirements (Data, Governance, User Experience) while strictly preserving the underlying evidence, stakeholder insights, and academic grounding.

## 2. Agent Roles (The Harness Architecture)
This operation follows the strict mandates of the `/writing-th` (v3.0.0) skill.
*   **Main Agent (Oracle):** Acts as Strategy Consultant and Harness Warden. Responsible for strategy, evidence foraging, subagent orchestration, and the Stage 5 final audit (Late-Pass Diction Cleanup).
*   **Subagents (The Drafters):** Operate under 1-to-1 Micro-Scoping (one agent per chapter). Responsible for generating the initial Thai prose and performing the Stage 3 Payload Gate (4-Pillar Extraction).

## 3. The 6-Stage Execution Pipeline

### Stage 0: Calibration (Feedforward Control)
*   **Action:** Main Agent loads `ψ/memory/style/STYLE_PACK_NCAIF-Institutional.md`.
*   **Constraint:** Establish absolute bans on conceptual English parentheticals, passive voice, and AI jargon.

### Stage 1: Strategy (The Mandates)
*   **5.2.3 (Academic Baseline):** Focus on IPCC standards, 4 core pillars, and FGD 1 requirements. *Mandate: Delete the 7-menu sitemap. Focus on the abstract Conceptual Data Model.*
*   **5.2.5 (Governance Realities):** Focus on FGD 2 feedback, the Data Management Ladder, and institutional governance roles. *Mandate: Delete the frontend sitemap updates. Focus purely on backend data rules.*
*   **5.2.7 (User Experience):** Focus on the May 12 Workshop, user journey workflows, and platform sustainability. *Mandate: Conclude that these UX requirements dictate the final architecture.*

### Stage 2: Foraging
*   **Action:** Main Agent reads and extracts the literal raw text from:
    *   `.../final_report/5.2/5.2.3 การจัดทำ (ร่าง) โครงสร้างข้อมูล... .md`
    *   `.../final_report/5.2/5.2.5 การปรับปรุง (ร่าง) กรอบ NCAIF... .md`
    *   `.../final_report/5.2/5.2.7 ปรับปรุงเติมต่อ (ร่าง) โครงสร้างข้อมูล... .md`

### Stage 3: The Payload Gate (4-Pillars)
*   **Action:** Forced upon the subagents. Before drafting, they must output a `<thought>` block extracting:
    1.  **Claim:** Core argument of the phase.
    2.  **Concrete Example:** Specific user feedback or data point.
    3.  **Consequence:** Why it matters.
    4.  **Mechanism:** How it was discovered.

### Stage 4: Governed Execution (1-to-1 Micro-Scoping)
*   **Action:** Main Agent invokes 3 concurrent subagents.
*   **Prompting:** Each subagent receives the Master Prompt, the Full Style Pack, their specific Chapter Raw Text, and their specific Stage 1 Mandate.
*   **Anti-Batching:** One agent, one chapter. No cross-contamination.

### Stage 5: Deterministic Validation & Cleanup (Feedback Control)
*   **Action:** Main Agent acts as the Auditor on the returning drafts.
*   **Checklist (Scale 4 Lexicon & Cleanup):**
    *   [ ] *Preservation-First:* Are the stakeholder examples and academic proofs fully intact?
    *   [ ] *Active Agency:* Has all passive voice (e.g., "ถูกออกแบบให้") been rewritten to active (e.g., "กรมฯ จัดทำ")?
    *   [ ] *Jargon Ban:* Are all conceptual English parentheticals removed?
    *   [ ] *Institutional Terminology:* Are words like `DCCE`, `use case`, and `workflow` correctly mapped to `กรมฯ`, `กรณีการใช้งาน`, and `ขั้นตอนการทำงาน`?
    *   [ ] *Anti-AI Shield:* Are structural crutches like "ไม่ได้...แต่..." or "อย่างไรก็ตาม" removed?
*   **Resolution:** 
    *   If minor diction errors exist, Main Agent performs surgical native edits.
    *   If structural or evidence failure occurs, Main Agent issues a Silent Rejection and re-triggers the subagent.
*   **Final Commit:** Main Agent uses native `replace_file_content` to commit the polished text to the respective markdown files.

---

## Appendix: Subagent Master Prompt

```markdown
# IDENTITY & LENS
You are a Strategy Consultant and a Harness Warden writing an official Thai government report for the Department of Climate Change and Environment (DCCE). You do not write like a standard AI. Your tone is authoritative, precise, active, and strictly tethered to concrete evidence.

# YOUR MISSION (1-to-1 Micro-Scoping)
You are assigned to rewrite exactly ONE section of the Interim Report. 
You will be provided with the RAW, literal text of your section, alongside a specific "Structural Mandate". 

Your goal is to rewrite the section to focus heavily on the "Requirements Gathering Journey", stripping out repetitive sitemap drafts that bloat the document, while fiercely protecting the underlying evidence and stakeholder insights.

# THE HARNESS CONSTRAINTS (ABSOLUTE LAWS)
1. **Preservation-First Rule:** You must NOT summarize or delete the concrete examples, stakeholder feedback, or academic justifications from the raw text. You are only deleting the redundant "Sitemap lists".
2. **Jargon & Language Ban:** NO conceptual English terms in parentheses. NO standard AI filler words (e.g., "อย่างไรก็ตาม", "เชิงบูรณาการ").
3. **Mandatory Lexicon:** Use `กรมฯ` (not DCCE), `กรณีการใช้งาน` (not use case), `ขั้นตอนการทำงาน` (not workflow).
4. **Active Voice Only:** Do NOT use passive voice constructs. Rewrite to state the actor clearly.

# FULL STYLE PACK RULES
[FULL STYLE PACK DYNAMICALLY INJECTED HERE]

# THE PAYLOAD GATE (MANDATORY THOUGHT PROCESS)
Before generating the final Thai text, you MUST output a `<thought>` block extracting the **4 Pillars** from your raw text to prove you understand the core evidence: (1) Claim, (2) Concrete Example, (3) Consequence, (4) Mechanism.

# OUTPUT FORMAT
After your `<thought>` block, output the final, polished Thai markdown.
```

## 4. Progress Log
*   **[2026-07-04 10:20] Stage 0-2 Complete:** SOP established. Execution initialized. Invoking 3 concurrent subagents for chapters 5.2.3, 5.2.5, and 5.2.7.
*   **[2026-07-04 10:22] Stage 5 (5.2.7) Complete:** Subagent 3 returned the draft for 5.2.7. Audit found a minor pseudo-contrast ("ไม่ได้...แต่..."). Natively corrected by Oracle to direct phrasing ("ตั้งต้นการค้นหา... มากกว่า..."). Replaced target file content.
*   **[2026-07-04 10:24] Stage 5 (5.2.3) Complete:** Subagent 1 returned the draft for 5.2.3. Corrected minor pseudo-contrast and formatted the 4 core pillars as a numbered list according to Style Pack Rule 24. Replaced target file content.
*   **[2026-07-04 10:26] Stage 5 (5.2.5) Complete:** Subagent 2 returned the draft for 5.2.5. Passed all audit constraints perfectly. The Data Management Ladder and Governance roles are preserved while the sitemap is removed. Replaced target file content. All operations complete.
