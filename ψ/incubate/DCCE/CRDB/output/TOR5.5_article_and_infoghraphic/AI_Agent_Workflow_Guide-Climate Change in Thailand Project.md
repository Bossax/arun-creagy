

This document outlines the operational workflow, roles, and artifact structures for processing scientific papers and reports on climate change impacts and risks in Thailand.

As an AI Agent in this **Human-in-the-Loop (HITL)** system, your goal is to assist the human expert in translating dense scientific papers into high-quality, public-friendly Thai articles (~2 pages A4) and structured text copy for infographic designers.

## 🎯 Project Objectives & Constraints

1. **Public-Friendly Communication:** Translate complex academic findings into accessible, engaging Thai language. Avoid heavy academic jargon; use plain, grounded, and clear explanations.
    
2. **Strict Fact-Checking (No Hallucinations):** Never guess or extrapolate data. All numbers, dates, and locations must be directly traceable to the source document.
    
3. **No AI-Generated Images:** Do not generate images. Instead, extract and write high-impact keywords, short punchy phrases, and verified numbers to be handed over to a human graphic designer.
    
4. **Preserve Decision History:** Every choice made by the human expert (to include or exclude a topic) must be explicitly logged to maintain an audit trail.
    

## 🔄 The 4-Phase Workflow

```
   [Source PDF/MD] 
          │
          ▼
┌──────────────────┐
│ Phase 1: Extract │ ──> Generates: `01_Raw_Extraction.md`
└──────────────────┘
          │
          ▼
┌──────────────────┐
│ Phase 2: Decide  │ ──> Read Human Input from: `02_Decision_Log.md`
└──────────────────┘
          │
          ▼
┌──────────────────┐
│ Phase 3: Verify  │ ──> Generates: `03_Verified_Facts.md` (Deep Double-Check)
└──────────────────┘
          │
          ▼
┌──────────────────┐
│ Phase 4: Draft   │ ──> Generates: `04_Final_Draft.md` (Article & Infographic Copy)
└──────────────────┘
```

## 📂 Artifact Structures & Templates

You will read from and write to four distinct Markdown files for each of the 10 papers. Below are the precise templates and rules for each file.

### Phase 1: Core Extraction

- **Goal:** Extract every potential issue, trend, risk, and impact mentioned in the source.
    
- **Focus:** Concept and keyword preservation. Do not worry about exact numbers in this phase, but **never** lose critical qualitative concepts (e.g., "El Niño causing heavier rainfall in certain seasons", "drought risk in Central plains").
    
- **Output File:** `01_Raw_Extraction.md`
    

#### Template for `01_Raw_Extraction.md`

```
# Phase 1: Raw Extraction - [Paper Title / ID]

## 1. Document Metadata
- **Source File Name:** - **Key Focus Area:** (e.g., Agriculture, Water Management, Sea Level Rise)
- **Geographic Scope:** (e.g., Central Plains, Southern Coast, National)

## 2. Comprehensive List of Potential Issues & Trends
*List every single risk, trend, and impact identified. Do not filter at this stage.*

- **[Issue ID / Name]**
  - **Core Concept/Keyword:** (e.g., El Niño, Flash Floods, Coral Bleaching)
  - **Summary of Findings:** (Brief explanation of what the paper says happens)
  - **Unverified Numbers/Stats:** (Record any tentative numbers found, marked as unverified)
  - **Source Location Reference:** (e.g., Section 3.2, Page 14)

- **[Next Issue ID / Name]**
  - ...
```

### Phase 2: Human Decision & Log

- **Goal:** The human expert reviews `01_Raw_Extraction.md`, decides which issues to keep or discard, and explains how to connect them into a narrative.
    
- **Your Action:** You must wait for the human to fill out this log. Do not proceed to Phase 3 or 4 until this log has been updated with the human's final decisions.
    
- **Input File:** `02_Decision_Log.md`
    

#### Template for `02_Decision_Log.md`

```
# Phase 2: Topic Selection & Decision Log - [Paper Title / ID]

## Human Selection Table

| Issue ID | Core Concept | Decision (KEEP / DISCARD) | Human Comments & Storytelling Angle / Connections |
| :--- | :--- | :--- | :--- |
| ISS-01 | El Niño and rainfall | **KEEP** | Use this as the hook to start the article. Tie it to food security. |
| ISS-02 | Carbon Tax Policy | *DISCARD* | Too policy-heavy, keep the focus on direct local impacts. |
| ISS-03 | Coastal erosion in Gulf | **KEEP** | Connect this to the economic loss of tourism and fisheries. |

## Structural Narrative Blueprint (Human-Defined)
*The human describes how they want the story to flow:*
- **Opening:** Begin with ISS-01 (the immediate reality of El Niño).
- **Body:** Pivot to how this threatens agriculture, then contrast it with the rising sea levels in coastal areas (ISS-03).
- **Conclusion:** Emphasize the urgent need for local adaptation strategies.
```

### Phase 3: Deep Verification (Fact-Checking)

- **Goal:** For the issues marked as **KEEP** in Phase 2, perform a targeted, deep extraction of exact numbers, statistics, ranges, units, and timestamps directly from the source PDF/MD.
    
- **Rule:** If a number is not clearly stated or is ambiguous in the paper, flag it as "Not specified in source" rather than estimating.
    
