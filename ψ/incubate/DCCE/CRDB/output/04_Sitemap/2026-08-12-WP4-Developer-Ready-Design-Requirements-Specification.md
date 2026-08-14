# NCAIF Website — Design Requirements for the Build Phase

**Date** 12 August 2026 (revised 13 August 2026)
**Covers** 72 content and function requirements across the 15 main sections of the site map (one requirement, REQ-029, was reviewed and dropped as not relevant — see Appendix E)
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
| `2026-08-12-WP4-DRD-requirements.csv` | 72 requirements, one per row, with status, handling, deliverable, brief, data specification, matched assets and the reasoning behind each match (REQ-029 kept as a struck-through, excluded record) |
| `2026-08-12-WP4-DRD-deliverables.csv` | The 14 deliverables and the requirements each one serves |
| `2026-08-12-WP4-DRD-service-briefs.csv` | The 6 services awaiting a decision (E-1 through E-6), plus the Loss and Damage product line — committed, not awaiting a decision |
| `2026-08-12-WP4-DRD-data-specs.csv` | The 10 data specifications as structured fields (DS-10 kept as a struck-through, excluded record — REQ-071 was re-scoped to a curated links page with no live data connection) |
| `2026-08-12-WP4-DRD-assets-cited.csv` | The 87 assets cited, with owner, link, and which requirements rely on each |

The requirements file carries both the Thai requirement text and its English rendering, along with the status before and after the correction of 11 August, so the change is traceable without reading the diff.

### The five ways a requirement is handled

Not every requirement needs a full specification. Writing one for something that already exists wastes the reader's time, and writing one for a service nobody has agreed to build wastes the writer's. Each of the 72 addressable requirements is handled in one of five ways (a 73rd, REQ-029, was reviewed and dropped — see Appendix E).

| | Handling | Count | What you get |
|---|---|---|---|
| **A** | Already covered | 15 | One line naming the existing source |
| **B** | An existing product could sit here | 9 | One line naming the product, with an explicit warning that we have not verified whether its data is sufficient |
| **C** | Belongs to the loss and damage work | 4 | A forward reference, since that specification is not written yet — but committed and high priority, not optional (see the Loss and Damage entry, Appendix B) |
| **D** | **Ready to build** | **30** | **A full specification with acceptance criteria** |
| **E** | Waiting on a decision | 14 | A summary in Appendix B, not a specification |

The thirty items marked D are the working part of this document.

---

## What the numbers say

Of 72 addressable requirements, 15 are already served by something DCCE holds today. The remaining 57 need work, and they divide sharply.

Thirty can be specified and built now. Fourteen belong to services DCCE has not yet decided to build, so they are described rather than specified. Four belong to the loss and damage work being scoped separately — committed and high priority, not optional. Nine sit on pages where an existing DCCE product could appear, and those carry an important caution explained below.

| Section | | A | B | C | D | E | Total |
|---|---|---|---|---|---|---|---|
| 1.1 | Overview of Thailand's climate risk | 3 | 2 | 0 | 2 | 0 | 7 |
| 1.2 | Area-based data search | 0 | 2 | 0 | 1 | 0 | 3 |
| 2.1 | National climate change situation | 0 | 1 | 1 | 1 | 0 | 3 |
| 2.2 | Area and sector risk profiles | 0 | 1 | 0 | 1 | 0 | 2 |
| 2.3 | Policy, legal and financial tools | 4 | 0 | 0 | 2 | 5 | 11 |
| 2.4 | Planning data services | 0 | 1 | 0 | 1 | 0 | 2 |
| 3.1 | Climate drivers and future scenarios | 0 | 0 | 0 | 6 | 2 | 8 |
| 3.2 | Risk, impact chains and loss and damage | 1 | 1 | 3 | 8 | 1 | 14 |
| 3.3 | Adaptation planning and measures | 1 | 0 | 0 | 6 | 6 | 13 |
| 3.4 | Monitoring and evaluation | 4 | 0 | 0 | 0 | 0 | 4 |
| 4.1 | Data catalog | 1 | 0 | 0 | 0 | 0 | 1 |
| 4.2 | Visualisation and analytics | 0 | 1 | 0 | 0 | 0 | 1 |
| 4.3 | External tools and data hub | 0 | 0 | 0 | 1 | 0 | 1 |
| 5.1 | Announcements and activities | 1 | 0 | 0 | 0 | 0 | 1 |
| 5.2 | Feedback and user services | 0 | 0 | 0 | 1 | 0 | 1 |
| | **Total** | **15** | **9** | **4** | **30** | **14** | **72** |

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
- **REQ-007** Examples of high-value adaptation measures. Covered by a success factors article spanning several sectors and the nature-based solutions guidance dataset (`DAT-022`).

**An existing product could sit here**

- **REQ-004** National risk summary cards. The seven-sector composite risk index holds real numbers, but they are flagged draft and unverified, and nothing renders them as summary cards. Whether the index is fit for this purpose is **not assessed**. Depends on where the index itself ends up hosted — see DEL-13, Appendix A.
- **REQ-005** Critical hotspots by sector and region. This is recorded as fully covered, and the source is the same risk dataset behind the existing products. **Confirmed limitation: the risk map product does not carry location-level exposure, vulnerability, or risk data.** Where the underlying index is province-level, any "hotspot" claim below that level is not spatially explicit — it rests on the same reasoning that was found wanting for three other requirements during the 11 August review. See the investigation in Appendix B2 and DEL-13 (Appendix A) before treating this as complete.

### Ready to build

#### REQ-001 — History and trends of natural disaster events

**Status today** Partial. DDPM holds a real 10-year historical disaster occurrence dataset (`DDPM_2_1`), but it has real limits: restricted access, `Baseline-Draft`/`Unverified-Baseline`, one-way reporting from local administrative organizations up to province level with no ground-truthing, and no UNDRR-aligned taxonomy. No DCCE asset addresses this on its own.

**Who this is for** A first-time visitor, and a policy maker who needs the national picture before looking at any specific hazard.

**What exists today** `DDPM_2_1` (10-year historical disaster occurrence data, DDPM) is a genuine starting point, not a from-scratch compilation task — but its data quality issues (one-way reporting, no ground-truthing, missing taxonomy) need handling before it's presentable. Records also exist across other DDPM holdings more broadly; some may still need gathering beyond this one dataset.

**What the system must do**
- Present a chronological account of significant natural disaster events in Thailand, covering at minimum flood, drought, and storm. Extreme heat is excluded — it has not been registered as a disaster event category in Thailand.
- Build from `DDPM_2_1` as the primary source, structuring it into DS-08 and presenting frequency and severity over time as an interactive product, not a static narrative — this is one of the two new native-hosted products built in the next project (see DEL-12, Appendix A), alongside the Loss and Damage dashboard, which draws on the same underlying DDPM source records.
- Handle `DDPM_2_1`'s known data-quality issues explicitly: flag that reporting is one-way and unverified, and note where the missing UNDRR taxonomy limits how finely events can be categorized.
- Name the source and period for every figure shown.
- Link each hazard type to the specific pages that already cover it — the Thailand Climatology Dashboard (temperature and rainfall extremes) and the Slow-Onset Hazards Profile (coastal and subsidence hazards) — rather than assuming a complete hazard-by-hazard analysis library exists.

**Data spec** DS-08

**Done when**
- [ ] A reader can see how disaster frequency has changed over at least the last two decades.
- [ ] Every figure carries a named source and a date.
- [ ] `DDPM_2_1`'s reporting caveats (one-way, unverified, no UNDRR taxonomy) are stated on the page, not hidden.
- [ ] Each hazard type links to the specific page that covers it, where one exists.
- [ ] The page states clearly which hazards are not covered and why.

**Note** `DDPM_2_1` gives this a real head start — not a from-scratch compilation. It's the same underlying DDPM source data that feeds the Loss and Damage dashboard (REQ-049); gather it once, use it for both. See DEL-12, Appendix A.

#### REQ-003 — Physical risk and transition risk

**Status today** Nothing exists.

**Who this is for** Policy makers and financial sector readers, for whom this distinction is standard vocabulary and its absence is conspicuous.

**What exists today** No DCCE asset addresses this pairing. It is common in climate finance material but absent from DCCE's holdings.

**What the system must do**
- Define physical risk and transition risk, and explain how they differ.
- Give Thai examples of each, drawn from sectors the site already covers.
- Explain why an organisation planning adaptation needs to consider both.
- Connect physical risk to the risk analysis sections and transition risk to the policy and finance sections, including the Climate Change Act and the EU's Carbon Border Adjustment Mechanism (CBAM) as concrete transition-risk drivers for Thai exporters.

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

- **REQ-009** Map integration showing administrative boundaries over the risk map. No map overlay interface or design exists today. **Confirmed limitation: the underlying spatial data does not carry sub-provincial location data**, so an overlay below province level would show administrative boundaries with no real data behind them. See DEL-13, Appendix A.
- **REQ-010** Quick-view dashboard showing vulnerability, threats and recommended measures for a selected point. **Confirmed limitation: vulnerability and threat data has not been compiled anywhere on the site, at any level.** The recommended-measures half has nothing behind it either.

