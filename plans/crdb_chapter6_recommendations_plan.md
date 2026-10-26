# Implementation Plan: Restructuring CRDB Full Report Chapter 6 (Draft Version) vs Chapter 7 (Final Version) Strictly under TOR Framing

## Goal Description

The project evaluation committee noted that under the project Terms of Reference (TOR), **Chapter 6** must correspond to **Scope Item 5.3.9: (Draft) Policy and Technical Recommendations** (`จัดทำ (ร่าง) ข้อเสนอแนะเชิงนโยบายและเชิงเทคนิค...`), while the final synthesized recommendations belong in **Chapter 7 (Section 7.3)** as the contract-closing deliverable under Installment 4.

Crucially, the committee requires that the reporting strictly mirror the contractual TOR wording:
> **"ข้อมูลเสนอแนะเชิงนโยบายและเชิงเทคนิคในการพัฒนารายการชุดข้อมูลพื้นฐาน รายการผลิตภัณฑ์ข้อมูลและสารสนเทศและการบริหารจัดการข้อมูลในระยะยาว"**  
> *(Policy and Technical Recommendations for developing Baseline Data Inventory, Information Product Inventory, and Long-Term Data Management)*

Right now, the submitted file [`Chapter 6-report-first-submission.md`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/drafts/crdb-full-report-6/Chapter%206-report-first-submission.md) already contains the end-state, ultra-hardened procurement blueprint (SDLC 6-phase framework, 8 handover components, 4 decision-authority prioritized recommendations including the in-house data talent mandate, and the 2-track parallel roadmap). Consequently, the report currently lacks the authentic "Draft Version" reflecting the direct study findings under TOR 5.3.9, creating narrative redundancy and a temporal disconnect with Chapter 7.

This plan details:
1. The structural mapping of recommendations across both chapters strictly conforming to the TOR frame.
2. The substantial presence of **การบริหารจัดการข้อมูลในระยะยาว (Long-Term Data Management)** in Chapter 7.3 across Policy, Technical, and Concluding Roadmap sections.
3. The directory structure and completed harvesting materials organized in `plans/chapter6/` and `plans/chapter7_3/`.
4. The transition logic explaining what was enhanced, dissected, or dropped from Chapter 6 to Chapter 7.3.
5. The complete, unit-by-unit drafting specifications (`drafting_plan.md`) for both chapters.

---

## User Review Required

> [!IMPORTANT]
> **Clarification on Long-Term Data Management in Chapter 7.3**:
> Long-Term Data Management is not missing in Chapter 7.3; it is the **central operational backbone** of the final recommendations:
> - **Policy (§7.3.1.3)**: 4-Tier Internal Data Governance Structure (`REC-MGMT-POL-01`) + In-House Data Capability Building (Data Engineers, Analysts, Managers) (`REC-MGMT-POL-02`) + Agile Software Delivery Governance (`REC-MGMT-POL-03`).
> - **Technical (§7.3.2.3)**: Automated CMS Validation Rules & Data Pipeline Protocols (`REC-MGMT-TECH-01`).
> - **Concluding Overarching Section (§7.3.3)**: The 2-Track Implementation Roadmap (Software Contract Track + 8 DCCE Internal Governance Tasks: 4 short-term $\le 6$ mo, 4 medium-term 1–3 yr) and Contract-Governance Convergence Gates (`REC-MGMT-ROADMAP-01`).

> [!NOTE]
> Based on Boss's selections:
> 1. In **Chapter 6 (Draft)**, capability positioning concepts are toned down to standard administrative Thai phrasing (e.g., บทบาทการเป็นหน่วยงานรับรองมาตรฐานชุดข้อมูลอ้างอิงกลาง, การเป็นสะพานเชื่อมและแปลงข้อมูลวิทยาศาสตร์สู่การตัดสินใจ) rather than stylized English slogans.
> 2. In **Chapter 7.3 (Final)**, the 2-Track Implementation Roadmap is positioned as a dedicated concluding synthesis subsection (**Section 7.3.3**).

---

## 1. Directory Structure & Harvested Evidence in `plans/`

All planning documents, evidence maps, outlines, and unit-by-unit drafting specifications have been completed and organized into dedicated subfolders in `plans/`:

