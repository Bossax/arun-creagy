# WP4 Content-Source Gap Analysis — Node-Level Deep Dives

**Date:** 11 August 2026
**Companion to:** `2026-08-10-WP4-Content-Source-Gap-Analysis-Report.md`

## What this document is

The main report makes its case with three worked examples, picked to illustrate the method. This document extends that same page-by-page treatment to every **second-level sitemap node** (the `X.X` grain — e.g. `2.3`, `3.2`, `4.2`) rather than stopping at three. Third-level and fourth-level sub-items (`X.X.X`, `X.X.X.X`) are not broken out as their own sections here — where a second-level node has sub-nodes under it, this document rolls all of that node's requirements up into one write-up, so the grain matches how the sitemap is actually organized into topical sections, not every individual bullet point.

All 15 second-level nodes are covered below, in sitemap order. Per the same convention as the main report: no internal asset codes or reference IDs in the body — real names and plain descriptions throughout. Full traceability (asset IDs, exact match rationale) lives in the working CSV.

The per-node tallies below sum to the same totals as the main report: **21 full, 24 partial, 28 gap, 73 requirements.**

---

## Node 1.1 — Overview of Thailand's Climate Risk

*Rolls up: Overview of Climate Change Risk in Thailand (1.1.1), Key Risks and National Adaptation Priorities (1.1.2) — 7 requirements.*

### What this node needs, in full

Historical natural-disaster trends and history for the country; the IPCC-standard hazard/exposure/vulnerability concept framework; an understanding of physical risk versus transition risk; national risk-profile summary cards; sector- and region-level adaptation hotspots; a National Adaptation Plan (NAP) summary; and examples of high-value, proactive adaptation measures.

### What actually exists

The IPCC framework definitions are well covered — the impact-chain manual embeds the methodology, and a dataset is explicitly tagged with IPCC, vulnerability, and adaptation terms. Sector and regional hotspots have a real, purpose-built source in the six-sector spatial risk dataset. The NAP summary is one of the strongest matches anywhere in the sitemap — the official document itself, a dataset entry, and multiple English- and Thai-language media explainers all exist. High-value adaptation measure examples are backed by a cross-sector success-factors media piece and a nature-based-solutions dataset with concrete content.

What's missing or partial: historical disaster trend history has nothing behind it at all — no dataset or publication tracks Thailand's natural-disaster history as a narrative or time series. Physical-risk-versus-transition-risk framing, a conceptual pairing common in climate-finance literature, is also a total gap. And the risk-profile summary cards, after the dataset-catalog cross-check, moved from gap to partial: DCCE's seven-sector composite risk index supplies real numbers, but it's flagged draft/unverified and isn't rendered into anything resembling a summary card yet.

### Coverage tally

4 full · 1 partial · 2 gap (out of 7 requirements)

### Assessment

This node is the site's front door, and it's in genuinely good shape for the "here's what the country's adaptation priorities are" half — NAP summary and hotspot data are strong, reusable assets. But the "why this matters" framing half is thinner than it looks: historical disaster trends and transition-risk framing are both completely unaddressed, and they're exactly the kind of scene-setting content a front-door page needs before it gets into NAP details. Both gaps are also unusually cheap relative to most gaps in this sitemap — historical disaster trends, in particular, is closer to a compilation task from existing (if scattered) government records than new data collection.

---

## Node 1.2 — Area-Based Data Search

*Direct node, 3 requirements.*

### What this node needs, in full

A search hierarchy supporting province → district → subdistrict administrative levels; map integration overlaying administrative boundaries on the spatial risk map; and a quick-view dashboard showing point-level vulnerability, key threats, and initial recommended measures.

### What actually exists

The spatial risk map overlay is fully covered — DCCE's existing risk-map web application, backed by the six-sector spatial dataset and, per the dataset-catalog cross-check, further supported by province-granularity composite risk index data, genuinely does render spatial risk over administrative boundaries. The quick-view dashboard is partial: the same web application could plausibly be extended into a point-level summary UI, and real vulnerability/threat data exists to populate half of it, but the "recommended measures" half has zero data support anywhere, and no purpose-built dashboard product exists yet.

