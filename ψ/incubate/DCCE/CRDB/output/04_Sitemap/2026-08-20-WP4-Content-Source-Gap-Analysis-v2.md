# WP4 Content Source Gap Analysis v2 — Sitemap Requirement Items vs. DCCE Digital Asset Inventory

Date: 2026-08-20
Supersedes: `2026-08-10-WP4-Content-Source-Gap-Analysis.md` + `.csv` (D-061)
Companion node list: `NCAIF_Detailed_Sitemap_v9.md` (D-075)

## What changed from v1, and why

This is a **delta pass**, not a full re-extraction. Per Boss's decision this session, matched assets, rationale, and coverage ratings for every requirement item v9 left untouched are carried forward unchanged from v1 — only items actually affected by the v8→v9 restructuring were touched. Four kinds of change:

1. **Removed (3 items).** Section 2.4 collapsed to a pure router link in v9 (no longer a content hub — Boss's decision this session, see D-075). Its three requirement items (local vulnerability index, integrated spatial risk map, data-security guidance) are dropped; the underlying capabilities they gestured at are already covered elsewhere (2.2's profile content, 1.2/4's shared risk map, Section 4/5.2's governance references).
2. **Re-parented (6 items), no new research.** A node-assignment fix and two structural merges, all mechanical: (a) one item mis-tagged `SIT-3.1.2` in v1 that actually belongs under `SIT-3.1.3` per both v8 and v9 text ("explainer on using climate scenarios"); (b) 3.3.5's two project-tracking items moved to `SIT-3.4.2`, since v9 merges Project Tracking Status into the Adaptation M&E Platform (3.3.5 is now a pointer, not a second description); (c) Section 4's three sub-node items (4.1/4.2/4.3) re-parented to flat `SIT-4`, since v9 removes the 4.1/4.2/4.3 split entirely in favor of one tag-filterable tool grid.
3. **New items requiring fresh registry matching (3 items).** The three restored-from-v6 content items with no prior v1 row: 2.3's NAP Implementation Status, 3.1.3's climate-scenario data-source pointer, 3.2.2's other-risk-assessment-sources pointer. Matched against `DCCE_Unified_Digital_Asset_Database.csv` this session (see table below).
4. **New items, unvalidated (2 items).** Section 4's two mockup-sourced tool cards (Climate Impact Explorer, Adaptation Options Explorer) have no Layer 1/2 requirement behind them at all — they were invented during mockup production, not extracted from the original 73-item pass. Logged here as GAP with a flag for Phase 3's DRD update to decide whether they become real deliverables or get cut.

One item's wording was widened without changing its match: 2.3.1's finance-directory item now explicitly includes "พร้อมกรณีศึกษาการใช้งานจริง" (with real-usage case studies), restoring v6's case-study emphasis v8 had dropped. The existing PARTIAL rating and matched assets (fund directories/guides, not case-study documents) already covered this honestly, so only the requirement text and uncovered-subtopics note were updated.

**A pre-existing inconsistency found and corrected in passing:** v1's own `.md` rollup table claimed a 20 FULL / 19 PARTIAL / 34 GAP split, but v1's `.csv` — the source of truth, including the 2026-08-10 addendum's sub-topic-leak reclassification — actually tallies to **18 FULL / 25 PARTIAL / 30 GAP**. The `.md` table was written before the addendum's reclassification was applied to the CSV and never regenerated. This v2 report's tables are computed directly from the v2 CSV (script-generated, not hand-transcribed), so this can't recur silently.

**Total: 73 → 75 requirement items** (73 − 3 removed + 5 new).

## Per-node rollup

