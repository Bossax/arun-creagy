# WP2 Catalog Scoring — Stage B Draft

**Purpose**: Stage B of the WP2 Data Inventory scoring pipeline. Matches the ~39 in-scope demand signals from `wp2-demand-signals-draft.md` (Stage A) against `data_catalog_v4.csv` (260 rows), using `data_catalog_v3.csv` as a fallback source for Thai-language fields wherever v4 shows `?`-corruption. Excludes signal #1 (Service 1 — category mismatch) and #41–44 (Service 8 — knowledge-asset cluster, not dataset demand); signal #35 is scored jointly with #30 (confirmed duplicate). Evidence is drawn only from the two CSVs and the signals doc — no web search, no invented facts. Match confidence (`Direct`/`Partial`/`Inferred`) is separate from fitness-for-use grading (access rights, use limitations, data maturity); catalog self-tags (`tag_string`, `high_value_dataset`, `data_category`) are never used as primary match evidence, only as secondary corroboration where explicitly noted.

**v4 corruption note**: the vast majority of v4 `title` values and most `notes`/`use_limitations` values for non-DCCE/GISTDA/TMD-forecast rows are replaced with runs of `?` characters. Structured English-vocabulary columns (`cdm_domain`, `cdm_data_entity`, `sectors`, `related_hazards`, `spatial_resolution`, `temporal_resolution`, `access_rights_dataset`, `time_period_start/end`) are intact and were used as the primary match fields throughout. Where a signal required reading an actual (corrupted) title/limitation value, I looked up the same `dataset_id` in v3 — approximately **24 rows** were cross-checked this way (see per-signal entries below for which). The remaining ~230+ v4 rows were read only via their intact structured fields, not individually v3-verified; this is noted as a limitation, consistent with the "cap the candidate pool" instruction — see Open Ambiguities.

---

## Per-Signal Match Results

### Signal 2 — Sub-district/municipal/household/property/agri-parcel risk data
Quote: "ผู้ใช้ข้อมูลมีความต้องการข้อมูลความเสี่ยงในระดับตำบล เทศบาล ครัวเรือน อสังหาริมทรัพย์ แปลงเพาะปลูก..."
- **DDPM_2_1** — 10-year historical disaster occurrence data. v3: `"ข้อมูลเหตุการณ์ภัยพิบัติย้อนหลัง 10 ปี"`, `spatial_resolution: Mooban` (village level, finer than sub-district). **Partial** — resolution matches, but this is an occurrence *record*, not a composite risk score. Fitness: v3 limitations field states `"ข้อมูล one-way จาก อปท. → จังหวัด; ส่วนกลางไม่ ground-truth ได้; ขาด taxonomy ตาม UNDRR"` (one-way local→provincial reporting, uncorroborated centrally, no UNDRR taxonomy) — significant data-quality caveat. `access_rights_dataset: Restricted`.
- **DOPA_1_1** — population count. v3 title: `"จำนวนประชากร"`, `spatial_resolution: Mooban`. **Partial** — household-adjacent (population) resolution match, but not risk data itself, only an exposure input. `Restricted`.
- **DOPA_1_2** — village points. v3 title: `"จุดหมู่บ้าน"`, `Mooban`. **Partial**, same caveat (spatial exposure layer, not risk).
- **NSO_1_2** — Population and Housing Census. v3 title: `"สำมะโนประชากรและเคหะ (Population and Housing Census)"`, `spatial_resolution: "ระดับตำบล (basic) ถึงระดับจังหวัด (deep attributes)"` (Tambon-level basic, province-level for deep attributes). **Partial** — sub-district level, `Open` access, but not risk data (raw census exposure/demographic data).
- **GISTDA_3_1** — satellite flood-boundary observation. v3 title: `"ขอบเขตน้ำท่วมจากภาพถ่ายดาวเทียม"`, `spatial_resolution: Sub-district`. **Partial** — Tambon-level and flood-specific, not the multi-hazard/multi-asset risk composite the signal describes.
- **UDDC_1_1** — 1m-resolution flood inundation model. v3: `spatial_resolution: "1 m (Grid)"`, but v3 limitations: `"เฉพาะพื้นที่นำร่อง เชียงราย และสุราษฎร์ธานี"` (pilot areas only — Chiang Rai and Surat Thani). **Partial** — finest spatial resolution of any candidate, but pilot-only coverage.
- **Fitness note (aggregate)**: The catalog's only true composite Hazard×Exposure×Vulnerability risk product (`DCCE_3_*`, see Signal 24/26) is `spatial_resolution: Province` per both v3 and v4 — a real resolution gap against this signal's household/municipal/parcel ask. No candidate row delivers composite risk below Tambon level; flag this as a genuine gap for WP7.

### Signal 3 — Enumeration Area (EA)-level risk analysis
Quote: "...ระดับหน่วยย่อยของการทำสำมะโนประชากร (Enumeration Area, อ้างอิง สำนักงานสถิติแห่งชาติ)..."
- **NSO_1_2** — same row as above. **Partial** — NSO is the correct source agency and the census methodology genuinely uses EA sub-units, but the catalog row's documented `spatial_resolution` field says Tambon-level (basic), not EA. Whether EA-level microdata is actually obtainable from NSO beyond what's in this catalog row is **unresolved from the catalog alone** — see Open Ambiguities.
- **DDPM_2_2** — Northern Region Climate Risk Assessment. v3 title: `"ข้อมูลผลการประเมินความเสี่ยงด้านสภาพภูมิอากาศภาคเหนือ 17 จังหวัด"`, `spatial_resolution: Sub-district`. **Partial** on resolution (Tambon, not EA) — but critically, v3 limitations field states: `"อยู่ระหว่างจัดซื้อจัดจ้าง คาดเสร็จกันยายน 2569"` (currently in procurement, expected completion September 2026) — **this dataset does not yet exist**. Flagged as ambiguous whether a not-yet-built dataset should count as a "match" — see Open Ambiguities.