### Ready to build

#### REQ-008 — Search by administrative level, province to district to sub-district

**Status today** Partial. Province-level composite risk data exists (`DCCE_3_1`–`DCCE_3_6`, DS-01) and can support search down to province level. District and sub-district data does not exist.

**Who this is for** A provincial or local government planner who thinks in terms of their own administrative area, not in terms of grid cells.

**What exists today** The spatial risk database provides composite risk indices at province level. District and sub-district figures are not in it. **Confirmed limitation: DCCE's current data assets and the risk map do not carry sub-provincial exposure, vulnerability, or risk data at all.** Closing that gap needs one of two separate undertakings, not assumed into this build: extracting content from Provincial Climate Change Plans and Provincial Disaster Prevention & Mitigation Plans (Brief E-5, Appendix B), or re-aggregating the risk map's own input data onto real administrative geometry (Brief E-6, Appendix B).

**What the system must do**
- Let a user select a province, then a district, then a sub-district. Note that this hierarchy follows DOPA's administrative boundaries (province/district/sub-district), which is **not the same geography as LAO jurisdiction** — a municipality can span or straddle sub-district lines, so a "district" or "sub-district" selection does not represent a municipality's actual boundary. อบจ. is province-wide and unaffected by this mismatch.
- Return risk information at the finest level available for that place.
- **When data below province level does not exist, show the province figure, state plainly that it is a province-level figure, and mark the finer levels as not yet available.** The interface must never return an empty result or imply that no risk exists where data is simply missing.
- Record which places have finer data, so coverage improves visibly as it is added.

**Data spec** DS-01

**Done when**
- [ ] Selecting any of the 77 provinces returns a result.
- [ ] Selecting a district or sub-district without data returns the province figure with a clear label saying so, never a blank result.
- [ ] The label distinguishes "data not yet available" from "no risk identified".
- [ ] Adding finer data for one area does not require a code change.
- [ ] The interface does not imply that a "district" or "sub-district" result represents a municipality's actual jurisdiction.

**Note** The fallback behaviour is the important part of this specification. Without it a developer will build a search that appears broken across most of the country. See Appendix E for the broader DOPA-versus-LAO geography limitation.

---

## 2.1 National climate change situation

The national picture in numbers. Historical extremes, economic losses, and how exposure is changing.

**An existing product could sit here**

- **REQ-013** National exposure trends. The six-sector spatial dataset gives a snapshot of exposure but not a trend over time. Recorded as a gap after the 11 August review. **Confirmed limitation: the underlying data does not support a trend view**, not just for exposure but for hazard and risk equally — this is a limit of the six-sector dataset itself, not something specific to exposure. Kept scoped to exposure trends here; present alongside the disaster-statistics product (REQ-001) rather than standalone, so a reader sees both the trend and the actual events together.

**Belongs to the loss and damage work**

- **REQ-012** National macroeconomic loss and damage statistics. What exists in the catalog is records of damaged assets, human impacts and government emergency payments. Those are not macroeconomic loss figures, they are not aggregated, and their own source flags them as needing cleanup. This can likely be delivered as a summary/rollup view built on the same underlying data as the Loss and Damage dashboard (REQ-049) rather than as its own independent build. **See the Loss and Damage entry in Appendix B.**

### Ready to build

#### REQ-011 — Historical extreme weather statistics

**Status today** Partial. `DDPM_2_1` gives this a real head start, the same source that backs REQ-001. The statistics do not exist yet.

**Who this is for** Planners and researchers who need to know how often an extreme weather event has occurred and how severe it was.

**What exists today** `DDPM_2_1`, DDPM's ten-year historical disaster occurrence dataset — the same underlying source as REQ-001's disaster-history product. It carries the same known issues: reporting flows one way from local administrative organizations up to province level with no central ground-truthing, and it doesn't use the standard UNDRR hazard taxonomy. This is a corrected re-scope from an earlier draft of this requirement, which incorrectly tied it to DCCE's climatology grids (`DCCE_2_1`, `DCCE_2_2`) instead — that data belongs to REQ-033's Climatology Dashboard, a genuinely different product built from meteorological grid data rather than recorded disaster events.

**What the system must do**
- Derive extreme-weather-event statistics — frequency, intensity, and duration of flood, drought, and storm events at minimum — from `DDPM_2_1`, the same historical disaster record that backs REQ-001 (DS-08, DEL-12). This is not a standalone build: gather the DDPM data once and use it for both REQ-001 and REQ-011, presented differently (REQ-001 as the chronological event history on 1.1, REQ-011 as aggregated extreme-event statistics here on 2.1).
- Present frequency, intensity and duration for each extreme type, aggregated to a level a planner can use.
- State the period covered and the known reporting-quality caveats (one-way, unverified reporting; no UNDRR taxonomy) on the page, not hidden.
- Handle the restricted access status on `DDPM_2_1` the same way REQ-001 does.

**Data spec** DS-08

**Done when**
- [ ] Extreme-event statistics are computed from `DDPM_2_1`, not asserted from another source.
- [ ] Each statistic shows its period and the reporting-quality caveats that apply.
- [ ] Access control matches the restriction on the source data.
- [ ] The method used to define an extreme event is documented on the page.
- [ ] The page does not conflate this content with the Thailand Climatology Dashboard (REQ-033) — different source, different product.

---

## 2.2 Area and sector risk profiles

Risk profiles for all 77 provinces and for the six priority sectors. This section reads from the same underlying data as the area-based search in 1.2, presented as a summary rather than a query.

**An existing product could sit here**

- **REQ-015** Risk profiles for the six priority sectors. The six-sector spatial dataset provides a baseline, but no summarised profile document exists. Sectoral studies and plans such as the health national adaptation plan could support this. **Confirmed limitation: this rests on the same province-level-only spatial data as the rest of this cluster** — treat any sub-provincial sectoral claim as unsupported until Brief E-5 or E-6 (Appendix B) closes the gap.

### Ready to build

#### REQ-014 — Risk and vulnerability profiles by area, 77 provinces and local government

**Status today** Partial. Province-level composite risk data exists (`DCCE_3_1`–`DCCE_3_6`, DS-01), and A-BTR Section B adds narrative hazard-hotspot content by province (B-039 flood, B-045 drought) — neither is packaged into the 77-province profile format the requirement asks for.

**Who this is for** อบจ. staff, provincial line-agency offices, and the Governor's office — the province-level profile serves all three of these as-is. It does **not**, and structurally cannot, serve municipality-tier Local Administrative Organizations (LAO) below province level: this isn't only a missing-data problem, a municipality's actual boundary doesn't nest inside the district/sub-district geometry this data would use even if the data existed. See Appendix E for the DOPA-versus-LAO geography limitation.

**What exists today** No dataset or publication presents risk profiles for all 77 provinces in a summarised, ready-to-use form. Province-level composite index figures exist within the risk data, so this may be a presentation problem rather than a data problem. That cannot be confirmed until the investigation in Appendix B2 is done. Provincial Climate Change Plans and Provincial Disaster Prevention & Mitigation Plans could add real sub-provincial detail — see Brief E-5, Appendix B, for the scale of that undertaking.

**What the system must do**
- Produce a profile for each of the 77 provinces covering the main hazards, the exposed sectors, and the vulnerability picture.
- Use one consistent structure across all provinces so they can be compared.
- State plainly that municipality-tier LAO coverage is not available at this level, rather than attempting a sub-provincial cut this data can't support.
- State the source and vintage of every figure, including any draft or unverified flag carried from the source.

**Data spec** DS-01

**Done when**
- [ ] All 77 provinces have a profile with no blanks in the standard structure.
- [ ] Profiles follow one structure and are comparable side by side.
- [ ] Draft or unverified source flags are visible to the reader rather than hidden.
- [ ] The page states plainly that municipality-tier LAO coverage is not available at this level, and why.

---

## 2.3 Policy, legal and financial tools

The largest section in the first half of the site, covering the climate change act, funding sources, budget tracking and institutional arrangements.

The pattern here is sharp, but not in the direction the source material first suggests. Who is in charge and how participation is tracked is well covered. Adaptation finance itself — which funds exist, how to justify a budget, how to tag climate spending, how to track technology and technical assistance — is thin across the board, not just at the edges. The funding directory names the major funds, but genuine finance guidance is light.

**Already covered**

- **REQ-016** Implementation status of the draft climate change act. Covered by an official summary, the draft text and two explainers.
- **REQ-023** DCCE's role as national focal point. Covered by real institutional documents.
- **REQ-024** Structure of the national climate policy committee and its sub-committees. Covered by committee appointment orders.
- **REQ-026** Participation channels and statistics for civil society, private sector and academia. Covered by multi-year disclosure publications and an active tracking system.

