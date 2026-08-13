# WP4 DRD — Deliverable to Asset Mapping

**Date** 13 August 2026
**Companion to** `2026-08-12-WP4-Developer-Ready-Design-Requirements-Specification.md` and its 5 CSVs

## How to read this

Each of the 13 deliverables in Appendix A of the DRD gets two lists here.

**Confirmed assets** are the assets the WP4 gap-analysis process already matched to a requirement in this deliverable. They are named directly — asset ID, title, type, owner, link — pulled from `2026-08-12-WP4-DRD-requirements.csv` and resolved against DCCE's two asset registries. Where a requirement in the deliverable has no matched asset at all, that is stated plainly as a confirmed gap, not left blank.

**Other potentially relevant datasets** come from a fresh scan of the full WP2 data catalog (`data_catalog_v4.csv`, 260 rows) for datasets that share the deliverable's subject matter but were never formally matched to a requirement. These are leads, not confirmed fits. Almost everything in that catalog carries the flags `Baseline-Draft` and `Unverified-Baseline`, and most rows are access-restricted — a developer still has to check each one before relying on it.

Two registries were used to resolve confirmed assets: `DCCE_Unified_Digital_Asset_Database.csv` for dash-style codes (`PUB-`, `DAT-`, `MED-`, `SYS-`, `VID-`) and `output/02_Data_Inventory/data_catalog_v4.csv` for underscore-style codes (`DCCE_x_y`, `MD_1_2`, `DMCR_x_x`, `DDPM_x_x`, `RFD_1_2`).

---

## DEL-1 — Thailand Climatology Dashboard

**Serves** REQ-011, REQ-033 · **Sections** 2.1, 3.1

### Confirmed assets

| Asset | Title | Type | Owner | Link | Flags |
|---|---|---|---|---|---|
| `DCCE_2_1` | ปริมาณน้ำฝน (GridData, historical) | Dataset | DCCE | https://clim-webbased.dcce.go.th/DataServices | Restricted, Unverified-Baseline |
| `DCCE_2_2` | อุณหภูมิสูงสุด (GridData, historical) | Dataset | DCCE | https://clim-webbased.dcce.go.th/DataServices | Restricted, Unverified-Baseline |

Both requirements resolve to the same two datasets — this is the shared backend for the dashboard.

### Other potentially relevant datasets

The same DCCE grid family has more variables than the two currently matched, all sharing the same access/status flags and the same access URL (`clim-webbased.dcce.go.th`):

| Asset | Title |
|---|---|
| `DCCE_2_3` | อุณหภูมิต่ำสุด (GridData, historical) |
| `DCCE_2_4` | อุณหภูมิเฉลี่ย (GridData, historical) |
| `DCCE_2_5` | ความชื้นสัมพัทธ์ (GridData, historical) |

TMD's climate extreme indices are a strong lead for the dashboard's "extreme statistics" view (REQ-011) — these look purpose-built for exactly this kind of product, though not yet assessed for this use: `TMD_6_1` (TXx, max of daily max temp), `TMD_6_2` (TNx), `TMD_6_9` (Rx1day, max 1-day rainfall), `TMD_6_10` (Rx5day), `TMD_6_11` (SDII, daily rainfall intensity), `TMD_6_14` (PRCPTOT), `TMD_6_19` (SPI-1, standardized precipitation index), `TMD_6_22`–`TMD_6_24` (heat/flood/drought hazard indices).

### Developer headstart

Start by resolving the `DCCE_2_1`/`DCCE_2_2` access restriction — that unblocks both REQ-011 and REQ-033 at once. Then check whether the TMD extreme-indices series above is something DCCE can pull in directly (it would save real derivation work) or whether it needs its own agreement with TMD.

---

## DEL-2 — Provincial risk profile layer

**Serves** REQ-008, REQ-014, REQ-027 · **Sections** 1.2, 2.2, 2.4

### Confirmed assets

| Asset | Title | Type | Owner | Link | Flags |
|---|---|---|---|---|---|
| `MED-015` | การวิเคราะห์ความเปราะบางและขีดความสามารถในการปรับตัว (Measuring Vulnerability & Adaptive Capacity) | E-book Reader | กลุ่มประชาสัมพันธ์และสื่อสารสิ่งแวดล้อม | https://www.dcce.go.th/media/23820/ | Unverified — matched to REQ-027 as a methodology explainer only, not an actual index dataset |

