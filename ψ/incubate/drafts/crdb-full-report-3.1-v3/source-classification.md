# Source classification — 3.1 rewrite v3 (Stage 1 traceability sidecar)

For every source considered for `argument-map.json`: domain, glossary TERM_ID justifying the
placement, full name (as given in the source, where useful), owning agency, URL or "no URL", and
the catalog row id / asset id / web URL used to find it. TERM_IDs, file names, dataset_ids,
product ids and row ids live in this sidecar only — the map's `claim`/`grounds`/`warrant`/
`application_to_design` fields and its `verbalization_payload` no longer carry any of them, per
Boss's session rule (2026-09-30: "the report is audience-facing final, so no citing of internal
artifacts, notes or interim reports") and Boss's follow-up steer (2026-09-30, after reading the
first map: move internal codes and working-note reasoning out of the map's main fields too, not
just the payload).

No web search was performed by the mapper directly for this run. The two relief/advance-payment
public sources in the loss-and-damage section below were found and verified by Boss, not by this
agent (no web-search tool is available in this session) — see the flag under that section.

Citation form is relaxed as of Boss's second steer: an agency name plus the agency's or system's
website is sufficient in the map and in the eventual prose. Full dataset names are not required.
This sidecar still records fuller detail (dataset titles, row ids) for traceability, but the map
itself does not need to carry it.

## v5 differences (round 3, 2026-09-30)

Boss ruled `data_catalog_v5.csv` replaces `data_catalog_v4.csv` as the basis for this round's
verification. Every source named in `argument-map.json` and every source `draft.md` names was
checked against v5. `writing-contract.json`'s `evidence_policy`/`source_paths` still name v4 —
Boss's instruction for that file was to change only `required_concepts`, `inclusions`, and
`exclusions` and "keep everything else," so the contract's file list was not updated to v5 in this
round. Flagging that inconsistency here for Boss's decision.