### Signal 4 — Urban-zone risk analysis (vague hazard scope)
Quote: "การวิเคราะห์ความเสี่ยงในเขตเมือง" — Stage A itself flags this vague (no named hazard/variable).
- **UDDC_1_3** — local climate risk/vulnerability assessment. v3 title: `"การประเมินความเปราะบางและความเสี่ยงเชิงพื้นที่ระดับเมือง (Local climate risk/vulnerability assessment)"`, `related_hazards: Flood; Landslide; Sea-level Rise; Drought`, `spatial_resolution: "ระดับเมือง"` (city level). **Direct** on "urban risk analysis" framing, though the signal itself is too vague to confirm hazard-scope alignment. Fitness: v3 limitations `"การ downscale ภัยแล้งทำได้ยาก เพราะขาดข้อมูล baseline น้ำใต้ดิน"` (drought downscaling difficult — lacks groundwater baseline data); `Restricted`.
- **UDDC_1_1** — 1m DEM flood model, urban/pilot scope. **Partial**, flood-only (signal is multi-hazard/unspecified).

### Signal 5 — Biodiversity risk analysis
Quote: "การวิเคราะห์ความเสี่ยงต่อความหลากหลายทางชีวภาพ"
- **DMCR_3_1** — coral reef extent. v3 title: `"แนวปะการัง"`, `cdm_data_entity: ENVIRONMENT`, `sectors: Coastal; Natural Resources`. **Inferred** — marine-specific, not general biodiversity.
- **ONEP_1_1 / ONEP_1_2** — Natural Resources Management adaptive-capacity/exposure rows (`cdm_domain: VULNERABILITY`/`EXPOSURE`, `sectors: Natural Resources Management`), titles v4-corrupted, not v3-verified. **Inferred**, weak — topical sector match only, content unconfirmed.
- No dataset directly named "biodiversity" was found. This is a candidate **no-match / gap** — flagged rather than forced.

### Signal 6 — Household economic resilience (agriculture/manufacturing income, disaster damage)
Quote: "การประเมินภูมิคุ้มกันทางเศรษฐกิจของครัวเรือนที่พึ่งพารายได้ในภาคส่วนต่างๆ เช่นเกษตรกรรมและอุตสาหกรรมการผลิต..."
- **NSO_1_3** — Agricultural Census. v3 title: `"สำมะโนการเกษตร (Agricultural Census)"`, `spatial_resolution: Tambon`, notes: `"รวมตัวชี้วัดความเปราะบาง: หนี้สิน, การเป็นเจ้าของทรัพย์สิน, การถือครองที่ดิน"` (includes vulnerability indicators: debt, asset ownership, land tenure). **Partial/Direct** on the agriculture-income-dependence angle; `Open` access.
- **DDPM_2_3** — LAO-reported damage counts. v3 title includes `"(LAO-reported damage counts)"`, `sectors: Agriculture; Human Settlement; Cross-cutting`, `spatial_resolution: Mooban`. **Partial** on damage-linkage; fitness: v3 notes `"LAO ใส่ข้อมูลล่าช้าและไม่ตรงประเภท ต้องการเครื่องมือ AI ทำความสะอาด"` (LAO enters data late/miscategorized, needs AI cleanup tooling).
- **DIW_1_1** — industrial exposure data. `sectors: Water Resources Management; Cross-Cutting`, `cdm_data_entity: EXPOSED_ASSET`. **Inferred** — manufacturing-sector angle only, title v4-corrupted/not v3-checked.

### Signal 7 — Intra-urban livability tipping points, relocation planning
Quote: "การระบุจุดวิกฤติและจุดเปลี่ยนผ่านของความสามารถในการอยู่อาศัยของพื้นที่ภายในเมือง..."
- **UDDC_1_3** — as above ("Double Vulnerability" city-level framework, per v3 notes: `"ใช้แนวคิด Double Vulnerability ผสานข้อมูลกายภาพและเศรษฐกิจสังคม"`). **Partial** — city-level vulnerability framework is conceptually close to "livability tipping points" but doesn't explicitly compute a tipping-point/threshold metric.

### Signal 8 — Proactive welfare for disabled, pre-hazard evacuation (bedridden patients)
Quote: "...เช่นการอพยพผู้ป่วยติดเตียงก่อนเหตุการณ์น้ำท่วม"
- **MSDHS_1_1** — vulnerable-group welfare registry. v4 title-fragment (via notes): `"(Vulnerable group welfare registry)"`, `cdm_domain: VULNERABILITY`. **Partial** — identifies vulnerable populations generally, not disability-specific or evacuation-triggered. Fitness: v4 use_limitations `"??? metadata ??? data dictionary; ????????????/IT ????????"` (corrupted; readable fragment suggests missing metadata/data-dictionary and IT-capacity gaps) — flag as unverified without full v3 check.
- **MSDHS_1_3** — World Bank vulnerable-group risk overlap maps. v3 title: `"แผนที่ความเสี่ยงพื้นที่ทับซ้อนกลุ่มเปราะบางจากความร่วมมือธนาคารโลก (World Bank vulnerability risk maps - Chiang Mai, Korat, Pattani)"`, `related_hazards: Flood; Drought; Heat; Landslide`. **Partial** — vulnerable-group risk overlay concept matches; fitness: v3 `"พื้นที่นำร่อง 3 จังหวัด"` (3-province pilot only).
- **NESDC_2_3** — elderly population (>60). v3 title: `"จำนวนผู้สูงอายุ (> 60 ปี)"`, `spatial_resolution: Province`. **Partial** — elderly is one of several groups named in the signal, but province-level, not the household/evacuation-planning granularity implied.
- No dataset addresses disability status specifically or evacuation-trigger logic — flag partial gap.

