# NCAIF Website — Content Storyboard and Synthesis Guide

**Date** 13 August 2026
**Companion to** `2026-08-12-WP4-Developer-Ready-Design-Requirements-Specification.md` and `2026-08-13-WP4-DRD-Deliverable-Asset-Mapping.md`

## What this document is

The Developer-Ready Design Requirements Specification tells a developer what to build. This document tells a DCCE content owner what each page should actually say, in what order, and how close it is to ready. It covers all 31 addressable pages in the site map, in site order, from the front page through to the feedback channel.

**Structure note (19 August 2026):** Per the Homepage Concept draft (`2026-08-19-WP4-Homepage-Concept.md`), 1.1.1 and 1.1.2 — previously nested under "1. หน้าแรก — Home" — now sit in their own Country Overview section, a sibling of Home rather than Home's content. Home becomes a router (search + task-based service cards); 1.2 (Area Search) is what stays on it. Node codes are unchanged here pending the Tier 1 sitemap-data update.

Each page gets three things:

**A readiness score, from 1 to 5.** This is a quick way to judge how much work a page needs before it can go live.

- **5 — Ready to format.** Real, matched material covers the page in full. The only work left is porting it into the page.
- **4 — Ready to compile.** Real material exists but is scattered across documents. It needs compiling into one page, not new research.
- **3 — Ready to synthesize.** Real underlying data exists but needs computation, structuring, or synthesis before it is presentable.
- **2 — Needs new content.** Little or no existing material. Original writing or research is required, but nothing outside DCCE is blocking it.
- **1 — Blocked.** The page cannot meaningfully move forward until an external agreement, a DCCE decision, or another work package's output exists.

**A content storyboard.** What the page should contain, in the order a reader would encounter it. This is not a developer specification. It is a description of the reading experience, written so a content owner can picture the finished page.

**A synthesis starting point.** What already exists, who owns it, and what a content writer or analyst should do first to start building the page from what is available today.

Some pages hold content that depends on a decision DCCE has not made yet, or on a separate work package's methodology landing first. Where that is the case, this document says so plainly and keeps that content visually separate from what is already committed.

---

# ภาพรวมประเทศ — Country Overview (sections 1.1.1–1.1.2)

##  1.1.1 — Overview of Thailand's climate risk

**Readiness: 2/5 — Needs new content**

Part of this page is finished (the concept definitions in REQ-002) and part of it now has a real dataset behind it (REQ-001), but two pieces still need genuinely new work: the physical-versus-transition-risk explainer has nothing written yet, and the risk summary cards depend on an investigation that hasn't happened.

### What this page should contain, in order

1. A short opening statement on why climate risk matters for Thailand, setting up everything that follows. Nothing in the current requirements writes this explicitly, but the page needs it before the detail begins.
2. The IPCC framework for hazard, exposure, and vulnerability, defined in Thai and English (REQ-002). This is already covered material, so it can go up largely as-is.
3. Physical risk and transition risk, defined and contrasted with Thai examples, connected forward to the risk-analysis sections and to the policy sections including the Climate Change Act and the EU's CBAM (REQ-003).
4. National risk summary cards showing the seven-sector composite index at a glance (REQ-004). These should carry a visible flag that the underlying figures are still draft and unverified, and a note that the composite index is currently the only available measure for this purpose, not necessarily the right one long-term.
5. History and trends of natural disaster events in Thailand, shown as an interactive chart covering at least the last two decades, built from DDPM's disaster occurrence data (REQ-001). The chart should state its source and period clearly and link out to the disaster statistics product, not the Thailand Climatology Dashboard — disaster events and losses are a different, politically-determined dataset from the Dashboard's meteorological and climatic variables, and the two should not be cross-linked as if they were the same product.

### What's already there and how to start

- REQ-002 is done. DCCE's impact chain manual and the IPCC-tagged dataset already say what's needed — the dataset is explanatory/definitional grounding for the IPCC framework terms, not an analytical input the page computes from. Port this content directly.
- REQ-007-style success content does not belong here (it's on the next page), so skip ahead for that.
- REQ-003 has nothing to build from. Someone needs to write the physical-versus-transition-risk explainer from scratch, including at least two Thai examples for each term and the link to the Climate Change Act and CBAM.
- REQ-004 has real numbers behind it (the seven-sector composite index, `DCCE_3_1` through `DCCE_3_7`), but nobody has confirmed whether those numbers are fit to show as summary cards, and they carry a draft/unverified flag. Wait for the hosting-migration investigation (DEL-13) before publishing this with confidence, or publish now with the draft flag stated plainly.
- REQ-001 has a real starting point: `DDPM_2_1`, DDPM's ten-year disaster occurrence dataset. It is not a from-scratch compilation job anymore. The first step is requesting access and working through its known problems (reporting only flows one way from local administrations up to the province, nobody checks it against the ground, and it doesn't use the standard UNDRR hazard categories). Those caveats need to show on the page, not be hidden. This same DDPM data also feeds the future Loss and Damage dashboard, so the data-gathering step should happen once and serve both.

---

##  1.1.2 — Thailand's key risks and adaptation priorities

**Readiness: 3/5 — Ready to synthesize**

The hotspot synthesis for this page draws on a literature review, not on the spatial risk database (risk map) product, which is why readiness stays at 3/5. (Side note: if sub-district-level risk turns out to be required instead, readiness drops to 1/5, blocked by data availability.)

Two of the three pieces here are genuinely finished and just need to be laid out. The third, the hotspot map, has a real problem: it was recorded as complete on the assumption that the risk map shows location-specific detail, and it does not.

### What this page should contain, in order

1. Critical hotspots by sector and region, drawn from the same composite risk data used elsewhere on the site. This needs a visible caveat: the underlying index is province-level, so anything presented as a finer-grained hotspot is not actually spatially precise yet (REQ-005). Presenting these hotspots at province scale is pending DCCE's explicit sign-off on whether that scale of "hotspot" presentation is useful at all; if DCCE does not approve it, this section falls back to literature-reviewed content instead.
2. A summary of Thailand's National Adaptation Plan, giving the reader the country's overall direction after the risk picture, so the plan reads as a response to the risk just shown (REQ-006).
3. Examples of high-value adaptation measures that have worked in Thailand, moving the page from problem framing into concrete solutions (REQ-007).

### What's already there and how to start

- REQ-006 is done. The National Adaptation Plan itself, its dataset entry, and several Thai and English explainers already exist. Port this content directly.
- REQ-007 is done. A success-factors article covering six sectors already exists, and the nature-based solutions guidance dataset (`DAT-022`) backs it directly. Cite that dataset by name rather than describing it vaguely.
- REQ-005 needs care before it goes up as "complete." The composite risk data is real, but do not publish or imply hotspots below province level until the Appendix B2 investigation confirms what the index actually supports. In the meantime, present the hotspots explicitly as province-level, with the same draft and unverified flag the underlying data carries, and hold this section for DCCE's explicit approval on whether province-level "hotspot" framing is worth shipping at all — without that approval, fall back to literature-reviewed content instead.

---

# 1. หน้าแรก — Home

##  1.2 — Area-based data search

**Readiness: 2/5 — Needs new content**

This is an interactive search tool, not a content page, and it needs real interface and fallback-logic work. It is also a different access surface onto the same composite risk index / risk map used across the site (see also 1.1.2 and 2.2, which surface the same underlying data), not a separate analytical build — worth keeping in mind so this and related pages aren't scoped as if each needed its own new analysis. None of its three pieces has a matched data asset behind it yet, and one part (recommended measures for a selected point) has nothing anywhere on the site to draw from.