**Waiting on a decision** — five requirements, all belonging to the financial and budget evidence service. See Brief E-1 in Appendix B.

### Ready to build

#### REQ-017 — Summary of supporting laws and policy instruments

**Status today** Partial. No DCCE-published asset summarises this, but A-BTR Section A already extracts the disaster prevention act's coverage and several supporting instruments.

**Who this is for** A local government officer who needs to know which legal instruments they can act under.

**What exists today** No DCCE asset summarises the supporting legal framework, and the unified asset database was re-searched specifically for this review with no new hits. But A-BTR Section A already names the Disaster Prevention and Mitigation Act (2007) as the primary DRM framework, with its coverage of prevention, preparedness, response, recovery, and institutional responsibilities (A-REQ-029) — real starting content for the instrument REQ-017 itself says DCCE doesn't cover. Section A also covers the Gender Equality Act, Child Protection Act, Older Persons Act, and Persons with Disabilities Empowerment Act as supporting instruments. The climate change act itself is well covered. Town planning regulations remain genuinely uncovered by any source checked.

**What the system must do**
- Start from the adaptation measures the site already describes, then work backward to which legal and policy instruments support them — not the other way around. Compiling a legal-instrument list first, in isolation from the measures it's meant to support, risks producing a list that doesn't actually line up with what the site's own content needs.
- For each instrument, state which institutional actor it binds — Local Administrative Organizations (LAO), under decentralization/local-administration law, a specific line agency under its own sectoral mandate, or both. LAO and line agencies operate under genuinely different legal bases; a flat, actor-blind list isn't usable by either.
- For each one, also state what it enables and its current status.
- Link to the authoritative text of each instrument.
- Show how each relates to the climate change act, so the reader sees one framework rather than a list.

**Data spec** None needed. This is content.

**Done when**
- [ ] The disaster prevention act and town planning regulations are both covered.
- [ ] Each instrument states which actor (LAO, a named line agency, or both) it binds, plus what it enables and its current status.
- [ ] Each links to its authoritative source text.
- [ ] The relationship to the climate change act is explained.

#### REQ-025 — Coordination between national and local government

**Status today** Partial. DCCE's own role and the national committee structure are documented, and A-BTR Section A has real, adjacent grounding on institutional arrangements — but not this site's specific institutional model.

**Who this is for** Officers at both levels who need to know the route between national policy and local action.

**What exists today** DCCE's own role and the national committee structure are documented. The mechanism connecting national bodies to local administrations is not, but A-BTR Section A's institutional-arrangements entries (A-REQ-019–022) cover sectoral focal points, cross-cutting interagency collaboration, and stakeholder participation across the adaptation cycle — real background, though general and BTR-reporting-shaped rather than built for this site's specific DOPA-vs-LAO-vs-Governor's-office model (Appendix E).