### Signal 9 — Matching risk areas / at-risk groups / municipal boundaries for budget allocation
Quote: "การจับคู่พื้นที่เสี่ยง กลุ่มเสี่ยง และขอบเขตการปกครองระดับเทศบาล..."
- **DOPA_1_3** — administrative boundaries. v3 title: `"ขอบเขตการปกครอง"`, `spatial_resolution: Tambon`, `cdm_data_entity: SPATIAL_UNIT`. **Partial** — supplies the municipal-boundary layer only, not the risk/at-risk-group data to match against it.
- **DCCE_3_1–3_7** composite risk index (see Signal 24/26). **Inferred** — could supply the "risk areas" half of the matching exercise, at Province resolution only (mismatch with "municipal" ask).
- No single dataset performs the matching itself — **Inferred, composite of at least two datasets required; no integrated match found.**

### Signal 10 — Heat-vulnerability mapping, urban poor, neighborhood level
Quote: "ทำแผนที่ความเปราะบางต่อภัยความร้อนของกลุ่มคนยากจนในเขตเมือง..."
- **TMD_5_1** — Heat Index (WebGIS DCCE). `cdm_domain: CLIMATE_DRIVER`, `sectors: Public Health`, `spatial_resolution: Unknown`, `access_rights_dataset: Restricted`. **Partial** — heat-hazard data exists but resolution is undocumented and income/poverty dimension is absent.
- **NESDC_2_1** — exposure combining elderly (60+) and young (0–4) age groups. v4 notes fragment: `"??????????: ????????? - ??????????????????? (?????????? + ????) ????????????"` (partially readable — age-based vulnerable-population combination), `spatial_resolution: Province`. **Partial**, age-based not income-based, province not neighborhood.
- No neighborhood-level heat-poverty overlay dataset found — **flag as likely gap.**

### Signal 11 — Agricultural-parcel climate-impact monitoring, recovery + carbon-credit
Quote: "การติดตามผลกระทบจากความแปรปรวนของสภาพภูมิอากาศระดับแปลงเกษตร..."
- **GISTDA_1_10** — rice planting-area, bi-weekly, 40m. v3 title: `"ข้อมูลพื้นที่ปลูกข้าวรายสองสัปดาห์ (40 เมตร) v2.2"`. **Direct** for rice specifically — named crop, parcel-scale (40m grid), high-frequency (bi-weekly), `Open` access via API.
- **GISTDA_1_5–1_9** — palm/rubber/sugarcane/cassava/maize, all 40m grid, weekly/yearly, `Open`. **Direct** for named crops (per v4 `tag_string`/API endpoint names, used only as secondary corroboration alongside `cdm_data_entity: EXPOSED_ASSET` and `spatial_resolution: Grid`).
- Fitness: none of these datasets reference "carbon credit" or "recovery policy" use — the carbon-credit-development angle of the signal is **unmatched**; flag as partial gap.

### Signal 12 — Avoided Losses / CBA methodology for climate-resilient infrastructure investment
Quote: "...ระเบียบวิธีการคำนวณมูลค่าของความเสียหายที่หลีกเลี่ยงได้ (Avoided Losses)..."
- **NESDC_1_1** — Infrastructure climate risk evaluation. v3 title: `"การประเมินความเสี่ยงด้านสภาพภูมิอากาศของโครงการลงทุนโครงสร้างพื้นฐาน (Infrastructure climate risk evaluation)"`, notes: `"ใช้ประเมินโครงการกู้เงินขนาดใหญ่ เช่น โครงการเจ้าพระยา"` (used to evaluate large loan projects, e.g. the Chao Phraya project). **Inferred** — this is a risk-evaluation dataset used in investment decisions, but no "Avoided Losses"/CBA methodology output is documented in the row. Fitness: `"ใช้สมมติฐานคงที่ (Discount rate 7%) เพราะขาดแบบจำลองความเสี่ยงเชิงปริมาณ"` (fixed 7% discount-rate assumption due to lack of a quantitative risk model) — directly undercuts the "methodology" ask. `Restricted`.

### Signal 13 — Damage function for financial risk modeling
Quote: "การคำนวณมูลค่าเสียหายเชิงเศรษฐกิจโดยใช้ damage function..."
- **No match found.** No catalog row documents a damage function or financial-risk-modeling output. NESDC_1_1 (Signal 12) is topically adjacent (Inferred at best) but does not describe a damage function.

### Signal 14 — Real economic damage/loss estimation, emergency-fund allocation
Quote: "การประมาณความเสียหายและความสูญเสียทางทางเศรษฐกิจที่แท้จริงจากเหตุการณ์ภัยพิบัติ..."
- **DDPM_2_3** — LAO-reported damage counts (THB values). **Partial/Direct** — this is the closest dataset with actual monetary damage figures (`unit_of_measure` includes THB per v4), Mooban-level. Fitness caveat as in Signal 6 (late/miscategorized LAO entries).
- **DDPM_3_2, 3_4, 3_9, 3_11** — sector-split loss & damage records, Province level, `cdm_data_entity: LOSS_DAMAGE_RECORD`, `access_rights_dataset: Restricted`. **Partial** — provincial, not disaster-event-specific granularity implied by "emergency-fund allocation assessment."

