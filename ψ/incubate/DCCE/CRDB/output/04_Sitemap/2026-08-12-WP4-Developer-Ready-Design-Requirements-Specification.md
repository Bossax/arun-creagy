# NCAIF Website — Design Requirements for the Build Phase

**Date** 12 August 2026
**Covers** All 73 content and function requirements across the 15 main sections of the site map
**Companion to** `2026-08-11-WP4-Node-Level-Deep-Dives.md` and `2026-08-10-WP4-Content-Source-Gap-Analysis-Report.md`

---

## How to read this document

The earlier analysis said which parts of the planned website have content behind them and which do not. It stopped there. A developer reading it still could not tell what to build, because "gap" describes a hole rather than a specification.

This document turns that analysis into instructions. It keeps the same order as the site map, section 1.1 through 5.2, so anyone who knows the site map already knows how to navigate this. Nothing has been regrouped.

There are two ways through it.

**If you are reviewing the plan for the website**, read the body straight through. Each section of the site appears in order, and under each one every requirement is listed with what happens to it. You never need to read the appendices.

**If you are building the platform**, the requirement cards in the body are the specifications. Appendix A groups them into the smaller number of things you actually have to build, since several pages depend on the same underlying work. Appendix B2 holds the data specifications and one recommendation you should read before starting.

### The same content as data

Everything in the appendices is also published as CSV, in the same folder as this document, for anyone who needs to filter, sort or load it rather than read it.

| File | Holds |
|---|---|
| `2026-08-12-WP4-DRD-requirements.csv` | All 73 requirements, one per row, with status, handling, deliverable, brief, data specification, matched assets and the reasoning behind each match |
| `2026-08-12-WP4-DRD-deliverables.csv` | The 11 deliverables and the requirements each one serves |
| `2026-08-12-WP4-DRD-service-briefs.csv` | The 4 services awaiting a decision, with readiness and blocker |
| `2026-08-12-WP4-DRD-data-specs.csv` | The 11 data specifications as structured fields |
| `2026-08-12-WP4-DRD-assets-cited.csv` | The 86 assets cited, with owner, link, and which requirements rely on each |

The requirements file carries both the Thai requirement text and its English rendering, along with the status before and after the correction of 11 August, so the change is traceable without reading the diff.

### The five ways a requirement is handled

Not every requirement needs a full specification. Writing one for something that already exists wastes the reader's time, and writing one for a service nobody has agreed to build wastes the writer's. Each of the 73 requirements is handled in one of five ways.

| | Handling | Count | What you get |
|---|---|---|---|
| **A** | Already covered | 16 | One line naming the existing source |
| **B** | An existing product could sit here | 9 | One line naming the product, with an explicit warning that we have not verified whether its data is sufficient |
| **C** | Belongs to the loss and damage work | 4 | A forward reference, since that specification is not written yet |
| **D** | **Ready to build** | **30** | **A full specification with acceptance criteria** |
| **E** | Waiting on a decision | 14 | A summary in Appendix B, not a specification |

The thirty items marked D are the working part of this document.

---

## What the numbers say

Of 73 requirements, 16 are already served by something DCCE holds today. The remaining 57 need work, and they divide sharply.

Thirty can be specified and built now. Fourteen belong to services DCCE has not yet decided to build, so they are described rather than specified. Four belong to the loss and damage work being scoped separately. Nine sit on pages where an existing DCCE product could appear, and those carry an important caution explained below.

| Section | | A | B | C | D | E | Total |
|---|---|---|---|---|---|---|---|
| 1.1 | Overview of Thailand's climate risk | 3 | 2 | 0 | 2 | 0 | 7 |
| 1.2 | Area-based data search | 0 | 2 | 0 | 1 | 0 | 3 |
| 2.1 | National climate change situation | 0 | 1 | 1 | 1 | 0 | 3 |
| 2.2 | Area and sector risk profiles | 0 | 1 | 0 | 1 | 0 | 2 |
| 2.3 | Policy, legal and financial tools | 4 | 0 | 0 | 2 | 5 | 11 |
| 2.4 | Planning data services | 1 | 1 | 0 | 1 | 0 | 3 |
| 3.1 | Climate drivers and future scenarios | 0 | 0 | 0 | 6 | 2 | 8 |
| 3.2 | Risk, impact chains and loss and damage | 1 | 1 | 3 | 8 | 1 | 14 |
| 3.3 | Adaptation planning and measures | 1 | 0 | 0 | 6 | 6 | 13 |
| 3.4 | Monitoring and evaluation | 4 | 0 | 0 | 0 | 0 | 4 |
| 4.1 | Data catalog | 1 | 0 | 0 | 0 | 0 | 1 |
| 4.2 | Visualisation and analytics | 0 | 1 | 0 | 0 | 0 | 1 |
| 4.3 | External tools and data hub | 0 | 0 | 0 | 1 | 0 | 1 |
| 5.1 | Announcements and activities | 1 | 0 | 0 | 0 | 0 | 1 |
| 5.2 | Feedback and user services | 0 | 0 | 0 | 1 | 0 | 1 |
| | **Total** | **16** | **9** | **4** | **30** | **14** | **73** |

Two patterns are worth naming before the detail.

The build work concentrates in sections 3.1, 3.2 and 3.3. Those three sections hold twenty of the thirty ready-to-build items, and they are the analytical heart of the site. Sections 4.1, 3.4 and 5.1 are essentially finished and need only linking.

The waiting items also cluster. Nine of the fourteen belong to one service, the financial and budget evidence work, spread across sections 2.3 and 3.3. That is not fourteen scattered problems. It is mostly one decision DCCE has not taken yet.

---

## How each requirement was sorted

The sorting rests on the earlier analysis rather than on fresh judgement, and it uses one rule per category.

A requirement is **already covered** when the earlier analysis found a real DCCE document, dataset or system that serves it in full.

A requirement is **ready to build** when the work needed is self-contained. Someone can start it without waiting for a decision about which services DCCE will offer, and without waiting for another work package to finish. This includes content that needs writing, data that needs processing into a usable form, and new functions such as the feedback platform.

A requirement is **waiting on a decision** when the work only makes sense if DCCE commits to a service it has not yet committed to. Writing a full specification for these would imply a decision that has not been made. They get a summary instead, with a clear note that proper requirement gathering is needed if DCCE selects them.

A requirement **belongs to the loss and damage work** when it is part of the historical loss statistics product being specified separately. That specification is not written yet, so these four items point forward rather than sideways.

### A caution about the three existing products

Nine requirements sit on pages where one of DCCE's three existing analytical tools could appear. These are the spatial risk database, the hazard and exposure map, and the climate risk index.

**We do not know what data sits behind those tools, and this document does not assume anything about it.**

The asset registry tells us the tools exist and where they are published. It does not tell us what feeds them. The composite risk index makes this concrete. Its method multiplies and normalises its inputs in a way that cannot be reversed, so the published index cannot be traced back to the line agency data that produced it.

This matters because it is easy to look at a page, see that a risk map already exists, and conclude the page is nearly finished. The stricter review of 11 August found three requirements that had been recorded as complete on exactly that reasoning and were not.

So for these nine, this document says only that the page is a place where the product could appear. It does not claim the requirement is met, and it does not claim the remaining work is only interface work. **Appendix B2 carries a recommendation to resolve this properly at the start of the build phase.**

---

# The site, section by section

---

## 1.1 Overview of Thailand's climate risk

The front door of the site. It sets out what climate risk means for Thailand before a reader reaches anything detailed.

This section is in reasonable shape. The national adaptation plan summary is one of the best-supported requirements anywhere on the site, and the sector and regional analysis has a real dataset behind it. What is missing is the opening framing, the part that explains why any of this matters before the detail begins.

**Already covered**

- **REQ-002** The IPCC framework for hazard, exposure and vulnerability. Covered by DCCE's impact chain manual and a dataset tagged to IPCC terms.
- **REQ-006** National adaptation plan summary. Covered by the plan itself, a dataset entry, and several Thai and English explainers.
- **REQ-007** Examples of high-value adaptation measures. Covered by a success factors article spanning several sectors and a nature-based solutions dataset.

**An existing product could sit here**

- **REQ-004** National risk summary cards. The seven-sector composite risk index holds real numbers, but they are flagged draft and unverified, and nothing renders them as summary cards. Whether the index is fit for this purpose is **not assessed**.
- **REQ-005** Critical hotspots by sector and region. This is recorded as fully covered, and the source is the same risk dataset behind the existing products. It rests on the same reasoning that was found wanting for three other requirements during the 11 August review. Treat its completeness as **unverified** until the investigation in Appendix B2 is done.

### Ready to build

#### REQ-001 — History and trends of natural disasters in Thailand

**Status today** Nothing exists. No dataset or publication tracks Thailand's disaster history as a narrative or a time series.

**Who this is for** A first-time visitor, and a policy maker who needs the national picture before looking at any specific hazard.

**What exists today** No DCCE asset addresses this. Records exist across other government bodies, particularly the disaster prevention department, but they have not been gathered or written up.

**What the system must do**
- Present a chronological account of significant natural disasters in Thailand, covering at minimum flood, drought, storm and heat events.
- Show frequency and severity over time, so that a change in pattern is visible rather than asserted.
- Name the source and period for every figure shown.
- Link each hazard type to the relevant analysis section deeper in the site.

**Data spec** DS-08

**Done when**
- [ ] A reader can see how disaster frequency has changed over at least the last three decades.
- [ ] Every figure carries a named source and a date.
- [ ] Each hazard type links to its corresponding section of the site.
- [ ] The page states clearly which hazards are not covered and why.

**Note** This is compilation work rather than new data collection, which makes it one of the cheaper items in this document relative to its position on the site.

#### REQ-003 — Physical risk and transition risk

**Status today** Nothing exists.

**Who this is for** Policy makers and financial sector readers, for whom this distinction is standard vocabulary and its absence is conspicuous.

**What exists today** No DCCE asset addresses this pairing. It is common in climate finance material but absent from DCCE's holdings.

**What the system must do**
- Define physical risk and transition risk, and explain how they differ.
- Give Thai examples of each, drawn from sectors the site already covers.
- Explain why an organisation planning adaptation needs to consider both.
- Connect physical risk to the risk analysis sections and transition risk to the policy and finance sections.

**Data spec** None needed. This is explanatory content.

**Done when**
- [ ] Both terms are defined in plain Thai and English.
- [ ] At least two Thai examples are given for each.
- [ ] The page links to both the risk analysis and the policy sections.

---

## 1.2 Area-based data search

An interactive gateway rather than a page of content. It lets a user find risk information for a place they care about.

The whole section depends on data granularity, and that is where it runs into trouble. The existing spatial risk map holds composite indices at province level only. Districts and sub-districts do not exist in it.