The administrative search hierarchy itself (province → district → subdistrict drill-down) is a pure gap — and a different kind of gap than most in this report: it's a navigation/UI feature, not something a document or dataset would ever directly address.

### Coverage tally

1 full · 1 partial · 1 gap (out of 3 requirements)

### Assessment

This node is really two different kinds of work wearing one page title. The map-overlay piece is close to done. The search hierarchy is a pure engineering/UX build task with no content-sourcing angle at all — worth flagging to the build team early so it isn't mistakenly bundled into "content gap" planning and left unscoped. The quick-view dashboard's "recommended measures" gap connects to a pattern that recurs across the sitemap: DCCE's inventory is much better at describing risk than prescribing what to do about it.

---

## Node 2.1 — National Climate Change Situation

*Direct node, 3 requirements.*

### What this node needs, in full

Historical extreme-weather-event statistics (temperature max/min, cumulative rainfall); a macroeconomic loss-and-damage statistics database; and a summary of national exposure trends.

### What actually exists

Exposure trends are fully covered by the six-sector spatial dataset. The other two both improved under the dataset-catalog cross-check but remain partial: historical extreme-weather statistics now have real underlying data (1981–2023 daily/monthly temperature and rainfall grids), though it's Restricted-access raw grid data, not pre-computed event statistics. The macroeconomic loss-and-damage database is confirmed partial even after the deeper check — real per-hazard economic loss records exist in the dataset catalog, but nothing aggregates them into a genuine macroeconomic database, and the records are fragmented, access-restricted, and self-flagged by their own source as needing data-quality cleanup.

### Coverage tally

1 full · 2 partial · 0 gap (out of 3 requirements)

### Assessment

No total gaps here, which sounds like good news, but both partial items need real technical work rather than simple content sourcing — turning raw climate grids into usable statistics, and consolidating fragmented per-hazard loss records into a coherent macroeconomic database, are data-engineering tasks, not writing tasks. A good example of why "nothing is a flat gap" doesn't mean "this page is nearly done."

---

## Node 2.2 — Area and Sector Risk Profile Summary

*Direct node, 2 requirements.*

### What this node needs, in full

Risk and vulnerability profile summaries at both the sub-national level (all 77 provinces plus local government) and by the six priority sectors.

### What actually exists

The sector-specific version is fully covered — the same six-sector spatial risk dataset, reused extensively across this sitemap, is organized exactly along the sector lines the requirement asks for. The province/local-government version has nothing behind it at all: no dataset or publication currently disaggregates risk profiles down to all 77 provinces and local administrative units in a summarized, ready-to-use form.

### Coverage tally

1 full · 0 partial · 1 gap (out of 2 requirements)

### Assessment

A clean, sharply-defined node — half genuinely done, half a genuine gap. The gap is notable because the underlying province-level risk data does exist elsewhere in DCCE's holdings (the composite risk index found during the dataset-catalog cross-check is province-level), so this may be less a "no data" problem and more a "no summarized, localized presentation layer built on top of existing data" problem — worth a build-team conversation about whether this is really a content gap or a product-design gap.

---

## Node 2.3 — Policy, Legal & Financial Tools

*Rolls up: direct node-level requirements, plus Funding Sources & Budget Tracking (2.3.1) and Institutional Mechanisms & Coordination (2.3.2) — 11 requirements total.*

### What this node needs, in full

At the node's own level: the implementation status of Thailand's draft Climate Change Act; a summary of supporting legal/policy instruments (disaster-prevention law, town-planning regulations); and a certification system for an "avoided losses" analysis tool. Under Funding Sources & Budget Tracking: a directory of public/private/international funding sources with a cost-benefit methodology guide for budget justification; statistics on national budget allocation and climate budget tagging; tracking of financial aid, technology transfer, and technical assistance received from major climate funds; and engagement/mobilization of private-sector finance. Under Institutional Mechanisms & Coordination: DCCE's role as national focal point; the structure of the national climate policy committee and sub-committees; coordination mechanisms between national and local government; and civil-society/private-sector/academic participation channels and statistics.