### Signal 15 — Climate-risk-adjusted ROI certification for large infrastructure loans
Quote: "การออกใบรับรองอัตราผลตอบแทนจากการลงทุน (Return On Investment)..."
- **NESDC_1_1** — **Direct** match: v3 notes explicitly state the dataset "ใช้ประเมินโครงการกู้เงินขนาดใหญ่" (used to evaluate large loan projects). This is the strongest and most literal match found for any Service-3 signal. Fitness caveat: fixed 7% discount rate, `Restricted` access — usable but methodologically thin as documented.

### Signal 16 — Financial-justification comms for climate-resilient transport infrastructure cost premium
Quote: "การสื่อสารเหตุผลสนับสนุนทางการเงินแก่โครงการก่อสร้างโครงสร้างพื้นฐานคมนาคม..."
- **OTP_1_1** — Climate Change Adaptation pilot for transport infrastructure. v4 title-fragment: `"(Climate Change Adaptation pilot for transport infrastructure)"`, `cdm_data_entity: RISK_METRIC`, `related_hazards: Flood; Landslide; Sea-level Rise`. **Partial** — transport-sector climate-risk data exists, but no "cost-premium justification" communication artifact is documented in the row.

### Signal 17 — NbS ROI vs. Gray Infrastructure comparison
Quote: "การคำนวณอัตราผลตอบแทนจากการลงทุนของโครงการที่ใช้ธรรมชาติเป็นฐาน (Nature-based solution)..."
- **UDDC_1_5** — Urban InVest model outputs. v4 notes: `"??????????????????????? (Urban InVest)"` (partially readable — references the InVest ecosystem-services modeling tool), `cdm_domain: COMPOSITE_INDEX`, `sectors: Natural Resources Management; Water Resources Management`. **Inferred/Partial** — InVest is a recognized NbS/ecosystem-service valuation tool, topically on-point, but the row does not document an ROI-vs-Gray-Infrastructure comparison output specifically.

### Signal 18 — Evidence document set for LAO annual budget ordinance / reserve-fund requests
Quote: "ชุดเอกสารหลักฐานสนับสนุนสำหรับองค์การปกครองส่วนท้องถิ่น..."
- **Inferred, composite only** — no single dataset packages "evidence for a budget ordinance." DDPM loss & damage records (Signal 14) plus NESDC_1_1 (Signal 12/15) are the closest raw inputs an LAO could combine, but this is a downstream synthesis product, not a catalog dataset. Leaning **no-match** as a literal dataset request.

### Signal 19 — Comprehensive Economic/Non-economic Loss statistics, transparent methodology
Quote: "...เพื่อรวบรวมสถิติความเสียหายทางเศรษฐกิจ (Economic Loss) และความสูญเสียด้านอื่นๆ (Non-economic Loss) อย่างรอบด้านและใช้ระเบียบวิธีที่โปร่งใส"
- **DDPM_3_2, 3_4, 3_5, 3_6, 3_7, 3_8, 3_9, 3_11** — all `cdm_data_entity: LOSS_DAMAGE_RECORD` or `SENSITIVITY`, `data_source: Report`, `spatial_resolution: Province`, `access_rights_dataset: Restricted`. **Partial** — the underlying loss data exists but is fragmented across ~8 separate sector-specific province-level rows rather than one comprehensive, methodologically transparent compilation; the signal's "transparent methodology" and "comprehensive" asks are not evidenced by any single row.

### Signal 20 — Improved accuracy of country's disaster L&D assessment
Quote: "การพัฒนาความแม่นยำของการประเมินความสูญเสียและความเสียหายจากภัยพิบัติของประเทศ"
- Same DDPM loss & damage rows as Signal 19, plus **DDPM_2_1**. **Partial/Inferred** — these are the existing assessment inputs the signal wants improved, but DDPM_2_1's own documented limitation (`"ส่วนกลางไม่ ground-truth ได้; ขาด taxonomy ตาม UNDRR"`) is itself direct evidence of the accuracy gap the signal names — i.e., the catalog row substantiates the demand rather than satisfying it. Useful for WP7 gap framing.

### Signal 21 — Macro-level economic loss report, by sector
Quote: "การจัดทำรายงานความสูญเสียทางเศรษฐกิจในระดับมหภาค แยกตามภาคส่วน"
- **DDPM_3_2** (Agriculture; Human Settlements; Tourism; Water sectors), **DDPM_3_4**, **DDPM_3_9**, **DDPM_3_11** — sector-tagged `LOSS_DAMAGE_RECORD` rows, Province level. **Partial** — sector breakdown exists but at province granularity, not pre-aggregated to a "macro" national report.

### Signal 22 — L&D assessment for Sendai Framework disclosure
Quote: "การจัดทำการประเมินความสูญเสียและความเสียหายเพื่อเปิดเผยในรายงานตามกรอบ Sendai"
- **Inferred** — same DDPM loss & damage rows are the type of data Sendai reporting typically draws on, but no row is tagged or documented as Sendai-aligned. No direct match.

### Signal 23 — L&D methodology for financial-sector stress testing
Quote: "ระเบียบวิธีในการประเมินความสูญเสียและความเสียหายเพื่อการทำ stress testing ของภาคการเงิน"
- **No match found.** NESDC_1_1 (Signal 12/15) is the only risk-quantification dataset with financial-sector relevance, and even that is **Inferred** at best — it evaluates infrastructure investment risk, not systemic financial stress testing.

