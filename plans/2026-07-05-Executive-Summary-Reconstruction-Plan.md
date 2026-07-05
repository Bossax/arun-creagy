# SOP: Executive Summary Reconstruction & Expansion (Official Source Mapped)

## 1. Output Deliverables
The execution pipeline will produce exactly **3 distinct documents** to ensure technical depth hierarchy and prevent lossy compression:
1.  **Chapter 5.2 Executive Summary**: Exactly 8 paragraphs. Focused on the Platform Architecture & Governance Engine.
2.  **Chapter 5.3 Executive Summary**: Exactly 9 paragraphs. Focused on Strategic Impact, Services, Gaps, and the Roadmap.
3.  **The Report-Level Executive Summary**: A combined synthesis of 17 paragraphs maintaining the exact order (8 paragraphs from 5.2, followed by 9 paragraphs from 5.3).

We will write these files to:
-   `ψ/incubate/DCCE/CRDB/output/final_report/5.2_Executive_Summary.md`
-   `ψ/incubate/DCCE/CRDB/output/final_report/5.3_Executive_Summary.md`
-   `ψ/incubate/DCCE/CRDB/output/final_report/Report_Executive_Summary.md`

## 2. Strategic Framing & Narrative Logic
*   **The 5.2 Frame (The Engine):** Chapter 5.2 provides the required governance standards, architectural artifacts (CDM, Glossary), and role assignments necessary to build and keep the platform running.
*   **The 5.3 Frame (The Impact):** Chapter 5.3 focuses on the strategic, long-term development of climate information products and services, bridging architecture to institutional value.

### Chapter 5.2 Paragraph Mappings (8 Paragraphs)
*   **Paragraph 1: ที่มาและความสำคัญของแพลตฟอร์ม**
    -   *Source File*: `5.2.1` & `5.2.2`
*   **Paragraph 2: บทเรียนจากต่างประเทศและรูปแบบการออกแบบ**
    -   *Source File*: `5.2.1`
*   **Paragraph 3: สถานะและหลักเกณฑ์ของเว็บไซต์กรมในปัจจุบัน**
    -   *Source File*: `5.2.2`
*   **Paragraph 4: กระบวนการรวบรวมข้อมูลและการรับฟังความคิดเห็น**
    -   *Source Files*: `5.2.4` & `5.2.6` & `5.2.8`
*   **Paragraph 5: หลักการออกแบบสถาปัตยกรรมข้อมูลและประสบการณ์ผู้ใช้**
    -   *Source File*: `5.2.3` & `5.2.5`
*   **Paragraph 6: การออกแบบระบบหน้าบ้าน (Sitemap) และระบบหลังบ้าน (Data Governance)**
    -   *Source File*: `5.2.7`
*   **Paragraph 7: สรุปปิดท้ายแผนผังเว็บไซต์ (Sitemap)**
    -   *Source File*: `5.2.9`
*   **Paragraph 8: สรุปปิดท้ายกรอบธรรมาภิบาลข้อมูล (ตามบทที่ 5.2.9)**
    -   *Source File*: `5.2.9`

### Chapter 5.3 Paragraph Mappings (9 Paragraphs)
*   **Paragraph 1: การทบทวนสถานะปัจจุบันของกรม (Baseline)**
    -   *Source Files*: `5.3.1` & `5.3.2`
*   **Paragraph 2: ผลจากการสัมภาษณ์เชิงลึกและการประชุมเชิงปฏิบัติการ (Workshop)**
    -   *Source Files*: `5.3.2` & `5.3.3`
*   **Paragraph 3: กรณีการใช้งาน (Use Cases) อุปสรรค และความต้องการของกลุ่มผู้ใช้**
    -   *Source File*: `5.3.3`
*   **Paragraph 4: การออกแบบ 8 บริการหลัก (8 Core Services)**
    -   *Source File*: `5.3.3`
*   **Paragraph 5: การทบทวนกลไกและช่องว่างระบบรายงานภัย ปภ. (DDPM/PDNA) เทียบกับมาตรฐานสากล**
    -   *Source File*: `5.3.6`