### What actually exists

The Climate Change Act's status is well covered — an official summary, the full draft text, and two media explainers all exist. DCCE's role as national focal point, the policy committee's structure, and public-participation statistics are all backed by real, purpose-built documents or datasets (committee appointment orders, multi-year public disclosure publications, an active participation-tracking system). The funding-sources directory is genuinely solid: DCCE's own funding guide plus dedicated publications for each of the three major international climate funds, and DCCE's own internal process for endorsing fund project proposals is real, operational documentation, not just a description.

Beyond straightforward financial tracking, coverage drops sharply. No cost-benefit/budget-justification methodology guide exists — only fund directories, which are a different thing. No budget-allocation statistics or climate budget tagging exist at all. And — repeating a pattern that shows up elsewhere in the sitemap — technology transfer and technical assistance tracking are consistently absent; every matched asset for the "financial aid, technology, and technical assistance" requirement turns out to track money only. The avoided-losses certification system, national-to-local coordination mechanisms, and private-sector finance mobilization are all total gaps as well.

### Coverage tally

4 full · 2 partial · 5 gap (out of 11 requirements)

### Assessment

This node's headline number is more mixed than it first looks: just over a third of its requirements are fully covered, concentrated almost entirely in "what money exists, who's in charge, and how is participation tracked." Everywhere the requirement asks for something adjacent to that — cost-benefit justification, budget tagging, technology transfer, technical assistance, cross-level coordination, an avoided-losses certification model — coverage is thin or absent. That's a specific, nameable content-production program (methodology guides, a technology/capacity-building tracking mechanism, an intergovernmental coordination write-up), not a scattering of unrelated small gaps, and it's a larger lift than the full-coverage count alone would suggest.

---

## Node 2.4 — Planning Data Services

*Direct node, 3 requirements.*

### What this node needs, in full

Local vulnerability and adaptive-capacity indices and statistics; integrated spatial risk maps; and national data-security guidance for academic and research search use.

### What actually exists

The integrated spatial risk map and the data-security guidance are both fully covered — the former by the same reused risk-map application and dataset, the latter by DCCE's existing data-governance manual, available in both document and media form. Local vulnerability and adaptive-capacity indices remain partial: a methodology explainer exists, and the dataset-catalog cross-check found a genuinely large body of underlying proxy indicators (weather-station density, water-monitoring station counts, agricultural census vulnerability measures), but nothing computes these into an actual composite index — the raw ingredients exist, the index itself doesn't.

### Coverage tally

2 full · 1 partial · 0 gap (out of 3 requirements)

### Assessment

One of the strongest nodes in the sitemap. The one partial item is a well-defined, comparatively easy build task: DCCE has plenty of province-level proxy data for vulnerability and adaptive capacity, so producing an actual index is a data-synthesis exercise using existing inputs, not a new data-collection effort — a materially lighter lift than most other partial items in this report.

---

## Node 3.1 — Climate Drivers: Observation, Drivers & Future Scenarios

*Rolls up: Observational Data (3.1.1), Climate Drivers (3.1.2), Future Climate Scenarios (3.1.3) — 8 requirements.*

### What this node needs, in full

Short/medium-term weather-station data (in cooperation with the Meteorological Department); satellite observation data covering forest cover, land cover, water bodies, and coral bleaching; monitoring data for internationally significant climate phenomena (ENSO, AMOC); climatology and key climate-variable data (temperature and rainfall trends); a usage guide for climate scenarios; a library of high-resolution downscaled national future-climate projections; a national standard for managing forecast uncertainty and choosing between projection datasets; and case studies applying climate-projection models to long-term strategic planning.