**An existing product could sit here**

- **REQ-009** Map integration showing administrative boundaries over the risk map. No map overlay interface or design exists today. The spatial data exists, but whether it supports this overlay is **not assessed**.
- **REQ-010** Quick-view dashboard showing vulnerability, threats and recommended measures for a selected point. Real vulnerability data exists for part of it. The recommended measures half has nothing behind it anywhere on the site. Adequacy of the rest is **not assessed**.

### Ready to build

#### REQ-008 — Search by administrative level, province to district to sub-district

**Status today** Nothing exists, and the data to support the lower levels does not exist either.

**Who this is for** A provincial or local government planner who thinks in terms of their own administrative area, not in terms of grid cells.

**What exists today** The spatial risk database provides composite risk indices at province level. District and sub-district figures are not in it and would have to come from other agencies. Provincial climate change plans exist and are scattered. They contain sectoral and location-specific risk information that could populate the lower levels, but they are documents rather than data.

**What the system must do**
- Let a user select a province, then a district, then a sub-district.
- Return risk information at the finest level available for that place.
- **When data below province level does not exist, show the province figure, state plainly that it is a province-level figure, and mark the finer levels as not yet available.** The interface must never return an empty result or imply that no risk exists where data is simply missing.
- Record which places have finer data, so coverage improves visibly as it is added.

**Data spec** DS-01

**Done when**
- [ ] Selecting any of the 77 provinces returns a result.
- [ ] Selecting a district or sub-district without data returns the province figure with a clear label saying so, never a blank result.
- [ ] The label distinguishes "data not yet available" from "no risk identified".
- [ ] Adding finer data for one area does not require a code change.

**Note** The fallback behaviour is the important part of this specification. Without it a developer will build a search that appears broken across most of the country.

---

## 2.1 National climate change situation

The national picture in numbers. Historical extremes, economic losses, and how exposure is changing.

**An existing product could sit here**

- **REQ-013** National exposure trends. The six-sector spatial dataset gives a snapshot of exposure but not a trend over time. Recorded as a gap after the 11 August review. Whether the underlying data can produce a trend is **not assessed**.

**Belongs to the loss and damage work**

- **REQ-012** National macroeconomic loss and damage statistics. What exists in the catalog is records of damaged assets, human impacts and government emergency payments. Those are not macroeconomic loss figures, they are not aggregated, and their own source flags them as needing cleanup. **See Appendix B2. Specification belongs to the loss and damage work package.**

### Ready to build

#### REQ-011 — Historical extreme weather statistics

**Status today** Partial. The underlying measurements exist. The statistics do not.

**Who this is for** Planners and researchers who need to know how often an extreme event has occurred and how severe it was.

**What exists today** Daily and monthly temperature maximum and minimum and rainfall grid data covering 1981 to 2023, national coverage. It is raw grid data, access is restricted, and it is flagged draft and unverified. Nothing has been computed from it.

**What the system must do**
- Derive event statistics from the grids, covering at minimum maximum and minimum temperature and accumulated rainfall.
- Present frequency, intensity and duration for each extreme type, aggregated to a level a planner can use.
- State the period covered and the number of observations behind each figure.
- Handle the restricted access status, either by publishing derived statistics that are releasable or by placing the raw layer behind appropriate control.

**Data spec** DS-02

**Done when**
- [ ] Extreme event statistics are computed from the 1981 to 2023 grids, not asserted from another source.
- [ ] Each statistic shows its period and observation count.
- [ ] Access control matches the restriction on the source data.
- [ ] The method used to define an extreme is documented on the page.

---

## 2.2 Area and sector risk profiles

Risk profiles for all 77 provinces and for the six priority sectors. This section reads from the same underlying data as the area-based search in 1.2, presented as a summary rather than a query.

**An existing product could sit here**

- **REQ-015** Risk profiles for the six priority sectors. The six-sector spatial dataset provides a baseline, but no summarised profile document exists. Sectoral studies and plans such as the health national adaptation plan could support this. Adequacy is **not assessed**.

### Ready to build

#### REQ-014 — Risk and vulnerability profiles by area, 77 provinces and local government

**Status today** Nothing exists in usable form.

**Who this is for** A provincial officer who needs their own province's profile without running an analysis.

**What exists today** No dataset or publication presents risk profiles for all 77 provinces in a summarised, ready-to-use form. Province-level composite index figures exist within the risk data, so this may be a presentation problem rather than a data problem. That cannot be confirmed until the investigation in Appendix B2 is done.

**What the system must do**
- Produce a profile for each of the 77 provinces covering the main hazards, the exposed sectors, and the vulnerability picture.
- Use one consistent structure across all provinces so they can be compared.
- Show local government level where data supports it, and say so plainly where it does not.
- State the source and vintage of every figure, including any draft or unverified flag carried from the source.

**Data spec** DS-01

**Done when**
- [ ] All 77 provinces have a profile with no blanks in the standard structure.
- [ ] Profiles follow one structure and are comparable side by side.
- [ ] Draft or unverified source flags are visible to the reader rather than hidden.
- [ ] Local government coverage is stated explicitly, including where it is absent.

---

## 2.3 Policy, legal and financial tools

The largest section in the first half of the site, covering the climate change act, funding sources, budget tracking and institutional arrangements.

The pattern here is sharp. Everything about what money exists, who is in charge, and how participation is tracked is well covered. Everything adjacent to that, meaning how to justify a budget, how to tag climate spending, and how to track technology and technical assistance, is thin or absent.

**Already covered**

- **REQ-016** Implementation status of the draft climate change act. Covered by an official summary, the draft text and two explainers.
- **REQ-023** DCCE's role as national focal point. Covered by real institutional documents.
- **REQ-024** Structure of the national climate policy committee and its sub-committees. Covered by committee appointment orders.
- **REQ-026** Participation channels and statistics for civil society, private sector and academia. Covered by multi-year disclosure publications and an active tracking system.

**Waiting on a decision** — five requirements, all belonging to the financial and budget evidence service. See Brief E-1 in Appendix B.

### Ready to build

#### REQ-017 — Summary of supporting laws and policy instruments

**Status today** Nothing exists.

**Who this is for** A local government officer who needs to know which legal instruments they can act under.

**What exists today** No DCCE asset summarises the supporting legal framework. The climate change act itself is well covered, but the surrounding instruments, particularly the disaster prevention and mitigation act and town planning regulations, are not.

**What the system must do**
- Summarise each relevant legal and policy instrument that supports adaptation action.
- For each one, state what it enables, who it applies to, and its current status.
- Link to the authoritative text of each instrument.
- Show how each relates to the climate change act, so the reader sees one framework rather than a list.

**Data spec** None needed. This is content.

**Done when**
- [ ] The disaster prevention act and town planning regulations are both covered.
- [ ] Each instrument states what it enables and who it applies to.
- [ ] Each links to its authoritative source text.
- [ ] The relationship to the climate change act is explained.

#### REQ-025 — Coordination between national and local government

**Status today** Nothing exists.

**Who this is for** Officers at both levels who need to know the route between national policy and local action.

**What exists today** DCCE's own role and the national committee structure are documented. The mechanism connecting national bodies to local administrations is not.

**What the system must do**
- Describe the coordination mechanisms between national agencies and local administrative organisations.
- Show the route a local plan takes to reach national attention, and the route a national policy takes to reach local implementation.
- Name the responsible body at each step.
- Identify where coordination currently has no defined mechanism, rather than presenting an incomplete picture as complete.

**Data spec** None needed. This is content.

**Done when**
- [ ] Both directions of coordination are described.
- [ ] A responsible body is named at each step.
- [ ] Gaps in the mechanism are stated rather than glossed.

---

## 2.4 Planning data services

One of the strongest sections on the site. Two of its three requirements are already met.

**Already covered**

- **REQ-029** National data security guidance for research use. Covered by DCCE's data governance manual in both document and media form.

**An existing product could sit here**

- **REQ-028** Integrated spatial risk map. Recorded as fully covered by the existing risk map application and its dataset. This rests on the same product credit found wanting elsewhere, so treat completeness as **unverified** until the Appendix B2 investigation is done.

### Ready to build

#### REQ-027 — Local vulnerability and adaptive capacity indices

**Status today** Partial. The ingredients exist. The index does not.

**Who this is for** Planners who need a single comparable measure of how vulnerable an area is and how well it can cope.

**What exists today** An explainer on how vulnerability and adaptive capacity are measured. No actual index. Underlying proxy indicators exist in quantity, including weather station density, water monitoring station counts and agricultural census vulnerability measures.

**What the system must do**
- Compute vulnerability and adaptive capacity indices from the available proxy indicators.
- Publish the method, including which indicators are used and how they are weighted.
- Produce values at province level for all 77 provinces, and at finer levels where indicators support it.
- **Where an indicator is missing for an area, show the index as incomplete for that area rather than substituting a national average silently.**

**Data spec** DS-03

**Done when**
- [ ] Index values exist for all 77 provinces.
- [ ] The method and indicator list are published alongside the values.
- [ ] Areas with missing indicators are marked incomplete, not filled in silently.
- [ ] The index can be recomputed when new indicators are added.

**Note** This is synthesis from data DCCE already holds, not new collection, which makes it lighter than most items in this section of the document.

---

## 3.1 Climate drivers, observations and future scenarios

The weakest section on the site. Nothing here is fully covered. Six of its eight requirements are ready to build, but several of those depend on getting access to data another agency holds, which is a different kind of task from writing content.

Read the notes on data partnership carefully. Five requirements in this document cannot be completed by DCCE alone, and four of them are here.

**Waiting on a decision** — two requirements belonging to the uncertainty governance service. See Brief E-2 in Appendix B.

### Ready to build

#### REQ-030 — Weather station observation data, short and medium range

**Status today** Nothing exists in DCCE's holdings.

**Who this is for** Researchers and engineers who need point measurements rather than modelled grids.

**What exists today** No DCCE asset holds station-level weather data. The meteorological department holds it.

**What the system must do**
- Establish a route for station observation data from the meteorological department, whether by data sharing agreement or service connection.
- Present station data with location, elevation, variables recorded, and period of record.
- Show which stations are active and which are historical.
- State the update frequency and the delay between observation and publication.

**Data spec** DS-04

**Done when**
- [ ] A formal data route from the meteorological department exists and is documented.
- [ ] Station metadata includes location, variables and period of record.
- [ ] Update frequency and publication delay are stated on the page.

**Note** This requires an agreement with another agency before any build work. Treat the agreement as the first task, not the interface.

#### REQ-031 — Satellite observation data for forest, land cover, water and coral

**Status today** Nothing exists in DCCE's holdings.

**Who this is for** Analysts tracking change in natural systems over time.