REQ-008 and REQ-014 both have **no matched asset** — confirmed gap. The province-level composite data they'd draw on lives in DS-01 (`DCCE_3_1`–`DCCE_3_7`, see DEL-13 below), and neither requirement can get below province level without Brief E-5 or E-6.

### Other potentially relevant datasets

For sub-provincial administrative geography (the DOPA-vs-LAO boundary problem, see Appendix E of the DRD): `DOPA_1_1` (population counts), `DOPA_1_2` (village points), `DOPA_2_1` (households within municipal boundaries) — these carry the actual DOPA administrative geometry a build team would need to even attempt Brief E-6's disaggregation work.

For vulnerability/profile content: `NESDC_2_1` through `NESDC_2_13` (poverty index, elderly/child counts, human development index, GRP per capita, inequality coefficient — all province-level) and `NSO_1_2` through `NSO_1_6` (population and housing census, agricultural census, labor force survey, socio-economic survey) are a strong lead for filling out a real provincial risk profile beyond the composite index alone.

### Developer headstart

The provincial composite index (DEL-13) is the backbone; the NESDC and NSO series above are the most promising unexplored leads for making REQ-014's profiles genuinely richer than a single index number. Confirm access terms on NESDC/NSO data before counting on it.

---

## DEL-3 — External-source explainers with data-sharing agreements

**Serves** REQ-030, REQ-031 · **Section** 3.1

### Confirmed assets

Both requirements have **no matched asset** — confirmed gap, expected, since the whole point of these two is that DCCE doesn't hold this data. TMD holds station data; GISTDA and marine bodies hold the satellite products.

### Other potentially relevant datasets

These aren't assets DCCE can cite as evidence of coverage, but they are the actual external products the explainer pages (REQ-030/031) should point readers to:

**Station observations (REQ-030):** `TMD_1_1` (hourly rainfall), `TMD_1_2` (24-hour rainfall), `TMD_1_3` (sea-level pressure), `TMD_1_4` (relative humidity), `TMD_1_5` (2m surface temperature), `TMD_1_6` (10m wind), `TMD_6_25` (station count).

**Satellite observations (REQ-031):** `GISTDA_1_1`/`GISTDA_1_2` (burn area), `GISTDA_2_1` (sea surface temperature), `GISTDA_2_2` (nighttime lights), `GISTDA_3_1` (satellite-derived flood extent), `GISTDA_3_3` (soil moisture, SMAP), `GISTDA_4_1` (satellite imagery), `DMCR_2_1` (coral bleaching), `DMCR_3_1` (coral reefs).

### Developer headstart

Nothing to build yet beyond the explainer pages and the outbound links. If DCCE later pursues a live connection, the TMD and GISTDA rows above are the concrete list of what to request access to first.

---

## DEL-4 — Slow-Onset Hazards Profile

**Serves** REQ-042, REQ-043, REQ-044, REQ-045 (one page, sitemap node 3.2.2.1) · **Section** 3.2

### Confirmed assets

| Asset | Title | Type | Owner | Link | Flags |
|---|---|---|---|---|---|
| `MD_1_2` | ข้อมูลระดับน้ำทะเล (sea level) | Dataset | MD (Marine Department, hydrology group) | http://hydro.md.go.th/ | Restricted, Unverified-Baseline |
| `DMCR_1_1` | พื้นที่กัดเซาะชายฝั่ง (WebGIS DCCE) | Dataset | DMCR | https://tcs.dmcr.go.th/dmcr/v2/router?page=dashboard | Restricted, Unverified-Baseline |
| `DMCR_4_1` | พื้นที่กัดเซาะชายฝั่ง (DMCR ภาคสนาม) | Dataset | DMCR | https://tcs.dmcr.go.th/dmcr/v2/router?page=dashboard | Restricted, Unverified-Baseline |
| `MED-127`–`MED-137` (9 items) | Coastal adaptation infographic series | Knowledge Asset | กลุ่มประชาสัมพันธ์และสื่อสารสิ่งแวดล้อม | dcce.go.th/media/… (see Appendix D of the DRD for each link) | Narrative infographics, no underlying data |