```
plans/
├── current_chapter6_components_viz.html             # Interactive visual model of first submission & TOR matrix
├── recommendations_genealogy_and_line_drawing_viz.html # Interactive 4-epoch forensic timeline & side-by-side comparison
├── crdb_recommendations_evaluator.json              # Machine-readable LLM evaluation harness for Chapter 7.3
├── transition_logic_ch6_to_ch7_3.md                 # Detailed rationales for what was enhanced, dissected, or dropped
├── chapter6/
│   ├── evidence_map.md                              # Harvested evidence sources, quotes, and ledger anchors for Chapter 6
│   ├── english_outline.md                           # Structural English outline for Chapter 6 under TOR frame
│   └── drafting_plan.md                             # Unit-by-unit drafting specification for Chapter 6 (Units 1–4)
└── chapter7_3/
    ├── evidence_map.md                              # Harvested evidence sources, DRD v2 specs, and ledger anchors for 7.3
    ├── english_outline.md                           # Structural English outline for Section 7.3 under TOR frame
    └── drafting_plan.md                             # Unit-by-unit drafting specification for Section 7.3 (Units 1–3)
```

---

## 2. Structural Layout for Chapter 6 (Draft Version)

**Title**: บทที่ 6 (ร่าง) ข้อมูลเสนอแนะเชิงนโยบายและเชิงเทคนิคในการพัฒนารายการชุดข้อมูลพื้นฐาน รายการผลิตภัณฑ์ข้อมูลและสารสนเทศและการบริหารจัดการข้อมูลในระยะยาว  
*(Fulfills TOR Scope Item 5.3.9 under Installment 3)*

- **6.1 บริบทและความเชื่อมโยงจากผลการวิเคราะห์ช่องว่างสู่กรอบข้อเสนอแนะฉบับร่าง**
  - สรุปข้อค้นพบ 5 ประการจาก Gap Analysis (5.3.8) และการเปลี่ยนบทบาทของ กรม สส. จากคลังเก็บไฟล์สู่การเป็นผู้นำด้านบริการข้อมูลการปรับตัว
- **6.2 ข้อมูลเสนอแนะเชิงนโยบาย (Policy Recommendations)**:
  - *6.2.1 ด้านการพัฒนารายการชุดข้อมูลพื้นฐาน*: นโยบายการเปิดเผยข้อมูลสาธารณะ และการสร้างความร่วมมือเชิงสถาบันกับหน่วยงานต้นทาง (อม., GISTDA, สถิติ, แหล่งน้ำ)
  - *6.2.2 ด้านการพัฒนารายการผลิตภัณฑ์ข้อมูลและสารสนเทศ*: นโยบายการบริหารระบบข้อมูลในฐานะ Service Portfolio 4 กลุ่มบริการ และบทบาทการเป็นหน่วยงานรับรองมาตรฐานชุดข้อมูลอ้างอิงกลางและการแปลงข้อมูลวิทยาศาสตร์สู่การตัดสินใจเชิงนโยบาย
  - *6.2.3 ด้านการบริหารจัดการข้อมูลในระยะยาว*: การสถาปนากรอบธรรมาภิบาลข้อมูลภายใน 6 องค์ประกอบ, กลไกคุ้มครองการปฏิบัติงานของเจ้าหน้าที่ (Institutional Protection), และนโยบายทรัพยากร โครงสร้างพื้นฐานไอที และการพัฒนากำลังคนเฉพาะทางรายสาขา
- **6.3 ข้อมูลเสนอแนะเชิงเทคนิค (Technical Recommendations)**:
  - *6.3.1 ด้านการพัฒนารายการชุดข้อมูลพื้นฐาน*: มาตรฐานคำอธิบายข้อมูล (Metadata Standard 12 ฟิลด์), พจนานุกรมข้อมูลกลาง (Data Dictionary) และแบบจำลองข้อมูลเชิงแนวคิด (CDM 8 โดเมน)
  - *6.3.2 ด้านการพัฒนารายการผลิตภัณฑ์ข้อมูลและสารสนเทศ*: ระบบสารบัญระเบียบวิธีวิเคราะห์ความเสี่ยง (Risk Methodology Catalog), มาตรฐานการแปลงวิทยาศาสตร์สู่การตัดสินใจ (Science-to-Decision), และมาตรฐานการสื่อสารความไม่แน่นอน (Uncertainty Communication)
  - *6.3.3 ด้านการบริหารจัดการข้อมูลในระยะยาว*: มาตรฐานการเชื่อมต่อ Interoperability/API, การฝังกฎตรวจสอบอัตโนมัติในระบบจัดการข้อมูล, และกรอบลำดับการดำเนินงานเชิงวิเคราะห์ 3 ขอบฟ้า (3 Horizons)