**What exists today** No DCCE asset holds satellite observation data. The space technology agency holds relevant products, and marine bodies hold coral observations.

**What the system must do**
- Establish routes to satellite-derived products for forest cover, land cover, water bodies and coral bleaching.
- Present each layer with its resolution, observation date and processing level.
- Allow comparison of the same layer across dates so change is visible.
- State the source agency and licence for each layer.

**Data spec** DS-04

**Done when**
- [ ] All four layers named in the requirement have an established source.
- [ ] Each layer shows resolution, date and processing level.
- [ ] Two dates of the same layer can be compared.

**Note** Also requires agreements with other agencies before build work.

#### REQ-032 — Monitoring of globally significant climate phenomena

**Status today** Partial, and weakly so.

**Who this is for** Planners who need to know whether the coming season is likely to be unusual.

**What exists today** One general-audience article explaining ENSO-neutral conditions. Nothing on the Atlantic overturning circulation at all. There is no monitoring feed, only a one-off explainer.

**What the system must do**
- Present the current state of ENSO and its expected trajectory, refreshed on a stated cycle.
- Explain what the current state means for Thailand in seasonal terms.
- Cover the Atlantic overturning circulation at explanatory level, since no Thai monitoring role exists for it.
- Link each phenomenon to the sectors it most affects.

**Data spec** DS-05

**Done when**
- [ ] ENSO state is shown with a date and a stated refresh cycle, not as static text.
- [ ] The seasonal implication for Thailand is stated in plain language.
- [ ] The overturning circulation is explained even though it is not monitored locally.

#### REQ-033 — Climatology and key climate variables

**Status today** Partial. Multi-decade data exists but nothing has been derived from it.

**Who this is for** Anyone who needs the baseline climate against which change is measured.

**What exists today** National grid data for temperature and rainfall covering 1981 to 2023. Raw grid, restricted access, flagged draft and unverified. No trend statistics have been computed.

**What the system must do**
- Derive climatological baselines and trend statistics for temperature and rainfall from the existing grids.
- Present trends at a level a planner can use, meaning province or region rather than grid cell.
- State the baseline period used and keep it consistent across the site.
- Show the uncertainty around each trend rather than a single number alone.

**Data spec** DS-02

**Done when**
- [ ] Trend statistics are derived from the 1981 to 2023 grids.
- [ ] One baseline period is used consistently across every page that shows a trend.
- [ ] Each trend is presented with its uncertainty.
- [ ] Access control matches the restriction on the source.

**Note** Depends on the same restricted grid data as REQ-011. Resolve access once for both.

#### REQ-035 — Library of high-resolution downscaled future projections

**Status today** Partial. Real projection data exists, but not at the resolution the requirement asks for.

**Who this is for** Engineers and planners designing for conditions decades ahead.

**What exists today** Downscaled projection datasets running to 2099 and 2100, produced both dynamically and statistically, covering national extent. Access is restricted and resolution is national grid rather than the high-resolution sub-national product the requirement describes.

**What the system must do**
- Publish the available projection datasets with their driving model, downscaling method, scenario and period.
- State plainly that resolution is national grid, and what that means for sub-national use.
- Allow selection by scenario and period.
- Record what higher-resolution product would be needed to meet the requirement fully, so the gap is visible rather than implied.

**Data spec** DS-06

**Done when**
- [ ] Every published dataset shows model, method, scenario and period.
- [ ] The resolution limitation is stated on the page, not buried in metadata.
- [ ] A user can select by scenario and period.
- [ ] The remaining gap to true high-resolution projections is documented.

**Note** Whether the existing national-resolution data is sufficient is a judgement for DCCE, not one this document makes.

#### REQ-037 — Case studies applying climate projections to long-term planning

**Status today** Nothing exists.

**Who this is for** Planners who understand that projections exist but not how to use them in a real decision.

**What exists today** No DCCE asset shows a projection being applied to a planning decision.

**What the system must do**
- Present worked examples in which climate projection data informed a long-term plan or investment.
- For each, show the decision, the data used, how uncertainty was handled, and the outcome or current status.
- Cover more than one sector.
- Link each case to the projection datasets it used.

**Data spec** None needed. This is content built on existing datasets.

**Done when**
- [ ] At least two case studies covering different sectors are published.
- [ ] Each shows the decision, the data, and the treatment of uncertainty.
- [ ] Each links to the underlying projection dataset.

---

## 3.2 Risk, vulnerability, impact chains, and loss and damage

The analytical core of the site, and the section where the most work sits. Fourteen requirements, of which eight are ready to build and three belong to the loss and damage work.

One strength runs through this section. DCCE's impact chain manual is a real, purpose-built document. It is also being asked to stand in for several things it was not written to be, which is why some requirements below are partial rather than covered.

**Already covered**

- **REQ-046** Multi-hazard impact chain diagram. Covered by the impact chain manual.

**An existing product could sit here**

- **REQ-041** Sector risk results for food security, water, health and business disruption. The six-sector dataset provides results for food, water and settlement. Heat and health impact and business disruption are not represented. Adequacy of the rest is **not assessed**.

**Belongs to the loss and damage work**

- **REQ-049** Dashboard of historical economic and physical losses. Real machine-readable damage records exist for several hazards but are not dashboard-ready. **See Appendix B2.**
- **REQ-050** Record of non-economic losses covering mental health, biodiversity and cultural heritage. Only biodiversity has material. **See Appendix B2.**
- **REQ-051** Standard national manual for risk, impact and loss calculation. The impact chain manual is the closest proxy and was not written for this. **See Appendix B2.**

**Waiting on a decision** — one requirement, the sector damage function library. See Brief E-1 in Appendix B.

### Ready to build

#### REQ-038 — Definitions of exposure, sensitivity, adaptive capacity and resilience

**Status today** Partial. Two of the four concepts are covered directly, two only by implication.

**Who this is for** Every reader of the analytical sections, who needs these terms to mean the same thing throughout the site.

**What exists today** A dataset defining adaptation and vulnerability concepts in IPCC terms, and an article on measuring vulnerability and adaptive capacity. Sensitivity and resilience are implicit rather than stated.

**What the system must do**
- Define all four concepts explicitly, in Thai and English, following IPCC usage.
- Show how the concepts relate to each other and to the risk framework used elsewhere on the site.
- Give a Thai example for each.
- Serve as the single definition source that other pages link to, so the terms cannot drift.

**Data spec** None needed. This is content.

**Done when**
- [ ] All four concepts are defined explicitly, not implied.
- [ ] Definitions follow IPCC usage and say so.
- [ ] Other analytical pages link here rather than redefining terms locally.

#### REQ-040 — A single national risk assessment methodology

**Status today** Partial. A proxy exists.

**Who this is for** Any agency conducting a risk assessment that should be comparable with others.

**What exists today** DCCE's impact chain manual, which is the closest existing methodology document. No purpose-built national risk assessment standard exists.

**What the system must do**
- Set out the national methodology for risk assessment, covering the steps, the required inputs and the expected outputs.
- State how it relates to the impact chain method, whether as an extension or a distinct procedure.
- Define what makes an assessment compliant, so results from different agencies can be compared.
- Provide a template or worked example.

**Data spec** None needed. This is methodology content.

**Done when**
- [ ] The methodology is published as its own document, not as a reading of the impact chain manual.
- [ ] Its relationship to the impact chain method is stated explicitly.
- [ ] Compliance criteria are defined.
- [ ] A template or worked example is included.

#### REQ-042 — Statistics and assessment of slow-onset hazards

**Status today** Nothing exists as a consolidated report.

**Who this is for** Long-term planners, for whom gradual change matters more than individual events.

**What exists today** No consolidated slow-onset assessment. Individual components exist separately, including sea level data covered under REQ-043 and erosion data under REQ-045.

**What the system must do**
- Consolidate slow-onset hazard tracking covering rising average temperature and shifting rainfall distribution.
- Present rate of change with its uncertainty, not just current state.
- Distinguish observed change from projected change.
- Link to the individual hazard datasets rather than duplicating them.

**Data spec** DS-02

**Done when**
- [ ] Temperature and rainfall distribution change are both covered with rates and uncertainty.
- [ ] Observed and projected change are visually and textually distinct.
- [ ] The page links to source datasets instead of restating their figures.

#### REQ-043 — Sea level rise along the Thai coast and the Gulf

**Status today** Partial. Observations exist. A derived rate does not.

**Who this is for** Coastal planners and infrastructure engineers.

**What exists today** An annual sea level observation dataset from the marine department hydrology group, national coverage through 2026, tagged to sea level rise. These are raw annual readings, restricted access, and no rate of rise has been derived.

**What the system must do**
- Derive rate of sea level rise from the annual observations, with uncertainty.
- Present rates by coastal segment rather than one national figure, since the Gulf and Andaman differ.
- Show the observation record alongside the derived rate.
- State the period of record and any gaps in it.

**Data spec** DS-07

**Done when**
- [ ] A rate of rise with uncertainty is derived from the observations.
- [ ] Rates are presented by coastal segment.
- [ ] The observation record and its gaps are visible.
- [ ] Access control matches the source restriction.

#### REQ-044 — Land subsidence and salinity intrusion

**Status today** Nothing exists.

**Who this is for** Bangkok and central region planners, for whom subsidence compounds flood and sea level risk.

**What exists today** No DCCE asset covers either subsidence or salinity intrusion. Neither appeared in the document inventory or the dataset catalog.

**What the system must do**
- Establish sources for land subsidence measurement in Bangkok and the surrounding provinces.
- Establish sources for salinity intrusion in the affected river systems.
- Present both with location, rate and period.
- Show how subsidence interacts with sea level rise and flooding, since the combined effect is the planning concern.

**Data spec** DS-04

**Done when**
- [ ] A source is established for each of subsidence and salinity intrusion.
- [ ] Both are presented with location, rate and period.
- [ ] The interaction with sea level rise and flooding is explained.

**Note** Requires agreements with other bodies. This is foundational data that a build team cannot substitute from DCCE material.

#### REQ-045 — Coastal erosion index and beach area loss

**Status today** Partial. Quantitative data exists but is not built into an index.

**Who this is for** Coastal province planners and marine resource managers.

**What exists today** Real area-based erosion extent data from marine resource bodies, alongside a series of nine coastal adaptation infographics. The data is raw area figures rather than a computed index.

**What the system must do**
- Compute an erosion index from the existing extent data, covering the affected coastline.
- Present beach area lost over time by coastal segment.
- Publish the index method alongside the values.
- Link to the existing coastal adaptation material rather than duplicating it.

**Data spec** DS-07

**Done when**
- [ ] An erosion index is computed and published with its method.
- [ ] Area loss over time is shown by coastal segment.
- [ ] Existing coastal adaptation content is linked rather than rewritten.