REQ-042 (temp/rainfall slow-onset trend) shares its data with DEL-1 (`DCCE_2_1`/`DCCE_2_2`) — no separate asset. REQ-044 (subsidence/salinity) has **no matched asset anywhere** — confirmed gap, nothing in either registry.

### Other potentially relevant datasets

`DMCR_3_2` (mangrove extent) is a lead for coastal resilience context alongside erosion. `RTSD_1_1` (elevation above sea level) could support both the sea-level and subsidence explainers. Nothing in the 260-row catalog addresses land subsidence directly — this confirms REQ-044's "nothing exists" status rather than surfacing a hidden lead.

### Developer headstart

Ship the four static explainers first — they don't depend on any of the Restricted assets above. If DCCE later funds the stretch items (rate derivation, index computation, subsidence source-finding), `MD_1_2` and `DMCR_1_1`/`DMCR_4_1` access needs resolving first for the sea-level and erosion pieces; subsidence has no starting point in DCCE's holdings at all and needs a new external source.

---

## DEL-5 — External-source explainers, monitoring and projections

**Serves** REQ-032, REQ-035 · **Section** 3.1

### Confirmed assets

| Asset | Title | Type | Owner | Link | Flags |
|---|---|---|---|---|---|
| `MED-105` | ทำความรู้จักกับ "สภาวะ ENSO-Neutral" | E-book Reader | กลุ่มประชาสัมพันธ์และสื่อสารสิ่งแวดล้อม | https://www.dcce.go.th/media/8254/ | One-off explainer, not a live feed |
| `DCCE_2_11` | ปริมาณน้ำฝน (RegCM5, EC-Earth3-Veg) | Dataset | DCCE | https://clim-webbased.dcce.go.th/DataServices | Restricted, Unverified-Baseline |
| `DCCE_2_16`–`DCCE_2_19` | Statistical downscaling series (rainfall, max/min/mean temp, CMIP6) | Dataset | DCCE | https://clim-webbased.dcce.go.th/DataServices | Restricted, Unverified-Baseline |
| `clim-webbased.dcce.go.th` | DCCE's downscaled climate projection platform | Data Product | **Not yet in either canonical registry — needs a formal entry** | https://clim-webbased.dcce.go.th/Home | Referenced as the access URL inside the DCCE_2_x rows above, so it's a real active platform even without its own registry entry |

### Other potentially relevant datasets

`TMD_6_19`–`TMD_6_21` (SPI drought indices) are a lead for the ENSO/seasonal-outlook explainer, since ENSO's main practical signal for Thailand is drought risk.

### Developer headstart

Both requirements resolve to explainer + link content. The one real task: get `clim-webbased.dcce.go.th` formally registered as an asset so future documents don't have to keep flagging it as unregistered.

---

## DEL-6 — Concept and methodology standards

**Serves** REQ-038, REQ-040, REQ-048 · **Section** 3.2

### Confirmed assets

| Asset | Title | Type | Owner | Link | Flags |
|---|---|---|---|---|---|
| `DAT-014` | ข้อมูลการประเมินผลการปรับตัวต่อการเปลี่ยนแปลงสภาพภูมิอากาศ | Document | กลุ่มประเมินผลการปรับตัวต่อการเปลี่ยนแปลงสภาพภูมิอากาศ | https://dgf.dcce.go.th/dataset/m-and-e | REQ-038 |
| `MED-015` | Measuring Vulnerability & Adaptive Capacity | E-book Reader | กลุ่มประชาสัมพันธ์และสื่อสารสิ่งแวดล้อม | https://www.dcce.go.th/media/23820/ | REQ-038 |
| `PUB-012` | คู่มือการจัดทำห่วงโซ่ผลกระทบจากการเปลี่ยนแปลงสภาพภูมิอากาศ (impact chain manual) | Document | กองยุทธศาสตร์และความร่วมมือระหว่างประเทศ | https://www.dcce.go.th/datacenter/19243/ | REQ-040, closest existing proxy, not purpose-built |
| `MED-125` | Same impact chain manual, media reprint | E-book Reader | กลุ่มประชาสัมพันธ์และสื่อสารสิ่งแวดล้อม | https://www.dcce.go.th/media/5075/ | REQ-040 |
| `PUB-026` | กองทุนจัดการความสูญเสียและความเสียหายจากสภาพภูมิอากาศ (FRLD) | Web Page | กองยุทธศาสตร์และความร่วมมือระหว่างประเทศ | https://www.dcce.go.th/datacenter/25096/ | REQ-048, funding page, not a framework explainer |