| node_id | node_title | # items | # full | # partial | # gap |
|---|---|---:|---:|---:|---:|
| SIT-1.1.1 | ภาพรวมความเสี่ยงจากการเปลี่ยนแปลงสภาพภูมิอากาศในประเทศไทย | 4 | 1 | 1 | 2 |
| SIT-1.1.2 | ความเสี่ยงสำคัญ และลำดับความสำคัญในการปรับตัวของประเทศไทย | 3 | 3 | 0 | 0 |
| SIT-1.2 | สืบค้นข้อมูลรายพื้นที่ | 3 | 0 | 1 | 2 |
| SIT-2.1 | สถานการณ์การเปลี่ยนแปลงสภาพภูมิอากาศของประเทศ | 3 | 0 | 2 | 1 |
| SIT-2.2 | สรุปโปรไฟล์ของความเสี่ยงรายพื้นที่และรายภาคส่วน | 2 | 0 | 1 | 1 |
| SIT-2.3 | เครื่องมือทางนโยบาย กฎหมาย และการเงิน | 4 | 1 | 1 | 2 |
| SIT-2.3.1 | แหล่งทุนและการติดตามงบประมาณปรับตัว | 4 | 0 | 2 | 2 |
| SIT-2.3.2 | กลไกเชิงสถาบันและการประสานงาน | 4 | 3 | 0 | 1 |
| SIT-3.1.1 | ข้อมูลสังเกตุการณ์ | 3 | 0 | 1 | 2 |
| SIT-3.1.2 | ปัจจัยขับเคลื่อนทางภูมิอากาศ | 2 | 0 | 2 | 0 |
| SIT-3.1.3 | ฉากทัศน์ภูมิอากาศในอนาคต | 4 | 0 | 1 | 3 |
| SIT-3.2.1 | การวิเคราะห์ความเปราะบางและการเปิดรับภัย | 2 | 0 | 1 | 1 |
| SIT-3.2.2 | การวิเคราะห์ความเสี่ยง | 3 | 0 | 2 | 1 |
| SIT-3.2.2.1 | การติดตามภัยคุกคามที่เกิดขึ้นช้า | 4 | 0 | 2 | 2 |
| SIT-3.2.3 | ผลกระทบลูกโซ่ | 2 | 1 | 1 | 0 |
| SIT-3.2.4 | ความสูญเสียและความเสียหาย | 3 | 0 | 3 | 0 |
| SIT-3.2.5 | กรอบทฤษฎีและเอกสารคู่มือ | 1 | 0 | 1 | 0 |
| SIT-3.3.1 | แนวทางการวางแผนและการออกแบบโครงการแบบมีส่วนร่วม | 4 | 0 | 1 | 3 |
| SIT-3.3.2 | เส้นทางกลยุทธ์การปรับตัวของประเทศ | 4 | 1 | 1 | 2 |
| SIT-3.3.3 | ห้องสมุดมาตรการปรับตัวตามสาขา | 2 | 0 | 1 | 1 |
| SIT-3.3.4 | กรณีศึกษาการวางแผนการปรับตัว | 1 | 0 | 0 | 1 |
| SIT-3.4.1 | แนวทางการติดตามและประเมินผลการปรับตัว | 2 | 2 | 0 | 0 |
| SIT-3.4.2 | ระบบฐานข้อมูลด้านการติดตามและประเมินผลของประเทศไทย | 3 | 1 | 0 | 2 |
| SIT-3.4.3 | กรณีศึกษาโครงการปรับตัวที่ประสบความสำเร็จ | 1 | 1 | 0 | 0 |
| SIT-4 | เครื่องมือและบริการสารสนเทศด้านภูมิอากาศ | 5 | 1 | 1 | 3 |
| SIT-5.1 | ประกาศและกิจกรรมการมีส่วนร่วม | 1 | 1 | 0 | 0 |
| SIT-5.2 | ช่องทางการรับฟังข้อคิดเห็นและบริการผู้ใช้ | 1 | 0 | 0 | 1 |

(SIT-2.4 no longer appears — collapsed to a router link, no content requirements of its own.)

## New items matched this session (delta-only scope)

| node_id | requirement_item | matched_asset_ids | rationale |
|---|---|---|---|
| SIT-2.3 | สถานะการดำเนินการตามแผนการปรับตัวระดับชาติ (NAP Implementation Status) | DAT-014 | DCCE's live Adaptation M&E dataset is tagged NAP among its keywords and tracks progress annually — same asset already backing 3.4.1/3.4.2 — but it's the general M&E platform, not a NAP-plan-progress tracker specifically. PARTIAL. |
| SIT-3.1.3 | แหล่งข้อมูล climate scenario | DCCE_2_11;DCCE_2_16;DCCE_2_17;DCCE_2_18;DCCE_2_19 | Same downscaled climate-projection datasets already backing 3.1.2's projections item — this is a pointer to that same data, not a separate dataset. PARTIAL. |
| SIT-3.2.2 | แหล่งข้อมูลผลการประเมินความเสี่ยงอื่นๆ | GAP | No directory of "other risk-assessment sources/pointers" exists as a distinct asset. GAP. |
| SIT-4 | ตัวสำรวจผลกระทบภูมิอากาศ (Climate Impact Explorer) | GAP | Mockup-sourced, no Layer 1/2 requirement or DRD deliverable behind it — flagged for Phase 3's DRD review. GAP. |
| SIT-4 | ตัวสำรวจมาตรการปรับตัว (Adaptation Options Explorer) | GAP | Mockup-sourced, no Layer 1/2 requirement or DRD deliverable behind it — flagged for Phase 3's DRD review. GAP. |

## Sub-topic Leaks — items with at least one matched asset that don't fully cover what's named

