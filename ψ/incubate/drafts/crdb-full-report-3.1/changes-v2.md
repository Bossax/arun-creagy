# Changes v1 → v2 — §3.1 (`polished-5.3.1.md` → `polished-5.3.1-v2.md`)

Trigger: committee comment, delivery 4, item 5.3.1 (add data provenance and checkable references), plus Boss's brief (agency-level depth, no per-product catalogue). Mode: **revise**. Headings unchanged. The overall arc is kept: purpose → evidence base (new) → table → landscape → agency accounts → cross-agency synthesis → three gaps → strategic role.

This file has two rounds. Round 1 is the first v2 draft. Round 2 applies Boss's decisions of 2026-09-29, relayed by the coordinator.

## Word count

Counted with pythainlp `newmm` after stripping markdown table and emphasis symbols.

| | Words | Characters (no whitespace) |
|---|---|---|
| v1 `polished-5.3.1.md` | 1,905 | 10,304 |
| v2 round 1 | 5,017 | 26,652 |
| v2 round 2 (current) | 6,379 | 33,633 |

## Round 2 — Boss's decisions applied

1. **TMD and GISTDA accounts added.** They sit after the two DCCE blocks and before DDPM, which groups the climate and hazard data producers ahead of the event, statistics, infrastructure, local, social and economic agencies. Each follows the other agencies' shape (holdings, access, spatial level and rhythm, limits, design implication) and uses a numbered list for the dataset groups. **Source support is catalog-only.** Neither agency was interviewed, the interim report does not describe their products, and WP7 gives only ownership counts plus general gap statements. Both blocks say so in the text. They are about the same length as the others because the catalog rows are detailed (37 and 17 rows), not because there is evidence beyond the catalog.
   - TMD: 37 datasets in five groups. These are 6 WRF forecast outputs (grid, open, images only); the heat index (province, daily, 2014–2019) and event-based storm tracks; 2 datasets DCCE requested for its WebGIS that had not been received when the catalog was compiled; 24 climate-extreme indices including composite heat, flood and drought hazard indices; and 3 input indicators. Also covered: 7 open, 27 with no spatial level recorded, and the ownership ambiguity (the catalog lists TMD as owner but notes the extreme indices are internal data from a DCCE project). The implication is lineage metadata.
   - GISTDA: 17 datasets, 16 open, through four channels. These are the API gateway (10 at 40 m, crops and burnt area), the Disaster Platform (flood extent, hotspots and soil moisture at tambon), the Marine GI Portal (SST, nighttime light) and the Data Cube (imagery), plus 1 input indicator. Limits covered: multi-step access, service versioning, and grid vs administrative units (WP7 Gap 3). The implication is to register channel, version and update rhythm; satellite flood extent may help locate affected areas alongside DDPM records.
   - The WP7 ownership-concentration figure (six agencies hold about half the catalog) is now used in the TMD block, since both missing agencies have accounts.
   - Table 3's external-agency row and the landscape list now name both agencies. The evidence-base block now says TMD and GISTDA were not interviewed. The cross-agency paragraph covers eight agencies and gains one sentence on TMD and GISTDA update rhythms.
2. **`[ต้องตรวจแหล่ง]` markers placed directly after each unsupported claim**, five occurrences in total:
   - the risk map "ได้รับการยอมรับในวงสนทนาระดับจังหวัดและระดับนโยบาย" (DCCE risk-map paragraph), and the same claim in Table 3 row 1, "ดัชนีชี้วัดที่ได้รับการยอมรับ";
   - DLA "อาศัยรอบการรายงานและการประเมินผลประจำปี" (DLA block, and again in the cross-agency paragraph);
   - DGA open data "ปรับปรุงตามรอบสถิติของแต่ละชุด" (cross-agency paragraph). The sentence is split so the marker covers only the DGA half, since the NSO half is supported.
3. **IPCC named.** The text now reads "รายงานฉบับกลางระบุว่า [the model and index layer] พัฒนาตามกรอบความเสี่ยงของคณะกรรมการระหว่างรัฐบาลว่าด้วยการเปลี่ยนแปลงสภาพภูมิอากาศ (IPCC) ในรายงานการประเมินครั้งที่ 6 ของคณะทำงานที่ 2 … พ.ศ. 2565 (ค.ศ. 2022)". One sentence states the framework (interaction of hazard, exposure and vulnerability; responses affect each). There is no chapter or page locator. Table 3 row 1 carries the same attribution in short form. The sidecar holds the URL, and the SREX/AR5 origin is kept in the sidecar only. I wrote "ครั้งที่ 6" rather than "ฉบับที่ 6" to stay clear of the lexicon's `ฉบับ` rule. Note that Table 3 precedes the prose, so "IPCC" appears in the table before its full expansion in the text.
4. **฿1.62 trillion** stays out.
5. **Status items:**
   - DDPM northern 17-province assessment: the procurement status and expected Sep 2569 completion are removed.
   - NESDC: the mid-2569 end date and WP7's "strong candidate for the calculation manual, not confirmed" are removed. The block now says the project was in development when the interim report was written, is now closed, and that the consultants adopted its framework into the **(ร่าง) มาตรฐานชุดข้อมูลขั้นต่ำ (Minimum Viable Dataset: MVD) สำหรับเหตุการณ์ด้านสภาพภูมิอากาศ**. The full name was found in the repo's draft-final-report and exec-summary texts. Table 3 and the cross-agency paragraph are updated to match. The closed status and the adoption rest on Boss's statement (status **B** in the sidecar); the LDM archive's NESDC-input notes give adjacent support only.
   - 5 km downscaled data: the text now states only what WP7 states and attributes it to "กรม สส.". **The research-centre name was dropped.** The repo does have a Thai name for a DCCE centre, "ศูนย์วิจัยการเปลี่ยนแปลงสภาพภูมิอากาศและสิ่งแวดล้อม (Climate Change and Environment Research Center)", but WP7's English name differs ("Climate Change Research Center") and no source ties the 5 km data to that centre. **FLAG**: Boss can reinstate the name if they are the same unit.

