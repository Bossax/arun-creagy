# WP4 Content Source Gap Analysis — Sitemap Requirement Items vs. DCCE Digital Asset Inventory

Date: 2026-08-10

Fresh matching exercise between the 73 rows of `wp4-requirement-items-v8.csv` (sitemap content requirements) and the 391 rows of `DCCE_Unified_Digital_Asset_Database.csv` (DCCE's current digital asset inventory). Matching is topical relevance only (title/description/tags/owner) — no judgment is made on whether a matched asset's actual content is ready to use or needs rework, since full asset content was not read. Note: the task brief described the requirement-items file as having 63 rows; the file as delivered has 73 data rows (1 header + 73), and this analysis processes all 73 rows found in the file, since it is the authoritative full list per the task instructions.

**2026-08-10 addendum — sub-topic leak audit.** Sanity-sampling by Boss found that several requirement items are compound (they name multiple distinct sub-topics in one line, e.g. "non-economic losses: mental health, biodiversity, cultural heritage"), and the original pass marked the whole item "matched" the moment *any one* sub-topic found an asset. A follow-up pass re-examined all 39 originally-matched rows against their asset rationale and the original sitemap text, and split them into **FULL** (single-topic item, or every named sub-topic covered) vs. **PARTIAL** (some sub-topics covered, others explicitly named as missing, or the matched asset is a weak/self-flagged proxy rather than a real source). The `coverage_completeness` and `uncovered_subtopics` columns in the CSV reflect this; the 34 zero-match rows were not re-examined (already at the floor). Revised true picture: **20 FULL / 19 PARTIAL / 34 GAP**, not the original binary 39/34.

Priority flag heuristic: sitemap requirement items whose btr_tag begins with '1' (institutional arrangements) or '4' (climate finance/budget tracking) are flagged A-BTR, since national institutional-arrangement and finance-tracking content is exactly what Thailand's Biennial Transparency Report (BTR) national reporting chapters require. Items whose btr_tag begins with '5' (the sitemap's own Loss & Damage chapter) are flagged disaster-loss-statistics. This is an inference from the btr_tag numbering pattern in the source CSV, not an explicit label in the data — flagged here for human review.

## Per-node rollup (revised — three-way split)