| node_id | requirement_item | matched_asset_ids | uncovered_subtopics |
|---|---|---|---|
| SIT-1.1.1 | National Risk Profile Summary Cards | DCCE_3_1…3_7 | Composite index data exists but is unverified/draft, not a rendered summary-card UI. |
| SIT-1.2 | Quick-view Dashboard | SYS-003 | No dedicated dashboard product — general risk-map app is a stretch. |
| SIT-2.1 | Extreme-event historical statistics | DCCE_2_1;DCCE_2_2 | Raw historical grids exist but need aggregation into event statistics; access Restricted. |
| SIT-2.1 | Macroeconomic Loss & Damage Database | PUB-026;MED-050 | No actual structured database — only a fund page and one static report. |
| SIT-2.2 | 6-sector risk profiles | DAT-005;DAT-014 | (carried from v1, unchanged) |
| SIT-2.3 | NAP Implementation Status *(new)* | DAT-014 | No NAP-plan-progress tracker distinct from the general M&E platform; restored from v6 this session. |
| SIT-2.3.1 | Fund directory + case studies + สตง. CBA guide | MED-079;PUB-027;PUB-028;PUB-029 | CBA/สตง. guide not covered; case-study documents (restored from v6) also not covered — matched assets are directories/guides only. |
| SIT-2.3.1 | GCF/AF/GEF + tech/technical-assistance tracking | PUB-027;PUB-028;PUB-029;DAT-054;MED-147 | Technology transfer / technical-assistance tracking not covered, financial aid only. |
| SIT-3.1.1 | ENSO & AMOC monitoring | MED-105 | AMOC not covered; ENSO only a general-audience explainer, not a data feed. |
| SIT-3.1.2 | Climatology/temperature/rainfall variables | DCCE_2_1;DCCE_2_2 | Raw grid data exists; trend-derivation still needed. Access Restricted. |
| SIT-3.1.2 | Downscaled climate projections | DCCE_2_11;DCCE_2_16-19 | Real data through 2099 at national (not sub-national) resolution, Restricted access. |
| SIT-3.1.3 | Climate scenario data source *(new)* | DCCE_2_11;DCCE_2_16-19 | Same dataset/caveats as 3.1.2's projections item; restored from v6 this session. |
| SIT-3.2.1 | Exposure/Sensitivity/Adaptive Capacity/Resilience definitions | DAT-014;MED-015 | Sensitivity and Resilience only implicitly covered. |
| SIT-3.2.2 | National risk-assessment framework/steps | PUB-012;MED-125 | No purpose-built standard document — impact-chain manual is a proxy. |
| SIT-3.2.2 | Sectoral risk (food/water/heat-health/SME) | DAT-005;MED-004;MED-033 | SME disruption not covered; heat-specific health impact unclear. |
| SIT-3.2.2.1 | Sea-level rise data | MD_1_2 | Raw annual readings, not a derived rate-of-rise statistic; access Restricted. |
| SIT-3.2.2.1 | Coastal erosion statistical index | MED-127…137;DMCR_1_1;DMCR_4_1 | Real area-based erosion data exists but is raw figures, not a pre-built statistical index. |
| SIT-3.2.3 | Impact Chain case study, agriculture + urban | MED-048 | Agriculture case study missing — only urban/flood (Hat Yai) covered. |
| SIT-3.2.4 | UNFCCC L&D theoretical framework | PUB-026 | No dedicated framework doc — matched asset is a funding-mechanism page. |
| SIT-3.2.4 | Economic/physical loss dashboard | MED-050;DDPM_3_2;DDPM_2_3;RFD_1_2 | Real per-hazard loss records exist but nothing aggregates them into one dashboard. |
| SIT-3.2.4 | Non-economic losses (mental health/biodiversity/heritage) | MED-108;MED-150 | Mental health and cultural heritage not covered, biodiversity only. |
| SIT-3.2.5 | L&D calculation methodology manual | PUB-012;MED-125 | No dedicated L&D calculation manual — impact-chain manual is a proxy. |
| SIT-3.3.1 | Vulnerable-group protection (children/elderly/disabled/border-coastal) | MED-002 | None of the four named groups specifically covered. |
| SIT-3.3.2 | Financial + tech + capacity-building support needs | MED-079;PUB-027;PUB-028;PUB-029 | Technology and capacity-building support not covered, financial only. |
| SIT-3.3.3 | Grey Infrastructure + NBS measures | DAT-022;MED-042;VID-036 | Grey/structural infrastructure not covered at all, NBS only. |
| SIT-4 | Climate Risk Map w/ IDF/design-curve engineering outputs | SYS-003;DAT-005 | No IDF/design-curve outputs exist — core civil-engineering deliverable absent. |

## Real Gaps — zero topically-relevant assets