### Other potentially relevant datasets

None found in `data_catalog_v4.csv` — this deliverable is content/methodology work, not something a raw dataset scan surfaces leads for. CRVA and CRM (GIZ/UNDRR multi-hazard risk assessment methodologies) are worth requesting directly from those organizations as reference material for REQ-040; they aren't in either DCCE registry since they're external.

### Developer headstart

All three requirements are content work, not data engineering. Start with REQ-040 since the CRVA/CRM reference methodologies need to be sourced externally before writing begins.

---

## DEL-7 — Risk framing and worked examples

**Serves** REQ-003, REQ-037, REQ-047 · **Sections** 1.1, 3.1, 3.2

### Confirmed assets

| Asset | Title | Type | Owner | Link |
|---|---|---|---|---|
| `MED-048` | เจาะลึกห่วงโซ่ผลกระทบ "น้ำท่วมหาดใหญ่ 2025" | E-book Reader | กลุ่มประชาสัมพันธ์และสื่อสารสิ่งแวดล้อม | https://www.dcce.go.th/media/21308/ |

REQ-003 and REQ-037 both have **no matched asset** — confirmed gap. REQ-047 has this one asset covering the urban/flood case only; the agriculture-sector companion case study has nothing.

### Other potentially relevant datasets

For the agriculture-sector impact chain case study REQ-047 needs: `DDPM_2_1` (10-year historical disaster occurrence data) is a lead for sourcing a real agricultural disaster event to build the case study around. `OAE_1_3`/`OAE_1_4` (agricultural area and farming households) could support the exposure side of that case study.

### Developer headstart

REQ-003 is pure explanatory content, no data dependency. REQ-037 (case studies applying projections to planning) needs source material identified first — nothing in either registry currently covers this. REQ-047's agriculture case study is the most tractable of the three gaps; start with `DDPM_2_1` to find a real event to anchor it.

---

## DEL-8 — Policy and institutional content

**Serves** REQ-017, REQ-025, REQ-057 · **Sections** 2.3, 3.3

### Confirmed assets

All three requirements have **no matched asset** — confirmed gap across the board. This deliverable is pure content synthesis (legal instruments, institutional coordination, systemic barriers reporting) with nothing in DCCE's current holdings to build from directly.

### Other potentially relevant datasets

None found — this is legal/institutional analysis work, not something a dataset catalog scan surfaces leads for.

### Developer headstart