| node_id | node_title | # items | # full | # partial | # gap |
|---|---|---:|---:|---:|---:|
| SIT-1.1.1 | ภาพรวมความเสี่ยงจากการเปลี่ยนแปลงสภาพภูมิอากาศในประเทศไทย | 4 | 1 | 0 | 3 |
| SIT-1.1.2 | ความเสี่ยงสำคัญ และลำดับความสำคัญในการปรับตัวของประเทศไทย | 3 | 3 | 0 | 0 |
| SIT-1.2 | สืบค้นข้อมูลรายพื้นที่ | 3 | 1 | 1 | 1 |
| SIT-2.1 | สถานการณ์การเปลี่ยนแปลงสภาพภูมิอากาศของประเทศ | 3 | 1 | 1 | 1 |
| SIT-2.2 | สรุปโปรไฟล์ของความเสี่ยงรายพื้นที่และรายภาคส่วน | 2 | 1 | 0 | 1 |
| SIT-2.3 | เครื่องมือทางนโยบาย กฎหมาย และการเงิน | 3 | 1 | 0 | 2 |
| SIT-2.3.1 | แหล่งทุนและการติดตามงบประมาณปรับตัว | 4 | 0 | 2 | 2 |
| SIT-2.3.2 | กลไกเชิงสถาบันและการประสานงาน | 4 | 3 | 0 | 1 |
| SIT-2.4 | บริการข้อมูลสำหรับการวางแผน | 3 | 2 | 1 | 0 |
| SIT-3.1.1 | ข้อมูลสังเกตุการณ์ | 3 | 0 | 1 | 2 |
| SIT-3.1.2 | ปัจจัยขับเคลื่อนทางภูมิอากาศ | 3 | 0 | 0 | 3 |
| SIT-3.1.3 | ฉากทัศน์ภูมิอากาศในอนาคต | 2 | 0 | 0 | 2 |
| SIT-3.2.1 | การวิเคราะห์ความเปราะบางและการเปิดรับภัย | 2 | 0 | 1 | 1 |
| SIT-3.2.2 | การวิเคราะห์ความเสี่ยง | 2 | 0 | 2 | 0 |
| SIT-3.2.2.1 | การติดตามภัยคุกคามที่เกิดขึ้นช้า | 4 | 0 | 1 | 3 |
| SIT-3.2.3 | ผลกระทบลูกโซ่ | 2 | 1 | 1 | 0 |
| SIT-3.2.4 | ความสูญเสียและความเสียหาย | 3 | 0 | 3 | 0 |
| SIT-3.2.5 | กรอบทฤษฎีและเอกสารคู่มือ | 1 | 0 | 1 | 0 |
| SIT-3.3.1 | แนวทางการวางแผนและการออกแบบโครงการแบบมีส่วนร่วม | 4 | 0 | 1 | 3 |
| SIT-3.3.2 | เส้นทางกลยุทธ์การปรับตัวของประเทศ | 4 | 1 | 1 | 2 |
| SIT-3.3.3 | ห้องสมุดมาตรการปรับตัวตามสาขา | 2 | 0 | 1 | 1 |
| SIT-3.3.4 | กรณีศึกษาการวางแผนการปรับตัว | 1 | 0 | 0 | 1 |
| SIT-3.3.5 | โครงการที่กำลังดำเนินการ | 2 | 0 | 0 | 2 |
| SIT-3.4.1 | แนวทางการติดตามและประเมินผลการปรับตัว | 2 | 1 | 0 | 1 |
| SIT-3.4.2 | ระบบฐานข้อมูลด้านการติดตามและประเมินผลของประเทศไทย | 1 | 1 | 0 | 0 |
| SIT-3.4.3 | กรณีศึกษาโครงการปรับตัวที่ประสบความสำเร็จ | 1 | 1 | 0 | 0 |
| SIT-4.1 | บัญชีข้อมูล | 1 | 1 | 0 | 0 |
| SIT-4.2 | Visualization and Analytics Application | 1 | 0 | 1 | 0 |
| SIT-4.3 | ศูนย์รวมเครื่องมือและแหล่งข้อมูลภายนอก | 1 | 0 | 0 | 1 |
| SIT-5.1 | ประกาศและกิจกรรมการมีส่วนร่วม | 1 | 1 | 0 | 0 |
| SIT-5.2 | ช่องทางการรับฟังข้อคิดเห็นและบริการผู้ใช้ | 1 | 0 | 0 | 1 |

## Sub-topic Leaks — items marked "matched" that are actually only partially covered

These 19 rows have at least one asset, but the requirement names something specific the matched asset(s) do not actually cover. A developer relying on the "matched" label alone would build these pages assuming full source coverage and be wrong.