### What this page should contain, in order

1. A search that lets a user pick a province, then a district, then a sub-district (REQ-008). This follows the standard government administrative hierarchy, which is a different geography from Local Administrative Organization boundaries, so a "district" or "sub-district" pick will not always match a municipality's real boundary.
2. A result view that always shows something. When finer-than-province data does not exist, the province figure should display with a clear label saying so. It should never come back empty or imply there is no risk when the truth is that there is no data yet.
3. A map showing administrative boundaries layered over the risk map, with the same province-level caveat carried through visually (REQ-009).
4. A quick-view summary for a selected point, covering three things per the sitemap: vulnerability, main hazards/threats, and recommended measures. Show whatever vulnerability and hazard information genuinely exists, and mark the "recommended measures" portion as not yet available rather than leaving it blank without explanation (REQ-010). The "vulnerability" shown here is the non-climatic parameter grouping already inside DCCE's risk map, so this needs to add real value beyond re-displaying that same figure — otherwise it is just a repeat of what 1.1.2 and 2.2 already show.

### What's already there and how to start

- REQ-008 has no matched asset. The province-level composite data it would draw on (`DCCE_3_1` through `DCCE_3_7`) exists but stops at the province. Build the fallback behavior first (always show a labeled result, never a blank one) since that is the part of the specification that actually determines whether the tool feels broken. Closing the gap below province level is a separate, larger undertaking, either compiling content from Provincial Climate Change Plans and Disaster Prevention & Mitigation Plans, or re-working the underlying data onto real municipal geometry.
- REQ-009 can use the existing risk-map application as its base, but it can only meaningfully show province-level boundaries for now. Say so on the page rather than letting the map imply finer coverage than the data supports.
- REQ-010 can also start from the existing risk-map application for the point-lookup interaction, but there is no dedicated quick-view product today, and neither the vulnerability-and-hazard content nor the recommended-measures content has been compiled anywhere on the site, at any level. Since this quick-view content covers the same "country risk" ground as 1.1.2 (Thailand's key risks and adaptation priorities), build the two together rather than as independent efforts — they can share underlying content while differing in framing (general risk overview vs. point-specific lookup).

---

# 2. ศูนย์ข้อมูลสำหรับผู้กำหนดนโยบายและแผน — Policy maker information center

##  2.1 — National climate change situation

**Readiness: 2/5 — Needs new content**

One piece of this page has real underlying data waiting on an access decision, one needs reframing rather than new data, and one is genuinely stuck until a separate work package finishes its methodology.

### What this page should contain, in order

1. Historical extreme weather statistics, anchoring the page's "numbers" focus (REQ-011). This should be built from DDPM's disaster occurrence data, not the Thailand Climatology Dashboard — disaster events and losses are a distinct, politically-determined dataset from the Dashboard's meteorological and climatic variables, and the two should not be conflated here either.
2. National exposure trends, presented next to the disaster-history content rather than as an isolated chart, with a plain note that only exposure, not hazard or risk, can be shown as a trend given current data (REQ-013). This is a long-term monitoring-design problem, not a simple chart: the exposure variables shown need to be chosen against defined criteria for giving an unbiased picture of Thailand's climate exposure, not picked ad hoc through stakeholder consultation alone. Until that criteria-based selection is done, fall back to a descriptive summary rather than presenting an unvetted trend.
3. A forward-pointing note on national macroeconomic loss and damage statistics, explaining that this section will host a summary view once the Loss and Damage dashboard exists elsewhere on the site, with a link there rather than a placeholder chart (REQ-012).

### What's already there and how to start

- REQ-011 has been re-scoped: it draws on `DDPM_2_1`, DDPM's ten-year disaster occurrence dataset (the same dataset backing REQ-001 in section 1.1.1), not on the Thailand Climatology Dashboard's grids (`DCCE_2_1`, `DCCE_2_2`). This is now reflected consistently across the DRD, the Deliverable-Asset Mapping, and all five DRD CSVs — REQ-011 moved from DEL-1/DS-02 to DEL-12/DS-08.
- REQ-013 does not need new data collection, but it does need a criteria-based selection pass before the six-sector spatial dataset already in use elsewhere on the site can be shown as a monitoring trend. State plainly on the page that it only supports a trend for exposure, not for hazard or risk, place it next to the disaster-statistics content rather than on its own, and use a descriptive summary instead of a computed trend until the underlying variables have been checked against defined criteria.
- REQ-012 has nothing to build yet. Don't attempt an independent macroeconomic loss database. Point to the future Loss and Damage dashboard instead, since the loss-and-damage work package's own methodology has not been published.

---

##  2.2 — Area and sector risk profiles

**Readiness: 2/5 — Needs new content**

This page is the same underlying tool and data as 1.2 (Area-based data search), presented for the policy-maker audience — the two should be built identically underneath, differing mainly in their introductory framing, not as two separate builds. The province-level version of this page is buildable now, using real source material beyond the single composite index, but both pieces need the same honest caveat: nothing below province level exists yet, and no source has been assessed for how to close that.

### What this page should contain, in order

1. An introductory paragraph framed for a policy maker or planner: what this profile is for and how to use it when comparing provinces or sectors, distinct from 1.2's general-search framing but built on the same underlying data.
2. One consistent profile structure for all 77 provinces, covering main hazards, exposed sectors, and the vulnerability picture, so any two provinces can be compared side by side (REQ-014).
3. Within that structure, a breakdown for the six priority sectors, drawing on the same risk data used across the site rather than a separately built dataset (REQ-015).
4. A clear, plainly worded note, repeated wherever relevant, that municipality-tier Local Administrative Organization coverage is not available at this level, and why, plus a visible flag on any figure carried over in draft or unverified status.

### What's already there and how to start

- The introductory paragraph is the only genuinely new writing this page needs beyond what 1.2 already requires — write it once 1.2's underlying tool is scoped, so the two pages share build effort rather than duplicating it.
- REQ-014 has no matched asset in the formal registry yet, but real building blocks exist. The province-level composite index (`DCCE_3_1` through `DCCE_3_7`) is the backbone. Beyond that, NESDC's provincial indicators (poverty, elderly and child counts, human development index, income per capita) and NSO's census series (population and housing, agriculture, labor force, socio-economic survey) are strong, not-yet-checked leads for making these profiles more than a single index number. Confirm access terms on the NESDC and NSO material before relying on it.
- REQ-015 can reuse the same six-sector spatial dataset and the adaptation-evaluation dataset already used elsewhere on the site. Nothing new needs to be collected. The work here is presentation and honesty about the province-level limit, not new data gathering.

---

##  2.3 — Climate Change Act status and supporting laws

**Readiness: 2/5 — Needs new content**

One part of this page is already finished, one needs original writing, and one is a separate, not-yet-decided feature — the page as a whole is not close to done.

### What this page should contain, in order

1. The current status of the draft Climate Change Act: what stage it is at, what the act does, and links to the official summary and the full draft text. This part is ready now.
2. A summary of the other laws and policies that support adaptation action, built the right way round: start from the adaptation measures the site already describes, then work backward to which legal instruments back them up, not the other way around. At minimum, this must cover the Disaster Prevention and Mitigation Act and town planning ministerial regulations — both currently uncovered anywhere on the site, and both explicitly required. Each law should say plainly whether it applies to a Local Administrative Organization (LAO), to a specific line agency, or to both, since LAOs and line agencies operate under different legal bases and a law that does not say who it binds is not usable by either.
3. If DCCE decides to build the avoided-losses certification system, a clearly marked section describing that feature in plain terms: a formal system for certifying an agency's avoided-losses calculation — validating that a climate-resilient design's higher upfront cost is justified by the future losses it avoids, so the agency can cite that certification when justifying its budget request to สตง (the state audit office). This is a separate, not-yet-decided feature (see the financial evidence service, Brief E-1, in Appendix B of the DRD) and should not be blended into the two sections above, since committing to build it is a decision DCCE has not made yet.

### What's already there and how to start

- The Climate Change Act summary is ready to use directly: the official summary, the full draft text, and two existing explainer pieces (owned by the strategy and international cooperation division) cover this in full. Port this content as-is.
- Nothing exists yet for the supporting-laws summary, including the two laws explicitly required: the Disaster Prevention and Mitigation Act and town planning ministerial regulations. Before writing, get the correct list of adaptation measures the rest of the site already covers, since the law list has to be built from that, not from a general legal survey. Then identify which laws apply to LAOs and which apply to named line agencies — this determines how the content gets organized, not just how it reads.
- The certification-system section is not something to start on now. It only becomes real work if DCCE decides to commission the financial evidence service described in Appendix B.

---

##  2.3.1 — Funding, budget evidence and finance tracking

**Readiness: 1/5 — Blocked**

All four items on this page depend on DCCE deciding to commission the financial and budget evidence service. None of them can be finished without that decision, though a lighter interim version of one piece is possible now.

### What this page should contain, in order — if DCCE commits to this service

1. A directory of funding sources: the Adaptation Fund, the Green Climate Fund, the Global Environment Facility, and DCCE's own funding guide.
2. Cost-benefit guidance for using those funds to justify adaptation spending, including how a climate-resilient design's cost compares to a historical benchmark.
3. Budget allocation statistics and climate budget tagging, so spending on adaptation can be tracked as its own category.
4. Tracking of financial, technology, and technical assistance received, covering both money and the technology-transfer and capacity-building side, which nothing currently tracks at all.
5. An assessment of private sector participation in adaptation finance.

None of this should be built as a full specification yet. If DCCE has not committed to the service, this page should stay a short description of what it would eventually hold, not a built-out feature.

### What's already there and how to start

- The funding directory itself has real material to draw on right now, independent of the larger decision: DCCE's own funding guide, and dedicated publications for the Adaptation Fund, Green Climate Fund, and Global Environment Facility (all owned by the strategy and international cooperation division). A simple directory listing these could be published as an interim step even before DCCE decides on the full service, converted into a summary or explainer style that also links back to the original source rather than a bare listing.
- Everything past that (cost-benefit method, budget tagging, technology and technical-assistance tracking, private-sector mobilization) has nothing behind it. The existing GCF/AF/GEF-related assets, including the no-objection endorsement process material, only track money moving through those specific channels. They do not cover technology transfer or capacity-building support at all, which is a real, repeated gap DCCE should know about before scoping the service.
- Do not start building the cost-benefit methodology or budget-tagging pieces until DCCE has actually decided to commission this. The first real step is that decision, not a content draft.

---

##  2.3.2 — Institutional Governance and Coordination

**Readiness: 4/5 — Ready to compile**

Three of the four pieces on this page already exist and mostly need porting. The fourth needs new writing, but it is content only, with nothing blocking it.

### What this page should contain, in order

1. DCCE's role as Thailand's national focal point for international climate finance coordination.
2. The structure of the national climate policy committee and its sub-committees.
3. How national and local government coordinate on adaptation, described the way it actually works: each central-ministry line agency runs its own line down to its own provincial office (the general provincial administration, including DOPA's own office, is itself one line agency among these, not something separate). Local Administrative Organizations — municipalities and อบจ. — operate on their own, centrally-funded authority. The Governor, a DOPA official, provides a loose coordinating role across the province's line-agency offices, and that looseness should be described as how it actually works, not written up as if it were a gap.
4. Participation channels and statistics for civil society, the private sector, and academic institutions.

### What's already there and how to start

- DCCE's focal-point role, the committee structure, and the participation statistics are all ready to use directly: real institutional documents, committee appointment orders, and multi-year disclosure publications with an active tracking system behind them. Port these three sections with minimal editing.
- The coordination page (item 3) needs to be written from scratch, but it does not depend on any dataset. The main risk is getting the institutional model wrong — treating this as one national-to-local hierarchy instead of two separate channels (line agencies down their own line, LAOs on their own authority) plus the Governor's loose convening role. Write this section only after confirming that model, since it changes both what gets said and how it is organized.

---

##  2.4 — Planning data services

**Readiness: 2/5 — Needs new content**

This page is a planning-guideline hub, not a bare list of tools — it needs an opening frame that ties the two analytical tools below to an actual planning use case before either tool is presented, plus a forward pointer to tools not yet built. One tool is a straightforward explainer that can be written now. The other depends on an investigation that has not happened yet and should not be assumed finished.

### What this page should contain, in order

1. A short planning-guideline framing: what a planner should come to this page to do, and how the tools below support that task. Without this framing the page is just a hub of links, not planning guidance.
2. An explainer introducing the idea of a "Climate Resilience Index" — what it would measure, the reasoning behind it, and how it relates to the risk framework used elsewhere on the site. Alongside the concept, publish the intended method in principle: which categories of indicator it would draw on and roughly how they'd be weighted. This is a concept-and-method explainer, not a working tool — it should not present any computed per-province numbers, since the actual index has not been built and computing it is separate, later work.
3. A section presenting DCCE's integrated spatial risk map as an existing tool a reader can use. This section carries an important caveat: whether the map is actually fit for this purpose has not been confirmed, and it should not be presented as finished until the investigation described in Appendix B2 of the DRD, and the related infrastructure work in DEL-13, are both done.
4. A forward-pointing note on other planning tools still to come, such as the disaster statistics product, so the page reads as a growing planning hub rather than a closed list.

### What's already there and how to start

- The planning-guideline framing has nothing to draw from yet and needs to be written first, since it determines how the rest of the page is organized, not just how it opens.
- For the Climate Resilience Index explainer, one existing media piece explains how vulnerability and adaptive capacity are measured (owned by the communications division) — use it as a starting reference for the concept explanation, but write new content rather than reusing it directly, since it does not name or frame the index concept itself. The "method in principle" component (indicator categories, rough weighting) also has to be written from scratch — nothing today states even a proposed method, only the underlying proxy indicators (station density, water monitoring counts, agricultural census measures) that a future method could draw on.
- For the risk map section, the map application itself is real and live. But do not describe it as finished. The composite data behind it needs the Appendix B2 investigation before anyone can say what it actually supports. Flag this section as pending rather than presenting the map as a complete answer to this requirement.
- The forward-pointing note on future tools has nothing to draw from yet beyond naming the disaster statistics product as the clearest known candidate.

---

# 3. วงจรขับเคลื่อนการปรับตัว — Adaptation knowledge cycle

##  3.1.1 — Weather stations, satellite data and global climate monitoring

**Readiness: 2/5 — Needs new content**

Nothing here needs new data work from DCCE. All three pieces are explainer content that link out to other agencies, which is lighter than a data-build but still needs original writing.

### What this page should contain, in order

1. An explainer on weather station observation data: what it is, how it differs from the modelled climate grids used elsewhere on the site, and a link to Thailand's Meteorological Department (TMD), who already holds and publishes this data.
2. An explainer on satellite observation data covering forest cover, land cover, water bodies, and coral bleaching, each with a link to the agency that actually publishes it — GISTDA for land and water layers, the relevant marine body for coral.
3. An explainer on ENSO and the Indo-Pacific/Interdecadal Pacific Oscillation (IPO), what they mean for Thailand's coming season, with a link to TMD's or another authoritative source's live monitoring rather than a DCCE-run feed. The Atlantic overturning circulation gets a short explanatory mention only, since Thailand has no monitoring role for it.

DCCE does not need to build its own version of these monitoring dashboards. GISTDA and TMD already run this work, and DCCE's role here is to explain and point readers to the right place, not to duplicate it.

### What's already there and how to start

- Station data (item 1): nothing exists in DCCE's holdings, which is expected, since TMD holds this. Write the explainer and confirm the correct TMD service to link to before publishing.
- Satellite data (item 2): nothing exists in DCCE's holdings either. GISTDA and the relevant marine bodies hold the real products. Confirm the specific GISTDA and marine-body pages to link to for each of the four layers before writing.
- ENSO/IPO (item 3): one general-audience article on ENSO-neutral conditions already exists and can inform the writing, but it is not a live feed and nothing covers the IPO at all yet. Write new content covering both phenomena and find the correct authoritative external monitoring source to link to.
- None of the three items need a data-sharing agreement to ship as explainer content. A live data connection would need one later, but that is a future, separately funded step, not part of this page's committed scope.

---

##  3.1.2 — Climate variables, projections and the Thailand Climatology Dashboard

**Readiness: 2/5 — Needs new content**

This page holds the site's one committed analytical build alongside two lighter, explainer-only pieces — and one item that is blocked on a separate decision.

### What this page should contain, in order

1. The **Thailand Climatology Dashboard**: climatology and trend statistics for temperature and rainfall, computed from DCCE's own historical grid data and shown at province or region level with uncertainty ranges. This is the same backend that powers the historical extreme-weather statistics shown in section 2.1, built once and shown as an embedded view here and as a full application under the tools section of the site.
2. A small link to the scenario usage guide (see 3.1.3), rather than a full section here — the fuller guide on choosing and interpreting climate scenarios belongs on 3.1.3, and can also surface in the planning section once climate scenarios are introduced there.
3. An explainer on downscaled future climate projections. DCCE's downscaled projection data actually goes down to 5–25km grid resolution, not the coarser national-only resolution the original ask implied — state the real resolution plainly, note where it falls short of the finer sub-national resolution the original ask describes, and link to DCCE's own existing projection platform rather than republishing the datasets on this page.

### What's already there and how to start

- The Climatology Dashboard (item 1) has real underlying data: multi-decade temperature and rainfall grids covering 1981 to 2023. But the grids are restricted access and nothing has been computed from them yet, and it is not currently recorded whether the grid is built from weather stations or from a model reanalysis. Confirm that provenance question before computing and publishing any trend statistics, and resolve the access restriction once, since this same data also feeds the extreme-weather statistics in section 2.1.
- The scenario-guide link (item 2) just points to 3.1.3 — no separate content needs to be written here.
- The projections explainer (item 3) has real data to describe: downscaled projection datasets at 5–25km resolution running out to 2099 and 2100. DCCE already runs a platform for this at clim-webbased.dcce.go.th. Link to that platform rather than rebuilding it here — and note that this platform is not yet formally registered as a DCCE asset, which should be fixed as part of this work.

---

##  3.1.3 — Future climate scenarios

**Readiness: 2/5 — Needs new content**

One piece here is blocked on a decision DCCE has not made. The other two are straightforward content-writing tasks that can proceed on their own.

### What this page should contain, in order

1. An explainer on what a climate scenario is (for example, the SSP/RCP pathways), why projections are presented as a range of scenarios rather than a single forecast, and how to read them. This grounds the reader before the uncertainty and case-study content that follows.
2. If DCCE commits to the uncertainty governance service (see Appendix B of the DRD), a national standard for managing and communicating uncertainty in climate data. This section should be clearly marked as conditional and kept separate from the case studies below, since committing to it is a decision that has not been made.
3. Worked case studies showing climate projection data being used in a real long-term planning or investment decision, covering more than one sector, each one showing the decision made, the data used, how uncertainty was handled, and the outcome. This page is not part of the planning section, so keep the case studies focused on how the projection data itself was used and interpreted, and close with a link out to the planning section's own material rather than duplicating planning content here.

### What's already there and how to start

- The climate-scenario explainer has nothing dedicated to it yet. Write it from the same scenario framing used elsewhere on the site (SSP/RCP), keeping it plain-language and Thailand-specific where possible.
- The uncertainty standard has nothing behind it and should not be started unless DCCE decides to commission the uncertainty governance service.
- The case studies have nothing behind them yet either, but nothing is blocking them. Find at least two real examples, from different sectors, where a Thai planning or investment decision actually used climate projection data, and write them up showing the decision, the data, and how uncertainty in that data was handled. This can proceed independently of the uncertainty-standard section above.

---
# 3.2 การวิเคราะห์ผลกระทบ ความเสี่ยง และความเปราะบาง (Risk Analysis)
##  3.2.1 — Vulnerability and Exposure Analysis

**Readiness: 2/5 — Needs new content**

Real source material exists but only covers part of what the page needs, and one piece of it cannot be built yet at all because it depends on a service DCCE has not agreed to offer.

### What this page should contain, in order

1. Open with the four core concepts the rest of the analytical site depends on: exposure, sensitivity, adaptive capacity, and resilience. Define each one plainly, in Thai and English, following IPCC usage.
2. Show how the four concepts relate to each other and to the risk framework used elsewhere on the site, so a reader coming from any other analytical page recognizes the same vocabulary.
3. Give one Thai example for each concept, grounded in a sector the site already covers.
4. Close this section with a short note that every other analytical page on the site should link back here for these definitions rather than defining them again locally.
5. After the definitions, add a second section introducing the idea of a sector damage function library, the tool that would let agencies estimate what a hazard costs a given sector. State plainly that this does not exist yet and depends on DCCE deciding to build the wider financial and budget evidence service. Do not present this as a working feature.

### What's already there and how to start

- A dataset already defines adaptation and vulnerability concepts in IPCC terms, and a media article explains how vulnerability and adaptive capacity are measured. Start from these two for exposure and adaptive capacity.
- Sensitivity and resilience are not defined anywhere yet, only implied inside the existing material. A content writer needs to draft these two definitions directly, checking them against IPCC's own usage so they stay consistent with the other two.
- Nothing exists for the damage function library. This part of the page should stay a short explanatory note until DCCE decides whether to commission the financial and budget evidence service described in the Loss and Damage briefs. Do not start building this now.

---

##  3.2.2 — Risk Analysis: Methodology and Sector Results

**Readiness: 2/5 — Needs new content**

The page rests on real material, but neither half is ready to publish as is. The methodology needs restructuring into its own explainer, and the sector results need real synthesis work before they can be presented as an answer rather than a rough sketch.

### What this page should contain, in order

1. Open with the national risk assessment methodology. Present it as an explainer, not a formal standard: the broad steps a risk assessment follows, what inputs it needs, and what outputs it produces. State clearly how this relates to DCCE's impact chain manual, and mention CRVA and CRM, the multi-hazard methodologies from GIZ and UNDRR, as existing reference points DCCE could draw on.
2. Add one line stating plainly that an official, binding version of this methodology, with formal compliance rules and a template, is a separate undertaking for later. This page is the plain-language explainer only.
3. Follow with the sector risk results: what the site currently knows about risk to food security, water, health, and business continuity.
4. Be explicit that the underlying picture is a provincial-level risk map only. Present food, water, and settlement results as the strongest, since real spatial data supports them, and state that heat-specific health impact and business disruption are not represented in that data at all.
5. Note that going beyond the provincial risk map picture, toward a genuine sector-level read, needs a literature review rather than a repackaging of the existing dataset.

### What's already there and how to start

- DCCE's impact chain manual is the closest thing to a methodology document today. Use it as the source, but write a new standalone explainer rather than pointing readers at the manual itself.
- The six-sector spatial risk dataset gives real numbers for food, water, and settlement. There is nothing for heat-specific health impact or business disruption in that dataset.
- Before publishing anything framed as a "sector risk result," check it against the boundary-mismatch and product-verification work described in the Appendix B2 investigation and DEL-13 migration, since this page draws on the same underlying data.
- First step for a content writer: draft the methodology explainer from the impact chain manual, then scope a short literature review to fill the food security, water, health, and business disruption gaps rather than presenting the provincial risk map as if it already answers all four.

---

##  3.2.2.1 — Slow-Onset Hazards Profile

**Readiness: 3/5 — Ready to synthesize**

Three of the four hazards on this page have real source material to build from. The fourth, land subsidence and salinity intrusion, has nothing yet and needs a different kind of work entirely.

This page brings together four related slow-moving hazards that were previously written up separately: rising average temperature and shifting rainfall, sea level rise, land subsidence and salinity intrusion, and coastal erosion. They belong on one page because a planner thinking about long-term coastal and inland risk needs to see all four together, not as four disconnected topics.

### What this page should contain, in order

1. Open with a short framing paragraph explaining what a slow-onset hazard is and why these four sit together on one page, distinct from sudden events like floods or storms.
2. Present rising temperature and shifting rainfall first, since this draws on the same data pipeline as the Thailand Climatology Dashboard. Show the rate of change with its uncertainty, and keep observed change visually distinct from projected change.
3. Follow with sea level rise along the Thai coast and the Gulf. In this phase, this is a static explainer: what is observed, why it matters for the Thai coast, and what the observation record shows in general terms. State plainly that a derived rate of rise by coastal segment is not available yet and is a future addition, not something the page currently computes.
4. Next, land subsidence and salinity intrusion. Also a static explainer for now: what these two hazards are, why they matter most for Bangkok and the central region, and how they interact with sea level rise and flooding. State plainly that no data source has been established yet for either hazard.
5. Close with coastal erosion and beach area loss. A static explainer using the existing extent data and the nine coastal adaptation infographics already published. State plainly that a computed erosion index is not available yet and is a future addition.
6. End the page with links to the existing coastal adaptation material rather than repeating it.

### What's already there and how to start

- The temperature and rainfall trend view is not a separate build. It reuses the same underlying climate grid pipeline as the Thailand Climatology Dashboard, so once that pipeline exists, this page's first hazard can reuse it directly.
- Sea level rise has a real annual observation dataset from the marine department hydrology group, running through 2026. Use this to write the static explainer now. Deriving an actual rate of rise by coastal segment is real analytical work and should be scoped separately, only if DCCE can allocate budget for it later.
- Land subsidence and salinity intrusion have nothing behind them at all, not even a document. A content writer can still write the explainer half using general knowledge of why these hazards matter for Bangkok, but establishing real measurement sources needs agreements with other government bodies first. Treat that agreement as a distinct, later task.
- Coastal erosion has real area-based extent data from marine resource bodies and nine existing adaptation infographics. Use both directly for the static explainer. Computing a real erosion index is, like the sea level rate, a later addition contingent on budget.
- First step: write the shared framing paragraph and the temperature and rainfall section together, since both connect back to the Climatology Dashboard. Then move to sea level and erosion, which both have strong existing source material. Subsidence and salinity intrusion should come last, since nothing exists to draft from yet beyond general explanation.

---

##  3.2.3 — The impact chain method, and applying it by sector

**Readiness: 4/5 — Ready to compile**

Half of this page already exists in finished form. The other half follows an established pattern and now has a real event dataset to draw on.

### What this page should contain, in order

1. Open with the multi-hazard impact chain diagram, the visual explanation of how a hazard leads to consequences through a chain of effects. This part is already covered by DCCE's impact chain manual and needs formatting into the page, not new writing.
2. Follow with worked case studies applying the impact chain method to a real sector. Present the existing urban case, the 2025 Hat Yai flood, in full depth.
3. Add a matching agriculture sector case study, built to the same depth and following the same structure as the Hat Yai study, so the two can be read side by side.
4. In both case studies, show the full chain from hazard through to consequence, and be explicit about where the chain was uncertain rather than presenting it as fully known.

### What's already there and how to start

- The impact chain manual itself is finished, real, and ready to use directly for the diagram section.
- The Hat Yai flood case study already exists in depth and can be used as written for the urban half of this page.
- Nothing exists yet for the agriculture sector case study, but a real lead has surfaced: DDPM's ten-year historical disaster occurrence dataset. A content writer should check this dataset first for a real agricultural disaster event to anchor the new case study around, rather than starting from nothing.
- First step: format the diagram and the Hat Yai study for publication, since both are ready now. In parallel, pull a candidate event from the DDPM dataset and begin drafting the agriculture case study against the same structure as Hat Yai.

---

##  3.2.4 — Understanding loss and damage, and the record of past losses

**Readiness: 2/5 — Needs new content, with two items genuinely blocked**

One part of this page can move forward now. Two other parts have real supporting data behind them but cannot be finished as a working product until the loss and damage work package's own methodology is written elsewhere. This is a sequencing block, not a decision DCCE still needs to make about whether to build them.

### What this page should contain, in order

1. Open with the loss and damage concept itself, explained under the UNFCCC framework: the distinction between economic and non-economic loss, how loss and damage relates to adaptation and to mitigation, and Thailand's position and obligations. Keep this independent of the funding page, and link to the funding page only as one application of the framework, not as the framework itself. This part can be written now.
2. Follow with the historical loss dashboard, showing economic and physical losses from past hazard events. This is a mandatory requirement under the sitemap, not optional. State on the page that real DDPM loss records exist and are being prepared, but that the full dashboard depends on the loss and damage work package's methodology, which has not been finished yet.
3. Close with the record of non-economic losses, covering mental health impact, biodiversity loss, and lost cultural heritage. This one is a should-have requirement, not mandatory. State plainly that only biodiversity currently has real supporting material, and that mental health and cultural heritage content has not been started.

### What's already there and how to start

- A publication on the loss and damage response fund already exists and is grounded in the UNFCCC framework, though it was written as a funding page. Use it as a starting reference, but write the framework section as its own independent explainer.
- For the historical loss dashboard, real machine-readable damage records already exist: drought damage values, property damage data, and forest loss rates, all from DDPM and the forest department. These are not dashboard-ready yet. The same underlying DDPM disaster event data that feeds the site's disaster statistics page also connects here, so gathering that data is one shared task rather than two.
- For non-economic losses, one piece of media material on biodiversity impact under rising temperature already exists, along with an environmental education manual. Nothing exists yet for mental health impact or cultural heritage loss.
- First step: write and publish the loss and damage concept section now, since it needs no data. For the dashboard and the non-economic loss record, begin compiling the real DDPM and biodiversity material that already exists, but hold off on presenting either as a finished product until the loss and damage work package's methodology lands.

---

##  3.2.5 — Theoretical Framework and the National Risk, Impact, and Loss Manual

**Readiness: 2/5 — Needs new content, blocked on a dependency**

A proxy document exists, but it was not written for this purpose, and the real manual cannot be finished until the loss and damage work package's methodology is written. This node's "theoretical framework" half is not a separate build — it's satisfied by the concept definitions on 3.2.1 and the risk-assessment methodology on 3.2.2, which this manual should explicitly cite as its grounding rather than re-deriving. A second pass through the full DCCE asset catalog for any other risk-assessment-framework document turned up nothing beyond the impact-chain manual already cited on 3.2.2 — the near-hits (an internal anti-corruption risk assessment, an ecological/pollution-control video) are a different subject entirely, so the proxy framing above still stands.

### What this page should contain, in order

1. Present this page as the standard, government-wide manual for how to calculate risk, impact, and loss and damage, the kind of document another agency would follow to produce results comparable with DCCE's own.
2. Open by citing the theoretical grounding this manual builds on: the exposure/sensitivity/adaptive-capacity/resilience definitions on 3.2.1 and the national risk assessment methodology on 3.2.2. This manual is the calculation procedure built on top of that framework, not a separate theory of its own — say so explicitly rather than repeating the definitions here.
3. State plainly that DCCE's impact chain manual is the closest existing document, but that it was written for a narrower purpose and was not designed as a loss and damage calculation standard.
4. Note that finishing this manual depends on the loss and damage work package's methodology, which has not been written yet. This is a mandatory requirement under the sitemap, so the page should say clearly that the manual is coming, not that it does not matter.

### What's already there and how to start

- The impact chain manual is real and can be used as the starting reference point and structural model for the eventual manual.
- No dedicated loss and damage calculation manual exists anywhere in DCCE's holdings today.
- First step: hold this page as a short placeholder explaining what the manual will cover and why it is not ready yet, rather than attempting a first draft before the loss and damage methodology exists. Revisit once that methodology work package delivers its output.

---
# 3.3 การวางแผนการปรับตัวและการปฏิบัติ (Planning & Implementation)
##  3.3.1 — Planning Guidelines & Participatory Project Design

**Readiness: 2/5 — Needs new content**

Three of the four committed requirements on this page have nothing dedicated behind them today, though A-BTR's legal-framework citations give two of them real grounding to start from. The fourth exists only as a general heat-health article, not the dedicated coverage the page needs. A fifth, conditional piece — cost-benefit and avoided-losses methodology — depends on a decision DCCE has not made yet and is kept structurally separate from the committed content.

### What this page should contain, in order

1. Open with guidance on integrating gender equality, human rights, and social inclusion into adaptation measures, with practical steps at each stage of designing a measure, not principles alone. Include at least one Thai example of a measure that succeeded or failed on inclusion grounds.
2. Follow with protection and assistance measures for each of four named groups, covered separately: children, elderly people, disabled people, and border or coastal communities. For each group, state the specific risks they face and the measures that address them, covering flood, drought, and storm as well as heat. Name the responsible body for each measure.
3. Close with how local wisdom and traditional knowledge apply to community adaptation. Give documented Thai examples naming the community and region, and explain how traditional practice combines with technical measures rather than standing as an alternative to them. Cover cultural heritage both as something at risk and as a resource for adaptation.
4. Link the gender/inclusion guidance and the vulnerable-groups section to each other throughout, since they're meant to work together.
5. If DCCE commits to the financial and budget evidence service (Brief E-1, see Appendix B of the DRD), a cost-benefit and avoided-losses methodology section explaining how a climate-resilient design's cost compares to a historical benchmark. This section should be clearly marked as conditional and kept structurally separate from the committed content above, since committing to it is a decision that has not been made.

### What's already there and how to start

- One article on protecting vulnerable groups during extreme heat exists (`MED-002`, DCCE public relations). It's a useful reference but only covers one hazard and doesn't break out the four named groups.
- A-BTR's institutional and legal baseline (Section A) names the Gender Equality Act, the Child Protection Act, the Older Persons Act, and the Persons with Disabilities Empowerment Act as the legal grounding for gender-responsive adaptation and protecting the four named groups. This is legal/rights framing, not practical measures — pair it with the welfare registry below and the heat-health article for the operational detail.
- Nothing exists yet for local wisdom and traditional knowledge — that still needs to be written from scratch. Gender/inclusion guidance has real legal grounding to build on now; the practical, stage-by-stage steps still need writing.
- Before writing the vulnerable-groups section, check the Ministry of Social Development and Human Security's welfare registry (`MSDHS_1_1`) — it's the closest thing to real data on the four named groups and is worth requesting access to early, since it can ground the content in real numbers rather than description alone.
- Population data for children and elderly people (from NESDC sources) can support the exposure framing for those two groups, though it's demographic background, not a protection-measures inventory on its own.
- Local wisdom content will need outreach to community organizations or provincial offices to gather documented examples — this isn't sitting in any DCCE catalog waiting to be compiled.
- The cost-benefit and avoided-losses methodology has nothing behind it and should not be started unless DCCE decides to commission the financial and budget evidence service.

---

##  3.3.2 — National adaptation roadmap, barriers, and support needs

**Readiness: 2/5 — Needs new content**

The roadmap diagram itself is solid and ready to use. The systemic barriers report has real source material to start from in A-BTR; the support-needs piece still depends on a decision DCCE hasn't made yet.

### What this page should contain, in order

1. Open with the national adaptation strategy roadmap and execution staging diagram. This is already well supported by the National Adaptation Plan and its dataset entry, so it can be published close to as-is.
2. Follow with a report on systemic barriers by sector, covering at minimum data limitations, institutional coordination problems, and financial constraints. Distinguish barriers DCCE can address from those needing action elsewhere, and name the source behind each barrier rather than asserting it. Link each barrier to the part of the site that already addresses it, where one exists.
3. If DCCE commits to the financial and budget evidence service (Brief E-1), a separate section would cover the list of financial, technology, and capacity support needed, and personnel development needs for climate fund proposals. Keep this visually and structurally separate from the committed content above, since it isn't decided yet.

### What's already there and how to start

- The roadmap diagram can be pulled directly from the National Adaptation Plan (`PUB-009`, `DAT-021`) with light formatting work.
- A-BTR's Section C (priorities, barriers and strategy) already frames systemic barriers across the full planning-to-reporting cycle — data limitations, institutional coordination gaps, and financial constraints among them. Use it as the starting inventory and named-source base, then confirm and expand sector by sector, keeping a running log of the source for each one, since the requirement is explicit that assertions without a named source don't count.
- The support-needs and personnel-development content should not be started until DCCE decides whether to build the financial evidence service. If that decision comes through, the existing funding-source material (DCCE's funding guide, and the AF/GCF/GEF publications) covers money only, not technology transfer or capacity building, so that gap would still need filling separately.

---

##  3.3.3 — Adaptation measures library

**Readiness: 3/5 — Real sector material exists, needs compiling and building**

Nature-based solutions content is genuinely strong, and six sector-specific good-practice case studies — already compiled for the case-study library on 3.4.3 — give the searchable database real material to mine across every priority sector, not just nature-based. The searchable database itself and the grey infrastructure half of the comparison still need to be built. Note: this feature's build is owned by DCCE's adaptation measure development division, not the content/communications team — flag ownership before build starts, not after.

### What this page should contain, in order

1. Open with a searchable and filterable collection of adaptation measures, letting a user filter by hazard, sector, and budget together. Record for each measure what it does, where it's been used, and what it costs. Where cost isn't known, show the measure anyway with cost marked unknown, rather than hiding it from budget-filtered results.
2. Present grey and structural infrastructure measures alongside nature-based ones, at comparable depth, so a reader can compare both approaches for the same hazard and setting. State the conditions favoring each type, and cover combined approaches, since these are often the practical answer.

### What's already there and how to start

- Nature-based solutions content is ready to compile: a guidance dataset (`DAT-022`), an explainer (`MED-042`), and a video (`VID-036`) all exist and cover this material in depth.
- Six sector-specific good-practice assets (`MED-009` through `MED-014`, one each for human settlements & security, natural resources, public health, tourism, agriculture & food security, and water resources management) already cover concrete measures by sector — the same set used for the case-study library on 3.4.3. Mine these into structured, measure-level entries (what it does, where it's been used, what it costs) rather than treating them as case-study-only material.
- Grey and structural infrastructure measures have nothing behind them in DCCE's holdings. This will likely need to be sourced from outside DCCE, for example from the Department of Public Works and Town & Country Planning or the Royal Irrigation Department's own infrastructure planning material.
- The searchable database itself (filtering by hazard, sector, budget, with a "cost unknown" state) is a structured content-entry task once the measure descriptions exist across categories. Start entering nature-based and sector good-practice measures now, since that content is ready, while grey infrastructure content is being sourced.

---

##  3.3.4 — Repository of local and private sector risk management plans

**Readiness: 2/5 — Narrative case material exists, structured repository still blocked**

The structured, searchable repository depends on DCCE deciding to build the institutional and project tracking service. But real local and private-sector adaptation cases already exist in narrative form and can open the page today, even while that decision is pending.

### What this page should contain, in order

If DCCE selects this service (Brief E-3, Appendix B), the page would grow into a searchable repository of local and private sector climate risk management plans. That structured repository has nothing to build from today, and the underlying plan documents sit with DCCE programme staff and external organizations rather than in any searchable inventory. In the meantime, the page can open with illustrative local and private-sector cases DCCE has already published, rather than sitting empty until the decision lands.

### What's already there and how to start

- Real narrative case material exists: `MED-043` covers lessons from the Mae Sai flood toward recovery and adaptation guidelines, `MED-028` covers small-scale pig farm operators adapting to extreme heat, and `MED-006` covers model-area lessons feeding national-level rollout. None of these are formal risk management plan documents, but they're genuine local and private-sector adaptation cases DCCE already holds — compile them as the page's opening content now.
- The structured, searchable repository of actual plan documents is a separate matter and should not be drafted until DCCE makes the Brief E-3 decision.
- If that decision comes through, the first real task is establishing internal reporting routines to actually collect the plans themselves, since they aren't findable through any current inventory search. That's the genuine starting point for the structured repository, not content writing.

---

##  3.3.5 — Project Tracking Status

**Readiness: 1/5 — Blocked**

Both requirements on this page wait on separate DCCE decisions. Neither has anything to build from yet. The institutional tracking piece also carries a second, independent blocker: it depends on the current status and maturity of DCCE's own M&E platform, not just on DCCE choosing to build Brief E-3.

### What this page should contain, in order

If DCCE selects the institutional tracking service (Brief E-3), this page would show the status of national adaptation projects and their progress — the kind of projects the sitemap names as examples: crop insurance schemes, use of the Agri-Map database, and water-control infrastructure improvement. These are illustrative of the page's scope, not a commitment to track these specific projects. If DCCE separately selects the financial evidence service (Brief E-1), it would also carry budget readiness indicators for adaptation projects. These are two different decisions and could land on different timelines, so plan for the page to potentially grow in two separate steps rather than all at once.

### What's already there and how to start

- Nothing exists for either piece. Do not start drafting until the relevant decision is made.
- Even once DCCE decides on Brief E-3, this page can't move until the M&E platform itself is mature enough to support it — that's a separate gating condition, not just a sequencing note. Check the M&E platform's current status before assuming a green light on E-3 is enough to start building.
- Project tracking depends on the same internal reporting routines needed for  3.3.4's plans repository — worth scoping both together if DCCE commits to Brief E-3, since they share the same underlying blocker.

---

##  3.4.1 — Technology readiness and the Global Goal on Adaptation

**Readiness: 4/5 — Ready to compile**

Both pieces of this page have real material behind them. One needs a quick verification step before publishing.

### What this page should contain, in order

1. Open with the technology readiness framework, showing how ready an adaptation technology or innovation is for use.
2. Follow with how Thailand's indicators connect to the Global Goal on Adaptation (GGA), including the 59 Belém Indicators framework.

### What's already there and how to start

- The technology readiness framework is recorded as covered because it sits inside DCCE's active adaptation monitoring platform, not because a specific standalone document was matched to it. Confirm this content actually exists and is current before publishing it as done.
- The Global Goal on Adaptation material is a verified match: two media pieces (`MED-024`, `MED-049`) cover Thailand's alignment with the GGA indicators and the Belém Indicators specifically. This part can be compiled and published with light editing.

---

##  3.4.2 — National monitoring and evaluation tracker

**Readiness: 5/5 — Ready to format**

This is a live, maintained DCCE system. The content exists and just needs to be surfaced on the page.

### What this page should contain, in order

1. Present the national tracker for adaptation progress by sector and province, drawn from DCCE's live monitoring and evaluation data.

### What's already there and how to start

- `DAT-014` is a real, current dataset maintained by DCCE's dedicated Adaptation M&E Evaluation Group, tied to Thailand's official Biennial Transparency Report submitted under the UNFCCC. It was verified directly against DCCE's live catalog, not just matched from an extract.
- This is a linking and formatting task, not a content-writing one. Confirm the live data feed is accessible to the new platform and build the page around it.

---

##  3.4.3 — Successful adaptation project case studies

**Readiness: 5/5 — Ready to format**

This is the best-supported page in this whole document. Real material already exists across multiple sectors.

### What this page should contain, in order

1. Present a library of case studies distilling lessons learned from successful adaptation projects, covering not just what worked but the obstacles encountered along the way and the best-practice takeaways from both, drawn from DCCE's monitoring and evaluation lesson-extraction work.

### What's already there and how to start

- Eight separate assets already cover this, spanning cross-sector success factors, sector-specific good-practice case studies (human settlements, natural resources, and others), and a wrap-up media piece summarizing the M&E lesson-extraction project.
- This page can be built by compiling and formatting existing material. No new content development is needed to launch it.

---

# 4. เครื่องมือและบริการสารสนเทศด้านภูมิอากาศ — Tools and services

##  4.1 — Data catalog

**Readiness: 4/5 — Ready to compile**

The catalog system itself already works. What's missing is a decision on final scope, not new technology or new writing.

### What this page should contain, in order

1. A short introduction explaining what the data catalog is and who it serves — researchers, agencies, and the public looking for climate and adaptation data.
2. Search and browse access to the catalog itself, covering three distinct content types: raw datasets, analytical data products, and the metadata directory describing them — embedded or linked from DCCE's existing system.
3. A brief note on the security and governance standards the catalog follows, so users understand how access levels work.
4. A pointer to how users can request a dataset that isn't yet listed, or report an issue with an entry.

### What's already there and how to start

DCCE already runs a working data catalog system, has a publication describing it, and has a governance manual covering metadata and security standards. CRDB has also produced an initial data inventory as a starting seed.

What's not yet settled is the catalog's final content. CRDB's inventory is a seed, not the finished scope. Before this page is built out, DCCE needs to decide what datasets and products belong in the catalog for the new platform, since the existing system holds more than what this project can vouch for.

First step: get formal sign-off on catalog scope in the next project, using CRDB's initial inventory as the starting point. Once scope is settled, this page is mostly a linking and embedding task.

---

##  4.2 — Visualisation and analytics application

**Readiness: 4/5 — Ready to host once migration lands; one component is real work but deferred to a future project**

This page ships two things on different timelines. The hazard map and risk analysis tool is DCCE's existing, working application (`SYS-003`) — it hosts here once migrated. The rainfall/temperature design values engineers actually want (IDF curves) are real, needed work, but confirmed out of scope for this platform's launch — a future-project workstream, not something this build produces.

### What this page should contain, in order

1. An introduction explaining what the page offers: hazard maps and risk analysis for general planning.
2. The embedded hazard map and risk analysis tool (`SYS-003`), migrated per the platform's hosting decision, alongside the new disaster-statistics, Loss and Damage, and Thailand Climatology products built in the next project. Anything not owned by DCCE is linked out rather than rebuilt here.
3. A short, clearly separated note that engineering design values (rainfall intensity-duration-frequency curves) are planned as a future workstream, not part of this launch — say so plainly rather than building out a section that isn't coming yet.

### What's already there and how to start

DCCE's existing risk map application (`SYS-003`) is real and working, and can be migrated onto the new platform once the underlying data investigation (Appendix B2 in the DRD) is complete. That's this page's actual launch scope, and it's close to ready.

The design-value curves are separate, deferred work, not part of this build. A full search of DCCE's document and dataset holdings turned up nothing on intensity-duration-frequency curves, at any resolution, and this will not be built from `SYS-003`'s composite risk index — that data serves the general hazard map, not plot-level engineering statistics, and the two should not be conflated. It needs new statistical work using rainfall data DCCE does not currently have in a usable form, plus validation from engineering standards bodies. Scope and resource it as its own future project (Brief E-4), not as a page-content task for this build.

---

##  4.3 — External tools and data hub

**Readiness: 4/5 — Ready to compile as a curated links page**

This page hosts links to external sources — a curated reference list DCCE can compile from public information, not a live-integration build. No agency agreements or API access are required to launch it.

### What this page should contain, in order

1. A short explanation of what this page offers: curated links to major external data sources relevant to climate work in Thailand.
2. An entry for each named external source (the meteorological department's weather service, the space agency's geo-informatics portal, and the Copernicus climate data store), each stating what data it holds, what access conditions apply, and how it relates to data already on this site.
3. The agreement or licence each connection operates under, where publicly known.

### What's already there and how to start

No DCCE asset covers this today, but none is needed — this is a curated links page, compiled from public information about each external source, not a data-matching task.

First step: write the three entries directly, using each agency's own public documentation for the "what it holds" and "access conditions" fields. No outreach, agreement, or live-connection work is required to launch this page.

---

# 5. ข่าว ประกาศ และช่องทางการติดต่อ — News and contact

##  5.1 — Announcements and engagement activities

**Readiness: 5/5 — Ready to format**

Everything this page needs already exists and works. This is a linking task, not a build.

### What this page should contain, in order

1. A feed or listing of recent data updates and announcements.
2. A calendar or listing of training activities and workshops on interpreting and using climate data for planning.
3. Links into DCCE's existing seminar and training system and its public relations channel, so visitors can register or read further.

### What's already there and how to start

DCCE already runs a seminar and training system and a public relations news channel that cover this content directly. Nothing needs to be written or compiled from scratch.

First step: connect this page to the existing systems' feeds so updates appear automatically, rather than maintaining a separate, manually updated list. Confirm with the teams running those systems how their content can be pulled into the new platform.

---

##  5.2 — Feedback channels and user services

**Readiness: 2/5 — Needs new content**

Nothing exists today, in any form. This is a genuinely new capability for DCCE, but it does not depend on any outside agency, so it can be designed and built without waiting on anyone else.

### What this page should contain, in order

1. A short introduction explaining what the feedback platform is for: reporting data quality issues, requesting the scope of a dataset be extended, or confirming whether a need is being met.
2. A structured form for submitting feedback, tied to a specific dataset or page.
3. A way for a submitter to track the status of their own submission through to its outcome.
4. An aggregate view (likely for DCCE staff rather than the public) showing recurring issues across all submissions, so patterns are visible rather than buried in individual tickets.

### What's already there and how to start

No structured feedback or service-quality mechanism exists at DCCE today. This needs to be designed and built as new operational capability, alongside the external portal connections described on the previous page. Both are new systems work, not content synthesis, and both sit outside the pattern of "find existing material and adapt it" that covers most of this project.

First step: decide who at DCCE owns feedback triage and routing before building the submission form, since the form's fields and routing logic depend on that answer. Building the form itself without that decision risks a system nobody is set up to act on.

---

# Readiness summary

| Section | Page | Readiness |
|---|---|---|
| 1.1 | Overview of Thailand's climate risk | 2/5 |
| 1.1 | Key risks and adaptation priorities | 3/5 |
| 1.2 | Area-based data search | 2/5 |
| 2.1 | National climate change situation | 2/5 |
| 2.2 | Area and sector risk profiles | 2/5 |
| 2.3 | Climate Change Act and supporting laws | 2/5 |
| 2.3 | Funding, budget evidence, finance tracking | 1/5 |
| 2.3 | Institutional governance and coordination | 4/5 |
| 2.4 | Planning data services | 2/5 |
| 3.1 | Weather stations, satellite, global monitoring | 2/5 |
| 3.1 | Climate variables and projections | 2/5 |
| 3.1 | Future climate scenarios | 2/5 |
| 3.2 | Vulnerability and exposure analysis | 2/5 |
| 3.2 | Risk analysis: methodology and sector results | 2/5 |
| 3.2 | Slow-Onset Hazards Profile | 3/5 |
| 3.2 | Impact chain method and sector case studies | 4/5 |
| 3.2 | Loss and damage, historical losses | 2/5 |
| 3.2 | Theoretical framework and national risk/loss manual | 2/5 |
| 3.3 | Planning guidelines and inclusive adaptation | 2/5 |
| 3.3 | Adaptation roadmap, barriers, support needs | 2/5 |
| 3.3 | Adaptation measures library | 2/5 |
| 3.3 | Local/private sector plans repository | 1/5 |
| 3.3 | Project tracking status | 1/5 |
| 3.4 | Technology readiness and GGA indicators | 4/5 |
| 3.4 | National M&E tracker | 5/5 |
| 3.4 | Successful project case studies | 5/5 |
| 4.1 | Data catalog | 4/5 |
| 4.2 | Visualisation and analytics application | 2/5 |
| 4.3 | External tools and data hub | 2/5 |
| 5.1 | Announcements and engagement activities | 5/5 |
| 5.2 | Feedback channels and user services | 2/5 |

Six pages are ready to format or compile with light effort (3.4.2, 3.4.3, 5.1, 2.3.2, 3.4.1, 4.1). Three pages are fully blocked on a DCCE decision (2.3.1, 3.3.4, 3.3.5). The rest need real content work, some of it gated on data-lineage investigations or sequencing dependencies described in the DRD, but none of it blocked on a decision DCCE still needs to make.