### What actually exists

This is the weakest node in the entire sitemap on a raw-document basis, and the dataset-catalog cross-check only partially rescues it. Three items move to genuine partial coverage: climatology variables and downscaled climate projections both turn out to have real, multi-decade national grid datasets behind them (1981–2023 historical records; downscaled projections running through 2099 using both dynamical and statistical methods) — though both are Restricted-access, raw-grid, and national- rather than sub-national-resolution. ENSO/AMOC monitoring is also partial, but weakly so: a single general-audience media piece exists for ENSO, and AMOC has nothing at all.

Five of the eight requirements remain confirmed, total gaps even after the deeper check: station-level weather data, satellite observation data, a climate-scenario usage guide, a national uncertainty-governance standard, and climate-projection case studies for strategic planning. None of these turned up anywhere in either DCCE inventory.

### Coverage tally

0 full · 3 partial · 5 gap (out of 8 requirements)

### Assessment

This is the only node in the entire sitemap with zero full-coverage items, and even its partial items are raw, access-restricted, unprocessed data rather than anything close to publishable. This is the single clearest data-partnership priority in the whole exercise: real value would come from formal access arrangements with the Meteorological Department, the Marine Department, and whoever holds the underlying downscaled-projection modeling runs, rather than from DCCE content production. Framing this node as a "content gap" for a writer to fill would badly misdescribe the actual work required.

---

## Node 3.2 — Risk, Vulnerability, Impact-Chain & Loss-and-Damage Analysis

*Rolls up: Vulnerability & Exposure Analysis (3.2.1), Risk Analysis (3.2.2), Slow-Onset Hazard Tracking (3.2.2.1), Impact-Chain Analysis (3.2.3), Loss & Damage (3.2.4), Theoretical Framework & Manuals (3.2.5) — 14 requirements total.*

### What this node needs, in full

This is the analytical core of the whole platform — the place where raw hazard/exposure data is meant to turn into actual risk findings. Across its six sub-sections it needs: definitions of vulnerability/exposure/sensitivity/adaptive-capacity/resilience concepts; a library of sector-specific damage functions for hazard modeling; a single national risk-assessment methodology; sector-by-sector risk results (food security, water security, heat-health impact, SME business disruption); statistics and tracking for slow-onset hazards (rising average temperature and shifting rainfall patterns, sea-level rise, land subsidence, salinity intrusion, coastal erosion); a multi-hazard impact-chain diagram plus sector case studies (agriculture, urban); a Loss & Damage theoretical framework tied to the UNFCCC; a dashboard summarizing historical economic and physical losses; a record of non-economic losses (mental health, biodiversity, cultural heritage); and a standardized national manual for risk/impact/L&D calculation methodology.

### What actually exists

One real strength anchors this whole cluster: DCCE's impact-chain methodology manual. It's a genuine, purpose-built document, and it gets reused — appropriately — as the closest available source for four separate requirements: the general risk-assessment standard, the multi-hazard impact-chain diagram, the vulnerability/exposure concept definitions (partially — sensitivity and resilience are only implicit in it, not explicit), and the national L&D calculation manual. That reuse is legitimate, but it also means the same single document is being asked to stand in for several distinct things DCCE doesn't actually have purpose-built versions of yet.

Beyond that: DCCE's six-sector spatial risk dataset supplies real sector-level risk results for food, water, and settlement-related risks (though heat-specific health impact and SME business disruption are not represented). A 2025 flood case study gives a strong urban impact-chain example but nothing for agriculture. The Loss & Damage fund page and DCCE's commissioned assessment report are the closest things to a framework explainer and a loss dashboard, respectively — both are real and relevant, but one is a financing page (not a framework document) and the other is a static report (not dashboard-ready data). Non-economic loss material exists only for biodiversity; mental health and cultural heritage have nothing.