| node_id | requirement_item | matched_asset_ids | uncovered_subtopics |
|---|---|---|---|
| SIT-1.2 | Quick-view Dashboard (vulnerability cards, threats, recommended measures) | SYS-003 | No dedicated dashboard product exists — general risk-map app is a stretch. |
| SIT-2.1 | Macroeconomic Loss & Damage Database | PUB-026;MED-050 | No actual structured database — only a fund page and one static report. |
| SIT-2.3.1 | Funding source list + CBA guide for สตง. budget justification | MED-079;PUB-027;PUB-028;PUB-029 | Cost-benefit/สตง. budget-justification guide not covered. |
| SIT-2.3.1 | GCF/AF/GEF + technology/technical-assistance tracking | PUB-027;PUB-028;PUB-029;DAT-054;MED-147 | Technology transfer / technical-assistance tracking not covered, financial aid only. |
| SIT-2.4 | Local Vulnerability & Adaptive Capacity Indices | MED-015 | No actual index dataset — explainer methodology only. |
| SIT-3.1.1 | ENSO & AMOC monitoring | MED-105 | AMOC not covered; ENSO covered by a general-audience explainer only, not a data feed. |
| SIT-3.2.1 | Exposure, Sensitivity, Adaptive Capacity, Resilience definitions | DAT-014;MED-015 | Sensitivity and Resilience not explicitly covered, only Vulnerability/Adaptive Capacity. |
| SIT-3.2.2 | National risk-assessment framework/steps | PUB-012;MED-125 | No purpose-built standard document — impact-chain manual is a proxy. |
| SIT-3.2.2 | Sectoral risk: food, water, heat-health, SME disruption | DAT-005;MED-004;MED-033 | SME business-disruption risk not covered; heat-specific health impact unclear. |
| SIT-3.2.2.1 | Coastal erosion / beach-loss statistical index | MED-127…137 (9 infographics) | Narrative infographics only, not a quantitative statistical index. |
| SIT-3.2.3 | Impact-chain case study, agriculture + urban settlement | MED-048 | Agriculture-sector case study not represented, only urban/flood (Hat Yai). |
| SIT-3.2.4 | UNFCCC Loss & Damage theoretical framework | PUB-026 | No dedicated framework doc — matched asset is a funding-mechanism page. |
| SIT-3.2.4 | Economic/physical loss dashboard | MED-050 | Static PDF report only, not dashboard-ready data. |
| SIT-3.2.4 | Non-economic losses: mental health, biodiversity, cultural heritage | MED-108;MED-150 | Mental health and cultural heritage loss not covered, biodiversity only. |
| SIT-3.2.5 | L&D calculation methodology manual | PUB-012;MED-125 | No dedicated L&D calculation manual — impact-chain manual is a proxy. |
| SIT-3.3.1 | Vulnerable-group protection: children, elderly, disabled, border/coastal communities | MED-002 | None of the four named groups specifically covered — asset is only topically adjacent. |
| SIT-3.3.2 | Financial + technology + capacity-building support needs | MED-079;PUB-027;PUB-028;PUB-029 | Technology and capacity-building support not covered, financial only. |
| SIT-3.3.3 | Grey Infrastructure + Nature-based Solutions measures | DAT-022;MED-042;VID-036 | Grey/structural infrastructure not covered at all, NBS only. |
| SIT-4.2 | Visualization tool with IDF/design-curve engineering outputs | SYS-003;DAT-005 | No IDF/design-curve engineering outputs exist — core deliverable is absent. |

## Real Gaps — requirement items with zero topically-relevant assets in the current inventory

These are the items where nothing in DCCE's 391-asset inventory is even topically relevant. A developer starting on these sitemap pages has no existing DCCE source material to draw from and will need new data collection, a new methodology document, or an external data source.

**34 of 73 requirement items are gaps.**