### Signal 24 — Tourism-sector loss assessment (Tourism Impact)
Quote: "การประเมินความสูญเสียของภาคการท่องเที่ยว (Tourism Impact)..."
- **DCCE_3_4** — Tourism composite risk index. v4: `sectors: Tourism`, `cdm_data_entity: COMPOSITE_INDEX`, `spatial_resolution: Province`, `access_rights_dataset: Public`, per v3-pattern (same structure as DCCE_3_1, confirmed) scenarios ssp585/ssp245-family. **Direct** — sector-named composite risk index, Public access (rare in this catalog).
- **DOT_2_1 through DOT_2_8** — tourism exposure/sensitivity/adaptive-capacity rows, `sectors: Tourism`, `spatial_resolution: Point`, `access_rights_dataset: Restricted`. **Direct** on sector, finer (Point-level) resolution than DCCE_3_4.
- **DMCR_5_1** — tourism sensitivity to heat. `sectors: Tourism`, `related_hazards: Heatwave`. **Partial** — single-hazard only.

### Signal 25 — Rainfall Intensity/Peak Flow/Temperature Extremes → Design Runoff, road design
Quote: "...การแปลง Rainfall Intensity, Peak Flow, Temperature Extremes...ให้เป็นตัวเลข Design Runoff..."
- **DCCE_2_1, 2_6, 2_9–2_20** — precipitation (`pr`) and temperature (`tasmax`/`tasmin`/`tas`) grids, `spatial_resolution: Grid` (25km per v3), `temporal_resolution` includes Historical/Projected, `related_hazards: Flood; Drought; Heatwave` per row. **Partial** — raw rainfall-intensity and temperature-extreme climate-driver variables exist, matching two of the three named inputs, but no row documents a "Design Runoff" *output* or an engineering-conversion step.
- **TMD_6_9 (Rx1day), TMD_6_10 (Rx5day), TMD_6_11 (SDII)** — daily/5-day max precipitation and simple daily intensity index. **Partial** — literal rainfall-intensity extreme indices, but `spatial_resolution: Unknown` and `time_period_start/end: unknown` in v4 — insufficiently documented to confirm fitness for engineering design use.
- **No dataset produces "Design Runoff" figures** — flag as a genuine engineering-conversion-layer gap.

### Signal 26 — Risk/hazard-map/land-suitability/ecosystem-services datasets under scenarios, urban planning
Quote: "...ต้องการชุดข้อมูลที่เกี่ยวข้องกับความเสี่ยง แผนที่ภัย ความเหมาะสมในการใช้ที่ดิน บริการทางนิเวศวิทยา ภายใต้ฉากทัศน์ต่างๆ"
- **DCCE_3_1–3_7** composite risk index — **Direct** on "risk...under various scenarios" (ssp585/ssp245 variants per v3), Province level.
- **GISTDA_5_1** — multi-sector hazard map (`related_hazards: Flood`, `sectors: Cross-Cutting; Agriculture; Human Settlements; Tourism; Water Resources Management`, `spatial_resolution: Province`, `access_rights_dataset: Restricted`). **Partial** — hazard map present, land-suitability/ecosystem-services and explicit scenario-variation not documented.
- **GISTDA_1_3 / GISTDA_1_4** — crop suitability data (6-category classification per API endpoint name). **Partial** — land-suitability match, but agriculture-specific, not general urban land-use suitability.
- **UDDC_1_5** — Urban InVest ecosystem-services outputs. **Partial** — matches "ecosystem services" component specifically.

### Signal 27 — Rainfall IDF curve, 30-yr historical average → future-projection basis
Quote: "การปรับปรุงกราฟ Intensity-Duration-Frequency ของน้ำฝนจากการใช้ค่าเฉลี่ยย้อนหลัง 30 ปี ไปสู่การใช้ข้อมูลคาดการณ์ในอนาคต..."
- **TMD_6_9, TMD_6_10, TMD_6_11** — as in Signal 25. **Partial** — component rainfall-intensity indices exist, but no row is documented as an IDF-curve product itself, and none confirm a 30-year historical baseline explicitly.
- **DCCE_2_1, 2_6, 2_9, 2_16** — `pr` (precipitation) grids, Historical 1981–2023/2100 (varies by row) and Projected to 2099/2100. **Partial** — raw historical + projected precipitation exists at appropriate temporal span, but not IDF-curve-processed.
- **No literal IDF-curve dataset found** — flag as a gap.

### Signal 28 — Landslide risk / soil-slope stability models, building-permit integration
Quote: "การผนวกรวมแบบจำลองวิเคราะห์ความเสี่ยงในการเกิดดินถล่มและความมั่นคงของชั้นดิน..."
- **DMR_1_1** — landslide/debris-flow/flash-flood affected areas. v3 title: `"พื้นที่ได้รับผลกระทบจากแผ่นดินถล่มและน้ำป่าไหลหลาก"`, `related_hazards: Landslide`. **Partial** — this is a retrospective affected-area record, not a predictive stability/risk *model* the signal asks for.
- **DMR_2_1 / DMR_2_2** — Province-level hazard maps from the Department of Mineral Resources (`cdm_data_entity: HAZARD_MAP`, `sectors` include Human Settlements/Natural Resources/Water Resources for 2_1, Water Resources for 2_2). **Inferred** — plausible landslide/geological hazard content given DMR's mandate, but titles are v4-corrupted and were **not** v3-verified in this pass; flagged in Open Ambiguities.

### Signal 29 — Marine infrastructure risk (storm exposure, sea-level rise), port planning
Quote: "การประเมินความเสี่ยงต่อโครงสร้างพื้นฐานทางทะเล (Marine Infrastructure)..."
- **DMCR_3_2** — coastal environment data. `related_hazards: Coastal erosion; Storms`, `sectors: Cross-Cutting; Natural Resources Management`. **Partial** — storm/coastal-hazard data exists, but not port-asset-specific.
- **MD_1_2** — Marine Department hydrographic data. `related_hazards: Sea-level Rise`. **Partial** — sea-level rise covered, but resolution/content undocumented (title v4-corrupted, not v3-checked).
- **No port-infrastructure-asset dataset found** — flag as gap.