All three need original research and writing, not data engineering. REQ-017 and REQ-025 both depend on getting the institutional-actor model right first (LAO vs. line agencies vs. the Governor's office, per Appendix E of the DRD) before drafting content.

---

## DEL-9 — Inclusion and community adaptation content

**Serves** REQ-053, REQ-054, REQ-055 · **Section** 3.3

### Confirmed assets

| Asset | Title | Type | Owner | Link |
|---|---|---|---|---|
| `MED-002` | ซูเปอร์เอลนีโญกับสุขภาพคนไทย ปกป้องชีวิตและกลุ่มเปราะบาง | E-book Reader | กลุ่มประชาสัมพันธ์และสื่อสารสิ่งแวดล้อม | https://www.dcce.go.th/media/26317/ |

Matched to REQ-054 but only topically adjacent (general heat-health vulnerability, not a protection-measures inventory for the four named groups). REQ-053 and REQ-055 have **no matched asset** — confirmed gap.

### Other potentially relevant datasets

Strong leads for REQ-054's four named vulnerable groups (children, elderly, disabled, border/coastal communities): `CDD_1_1` (vulnerable households count), `NESDC_2_1` (elderly >60 and children 0-4 proportions), `NESDC_2_3`/`NESDC_2_4` (elderly and child population counts), `NESDC_2_13` (dependent elderly count), `MSDHS_1_1` (vulnerable group welfare registry — Ministry of Social Development and Human Security), `MSDHS_2_2` (persons with disabilities count).

### Developer headstart

The MSDHS welfare registry (`MSDHS_1_1`) is the most promising lead for REQ-054 — it's the one dataset that's actually about the named vulnerable groups rather than a general demographic proxy. Worth checking its access terms early.

---

## DEL-10 — Adaptation measures library

**Serves** REQ-060, REQ-061 · **Section** 3.3

### Confirmed assets

| Asset | Title | Type | Owner | Link |
|---|---|---|---|---|
| `DAT-022` | ชุดเเนวทางการปรับตัวต่อการเปลี่ยนเเปลงสภาพภูมิอากาศโดยใช้เเนวทางธรรมชาติ (NbS) | Document | กองขับเคลื่อนการปรับตัวต่อการเปลี่ยนเเปลงสภาพภูมิอากาศ | https://dgf.dcce.go.th/dataset/nbs |
| `MED-042` | แนวทางการแก้ปัญหาโดยอาศัยธรรมชาติเป็นฐาน (NbS) | E-book Reader | กลุ่มประชาสัมพันธ์และสื่อสารสิ่งแวดล้อม | https://www.dcce.go.th/media/6463/ |
| `VID-036` | รู้ไหม? ธรรมชาติก็เป็นนักแก้ปัญหาตัวยง! | Knowledge Asset (YouTube) | กลุ่มประชาสัมพันธ์และสื่อสารสิ่งแวดล้อม | https://www.youtube.com/watch?v=cgFAOTv64cE |

All three cover nature-based solutions only. REQ-060 (searchable database) has no matched asset — confirmed gap. Grey/structural infrastructure content (the other half of REQ-061) has nothing behind it.

### Other potentially relevant datasets

None found for grey/structural infrastructure measures specifically — this gap is real and confirmed by the scan, not just by the original gap analysis.

### Developer headstart

The nature-based-solutions half of REQ-061 is well-supported and can move fast. Grey infrastructure content needs to be written from scratch or sourced externally (e.g. from DPT or RID's infrastructure planning material) — nothing in DCCE's own holdings covers it.

---

## DEL-11 — New operational capabilities

**Serves** REQ-071, REQ-073 · **Sections** 4.3, 5.2

### Confirmed assets

Both requirements have **no matched asset** — confirmed gap, as expected. This deliverable is new build work (external portal connections, feedback platform), not content synthesis.

### Other potentially relevant datasets

Not applicable — REQ-071 explicitly names its target portals (TMD weather API, GISTDA geo-informatics portal, Copernicus climate data store) rather than needing a dataset lead.

### Developer headstart

Both requirements are integration/build work. Start REQ-071 by requesting API access terms from TMD, GISTDA, and Copernicus in parallel — that's the actual bottleneck, not implementation.

---

## DEL-12 — Disaster statistics product

**Serves** REQ-001 · **Section** 1.1

### Confirmed assets

`DDPM_2_1` — ข้อมูลเหตุการณ์ภัยพิบัติย้อนหลัง 10 ปี (10-year historical disaster occurrence data). Type: Dataset. Owner: DDPM. Link: https://www.disaster.go.th. Status: Restricted, Baseline-Draft, Unverified-Baseline. Confirmed as REQ-001's real starting point (Boss review, 2026-08-13) — not a from-scratch compilation. Known limitations: reporting is one-way, from local administrative organizations up to province level, with no central ground-truthing, and no UNDRR-aligned hazard taxonomy. These need handling before the data is presentable, but the dataset itself is real.

### Other potentially relevant datasets

Also worth checking against `DDPM_2_1`'s coverage: `DDPM_3_1` (severe drought-affected areas), `DDPM_3_3` (severe flood-affected areas), `DDPM_1_1` (flood risk map) — not yet assessed for this specific use.

### Developer headstart

Start from `DDPM_2_1` directly — request access and evaluate its one-way-reporting and taxonomy gaps first; that's the real work, not gathering records from scratch. This also directly feeds REQ-049 (Loss and Damage dashboard, same DDPM source family) — resolving access to DDPM's disaster-event data once serves both.

---

## DEL-13 — Migrate existing DCCE analytical products onto platform infrastructure

**Serves** REQ-004, REQ-005, REQ-009, REQ-010, REQ-013, REQ-015, REQ-028, REQ-041, REQ-070 · **Sections** 1.1, 1.2, 2.1, 2.2, 2.4, 3.2, 4.2

### Confirmed assets

| Asset | Title | Type | Owner | Link | Flags |
|---|---|---|---|---|---|
| `SYS-003` | ฐานข้อมูลความเสี่ยงจากการเปลี่ยนแปลงสภาพภูมิอากาศ (risk map application) | Data Product | กลุ่มพัฒนาเทคโนโลยีดิจิทัล | https://ccic.dcce.go.th/riskarea | The application itself — REQ-009, REQ-010, REQ-028, REQ-070 |
| `DAT-005` | ข้อมูลความเสี่ยงจากการเปลี่ยนแปลงสภาพภูมิอากาศ (6-sector spatial risk data) | Data Product | กองขับเคลื่อนการปรับตัวต่อการเปลี่ยนแปลงสภาพภูมิอากาศ | https://dgf.dcce.go.th/dataset/db0303-001 | Public but Unverified-Baseline — REQ-005, REQ-009, REQ-013, REQ-015, REQ-028, REQ-041, REQ-070 |
| `DCCE_3_1`–`DCCE_3_7` | Seven-sector composite risk index + climate index, by province | Dataset | DCCE | https://ccic.dcce.go.th/riskarea | Restricted scenarios (ssp585/ssp245 only), Public access, Unverified-Baseline — REQ-004 |
| `DAT-014` | ข้อมูลการประเมินผลการปรับตัวต่อการเปลี่ยนแปลงสภาพภูมิอากาศ | Document | กลุ่มประเมินผลการปรับตัวต่อการเปลี่ยนแปลงสภาพภูมิอากาศ | https://dgf.dcce.go.th/dataset/m-and-e | REQ-015 |
| `MED-004` | ซูเปอร์เอลนีโญกับความมั่นคงด้านน้ำของประเทศไทย | E-book Reader | กลุ่มประชาสัมพันธ์และสื่อสารสิ่งแวดล้อม | https://www.dcce.go.th/media/26076/ | REQ-041 |
| `MED-033` | เกษตรบนเส้นทางเปราะบางต่อภูมิอากาศ : บังกลาเทศ | E-book Reader | กลุ่มประชาสัมพันธ์และสื่อสารสิ่งแวดล้อม | https://www.dcce.go.th/media/22841/ | REQ-041 |

### Other potentially relevant datasets

This deliverable is exactly what the Appendix B2 investigation is meant to resolve — what actually feeds these composite products. Candidate underlying-input datasets to check as part of that investigation: `DDPM_1_1` (flood risk map), `DMR_2_1`/`DMR_2_2` (landslide risk areas), `DPT_1_1`/`DPT_1_5` (urban flood-prone area planning maps, resilient urban planning risk maps), `HII_1_1` (drought risk areas), `LDD_2_7` (drought risk areas, alternate source), `TMD_6_22`–`TMD_6_24` (heat/flood/drought hazard indices). Several agencies maintain parallel hazard-area products that were never cross-checked against DCCE's own composite index — exactly the kind of thing the B2 investigation should surface.

### Developer headstart

Do not start hosting-migration engineering before the Appendix B2 investigation completes — this deliverable is explicitly sequenced after it. When the investigation runs, the datasets listed above are a starting checklist of "other agencies' hazard products that might overlap with or explain gaps in DCCE's own composite index."

---

## Open registry item

`clim-webbased.dcce.go.th` is a real, active DCCE platform — it's the access URL cited inside multiple `data_catalog_v4.csv` rows (`DCCE_2_1`, `DCCE_2_10`, `DCCE_2_11`, `DCCE_2_16`–`DCCE_2_19`, and others) — but it has no entry of its own in either canonical asset registry (`DCCE_Unified_Digital_Asset_Database.csv` or `data_catalog_v4.csv`). It should be registered as its own asset before REQ-035's card treats it as a stable link target.