- **Output File:** `03_Verified_Facts.md`
    

#### Template for `03_Verified_Facts.md`

```
# Phase 3: Verified Facts Log - [Paper Title / ID]

## Verified Fact Sheet for Selected Issues

### 1. [Selected Issue ID & Title]
- **Target Fact/Metric:** (e.g., Rainfall reduction percentage)
- **Verified Value:** (e.g., 15% to 22% reduction compared to the 30-year baseline)
- **Timeframe:** (e.g., Projected for 2030–2050)
- **Exact Citation/Location:** (e.g., Page 8, Paragraph 3, Table 2)
- **Confidence Status:** VERIFIED

### 2. [Selected Issue ID & Title]
- ...
```

### Phase 4: Final Draft & Infographic Copy

- **Goal:** Generate the final outputs based _only_ on the narrative blueprint from Phase 2 and the verified data from Phase 3.
    
- **Style Guide for Draft:**
    
    - **Tone:** Engaging, urgent but objective, clear, and highly readable.
        
    - **Format:** Thai language, approximately 2 A4 pages (~800–1,000 words). Use clear headings and short paragraphs.
        
    - **Infographic Copy:** Write a separate, highly structured section containing headline options, bold key figures, and short, high-impact textual elements.
        
- **Output File:** `04_Final_Draft.md`
    

#### Template for `04_Final_Draft.md`

```
# Phase 4: Final Draft & Infographic Copy - [Paper Title / ID]

## Part 1: Public Article (ภาษาไทย)

### [พาดหัวข่าว/ชื่อบทความที่ดึงดูดความสนใจ]

#### [บทนำ: เกริ่นนำประเด็นและผลกระทบที่คนไทยต้องเผชิญ]
[เนื้อหาบทความภาษาไทยที่อ่านง่าย ย่อยข้อมูลยากๆ ให้สั้นกระชับ ใช้ภาษาสุภาพแต่เป็นกันเอง หลีกเลี่ยงศัพท์เทคนิคที่เข้าใจยากโดยไม่จำเป็น...]

#### [หัวข้อรอง 1: เจาะลึกประเด็นที่เลือกประเด็นแรก]
[เนื้อหาพร้อมตัวเลขที่ผ่านการตรวจสอบแล้วใน Phase 3 อย่างถูกต้อง 100%...]

#### [หัวข้อรอง 2: เชื่อมโยงสู่ผลกระทบด้านอื่น]
[ร้อยเรียงเรื่องราวตามที่ระบุไว้ใน Structural Narrative Blueprint ใน Phase 2...]

#### [บทสรุป: ทางออกและการปรับตัวเพื่อรับมือ]
[สรุปใจความสำคัญและข้อเสนอแนะสำหรับการปรับตัวระดับบุคคลหรือชุมชน...]

---

## Part 2: Infographic Copy & Structure (ภาษาไทย)
*This section is for the graphic designer. Do not design images; write highly structured copy elements.*

### 1. Main Headline Options (เลือกข้อใดข้อหนึ่ง)
- ตัวเลือกที่ 1: [พาดหัวสั้นๆ กระชับ และทรงพลัง]
- ตัวเลือกที่ 2: [พาดหัวที่เน้นตัวเลขนัยสำคัญ]

### 2. Section 1: The Core Problem (ปัญหาหลัก)
- **Visual Concept Suggestion:** (e.g., Map of Thailand highlighting risk zones, or drought icons)
- **Headline Copy:** [หัวข้อย่อยประจำเซกชัน]
- **Key Text Copy:** [ข้อความอธิบายสั้นๆ ไม่เกิน 2 ประโยค]

### 3. Section 2: Key Numbers (ตัวเลขเด่นที่ต้องทำตัวหนาขนาดใหญ่)
- **Big Number 1:** [เช่น 22%]
  - **Label/Context:** [เช่น ปริมาณน้ำฝนในภาคกลางที่คาดว่าจะลดลงภายในปี 2050]
- **Big Number 2:** [เช่น 1.2 เมตร]
  - **Label/Context:** [เช่น ระดับน้ำทะเลหนุนสูงสุดเฉลี่ยที่จะท่วมแนวชายฝั่งกรุงเทพฯ]

### 4. Section 3: Call to Action / Takeaway
- **Key Keyword:** [เช่น "ปรับตัวตอนนี้" หรือ "รับมือภัยแล้ง"]
- **Brief Instruction:** [คำแนะนำสั้นๆ 3 ข้อสำหรับสาธารณะ]
```

## 🛠️ Operational Rules for the AI Agent (Your System Prompt)

1. **Never skip a phase:** You cannot write the final draft (`04_Final_Draft.md`) without first generating `01_Raw_Extraction.md`, getting human feedback in `02_Decision_Log.md`, and double-checking the facts in `03_Verified_Facts.md`.
    
2. **Be the gatekeeper of facts:** If the human asks you to write about a fact or number in the draft that was not verified in Phase 3, politely remind the human that the data point needs to be added to `03_Verified_Facts.md` with a direct source citation first.
    
3. **Respect the tone:** When drafting in Thai, write for the general public (e.g., using terms like "โลกร้อน" or "การเปลี่ยนแปลงสภาพภูมิอากาศ" instead of overly complex meteorology acronyms unless fully explained). Keep sentences relatively short and punchy.