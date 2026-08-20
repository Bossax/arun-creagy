# WP4 Content-Source Gap Analysis — Node-Level Deep Dives v2

**Date:** 20 August 2026
**Supersedes:** `2026-08-11-WP4-Node-Level-Deep-Dives.md` (D-062)
**Companion to:** `2026-08-20-WP4-Content-Source-Gap-Analysis-v2.md`, `NCAIF_Detailed_Sitemap_v9.md` (D-075)

## What this document is

The main report makes its case with three worked examples, picked to illustrate the method. This document extends that same page-by-page treatment to every **second-level sitemap node** (the `X.X` grain — e.g. `2.3`, `3.2`, `4.2`) rather than stopping at three. Third-level and fourth-level sub-items (`X.X.X`, `X.X.X.X`) are not broken out as their own sections here — where a second-level node has sub-nodes under it, this document rolls all of that node's requirements up into one write-up, so the grain matches how the sitemap is actually organized into topical sections, not every individual bullet point.

**This is a delta pass against v9 (Boss's decision this session, same delta-only approach as the companion CSGA and DRD v2), not a full re-derivation.** Node write-ups v9 left factually unchanged are carried forward verbatim. Six nodes changed:

- **2.3** gains one restored-from-v6 item (NAP Implementation Status, PARTIAL) — tally updated, prose extended.
- **2.4 retired** — collapsed to a pure router link in v9, no distinct content requirements remain. Section removed; its former 3 items (2 full, 1 partial) drop out of the totals.
- **3.1** gains one restored-from-v6 item (climate-scenario data source, PARTIAL) — tally updated, prose extended.
- **3.2** gains one restored-from-v6 item (other risk-assessment sources, GAP) — tally updated, prose extended.
- **3.3** loses two items (ongoing-project tracking, budget-readiness indicators) — merged into 3.4 per Boss's decision this session, since 3.3.5 (Project Tracking Status) now points to 3.4.2 (Adaptation M&E Platform) instead of describing its own content. Tally and prose updated.
- **3.4** gains those same two items (both GAP — nothing existed for either before, and that hasn't changed) — tally updated, prose extended.
- **4.1/4.2/4.3 merged into one Node 4** — v9 flattens Section 4 to a single tag-filterable tool grid, no sub-node split. The three write-ups below are combined into one, plus two new mockup-sourced, unvalidated items (Climate Impact Explorer, Adaptation Options Explorer — both GAP).

Fourteen second-level nodes are covered below (down from v1's 15 — 2.4 retired, 4.1/4.2/4.3 merged to one Node 4, net −1). Per the same convention as the main report: no internal asset codes or reference IDs in the body — real names and plain descriptions throughout. Full traceability (asset IDs, exact match rationale) lives in the working CSV.

The per-node tallies below sum to the v2 CSGA's totals: **16 full, 26 partial, 33 gap, 75 requirements** (up from v1's 18/25/30/73 — see the per-node deltas above and the Summary Table's own note for the full reconciliation).

---

## Node 1.1 — Overview of Thailand's Climate Risk (Country Overview)

**Structure note (19 August 2026):** Per the Homepage Concept draft, this node no longer sits under Home — it's its own Country Overview section, a sibling of Home. Home becomes a router (search + task-based service cards).

*Rolls up: Overview of Climate Change Risk in Thailand (1.1.1), Key Risks and National Adaptation Priorities (1.1.2) — 7 requirements.*

### What this node needs, in full

Historical natural-disaster trends and history for the country; the IPCC-standard hazard/exposure/vulnerability concept framework; an understanding of physical risk versus transition risk; national risk-profile summary cards; sector- and region-level adaptation hotspots; a National Adaptation Plan (NAP) summary; and examples of high-value, proactive adaptation measures.

### What actually exists

The IPCC framework definitions are well covered — the impact-chain manual embeds the methodology, and a dataset is explicitly tagged with IPCC, vulnerability, and adaptation terms (these are correctly assigned to their corresponding data domains). Sector and regional hotspots have a real, purpose-built source in the six-sector spatial risk dataset. The NAP summary is one of the strongest matches anywhere in the sitemap — the official document itself, a dataset entry, and multiple English- and Thai-language media explainers all exist. High-value adaptation measure examples are backed by a cross-sector success-factors media piece and a nature-based-solutions dataset with concrete content.

What's missing or partial: historical disaster trend history has nothing behind it at all — no dataset or publication tracks Thailand's natural-disaster history as a narrative or time series. Physical-risk-versus-transition-risk framing, a conceptual pairing common in climate-finance literature, is also a total gap. And the risk-profile summary cards, after the dataset-catalog cross-check, moved from gap to partial: DCCE's seven-sector composite risk index supplies real numbers, but it's flagged draft/unverified and isn't rendered into anything resembling a summary card yet. 

### Coverage tally

4 full · 1 partial · 2 gap (out of 7 requirements)

### Assessment

This node is the Country Overview a user reaches from Home's router, and it's in genuinely good shape for the "here's what the country's adaptation priorities are" half — NAP summary and hotspot data are strong, reusable assets. But the "why this matters" framing half is thinner than it looks: historical disaster trends and transition-risk framing are both completely unaddressed, and they're exactly the kind of scene-setting content this page needs before it gets into NAP details. Both gaps are also unusually cheap relative to most gaps in this sitemap — historical disaster trends, in particular, is closer to a compilation task from existing (if scattered) government records than new data collection.

---

## Node 1.2 — Area-Based Data Search

*Direct node, 3 requirements.*

### What this node needs, in full

A search hierarchy supporting province → district → subdistrict administrative levels; map integration overlaying administrative boundaries on the spatial risk map; and a quick-view dashboard showing point-level vulnerability, key threats, and initial recommended measures.

### What actually exists

This node has evolved in v6 to be an "Interactive Search" UI rather than a distinct repository of new content. It serves as a navigational gateway to the data mart that powers Node 2.2 and the spatial risk database. 

The spatial risk map overlay is a gap — while raw spatial dataset exists, there is no actual built map-overlay UI or design currently available from DCCE. The quick-view dashboard is partial: the data could plausibly be extended into a point-level summary UI (pointing to the spatial risk database), and real vulnerability/threat data exists to populate half of it, but the "recommended measures" half has zero data support anywhere, and no purpose-built dashboard product exists yet.

The administrative search hierarchy itself (province → district → subdistrict drill-down) presents a hard data gap: the DCCE spatial climate risk map only provides composite risk indices at the province level. District and subdistrict granularities do not exist in the current spatial risk map and require more granular data from other line agencies. However, scattered provincial climate change plans do exist and can serve as sources of sectoral and location risk hotspots to help flesh out the lower-level details.

### Coverage tally

0 full · 1 partial · 2 gap (out of 3 requirements)

### Assessment

This node is a UI/UX navigational gateway rather than a pure content node. The map-overlay piece is a gap since no design or interface has been built yet. The search hierarchy reveals a severe data limitation: drilling down past the province level is not currently supported by DCCE's own spatial risk database. Planners should note that populating this interactive search below the province level will require aggregating scattered provincial climate change plans or securing data from other line agencies. The quick-view dashboard's "recommended measures" gap connects to a recurring pattern: DCCE's inventory is much better at describing risk than prescribing what to do about it.

---

## Node 2.1 — National Climate Change Situation

*Direct node, 3 requirements.*

### What this node needs, in full

Historical extreme-weather-event statistics (temperature max/min, cumulative rainfall); a macroeconomic loss-and-damage statistics database; and a summary of national exposure trends.

### What actually exists

Exposure trends are a total gap. While the six-sector spatial dataset provides a static snapshot of exposure, it does not inherently provide a time-series trend of how exposure is changing. The other two items are partial: historical extreme-weather statistics have real underlying data (1981–2023 daily/monthly temperature and rainfall grids), though it's Restricted-access raw grid data, not pre-computed event statistics. 

Crucially, the macroeconomic loss-and-damage database is heavily restricted/partial. We do not have true macroeconomic economic loss records. What exists in the dataset catalog are records of reported damaged assets, human impacts, and government advance payments (เงินทดรองราชการ). These fiscal payout caps and damage tallies do not reflect the true reality of economic damage, they are not aggregated into a macroeconomic database, and they are self-flagged as needing data-quality cleanup.

### Coverage tally

0 full · 2 partial · 1 gap (out of 3 requirements)

### Assessment

No total gaps here, which sounds like good news, but both partial items need real technical work rather than simple content sourcing — turning raw climate grids into usable statistics, and consolidating fragmented per-hazard loss records into a coherent macroeconomic database, are data-engineering tasks, not writing tasks. A good example of why "nothing is a flat gap" doesn't mean "this page is nearly done."

---

## Node 2.2 — Area and Sector Risk Profile Summary

*Direct node, 2 requirements.*

### What this node needs, in full

Risk and vulnerability profile summaries at both the sub-national level (all 77 provinces plus local government) and by the six priority sectors.

### What actually exists

Note that this node fundamentally relies on the same underlying data mart as the Interactive Search (Node 1.2), just presented through a different interface (a summary profile rather than an interactive query).

The sector-specific version is partially covered. The six-sector spatial risk dataset provides the spatial baseline, but there is no summarized, ready-to-use profile document. However, scattered sectoral studies and plans (like the Health National Adaptation Plan - HNAP) do exist and can be leveraged to build these profiles. The province/local-government version has nothing behind it at all: no dataset or publication currently disaggregates risk profiles down to all 77 provinces and local administrative units in a summarized, ready-to-use form.

### Coverage tally

0 full · 1 partial · 1 gap (out of 2 requirements)

### Assessment

A clean, sharply-defined node — half genuinely done, half a genuine gap. The gap is notable because the underlying province-level risk data does exist elsewhere in DCCE's holdings (the composite risk index found during the dataset-catalog cross-check is province-level), so this may be less a "no data" problem and more a "no summarized, localized presentation layer built on top of existing data" problem — worth a build-team conversation about whether this is really a content gap or a product-design gap.


%%this is the same thing as "Area-Based Data Search" just different interfaces (should rely on the same data mart%%

	%%also there are scattering sectoral studies or sectoral plan like HNAP%%

---

## Node 2.3 — Policy, Legal & Financial Tools

*Rolls up: direct node-level requirements, plus Funding Sources & Budget Tracking (2.3.1) and Institutional Mechanisms & Coordination (2.3.2) — 12 requirements total (v1: 11; +1, NAP Implementation Status, restored from v6 this session).*

### What this node needs, in full

At the node's own level: the implementation status of Thailand's draft Climate Change Act; **the implementation status of the NAP itself, distinct from the Act's legal status (restored from v6 this session)**; a summary of supporting legal/policy instruments (disaster-prevention law, town-planning regulations); and a certification system for an "avoided losses" analysis tool. Under Funding Sources & Budget Tracking: a directory of public/private/international funding sources with a cost-benefit methodology guide for budget justification; statistics on national budget allocation and climate budget tagging; tracking of financial aid, technology transfer, and technical assistance received from major climate funds; and engagement/mobilization of private-sector finance. Under Institutional Mechanisms & Coordination: DCCE's role as national focal point; the structure of the national climate policy committee and sub-committees; coordination mechanisms between national and local government; and civil-society/private-sector/academic participation channels and statistics.

### What actually exists

The Climate Change Act's status is well covered — an official summary, the full draft text, and two media explainers all exist. DCCE's role as national focal point, the policy committee's structure, and public-participation statistics are all backed by real, purpose-built documents or datasets (committee appointment orders, multi-year public disclosure publications, an active participation-tracking system). The funding-sources directory is genuinely solid: DCCE's own funding guide plus dedicated publications for each of the three major international climate funds, and DCCE's own internal process for endorsing fund project proposals is real, operational documentation, not just a description.

Beyond straightforward financial tracking, coverage drops sharply. No cost-benefit/budget-justification methodology guide exists — only fund directories, which are a different thing. No budget-allocation statistics or climate budget tagging exist at all. And — repeating a pattern that shows up elsewhere in the sitemap — technology transfer and technical assistance tracking are consistently absent; every matched asset for the "financial aid, technology, and technical assistance" requirement turns out to track money only. The avoided-losses certification system, national-to-local coordination mechanisms, and private-sector finance mobilization are all total gaps as well.

**New this session:** NAP Implementation Status matches to the same live Adaptation M&E dataset used elsewhere on the site (nodes 3.4's tracker), but that dataset is the general M&E platform, not a tracker dedicated to "is the NAP plan itself on schedule" specifically — PARTIAL, same honest-hedge pattern as several other items in this node.

### Coverage tally

4 full · 3 partial · 5 gap (out of 12 requirements)

### Assessment

This node's headline number is more mixed than it first looks: just under a third of its requirements are fully covered, concentrated almost entirely in "what money exists, who's in charge, and how is participation tracked." Everywhere the requirement asks for something adjacent to that — cost-benefit justification, budget tagging, technology transfer, technical assistance, cross-level coordination, an avoided-losses certification model — coverage is thin or absent. That's a specific, nameable content-production program (methodology guides, a technology/capacity-building tracking mechanism, an intergovernmental coordination write-up), not a scattering of unrelated small gaps, and it's a larger lift than the full-coverage count alone would suggest.

---

## Node 2.4 — Planning Data Services (retired, 2026-08-20)

**v9 status: collapsed to a pure router link — no distinct content requirements remain.** Per Boss's decision this session, this node no longer carries the local vulnerability index, integrated spatial risk map, or data-security guidance content v1 described here — the map/profile content is already reachable via 1.2, 2.2, and Section 4, and a dedicated hub page would duplicate an entry point rather than add one. Its 3 requirements (2 full, 1 partial) were removed from the CSGA v2 and DRD v2 accordingly and no longer count toward this document's totals.

---

## Node 3.1 — Climate Drivers: Observation, Drivers & Future Scenarios

*Rolls up: Observational Data (3.1.1), Climate Drivers (3.1.2), Future Climate Scenarios (3.1.3) — 9 requirements (v1: 8; +1, climate-scenario data source, restored from v6 this session).*

### What this node needs, in full

Short/medium-term weather-station data (in cooperation with the Meteorological Department); satellite observation data covering forest cover, land cover, water bodies, and coral bleaching; monitoring data for internationally significant climate phenomena (ENSO, AMOC); climatology and key climate-variable data (temperature and rainfall trends); a usage guide for climate scenarios; **a data-source pointer for climate scenarios, distinct from the usage guide — "where do I get this data," not "how do I read it" (restored from v6 this session)**; a library of high-resolution downscaled national future-climate projections; a national standard for managing forecast uncertainty and choosing between projection datasets; and case studies applying climate-projection models to long-term strategic planning.

### What actually exists

This is the weakest node in the entire sitemap on a raw-document basis, and the dataset-catalog cross-check only partially rescues it. Three items move to genuine partial coverage: climatology variables and downscaled climate projections both turn out to have real, multi-decade national grid datasets behind them (1981–2023 historical records; downscaled projections running through 2099 using both dynamical and statistical methods) — though both are Restricted-access, raw-grid, and national- rather than sub-national-resolution. ENSO/AMOC monitoring is also partial, but weakly so: a single general-audience media piece exists for ENSO, and AMOC has nothing at all.

**New this session:** the climate-scenario data-source pointer matches the same downscaled-projection datasets already backing this node's projections item — it's a pointer to that same data, not a separate dataset, so it inherits the same PARTIAL rating and Restricted-access, national-resolution caveats.

Five of the eight original requirements remain confirmed, total gaps even after the deeper check: station-level weather data, satellite observation data, a climate-scenario usage guide, a national uncertainty-governance standard, and climate-projection case studies for strategic planning. None of these turned up anywhere in either DCCE inventory.

### Coverage tally

0 full · 4 partial · 5 gap (out of 9 requirements)

### Assessment

This is the only node in the entire sitemap with zero full-coverage items, and even its partial items are raw, access-restricted, unprocessed data rather than anything close to publishable. This is the single clearest data-partnership priority in the whole exercise: real value would come from formal access arrangements with the Meteorological Department, the Marine Department, and whoever holds the underlying downscaled-projection modeling runs, rather than from DCCE content production. Framing this node as a "content gap" for a writer to fill would badly misdescribe the actual work required.

---

## Node 3.2 — Risk, Vulnerability, Impact-Chain & Loss-and-Damage Analysis

*Rolls up: Vulnerability & Exposure Analysis (3.2.1), Risk Analysis (3.2.2), Slow-Onset Hazard Tracking (3.2.2.1), Impact-Chain Analysis (3.2.3), Loss & Damage (3.2.4), Theoretical Framework & Manuals (3.2.5) — 15 requirements total (v1: 14; +1, other risk-assessment sources pointer, restored from v6 this session).*

### What this node needs, in full

This is the analytical core of the whole platform — the place where raw hazard/exposure data is meant to turn into actual risk findings. Across its six sub-sections it needs: definitions of vulnerability/exposure/sensitivity/adaptive-capacity/resilience concepts; a library of sector-specific damage functions for hazard modeling; a single national risk-assessment methodology; sector-by-sector risk results (food security, water security, heat-health impact, SME business disruption); statistics and tracking for slow-onset hazards (rising average temperature and shifting rainfall patterns, sea-level rise, land subsidence, salinity intrusion, coastal erosion); a multi-hazard impact-chain diagram plus sector case studies (agriculture, urban); a Loss & Damage theoretical framework tied to the UNFCCC; a dashboard summarizing historical economic and physical losses; a record of non-economic losses (mental health, biodiversity, cultural heritage); and a standardized national manual for risk/impact/L&D calculation methodology.

### What actually exists

One real strength anchors this whole cluster: DCCE's impact-chain methodology manual. It's a genuine, purpose-built document, and it gets reused — appropriately — as the closest available source for four separate requirements: the general risk-assessment standard, the multi-hazard impact-chain diagram, the vulnerability/exposure concept definitions (partially — sensitivity and resilience are only implicit in it, not explicit), and the national L&D calculation manual. That reuse is legitimate, but it also means the same single document is being asked to stand in for several distinct things DCCE doesn't actually have purpose-built versions of yet.

Beyond that: DCCE's six-sector spatial risk dataset supplies real sector-level risk results for food, water, and settlement-related risks (though heat-specific health impact and SME business disruption are not represented). A 2025 flood case study gives a strong urban impact-chain example but nothing for agriculture. The Loss & Damage fund page and DCCE's commissioned assessment report are the closest things to a framework explainer and a loss dashboard, respectively — both are real and relevant, but one is a financing page (not a framework document) and the other is a static report (not dashboard-ready data). Non-economic loss material exists only for biodiversity; mental health and cultural heritage have nothing.

The follow-up cross-check against DCCE's separate dataset catalog changed the picture for the slow-onset hazard sub-section specifically: real annual sea-level observation data exists (previously recorded as a total gap), and the coastal erosion sub-requirement turned out to have genuine area-based erosion-extent data behind it, not just the narrative infographics originally credited. It also strengthened the Loss & Damage dashboard's evidence — real, machine-readable annual damage and property-loss records exist for several hazards, not just the one static report. Both upgrades come with the same caveat as elsewhere in this cross-check: the data is Restricted-access, self-flagged as needing quality cleanup in places, and not aggregated into anything dashboard-ready. Land subsidence and salinity intrusion, and a dedicated sector damage-functions library, remain confirmed, total gaps — nothing in either DCCE inventory speaks to them at all.

**New this session:** a pointer to other risk-assessment result sources beyond what this node's own methodology and sector-results content covers — no directory of "other sources" exists as a distinct asset, a genuine new GAP, restored from v6 alongside the rest of this node's content.

### Coverage tally

1 full · 10 partial · 4 gap (out of 15 requirements)

### Assessment

This is the most heavily "partial" node in the entire sitemap, and that's not a coincidence — it's the analytical layer that everything else feeds into, so its gaps are structural rather than cosmetic. The single genuine full-coverage item (the impact-chain methodology) is real strength, but it's being stretched across roles it wasn't written for. The three confirmed gaps are not small: a damage-functions library and land subsidence/salinity data are foundational modeling inputs that a build-phase team cannot substitute with existing DCCE material at all — these need genuine data-partnership work (likely with the Marine Department, DMCR, or academic partners), not content writing. The ten partial items are where the bulk of the build effort should concentrate, and per-item specificity matters here more than almost anywhere else in the sitemap: "SME business disruption risk," "mental health loss," and "cultural heritage loss" are each a fully separate content-sourcing task, not a subset of what already exists.

---

## Node 3.3 — Adaptation Planning & Measures Library

*Rolls up: Participatory Planning & Project Design Guidance (3.3.1), National Adaptation Strategy Roadmap (3.3.2), Sector Adaptation Measures Library (3.3.3), Adaptation Planning Case Studies (3.3.4), Ongoing Projects (3.3.5) — 11 requirements (v1: 13; −2, ongoing-project tracking and budget-readiness indicators moved to node 3.4 this session, since 3.3.5 now points to 3.4.2's Adaptation M&E Platform instead of describing its own content).*

### What this node needs, in full

Cost-benefit/avoided-losses analysis methodology; gender-equality and social-inclusion (GESI) integration guidance; protection-measure information for named vulnerable groups (children, elderly, disabled, border/coastal communities); guidance on applying local wisdom, traditional knowledge, and cultural heritage to community adaptation; a roadmap/staging diagram for national adaptation strategy execution; a systemic-barriers report by sector; a list of financial, technology, and capacity-building support needs; personnel-development needs for climate-fund proposal writing; a searchable database of technical/policy adaptation measures by hazard, sector, and budget; and a combined list of grey-infrastructure and nature-based adaptation measures. (Ongoing-project tracking and budget-readiness indicators now live under node 3.4 — see below.)

### What actually exists

Only one item is fully covered — the NAP roadmap/staging diagram, sourced directly from the National Adaptation Plan document and dataset. Three items are partial: vulnerable-group protection measures (a heat-health media piece exists but doesn't name any of the four required groups specifically); financial/technology/capacity-building support needs (financial funding sources are well documented, but technology and capacity-building tracking are absent — the same pattern found in node 2.3); and the grey-infrastructure/nature-based measures list (three separate assets cover nature-based solutions in depth, but grey/structural infrastructure measures have nothing at all).

Seven of eleven requirements are total gaps: cost-benefit/avoided-losses methodology, GESI integration guidance, local-wisdom/cultural-heritage application guidance, the systemic-barriers report, climate-fund-proposal personnel development, the searchable measures database, and the local/private-sector plans repository.

### Coverage tally

1 full · 3 partial · 7 gap (out of 11 requirements)

### Assessment

This is, by gap count, still the single weakest section of the sitemap, even after two of its gaps moved to node 3.4. It's also the node where the "planning and doing" layer of adaptation work lives — as opposed to node 3.2's "understanding the risk" layer — and DCCE's current holdings are heavily skewed toward the latter. Seven confirmed gaps in one node signals this isn't a scattering of individually small content tasks; it's a section that needs a dedicated planning-content work stream of its own.

---

## Node 3.4 — Monitoring & Evaluation of Adaptation

*Rolls up: Adaptation M&E Guidance (3.4.1), Thailand's M&E Database System (3.4.2), Successful Adaptation Project Case Studies (3.4.3) — 6 requirements (v1: 4; +2, ongoing-project tracking and budget-readiness indicators, moved from node 3.3 this session — 3.3.5 now points here instead of describing its own content).*

### What this node needs, in full

A technology-readiness-level framework for adaptation technology and innovation; a linkage to the international Global Goal on Adaptation indicators; a national tracker index for adaptation progress and vulnerability reduction by sector and province; a library of successful-project case studies with lessons learned; **a project-tracking system for ongoing national adaptation projects (moved from node 3.3 this session)**; and **budget-readiness indicators for those projects (moved from node 3.3 this session)**.

### What actually exists

The Global Goal on Adaptation linkage and the success-story case-study library are both fully covered, the latter unusually well — eight separate assets span multiple sectors and a dedicated lesson-extraction project. The national M&E tracker is also fully covered: its cited asset is a real, current dataset on DCCE's own live Data Governance Framework catalog, maintained by DCCE's dedicated Adaptation M&E Evaluation Group and tied to Thailand's official Biennial Transparency Report submitted under the UNFCCC. (This status was briefly questioned during the dataset-catalog cross-check, since the asset didn't appear in that narrower 260-item extract — checked directly against DCCE's live catalog instead, it verified out as real and current, so the original full-coverage rating stands.)

The technology-readiness-level framework was marked covered on a different basis than the rest of this node: rather than a document match, it was assumed in scope because it falls within DCCE's confirmed, actively maintained Adaptation M&E platform — the reasoning being that anything genuinely part of that platform's territory should be assumed covered, not checked item by item the way the rest of this report works. That's a judgment call worth a spot-check later, not a verified match.

**Moved in this session:** ongoing-project tracking and budget-readiness indicators carry the same status they had at node 3.3 — both total gaps. Nothing exists for either, and the tracking item is additionally gated on the M&E platform (item above) being mature enough to support it, not just on DCCE deciding to build it.

### Coverage tally

4 full · 0 partial · 2 gap (out of 6 requirements)

### Assessment

This node closed out mostly covered by two different routes worth keeping distinct: three items (GGA linkage, case-study library, M&E tracker) are genuine, individually-verified document or dataset matches. The technology-readiness-level framework is an assumption extended from the platform's confirmed existence, not an independently checked match — a build-phase team should still confirm that specific content exists before treating it as done. The two items moved in from node 3.3 this session are genuine gaps, not an artifact of the merge — nothing existed for either before, and moving where they're described doesn't change what exists. Separately, this node's M&E tracker status is the clearest example in this whole exercise of why the 260-item WP2 dataset catalog should never be read as DCCE's complete inventory — an asset's absence from that extract only means the extract didn't capture it, not that DCCE doesn't have it.

---

## Node 4 — Tools & Services (merged from 4.1/4.2/4.3, 2026-08-20)

*Rolls up: Data Catalog (formerly 4.1), Climate Risk Map / Visualization and Analytics (formerly 4.2), External Tools & Data Hub (formerly 4.3), plus 2 new mockup-sourced items — 5 requirements (v1: 3 across three separate nodes; +2 new, both GAP).* Per Boss's decision this session, v9 removes the 4.1/4.2/4.3 split in favor of one searchable, tag-filterable tool grid, so this document now treats Section 4 as one node rather than three, matching the sitemap.

### What this node needs, in full

A searchable system for raw datasets, analytical data products, and their metadata descriptions, meeting national data-security standards (Data Catalog). An interactive web application showing hazard maps and risk analysis, specifically able to give a civil engineer rainfall-intensity and temperature design values at the plot level — Intensity-Duration-Frequency (IDF) curves and design curves (Climate Risk Map / visualization application). Connection points to international and specialized external data portals — the Meteorological Department's Weather API, GISTDA's Geo-Informatics Portal, the Copernicus Climate Data Store (External Tools & Data Hub). **Two new, mockup-sourced tool cards with no Layer 1/2 requirement behind them (added to the sitemap this session, flagged unvalidated): a Climate Impact Explorer, and an Adaptation Options Explorer.**

### What actually exists

Data Catalog is fully covered: DCCE already operates a live data catalog system, has a publication describing it, and has a data governance manual covering metadata and security standards.

The Climate Risk Map / visualization application is more mixed than it first looks. DCCE's existing risk-map web application is a real, working interactive tool, and the dataset-catalog cross-check confirmed genuine spatial risk data (the same provincial composite-index and hazard-map data found elsewhere in this exercise, and the same shared build now merged with node 1.2/2.2's risk-map cluster at the DRD level) sits behind it — so the general "interactive map + risk visualization" half is reasonably well served. The specific civil-engineering half is not: an explicit search across both DCCE's document/publication inventory and its separate dataset catalog for anything resembling IDF curves or engineering design curves came back completely empty — not "narrative material exists but isn't structured," but zero material of any kind, anywhere. That gap is the requirement's actual differentiator (the reason this is a distinct capability rather than a duplicate of the general risk map elsewhere on the site), so reading the PARTIAL rating as "mostly there" would badly underestimate the remaining work — producing IDF curves means computing them from rainfall intensity-duration-frequency statistics that don't exist in any form in DCCE's current holdings.

External Tools & Data Hub is a total, confirmed gap — but a different kind of gap than most in this sitemap: this isn't missing content DCCE needs to produce, it's missing integration work (API connections, access agreements with named external agencies), a technical-partnership task for the build team, not a content-sourcing task.

**New this session:** neither Climate Impact Explorer nor Adaptation Options Explorer has any Layer 1/2 requirement or DRD deliverable behind it — both originated in mockup production, not the original 73-item extraction. Both are genuine, confirmed gaps for now, but of a third kind again: not missing content and not missing integration work, but an open question of whether these should be committed deliverables at all. That decision belongs to a future DRD pass.

### Coverage tally

1 full · 1 partial (with a hidden gap inside it) · 3 gap (out of 5 requirements)

### Assessment

This merged node now spans three genuinely different kinds of work under one roof: infrastructure that's done (Data Catalog), a real tool with one hard-blocked engineering-specific gap inside an otherwise-served requirement (Climate Risk Map), integration work rather than content work (External Tools & Data Hub), and two items that shouldn't be scoped as build work at all until DCCE decides they're real (the two mockup-sourced explorers). A build-phase team reading only the coverage tally would badly misread this node — each of its five items needs a different kind of next step, not one shared content-production plan.

---

## Node 5.1 — Announcements & Engagement Activities

*Direct node, 1 requirement.*

### What this node needs, in full

A system for distributing data-update announcements and workshop/training activities focused on analyzing and interpreting climate data for spatial planning.

### What actually exists

Fully covered: DCCE's existing seminar/training system and its public-relations news publication channel both directly serve this requirement.

### Coverage tally

1 full · 0 partial · 0 gap (out of 1 requirement)

### Assessment

Straightforward — existing DCCE operational systems already do what this page asks for; this is a linking task, not a content or data task.

---

## Node 5.2 — Feedback Channels & User Services

*Direct node, 1 requirement.*

### What this node needs, in full

A systematic platform for user agencies to give feedback aimed at improving dataset quality, expanding service scope, and verifying that institutional needs are being met.

### What actually exists

Nothing — a total, confirmed gap.

### Coverage tally

0 full · 0 partial · 1 gap (out of 1 requirement)

### Assessment

This is a genuinely new capability for DCCE to build, not a content gap — a structured feedback/service-quality mechanism doesn't currently exist in any form. Pairs naturally with node 4.3 as a "build a new operational capability" work item, distinct from the rest of this report's "find or produce content" gaps.

---

## Summary Table (v9)

| Node | Topic | Full | Partial | Gap | Total | Δ vs. v1 |
|---|---|---|---|---|---|---|
| 1.1 | Overview of Thailand's Climate Risk | 4 | 1 | 2 | 7 | unchanged |
| 1.2 | Area-Based Data Search | 0 | 1 | 2 | 3 | unchanged |
| 2.1 | National Climate Change Situation | 0 | 2 | 1 | 3 | unchanged |
| 2.2 | Area and Sector Risk Profile Summary | 0 | 1 | 1 | 2 | unchanged |
| 2.3 | Policy, Legal & Financial Tools | 4 | 3 | 5 | 12 | +1 partial (NAP status, v6) |
| ~~2.4~~ | ~~Planning Data Services~~ | — | — | — | — | *retired, −3 (2 full, 1 partial)* |
| 3.1 | Climate Drivers: Observation, Drivers & Future Scenarios | 0 | 4 | 5 | 9 | +1 partial (scenario source, v6) |
| 3.2 | Risk, Vulnerability, Impact-Chain & Loss-and-Damage Analysis | 1 | 10 | 4 | 15 | +1 gap (other risk sources, v6) |
| 3.3 | Adaptation Planning & Measures Library | 1 | 3 | 7 | 11 | −2 gap (moved to 3.4) |
| 3.4 | Monitoring & Evaluation of Adaptation | 4 | 0 | 2 | 6 | +2 gap (moved from 3.3) |
| 4 | Tools & Services (merged 4.1+4.2+4.3) | 1 | 1 | 3 | 5 | merged 3 nodes into 1; +2 gap (mockup explorers) |
| 5.1 | Announcements & Engagement Activities | 1 | 0 | 0 | 1 | unchanged |
| 5.2 | Feedback Channels & User Services | 0 | 0 | 1 | 1 | unchanged |
| **Total** | | **16** | **26** | **33** | **75** | net +2 nodes' worth of items, −1 node count |

Node 3.3 (Adaptation Planning & Measures) is still the single weakest cluster by gap count even after losing 2 gaps to node 3.4 — 7 confirmed gaps, the largest of any node. Node 3.1 (Climate Drivers) follows at 5. Node 3.2 (Risk & Loss-Damage Analysis) is the largest concentration of partial coverage, at 10 of its 15 requirements. Nodes 3.4, 5.1, and 5.2 sit at the opposite extremes — mostly solved or fully unaddressed; Node 4 no longer belongs in that "extreme" group post-merge, since it now spans a genuine, mixed 1/1/3 split across three different kinds of gap (see its own assessment above).