*(See [`plans/chapter6/drafting_plan.md`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/plans/chapter6/drafting_plan.md) for full paragraph blueprints).*

---

## 3. Structural Layout for Chapter 7.3 (Final Version)

**Title**: 7.3 ข้อมูลเสนอแนะเชิงนโยบายและเชิงเทคนิคในการพัฒนารายการชุดข้อมูลพื้นฐาน รายการผลิตภัณฑ์ข้อมูลและสารสนเทศและการบริหารจัดการข้อมูลในระยะยาว (ฉบับสมบูรณ์)  
*(Fulfills TOR Installment 4 Deliverable 4)*

- **7.3.0 บริบทวิวัฒนาการ ข้อมูลประจักษ์ใหม่ และแนวทางการกำหนดข้อเสนอแนะ (Contextual Evolution, New Empirical Findings & Analytical Framing)**:
  - สรุปความต่อเนื่องในการประยุกต์ใช้ผลงานผ่านเลนส์วงจรการพัฒนาระบบ (SDLC) ซึ่งโครงการนี้ได้ส่งมอบระยะ Planning (~70%) และ System Design (~80%) แล้ว
  - การผสาน 4 ชุดข้อมูลเชิงประจักษ์ใหม่: บัญชีข้อมูล 260 ชุด (5 หน่วยงานถือครอง 97 ชุด / ร้อยละ 37.3), พิมพ์เขียวสถาปัตยกรรม 8 รายการในภาคผนวก ฌ, พันธกรณีการรายงาน A-BTR 147 ตัวชี้วัด, และความพร้อมข้อมูล Loss & Damage แบบ 2-Step MVP
  - คำอธิบายกระชับถึงแนวทางการกำหนดข้อเสนอแนะ และสรุปประเด็นการยกระดับในฉบับสมบูรณ์เป็นหัวข้อชัดเจน (`REC-INTRO-EVOL-01`)
- **7.3.1 ข้อมูลเสนอแนะเชิงนโยบาย (Policy Recommendations)**:
  - *7.3.1.1 ด้านการพัฒนารายการชุดข้อมูลพื้นฐาน*: นโยบายการจัดทำข้อตกลงแลกเปลี่ยนข้อมูลเชิงรุกกับ 5 หน่วยงานหลัก (ถือครอง 97 ชุดข้อมูล / 37.3%) โดยยึดความต้องการของ กรม สส. เป็นตัวตั้ง และดำเนินงานคู่ขนาน (`REC-BASE-POL-01`)
  - *7.3.1.2 ด้านการพัฒนารายการผลิตภัณฑ์ข้อมูลและสารสนเทศ*: ยุทธศาสตร์ผลิตภัณฑ์นำและการจัดลำดับ 5 บริการสำคัญ (3 เดิม + 2 ใหม่: A-BTR, Disaster Loss & Damage MVP ร่วมกับ สศช.) และระบบแค็ตตาล็อกข้อมูล (`REC-PROD-POL-01`)
  - *7.3.1.3 ด้านการบริหารจัดการข้อมูลในระยะยาว*:
    1. โครงสร้างธรรมาภิบาลข้อมูลภายใน 4 ระดับ (คณะกรรมการกองฯ, Data Owner, Data Steward, Data Custodian) (`REC-MGMT-POL-01`)
    2. **นโยบายการสร้างกำลังคนด้านข้อมูลภายในองค์กร (Data Engineers, Analysts, Managers แยกขาดจากฝ่ายไอทีเดิม)** (`REC-MGMT-POL-02`)
    3. **กรอบการบริหารสัญญาจ้างพัฒนาระบบแบบคล่องตัว (Agile) อย่างน้อย 2 รอบ พร้อมหมุดหมายทดสอบ Beta กลางสัญญา** (`REC-MGMT-POL-03`)