**33 of 75 requirement items are gaps** (up from 30 of 73 in v1's actual CSV tally — net effect of the 5 new items minus items removed with the 2.4 collapse).

| node_id | requirement_item | btr_tag | priority_flag |
|---|---|---|---|
| SIT-1.1.1 | ประวัติศาสตร์และแนวโน้มภัยธรรมชาติของประเทศ | | |
| SIT-1.1.1 | ความเข้าใจความเสี่ยงทางกายภาพ และความเสี่ยงจากการเปลี่ยนผ่าน | 2, MUST | |
| SIT-1.2 | Search Hierarchy (จังหวัด -> อำเภอ -> ตำบล) | | |
| SIT-1.2 | Map Integration (Spatial Risk Map) | 2, MUST | |
| SIT-2.1 | Exposure Trends | 2, MUST | |
| SIT-2.2 | สรุปโปรไฟล์ความเสี่ยงรายพื้นที่ (77 จังหวัด/อปท.) | 2, MUST | |
| SIT-2.3 | สรุปมาตรการทางกฎหมายและนโยบาย (พ.ร.บ. สาธารณภัย/ผังเมือง) | 1, MUST | A-BTR |
| SIT-2.3 | Avoided Losses Certification Model | 3, MUST | |
| SIT-2.3.1 | Climate Budget Tagging | 4, SHOULD | A-BTR |
| SIT-2.3.1 | Private-sector finance engagement | 4, SHOULD | A-BTR |
| SIT-2.3.2 | กลไกการประสานงานระหว่างหน่วยงานรัฐและ อปท. | 1, MUST | A-BTR |
| SIT-3.1.1 | ชุดข้อมูลสภาพอากาศรายสถานี (กรมอุตุฯ) | | |
| SIT-3.1.1 | ชุดข้อมูลสังเกตการณ์ผ่านดาวเทียม | 2, MUST | |
| SIT-3.1.3 | คู่มือและบทอธิบายการใช้งานฉากทัศน์ภูมิอากาศ | | |
| SIT-3.1.3 | National Climate Uncertainty Governance Standard | 2, MUST | |
| SIT-3.1.3 | ตัวอย่างกรณีศึกษาการประยุกต์ใช้แบบจำลองคาดการณ์ | | |
| SIT-3.2.1 | Damage Functions library | 2, MUST | |
| SIT-3.2.2 | แหล่งข้อมูลผลการประเมินความเสี่ยงอื่นๆ *(new)* | | |
| SIT-3.2.2.1 | Slow-onset threat statistics | 5, MUST | disaster-loss-statistics |
| SIT-3.2.2.1 | Land subsidence / salinity intrusion | 5, MUST | disaster-loss-statistics |
| SIT-3.3.1 | Cost-Benefit Analysis / Avoided Losses Calculus | 3, MUST | |
| SIT-3.3.1 | GESI integration guidance | 3, SHOULD | |
| SIT-3.3.1 | ภูมิปัญญาท้องถิ่นและมรดกทางวัฒนธรรม | 3, SHOULD | |
| SIT-3.3.2 | Systemic Barriers report | 3, MUST | |
| SIT-3.3.2 | Proposal-writing capacity-development needs | 3, SHOULD | |
| SIT-3.3.3 | Searchable measures database | | |
| SIT-3.3.4 | คลังแผนจัดการความเสี่ยงของท้องถิ่น/ภาคเอกชน | | |
| SIT-3.4.2 | โครงการนำร่อง (ประกันภัยพืชผล/Agri-Map/โครงสร้างควบคุมน้ำ) | 4, SHOULD | A-BTR |
| SIT-3.4.2 | ตัวชี้วัดความพร้อมของโครงการงบประมาณ | | |
| SIT-4 | External hub links (TMD/GISTDA/Copernicus) | | |
| SIT-4 | Climate Impact Explorer *(new, mockup-sourced)* | | |
| SIT-4 | Adaptation Options Explorer *(new, mockup-sourced)* | | |
| SIT-5.2 | Feedback & Helpdesk platform | | |

## Totals

v1 CSV actual (post-addendum, corrected from the stale `.md` figure): 18 FULL / 25 PARTIAL / 30 GAP of 73.

v2: **16 FULL / 26 PARTIAL / 33 GAP of 75.**

- FULL dropped by 2 net — both were among the 3 items removed with the 2.4 collapse (2 FULL + 1 PARTIAL lost, 0 gained back).
- PARTIAL rose by 1 net — 1 lost with 2.4, 2 gained from the new v6-restored items (NAP status, climate-scenario source).
- GAP rose by 3 net — all 3 new GAP items (other-risk-sources pointer, 2 mockup-sourced Tools & Services cards), no GAP items were among those removed.

**21% FULL / 35% PARTIAL / 44% GAP** — genuinely-ready coverage is lower as a share than v1's 25% FULL, mainly because the 2.4 collapse removed two of v1's easier FULL wins (an existing map app and an existing governance manual, both stretched matches) rather than any real content getting less sourced.