#### REQ-047 — Impact chain case studies for agriculture and urban settlement

**Status today** Partial. One of the two sectors is covered.

**Who this is for** Analysts learning to apply the impact chain method to their own sector.

**What exists today** An in-depth case study of the 2025 Hat Yai flood using impact chain analysis, which covers the urban case well. Nothing for agriculture.

**What the system must do**
- Produce an agriculture sector impact chain case study to the same depth as the existing urban one.
- Follow the structure of the impact chain manual so the two are comparable.
- Show the full chain from hazard through to consequence, including where the chain was uncertain.
- Present both case studies together as a pair.

**Data spec** None needed. This is analytical content.

**Done when**
- [ ] An agriculture case study exists at comparable depth to the Hat Yai study.
- [ ] Both follow the impact chain manual structure.
- [ ] Points of uncertainty in each chain are stated.

#### REQ-048 — Loss and damage framework under the UNFCCC

**Status today** Partial. The closest asset is about funding rather than framework.

**Who this is for** Readers who need to understand what loss and damage means as a concept before reading the statistics.

**What exists today** A publication on the loss and damage response fund, grounded in the UNFCCC framework but written as a funding mechanism page rather than a framework explainer.

**What the system must do**
- Explain the loss and damage concept as defined under the UNFCCC, including the distinction between economic and non-economic loss.
- Explain how loss and damage relates to adaptation and to mitigation.
- Set out Thailand's position and obligations.
- Link to the funding page as one application of the framework, not as the framework itself.

**Data spec** None needed. This is content.

**Done when**
- [ ] The concept is explained independently of the funding mechanism.
- [ ] Economic and non-economic loss are distinguished.
- [ ] Thailand's position and obligations are stated.
- [ ] The framework page and the funding page are clearly distinct.

---

## 3.3 Adaptation planning and measures library

The largest section on the site by requirement count, and the weakest by coverage. Where section 3.2 is about understanding risk, this section is about acting on it, and DCCE's holdings lean heavily towards the former.

Six requirements are ready to build and six are waiting on a decision, which makes this the most evenly split section in the document.

**Already covered**

- **REQ-056** National adaptation strategy roadmap and staging diagram. Covered directly by the national adaptation plan and its dataset entry.

**Waiting on a decision** — six requirements. Four belong to the financial and budget evidence service and two to institutional tracking. See Briefs E-1 and E-3 in Appendix B.

### Ready to build

#### REQ-053 — Gender equality and social inclusion guidance

**Status today** Nothing exists.

**Who this is for** Anyone designing an adaptation measure who must show it reaches people equitably.

**What exists today** No DCCE asset addresses gender equality or social inclusion in adaptation.

**What the system must do**
- Provide guidance on integrating gender, equality and human rights considerations into adaptation measures.
- Give practical steps at each stage of designing a measure, not principles alone.
- Include Thai examples where a measure succeeded or failed on inclusion grounds.
- Connect to the vulnerable groups material in REQ-054 so the two work together.

**Data spec** None needed. This is guidance content.

**Done when**
- [ ] Guidance covers gender, equality and human rights.
- [ ] Practical steps are given for each design stage.
- [ ] At least one Thai example is included.
- [ ] The guidance links to the vulnerable groups material.

#### REQ-054 — Protection measures for named vulnerable groups

**Status today** Partial, and only topically.

**Who this is for** Local officers responsible for specific groups during a hazard event.

**What exists today** One article on protecting vulnerable groups during extreme heat. None of the four groups named in the requirement, meaning children, elderly people, disabled people and border or coastal communities, has dedicated coverage.

**What the system must do**
- Cover protection and assistance measures for each of the four named groups separately.
- For each group, state the specific risks they face and the measures that address them.
- Cover more than heat, extending to flood, drought and storm.
- Name the responsible body for each measure.

**Data spec** None needed. This is content.

**Done when**
- [ ] All four named groups have dedicated coverage.
- [ ] Each group's specific risks and matching measures are stated.
- [ ] Coverage extends beyond heat to other major hazards.
- [ ] A responsible body is named for each measure.

#### REQ-055 — Local wisdom, traditional knowledge and cultural heritage in adaptation

**Status today** Nothing exists.

**Who this is for** Community-level practitioners and the officers supporting them.

**What exists today** No DCCE asset addresses this.

**What the system must do**
- Present how local wisdom and traditional knowledge can be applied in community adaptation.
- Give documented Thai examples with the community and region named.
- Explain how traditional practice can be combined with technical measures rather than presented as an alternative to them.
- Address cultural heritage as something at risk as well as a resource for adaptation.

**Data spec** None needed. This is content.

**Done when**
- [ ] Documented Thai examples are given with community and region named.
- [ ] The combination of traditional and technical approaches is addressed.
- [ ] Cultural heritage appears both as a resource and as something at risk.

#### REQ-057 — Report on systemic barriers by sector

**Status today** Nothing exists.

**Who this is for** Policy makers deciding where to intervene, who need to know why adaptation stalls.

**What exists today** No DCCE asset reports on systemic barriers.

**What the system must do**
- Identify barriers by sector across at minimum data limitations, institutional coordination problems and financial constraints.
- Distinguish barriers that DCCE can address from those requiring action elsewhere.
- Draw on documented experience rather than assertion, naming the source of each barrier identified.
- Connect each barrier to the part of the site that addresses it, where one exists.

**Data spec** None needed. This is analytical content.

**Done when**
- [ ] Barriers are identified per sector across all three named categories.
- [ ] Each barrier states its evidence source.
- [ ] Barriers within DCCE's control are distinguished from those outside it.

#### REQ-060 — Searchable database of technical and policy measures

**Status today** Nothing exists.

**Who this is for** A planner looking for measures that fit their hazard, sector and budget.

**What exists today** No searchable measures database. Individual measures are described across scattered publications.

**What the system must do**
- Provide a searchable and filterable collection of adaptation measures.
- Support filtering by hazard, by sector and by budget range, as the requirement specifies.
- Record for each measure what it does, where it has been used, and what it costs.
- **Where cost information is unavailable, show the measure with cost marked unknown rather than excluding it from budget-filtered results without explanation.**
- Allow new measures to be added without a code change.

**Data spec** DS-09

**Done when**
- [ ] Measures can be filtered by hazard, sector and budget together.
- [ ] Each entry records function, prior use and cost.
- [ ] Measures with unknown cost remain findable and are marked as such.
- [ ] Adding a measure requires no code change.

#### REQ-061 — Combined list of grey infrastructure and nature-based measures

**Status today** Partial. One half is well covered, the other not at all.

**Who this is for** Planners comparing structural and natural approaches for the same problem.

**What exists today** Three assets covering nature-based solutions in depth, including a guidance dataset, an explainer and a video. Grey and structural infrastructure measures have nothing.

**What the system must do**
- Cover grey and structural infrastructure measures to the same depth as the existing nature-based material.
- Present both types together so they can be compared for the same hazard and setting.
- State the conditions under which each type is appropriate.
- Cover combined approaches, since these are frequently the practical answer.

**Data spec** DS-09

**Done when**
- [ ] Grey infrastructure measures are covered at comparable depth to nature-based ones.
- [ ] Both types are presented together and comparably for the same hazard.
- [ ] Conditions favouring each type are stated.
- [ ] Combined approaches are covered.

---

## 3.4 Monitoring and evaluation of adaptation

Fully covered, by two different routes worth keeping distinct.

**Already covered**

- **REQ-065** Technology readiness framework for adaptation technology. Recorded as covered because it falls within DCCE's active monitoring platform rather than because a specific document was matched. **A build team should confirm this content exists before treating it as done.**
- **REQ-066** Link to the global goal on adaptation indicators. Verified match.
- **REQ-067** National tracker for adaptation progress by sector and province. Verified against DCCE's live catalog, maintained by the adaptation monitoring group and tied to Thailand's transparency reporting.
- **REQ-068** Library of successful project case studies. Unusually well covered, with eight assets across multiple sectors.

---

## 4.1 Data catalog

The cleanest section on the site. Infrastructure that already exists and needs linking rather than building.

**Already covered**

- **REQ-069** Searchable system for datasets, data products and metadata meeting national security standards. DCCE already operates the catalog, has a publication describing it, and has a governance manual covering metadata and security.

---

## 4.2 Visualisation and analytics application

One requirement, and it needs care. The page-level picture looks better than the detail warrants.

**An existing product could sit here**

- **REQ-070** Interactive application showing hazard maps and supporting risk analysis, specifically so an engineer can obtain rainfall intensity and temperature design values at plot level. DCCE's existing risk map application is a real working tool and could appear here. Its adequacy is **not assessed**.

**The important part of this requirement is not covered at all.** A search across both the document inventory and the dataset catalog for intensity-duration-frequency curves or engineering design curves returned nothing of any kind. That is the specific reason this page exists as its own section rather than repeating the general risk map elsewhere on the site.

Producing those curves means computing rainfall intensity-duration-frequency statistics that do not exist in DCCE's holdings in any form. Anyone reading the page-level status as "an application already exists, so this is nearly done" will underestimate this page severely. The engineering design variables work is described in Brief E-4 in Appendix B.

---

## 4.3 External tools and data hub

One requirement, entirely uncovered, and a different kind of work from the rest of the site.

### Ready to build

#### REQ-071 — Connections to international and specialist data portals

**Status today** Nothing exists.

**Who this is for** Researchers and analysts who need data DCCE does not hold and currently go looking for it themselves.

**What exists today** No DCCE asset provides these connections. This is integration work rather than content production, so no content gap analysis applies.

**What the system must do**
- Provide connection points to the external portals named in the requirement, meaning the meteorological department weather service, the space technology agency geo-informatics portal, and the Copernicus climate data store.
- For each, state what data it holds, what access conditions apply, and how it relates to data on this site.
- Where a service connection is possible, connect to it rather than linking to a home page.
- **Show the status of each connection, so a reader can tell a working connection from a broken one.**
- Record the agreement or licence under which each connection operates.

**Data spec** DS-10

**Done when**
- [ ] All three named portals have a connection point.
- [ ] Each states its holdings, access conditions and relationship to local data.
- [ ] Connection status is visible to the reader.
- [ ] The governing agreement or licence is recorded for each.

**Note** This is technical partnership work and should be scoped and budgeted separately from content production.

---

## 5.1 Announcements and engagement activities

**Already covered**

- **REQ-072** System for distributing data update announcements and training activities. Covered by DCCE's existing seminar and training system and its public relations channel. A linking task rather than a build.

---

## 5.2 Feedback channels and user services

One requirement, entirely uncovered, and a genuinely new capability for DCCE.

### Ready to build

#### REQ-073 — Feedback platform for user agencies