*   **Paragraph 6: แบบจำลองข้อมูลและชุดข้อมูลขั้นต่ำสำหรับความสูญเสียและความเสียหายจากภัยพิบัติ (MVD)**
    -   *Source File*: `5.3.7`
*   **Paragraph 7: การวิเคราะห์ช่องว่างข้อมูล (Data Gap Analysis)**
    -   *Source Files*: `5.3.8` & `5.3.11`
*   **Paragraph 8: ข้อเสนอแนะเชิงยุทธศาสตร์ 7 ข้อ**
    -   *Source File*: `5.3.9`
*   **Paragraph 9: แผนงานการจัดตั้งธรรมาภิบาลข้อมูล (Data Governance Roadmap)**
    -   *Source File*: `5.3.9`

---

## 3. The 6-Stage Execution Pipeline (via `/writing-th` v3.0.0)

This pipeline mandates the **Harness Architecture**, strictly enforcing Causal Chaining and 1-to-1 Micro-Scoping. *Crucially, we focus first on structural layout and content accuracy before detailed stylistic refinement to prevent sub-agent glitching.*

### Stage 0: Calibration (Structural Focus)
*   **Action**: Main Agent prepares for a layout-first generation. We will initially hold back complex stylistic mandates to prevent sub-agent cognitive overload and hallucinations.

### Stage 1: Strategy (The Mandates)
*   **Action**: Define the Stance (The Executive View) for the target deliverables. Focus strictly on correct mapping of content to the specified paragraphs and ensuring bundled topics in 5.3 are clearly split.

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
*   **Action**: Main Agent spawns subagents to draft content section by section.
*   **Anti-Batching Law**: Subagents are assigned to specific sections of 5.2 or 5.3 individually. No subagent writes an entire chapter at once.
*   **Structural Priority**: Ensure the paragraph splits (especially for 5.3 bundled topics) are strictly enforced to avoid confusing the reader.

### Stage 5: Deterministic Validation (Feedback Control) & Tone Refinement
*   **Action**: Main Agent acts as the Auditor on the returning drafts.
*   **Checklist (The Warden's Audit - Structural)**:
    - [ ] **Paragraph Count**: Are there exactly 8 (for 5.2) or 9 (for 5.3) paragraphs?
    - [ ] **Payload Check**: Did the subagent output the 4-Pillar thought block?
    - [ ] **Preservation Check**: Are the technical models and specific 8 services retained?
*   **Phase 2: Tone & Style Refinement**: *After* the structural layout is confirmed, the Main Agent performs native edits to enforce the `LEXICON_NCAIF-Institutional.json` and `STYLE_PACK_NCAIF-Institutional.md`. This includes replacing DCCE with กรมฯ, removing passive voice, and dropping redundant subjects to ensure natural Thai institutional flow.

---

## 4. Subagent Master Prompt Template (For Stage 4 - Structural Focus)

```markdown
# IDENTITY & LENS
You are a Strategy Consultant and Harness Warden writing an executive summary section for the Department of Climate Change and Environment (DCCE). You operate under the strict mandates of `/writing-th` (v3.0.0).

# THE HARNESS CONSTRAINTS (ABSOLUTE LAWS)
1. **Preservation-First Rule:** Do not use lossy compression. Retain specific technical models and stakeholder evidence.
2. **Structural Strictness:** Focus on clear separation of ideas. Ensure bundled topics are clearly split into separate paragraphs as mapped.
3. **Drafting Priority (Avoid Over-Styling):** Focus on logical flow, causal chaining, and accurate information architecture. Detailed tonal refinement (like strict jargon bans or pro-drop rules) will be handled in a subsequent pass. Prioritize structural correctness.

# THE PAYLOAD GATE (MANDATORY)
Before generating the final Thai text, you MUST output a `<thought>` block extracting the **4 Pillars** from your raw evidence packet: (1) Claim, (2) Concrete Example, (3) Consequence, (4) Mechanism.

# OUTPUT
After your `<thought>` block, output the drafted Thai markdown for your specific assigned section. Must match the designated paragraph count perfectly.
```
