# Refinement Plan: Restructuring, Outlining & Synthesizing the WP9 Thai Docu-Slide Deck

**Date**: 2026-08-10  
**Target File**: [`2026-08-10_WP9_LossDamage_DocuSlide_Deck_TH.md`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRDB/output/09_LDM_LossDamage_DataModel/2026-08-10_WP9_LossDamage_DocuSlide_Deck_TH.md)  
**Status**: Completed & Merged into Project Repository  

---

## 1. Goal & Rationale

Refine and restructure the WP9 Thai Docu-Slide deck (`2026-08-10_WP9_LossDamage_DocuSlide_Deck_TH.md`) to address all user feedback and inline comments, relieve visual density, enforce institutional Thai language style (NCAIF style), and transform the deck from a technical SQL developer schema into an **Executive Mindset Policy & Governance Deck**.

Instead of forcing all synthesis into a crammed 10-slide container, the deck was iteratively expanded to **16 focused slides** with clean breathing room per slide.

---

## 2. Synthesis Directives & User Constraints

1. **Clean Thai Headings Rule**:
   - All Slide Headings (`# Slide X: ...` and `### Slide X: ...`) MUST NOT contain any English words or parenthetical translations.
   - Example: `# Slide 1: บริบทและข้อกำหนด TOR: ขอบเขตการพัฒนาฐานข้อมูลความสูญเสียและความเสียหาย (TOR §5.3.6–5.3.7)`

2. **Ban `CRDB` & `LDM` Shorthand**:
   - Remove internal Creagy shorthand `CRDB` and `LDM`.
   - Replace with official TOR project title: **"โครงการจัดจ้างที่ปรึกษาพัฒนาระบบฐานข้อมูลด้านการปรับตัวต่อการเปลี่ยนแปลงสภาพภูมิอากาศของประเทศ"** or **"ระบบฐานข้อมูลความสูญเสียและความเสียหาย"** / **"มาตรฐานชุดข้อมูลขั้นต่ำ (MVD)"**.

3. **Executive Mindset Alignment for Architecture & Quality Gates**:
   - **Slide 10 & 11**: Refactored to provide an executive business defense for the 6 core relational tables (Single Source of Truth, GIS layering, Audit trail, Market replacement cost, Economic flow & `Rent_Housing`, Build Back Better budgeting).
   - **Slide 14**: Refactored quality control rules into high-level governance: **"5 ด่านการตรวจสอบคุณภาพ (Quality Validation Gates G1–G5)"**.

4. **De-stressing & Slide Density Management**:
   - Trim subheadings to 1-sentence action takeaways.
   - Split overcrowded slides (e.g. Slide 3 split into Slide 3 & 4; Slide 10 split into Slide 10 & 11).

---

## 3. Final 16-Slide Architecture & Content Mapping