**Status today** Nothing exists in any form.

**Who this is for** Agencies using the platform's data who currently have no route to report a problem or request a change.

**What exists today** No structured feedback or service quality mechanism exists at DCCE today.

**What the system must do**
- Provide a structured route for user agencies to submit feedback on data quality, request scope extensions, and confirm whether their needs are being met.
- Record who submitted each item, what it concerns, and which dataset or page it relates to.
- Track each item through to a stated outcome, so a submitter can see what happened.
- Report on feedback in aggregate, so recurring problems become visible rather than being handled one at a time.
- Route items to a responsible owner rather than a shared inbox.

**Data spec** DS-11

**Done when**
- [ ] An agency can submit feedback tied to a specific dataset or page.
- [ ] Each item has a named owner and a visible status.
- [ ] A submitter can see the outcome of their own submission.
- [ ] Aggregate reporting shows recurring issues across submissions.

**Note** This pairs naturally with REQ-071. Both build new operational capability rather than filling a content gap, and both sit outside the content production work that covers most of this document.

---

# Appendix A — What actually has to be built

The thirty ready-to-build requirements are not thirty separate pieces of work. Several pages draw on the same underlying effort, so building once serves several requirements.

This appendix groups them into eleven deliverables. **This is the planning view. Anyone scheduling the build should work from this table rather than counting requirement cards.**

| | Deliverable | Type | Serves | Requirements |
|---|---|---|---|---|
| **DEL-1** | Climate grid processing | Data engineering | 2.1, 3.1, 3.2 | REQ-011, REQ-033, REQ-042 |
| **DEL-2** | Provincial risk profile layer | Data engineering and interface | 1.2, 2.2, 2.4 | REQ-008, REQ-014, REQ-027 |
| **DEL-3** | Line agency data agreements | Partnership | 3.1, 3.2 | REQ-030, REQ-031, REQ-044 |
| **DEL-4** | Coastal and marine data derivation | Data engineering | 3.2 | REQ-043, REQ-045 |
| **DEL-5** | Projection and monitoring publication | Data publication | 3.1 | REQ-032, REQ-035 |
| **DEL-6** | Concept and methodology standards | Content | 3.2 | REQ-038, REQ-040, REQ-048 |
| **DEL-7** | Risk framing and worked examples | Content | 1.1, 3.1, 3.2 | REQ-001, REQ-003, REQ-037, REQ-047 |
| **DEL-8** | Policy and institutional content | Content | 2.3, 3.3 | REQ-017, REQ-025, REQ-057 |
| **DEL-9** | Inclusion and community adaptation content | Content | 3.3 | REQ-053, REQ-054, REQ-055 |
| **DEL-10** | Adaptation measures library | Product and content | 3.3 | REQ-060, REQ-061 |
| **DEL-11** | New operational capabilities | Build | 4.3, 5.2 | REQ-071, REQ-073 |

Three observations for whoever plans this work.

**DEL-3 has to start first.** Data agreements with other agencies take longer than anything else here and nothing downstream can proceed without them. It is also the only deliverable DCCE cannot complete alone.

**DEL-1 and DEL-4 share a constraint.** Both derive statistics from restricted-access source data. Resolve the access question once, for both, rather than twice.

**Six of the eleven are content production.** DEL-6 through DEL-10 and part of DEL-7 need writers and subject specialists rather than engineers. That is a different procurement from the rest of this document and is easy to overlook when reading a specification framed around a website build.

---

# Appendix B — Services awaiting a decision

Fourteen requirements belong to services DCCE has not yet decided to build. Writing full specifications for them would imply a commitment that has not been made, so they are summarised here instead.

**If DCCE selects any of these, proper requirement gathering is needed before building.** These briefs establish scale and blockers. They are not specifications.

## Brief E-1 — Financial and budget evidence

**Requirements** 10 · **Sections affected** 2.3, 3.3, 3.2

REQ-018, REQ-019, REQ-020, REQ-021, REQ-022, REQ-039, REQ-052, REQ-058, REQ-059, REQ-064

**What this service would do.** Give agencies the evidence to justify adaptation spending, particularly where a climate-resilient design costs more than the historical benchmark for comparable work. It covers avoided losses calculation, cost-benefit analysis, budget tagging, and tracking of support received.

**Demand.** The strongest single cluster in this document. Ten of the fourteen waiting requirements sit here, and the demand analysis records it as a repeated concern from agencies facing budget scrutiny.

**What exists.** The funding side is genuinely well covered. DCCE's funding guide and dedicated publications for the major international climate funds are real and operational.

**Core blocker.** Everything beyond listing funding sources is absent. There is no cost-benefit methodology, no budget tagging statistics, no avoided-losses calculation standard, and no damage function library to compute avoided losses from. This is a methodology development problem before it is a platform problem.

**Readiness.** Ready for joint development. Strong demand, but the valuation method and data linking rules have to be built first.

**A recurring pattern worth noting.** Every requirement here that asks about technology transfer or capacity building support returns assets that track money only. This appears in both section 2.3 and section 3.3, and it is one absence rather than two.

## Brief E-2 — Uncertainty governance

**Requirements** 2 · **Sections affected** 3.1

REQ-034, REQ-036

**What this service would do.** Give agencies a standard way to handle and communicate uncertainty in climate data, so that uncertainty becomes a basis for careful decisions rather than a reason to avoid them. It would assess the readiness and appropriate use of each data product.

**Demand.** Raised specifically by financial sector and infrastructure planning bodies, who must communicate risk without overstating confidence.

**What exists.** Nothing. Neither a scenario usage guide nor an uncertainty management standard exists.

**Core blocker.** This requires methodology development and institutional agreement rather than data or software. It also cuts across everything else, since each dataset on the site would need a readiness assessment.

**Readiness.** A foundation that touches everything else. The demand analysis suggests building it into each service rather than standing it up as a product on its own.

## Brief E-3 — Institutional and project tracking

**Requirements** 2 · **Sections affected** 3.3

REQ-062, REQ-063

**What this service would do.** Track the status of national adaptation projects and hold a repository of local and private sector risk management plans.

**Demand.** Moderate. Policy makers and funding bodies need it to see progress and avoid duplicated spending.

**What exists.** Nothing. Neither a project tracking system nor a plans repository exists.

**Core blocker.** The information is held by DCCE programme staff and by external organisations. It is not findable through any inventory search, so this depends on establishing internal reporting routines rather than on locating existing material.

**Readiness.** Dependent on foundations. It requires indicators and reporting routines to exist before a system can hold them.

## Brief E-4 — Engineering design variables

**Requirements** 0 in this category, but see below · **Sections affected** 4.2

**What this service would do.** Convert climate projections into the design values engineers use, meaning rainfall intensity-duration-frequency curves, peak flow figures and temperature extremes at usable resolution.

**Why it appears here despite having no requirement of its own.** Section 4.2 holds a single requirement, REQ-070, which is recorded as an existing product surface because DCCE's risk map application could appear there. The substantive gap, the intensity-duration-frequency curves, sits inside that requirement rather than beside it.

**What exists.** Nothing for the engineering half. A search across both the document inventory and the dataset catalog returned no material of any kind on design curves.

**Core blocker.** Producing these curves means computing rainfall intensity-duration-frequency statistics that do not exist in DCCE's holdings at any resolution. This is closer in effort to the confirmed gaps in section 3.2 than to anything else in section 4.

**Readiness.** Ready for joint development, but requires engineering standards bodies and specialist validation.

**A warning for planners.** Because REQ-070 reads as partially covered at page level, this work is easy to miss entirely. It should be scoped explicitly rather than assumed to fall out of the visualisation build.

---

# Appendix B2 — Data specifications, and one thing to do first

## Read this before starting the build

**Recommendation. Before building anything, establish what data actually sits behind DCCE's three existing analytical products, bring it into the platform, and then reassess the gaps in this document.**

The three products are the spatial risk database, the hazard and exposure map, and the climate risk index. Nine requirements in this document touch pages where one of them could appear, and for all nine this document declines to say whether the requirement is met.

That is not caution for its own sake. The composite risk index combines its inputs by multiplying and normalising them, and that operation cannot be reversed. The published index therefore cannot be traced back to the line agency data that produced it. Knowing the index exists tells you nothing about whether the underlying data supports a district-level search, a sector profile, or an exposure trend.

The stricter review of 11 August 2026 found three requirements recorded as complete on precisely this reasoning, and moved all three back to gap or partial. Two further requirements, REQ-005 and REQ-028, still rest on the same reasoning and are flagged in the body above.

**The specific work.**

1. Inventory what feeds each of the three products. Not the published output, but the inputs, their sources, their granularity, their refresh cycle and their owners.
2. Bring those datasets into the platform's data layer, so they can be queried directly rather than only through the product that presents them.
3. Reassess the nine flagged requirements, and the two flagged as covered, against what the inventory reveals.

**What this will change.** Some recorded gaps will close, because the data turns out to exist. Some items recorded as covered will reopen. Either way the picture becomes real, and the schedule built on it becomes trustworthy. Doing this at the start costs weeks. Discovering it midway through the build costs more.

## Data specifications

Each specification covers one dataset or group, and is referenced from the requirement cards above. Fields are taken from DCCE's data catalog. **Where a field is not recorded there, it is marked unknown rather than estimated.**

Two observations apply to every sheet below. Every DCCE dataset examined carries the status `Baseline-Draft` and the flag `Unverified-Baseline`. And no dataset in the catalog records a maintainer. Both need resolving before any of this data is published as authoritative.

### DS-01 — Provincial composite risk data
**Serves** REQ-008, REQ-014 · **Source** `DCCE_3_1` to `DCCE_3_6`, six sector datasets
**Granularity** Province · **Coverage** National, 1960 to 2100 · **Frequency** Annual
**Format** CSV · **Access** Public · **Status** Baseline-Draft, Unverified-Baseline
**Limitations** Scenarios limited to two pathways. Composite method is not reversible to inputs.
**Maintainer** UNKNOWN — pending investigation
**Note** Whether this supports anything below province level is **unassessed**. This is the central question for the investigation above.

### DS-02 — Historical climate grids
**Serves** REQ-011, REQ-033, REQ-042 · **Source** `DCCE_2_1` rainfall, `DCCE_2_2` maximum temperature
**Granularity** Grid · **Coverage** National, 1981 to 2023 · **Frequency** Daily and monthly
**Format** Raster · **Access** **Restricted** · **Status** Baseline-Draft, Unverified-Baseline
**Limitations** Raw grids only. No derived statistics exist. Access restriction must be resolved before publication.
**Maintainer** UNKNOWN — pending investigation