**Confirmed unchanged in v5** (title and/or URL match v4, or the URL cited in the map already used
the v5 form): TMD_1_1 (ปริมาณฝนสะสม 1 ชั่วโมง, https://hpc.tmd.go.th/imgda), GISTDA_1_1 (burnt-area
extent, same URL), GISTDA_5_1 (พื้นที่น้ำท่วมซ้ำซาก, https://www.gistda.or.th), DMCR_1_1/DMCR_4_1
(coastal erosion, https://tcs.dmcr.go.th/... — v5 retitles these
"พื้นที่กัดเซาะชายฝั่งจากการวิเคราะห์เชิงพื้นที่" / "...จากการสำรวจภาคสนาม" but the URL is
unchanged), DMCR_3_1/DMCR_3_2 (coral reef / mangrove extent, https://marinemap.dmcr.go.th/),
NSO_1_2/NSO_1_3 (census, https://nsodw.nso.go.th/dwportal/Home.aspx), MSDHS_1_1/MSDHS_1_3
(https://www.m-society.go.th), DDPM_2_3 (ข้อมูลความเสียหายของทรัพย์สินตามรายงานของ อปท.,
https://www.disaster.go.th, still tagged `cdm_sub_domain` LOSS_&_DAMAGE in v5), DMCR_2_1 (coral
bleaching — v5 title "แผนที่ปะการังฟอกขาว", URL https://thailandcoralbleaching.dmcr.go.th/th/home,
same domain as before).

**Changed in v5 — map updated to match:**

| Row id | v4 URL (previous map) | v5 URL (now cited) | Where updated |
|---|---|---|---|
| DMR_2_2 | https://www.dmr.go.th | https://gis.dmr.go.th/DMR-GIS/ | `arg-03` grounds |
| RID_1_2 | https://www.rid.go.th | https://telehydro.rid.go.th/ | `arg-03` grounds (cited as RID's representative URL for the "water-resource monitoring" group) |
| RID_1_11 | https://www.rid.go.th | https://app.rid.go.th/reservoir/ | not cited directly in the map (RID_1_2's URL is used as the group's single representative link); recorded here for completeness |
| DDPM_2_1 | https://www.disaster.go.th; title "ข้อมูลเหตุการณ์ภัยพิบัติย้อนหลัง 10 ปี" | https://catalog.disaster.go.th/dataset/dpm-gd038; v5 title "สถิติการเกิดสาธารณภัยรายหมู่บ้าน"; `cdm_domain` now DISASTER_RECORD (was mixed) | `arg-04` grounds and payload, cited as DDPM's open-data disaster-occurrence source |

**New in v5, not in v4 — the source of arg-05's DDPM damage-value items:** DDPM_3_12
(ความเสียหายจากดินโคลนถล่ม / landslide damage, `LOSS_&_DAMAGE`,
https://catalog.disaster.go.th/dataset/dpm-gd042), DDPM_3_13 (ความเสียหายจากอุทกภัย / flood
damage, `LOSS_&_DAMAGE`, https://catalog.disaster.go.th/dataset/dpm-gd041), DDPM_3_2
(พื้นที่ความเสียหายจากภัยแล้ง / drought damage area, `LOSS_&_DAMAGE`,
https://catalog.disaster.go.th/dataset/dpm-gd028). All three are cited in `arg-05` grouped as
"open data ... covering landslide, flood and drought," with `https://catalog.disaster.go.th/` as
the representative website per the relaxed citation form.

**Owner/URL mismatch — flagged, not guessed at, current map wording kept unchanged:**
`DOHealth_1_2` (สถิติผู้ป่วยจากโรคที่เกี่ยวกับการเปลี่ยนแปลงสภาพภูมิอากาศ) carries `owner_org`
DOHealth (กรมอนามัย / Department of Health) in both v4 and v5, but its v5 `url` is
`https://doe.moph.go.th/app01/?page_id=764`, which by its domain name (`doe.moph.go.th`, "Division
of Epidemiology") looks like it belongs to the Department of Disease Control (กรมควบคุมโรค), not
the Department of Health. `argument-map.json`'s `arg-04` still cites "the Department of Health
(https://www.anamai.moph.go.th)" — the pre-existing, unchanged citation — rather than switching to
the v5 URL, since the owner and the URL's apparent agency disagree and this agent was told not to
guess. **This needs Boss's decision**: whether the owner field or the URL is correct, and whether
the map should cite กรมอนามัย/anamai.moph.go.th (current), กรมควบคุมโรค/doe.moph.go.th (v5's URL),
or both.

**Not found in v5 (confirms Boss's ruling):** `DDPM_3_5` and `DDPM_3_6` (flood duration and depth
in residential areas), already excluded from the map in the prior round, do not appear in v5
either — consistent with Boss's finding that these were never real DDPM holdings.

**RFD_1_2** is present in v5 (พื้นที่ป่าไม้แยกรายจังหวัด / forest area by province,
`LOSS_&_DAMAGE`, https://forestinfo.forest.go.th/Content.aspx?id=10437 — URL also changed from v4's
https://www.forest.go.th) but is removed from the map per Boss's round-3 ruling #1; see "Sources
considered and excluded" below.

## Agency Thai names — sourced vs. confirmed-by-Boss

The `agencies` sheet of the product inventory xlsx gives the official Thai name for 15 of the 17
agencies considered in this review:

| Abbreviation | Official Thai name (agencies sheet) |
|---|---|
| TMD | กรมอุตุนิยมวิทยา |
| GISTDA | สำนักงานพัฒนาเทคโนโลยีอวกาศและภูมิสารสนเทศ (องค์การมหาชน) |
| DMR | กรมทรัพยากรธรณี |
| DMCR | กรมทรัพยากรทางทะเลและชายฝั่ง |
| LDD | กรมพัฒนาที่ดิน |
| DPT | กรมโยธาธิการและผังเมือง |
| NSO | สำนักงานสถิติแห่งชาติ |
| DOH | กรมทางหลวง |
| MSDHS | กระทรวงการพัฒนาสังคมและความมั่นคงของมนุษย์ |
| RID | กรมชลประทาน |
| OTP | สำนักงานนโยบายและแผนการขนส่งและจราจร |
| NESDC | สำนักงานสภาพัฒนาการเศรษฐกิจและสังคมแห่งชาติ |
| DOHealth | กรมอนามัย |
| DDPM | กรมป้องกันและบรรเทาสาธารณภัย |
| DCCE | กรมการเปลี่ยนแปลงสภาพภูมิอากาศและสิ่งแวดล้อม |

Not in the agencies sheet — Boss-confirmed (2026-09-30), flagged as not sourced from the
inventory:

| Abbreviation | Thai name used | Source |
|---|---|---|
| DGR | กรมทรัพยากรน้ำบาดาล | Boss, verbally confirmed; not in the agencies sheet (which lists DWR, กรมทรัพยากรน้ำ, a different agency, but not DGR) |

HII (Hydro-Informatics Institute, สถาบันสารสนเทศทรัพยากรน้ำ (องค์การมหาชน)) is in the agencies
sheet and is cited in `arg-03` for water-resource monitoring; its Thai name comes from the same
`agencies` sheet.

RFD (กรมป่าไม้, Boss-confirmed, not in the agencies sheet) is no longer used in the map as of
round 3 — see "Sources considered and excluded."

## Method (unit arg-01)

Not a per-dataset unit; the definitions of risk, hazard, exposure, vulnerability, and loss and
damage come from the project glossary (`Glossary-v5.csv`: TERM_005, TERM_027, TERM_003, TERM_004,
TERM_006). The dataset/product inventory (section 3.4, underlying files `data_catalog_v5.csv` and
the product inventory's `all_datasets` sheet) and DCCE's digital-asset records (section 2.2,
underlying files `DCCE_Data_Assets.csv`, `DCCE_Unified_Digital_Asset_Database.csv`,
`DCCE_Information_System_Database.csv`) are the instruments used to confirm names and URLs.

## Climate risk assessment domain (units arg-02, arg-03)

Boss's second steer merged the earlier two-unit split (DCCE holdings / line-agency holdings) into
one compact diagnose unit, with a single key message: only DCCE's Climate Risk Database module is
a climate-risk data product in the strict sense; the rest is grouped by kind of data, not listed
dataset by dataset, and not framed as a gap. Round 3 did not change this unit's structure, only
verified and updated URLs against v5 (see "v5 differences" above).

### Cited in arg-03

| Full name / description | Owning agency | TERM_ID | URL cited in map | Row/asset id |
|---|---|---|---|---|
| Climate Risk Database module, on the Climate Change Information Center portal | DCCE | TERM_005/TERM_030 | https://ccic.dcce.go.th/riskarea | DCCE_Information_System_Database.csv asset_id SYS-003 (also DAT-005; product inventory P060) |
| Weather/hazard observation (grouped) | TMD — กรมอุตุนิยมวิทยา | TERM_027/TERM_002 | https://hpc.tmd.go.th/imgda | data_catalog_v5.csv dataset_id TMD_1_1 |
| Satellite hazard monitoring (grouped) | GISTDA — สำนักงานพัฒนาเทคโนโลยีอวกาศและภูมิสารสนเทศ (องค์การมหาชน) | TERM_027 | https://gistdaportal.gistda.or.th/portal/home/index.html | Product Inventory product_id P048 (GISTDA Portal); underlying hazard datasets at GISTDA_1_1/GISTDA_5_1 |
| Geological hazard mapping (grouped) | DMR — กรมทรัพยากรธรณี | TERM_027 | https://gis.dmr.go.th/DMR-GIS/ | data_catalog_v5.csv dataset_id DMR_2_2 (URL updated from v4) |
| Coastal hazard mapping (grouped) | DMCR — กรมทรัพยากรทางทะเลและชายฝั่ง | TERM_027 | https://tcs.dmcr.go.th | data_catalog_v5.csv dataset_id DMCR_1_1/DMCR_4_1 |
| Population/asset exposure baseline (grouped) | NSO — สำนักงานสถิติแห่งชาติ | TERM_003 | https://nsodw.nso.go.th/dwportal/Home.aspx | data_catalog_v5.csv dataset_id NSO_1_2/NSO_1_3 |
| Water-resource monitoring (grouped) | RID — กรมชลประทาน | TERM_004/TERM_003 | https://telehydro.rid.go.th/ | data_catalog_v5.csv dataset_id RID_1_2 (URL updated from v4; RID_1_11's v5 URL, https://app.rid.go.th/reservoir/, is a second RID holding not individually cited) |
| Water-resource monitoring (grouped) | HII — สถาบันสารสนเทศทรัพยากรน้ำ (องค์การมหาชน) | TERM_003/TERM_004 | https://www.thaiwater.net | Product Inventory product_id P056/P057 |
| Social vulnerability registry (grouped) | MSDHS — กระทรวงการพัฒนาสังคมและความมั่นคงของมนุษย์ | TERM_004 | https://www.m-society.go.th | data_catalog_v5.csv dataset_id MSDHS_1_1/MSDHS_1_3 |

**Flag — dropped claim (carried over from round 2):** the earlier map version argued that DCCE's
holdings run at national or sectoral index level while line-agency holdings run at asset, station
or village level, as the basis for calling the relationship "complementary." Boss's second steer
dropped this claim as unsourced; `arg-03` argues a different, sourced distinction (risk product
vs. response/warning data) and does not use complementarity language.

**Flag — two-domain candidate, not cited in the current map:** DMCR coastal erosion data
(`DMCR_1_1`/`DMCR_4_1`) is tagged HAZARD in the catalog and could instead read as a loss-and-damage
record (land already lost). Boss confirmed on 2026-09-30 that it stays under climate risk
assessment. It is folded into the "coastal hazard mapping" group in `arg-03` above rather than
named individually, consistent with the relaxed citation form.

**Not cited in the current map, considered in an earlier version:** DPT flood-prone planning maps
(กรมโยธาธิการและผังเมือง, https://www.dpt.go.th, DPT_1_1), LDD recurrent flood-area maps
(กรมพัฒนาที่ดิน, http://sql.ldd.go.th/ldddata/mapsoilH2.html, LDD_1_1), DOH road network and
repeat-flood-area road length (กรมทางหลวง, https://hris.doh.go.th/highway /
https://www.doh.go.th, DOH_1_1/DOH_2_1), DGR groundwater abstraction (กรมทรัพยากรน้ำบาดาล,
https://www.dgr.go.th, DGR_1_1), OTP transport-infrastructure risk assessment
(สำนักงานนโยบายและแผนการขนส่งและจราจร, https://www.otp.go.th, OTP_1_1), and NESDC infrastructure
investment climate-risk evaluation (สำนักงานสภาพัฒนาการเศรษฐกิจและสังคมแห่งชาติ,
https://www.nesdc.go.th, NESDC_1_1). These remain valid, sourced examples of the same grouped
kinds cited in `arg-03`; they are not individually named in the map because Boss's steer calls for
a few representative agencies per kind, not a long list. Stage 2/3 may swap in any of these in
place of the currently cited example for the same group if a different representative agency is
preferred. (Not re-verified against v5 in this round, since they are not currently cited.)

## Climate impact domain (unit arg-04)

| Full name / description | Owning agency | TERM_ID | URL cited in map | Row id |
|---|---|---|---|---|
| Disaster-occurrence statistics, published as open data | DDPM — กรมป้องกันและบรรเทาสาธารณภัย | TERM_045 Disaster Record | https://catalog.disaster.go.th/ | data_catalog_v5.csv dataset_id DDPM_2_1 (v5 title "สถิติการเกิดสาธารณภัยรายหมู่บ้าน"; URL updated from v4's www.disaster.go.th to catalog.disaster.go.th/dataset/dpm-gd038) |
| Locally (LAO) reported damage counts on roads, livestock and temples | DDPM — same | TERM_045 | https://www.disaster.go.th | DDPM_2_3 (unchanged in v5; still tagged `LOSS_&_DAMAGE` in the catalog, override explained below) |
| Climate-linked illness statistics | DOHealth — กรมอนามัย | TERM_045-style sectoral impact statistic | https://www.anamai.moph.go.th | DOHealth_1_2 — **owner/URL mismatch in v5, see "v5 differences" above; current citation kept unchanged pending Boss's decision** |
| GIS system compiling hospital locations with climate-disease statistics | DOHealth — same, with MoPH — กระทรวงสาธารณสุข | same | https://gis-health.moph.go.th/ | Product Inventory product_id P084 (not in data_catalog, not re-verified against v5) |

**Reasoning for the impact/loss-and-damage line (kept out of the map's main fields per Boss's
steer, recorded here instead):** `data_catalog_v5.csv` tags the DDPM row `DDPM_2_3` as
`cdm_sub_domain` LOSS_&_DAMAGE. Per Boss's ruling, this specific dataset (LAO-reported damage
*counts*, not damage *values*) is closer to human/asset impact than to a completed loss valuation,
so it stays under climate impact here, overriding the catalog's own tag. This is distinct from the
round-3 addition to `arg-05` of DDPM's damage-*value* datasets (DDPM_3_12, DDPM_3_13, DDPM_3_2),
which do carry a value and were moved to loss and damage. This override is deliberate, not an
oversight.

**Scope note:** DDPM's own systems/platforms (Disaster Information Center, DPM Portal, DDPM
Dashboard, alert apps) are not named in this section because they risk restating chapter 4.1's
disaster-reporting-system methodology; only DDPM's underlying datasets are cited.

## Loss and damage domain (unit arg-05)

### (a) and (b): catalog-sourced

| Full name / description | Owning agency | TERM_ID | URL cited in map | Row id |
|---|---|---|---|---|
| Coral bleaching monitoring (also published as Thailand Coral Bleaching Assessment System) | DMCR — กรมทรัพยากรทางทะเลและชายฝั่ง | TERM_006 Loss & Damage | https://thailandcoralbleaching.dmcr.go.th/ | data_catalog_v5.csv DMCR_2_1; Product Inventory product_id P082 |
| Damage from landslide (ความเสียหายจากดินโคลนถล่ม) | DDPM — กรมป้องกันและบรรเทาสาธารณภัย | TERM_006 | https://catalog.disaster.go.th/ | data_catalog_v5.csv dataset_id DDPM_3_12 (https://catalog.disaster.go.th/dataset/dpm-gd042) |
| Damage from flood (ความเสียหายจากอุทกภัย) | DDPM — same | TERM_006 | https://catalog.disaster.go.th/ | DDPM_3_13 (https://catalog.disaster.go.th/dataset/dpm-gd041) |
| Damage area from drought (พื้นที่ความเสียหายจากภัยแล้ง) | DDPM — same | TERM_006 | https://catalog.disaster.go.th/ | DDPM_3_2 (https://catalog.disaster.go.th/dataset/dpm-gd028) |

### (c): government relief and advance-payment mechanisms

**Sourcing note — read before using this section:** these two mechanisms were identified and
verified by **Boss**, through public web search outside this agent's session (this agent has no
web-search tool). The mechanisms themselves (the regulation, the budget line, the example news
report) are public and citable. The specific link between DDPM and these payment records — i.e.
the claim that DDPM itself keeps or maintains records of payments made under either mechanism —
is **Boss-sourced, not publicly documented** (it rests on Boss's own knowledge and interview
notes). That specific claim does not appear anywhere in `argument-map.json`, including
`grounds`/`warrant` and every `verbalization_payload`. The map states only that a payment under
either mechanism carries a monetary value attached to a realized loss — a general, publicly
verifiable fact about how the mechanisms work, not a claim about who archives the record.

| Mechanism | Legal/institutional basis | Public source(s) | Opened by Boss? |
|---|---|---|---|
| Advance payment by the responsible agency (เงินทดรองราชการ) | ระเบียบกระทรวงการคลังว่าด้วยเงินทดรองราชการเพื่อช่วยเหลือผู้ประสบภัยพิบัติกรณีฉุกเฉิน พ.ศ. 2562, in force from 14 May 2562, made under the Public Financial Management Act 2561 (พ.ร.บ. วินัยการเงินการคลังของรัฐ พ.ศ. 2561) | Royal Gazette PDF: https://www.ratchakitcha.soc.go.th/DATA/PDF/2562/E/120/T_0036.PDF ; DDPM's operating manual for paying it: https://backofficeminisite.disaster.go.th/apiv1/apps/minisite_cco/204/sitedownload/32432/download?TypeMenu=MainMenu&filename=9e04f4dc2c7eeb675fc27762fa4373e3.pdf | Gazette PDF: found by search, not opened. Operating manual: not marked as opened. |
| Cabinet-approved payment from the central budget's emergency reserve (งบกลาง รายการเงินสำรองจ่ายเพื่อกรณีฉุกเฉินหรือจำเป็น) | Cabinet resolution, case by case; no standing regulation cited | Government Public Relations Department: https://saraburi.prd.go.th/th/content/category/detail/id/516/iid/433646 (reports Cabinet approval of direct bank-transfer payment to flood-affected households from this budget line) | Yes — opened and verified. |
| (Explanatory page, not used as a citation) | — | https://library.parliament.go.th/en/radioscript-rr2564-jan1 | No — 403 error, not opened. |

Both mechanisms are cited in `arg-05` by agency/institution name and website only, per the relaxed
citation form (Ministry of Finance regulation as the legal basis for the advance payment; the
Government Public Relations Department page as the example evidencing the central-reserve
mechanism). No baht amounts, payment counts, or household numbers appear in the map — per Boss's
explicit instruction, these never belong in `verbalization_payload`.

**Flag — thin even after these additions:** loss and damage remains the thinnest of the three
domains. Adding DDPM's damage-value datasets and the two relief mechanisms does not change that;
`arg-05`'s `application_to_design` instructs the writer to say so plainly rather than let the new
material read as if the domain were now well supplied.

## Sources considered and excluded

- International/global platforms in the product inventory (UNEP Strata, ENCORE, WESR Climate,
  ABC Map, EM-DAT, and similar, product_id P001–P037, P100, P101, P103, P104) are not Thai line
  agencies or DCCE, so they are out of the "DCCE and other line agencies" scope this section
  covers.
- T-Plat Info (product P061, thailandadaptationinfo.dcce.go.th) is excluded to avoid restating
  section 2.2's T-PLAT platform history.
- DCCE's Heat Index Platform (P063) and DDC's Disease & Health Forecast Tool (P064) were
  considered for the climate impact domain but excluded: both are forward-looking forecast/
  monitoring tools, not records of a realized impact, so under the domain definitions they read as
  risk-domain content (folded conceptually into the "weather and satellite hazard monitoring"
  group in `arg-03` rather than named individually).
- Flood duration and depth in residential areas (catalog rows DDPM_3_5, DDPM_3_6): excluded by
  Boss 2026-09-30; catalog source is the DCCE risk-database project report, ownership unconfirmed,
  modelled 1960-2100. Confirmed absent from `data_catalog_v5.csv` as well.
- Forest area by province (RFD_1_2, พื้นที่ป่าไม้แยกรายจังหวัด, กรมป่าไม้,
  https://forestinfo.forest.go.th/Content.aspx?id=10437 in v5, https://www.forest.go.th in v4):
  excluded by Boss 2026-09-30, round 3 — this is neither impact nor loss-and-damage data. It is a
  baseline area figure, not a record of loss that has occurred, even though the catalog tags it
  `LOSS_&_DAMAGE`. Removed from `arg-05` and from every other unit in the map.


## IPCC citation (added 2026-09-30, Boss's instruction)
- IPCC (2022), Climate Change 2022: Impacts, Adaptation and Vulnerability (AR6 WGII), Annex II Glossary: https://www.ipcc.ch/report/ar6/wg2/chapter/annex-ii/ . Risk, vulnerability, exposure and hazard wording matches the glossary text as returned by web search. The page returned HTTP 403 to the fetch tool, so it was not opened directly.
- Framework: Chapter 1 'Point of Departure and Key Concepts': https://www.ipcc.ch/report/ar6/wg2/chapter/chapter-1/ (verified in the earlier v2 traceability file).
- Loss and damage: the Thai definition is not an IPCC quotation (glossary anchor 'IPCC / DCCE M&E Platform'); left uncited in the text pending Boss's choice of source.
