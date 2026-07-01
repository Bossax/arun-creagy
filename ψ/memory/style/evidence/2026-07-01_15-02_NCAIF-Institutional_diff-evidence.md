# Style Edit Evidence: NCAIF-Institutional
- **Date**: 2026-07-01 15:02 +07:00
- **Session ID**: `833c4e75-4706-473b-b379-0c4773f7c5df`
- **Source Mode**: `In-Place Git Diff`
- **File Path**: [[ψ/incubate/DCCE/CRDB/output/final_report/5.3/5.3.8 วิเคราะห์ช่องว่างระหว่างอุปทานและอุปสงค์ของข้อมูล โดยการนำผลการสังเคราะห์ความต้องการใช้ข้อมูล มาเปรียบเทียบกับบัญชีรายการผลิตภัณฑ์ข้อมูลสารสนเทศและชุดข้อมูลที่มีอยู่ เพื่อวิเคราะห์หาช่องว่าง (Gap Analysis) ทั้งในเชิงปริมาณและเชิงคุณภาพ|5.3.8 วิเคราะห์ช่องว่างระหว่างอุปทานและอุปสงค์ของข้อมูล โดยการนำผลการสังเคราะห์ความต้องการใช้ข้อมูล มาเปรียบเทียบกับบัญชีรายการผลิตภัณฑ์ข้อมูลสารสนเทศและชุดข้อมูลที่มีอยู่ เพื่อวิเคราะห์หาช่องว่าง (Gap Analysis) ทั้งในเชิงปริมาณและเชิงคุณภาพ]]]

---

## 1. Concrete Diff Highlights

| Original / Committed | Human Edited | Typology |
| :--- | :--- | :--- |
| `DCCE` | `กรมฯ` | Abbreviation Standardisation |
| `use case` | `กรณีการใช้งาน` | English Jargon Translation |
| `workflow` | `ระบบงานจริง` / `การดำเนินงานจริง` | Jargon Naturalisation |
| `raster หรือขนาดกริด` | `ขนาดกริด` | Redundancy Removal |
| `ระดับกิโลเมตร` | `ระดับกริด 25 กิโลเมตร` / `ระดับความละเอียดที่ 5 กิโลเมตร` | Precision Enhancement |
| `interoperability` / `usability` | *Omitted, explained via operational realities* | Jargon Elimination |
| `เพื่อทำให้เห็นอย่างเป็นระบบว่า` | `เพื่อทำความเข้าใจต่อสถานการณ์...` | Institutional Voice Alignment |
| `lag time` | ` lag time... คาดหวังว่าข้อมูลจะเข้าสู่ระบบหลังจากผ่านเหตุการณ์ไปนานเท่าใด` | Clarification Translation |

---

## 2. Tone and Style Shift

* **Naturalizing English Jargon**: Replaced direct English nouns (`use case`, `workflow`, `raster`, `interoperability`, `usability`, `lag time`) with functional Thai policy terminology to fit the target audience of Thai public agencies.
* **Standardizing Abbreviations**: Substituted `DCCE` (the acronym) with `กรมฯ` (the standard official shorthand for the Department of Climate Change and Environment in Thai reports).
* **Quantifying Gaps with High Technical Depth**: Instead of making generic statements about "kilometer-scale projection gaps," specified the precise resolutions (25 km grid size vs the new 5 km statistical downscaling) and detailed the parameters (Precipitation, Max/Min/Mean Temperatures) and scenarios (SSP2-4.5, SSP5-8.5).
* **Transition from Dense Prose to Structured Lists**: Reformatted dense descriptive paragraphs into numbered sequences (`1)`, `2)`, `3)`) to match clean, scannable public policy report standards.

---

## 3. Candidate Rules

* **Rule 1 (No English Jargon)**: Banish direct English terms such as `use case`, `workflow`, and `interoperability` from main policy summaries. Substitute them with functional Thai descriptors:
  * `use case` -> `กรณีการใช้งาน`
  * `workflow` -> `ขั้นตอนการทำงาน` / `ระบบงานจริง` / `กระบวนงาน`
* **Rule 2 (DCCE -> กรมฯ)**: Refer to the department as `กรมฯ` rather than `DCCE` when writing public-facing Thai report prose.
* **Rule 3 (Technical Baseline Specification)**: Never leave gaps descriptive or vague. When writing about climate models or projection downscaling, explicitly state the resolutions (e.g. `25 กิโลเมตร`, `5 กิโลเมตร`), variables (Precipitation, Temperatures), and scenarios (SSP2-4.5, SSP5-8.5).