**What the system must do**
- Describe coordination as it actually works: two parallel channels, not one hierarchy. Each central-ministry line agency runs its own vertical line down to its own provincial or regional office (the provincial administration, including DOPA's own office, is itself one line agency among these, structurally a peer of the rest). Separately, Local Administrative Organizations — municipalities and อบจ. — operate on independent, centrally-funded authority under their own decision-making. The Governor, a DOPA official, chairs a loose convening role across the province's line-agency offices, but this is coordination, not command — each office still reports up its own ministry's line.
- State plainly that this looseness is the accurate description of how coordination works, not a documentation gap — while still flagging any place a defined mechanism is genuinely absent.
- Show the route a local plan takes to reach national attention, and the route a national policy takes to reach local implementation, for both channels.
- Name the responsible body at each step.

**Data spec** None needed. This is content.

**Done when**
- [ ] Both the line-agency channel and the LAO channel are described as parallel, not sequential.
- [ ] The Governor's convening role is described accurately as loose coordination, not a command hierarchy.
- [ ] A responsible body is named at each step.
- [ ] Gaps in the mechanism are stated rather than glossed.

---

## 2.4 Planning data services

A small section. One requirement is a genuine product-surface case pending investigation; the other is content-only.

**An existing product could sit here**

- **REQ-028** Integrated spatial risk map. Recorded as fully covered by the existing risk map application and its dataset. This rests on the same product credit found wanting elsewhere, so treat completeness as **unverified** until the Appendix B2 investigation and DEL-13 (hosting migration, Appendix A) are done. The data product inventory holds more entries relevant to this page than are currently cited here — worth a fresh pass during that same investigation.

### Ready to build

#### REQ-027 — Local vulnerability and adaptive capacity indices

**Status today** Partial. The ingredients exist. The index does not.

**Who this is for** Planners who need a single comparable measure of how vulnerable an area is and how well it can cope.

**What exists today** An explainer on how vulnerability and adaptive capacity are measured. No actual index. Underlying proxy indicators exist in quantity, including weather station density, water monitoring station counts and agricultural census vulnerability measures.

**What the system must do**
- Present vulnerability and adaptive capacity at a theoretical, concept level — framed as a named concept, the **Climate Resilience Index** — explaining what it would measure, the logic behind it, and how it relates to the risk framework used elsewhere on the site.
- Publish the intended method in principle: which categories of indicator it would draw on and roughly how they'd be weighted.
- Do **not** compute or publish actual index values per province in this phase — that's analytical content, out of scope until the underlying proxy indicators have been properly assessed.

**Data spec** DS-03

**Done when**
- [ ] The Climate Resilience Index concept is explained clearly, in Thai and English, without asserting computed values.
- [ ] The intended method and indicator categories are described.
- [ ] The page does not present any per-province number as if it were computed.

**Note** This is a lighter, explainer-only deliverable in this phase. Computing and publishing real index values is a separate, later undertaking once the underlying indicators are assessed.

---

## 3.1 Climate drivers, observations and future scenarios

The weakest section on the site by raw coverage, but most of that gap should not be closed by DCCE building analytical dashboards. Most of the analytical work this section might imply — station networks, satellite monitoring, seasonal forecasting — is already done elsewhere, by GISTDA and TMD in particular, and is outside DCCE's expertise to run or maintain. This section's job is mostly communication: explain what these observations and drivers mean, and link out to the agency that actually holds and maintains them. Ingesting external feeds into this platform to run DCCE's own statistical analysis is something to do deliberately, not by default.

The one deliberate exception is the **Thailand Climatology Dashboard** (REQ-033 below) — a Thailand-specific analytical product in the spirit of the World Bank's Climate Knowledge Portal, built once as a shared backend and surfaced both as a full app (sections 4.2/4.3) and as embedded views on the pages where its content is relevant. This is judged unique and strategic enough to justify building, unlike the station/satellite/seasonal-monitoring items below.

**Waiting on a decision** — two requirements belonging to the uncertainty governance service. See Brief E-2 in Appendix B.

### Ready to build

#### REQ-030 — Weather station observation data, short and medium range

**Status today** Nothing exists in DCCE's holdings.

**Who this is for** Researchers and engineers who need point measurements rather than modelled grids.

**What exists today** No DCCE asset holds station-level weather data. The meteorological department (TMD) holds it and already publishes it.

**What the system must do**
- Explain what station observation data is and how it differs from modelled grids, in plain language.
- Link directly to TMD's own station data services rather than re-hosting the data on this platform.
- State what TMD's data covers (variables, typical update cadence) so a reader knows what to expect before clicking through.

**Data spec** DS-04

**Done when**
- [ ] The explainer clearly distinguishes station observations from modelled grids.
- [ ] A working link to TMD's station data service is in place.
- [ ] The page states what TMD's data covers without duplicating it.

**Note** A live data connection (rather than a link) would still require a formal agreement with TMD — that stays a future, budget-contingent option, not committed scope here.

#### REQ-031 — Satellite observation data for forest, land cover, water and coral

**Status today** Nothing exists in DCCE's holdings.

**Who this is for** Analysts tracking change in natural systems over time.

**What exists today** No DCCE asset holds satellite observation data. GISTDA holds the relevant land/water products, and marine bodies hold coral observations — both already publish this material.

**What the system must do**
- Explain what each layer (forest cover, land cover, water bodies, coral bleaching) is and why it matters for adaptation.
- Link directly to GISTDA's and the relevant marine body's own published products rather than re-hosting them.
- State the source agency and how current each external product is.

**Data spec** DS-04

**Done when**
- [ ] All four layers named in the requirement have an explainer and a working link to the source agency's own product.
- [ ] The source agency is named for each layer.

**Note** A live data connection would still require agreements with GISTDA and the relevant marine bodies — a future, budget-contingent option, not committed scope here.

#### REQ-032 — Monitoring of globally significant climate phenomena

**Status today** Partial, and weakly so.

**Who this is for** Planners who need to know whether the coming season is likely to be unusual.

**What exists today** One general-audience article explaining ENSO-neutral conditions. Nothing on the Indo-Pacific/Interdecadal Pacific Oscillation (IPO) or the Atlantic overturning circulation. There is no monitoring feed, only a one-off explainer.

**What the system must do**
- Explain ENSO and IPO — what they are, and why Thailand's seasonal outlook depends on them — and link to TMD's or another authoritative source's live monitoring rather than running an independent feed.
- Explain what the current state of these phenomena typically means for Thailand in seasonal terms.
- Cover the Atlantic overturning circulation at explanatory level only, since no Thai monitoring role exists for it.
- Link each phenomenon to the sectors it most affects.

**Data spec** DS-05

**Done when**
- [ ] ENSO and IPO are both explained, with a working link to an authoritative live monitoring source.
- [ ] The seasonal implication for Thailand is stated in plain language.
- [ ] The overturning circulation is explained even though it is not monitored locally.

#### REQ-033 — Climatology and key climate variables

**Status today** Partial. Multi-decade data exists but nothing has been derived from it.

**Who this is for** Anyone who needs the baseline climate against which change is measured.

**What exists today** National grid data for temperature and rainfall covering 1981 to 2023. Raw grid, restricted access, flagged draft and unverified. No trend statistics have been computed. Provenance (station-interpolated versus reanalysis output) is not stated in the catalog — confirm before publishing derived statistics.

**What the system must do**
- This is the core view of the Thailand Climatology Dashboard backend (DEL-1, Appendix A) — derive climatological baselines and trend statistics for temperature and rainfall from the same grids.
- Present trends at a level a planner can use, meaning province or region rather than grid cell, surfaced both as an embedded view on this page and inside the full Climatology Dashboard app (4.2/4.3).
- State the baseline period used and keep it consistent across the site.
- Show the uncertainty around each trend rather than a single number alone.

**Data spec** DS-02

**Done when**
- [ ] Trend statistics are derived from the 1981 to 2023 grids.
- [ ] One baseline period is used consistently across every page that shows a trend.
- [ ] Each trend is presented with its uncertainty.
- [ ] Access control matches the restriction on the source.
- [ ] The grid's provenance is confirmed and stated before publication.

**Note** REQ-011 was previously (incorrectly) tied to this same grid data — it has been re-scoped to `DDPM_2_1` instead (see REQ-011, section 2.1). REQ-033's grid access question stands on its own now.

#### REQ-035 — Library of high-resolution downscaled future projections

**Status today** Partial. Real projection data exists, but not at the resolution the requirement asks for, and DCCE already runs a platform for this.

**Who this is for** Engineers and planners designing for conditions decades ahead.

**What exists today** Downscaled projection datasets running to 2099 and 2100, produced both dynamically and statistically, covering national extent. Access is restricted and resolution is national grid rather than the high-resolution sub-national product the requirement describes. DCCE's own `clim-webbased.dcce.go.th` platform already appears to serve this kind of material — **this asset is not yet in either canonical asset registry checked for this document and needs a formal registry entry**, but should be the link target rather than re-publishing the datasets here.

**What the system must do**
- Explain what downscaled projections are and what "national grid resolution" means for a reader planning at sub-national scale.
- Link to `clim-webbased.dcce.go.th` (or a Thai-language front end of it) rather than ingesting and re-hosting the underlying datasets on this platform.
- State plainly that resolution is national grid, not the high-resolution sub-national product the original requirement describes, and what that means for sub-national use.
- Record what higher-resolution product would be needed to meet the requirement fully, so the gap is visible rather than implied.

**Data spec** DS-06

**Done when**
- [ ] The explainer states what's available (model, method, scenario, period) and links to `clim-webbased.dcce.go.th`.
- [ ] The resolution limitation is stated on the page, not buried in metadata.
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

The analytical core of the site, and the section where the most work sits. Fourteen requirements, of which eight are ready to build and three belong to the loss and damage work. Most of this section is content — definitions, methodology explainers, case studies — rather than new analytical products; the exceptions are the Slow-Onset Hazards Profile (REQ-042/043/044/045, its own consolidated deliverable below) and the Loss and Damage product line.

One strength runs through this section. DCCE's impact chain manual is a real, purpose-built document. It is also being asked to stand in for several things it was not written to be, which is why some requirements below are partial rather than covered.

**Already covered**

- **REQ-046** Multi-hazard impact chain diagram. Covered by the impact chain manual.

**An existing product could sit here**

- **REQ-041** Sector risk results for food security, water, health and business disruption. The six-sector dataset provides results for food, water and settlement. Heat and health impact and business disruption are not represented. **Confirmed limitation: what exists is the risk map at provincial level only** — any sector-level insight beyond that would need to be synthesized from literature review, not asserted from the existing dataset.

**Belongs to the loss and damage work**

- **REQ-049** Dashboard of historical economic and physical losses. Real machine-readable damage records exist for several hazards but are not dashboard-ready. Shares its underlying DDPM source data with REQ-001's disaster-statistics product (DEL-12) — gather that data once, use it for both. **See the Loss and Damage entry in Appendix B.**
- **REQ-050** Record of non-economic losses covering mental health, biodiversity and cultural heritage. Only biodiversity has material. **See the Loss and Damage entry in Appendix B.**
- **REQ-051** Standard national manual for risk, impact and loss calculation. The impact chain manual is the closest proxy and was not written for this. **See the Loss and Damage entry in Appendix B.**

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

#### REQ-040 — A national risk assessment methodology

**Status today** Partial. A proxy exists.

**Who this is for** Any agency conducting a risk assessment that should be comparable with others.

**What exists today** DCCE's impact chain manual, which is the closest existing methodology document. No purpose-built national risk assessment standard exists. Existing multi-hazard methodologies — CRVA and CRM, from GIZ and UNDRR — offer a more analytical, quantitative reference point DCCE could adapt rather than starting from nothing.

**What the system must do**
- Committed scope is an explainer-level framework: set out the broad steps, the required inputs, and the expected outputs of a national risk assessment, in plain language.
- State how it relates to the impact chain method, whether as an extension or a distinct procedure, and note CRVA/CRM as reference methodologies DCCE could draw on.
- Defer the official, binding guideline — compliance criteria and a formal template or worked example — to a later phase. Publishing those now would imply a standard-setting decision this project doesn't make.

**Data spec** None needed. This is methodology content.

**Done when**
- [ ] The framework is published as its own explainer, not as a reading of the impact chain manual.
- [ ] Its relationship to the impact chain method, and to CRVA/CRM, is stated explicitly.
- [ ] The page states plainly that compliance criteria and a formal template are a later, separate undertaking, not covered here.

### Slow-Onset Hazards Profile — REQ-042, REQ-043, REQ-044, REQ-045

These four requirements are one page in the sitemap (node 3.2.2.1, Slow-Onset Hazards Profile), not four separate pages — they're presented as one consolidated deliverable (DEL-4, Appendix A). All four follow the same pattern: a static explainer is the committed scope now, and any real rate, index, or source-establishment work is a budget-contingent stretch item for later, not committed in this phase.

#### REQ-042 — Statistics and assessment of slow-onset hazards

**Status today** Nothing exists as a consolidated report.

**Who this is for** Long-term planners, for whom gradual change matters more than individual events.

**What exists today** No consolidated slow-onset assessment. Individual components exist separately, including sea level data covered under REQ-043 and erosion data under REQ-045.

**What the system must do**
- This trend content shares its backend with the Thailand Climatology Dashboard (REQ-033, DEL-1) — the same DS-02 pipeline computes it — but it's displayed here, on the Slow-Onset Hazards page, not on the climate-drivers page.
- Consolidate slow-onset hazard tracking covering rising average temperature and shifting rainfall distribution.
- Present rate of change with its uncertainty, not just current state.
- Distinguish observed change from projected change.
- Link to the other slow-onset hazards on this same page (REQ-043/044/045) rather than treating them as separate topics.

**Data spec** DS-02

**Done when**
- [ ] Temperature and rainfall distribution change are both covered with rates and uncertainty.
- [ ] Observed and projected change are visually and textually distinct.
- [ ] The page presents this alongside sea level, subsidence/salinity, and erosion as one Slow-Onset Hazards Profile.

#### REQ-043 — Sea level rise along the Thai coast and the Gulf

**Status today** Partial. Observations exist. A derived rate does not.

**Who this is for** Coastal planners and infrastructure engineers.

**What exists today** An annual sea level observation dataset from the marine department hydrology group, national coverage through 2026, tagged to sea level rise. These are raw annual readings, restricted access, and no rate of rise has been derived.

**What the system must do**
- Committed scope: a static explainer covering what's observed, why sea level rise matters for the Thai coast, and what the observation record shows in general terms.
- Deferred, budget-contingent scope: deriving an actual rate of rise by coastal segment with uncertainty. A real rate treatment at this resolution is a substantial undertaking on its own — worth doing if DCCE can allocate resource for it in the contractor's scope, but not committed here.
- Show the observation record itself alongside the explainer, even without a derived rate.
- State the period of record and any gaps in it.

**Data spec** DS-07

**Done when**
- [ ] The static explainer is published, covering the observation record and its significance.
- [ ] The page states plainly whether a derived rate exists yet, and if not, that it's a future undertaking.
- [ ] Access control matches the source restriction.

#### REQ-044 — Land subsidence and salinity intrusion

**Status today** Partial for subsidence, Gap for salinity. No DCCE asset covers either, but A-BTR Section B gives real, citable subsidence figures.

**Who this is for** Bangkok and central region planners, for whom subsidence compounds flood and sea level risk.

**What exists today** No DCCE asset covers either subsidence or salinity intrusion — neither appeared in the document inventory or the dataset catalog. A-BTR Section B fills part of the subsidence half: B-073 reports Bangkok's relative sea-level rise at about 0.021 m/year before groundwater regulation, declining to about 0.013 m/year after (subsidence-amplified), and B-040 reports Bangkok's compound flood risk from low elevation (0.5–1.5m above mean sea level) plus land subsidence. Salinity intrusion remains fully uncovered by any source checked.

**What the system must do**
- Committed scope: a static explainer covering what land subsidence and salinity intrusion are, why they matter for Bangkok and the central region, and how they interact with sea level rise and flooding.
- Deferred, budget-contingent scope: establishing real data sources for subsidence and salinity intrusion measurement and presenting them with location, rate, and period. This needs agreements with other bodies and is foundational data a build team cannot substitute from DCCE material — not committed in this phase.

**Data spec** DS-04

**Done when**
- [ ] The static explainer is published, covering both hazards and their interaction with sea level rise and flooding.
- [ ] The page states plainly that source data for either hazard doesn't yet exist and is a future undertaking.

**Note** Requires agreements with other bodies for the deferred scope. Treat that agreement as a separate, later task from the explainer.

#### REQ-045 — Coastal erosion index and beach area loss

**Status today** Partial. Quantitative data exists but is not built into an index.

**Who this is for** Coastal province planners and marine resource managers.

**What exists today** Real area-based erosion extent data from marine resource bodies, alongside a series of nine coastal adaptation infographics. The data is raw area figures rather than a computed index.

**What the system must do**
- Committed scope: a static explainer using the existing extent data and the nine coastal adaptation infographics, presenting what's known about erosion in general terms.
- Deferred, budget-contingent scope: computing a real erosion index and presenting beach area lost over time by coastal segment with a published method. Worth doing if DCCE can allocate resource for it, not committed here.
- Link to the existing coastal adaptation material rather than duplicating it.

**Data spec** DS-07

**Done when**
- [ ] The static explainer is published, using the existing extent data and infographics.
- [ ] The page states plainly whether a computed index exists yet, and if not, that it's a future undertaking.
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

**Status today** Partial. No DCCE asset addresses this, but A-BTR Section A has real legal grounding.

**Who this is for** Anyone designing an adaptation measure who must show it reaches people equitably.

**What exists today** No DCCE asset addresses gender equality or social inclusion in adaptation. A-BTR Section A names the Gender Equality Act, Child Protection Act, Older Persons Act, and Persons with Disabilities Empowerment Act as the legal grounding for gender-responsive and inclusive adaptation — legal/rights framing, not the practical stage-by-stage steps this requirement also needs.

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

**Status today** Partial. No DCCE asset reports on this, but A-BTR Section C already frames systemic barriers across the full cycle.

**Who this is for** Policy makers deciding where to intervene, who need to know why adaptation stalls.

**What exists today** No DCCE asset reports on systemic barriers. A-BTR Section C (priorities, barriers and strategy) already frames this: C-017 states that adaptation gaps and limitations remain across the full implementation and reporting cycle despite existing frameworks, and C-018 specifies that gaps span planning, measure design, budget allocation, implementation, monitoring and evaluation, and reporting. Real starting inventory, not the finished sector-by-sector report with named sources the requirement needs.

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

Infrastructure that already exists, but the content it holds is not settled yet.

**Already covered, with a scope decision still pending**

- **REQ-069** Searchable system for datasets, data products and metadata meeting national security standards. DCCE already operates the catalog, has a publication describing it, and has a governance manual covering metadata and security. **This is not zero-effort.** CRDB provides only an initial data-inventory seed for the catalog; what actually goes into it — its final scope and content — needs formal approval in the next project, not just a link to the existing system.

---

## 4.2 Visualisation and analytics application

One requirement, two components on different timelines. The map/analysis half ships at launch; the engineering half doesn't.

**Ships at launch — an existing product hosted as-is**

- **REQ-070** Interactive application showing hazard maps and supporting risk analysis. DCCE's existing risk map application (SYS-003) is a real working tool, hosted here once migrated (DEL-13). Its adequacy as a standalone map/analysis tool is **not assessed**.

**Hosting architecture for this page.** Native-hosted, on the new platform's own infrastructure: the three existing DCCE analytical products once migrated (DEL-13, Appendix A) and the new strategic products built in the next project — the disaster-statistics product (DEL-12), the Loss and Damage dashboard, and the Thailand Climatology Dashboard (DEL-1). Link-out hub, not natively hosted: anything not owned by DCCE.

**Not at launch — the engineering design values are separate, needed work on a different timeline.** The requirement also names rainfall intensity and temperature design values at plot level (IDF curves) for civil-engineering use. This is real, needed work, not something to drop from scope — but it does not ship with this platform launch. It requires new methodology and new rainfall/temperature statistical data DCCE does not currently hold, and it will **not** be built from SYS-003's composite risk index: that data serves the general hazard map, not plot-level engineering curves, and the two should not be conflated. Scope this as its own future-project workstream, not as a late addition to this build. Details in Brief E-4, Appendix B.

---

## 4.3 External tools and data hub

One requirement, entirely uncovered — but a content compilation task like most of the rest of the site, not an integration build.

### Ready to build

#### REQ-071 — Curated links to international and specialist data portals

**Status today** Nothing exists.

**Who this is for** Researchers and analysts who need data DCCE does not hold and currently go looking for it themselves.

**What exists today** No DCCE asset provides these links. There's no content gap analysis to apply since it's a fresh compile, not a match against existing material.

**What the system must do**
- Provide a link entry for each external portal named in the requirement: the meteorological department weather service, the space technology agency geo-informatics portal, and the Copernicus climate data store.
- For each, state what data it holds, what access conditions apply, and how it relates to data on this site.
- Record the agreement or licence under which each connection operates, where one is publicly known.

**Done when**
- [ ] All three named portals have a link entry.
- [ ] Each states its holdings, access conditions and relationship to local data.

**Note** This is a content compilation task, not technical integration work — no partnership agreements or live connections are required to launch it.

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

**Note** This builds new operational capability rather than filling a content gap, and sits outside the content production work that covers most of this document.

---

# Appendix A — What actually has to be built

The thirty ready-to-build requirements are not thirty separate pieces of work. Several pages draw on the same underlying effort, so building once serves several requirements.

This appendix groups them into fourteen deliverables. **This is the planning view. Anyone scheduling the build should work from this table rather than counting requirement cards.**

| | Deliverable | Type | Serves | Requirements |
|---|---|---|---|---|
| **DEL-1** | Thailand Climatology Dashboard | Data engineering + product | 3.1 | REQ-033 |
| **DEL-2** | Provincial risk profile layer | Data engineering and interface | 1.2, 2.2, 2.4 | REQ-008, REQ-014, REQ-027 |
| **DEL-3** | External-source explainers with data-sharing agreements | Content + partnership | 3.1 | REQ-030, REQ-031 |
| **DEL-4** | Slow-Onset Hazards Profile | Content, with derivation as a later stretch | 3.2 | REQ-042, REQ-043, REQ-044, REQ-045 |
| **DEL-5** | External-source explainers, monitoring and projections | Content + partnership | 3.1 | REQ-032, REQ-035 |
| **DEL-6** | Concept and methodology standards | Content | 3.2 | REQ-038, REQ-040, REQ-048 |
| **DEL-7** | Risk framing and worked examples | Content | 1.1, 3.1, 3.2 | REQ-003, REQ-037, REQ-047 |
| **DEL-8** | Policy and institutional content | Content | 2.3, 3.3 | REQ-017, REQ-025, REQ-057 |
| **DEL-9** | Inclusion and community adaptation content | Content | 3.3 | REQ-053, REQ-054, REQ-055 |
| **DEL-10** | Adaptation measures library | Product and content | 3.3 | REQ-060, REQ-061 |
| **DEL-11** | New operational capability (feedback platform) | Build | 5.2 | REQ-073 |
| **DEL-12** | Disaster statistics product | Data engineering + product | 1.1, 2.1 | REQ-001, REQ-011 |
| **DEL-13** | Migrate existing DCCE analytical products onto platform infrastructure | Data engineering + hosting | 1.1, 1.2, 2.1, 2.2, 2.4, 3.2, 4.2 | — (serves the product-surface items: REQ-004, REQ-005, REQ-009, REQ-010, REQ-013, REQ-015, REQ-028, REQ-041, REQ-070) |
| **DEL-14** | External data hub links | Content | 4.3 | REQ-071 |

Four observations for whoever plans this work.

**DEL-1 and DEL-4 (in part) share a backend; DEL-12 shares a different one.** The Thailand Climatology Dashboard (DEL-1) and the temperature/rainfall trend view inside the Slow-Onset Hazards Profile (DEL-4) run on the same DS-02 pipeline — resolve restricted-access questions once, for both. Separately, DEL-12's disaster-statistics product, REQ-011's extreme-weather statistics, and the Loss and Damage dashboard (Appendix B) all draw on the same underlying DDPM source records (`DDPM_2_1`, DS-08) — gather that data once, use it for all three.

**DEL-13 is separate from the Appendix B2 investigation, but related.** B2 asks what data actually feeds the three existing analytical products. DEL-13 is the follow-on hosting work — migrating those products onto this platform's own infrastructure once that question is answered. Treat them as two ordered steps, not one task.

**DEL-3 and DEL-5 no longer gate anything downstream.** Now that these deliverables are explainer-and-link content rather than data ingestion, the underlying agency data-sharing agreements (TMD, GISTDA) are a future, budget-contingent option — not a precondition for shipping the committed content.

**Six of the thirteen are primarily content production.** DEL-6 through DEL-10, DEL-3, and DEL-5 need writers and subject specialists rather than engineers. That is a different procurement from the rest of this document and is easy to overlook when reading a specification framed around a website build.

---

# Appendix B — Services awaiting a decision, and one committed but blocked

Fourteen requirements belong to services DCCE has not yet decided to build. Writing full specifications for them would imply a commitment that has not been made, so they are summarised here instead. Two further briefs (E-5, E-6) cover data-quality undertakings that need a resourcing decision rather than a policy decision. A separate entry, the Loss and Damage product line, is **not** in this category — it's already a committed, high-priority requirement, blocked on a sequencing dependency rather than a decision; it's placed here because, like the others, its full specification isn't written in this document.

**If DCCE selects any of the E-series briefs, proper requirement gathering is needed before building.** These briefs establish scale and blockers. They are not specifications.

## Brief E-1 — Financial and budget evidence

**Requirements** 10 · **Sections affected** 2.3, 3.3, 3.2

REQ-018, REQ-019, REQ-020, REQ-021, REQ-022, REQ-039, REQ-052, REQ-058, REQ-059, REQ-064

**What this service would do.** Give agencies the evidence to justify adaptation spending, particularly where a climate-resilient design costs more than the historical benchmark for comparable work. It covers avoided losses calculation, cost-benefit analysis, budget tagging, and tracking of support received.

**Demand.** The strongest single cluster in this document. Ten of the fourteen waiting requirements sit here, and the demand analysis records it as a repeated concern from agencies facing budget scrutiny.

**What exists.** The funding directory names the major funds — DCCE's funding guide and dedicated publications for AF, GCF, and GEF are real and operational. Beyond naming those sources, adaptation finance content is genuinely light, not well covered — there's no guidance on using them, no cost-benefit method, and no budget-tagging material.

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

**Why it appears here despite having no requirement of its own.** Section 4.2 holds a single requirement, REQ-070, which ships at launch as an existing product surface (DCCE's risk map application, SYS-003). The intensity-duration-frequency curves named in that same requirement are this engineering component — a separate, needed piece of work confirmed out of scope for this platform's launch.

**What exists.** Nothing for the engineering half. A search across both the document inventory and the dataset catalog returned no material of any kind on design curves. This does not draw on SYS-003 or any other launch-scope asset — it needs its own rainfall/temperature data, not a repurposing of the composite risk index that powers the map.

**Core blocker.** Producing these curves means computing rainfall intensity-duration-frequency statistics that do not exist in DCCE's holdings at any resolution. This is closer in effort to the confirmed gaps in section 3.2 than to anything else in section 4.

**Readiness.** Ready for joint development, but requires engineering standards bodies and specialist validation. Confirmed as a future-project workstream, not part of this launch.

**A warning for planners.** Because REQ-070 reads as partially covered at page level, this work is easy to mistake for something that falls out of the visualisation build for free. It doesn't — it's real work, on its own timeline, needing its own data.

## Brief E-5 — Provincial & District Plan Synthesis

**Requirements** 0 of their own — closes a gap underlying REQ-008, REQ-014, REQ-015 · **Sections affected** 1.2, 2.2

**What this service would do.** Extract structured, sub-provincial risk and vulnerability content from Thailand's 77 Provincial Climate Change Plans and Provincial Disaster Prevention & Mitigation Plans, and turn it into usable data for the area-based search and provincial profile pages.

**Why it appears here.** Neither DCCE's current data assets nor the risk map carry real sub-provincial exposure, vulnerability, or risk data. These plans are the only path to genuine sub-provincial content — but they exist as scattered documents, not data.

**What exists.** Nothing structured. The plans themselves exist across 77 provinces but have never been synthesized into a common format.

**Core blocker.** Scale. Reading and structuring content from 77 provinces' worth of planning documents is a large document-synthesis undertaking, not a data-engineering task. It genuinely provides information not available anywhere else in DCCE's holdings or the risk map.

**Readiness.** High value, high effort. Needs an explicit DCCE resourcing decision before it's scheduled — not assumed as part of this build phase.

## Brief E-6 — LAO-level data disaggregation

**Requirements** 0 of their own — closes a gap underlying REQ-008, REQ-014 · **Sections affected** 1.2, 2.2

**What this service would do.** Re-aggregate the risk map's underlying input datasets — currently disaggregated only to DOPA's administrative boundary (province/district/sub-district) — onto actual Local Administrative Organization (LAO) polygons, producing genuine LAO-level figures rather than administrative-boundary approximations.

**Why this is not a display problem.** The source data was never collected or tagged at LAO granularity in the first place, so no simple crosswalk of existing figures is possible. Municipalities in particular can span or straddle sub-district lines; อบจ. is province-wide and unaffected. Producing a real LAO-level figure means geospatial reallocation (e.g. area-weighted redistribution) of the underlying data — genuine geospatial engineering, distinct in kind from Brief E-5's document-synthesis work.

**What exists.** Nothing at LAO resolution. The underlying datasets exist only at DOPA administrative-boundary resolution.

**Core blocker.** A daunting geospatial/data-engineering undertaking. Real added value for municipality-tier LAO officials, who currently cannot get a figure that represents their actual jurisdiction.

**Readiness.** High value, high effort. Needs an explicit DCCE resourcing decision, distinct from Brief E-5 — the two are complementary, not substitutes for each other.

---

## Loss and Damage product line — committed, not awaiting a decision

**Requirements** 4 · **Sections affected** 2.1, 3.2

REQ-012, REQ-049, REQ-050, REQ-051

**Priority, per sitemap v8.** REQ-012 MUST · REQ-049 MUST · REQ-051 MUST · REQ-050 SHOULD. Three of the four are mandatory requirements, not optional ones — "belongs to a separate work package" should not be read as "belongs to a lower priority."

**What this would do.** A national macroeconomic loss and damage database (REQ-012), a dashboard of historical economic and physical losses (REQ-049), a record of non-economic losses (REQ-050), and a standard national manual for risk, impact, and loss calculation (REQ-051).

**What exists.** Real, machine-readable damage records exist for several hazards but aren't dashboard-ready. Only biodiversity has material for non-economic losses. The impact chain manual is the closest proxy for a calculation methodology, but it wasn't written for this purpose. REQ-049 shares its underlying source data with REQ-001's disaster-statistics product (DEL-12, Appendix A) — both draw on the same DDPM records, so that data-gathering step should happen once, for both. REQ-012 can likely be delivered as a summary or rollup view built on REQ-049's data rather than as its own independent build.

**Core blocker.** This is not a DCCE decision to make — it's a sequencing dependency. The loss-and-damage work package's own specification hasn't been written yet, and this document's requirements can't be built ahead of that methodology without guessing at it.

**Readiness.** Committed and high priority. Blocked on the separate work package's specification landing, not on DCCE choosing whether to build it.

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

**This investigation is step one of two.** Once the inventory is done, DEL-13 (Appendix A) is the follow-on work — actually migrating those three products onto this platform's own infrastructure. Treat them as ordered, not interchangeable.

## Data specifications

Each specification covers one dataset or group, and is referenced from the requirement cards above. Fields are taken from DCCE's data catalog. **Where a field is not recorded there, it is marked unknown rather than estimated.**

Two observations apply to every sheet below. Every DCCE dataset examined carries the status `Baseline-Draft` and the flag `Unverified-Baseline`. And no dataset in the catalog records a maintainer. Both need resolving before any of this data is published as authoritative.

### DS-01 — Provincial composite risk data
**Serves** REQ-008, REQ-014 · **Source** `DCCE_3_1` to `DCCE_3_6`, six sector datasets
**Granularity** Province · **Coverage** National, 1960 to 2100 · **Frequency** Annual
**Format** CSV · **Access** Public · **Status** Baseline-Draft, Unverified-Baseline
**Limitations** Scenarios limited to two pathways. Composite method is not reversible to inputs. **Confirmed: does not carry sub-provincial exposure, vulnerability, or risk data.** Closing that gap is Brief E-5 (document synthesis) or Brief E-6 (geospatial disaggregation), Appendix B — not assumed into this specification.
**Maintainer** UNKNOWN — pending investigation

### DS-02 — Historical climate grids
**Serves** REQ-033, REQ-042 (REQ-042's trend view shares this same pipeline but displays on the Slow-Onset Hazards page, DEL-4) · **Source** `DCCE_2_1` rainfall, `DCCE_2_2` maximum temperature
**Granularity** Grid · **Coverage** National, 1981 to 2023 · **Frequency** Daily and monthly
**Format** Raster · **Access** **Restricted** · **Status** Baseline-Draft, Unverified-Baseline
**Limitations** Raw grids only. No derived statistics exist. Access restriction must be resolved before publication. Provenance (station-interpolated versus reanalysis) is not recorded — confirm before publishing derived statistics.
**Maintainer** UNKNOWN — pending investigation

### DS-03 — Vulnerability and adaptive capacity indicators
**Serves** REQ-027 · **Source** Proxy indicators across several catalog entries, including monitoring station density and agricultural census measures
**Granularity** Mixed, mostly province · **Coverage** UNKNOWN, varies by indicator
**Access** Mixed · **Status** Baseline-Draft
**Limitations** No composite index exists. Indicator coverage varies by area, so completeness must be shown per area.
**Maintainer** UNKNOWN — pending investigation

### DS-04 — Observation data held by other agencies
**Serves** REQ-030, REQ-031 (both now explainer + link, not ingestion), REQ-044 (deferred, budget-contingent scope only) · **Source** External. Meteorological department, space technology agency, marine and groundwater bodies
**Granularity** UNKNOWN · **Coverage** UNKNOWN · **Frequency** UNKNOWN
**Access** **Not currently available to DCCE**
**Limitations** None of this data is in DCCE's catalog. Every field is unknown until an agreement exists.
**Note** A live data connection under any of these three requirements needs a formal agreement first — this stays a future, budget-contingent option, not committed scope in this phase.

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
**Serves** REQ-001 (DEL-12, its own native product), REQ-011 (extreme-weather statistics, DEL-12, section 2.1 — re-scoped from DS-02), and REQ-049 (the Loss and Damage dashboard, Appendix B) · **Source** `DDPM_2_1` — 10-year historical disaster occurrence data, DDPM
**Granularity** หมู่บ้าน (village) · **Coverage** DDPM's historical holdings, exact period unstated in the catalog · **Format** Database
**Access** Restricted · **Status** Baseline-Draft, Unverified-Baseline
**Limitations** Reporting is one-way, from local administrative organizations up to province level, with no central ground-truthing. No UNDRR-aligned hazard taxonomy. A real starting point, not a from-scratch compilation, but these quality issues need handling before publication.
**Maintainer** UNKNOWN — pending investigation
**Note** REQ-001, REQ-011, and REQ-049 all draw on the same underlying DDPM records — gather this data once, use it for all three, rather than treating them as separate compilation tasks.

### DS-09 — Adaptation measures library
**Serves** REQ-060, REQ-061 · **Source** New. To be compiled from existing publications and new content
**Granularity** Per measure · **Coverage** To be established
**Limitations** Cost information will be incomplete. The design must keep measures findable when cost is unknown.

### DS-10 — *(removed)* — was External portal connections
REQ-071 became a curated links page rather than a live data connection (see 4.3), so this spec no longer applies. Kept struck from the sequence rather than renumbered, so other data-spec references stay stable.

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
| REQ-001 | 1.1 | History and trends of natural disaster events | Partial | Ready to build | DEL-12 | DDPM_2_1 |
| REQ-002 | 1.1 | IPCC risk framework and definitions | Full | Already covered | — | PUB-012, DAT-014 |
| REQ-003 | 1.1 | Physical risk and transition risk | Gap | Ready to build | DEL-7 | — |
| REQ-004 | 1.1 | National risk summary cards | Partial | Product surface | Investigation, App. B2 + DEL-13 | DCCE_3_1, DCCE_3_2, DCCE_3_3, DCCE_3_4, DCCE_3_5, DCCE_3_6, DCCE_3_7 |
| REQ-005 | 1.1 | Critical hotspots by sector and region | Full | Product surface | Investigation, App. B2 + DEL-13 | DAT-005 |
| REQ-006 | 1.1 | National adaptation plan summary | Full | Already covered | — | PUB-009, DAT-021, MED-025, MED-111, MED-112 |
| REQ-007 | 1.1 | Examples of high-value adaptation measures | Full | Already covered | — | MED-008, DAT-022 |
| REQ-008 | 1.2 | Search by administrative level | Partial | Ready to build | DEL-2 | DCCE_3_1–DCCE_3_6 (province level only) |
| REQ-009 | 1.2 | Map integration with administrative boundaries | Gap | Product surface | Investigation, App. B2 + DEL-13 | SYS-003, DAT-005 |
| REQ-010 | 1.2 | Quick-view point dashboard | Partial | Product surface | Investigation, App. B2 + DEL-13 | SYS-003 |
| REQ-011 | 2.1 | Historical extreme weather statistics | Partial | Ready to build | DEL-12 | DDPM_2_1 |
| REQ-012 | 2.1 | National macroeconomic loss and damage statistics | Partial | Loss and Damage | Loss and Damage entry, App. B | PUB-026, MED-050 |
| REQ-013 | 2.1 | National exposure trends | Gap | Product surface | Investigation, App. B2 + DEL-13 | DAT-005 |
| REQ-014 | 2.2 | Risk profiles for 77 provinces and local government | Partial | Ready to build | DEL-2 | DCCE_3_1–DCCE_3_6 (province level); A-BTR Section B (hotspot narrative) |
| REQ-015 | 2.2 | Risk profiles for the six priority sectors | Partial | Product surface | Investigation, App. B2 + DEL-13 | DAT-005, DAT-014 |
| REQ-016 | 2.3 | Status of the climate change act | Full | Already covered | — | PUB-003, PUB-004, MED-074, MED-075 |
| REQ-017 | 2.3 | Summary of supporting laws and policy instruments | Partial | Ready to build | DEL-8 | A-BTR Section A |
| REQ-018 | 2.3 | Avoided losses certification system | Gap | Awaiting decision | Brief E-1 | — |
| REQ-019 | 2.3 | Funding directory and cost-benefit guidance | Partial | Awaiting decision | Brief E-1 | MED-079, PUB-027, PUB-028, PUB-029 |
| REQ-020 | 2.3 | Budget allocation statistics and climate budget tagging | Gap | Awaiting decision | Brief E-1 | — |
| REQ-021 | 2.3 | Tracking of financial, technology and technical assistance | Partial | Awaiting decision | Brief E-1 | PUB-027, PUB-028, PUB-029, DAT-054, MED-147 |
| REQ-022 | 2.3 | Private sector finance mobilisation | Gap | Awaiting decision | Brief E-1 | — |
| REQ-023 | 2.3 | DCCE role as national focal point | Full | Already covered | — | PUB-025 |
| REQ-024 | 2.3 | National climate policy committee structure | Full | Already covered | — | DAT-013 |
| REQ-025 | 2.3 | National to local government coordination | Partial | Ready to build | DEL-8 | A-BTR Section A |
| REQ-026 | 2.3 | Participation channels and statistics | Full | Already covered | — | SYS-024, PUB-053, PUB-054, PUB-055 |
| REQ-027 | 2.4 | Local vulnerability and adaptive capacity indices | Partial | Ready to build | DEL-2 | MED-015 |
| REQ-028 | 2.4 | Integrated spatial risk map | Full | Product surface | Investigation, App. B2 + DEL-13 | SYS-003, DAT-005 |
| REQ-029 | 2.4 | ~~National data security guidance~~ | — | **Dropped — not relevant** | — | — |
| REQ-030 | 3.1 | Weather station observation data | Gap | Ready to build | DEL-3 | — |
| REQ-031 | 3.1 | Satellite observation data | Gap | Ready to build | DEL-3 | — |
| REQ-032 | 3.1 | Monitoring of global climate phenomena | Partial | Ready to build | DEL-5 | MED-105 |
| REQ-033 | 3.1 | Climatology and key climate variables | Partial | Ready to build | DEL-1 | DCCE_2_1, DCCE_2_2 |
| REQ-034 | 3.1 | Climate scenario usage guide | Gap | Awaiting decision | Brief E-2 | — |
| REQ-035 | 3.1 | Downscaled future projection library | Partial | Ready to build | DEL-5 | DCCE_2_11, DCCE_2_16, DCCE_2_17, DCCE_2_18, DCCE_2_19, clim-webbased.dcce.go.th (unregistered — needs a formal asset entry) |
| REQ-036 | 3.1 | National uncertainty management standard | Gap | Awaiting decision | Brief E-2 | — |
| REQ-037 | 3.1 | Case studies applying projections to planning | Gap | Ready to build | DEL-7 | — |
| REQ-038 | 3.2 | Definitions of core vulnerability concepts | Partial | Ready to build | DEL-6 | DAT-014, MED-015 |
| REQ-039 | 3.2 | Sector damage function library | Gap | Awaiting decision | Brief E-1 | — |
| REQ-040 | 3.2 | National risk assessment methodology | Partial | Ready to build | DEL-6 | PUB-012, MED-125 |
| REQ-041 | 3.2 | Sector risk results | Partial | Product surface | Investigation, App. B2 + DEL-13 | DAT-005, MED-004, MED-033 |
| REQ-042 | 3.2 | Slow-onset hazard statistics | Gap | Ready to build | DEL-4 | — |
| REQ-043 | 3.2 | Sea level rise along the coast | Partial | Ready to build | DEL-4 | MD_1_2; A-BTR Section B (interim rates) |
| REQ-044 | 3.2 | Land subsidence and salinity intrusion | Partial | Ready to build | DEL-4 | A-BTR Section B (subsidence only — salinity remains Gap) |
| REQ-045 | 3.2 | Coastal erosion index and beach area loss | Partial | Ready to build | DEL-4 | MED-127, MED-128, MED-129, MED-130, MED-133, MED-134, MED-135, MED-136, MED-137, DMCR_1_1, DMCR_4_1; A-BTR Section B (B-095) |
| REQ-046 | 3.2 | Multi-hazard impact chain diagram | Full | Already covered | — | PUB-012, MED-125, MED-048 |
| REQ-047 | 3.2 | Impact chain case studies, agriculture and urban | Partial | Ready to build | DEL-7 | MED-048 |
| REQ-048 | 3.2 | Loss and damage framework under the UNFCCC | Partial | Ready to build | DEL-6 | PUB-026 |
| REQ-049 | 3.2 | Historical loss dashboard | Partial | Loss and Damage | Loss and Damage entry, App. B | MED-050, DDPM_3_2, DDPM_2_3, RFD_1_2 |
| REQ-050 | 3.2 | Non-economic loss records | Partial | Loss and Damage | Loss and Damage entry, App. B | MED-108, MED-150 |
| REQ-051 | 3.2 | National risk and loss calculation manual | Partial | Loss and Damage | Loss and Damage entry, App. B | PUB-012, MED-125 |
| REQ-052 | 3.3 | Cost-benefit and avoided losses methodology | Gap | Awaiting decision | Brief E-1 | — |
| REQ-053 | 3.3 | Gender equality and social inclusion guidance | Partial | Ready to build | DEL-9 | A-BTR Section A |
| REQ-054 | 3.3 | Protection measures for vulnerable groups | Partial | Ready to build | DEL-9 | MED-002 |
| REQ-055 | 3.3 | Local wisdom and cultural heritage in adaptation | Gap | Ready to build | DEL-9 | — |
| REQ-056 | 3.3 | National adaptation strategy roadmap | Full | Already covered | — | PUB-009, DAT-021 |
| REQ-057 | 3.3 | Report on systemic barriers by sector | Partial | Ready to build | DEL-8 | A-BTR Section C |
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
| REQ-069 | 4.1 | Searchable data catalog and metadata | Full | Already covered, scope pending | — | SYS-002, PUB-051, PUB-052 |
| REQ-070 | 4.2 | Visualisation and analytics application | Partial | Product surface (launch) + engineering component deferred | DEL-13 (launch); engineering deferred to future project, Brief E-4 | SYS-003, DAT-005 (map only — not the engineering component) |
| REQ-071 | 4.3 | Curated links to external data portals | Gap | Ready to build | DEL-14 | — |
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
| `clim-webbased.dcce.go.th` | DCCE's downscaled climate projection platform | Data Product — **not yet in either canonical asset registry checked for this document; needs a formal registry entry** |
| `DDPM_2_1` | ข้อมูลเหตุการณ์ภัยพิบัติย้อนหลัง 10 ปี (10-year historical disaster occurrence data) | Dataset, DDPM |

---

# Appendix E — Deferred, and known limits

This document is bounded. What follows is what it does not cover and where it is uncertain, so no one builds a schedule on a false reading of it.

## The loss and damage specification does not exist yet

Four requirements — REQ-012, REQ-049, REQ-050, REQ-051 — depend on the loss and damage work package's own specification, which hasn't been written yet. **See the Loss and Damage entry in Appendix B** for demand, what exists, and the sequencing blocker. Three of these four are MUST-priority per sitemap v8, not optional — whoever writes that specification should start from these four, since they establish where the loss and damage product surfaces on the site and what each page needs from it.

## Administrative geography: DOPA boundaries are not LAO boundaries

Any sub-provincial content on this site (search, profiles) is organized on DOPA's province/district/sub-district hierarchy. Local Administrative Organization (LAO) jurisdiction — especially municipalities — does not nest cleanly inside that hierarchy. A municipality can span multiple tambons or straddle sub-district lines. อบจ. is province-wide and unaffected.

This is not a display problem to fix with better UI. The underlying risk-map input data is itself only disaggregated to DOPA administrative boundary, not to LAO geometry, so there's no existing figure to simply relabel. A real fix means either extracting content from provincial planning documents (Brief E-5, Appendix B) or geospatially re-aggregating the underlying data onto actual LAO polygons (Brief E-6, Appendix B) — two distinct undertakings, not resolved in this document. See REQ-008 and REQ-014 for where this bites directly, and DEL-2 (Appendix A).

## Reporting requirements are handled separately, and later

Thailand's adaptation reporting obligations produce a large body of requirements which have been analysed already and mapped to this same site map. They are deliberately not threaded through the pages here.

The reason is sequencing. Reporting sits at the data layer, and the sensible order is to settle the website content and the products first, then compare the finished design against the reporting requirements. That comparison will show how much of the reporting need the platform already meets, and where extending the data layer slightly would close the rest.

The linkage already exists in the underlying data. Fifty-one of the 72 addressable requirements carry a reporting tag (REQ-029 was dropped as not relevant — see below), so the comparison can be made mechanically when the time comes. **It is not part of this document and should not be attempted before the design settles.**

## REQ-029 was dropped

National data security guidance for research use (REQ-029, section 2.4) was reviewed and judged not relevant to this platform. It's removed from the live requirement count and the traceability matrix rather than carried forward as "already covered" — kept as a struck-through record in the traceability matrix (Appendix C) rather than deleted outright, so the exclusion itself stays visible.

## Two services have nowhere to live on the site

The demand analysis identified eight information services. Two of them have no page anywhere in the current site map.

**Multi-hazard early warning.** No section of the site corresponds to it. The only nearby content is the impact chain diagram in section 3.2, which is a static analytical artefact rather than the live localised alerting the service describes.

**Uncertainty governance.** Only thinly represented, through the uncertainty standard in section 3.1 and the technology readiness framework in section 3.4. Neither matches the full service, which would assess the readiness and appropriate use of every data product.

This is a limit of the site map rather than of this analysis. A requirement-by-requirement review cannot surface a service that has no page to sit on. **Both should be raised with whoever owns the site map structure.**

## Two requirements recorded as covered are not verified

REQ-005 and REQ-028 are recorded as fully covered, and both rest on the presence of an existing analytical product. Three other requirements resting on the same reasoning were moved back to gap or partial during the 11 August review.

They are handled here as product surfaces rather than as covered, and both are in the investigation list in Appendix B2, and in scope for DEL-13's hosting migration (Appendix A). **Do not treat either as finished until that investigation resolves them.**

## Almost all source data is flagged draft

Every DCCE dataset examined for this document carries the status `Baseline-Draft` and the flag `Unverified-Baseline`. None records a maintainer.

That applies to the composite risk indices, the climate grids, the projections, and the coastal and marine observations. It is not a problem with any single dataset, it is the current state of the catalog.

Several datasets are also restricted, meaning the climate grids, the projections, the sea level record and the erosion data. Publishing derived statistics from restricted sources needs an access decision that has not been made.

**Both issues need resolving before any of this data is presented as authoritative.** A page that shows a draft, unverified figure without saying so is worse than a page that shows nothing.

## One caution carried forward

An earlier cross-check moved eight requirements between categories on the strength of a 260-item extract of the dataset catalog. Only one of those eight was independently verified against DCCE's live catalog.

The other seven are real entries with their own identifiers, so they are not in doubt as to existence. But several carry restricted-access or draft flags that have not been confirmed against the live system. Any schedule built on those seven specific items carries that residual uncertainty.

The general lesson holds beyond those seven. The absence of an asset from an extract means the extract did not capture it, not that DCCE does not hold it.