- **7.3.2 ข้อมูลเสนอแนะเชิงเทคนิค (Technical Recommendations)**:
  - *7.3.2.1 ด้านการพัฒนารายการชุดข้อมูลพื้นฐาน*: การบังคับใช้แบบจำลองข้อมูลเชิงแนวคิด (CDM 8 โดเมน), ทะเบียนทรัพย์สินดิจิทัล, และมาตรฐาน Metadata เป็นเกณฑ์เทคนิคของสัญญาจ้าง (`REC-BASE-TECH-01`)
  - *7.3.2.2 ด้านการพัฒนารายการผลิตภัณฑ์ข้อมูลและสารสนเทศ*: พิมพ์เขียวสถาปัตยกรรมระบบบนวงจร SDLC 6 ระยะ (ส่งมอบระยะ 1 (~70%) และ 2 (~80%)) พร้อมชุดข้อมูลสนับสนุนการพัฒนา 8 องค์ประกอบในภาคผนวก ฌ และการแบ่งบทบาท Content Writer vs System Developer (`REC-PROD-TECH-01`, `REC-PROD-TECH-02`)
  - *7.3.2.3 ด้านการบริหารจัดการข้อมูลในระยะยาว*: การฝังกฎตรวจสอบอัตโนมัติใน CMS และท่อส่งข้อมูล (Automated Validation Protocols) (`REC-MGMT-TECH-01`)
- **7.3.3 แผนที่นำทางสำหรับการพัฒนาระบบและธรรมาภิบาลข้อมูล และจุดบรรจบของสัญญา (Overarching Roadmap & Convergence Gates)**:
  - การแบ่งงานเป็น 2 กลุ่มงานคู่ขนาน: กลุ่มที่ 1 สัญญาจ้างพัฒนาระบบ (5 บริการ + แค็ตตาล็อก + Agile) และ กลุ่มที่ 2 ภารกิจธรรมาภิบาลข้อมูล 8 งาน (ระยะสั้น 4 งาน 6 เดือน, ระยะกลาง 4 งาน 1–3 ปี)
  - จุดบรรจบสำคัญระหว่างการรับรองมาตรฐานของ กรม สส. กับการสร้างกฎ CMS ของผู้รับจ้าง (`REC-MGMT-ROADMAP-01`)

*(See [`plans/chapter7_3/drafting_plan.md`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/plans/chapter7_3/drafting_plan.md) for full paragraph blueprints).*

---

## 4. Completed Planning Package Summary

| File Path | Description | Status |
|---|---|---|
| [`plans/chapter6/evidence_map.md`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/plans/chapter6/evidence_map.md) | Complete source harvest and quotes for Chapter 6 | **Ready** |
| [`plans/chapter6/english_outline.md`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/plans/chapter6/english_outline.md) | **Narrative English outline** for Chapter 6 detailing argumentative flow without bullet lists, AI clichés, or abstract nominalizations | **Ready (Narrative)** |
| [`plans/chapter6/drafting_plan.md`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/plans/chapter6/drafting_plan.md) | Unit-by-unit drafting specification for Chapter 6 (Units 1–4) | **Ready** |
| [`plans/chapter7_3/evidence_map.md`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/plans/chapter7_3/evidence_map.md) | Complete source harvest, DRD v2 specs, and ledger anchors for 7.3 | **Ready** |
| [`plans/chapter7_3/english_outline.md`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/plans/chapter7_3/english_outline.md) | **Narrative English outline** for Section 7.3 detailing argumentative flow without bullet lists, AI clichés, or abstract nominalizations | **Ready (Narrative)** |
| [`plans/chapter7_3/drafting_plan.md`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/plans/chapter7_3/drafting_plan.md) | Unit-by-unit drafting specification for Section 7.3 (Units 1–3) | **Ready** |
| [`plans/transition_logic_ch6_to_ch7_3.md`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/plans/transition_logic_ch6_to_ch7_3.md) | Transition logic & rationales for enhanced/dissected/dropped items | **Ready** |
| [`plans/crdb_recommendations_evaluator.json`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/plans/crdb_recommendations_evaluator.json) | Machine-readable evaluation matrix for automated verification | **Ready** |

---

## 5. Next Steps (Upon User Approval)

The planning phase is now complete. When ready to proceed to drafting:
1. **Chapter 6 Drafting**: Verbalize Chapter 6 draft into `ψ/incubate/drafts/crdb-full-report-6/Chapter 6-report-first-submission.md` following [`plans/chapter6/drafting_plan.md`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/plans/chapter6/drafting_plan.md).
2. **Section 7.3 Drafting**: Verbalize Section 7.3 into `ψ/incubate/drafts/crdb-full-report-7/draft.md` following [`plans/chapter7_3/drafting_plan.md`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/plans/chapter7_3/drafting_plan.md).
3. **Automated Verification**: Audit the drafted sections against [`plans/crdb_recommendations_evaluator.json`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/plans/crdb_recommendations_evaluator.json).