The follow-up cross-check against DCCE's separate dataset catalog changed the picture for the slow-onset hazard sub-section specifically: real annual sea-level observation data exists (previously recorded as a total gap), and the coastal erosion sub-requirement turned out to have genuine area-based erosion-extent data behind it, not just the narrative infographics originally credited. It also strengthened the Loss & Damage dashboard's evidence — real, machine-readable annual damage and property-loss records exist for several hazards, not just the one static report. Both upgrades come with the same caveat as elsewhere in this cross-check: the data is Restricted-access, self-flagged as needing quality cleanup in places, and not aggregated into anything dashboard-ready. Land subsidence and salinity intrusion, and a dedicated sector damage-functions library, remain confirmed, total gaps — nothing in either DCCE inventory speaks to them at all.

### Coverage tally

1 full · 10 partial · 3 gap (out of 14 requirements)

### Assessment

This is the most heavily "partial" node in the entire sitemap, and that's not a coincidence — it's the analytical layer that everything else feeds into, so its gaps are structural rather than cosmetic. The single genuine full-coverage item (the impact-chain methodology) is real strength, but it's being stretched across roles it wasn't written for. The three confirmed gaps are not small: a damage-functions library and land subsidence/salinity data are foundational modeling inputs that a build-phase team cannot substitute with existing DCCE material at all — these need genuine data-partnership work (likely with the Marine Department, DMCR, or academic partners), not content writing. The ten partial items are where the bulk of the build effort should concentrate, and per-item specificity matters here more than almost anywhere else in the sitemap: "SME business disruption risk," "mental health loss," and "cultural heritage loss" are each a fully separate content-sourcing task, not a subset of what already exists.

---

## Node 3.3 — Adaptation Planning & Measures Library

*Rolls up: Participatory Planning & Project Design Guidance (3.3.1), National Adaptation Strategy Roadmap (3.3.2), Sector Adaptation Measures Library (3.3.3), Adaptation Planning Case Studies (3.3.4), Ongoing Projects (3.3.5) — 13 requirements.*

### What this node needs, in full

Cost-benefit/avoided-losses analysis methodology; gender-equality and social-inclusion (GESI) integration guidance; protection-measure information for named vulnerable groups (children, elderly, disabled, border/coastal communities); guidance on applying local wisdom, traditional knowledge, and cultural heritage to community adaptation; a roadmap/staging diagram for national adaptation strategy execution; a systemic-barriers report by sector; a list of financial, technology, and capacity-building support needs; personnel-development needs for climate-fund proposal writing; a searchable database of technical/policy adaptation measures by hazard, sector, and budget; a combined list of grey-infrastructure and nature-based adaptation measures; a repository of local/private-sector risk-management plans; a project-tracking system for ongoing national adaptation projects; and budget-readiness indicators for those projects.

### What actually exists