| Slide # | Final Pure Thai Title | Core Focus & Synthesis Output |
| :--- | :--- | :--- |
| **Slide 1** | **บริบทและข้อกำหนด TOR: ขอบเขตการพัฒนาฐานข้อมูลความสูญเสียและความเสียหาย (TOR §5.3.6–5.3.7)** | Scope §5.3.6 & §5.3.7, Climate Act statutory mandate, DCCE budget & timeline context. |
| **Slide 2** | **สภาพการณ์ปัจจุบันของการจัดเก็บข้อมูลภัยพิบัติของกรมป้องกันและบรรเทาสาธารณภัย** | Legal mandate, response reporting chain, fiscal caps constraint on real market valuation. |
| **Slide 3** | **กรอบการทำงานประเมินความต้องการหลังเกิดภัยพิบัติ 4 ระยะ และฐานคิดสากล** | DDPM 4-phase PDNA framework, theoretical Stock vs. Flow definitions. |
| **Slide 4** | **คอขวดเชิงปฏิบัติงานของการประเมินความต้องการหลังเกิดภัยพิบัติในประเทศไทย** | Operational reality gaps, baseline data scarcity, theory vs. practice comparative matrix. |
| **Slide 5** | **ช่องว่างเชิงระบบและการปฏิบัติงาน 4 ประการ** | 4 Key gaps: Fiscal caps, Spatial/Temporal mismatch, Conflation of Damage/Loss, Inter-ministerial silos. |
| **Slide 6** | **การทบทวนมาตรฐานและกรอบแนวคิดสากล** | UNDRR DesInventar, World Bank DaLA, Sendai Framework 2015–2030 targets (A–D). |
| **Slide 7** | **ตารางเปรียบเทียบมาตรฐานสากลกับระบบปัจจุบันของกรมป้องกันและบรรเทาสาธารณภัย** | 4-way comparative matrix (DesInventar vs. DaLA vs. DDPM vs. Proposed MVD). |
| **Slide 8** | **กรอบแนวคิดและการประเมินมูลค่าความสูญเสียและความเสียหายของ สศช.** | NESDC 5 sectors ENUM, GDP baseline alignment, `Rent_Housing` social loss innovation. |
| **Slide 9** | **การตีความใหม่ของแบบฟอร์มจัดเก็บข้อมูลภาคสนามสู่ผลิตภัณฑ์นำเข้าข้อมูล** | Data Ingestion Product concept, empirical physical parameters, central unit cost calculation engine. |
| **Slide 10** | **โครงสร้างฐานข้อมูลความสูญเสียและความเสียหาย แบบ 3 ชั้น** | Rejection of category collapse; Layer A (Event Anchor), Layer B (Valuation), Layer C (Target). |
| **Slide 11** | **เหตุผลเชิงยุทธศาสตร์ที่ผู้บริหารต้องอนุมัติโครงสร้าง 6 ตารางหลัก** | Executive business justification for each table (`DISASTER_EVENT`, `EVENT_LOCATION`, `ASSESSMENT_CONTEXT`, `LD_PHYSICAL_DAMAGE`, `LD_ECONOMIC_LOSS`, `LD_RECOVERY_NEEDS`). |
| **Slide 12** | **กรอบการจัดเก็บข้อมูลระดับเผชิญเหตุและการพิสูจน์ยืนยันภัยพิบัติ** | Incident anchor keys, spatial georeferencing, audit trail time-capsule context. |
| **Slide 13** | **กรอบการประเมินมูลค่าความเสียหายทางกายภาพและความสูญเสียทางเศรษฐกิจ** | Market replacement cost valuation, 5-sector loss modeling, BBB recovery budgeting. |
| **Slide 14** | **ธรรมาภิบาลข้อมูลและระบบควบคุมคุณภาพ 5 ระดับ** | **5 ด่านการตรวจสอบคุณภาพ (G1–G5)** and UNFCCC L&D Fund readiness. |
| **Slide 15** | **ผลการทดสอบมาตรฐานชุดข้อมูลขั้นต่ำย้อนหลังกับ 3 เหตุการณ์ในอดีต** | Pilot findings for พิจิตร (อุทกภัย), ศรีสะเกษ (ภัยแล้ง), ลำปาง (วาตภัย). |
| **Slide 16** | **สรุปช่องว่างเชิงระบบและแผนผังขับเคลื่อนการจัดซื้อจัดจ้างตามกรอบ TOR70** | Root cause analysis & short-, medium-, long-term implementation roadmap for TOR70. |

---

## 4. Deterministic Script Verification

The synthesized deck was validated against the project's quality gates:
1. `lint_thai_writing.py` $\rightarrow$ **Exit Code 0** (Passed style & lexicon check).
2. `check_density.py` $\rightarrow$ **Ratio 0.78** (Passed structural density weight check).
3. `merge_draft.py` $\rightarrow$ **Merged successfully** into [`2026-08-10_WP9_LossDamage_DocuSlide_Deck_TH.md`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRDB/output/09_LDM_LossDamage_DataModel/2026-08-10_WP9_LossDamage_DocuSlide_Deck_TH.md).
