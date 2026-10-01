# Plan slice — บทที่ 7 สรุปรายงาน (full report, new closing chapter)

## Why this chapter exists
Committee comment on the draft final report, item 5.3.11 (checklist `ψ/incubate/DCCE/CRDB/inbox_note/2026-09-23-Checklist การปรับปรุงเล่มร่างรายงานฉบับสมบูรณ์ (Final Report).md`): add one more chapter that summarises the overall report; state the key points of each topic clearly; attach the related PowerPoint files in the appendix.
The item's own wording (CRDB English TOR, `inbox_source/CRDB-TOR.md` line 200): "Prepare a Summary Report containing the Inventories, MVD, Reporting Form, and Recommendations." The Thai inception report adds the policy and technical recommendations for developing the country's data inventories and data products. So the chapter summarises section 5.3 of the report only (not chapter 2, the data structure).
The 5.3.11 wording in `output/2026-05-18_TOR-Review/` is from the TOR70 builder's TOR (infographics, Policy Brief). It is a different item and is not used.

## Job
A short closing chapter that summarises, for the committee and DCCE readers, the four things the TOR names: the two inventories, the minimum data standard (MVD), the reporting form, and the recommendations. It adds no new analysis and states the key points of each part.

## Outline (agreed with Boss 2026-09-30)
- **บทที่ 7 สรุปรายงาน** (opening sentence of purpose, no roadmap)
- 7.1 บัญชีรายการผลิตภัณฑ์ข้อมูลและสารสนเทศ และบัญชีรายการชุดข้อมูลพื้นฐาน
- 7.2 (ร่าง) มาตรฐานชุดข้อมูลขั้นต่ำ (MVD) และ (ร่าง) แบบฟอร์มรายงานความสูญเสียและความเสียหาย
- 7.3 ข้อเสนอแนะเชิงนโยบายและเชิงเทคนิค
- Each part ends with its key points (สาระสำคัญ). Length about 1,000 to 1,500 words in total (Boss).

## Evidence base
| Source | Supplies |
|---|---|
| `ψ/incubate/DCCE/CRDB/output/03_Data_Product_Inventory/Section1.5-final-report-5.3.4.md` | Boss's final summary of the product inventory: 114 products, 56 owners; geographic scope, delivery channels, content types, use cases, sectors, source types, agency concentration; the closing observation about dispersion and missing lineage to source datasets. Contains chart images (base64) that must be skipped |
| `ψ/incubate/DCCE/CRDB/output/03_Data_Product_Inventory/Section3.5-final-report-5.3.5.md` | Boss's final summary of the baseline dataset inventory: 246 datasets, 46 owners; distribution by risk component, owners, file formats, access conditions, sectors and time dimension; the two gaps (content and technical). Same image caution |
| `ψ/incubate/drafts/crdb-full-report-4.2/draft.md` | The draft MVD and reporting form (design principles, structure, data dictionary, application) |
| `ψ/incubate/drafts/crdb-full-report-4.3/draft.md` | The pilot collection against the MVD (method, availability scoring, results, systemic findings, recommendations) |
| `ψ/incubate/drafts/crdb-full-report-6/Chapter6-report.md` | The recommendations (6.1 blueprint, 6.2 supporting information, 6.3 roadmap), file of record accepted by Boss |
| `ψ/incubate/drafts/crdb-full-report-3.1-v3/draft.md` | Accepted reference sample for voice and citation form |

## Session rules
- Actor: คณะที่ปรึกษา. First mention กรมการเปลี่ยนแปลงสภาพภูมิอากาศและสิ่งแวดล้อม, then กรม สส. only.
- Altitude: full report, but a summary. Key points, not full method.
- **Numbers follow Boss's two files** (114 products, 56 owners; 246 datasets, 46 owners). Where 3.4, 5.1 or chapter 6 disagree (they still say 260 datasets), chapter 7 follows the two files and the mismatches are listed separately for Boss (Boss's decision).
- **Gap wording is allowed as in the source files** (Boss): state the content gap and the technical gap once, as summarised there. No new gap analysis, no demand-supply matching.
- No TOR numbers, file names, codes or internal notes in the text; refer to other parts of the report by section number of the report. The source files themselves say "ขอบเขตงาน 5.3.4/5.3.5"; do not carry that over.
- Boss's standing writing rules: plain words, no consultant jargon, no colon-driven sentences, no "instead of X, do Y" contrasts, no audit tone, no empty intensifiers.
- Cite through footnotes in the form `[^n]` only where an external source is named (as in 3.1). Cross-references to other chapters are by section number, no footnote.
- The PowerPoint appendix is not part of this chapter's prose. It is listed separately (FGD3 2 July 2026 deck, final dissemination event deck, and the MVD slide document and executive briefing HTML/PDF).
- Ledgers are not touched.
- Execution: Stage 1 `th-argument-mapper` (fresh); Stage 3 the `thai-writer` agent (Boss's instruction); Stage 5 fresh `th-editorial-reviewer`.