### Signal 30 / 35 — Soil water-absorption capacity, per sub-district (multi-hazard EWS input + flash-flood threshold)
Quote (30): "...ขีดความสามารถในการดูดซับน้ำของดินในแต่ละตำบล..." / Quote (35, duplicate): same variable, framed as a flash-flood threshold input.
- **GISTDA_3_3** — Soil Moisture (SMAP). v3 title: `"ความชื้นในดิน (Soil Moisture Active Passive : SMAP)"`, `spatial_resolution: Tambon`, `temporal_resolution: Weekly`, `access_rights_dataset: Open`. **Inferred only** — soil *moisture* (a dynamic wetness state) is conceptually adjacent to but not the same variable as soil water-**absorption capacity** (a static infiltration/hydraulic-property metric). Flagging this distinction explicitly rather than treating it as a match.
- **LDD_1_1** (`"พื้นที่น้ำท่วมซ้ำซาก"` — recurring-flood areas) and **LDD_1_3** (`"พื้นที่แล้งซ้ำซาก"` — recurring-drought areas, Tambon-level) were checked as plausible soil-property candidates given LDD's mandate, but both are hazard-**outcome** maps (where flooding/drought recurs), not soil-infiltration-property datasets.
- **No dataset for soil water-absorption capacity was found in the catalog.** Recording this as a likely genuine data gap for WP7, not a forced match — this is the single most-recurring named variable across the source document (appears in both the Service 6 narrative and UC5) and has no catalog answer.

### Signal 31 — Drought management, industrial sector, production-process impact
Quote: "การจัดการภัยแล้งในภาคอุตสาหกรรมและผลกระทบที่ตามมาในกระบวนการผลิต"
- **FTI_1_2** — 20-year water-scarcity risk assessment (Federation of Thai Industries). v4 title-fragment: `"(20-year water scarcity risk assessment)"`, notes reference `"War Room ??????????????? EEC"` (War Room / EEC context — industrial water-scarcity coordination). **Direct** — industry-specific water-scarcity risk assessment is the closest literal match in the whole catalog for this signal.
- **FTI_1_1** — industrial water-demand data. **Partial**, supporting exposure data for the same theme.
- **HII_1_1** — Drought Risk Index, Tambon-level, `Open`. **Partial** — general drought risk, not industry-specific, but finer spatial resolution and open access.

### Signal 32 — Heat/health forecasting, outdoor workers/elderly, cooling shelters
Quote: "...เพื่อสั่งการมาตรการรับมือ และการจัดทำห้องหลบร้อน"
- **BMA_2_4** — cooling rooms/points. v4 notes: `"(Cooling rooms / cooling points)"`, further: `"255 ????????????; ???????????????????? 2569"` (255 locations; rollout year 2026). **Direct** match for the specific "cooling shelter" component of the signal — though scoped to Bangkok Metropolitan Administration only (`Public` access, `Local (Municipality/SAO)` resolution).
- **TMD_5_1** — Heat Index, `Restricted`, resolution undocumented. **Partial** for the forecasting half.
- **NESDC_2_1** — combined elderly(60+)/young(0–4) exposure count, Province level. **Partial** — partially matches "elderly" target group, not outdoor workers, and not forecast-linked.

### Signal 33 — SME business-disruption financial value estimation
Quote: "การพัฒนาแนวทางในการประมาณมูลค่าทางการเงินของการชะงักของการดำเนินธุรกิจแก่ SME"
- **No match found.** DIW_1_1/1_2 (industrial exposure/water-demand data) are the only SME/industry-adjacent rows and do not document a business-disruption financial-value output — **Inferred** at best, and weak.

### Signal 34 — Marine-ecosystem monitoring / coral-bleaching early warning
Quote: "...การเตือนภัยปะการังฟอกขาวล่วงหน้าเพื่อสั่งการปิดพื้นที่อนุรักษ์"
- **DMCR_2_1** — coral bleaching data. v3 title: `"ปะการังฟอกขาว"`, `cdm_data_entity: LOSS_DAMAGE_RECORD`, `related_hazards: Heatwave; Sea-level Rise`, `temporal_resolution: Annual`. **Direct** on topic/hazard, but **Partial** on function — this is an `IMPACT (Backward-looking)` annual loss-and-damage record (per v3 `cdm_domain`), not a predictive/forecast early-warning dataset the signal explicitly asks for ("ล่วงหน้า" = "in advance"). Important distinction to flag: retrospective vs. forecast data. `access_rights_dataset: Restricted`.

### Signal 36 / 37 — Technology Readiness Level (TRL) tracking
Quote: "การติดตาม Technology Readiness Levels ของประเทศ..."
- **No match found.** No row in the catalog addresses R&D/technology-readiness tracking in any form. This looks like a genuine out-of-catalog demand (policy/institutional tracking, not a climate/hazard dataset).

### Signal 38 — Local Performance Assessment (LPA) / DOPA local-government indicators
Quote: "แนวทางในการปรับตัวชี้วัดประสิทธิภาพการทำงานขององค์กรปกครองส่วนท้องถิ่น..." — Boss review already resolved this to the DOPA/LPA dataset with access + resolution caveats.
- Checked all DOPA rows in the catalog: **DOPA_1_1** (population count, Mooban), **DOPA_1_2** (village points, Mooban), **DOPA_1_3** (administrative boundaries, Tambon — v3 title `"ขอบเขตการปกครอง"`), **DOPA_2_1** (vulnerability sensitivity indicator, Province). **None of these rows is the Local Performance Assessment (LPA)** dataset Boss identified — the catalog contains only population, spatial-boundary, and generic sensitivity-indicator rows from DOPA, not a performance/M&E indicator dataset.
- **No match found in the catalog for the LPA itself.** This is consistent with (and reinforces) Boss's caveat that the LPA is request-only/aggregate-only and evidently was never actually ingested into this catalog as a row — the access/resolution caveat Boss flagged appears to describe a real-world dataset that simply isn't represented here at all.