## Round 1 — structural changes (still in force)

1. **New evidence-base block** after the purpose paragraph: a numbered list of the four evidence sets, then one paragraph on the catalog's status (all entries draft, none certified, no licence recorded, input-indicator provenance tentative).
2. **Agency accounts under bold lead-ins** (no new numbered headings). There are now ten blocks: DCCE risk map and climate data, DCCE website, TMD, GISTDA, DDPM, NSO, DGA, DLA, MSDHS, NESDC.
3. **v1's DCCE risk-map and website paragraphs split** by job.
4. **v1's external-agency paragraph kept** as the cross-agency synthesis after the agency accounts.
5. **Gap list items 1–3** each gain one catalog-backed example or figure (resolution split 122/41/36/59; about 17% open).
6. **Table caption** changed to "ตารางที่ 3: …" per format rule 9, with a source line added. Table cells were changed only where round 2 required it (row 1 IPCC attribution and marker; external row names TMD and GISTDA and the NESDC wording).
7. **Negation-first constructions** rewritten affirmatively. The closing disclaimer is kept as a trailing clause.
8. **"ประเทศไทยมี…"** changed to "กรม สส. และหน่วยงานภายนอกมี…". The typo "ตอ่" and a stray "ใน" are fixed.

## Added per agency, with source (round 1; see round 2 for TMD, GISTDA, NESDC changes)

| Agency | Added | Source |
|---|---|---|
| All (evidence base) | 11 interviews, 17 Feb–5 Mar 2569; catalog of 260 rows and its provenance split; draft/uncertified/no-licence status | Interview coverage table; data catalog; WP7 §3 |
| กรม สส. risk map | 7 catalog outputs, province/annual/CSV/public, 1960–2100, SSP2-4.5 and SSP5-8.5; third limit (socio-economic data held constant); province lock-in and single-score mechanism | Data catalog; interim report; WP7 Service 2 |
| กรม สส. climate data | 19 gridded datasets and their variables, periods and models; daily/monthly; on request; 5 km downscaled data | Data catalog; WP7 §3, Gap 2 |
| กรม สส. website | Content types; mission-website structure; no spatial user path; 391-holding content check | Interim report; WP7 §6 |
| DDPM | Reporting chain; 15 datasets; village-level event and damage data tied to relief; flood-risk map; northern assessment (no status or date); input indicators; data-flow and taxonomy limits; no monetary figures, ambiguous zeros | Interim report; INT-11; data catalog; WP7 Service 4 |
| NSO | FDES centre; 14 datasets (6 open, 8 on request) with census and survey detail; sample and frequency limits | Interim report; INT-06; data catalog |
| DGA | Interview topics; no DGA-owned datasets; linkage depends on exchange rules and metadata | INT-01; data catalog; interim report |
| DLA | Interview topics; no DLA-owned datasets; LAOs as both data source and user | INT-02; data catalog; interim report |
| MSDHS | 5 datasets; registry, ครู ก., World Bank overlap map; metadata and staffing limits; PDPA aggregation point | Interim report; INT-04; data catalog; WP7 Gap 4 |
| NESDC | 14 datasets; investment risk evaluation (7% discount rate); 13 input indicators; university-led L&D method | Interim report; INT-05; data catalog; WP7 Gap 10 |

## Unsupported claims marked `[ต้องตรวจแหล่ง]` (for Boss's review)

| Claim | Where in text | Why unsupported |
|---|---|---|
| Risk map "ได้รับการยอมรับในวงสนทนาระดับจังหวัดและระดับนโยบาย" / "ดัชนีชี้วัดที่ได้รับการยอมรับ" | DCCE risk-map paragraph; Table 3 row 1 | The interim report says "most advanced" and "most ready for public communication", not "accepted" |
| DLA "อาศัยรอบการรายงานและการประเมินผลประจำปี" | DLA block; cross-agency paragraph | Not in the interim report, INT-02 or the catalog |
| DGA open data "ปรับปรุงตามรอบสถิติของแต่ละชุด" | Cross-agency paragraph | No DGA-specific update-cycle evidence |

## Still flagged or left out

- **Research-centre name** for the 5 km data: dropped (see round 2 item 5).
- **฿1.62 trillion** L&D estimate: out, per Boss.
- **National adaptation monitoring platform** (WP7 Service 7): owner not named in the source, so it is not attributed.
- **OTP, FTI, banks, UDDC, NXPO:** interviewed, but the section does not name them; they appear only in the evidence-base sector list.
- **NESDC's closed status and MVD adoption** rest on Boss's statement, not a document. If a citable record exists (e.g., the MVD chapter of this report), the sidecar row should point to it.

## Lint

`lint_thai_writing.py … --scope report`: **MECHANICAL GATE PASSED** after round 2. Round 2's first run flagged `ผลงาน`, which was changed to `ผลผลิต`. Round 1 fixes: `นอกจากนี้` removed, `การนำทาง` changed to `เส้นทางการใช้งาน`. There are 21 non-blocking PARENTHETICAL notices, all first-occurrence technical terms or proper names (new in round 2: IPCC, Sixth Assessment Report, SPI, Lineage, GISTDA, API, Disaster Platform, Marine GI Portal, GISTDA Data Cube, MVD). The lint ran from a throwaway venv in the session scratchpad because the skill's own `.venv` does not exist.