### DS-03 — Vulnerability and adaptive capacity indicators
**Serves** REQ-027 · **Source** Proxy indicators across several catalog entries, including monitoring station density and agricultural census measures
**Granularity** Mixed, mostly province · **Coverage** UNKNOWN, varies by indicator
**Access** Mixed · **Status** Baseline-Draft
**Limitations** No composite index exists. Indicator coverage varies by area, so completeness must be shown per area.
**Maintainer** UNKNOWN — pending investigation

### DS-04 — Observation data held by other agencies
**Serves** REQ-030, REQ-031, REQ-044 · **Source** External. Meteorological department, space technology agency, marine and groundwater bodies
**Granularity** UNKNOWN · **Coverage** UNKNOWN · **Frequency** UNKNOWN
**Access** **Not currently available to DCCE**
**Limitations** None of this data is in DCCE's catalog. Every field is unknown until an agreement exists.
**Note** This specification cannot be completed by DCCE alone. Treat the data agreement as the first deliverable.

### DS-05 — Climate phenomena monitoring
**Serves** REQ-032 · **Source** No dataset. One general-audience article only
**Granularity** Not applicable · **Coverage** None
**Limitations** No monitoring feed exists. A source must be established, most likely external.
**Maintainer** Not applicable

### DS-06 — Downscaled climate projections
**Serves** REQ-035 · **Source** `DCCE_2_11` dynamical, `DCCE_2_16` to `DCCE_2_19` statistical
**Granularity** Grid, national · **Coverage** 1960 to 2099 dynamical, 1981 to 2100 statistical · **Frequency** Daily and monthly
**Format** Raster · **Access** **Restricted** · **Status** Baseline-Draft, Unverified-Baseline
**Limitations** National grid resolution, not the high-resolution sub-national product the requirement describes. State this on the page.
**Maintainer** UNKNOWN — pending investigation

### DS-07 — Coastal and marine observations
**Serves** REQ-043, REQ-045 · **Source** `MD_1_2` sea level from the marine department hydrology group, `DMCR_1_1` and `DMCR_4_1` coastal erosion
**Granularity** **UNKNOWN — not recorded in the catalog** · **Coverage** Sea level through 2026, erosion through 2025 · **Frequency** Annual
**Format** Vector and CSV · **Access** **Restricted**, and unrecorded for `DMCR_4_1` · **Status** Baseline-Draft, Unverified-Baseline
**Limitations** Raw observations only. Neither a rate of rise nor an erosion index has been derived. Spatial resolution is unrecorded, which must be resolved before use.
**Maintainer** UNKNOWN — pending investigation

### DS-08 — Historical disaster record
**Serves** REQ-001 · **Source** None in DCCE's holdings. Records exist across other government bodies
**Granularity** UNKNOWN · **Coverage** None currently
**Limitations** Compilation task. Sources exist but are scattered and have not been gathered.

### DS-09 — Adaptation measures library
**Serves** REQ-060, REQ-061 · **Source** New. To be compiled from existing publications and new content
**Granularity** Per measure · **Coverage** To be established
**Limitations** Cost information will be incomplete. The design must keep measures findable when cost is unknown.

### DS-10 — External portal connections
**Serves** REQ-071 · **Source** External. Meteorological service, geo-informatics portal, Copernicus climate data store
**Access** Governed by each provider's terms · **Status** No connection exists
**Limitations** Each connection needs its own agreement and licence record. Availability is outside DCCE's control, so connection status must be visible to users.

### DS-11 — Feedback records
**Serves** REQ-073 · **Source** New. Generated by the platform itself
**Granularity** Per submission · **Coverage** From launch
**Limitations** Contains identifiable submitter information, so retention and access rules are needed before launch.

---
# Appendix C — Traceability matrix

Every requirement, where it sits on the site, how it is handled, and where the work goes. Status reflects the corrected assessment of 11 August 2026.

Also published as `2026-08-12-WP4-DRD-requirements.csv`, which carries the Thai requirement text and the match reasoning as well.

| ID | Section | Requirement | Status | Handling | Goes to | Source assets |
|---|---|---|---|---|---|---|
| REQ-001 | 1.1 | History and trends of natural disasters | Gap | Ready to build | DEL-7 | — |
| REQ-002 | 1.1 | IPCC risk framework and definitions | Full | Already covered | — | PUB-012, DAT-014 |
| REQ-003 | 1.1 | Physical risk and transition risk | Gap | Ready to build | DEL-7 | — |
| REQ-004 | 1.1 | National risk summary cards | Partial | Product surface | Investigation, App. B2 | DCCE_3_1, DCCE_3_2, DCCE_3_3, DCCE_3_4, DCCE_3_5, DCCE_3_6, DCCE_3_7 |
| REQ-005 | 1.1 | Critical hotspots by sector and region | Full | Product surface | Investigation, App. B2 | DAT-005 |
| REQ-006 | 1.1 | National adaptation plan summary | Full | Already covered | — | PUB-009, DAT-021, MED-025, MED-111, MED-112 |
| REQ-007 | 1.1 | Examples of high-value adaptation measures | Full | Already covered | — | MED-008, DAT-022 |
| REQ-008 | 1.2 | Search by administrative level | Gap | Ready to build | DEL-2 | — |
| REQ-009 | 1.2 | Map integration with administrative boundaries | Gap | Product surface | Investigation, App. B2 | SYS-003, DAT-005 |
| REQ-010 | 1.2 | Quick-view point dashboard | Partial | Product surface | Investigation, App. B2 | SYS-003 |
| REQ-011 | 2.1 | Historical extreme weather statistics | Partial | Ready to build | DEL-1 | DCCE_2_1, DCCE_2_2 |
| REQ-012 | 2.1 | National macroeconomic loss and damage statistics | Partial | Loss and damage | Loss and damage work | PUB-026, MED-050 |
| REQ-013 | 2.1 | National exposure trends | Gap | Product surface | Investigation, App. B2 | DAT-005 |
| REQ-014 | 2.2 | Risk profiles for 77 provinces and local government | Gap | Ready to build | DEL-2 | — |
| REQ-015 | 2.2 | Risk profiles for the six priority sectors | Partial | Product surface | Investigation, App. B2 | DAT-005, DAT-014 |
| REQ-016 | 2.3 | Status of the climate change act | Full | Already covered | — | PUB-003, PUB-004, MED-074, MED-075 |
| REQ-017 | 2.3 | Summary of supporting laws and policy instruments | Gap | Ready to build | DEL-8 | — |
| REQ-018 | 2.3 | Avoided losses certification system | Gap | Awaiting decision | Brief E-1 | — |
| REQ-019 | 2.3 | Funding directory and cost-benefit guidance | Partial | Awaiting decision | Brief E-1 | MED-079, PUB-027, PUB-028, PUB-029 |
| REQ-020 | 2.3 | Budget allocation statistics and climate budget tagging | Gap | Awaiting decision | Brief E-1 | — |
| REQ-021 | 2.3 | Tracking of financial, technology and technical assistance | Partial | Awaiting decision | Brief E-1 | PUB-027, PUB-028, PUB-029, DAT-054, MED-147 |
| REQ-022 | 2.3 | Private sector finance mobilisation | Gap | Awaiting decision | Brief E-1 | — |
| REQ-023 | 2.3 | DCCE role as national focal point | Full | Already covered | — | PUB-025 |
| REQ-024 | 2.3 | National climate policy committee structure | Full | Already covered | — | DAT-013 |
| REQ-025 | 2.3 | National to local government coordination | Gap | Ready to build | DEL-8 | — |
| REQ-026 | 2.3 | Participation channels and statistics | Full | Already covered | — | SYS-024, PUB-053, PUB-054, PUB-055 |
| REQ-027 | 2.4 | Local vulnerability and adaptive capacity indices | Partial | Ready to build | DEL-2 | MED-015 |
| REQ-028 | 2.4 | Integrated spatial risk map | Full | Product surface | Investigation, App. B2 | SYS-003, DAT-005 |
| REQ-029 | 2.4 | National data security guidance | Full | Already covered | — | PUB-052, MED-026 |
| REQ-030 | 3.1 | Weather station observation data | Gap | Ready to build | DEL-3 | — |
| REQ-031 | 3.1 | Satellite observation data | Gap | Ready to build | DEL-3 | — |
| REQ-032 | 3.1 | Monitoring of global climate phenomena | Partial | Ready to build | DEL-5 | MED-105 |
| REQ-033 | 3.1 | Climatology and key climate variables | Partial | Ready to build | DEL-1 | DCCE_2_1, DCCE_2_2 |
| REQ-034 | 3.1 | Climate scenario usage guide | Gap | Awaiting decision | Brief E-2 | — |
| REQ-035 | 3.1 | Downscaled future projection library | Partial | Ready to build | DEL-5 | DCCE_2_11, DCCE_2_16, DCCE_2_17, DCCE_2_18, DCCE_2_19 |
| REQ-036 | 3.1 | National uncertainty management standard | Gap | Awaiting decision | Brief E-2 | — |
| REQ-037 | 3.1 | Case studies applying projections to planning | Gap | Ready to build | DEL-7 | — |
| REQ-038 | 3.2 | Definitions of core vulnerability concepts | Partial | Ready to build | DEL-6 | DAT-014, MED-015 |
| REQ-039 | 3.2 | Sector damage function library | Gap | Awaiting decision | Brief E-1 | — |
| REQ-040 | 3.2 | National risk assessment methodology | Partial | Ready to build | DEL-6 | PUB-012, MED-125 |
| REQ-041 | 3.2 | Sector risk results | Partial | Product surface | Investigation, App. B2 | DAT-005, MED-004, MED-033 |
| REQ-042 | 3.2 | Slow-onset hazard statistics | Gap | Ready to build | DEL-1 | — |
| REQ-043 | 3.2 | Sea level rise along the coast | Partial | Ready to build | DEL-4 | MD_1_2 |
| REQ-044 | 3.2 | Land subsidence and salinity intrusion | Gap | Ready to build | DEL-3 | — |
| REQ-045 | 3.2 | Coastal erosion index and beach area loss | Partial | Ready to build | DEL-4 | MED-127, MED-128, MED-129, MED-130, MED-133, MED-134, MED-135, MED-136, MED-137, DMCR_1_1, DMCR_4_1 |
| REQ-046 | 3.2 | Multi-hazard impact chain diagram | Full | Already covered | — | PUB-012, MED-125, MED-048 |
| REQ-047 | 3.2 | Impact chain case studies, agriculture and urban | Partial | Ready to build | DEL-7 | MED-048 |
| REQ-048 | 3.2 | Loss and damage framework under the UNFCCC | Partial | Ready to build | DEL-6 | PUB-026 |
| REQ-049 | 3.2 | Historical loss dashboard | Partial | Loss and damage | Loss and damage work | MED-050, DDPM_3_2, DDPM_2_3, RFD_1_2 |
| REQ-050 | 3.2 | Non-economic loss records | Partial | Loss and damage | Loss and damage work | MED-108, MED-150 |
| REQ-051 | 3.2 | National risk and loss calculation manual | Partial | Loss and damage | Loss and damage work | PUB-012, MED-125 |
| REQ-052 | 3.3 | Cost-benefit and avoided losses methodology | Gap | Awaiting decision | Brief E-1 | — |
| REQ-053 | 3.3 | Gender equality and social inclusion guidance | Gap | Ready to build | DEL-9 | — |
| REQ-054 | 3.3 | Protection measures for vulnerable groups | Partial | Ready to build | DEL-9 | MED-002 |
| REQ-055 | 3.3 | Local wisdom and cultural heritage in adaptation | Gap | Ready to build | DEL-9 | — |
| REQ-056 | 3.3 | National adaptation strategy roadmap | Full | Already covered | — | PUB-009, DAT-021 |
| REQ-057 | 3.3 | Report on systemic barriers by sector | Gap | Ready to build | DEL-8 | — |
| REQ-058 | 3.3 | Financial, technology and capacity support needs | Partial | Awaiting decision | Brief E-1 | MED-079, PUB-027, PUB-028, PUB-029 |
| REQ-059 | 3.3 | Personnel development for climate fund proposals | Gap | Awaiting decision | Brief E-1 | — |
| REQ-060 | 3.3 | Searchable measures database | Gap | Ready to build | DEL-10 | — |
| REQ-061 | 3.3 | Grey infrastructure and nature-based measures | Partial | Ready to build | DEL-10 | DAT-022, MED-042, VID-036 |
| REQ-062 | 3.3 | Repository of local and private sector plans | Gap | Awaiting decision | Brief E-3 | — |
| REQ-063 | 3.3 | National adaptation project tracking | Gap | Awaiting decision | Brief E-3 | — |
| REQ-064 | 3.3 | Budget readiness indicators | Gap | Awaiting decision | Brief E-1 | — |
| REQ-065 | 3.4 | Technology readiness framework | Full | Already covered | — | DAT-014, MED-016, MED-019 |
| REQ-066 | 3.4 | Link to global goal on adaptation indicators | Full | Already covered | — | MED-024, MED-049 |
| REQ-067 | 3.4 | National monitoring and evaluation tracker | Full | Already covered | — | DAT-014 |
| REQ-068 | 3.4 | Successful project case study library | Full | Already covered | — | MED-008, MED-009, MED-010, MED-011, MED-012, MED-013, MED-014, MED-017 |
| REQ-069 | 4.1 | Searchable data catalog and metadata | Full | Already covered | — | SYS-002, PUB-051, PUB-052 |
| REQ-070 | 4.2 | Visualisation and analytics application | Partial | Product surface | Investigation, App. B2 | SYS-003, DAT-005 |
| REQ-071 | 4.3 | Connections to external data portals | Gap | Ready to build | DEL-11 | — |
| REQ-072 | 5.1 | Announcements and training distribution | Full | Already covered | — | SYS-004, PUB-049 |
| REQ-073 | 5.2 | Feedback platform for user agencies | Gap | Ready to build | DEL-11 | — |