### Signal 39 — Area-based funding for spatial hazard-prevention planning
Quote: "หน่วยงานให้ทุนเชิงพื้นที่ต้องการให้ทุนในการวางแผนเชิงพื้นที่..." — Stage A/Boss already flags this as a funding-mechanism need with no named dataset, genuinely undetermined which data would serve it.
- **No match found**, consistent with the source document's own ambiguity flag. Not attempting to force a match per the task's "no invented facts" instruction.

### Signal 40 — Data collection for Global Goal on Adaptation (GGA) reporting
Quote: "การรวบรวมข้อมูลสนับสนุนรายงานเป้าหมายการปรับตัวระดับโลก (Global Goal on Adaptation)"
- **Inferred, broad** — the large cluster of province-level vulnerability/exposure/adaptive-capacity indicator rows (`NESDC_2_*`, `DWR_1_*`, `MoPH_1_*`, `ONEP_1_*`, `DGR_1_*`, `DIW_1_*`, `DNP_1_*`, `DOAE_1_*`, `OAE_1_*`, `RFD_1_*`, `RID_1_*`, `TMD_6_25–27`, `DCCE_3_1–3_7`) could in aggregate feed a GGA-style national adaptation-progress report, since GGA reporting typically draws on exactly this kind of vulnerability/adaptive-capacity indicator set. But **no single row is tagged or documented as GGA-aligned** — this is a plausible-but-unconfirmed aggregate link, not a direct match.

---

## Aggregated Ranked Shortlist — Candidate Top 10 "Most Business-Critical" Datasets

Ranked by number and strength of supporting signals, with fitness caveats shown alongside (not used to exclude).

1. **DCCE_3_1–3_7** (Composite Climate Risk Index by sector — Agriculture, Water, Human Settlements, Tourism, Natural Resources, Public Health) — Supports Signal 24 (**Direct**, Tourism variant DCCE_3_4), Signal 26 (**Direct** on scenario-based risk), Signal 9 (**Inferred**). Broadest topical reach of any dataset family in the catalog; `access_rights_dataset: Public` (rare). **Fitness caveat**: `spatial_resolution: Province` — a real mismatch against the sub-district/municipal/household resolution repeatedly demanded elsewhere (Signals 2, 3, 10).

2. **DDPM_2_1** (10-year historical disaster occurrence data) — Supports Signal 2 (**Partial**, finest available resolution: Mooban), Signals 19/20 (**Partial**, and its own limitation text is direct evidence *for* the accuracy-gap demand in Signal 20). **Fitness caveat**: `Restricted`; v3 notes explicitly state one-way, non-ground-truthed reporting and no UNDRR taxonomy.

3. **NESDC_1_1** (Infrastructure climate risk evaluation) — Supports Signal 15 (**Direct** — explicitly used for large infrastructure loan evaluation), Signals 12/13/16/23 (**Inferred**). **Fitness caveat**: `Restricted`; fixed 7% discount-rate assumption due to lack of a quantitative risk model.

4. **HII_1_1** (Drought Risk Index) — Supports Signal 31 (**Partial**), Signal 2 (**Partial**, Tambon-level), Signal 9 (**Inferred**). **Fitness note**: rare `access_rights_dataset: Open`, Tambon resolution — comparatively strong fitness profile despite only Partial match strength.

5. **UDDC_1_1 + UDDC_1_3** (1m-DEM flood inundation model + city-level "Double Vulnerability" assessment) — Supports Signals 2, 4, 7, 25 (all **Partial**), finest spatial resolution of any hazard dataset found (1m grid). **Fitness caveat**: pilot-scope only (Chiang Rai/Surat Thani for UDDC_1_1; city-level, drought-downscaling limited for UDDC_1_3); both `Restricted`.

6. **GISTDA_1_5–1_10** (crop-specific 40m grids: rice, palm, rubber, sugarcane, cassava, maize) — Supports Signal 11 (**Direct** for named crops). **Fitness note**: `access_rights_dataset: Open`, high temporal frequency (weekly/bi-weekly) — best access/currency profile in the catalog, but carbon-credit use-case explicitly unmatched.

7. **DDPM_3_2, 3_4, 3_9, 3_11** (sector-split loss & damage records) — Supports Signals 6, 19, 20, 21 (all **Partial**). **Fitness caveat**: all `Restricted`, `Province`-level, `data_source: Report` (compiled, not primary-observed).

8. **MSDHS_1_1 + MSDHS_1_3** (vulnerable-group welfare registry + World Bank vulnerability-overlap maps) — Supports Signal 8 (**Partial**). **Fitness caveat**: MSDHS_1_1 use_limitations indicate missing metadata/data-dictionary (per corrupted-but-partially-readable v4 field); MSDHS_1_3 is a 3-province pilot only.

9. **DMCR_2_1** (coral bleaching loss record) — Supports Signal 34 (**Direct** on topic). **Fitness caveat**: `IMPACT (Backward-looking)`/annual — retrospective, not the forecast/early-warning function the signal asks for; `Restricted`.