Only one item is fully covered — the NAP roadmap/staging diagram, sourced directly from the National Adaptation Plan document and dataset. Three items are partial: vulnerable-group protection measures (a heat-health media piece exists but doesn't name any of the four required groups specifically); financial/technology/capacity-building support needs (financial funding sources are well documented, but technology and capacity-building tracking are absent — the same pattern found in node 2.3); and the grey-infrastructure/nature-based measures list (three separate assets cover nature-based solutions in depth, but grey/structural infrastructure measures have nothing at all).

Nine of thirteen requirements are total gaps: cost-benefit/avoided-losses methodology, GESI integration guidance, local-wisdom/cultural-heritage application guidance, the systemic-barriers report, climate-fund-proposal personnel development, the searchable measures database, the local/private-sector plans repository, the ongoing-projects tracking system, and budget-readiness indicators.

### Coverage tally

1 full · 3 partial · 9 gap (out of 13 requirements)

### Assessment

This is the largest node by requirement count and, by gap count, the single weakest section of the sitemap. It's also the node where the "planning and doing" layer of adaptation work lives — as opposed to node 3.2's "understanding the risk" layer — and DCCE's current holdings are heavily skewed toward the latter. Nine confirmed gaps in one node signals this isn't a scattering of individually small content tasks; it's a section that needs a dedicated planning-content work stream of its own, likely requiring input from DCCE program/project staff directly (ongoing-project status, budget readiness) rather than anything findable in an inventory search.

---

## Node 3.4 — Monitoring & Evaluation of Adaptation

*Rolls up: Adaptation M&E Guidance (3.4.1), Thailand's M&E Database System (3.4.2), Successful Adaptation Project Case Studies (3.4.3) — 4 requirements.*

### What this node needs, in full

A technology-readiness-level framework for adaptation technology and innovation; a linkage to the international Global Goal on Adaptation indicators; a national tracker index for adaptation progress and vulnerability reduction by sector and province; and a library of successful-project case studies with lessons learned.

### What actually exists

The Global Goal on Adaptation linkage and the success-story case-study library are both fully covered, the latter unusually well — eight separate assets span multiple sectors and a dedicated lesson-extraction project. The national M&E tracker is also fully covered: its cited asset is a real, current dataset on DCCE's own live Data Governance Framework catalog, maintained by DCCE's dedicated Adaptation M&E Evaluation Group and tied to Thailand's official Biennial Transparency Report submitted under the UNFCCC. (This status was briefly questioned during the dataset-catalog cross-check, since the asset didn't appear in that narrower 260-item extract — checked directly against DCCE's live catalog instead, it verified out as real and current, so the original full-coverage rating stands.)

The technology-readiness-level framework was marked covered on a different basis than the rest of this node: rather than a document match, it was assumed in scope because it falls within DCCE's confirmed, actively maintained Adaptation M&E platform — the reasoning being that anything genuinely part of that platform's territory should be assumed covered, not checked item by item the way the rest of this report works. That's a judgment call worth a spot-check later, not a verified match.

### Coverage tally

4 full · 0 partial · 0 gap (out of 4 requirements)

### Assessment

This node closed out fully covered, but by two different routes worth keeping distinct: three items (GGA linkage, case-study library, M&E tracker) are genuine, individually-verified document or dataset matches. The fourth (technology-readiness-level framework) is an assumption extended from the platform's confirmed existence, not an independently checked match — a build-phase team should still confirm that specific content exists before treating it as done. Separately, this node's M&E tracker status is the clearest example in this whole exercise of why the 260-item WP2 dataset catalog should never be read as DCCE's complete inventory — an asset's absence from that extract only means the extract didn't capture it, not that DCCE doesn't have it. Any other reclassification from that cross-check that hasn't been independently re-verified against DCCE's live catalog carries the same residual uncertainty.

---

## Node 4.1 — Data Catalog

*Direct node, 1 requirement.*

### What this node needs, in full

A searchable system for raw datasets, analytical data products, and their metadata descriptions, meeting national data-security standards.

### What actually exists

Fully covered: DCCE already operates a live data catalog system, has a publication describing it, and has a data governance manual covering metadata and security standards.

### Coverage tally

1 full · 0 partial · 0 gap (out of 1 requirement)

### Assessment

The cleanest node in the sitemap — infrastructure that already exists and just needs linking into the new portal, not rebuilding. This is the report's featured "this one is genuinely done" example, and the node-level view confirms there's nothing more to check here.

---

## Node 4.2 — Visualization and Analytics Application

*Direct node, 1 requirement.*

### What this node needs, in full

An interactive web application that shows hazard maps and lets a user run risk analysis, specifically built so a civil engineer could pull out rainfall-intensity and temperature design values at the plot level — i.e., Intensity-Duration-Frequency (IDF) curves and design curves for infrastructure engineering.

### What actually exists

DCCE's existing risk-map web application is the closest thing to this — it's a real, working interactive tool, and the dataset-catalog cross-check confirmed genuine spatial risk data (the same provincial composite-index and hazard-map data found elsewhere in this exercise) sits behind it. So the general "interactive map + risk visualization" half of this requirement is reasonably well served.

The specific civil-engineering half is not. An explicit search across both DCCE's document/publication inventory and its separate dataset catalog for anything resembling IDF curves or engineering design curves came back completely empty — not "narrative material exists but isn't structured," but zero material of any kind, anywhere.

### Coverage tally

0 full · 1 partial (with a hidden gap inside it) · 0 gap (out of 1 requirement)

### Assessment

This node is a caution against reading "partial" as "mostly there." The page-level score is partial because a real, general-purpose visualization tool exists — but the requirement's actual differentiator, the reason it's a distinct node instead of a duplicate of the general risk map elsewhere in the sitemap, is the IDF/design-curve output for engineers, and that piece is a hard, total gap. If a build-phase planner reads "partial" and assumes most of the work is done, they will badly underestimate this page: producing IDF curves means computing them from rainfall intensity-duration-frequency statistics, which don't exist in any form in DCCE's current holdings, national or local grid. This is closer in effort to the confirmed gaps in node 3.2 than to the other partial items in this document.

---

## Node 4.3 — External Tools & Data Hub

*Direct node, 1 requirement.*

### What this node needs, in full

Connection points to international and specialized external data portals — named examples include the Meteorological Department's Weather API, GISTDA's Geo-Informatics Portal, and the Copernicus Climate Data Store.

### What actually exists

Nothing — this is a total, confirmed gap.

### Coverage tally

0 full · 0 partial · 1 gap (out of 1 requirement)

### Assessment

Worth flagging as a different kind of gap than most in this sitemap: this isn't missing content DCCE needs to produce, it's missing integration work — establishing API connections and access agreements with named external agencies and international data services. That's a technical-partnership task for the build team, not a content-sourcing task, and should be scoped and budgeted separately from the rest of this report's gap list.

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

## Summary Table

| Node | Topic | Full | Partial | Gap | Total |
|---|---|---|---|---|---|
| 1.1 | Overview of Thailand's Climate Risk | 4 | 1 | 2 | 7 |
| 1.2 | Area-Based Data Search | 1 | 1 | 1 | 3 |
| 2.1 | National Climate Change Situation | 1 | 2 | 0 | 3 |
| 2.2 | Area and Sector Risk Profile Summary | 1 | 0 | 1 | 2 |
| 2.3 | Policy, Legal & Financial Tools | 4 | 2 | 5 | 11 |
| 2.4 | Planning Data Services | 2 | 1 | 0 | 3 |
| 3.1 | Climate Drivers: Observation, Drivers & Future Scenarios | 0 | 3 | 5 | 8 |
| 3.2 | Risk, Vulnerability, Impact-Chain & Loss-and-Damage Analysis | 1 | 10 | 3 | 14 |
| 3.3 | Adaptation Planning & Measures Library | 1 | 3 | 9 | 13 |
| 3.4 | Monitoring & Evaluation of Adaptation | 4 | 0 | 0 | 4 |
| 4.1 | Data Catalog | 1 | 0 | 0 | 1 |
| 4.2 | Visualization and Analytics Application | 0 | 1 | 0 | 1 |
| 4.3 | External Tools & Data Hub | 0 | 0 | 1 | 1 |
| 5.1 | Announcements & Engagement Activities | 1 | 0 | 0 | 1 |
| 5.2 | Feedback Channels & User Services | 0 | 0 | 1 | 1 |
| **Total** | | **21** | **24** | **28** | **73** |

Node 3.3 (Adaptation Planning & Measures) and node 3.1 (Climate Drivers) are the two weakest clusters by gap count — 9 and 5 confirmed gaps respectively, together accounting for exactly half of the sitemap's 28 total gaps. Node 3.2 (Risk & Loss-Damage Analysis) is the largest concentration of partial coverage, at 10 of its 14 requirements. Nodes 4.1, 3.4, 5.1, and 4.3/5.2 sit at the opposite extremes — fully solved or fully unaddressed, with no middle ground.