---

# Appendix D — Plain names and their codes

The body of this document uses real names throughout. This table maps them to the codes used in DCCE registries, for anyone tracing a citation back to its source.

Also published as `2026-08-12-WP4-DRD-assets-cited.csv`, which adds the owner, the link, and which requirements rely on each asset.

| Code | Name | Type |
|---|---|---|
| `PUB-012` | คู่มือการจัดทำห่วงโซ่ผลกระทบจากการเปลี่ยนแปลงสภาพภูมิอากาศ | Knowledge Asset |
| `DAT-014` | ข้อมูลการประเมินผลการปรับตัวต่อการเปลี่ยนแปลงสภาพภูมิอากาศ | Knowledge Asset |
| `DCCE_3_1` | ความเสี่ยงสาขาการเกษตรและความมั่นคงทางอาหาร | Dataset, DCCE |
| `DCCE_3_2` | ความเสี่ยงสาขาการจัดการน้ำ | Dataset, DCCE |
| `DCCE_3_3` | ความเสี่ยงสาขาการตั้งถิ่นฐานและความมั่นคงมนุษย์ | Dataset, DCCE |
| `DCCE_3_4` | ความเสี่ยงสาขาการท่องเที่ยว | Dataset, DCCE |
| `DCCE_3_5` | ความเสี่ยงสาขาทรัพยากรธรรมชาติและสิ่งแวดล้อม | Dataset, DCCE |
| `DCCE_3_6` | ความเสี่ยงสาขาสาธารณสุข | Dataset, DCCE |
| `DCCE_3_7` | ดัชนีภูมิอากาศ | Dataset, DCCE |
| `DAT-005` | ข้อมูลความเสี่ยงจากการเปลี่ยนแปลงสภาพภูมิอากาศ | Data Product |
| `PUB-009` | แผนการปรับตัวต่อการเปลี่ยนแปลงสภาพภูมิอากาศแห่งชาติ (Thailand's National Adapt | Knowledge Asset |
| `DAT-021` | แผนการปรับตัวต่อการเปลี่ยนแปลงสภาพภูมิอากาศแหงชาติ | Knowledge Asset |
| `MED-025` | แผนการปรับตัวต่อการเปลี่ยนแปลงสภาพภูมิอากาศแห่งชาติ  (National Adaptation Plan | Knowledge Asset |
| `MED-111` | Thailand’s National Adaptation Plan (NAP) | English Edition | Knowledge Asset |
| `MED-112` | แผนการปรับตัวต่อการเปลี่ยนแปลงสภาพภูมิอากาศ (Thailand's National Adaptation Pl | Knowledge Asset |
| `MED-008` | ถอดรหัสความสำเร็จจากพื้นที่ต้นแบบทั้ง 6 สาขา ปัจจัยสู่ความเข้มแข็งและการปรับตั | Knowledge Asset |
| `DAT-022` | ชุดเเนวทางการปรับตัวต่อการเปลี่ยนเเปลงสภาพภูมิอากาศโดยใช้เเนวทางธรรมชาติ (Nbs) | Knowledge Asset |
| `SYS-003` | ฐานข้อมูลความเสี่ยงจากการเปลี่ยนแปลงสภาพภูมิอากาศ | Data Product |
| `DCCE_2_1` | ปริมาณน้ำฝน (GridData, historical) | Dataset, DCCE |
| `DCCE_2_2` | อุณหภูมิสูงสุด (GridData, historical) | Dataset, DCCE |
| `PUB-026` | กองทุนจัดการความสูญเสียและความเสียหายจากสภาพภูมิอากาศ (FRLD) | Knowledge Asset |
| `MED-050` | รายงานฉบับสมบูรณ์ (Final report) การประเมินเบื้องต้นต่อสถานภาพการดำเนินงานที่เ | Knowledge Asset |
| `PUB-003` | สรุป สาระสำคัญของร่างพระราชบัญญัติการเปลี่ยนแปลงสภาพภูมิอากาศ พ.ศ. ... | Knowledge Asset |
| `PUB-004` | ร่างพระราชบัญญัติการเปลี่ยนแปลงสภาพภูมิอากาศ พ.ศ. ... | Knowledge Asset |
| `MED-074` | (ร่าง) พระราชบัญญัติการเปลี่ยนแปลงสภาพภูมิอากาศ พ.ศ. .... (2/2) | Knowledge Asset |
| `MED-075` | (ร่าง) พระราชบัญญัติการเปลี่ยนแปลงสภาพภูมิอากาศ พ.ศ. .... (1/2) | Knowledge Asset |
| `MED-079` | คู่มือ แหล่งทุนด้านการเปลี่ยนแปลงสภาพภูมิอากาศ | Knowledge Asset |
| `PUB-027` | กองทุนด้านการปรับตัวต่อผลกระทบจากการเปลี่ยนแปลงสภาพภูมิอากาศ (AF) | Knowledge Asset |
| `PUB-028` | กองทุนภูมิอากาศสีเขียว (GCF) | Knowledge Asset |
| `PUB-029` | กองทุนสิ่งแวดล้อมโลก (GEF) | Knowledge Asset |
| `DAT-054` | คู่มือการพิจารณาออกหนังสือรับรองที่ประเทศไทยไม่มีข้อคัดค้าน (No-Objection Proc | Knowledge Asset |
| `MED-147` | กระบวนการพิจารณาออกหนังสือรับรองว่าประเทศไทยไม่มีข้อคัดค้านต่อข้อเสนอโครงการ G | Knowledge Asset |
| `PUB-025` | กระบวนการพิจารณาโครงการด้านการเปลี่ยนแปลงสภาพภูมิอากาศที่ขอรับการสนับสนุนทางกา | Knowledge Asset |
| `DAT-013` | คำสั่งแต่งตั้งคณะกรรมการ อนุกรรมการ คณะทำงาน ของหน่วยงานอื่น | Knowledge Asset |
| `SYS-024` | การเปิดโอกาสให้เกิดการมีส่วนร่วม | Data Product |
| `PUB-053` | การเปิดโอกาสให้เกิดการมีส่วนร่วม ปีงบประมาณ พ.ศ. 2569 | Knowledge Asset |
| `PUB-054` | การเปิดโอกาสให้เกิดการมีส่วนร่วม ปีงบประมาณ พ.ศ. 2568 | Knowledge Asset |
| `PUB-055` | การเปิดโอกาสให้เกิดการมีส่วนร่วม ปีงบประมาณ พ.ศ. 2567 | Knowledge Asset |
| `MED-015` | การวิเคราะห์ความเปราะบางและขีดความสามารถในการปรับตัว (Measuring Vulnerability  | Knowledge Asset |
| `PUB-052` | คู่มือแนวทางปฏิบัติการจัดทำธรรมาภิบาลข้อมูล (Data Governance User Manual) | Knowledge Asset |
| `MED-026` | คู่มือแนวทางปฏิบัติการจัดทำธรรมาภิบาลข้อมูล (Data Governance User Manual) | Knowledge Asset |
| `MED-105` | ทำความรู้จักกับ “สภาวะ ENSO-Neutral” | Knowledge Asset |
| `DCCE_2_11` | ปริมาณน้ำฝน (RegCM5, EC-Earth3-Veg) | Dataset, DCCE |
| `DCCE_2_16` | ปริมาณน้ำฝน (Statistical Downscaling, CMIP6) | Dataset, DCCE |
| `DCCE_2_17` | อุณหภูมิสูงสุด (Statistical Downscaling, CMIP6) | Dataset, DCCE |
| `DCCE_2_18` | อุณหภูมิต่ำสุด (Statistical Downscaling, CMIP6) | Dataset, DCCE |
| `DCCE_2_19` | อุณหภูมิเฉลี่ย (Statistical Downscaling, CMIP6) | Dataset, DCCE |
| `MED-125` | คู่มือการจัดทำห่วงโซ่ผลกระทบจากการเปลี่ยนแปลงสภาพภูมิอากาศ | Knowledge Asset |
| `MED-004` | ซูเปอร์เอลนีโญกับความมั่นคงด้านน้ำของประเทศไทย เมื่อ “น้ำ” กลายเป็นความเสี่ยงอ | Knowledge Asset |
| `MED-033` | เกษตรบนเส้นทางเปราะบางต่อภูมิอากาศ : บังกลาเทศการปรับตัวเพื่อความมั่นคงทางอาหา | Knowledge Asset |
| `MD_1_2` | ข้อมูลระดับน้ำทะเล | Dataset, MD |
| `MED-127` | ชายฝั่งในภาวะโลกรวน : หากอยากปรับตัวให้รอด ต้องอาศัยความร่วมมือจากทุกฝ่าย (Cli | Knowledge Asset |
| `MED-128` | ชายฝั่งในภาวะโลกรวน : 4 จังหวัดฝั่งอ่าวไทย ปรับตัวต่อโลกรวนอย่างเข้าใจธรรมชาติ | Knowledge Asset |
| `MED-129` | ชายฝั่งในภาวะโลกรวน : แก้ปัญหาอย่างเนียนไปกับธรรมชาติ (Climate Impacts on Coas | Knowledge Asset |
| `MED-130` | ชายฝั่งในภาวะโลกรวน : ตั้งรับ ยืดหยุ่น ปรับตัวต่อการเปลี่ยนแปลง (Climate Impac | Knowledge Asset |
| `MED-133` | ชายฝั่งในภาวะโลกรวน : กระทบที่อยู่ ปากท้อง และทรัพยากรในท้องทะเล (Climate Impa | Knowledge Asset |
| `MED-134` | ชายฝั่งในภาวะโลกรวน : 24 จังหวัดทะเลไทยแปรปรวน รวน ร้อน (Climate Impacts on Co | Knowledge Asset |
| `MED-135` | ชายฝั่งในภาวะโลกรวน : ชายฝั่งเอเชียตะวันออกเฉียงใต้ เปราะบางต่อโลกรวน (Climate | Knowledge Asset |
| `MED-136` | ชายฝั่งในภาวะโลกรวน  ปะการังอาจตายหมดหากโลกร้อนกว่านี้ (Climate Impacts on Coa | Knowledge Asset |
| `MED-137` | ชายฝั่งในภาวะโลกรวน : จากภัยพิบัติบนฝั่งถึงวิกฤตใต้ทะเล (Climate Impacts on Co | Knowledge Asset |
| `DMCR_1_1` | พื้นที่กัดเซาะชายฝั่ง (WebGIS DCCE) | Dataset, DMCR |
| `DMCR_4_1` | พื้นที่กัดเซาะชายฝั่ง (DMCR ภาคสนาม) | Dataset, DMCR |
| `MED-048` | เจาะลึกห่วงโซ่ผลกระทบ &#8220;น้ำท่วมหาดใหญ่ 2025&#8221; : มากกว่าแค่น้ำท่วม คื | Knowledge Asset |
| `DDPM_3_2` | มูลค่าความเสียหายจากภัยแล้ง | Dataset, DDPM |
| `DDPM_2_3` | ข้อมูลความเสียหายของทรัพย์สิน (ถนน ปศุสัตว์ วัด ฯลฯ) ตามรายงานของ อปท. (LAO-re | Dataset, DDPM |
| `RFD_1_2` | อัตราการสูญเสียพื้นที่ป่าในระยะเวลา 5 ปี รายจังหวัด | Dataset, RFD |
| `MED-108` | การคาดการณ์ผลกระทบต่อความหลากหลายทางชีวภาพภายใต้อุณหภูมิที่สูงขึ้น | Knowledge Asset |
| `MED-150` | คู่มือกิจกรรมสิ่งแวดล้อมศึกษา การเปลี่ยนแปลงสภาพภูมิอากาศและความหลากหลายทางชีว | Knowledge Asset |
| `MED-002` | ซูเปอร์เอลนีโญกับสุขภาพคนไทย ปกป้องชีวิตและกลุ่มเปราะบาง ท่ามกลางโลกที่ร้อนขึ้ | Knowledge Asset |
| `MED-042` | แนวทางการแก้ปัญหาโดยอาศัยธรรมชาติเป็นฐาน (NbS) : Nature-Based Solutions | Knowledge Asset |
| `VID-036` | รู้ไหม? ธรรมชาติก็เป็นนักแก้ปัญหาตัวยง!.มารู้จัก “Nature-based Solutions” กัน | Knowledge Asset |
| `MED-016` | เริ่มอย่างไรกับแนวทางการทำระบบติดตามประเมินผล (Monitoring &amp; Evaluation; M& | Knowledge Asset |
| `MED-019` | ระบบ M&amp;E เครื่องมือวัดความรอดในยุคโลกรวน กรณีศึกษาระบบติดตามประเมินผลของต่ | Knowledge Asset |
| `MED-024` | Global Goal on Adaptation (GGA) Indicator กับการปรับตัวของไทย | Knowledge Asset |
| `MED-049` | รู้จัก 59 ตัวชี้วัด &#8220;เบเล็ง&#8221; (Belém Indicators) เข็มทิศใหม่สู้โลกเ | Knowledge Asset |
| `MED-009` | โครงการจัดทำระบบติดตามประเมินผลการปรับตัวต่อการเปลี่ยนแปลงสภาพภูมิอากาศถอดบทเร | Knowledge Asset |
| `MED-010` | โครงการจัดทำระบบติดตามประเมินผลการปรับตัวต่อการเปลี่ยนแปลงสภาพภูมิอากาศถอดบทเร | Knowledge Asset |
| `MED-011` | โครงการจัดทำระบบติดตามประเมินผลการปรับตัวต่อการเปลี่ยนแปลงสภาพภูมิอากาศถอดบทเร | Knowledge Asset |
| `MED-012` | โครงการจัดทำระบบติดตามประเมินผลการปรับตัวต่อการเปลี่ยนแปลงสภาพภูมิอากาศถอดบทเร | Knowledge Asset |
| `MED-013` | โครงการจัดทำระบบติดตามประเมินผลการปรับตัวต่อการเปลี่ยนแปลงสภาพภูมิอากาศ ถอดบทเ | Knowledge Asset |
| `MED-014` | โครงการจัดทำระบบติดตามประเมินผลการปรับตัวต่อการเปลี่ยนแปลงสภาพภูมิอากาศถอดบทเร | Knowledge Asset |
| `MED-017` | ก้าวสำคัญของการรับมือโลกร้อน “โครงการจัดทำระบบติดตามประเมินผลการปรับตัวต่อการเ | Knowledge Asset |
| `SYS-002` | ระบบบัญชีข้อมูล (Data Catalog) กรมการเปลี่ยนแปลงสภาพภูมิอากาศและสิ่งแวดล้อม | Data Product |
| `PUB-051` | บัญชีข้อมูล (Data Catalogue) | Knowledge Asset |
| `SYS-004` | ระบบสัมมนาและฝึกอบรมด้านสิ่งแวดล้อม | Data Product |
| `PUB-049` | ข่าวสารประชาสัมพันธ์ | Knowledge Asset |

---

# Appendix E — Deferred, and known limits

This document is bounded. What follows is what it does not cover and where it is uncertain, so no one builds a schedule on a false reading of it.

## The loss and damage specification does not exist yet

Four requirements point to the loss and damage work rather than carrying a specification here. That work has not started, so those pointers are forward references rather than links.

REQ-012, REQ-049, REQ-050 and REQ-051 are affected. **Whoever writes that specification should start from these four**, since they establish where the loss and damage product surfaces on the site and what each page needs from it. That linkage does not exist anywhere else.

## Reporting requirements are handled separately, and later

Thailand's adaptation reporting obligations produce a large body of requirements which have been analysed already and mapped to this same site map. They are deliberately not threaded through the pages here.

The reason is sequencing. Reporting sits at the data layer, and the sensible order is to settle the website content and the products first, then compare the finished design against the reporting requirements. That comparison will show how much of the reporting need the platform already meets, and where extending the data layer slightly would close the rest.

The linkage already exists in the underlying data. Fifty-one of the 73 requirements carry a reporting tag, so the comparison can be made mechanically when the time comes. **It is not part of this document and should not be attempted before the design settles.**

## Two services have nowhere to live on the site

The demand analysis identified eight information services. Two of them have no page anywhere in the current site map.

**Multi-hazard early warning.** No section of the site corresponds to it. The only nearby content is the impact chain diagram in section 3.2, which is a static analytical artefact rather than the live localised alerting the service describes.

**Uncertainty governance.** Only thinly represented, through the uncertainty standard in section 3.1 and the technology readiness framework in section 3.4. Neither matches the full service, which would assess the readiness and appropriate use of every data product.

This is a limit of the site map rather than of this analysis. A requirement-by-requirement review cannot surface a service that has no page to sit on. **Both should be raised with whoever owns the site map structure.**

## Two requirements recorded as covered are not verified

REQ-005 and REQ-028 are recorded as fully covered, and both rest on the presence of an existing analytical product. Three other requirements resting on the same reasoning were moved back to gap or partial during the 11 August review.

They are handled here as product surfaces rather than as covered, and both are in the investigation list in Appendix B2. **Do not treat either as finished until that investigation resolves them.**

## Almost all source data is flagged draft

Every DCCE dataset examined for this document carries the status `Baseline-Draft` and the flag `Unverified-Baseline`. None records a maintainer.

That applies to the composite risk indices, the climate grids, the projections, and the coastal and marine observations. It is not a problem with any single dataset, it is the current state of the catalog.

Several datasets are also restricted, meaning the climate grids, the projections, the sea level record and the erosion data. Publishing derived statistics from restricted sources needs an access decision that has not been made.

**Both issues need resolving before any of this data is presented as authoritative.** A page that shows a draft, unverified figure without saying so is worse than a page that shows nothing.

## One caution carried forward

An earlier cross-check moved eight requirements between categories on the strength of a 260-item extract of the dataset catalog. Only one of those eight was independently verified against DCCE's live catalog.

The other seven are real entries with their own identifiers, so they are not in doubt as to existence. But several carry restricted-access or draft flags that have not been confirmed against the live system. Any schedule built on those seven specific items carries that residual uncertainty.

The general lesson holds beyond those seven. The absence of an asset from an extract means the extract did not capture it, not that DCCE does not hold it.