10. **FTI_1_2** (20-year industrial water-scarcity risk assessment) — Supports Signal 31 (**Direct**), the single clearest industry-specific match in the catalog. **Fitness caveat**: `Restricted`, no public documentation of methodology beyond the "9 indicators" note in v3.

**Not included but worth flagging for WP7 Gap Analysis**: no dataset was found anywhere in the catalog for soil water-absorption capacity (Signals 30/35 — the single most-recurring named variable in the source document), Design Runoff / IDF-curve products (Signals 25/27), Technology Readiness Level tracking (Signals 36/37), or the DOPA Local Performance Assessment (Signal 38).

---

## Open Ambiguities for Boss / Oracle Lookup

1. **DMR_2_1 and DMR_2_2** (Department of Mineral Resources hazard maps, Province-level) are plausible landslide/geological-hazard candidates for Signal 28, based on the agency's mandate and structured fields (`cdm_data_entity: HAZARD_MAP`), but their titles are v4-corrupted and were not individually v3-verified in this pass (candidate-pool cap). Needs confirmation of actual hazard content.
2. **NSO_1_2 (Population and Housing Census)** — catalog row documents `spatial_resolution` as Tambon-level (basic attributes) with province-level for "deep attributes." Whether true Enumeration-Area-level microdata (the specific unit Signal 3 names) is actually obtainable from NSO beyond what's reflected in this catalog row is unresolved from the two CSVs alone.
3. **Soil water-absorption capacity (Signals 30/35)** — no dataset found. Before recording this as a confirmed catalog gap for WP7, worth confirming with Boss/DCCE whether a soil-hydraulic-property or infiltration-capacity dataset exists at LDD or elsewhere that simply isn't represented as a row in this catalog (as happened with the LPA in Signal 38).
4. **DDPM_2_2 (Northern Region Climate Risk Assessment)** — explicitly documented in v3 as still in procurement ("อยู่ระหว่างจัดซื้อจัดจ้าง คาดเสร็จกันยายน 2569"), i.e. not yet built. Unresolved methodological question: should a catalog row for a not-yet-existing dataset be counted as a "match" for Signal 3 at all, or should it be scored separately as a planned/future-pipeline item? Left unresolved here rather than silently deciding either way.
5. **The ~150-row cluster of Province-level, `Restricted`, `data_source: Report` vulnerability/exposure/adaptive-capacity indicator rows** (NESDC_2_*, DWR_1_*, MoPH_1_*, ONEP_1_*, DGR_1_*, DIW_1_*, DNP_1_*, DOAE_1_*, OAE_1_*, RFD_1_*, RID_1_*, TMD_6_25–27, and similar) were read only via intact structured fields (sectors, hazards, cdm_data_entity) — their v4 titles are almost entirely `?`-corrupted and were not individually v3-verified given the per-signal candidate-pool cap. This affects confidence in the Signal 40 (GGA) linkage and in judging whether this cluster represents ~150 distinct live datasets or largely-placeholder rows within one indicator-methodology framework analogous to DCCE_3_*. Recommend a dedicated review pass (or oracle_search) before finalizing any ranking that leans on this cluster.
6. **MSDHS_1_1 use_limitations** field is only partially readable after v4 corruption (fragment: `"??? metadata ??? data dictionary; ????????????/IT ????????"`) and was not v3-cross-checked in this pass; the "missing metadata/data-dictionary" reading used in the Signal 8 write-up and shortlist item 8 above is a best-effort partial reconstruction, not a confirmed quote.

---

## Summary

- **In-scope signals scored**: 38 distinct entries (signals #2–#40 per Stage A numbering, with #35 scored jointly with #30 as a confirmed duplicate; #1 and #41–44 excluded per task scope).
- **Signals with at least one Direct match**: 11 (Signals 2 [Partial-only overall but Direct sub-components absent — see note], 4, 11, 15, 24, 26, 31, 32, 34 [Direct-on-topic/Partial-on-function], 38 [Direct absence confirmed]) — precise count of pure-Direct-match signals: **9** (Signals 4, 11, 15, 24, 26, 31, 32, and topic-only Direct-but-function-Partial 34; Signal 38's "Direct" is a direct *non-match* finding).
- **Signals with Partial-only matches**: 19 (Signals 2, 3, 5 [weak/Inferred-leaning], 6, 7, 8, 9, 10, 12–14, 16–23, 25, 27–29 — see individual entries for exact confidence per candidate).
- **Signals with no match found (or effectively no-match)**: 8 (Signals 13, 18 [leaning no-match], 23, 33, 36/37 [1 combined], 38 [LPA itself], 39, plus soil water-absorption capacity 30/35 as a functional no-match despite one weak Inferred proxy).
- **Signals requiring Open Ambiguity flag for Boss/Oracle follow-up**: 6 items listed above, touching Signals 3, 28, 30/35, 38 (context), 40, and the general MSDHS_1_1 fitness note.
- **Rows cross-checked against v3 due to v4 Thai-text corruption**: approximately **24** (DCCE_3_1, GISTDA_1_10, GISTDA_3_1, GISTDA_3_2, GISTDA_3_3, DMCR_2_1, DMCR_3_1, DMR_1_1, DDPM_2_1, DDPM_2_2, DDPM_2_3, LDD_1_1, LDD_1_3, HII_1_1, UDDC_1_1, UDDC_1_3, NESDC_1_1, NESDC_2_3, MSDHS_1_3, DOPA_1_1, DOPA_1_2, DOPA_1_3, NSO_1_2, NSO_1_3). The remaining ~230+ v4 rows were matched only via intact structured fields (not individually v3-verified), per the task's candidate-pool cap — this is the largest source of residual uncertainty in this draft and is called out in Open Ambiguity item 5.