| node_id | requirement_item | btr_tag | priority_flag |
|---|---|---|---|
| SIT-1.1.1 | ประวัติศาสตร์และแนวโน้มภัยธรรมชาติของประเทศ |  |  |
| SIT-1.1.1 | ความเข้าใจความเสี่ยงทางกายภาพ (Physical Risk) และความเสี่ยงจากการเปลี่ยนผ่าน (Transition Risk) | 2, MUST |  |
| SIT-1.1.1 | แผนภาพและบัตรข้อมูลสรุปความเสี่ยงระดับชาติ (National Risk Profile Summary Cards) |  |  |
| SIT-1.2 | Search Hierarchy: รองรับการค้นหารายระดับการปกครอง (จังหวัด -> อำเภอ -> ตำบล) |  |  |
| SIT-2.1 | สถิติเหตุการณ์อากาศสุดขั้วในอดีต (อุณหภูมิสูงสุด-ต่ำสุด สถิติปริมาณฝนสะสม) |  |  |
| SIT-2.2 | สรุปโปรไฟล์ความเสี่ยงและความเปราะบางรายพื้นที่ (รายภูมิภาค 77 จังหวัด และระดับท้องถิ่น/อปท.) | 2, MUST |  |
| SIT-2.3 | สรุปมาตรการทางกฎหมายและนโยบายที่ส่งเสริมการปรับตัว (พ.ร.บ. ป้องกันและบรรเทาสาธารณภัย กฎกระทรวงผังเมือง) | 1, MUST | A-BTR |
| SIT-2.3 | ระบบรับรองความเป็นทางการของเครื่องมือการวิเคราะห์การหลีกเลี่ยงความสูญเสีย (Avoided Losses Certification Model) | 3, MUST |  |
| SIT-2.3.1 | รายงานสถิติการจัดสรรงบประมาณแผ่นดินสำหรับการปรับตัวและ Climate Budget Tagging | 4, SHOULD | A-BTR |
| SIT-2.3.1 | การประเมินและการดึงดูดการมีส่วนร่วมของภาคการเงินและภาคเอกชนในการจัดหาทุนเพื่อการปรับตัว | 4, SHOULD | A-BTR |
| SIT-2.3.2 | กลไกการประสานงานและบูรณาการการดำเนินงานปรับตัวระหว่างหน่วยงานรัฐระดับชาติและระดับท้องถิ่น (อปท.) | 1, MUST | A-BTR |
| SIT-3.1.1 | ชุดข้อมูลสภาพอากาศรายสถานีสังเกตการณ์ระยะสั้นและระยะกลาง (ความร่วมมือกรมอุตุนิยมวิทยา) |  |  |
| SIT-3.1.1 | ชุดข้อมูลสังเกตการณ์ผ่านดาวเทียม (พื้นที่ป่าไม้ Land Cover แหล่งน้ำ แนวปะการังฟอกขาว) | 2, MUST |  |
| SIT-3.1.2 | ข้อมูล Climatology และตัวแปรทางสภาพภูมิอากาศที่สำคัญ (Temperature trends Rainfall intensity changes) | 2, MUST |  |
| SIT-3.1.2 | คู่มือและบทอธิบายการใช้งานฉากทัศน์ภูมิอากาศ (Climate Scenarios) |  |  |
| SIT-3.1.2 | คลังชุดข้อมูลคาดการณ์อนาคตความละเอียดสูงระดับประเทศ (Downscaled climate projections) | 2, MUST |  |
| SIT-3.1.3 | มาตรฐานการบริหารจัดการความไม่แน่นอนและแนวทางการเลือกชุดข้อมูลคาดการณ์อนาคต (National Climate Uncertainty Governance Standard) | 2, MUST |  |
| SIT-3.1.3 | ตัวอย่างกรณีศึกษาการประยุกต์ใช้แบบจำลองคาดการณ์สภาพภูมิอากาศในการวางแผนกลยุทธ์ระยะยาว |  |  |
| SIT-3.2.1 | คลังแบบจำลองฟังก์ชันความเสียหาย (Damage Functions) รายภาคส่วนสำหรับการประเมินภัย | 2, MUST |  |
| SIT-3.2.2.1 | รายงานสถิติและการประเมินภัยคุกคามระยะยาวที่เกิดขึ้นอย่างช้าๆ (การเพิ่มขึ้นของอุณหภูมิเฉลี่ย การเปลี่ยนแปลงคาบการกระจายน้ำฝน) | 5, MUST | disaster-loss-statistics |
| SIT-3.2.2.1 | ข้อมูลอัตราการเพิ่มขึ้นของระดับน้ำทะเล (Sea-Level Rise) ตลอดแนวชายฝั่งไทยและบริเวณอ่าวไทย | 5, MUST | disaster-loss-statistics |
| SIT-3.2.2.1 | ข้อมูลการทรุดตัวของแผ่นดิน (Land Subsidence) ในเขตกรุงเทพมหานครและปริมณฑล และการหนุนของน้ำเค็ม (Salinity Intrusion) | 5, MUST | disaster-loss-statistics |
| SIT-3.3.1 | ระเบียบวิธีประเมินต้นทุนและผลประโยชน์ (Cost-Benefit Analysis) และ Avoided Losses Calculus | 3, MUST |  |
| SIT-3.3.1 | แนวปฏิบัติการบูรณาการมิติด้านเพศวิถี ความเท่าเทียมทางเพศ และสิทธิมนุษยชนในมาตรการปรับตัว (GESI) | 3, SHOULD |  |
| SIT-3.3.1 | การประยุกต์ใช้ภูมิปัญญาท้องถิ่น องค์ความรู้ดั้งเดิม และมรดกทางวัฒนธรรมในการปรับตัวของชุมชน | 3, SHOULD |  |
| SIT-3.3.2 | รายงานอุปสรรคเชิงระบบจำแนกรายสาขา (Systemic Barriers: ข้อจำกัดด้านข้อมูล ปัญหาการประสานงานเชิงสถาบัน อุปสรรคด้านทรัพยากรการเงิน) | 3, MUST |  |
| SIT-3.3.2 | ความต้องการการพัฒนาบุคลากรในการเขียนข้อเสนอโครงการเพื่อขอรับทุนสนับสนุนภูมิอากาศโลก | 3, SHOULD |  |
| SIT-3.3.3 | ระบบสืบค้นและคัดกรองมาตรการเชิงเทคนิคและนโยบาย (Searchable Database) จำแนกตามภัย ภาคส่วน และงบประมาณ |  |  |
| SIT-3.3.4 | คลังข้อมูลแผนจัดการความเสี่ยงสภาพภูมิอากาศและนโยบายเชิงสถาบันของท้องถิ่นและภาคเอกชน |  |  |
| SIT-3.3.5 | ระบบติดตามสถานะและการดำเนินงานโครงการปรับตัวของประเทศ (โครงการประกันภัยพืชผล Agri-Map การปรับปรุงโครงสร้างควบคุมน้ำ) | 4, SHOULD | A-BTR |
| SIT-3.3.5 | ตัวชี้วัดความพร้อมของโครงการงบประมาณ |  |  |
| SIT-3.4.1 | กรอบการวิเคราะห์ระดับความก้าวหน้าทางเทคโนโลยีและนวัตกรรมปรับตัว (Technology Readiness Levels) | 4, SHOULD | A-BTR |
| SIT-4.3 | จุดเชื่อมต่อไปยังพอร์ทัลข้อมูลระดับสากลและพอร์ทัลเฉพาะทาง (TMD Weather API GISTDA Geo-Informatics Portal Copernicus Climate Data Store) |  |  |
| SIT-5.2 | แพลตฟอร์มรับเสียงสะท้อนจากหน่วยงานผู้ใช้งานในแบบที่เป็นระบบเพื่อปรับปรุงคุณภาพชุดข้อมูล ขยายขอบเขตการบริการ และทวนสอบการตอบสนองความต้องการเชิงสถาบัน |  |  |

## Totals

Original binary split: 39 of 73 requirement items matched to at least one existing DCCE asset; 34 are gaps.

Revised three-way split (after sub-topic leak audit):
- **20 of 73 (27%) — FULL**: genuinely ready to source from what's matched.
- **19 of 73 (26%) — PARTIAL**: some real source material exists, but a specifically-named part of the requirement is still missing (see Sub-topic Leaks table above).
- **34 of 73 (47%) — GAP**: nothing topically relevant in the current 391-asset inventory (unchanged from the original pass).

So only 27% of the sitemap's content requirements are actually fully sourced today — the original "39 matched" figure overstated readiness by counting every PARTIAL row as if it were FULL.