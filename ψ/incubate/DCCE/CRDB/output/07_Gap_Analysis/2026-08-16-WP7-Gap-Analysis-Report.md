# Gap Analysis: Data Demand and Data Supply for Thailand's National Climate Adaptation Information Platform

**Date:** 16 August 2026

## 1. Purpose and Scope

This report compares what users need from Thailand's climate adaptation data system against what the country currently holds, and describes the distance between the two.

It covers three layers together: the national dataset catalog that supplies the platform, the nine information services and reporting duties the platform is being designed to deliver, and the content the platform's website will need to publish. It is intended as the single place to read that picture in full.

The analysis extends an earlier version of this work by refreshing every quantitative finding against the current dataset catalog, adding two reporting duties that were defined after the first version was written, and adding the website content layer. The gap numbering used here is carried forward unchanged from that earlier version, so a reader familiar with it can follow the same references.

Two of the platform's layers are worth separating throughout. The **data platform** is the infrastructure that stores, moves, and governs data. The **web platform** is what people see and interact with. Sections 3 to 5 concern the data platform. Section 6 concerns the web platform. A well-built website drawing on ungoverned sources will present fragmentation faithfully, so both layers need to hold.

---

## 2. What Users Need

The demand side of this analysis comes from interviews, a stakeholder workshop, and a survey of how government and private organizations currently work with climate data.

A consistent theme ran through all of it. Users want data they can put directly to work inside their own mandate, in the form and vocabulary their organization already uses. Local government wants sub-district and municipal figures that connect to local development planning and budget requests. Financial institutions want asset-level probability of loss they can price into investment risk. Transport and infrastructure agencies want variables already converted into engineering design criteria. Policy and budget offices want a central reference dataset with enough standing to cite in a funding decision.

Grouped, that demand takes seven forms.

**Central reference baselines and indicators.** A single authoritative set of figures that different organizations can cite and be understood to mean the same thing.

**Spatial data fine enough to act on.** Sub-district, municipal, or individual asset grain, rather than a single value covering a whole province.

**Data and methods for calculating sector impact.** Not only the hazard information, but the means of converting it into an impact figure for agriculture, health, infrastructure, or the economy.

**Access that connects to working systems.** Data that arrives through a repeatable connection into the analysis a team already runs, rather than through a document request each time it is needed.

**A standard way of communicating uncertainty.** Enough context accompanying a projection that a reader can tell how confident it is and where it stops being appropriate to use.

Two further demands were defined after the original synthesis and are carried here for the first time.

**Traceable figures for international climate reporting.** Thailand reports adaptation progress on a fixed international cycle using indicators meant to stay comparable between rounds. That requires figures whose source can be traced after compilation.

**A validated national record of disaster loss.** A record of what past disasters actually cost, separate from what was paid out in relief, suitable for baselining models and for financial stress testing.

---

## 3. What Exists Today

The national catalog assembled for this platform holds **260 datasets** drawn from across government.

Ownership concentrates in a small number of organizations. The Thai Meteorological Department holds 37 datasets, DCCE itself 26, the Geo-Informatics and Space Technology Development Agency 17, the Department of Disaster Prevention and Mitigation 15, and the National Statistical Office and the Office of the National Economic and Social Development Council 14 each. Roughly half the catalog sits with those six. A working relationship with each would reach a large share of the whole.

By subject, the catalog holds 72 vulnerability datasets, 68 exposure datasets, 49 covering the physical climate signals that drive hazard models, and 36 finished hazard products such as flood and drought maps. The remainder covers loss and damage records, composite indices, risk metrics, and spatial reference layers.

Around 17% of the catalog is openly published. The rest is available on request. About half the catalog is recorded as CSV, with raster, vector, and document formats making up most of the balance.

On resolution, 122 datasets are held at province level, 41 at a local grain of sub-district, municipality, village, or individual monitoring point, and 36 as gridded surfaces. For 59 datasets — close to a quarter of the catalog — resolution is not recorded, so the grain is not knowable from the catalog alone.

All 260 entries currently carry draft status and none has completed a verification step, because that step does not yet exist as a process. This says nothing about the quality of the underlying data, much of which is sound; it describes a stage the catalog has not yet reached.

One recent addition changes the resolution picture materially. DCCE's Climate Change Research Center has produced statistically downscaled climate data at **5km resolution**, covering precipitation and maximum, minimum, and mean temperature, under both the SSP2-4.5 and SSP5-8.5 scenarios. This is the starting point from which finer-grained hazard and risk information can be derived, and it is a substantially better foundation than the 25km grid available when this analysis was first run.

---

## 4. The Gaps

Eleven gaps separate the demand in Section 2 from the supply in Section 3. Numbering for the first eight is carried forward from the earlier version of this analysis.

**Gap 1 — Balance between hazard, exposure, and vulnerability data.** The catalog describes hazards well, drawing on climate models, meteorological records, and satellite observation. Information describing the people, assets, and services that hazards affect is thinner and more scattered, particularly for infrastructure, economic assets, and social vulnerability. Work that requires several of these layers at once — identifying which vulnerable groups sit inside a risk area, ranking adaptation projects, assessing risk across an asset portfolio — needs that side of the catalog to grow. Even where hazard data itself is strong, it is mostly delivered as a single deterministic map or figure. Probabilistic detail, the range a projection covers and the assumptions a model rests on, is rarely exposed alongside it, which limits how safely that hazard information can be reused in someone else's risk calculation.

**Gap 2 — Spatial resolution.** Province-level figures support national strategy. Deciding where to build a drain or how high to set a seawall needs sub-district or asset grain. The new 5km downscaled climate data closes much of this at the climate-driver end. The environmental layers needed alongside it — digital elevation models, stream and sub-basin routing — still come from several sources at resolutions that do not align with each other, and population and asset data broken down by social and economic category is not yet available at a matching grain.

**Gap 3 — Compatibility between spatial units.** Hazard data arrives as grids. Population and social data arrives bounded by administrative areas. Asset data arrives as points and lines. Some economic data arrives at province or regional level. Without an agreed method for relating these to one another, each user converts and overlays them independently, which costs time, introduces error, and leaves results from different organizations that cannot be compared. The practical result is that no single scale can be served reliably. A risk figure at a given resolution needs its hazard, exposure, and vulnerability inputs all available at that resolution together, and that alignment does not yet exist for most combinations.

**Gap 4 — Access.** Most of the catalog is available on request rather than published. Three things drive this: internal rules at data-holding agencies with no systematic cross-ministry sharing policy; personal data protection requirements, which are sometimes read as preventing release of an entire dataset when aggregation would resolve the concern; and limited budget and technical staffing for building and maintaining automated data connections. The effect is sharpest on work that needs current information — impact-based warning, periodic financial analysis, risk assessment on a refresh cycle, and policy monitoring drawing on many sources.

**Gap 5 — Metadata standards.** There is not yet an agreed national standard covering the descriptive information that travels with a dataset: discovery metadata for finding it, technical metadata for using it, a data dictionary for interpreting its fields, and lineage for tracing where it came from. Update frequency and expected lag between an event and its appearance in the data are also generally unstated. Without these, a user cannot judge whether a dataset is suitable before relying on it. Which of these fields matter most for a given product's credibility is not yet settled either, and until it is named as an official, enforced requirement rather than a general expectation, metadata quality will keep varying by how much a given data holder chooses to provide.

**Gap 6 — Format of products and services.** A finished information product delivers less than it could when it can only be viewed. A crop suitability map published solely through a web interface can be read on screen but cannot be taken as input to further analysis. This matters most for the work that treats a product as an ingredient: financial risk assessment, conversion of climate data into engineering variables, macroeconomic impact analysis, infrastructure risk modelling, and warning systems that draw several sources together. This overlaps with Gap 4. A data owner who would allow a document or a map to be viewed is often unwilling to release the same information as a downloadable analytical file, because a file that leaves their control is a file whose downstream use they can no longer answer for.

**Gap 7 — Time coverage and delay.** Different uses need different time horizons. Comparing risk against a stable reference needs 10 to 20 years of history. Planning national infrastructure needs projections 20 to 50 years out. Warning systems need information arriving close to real time. The catalog does not yet cover all three consistently.

**Gap 8 — Risk methodology and data selection.** Thailand does not yet have a national approach to defining risk or a catalog of risk methods matched to the purposes they suit. Without that guidance, data can be applied outside the context it was built for — a single-scenario long-range projection used directly as an engineering design value without accounting for model uncertainty, for instance, where comparing relative risk between areas would be better served by an index-based map than by asset-level financial loss statistics. This carries a real risk of maladaptation.

**Gap 9 — Certification and stewardship.** No step currently exists in which a dataset is checked, endorsed, and marked as an official reference, which is why all 260 entries sit in draft. No dataset yet has a named person or office responsible for keeping it current, and there is no agreed process when a holding agency declines to share.

**Gap 10 — Calculation methods that do not yet exist.** Distinct from Gap 8, which concerns choosing among available methods, several services need a method that has not been built. There is no agreed approach to weighing costs against benefits for a resilience investment, no standard for classifying government spending as climate-related, no accepted way to value losses avoided by an investment, and no reference library relating a hazard to the damage it typically causes. National economic planners have commissioned a university-led effort to build an economic loss and damage methodology aligned to international practice, which addresses part of this.

**Gap 11 — Decisions awaiting a determination.** Several gaps close on a decision rather than on new data or analysis. These are listed in Section 8.

---

## 5. How the Gaps Affect Each Service

The platform's nine services and reporting duties each meet a different combination of these gaps.

| Service | Gaps involved |
| :--- | :--- |
| 1. Certified climate data repository and official endorsement | 4, 5, 6, 9 |
| 2. High-resolution spatial risk analysis | 1, 2, 3 |
| 3. Finance and budget decision support | 6, 7, 8, 10 |
| 4. Historical loss and damage assessment | 1, 3, 7, 10 |
| 5. Engineering design variables | 2, 7, 8, 10 |
| 6. Multi-hazard impact-based warning | 4, 6, 7 |
| 7. Adaptation policy monitoring and evaluation | 1, 3, 5, 11 |
| 8. Uncertainty management standards | 5, 8 |
| 9. International climate reporting pipeline | 5, 10 |

### Service 1 — Certified climate data repository and official endorsement

Fragmentation is the most frequently raised difficulty across every stakeholder group, and there is currently no consistent way to distinguish a checked dataset from an unchecked one. The platform's certified catalog, planned as a separate system from DCCE's general open data service and built for the sourcing and trust information climate data needs, holds a starting seed of content with its full scope still to be set. Gap 9 is the central one here. How datasets should be classified for licensing remains open, and that classification is a prerequisite for sharing a meaningful share of the catalog.

### Service 2 — High-resolution spatial risk analysis

Banks assessing loan exposure and infrastructure planners both need flood depth and duration for a specific site rather than a single province-wide value. Two structural properties of the current risk index stand in the way. Its unit of analysis is fixed at province before the calculation begins, so a finer result cannot be recovered afterward. Its inputs are multiplied and normalized into one score, which cannot be worked backward to the detail that went into it. Two routes forward have been identified — extracting detail from the country's 77 provincial risk reduction plans, and reworking municipal boundary data — both awaiting a decision to resource them.

This service shows how gaps compound. Even with rainfall projections in hand, if the model is coarse relative to the decision (Gap 2) and stored on a grid that cuts across administrative boundaries (Gap 3), it cannot be combined with community-level vulnerability data (Gap 1), and local risk mapping does not become possible. The new 5km downscaled data materially improves the first of those three.

### Service 3 — Finance and budget decision support

Climate-resilient infrastructure costs more than historical comparisons suggest, and officials need a defensible way to explain that difference to auditors and budget reviewers. This service depends on Gap 10 more than any other: it needs a cost-benefit method, a spending classification standard, an avoided-loss calculation, and a damage function library, none of which exist yet. Records of international climate finance and technology transfer show funds moving but little about the resulting capability. Direct research with intended users will be needed, since which figures would actually persuade different audiences is not yet established.

### Service 4 — Historical loss and damage assessment

Relief and recovery spending records what was paid, which is a different quantity from what disasters cost the economy. The commissioned national methodology noted under Gap 10 addresses the method side; focused initially on agricultural losses and running through mid-2026, it has produced a first estimate of roughly ฿1.62 trillion in cumulative loss and damage between 2006 and 2024. Whether it can also serve as the platform's official calculation manual is a strong possibility that has not been confirmed.

With the method in view, the remaining distance is data. Disaster agency records capture who was affected and what relief was paid, without a monetary damage figure or a breakdown by sector and province, and with recorded zeros that may mean either no event or no collection. Releasing the more detailed records raises a personal data question, since some are household-level, and the timeline for that release is not yet known.

Of the six specific figures this service needs, three have supporting data in the catalog. The other three are requests for improved accuracy, for adopting an international disclosure practice, and for stress-testing capability — needs that no dataset alone would meet.

Four elements of the finished product were recorded as blocked pending this methodology: a national economic loss database, a public dashboard of that history, a record of losses that do not appear on a balance sheet, and the calculation manual. Of the three loss categories in that third element — mental health, biodiversity, and cultural heritage — only biodiversity currently has supporting material, and the commissioned economic methodology does not extend to any of them.

### Service 5 — Engineering design variables

Design standards still rest on historical statistics that no longer describe current conditions. The variables this service needs — rainfall intensity-duration-frequency curves adjusted for climate scenario, runoff coefficients, peak flow, temperature extremes, wind gust — are not yet held anywhere, at any grain. The general risk index serves hazard awareness rather than plot-level design, so it cannot substitute. This service has been set aside for the current phase; closing it will take a sustained working relationship with engineering specialists alongside the data work.

### Service 6 — Multi-hazard impact-based warning

Practitioners want a warning that states what to do — open cooling centers, estimate likely business interruption — rather than a forecast value alone. This service is the least developed: no product exists yet, and the only related material is a static diagram showing how hazards cascade into impacts. Gap 4 and Gap 7 are decisive here, since a warning service needs automated connections to sensors, models, and operating agencies on a timescale the current request-based access cannot support. Where this belongs on the site is also unsettled, since it is an operational tool rather than a page of reference material.

### Service 7 — Adaptation policy monitoring and evaluation

A national monitoring platform already operates here, collecting manually entered progress data from eighteen agencies across the national plan's six sectors, holding a few hundred rows a year with no automated feed. The open question is whether this platform builds on that system or replaces it, which is a Gap 11 decision. Two details about the existing system remain unclear: whether it already assesses technology readiness, and where individual project status is held, which currently appears to rest on staff knowledge. Comparing results across agencies is additionally limited by scattered vulnerability data on differing spatial units (Gaps 1 and 3) and by unstated update cycles (Gap 5).

### Service 8 — Uncertainty management standards

Financial institutions and infrastructure planners are cautious about using probabilistic projections in decisions that carry liability, and some currently treat a flood probability map as a certainty map. This is a methodology and confidence question rather than a data question. Uncertainty in a projection remains an unfamiliar concept for many intended users, and building shared institutional understanding of how to read it is work in its own right rather than a feature of another service. A place for this content has been identified on the site.

### Service 9 — International climate reporting pipeline

Producing Thailand's international adaptation report currently means compiling figures by hand from spreadsheets held across several agencies, without a shared definition of terms like avoided loss or adaptation coverage, and with final figures difficult to trace back to source. Four structural conditions sit underneath: gaps in underlying data and shared definitions, coordination across the agencies holding each piece, resourcing for the compilation work, and a consistent means of monitoring progress.

The information this report needs was broken into 122 individual items and checked against the catalog. Roughly half have supporting data, some ready and some needing further work. Roughly half return nothing. Six items need a judgment rather than a search, the most consequential being whether a dataset DCCE already maintains is the same measure the reporting framework refers to under a different name.

Where the unmatched items concentrate is instructive. Raw hazard data is rarely the missing piece. What is missing is the calculated figure the report cites — return periods, scenario-specific probabilities, the loss and damage assessment methodology international reporting expects, financial stress test results. The ingredients are often present; the method that turns them into a reportable number is Gap 10.

---

## 6. Website Content

The platform's page-by-page design is complete and approved. Separately, each page's content promises were checked against DCCE's full digital holdings — 391 publications, datasets, live tools, and media items — and, for pages needing structured data, against the 260-dataset catalog.

That check identified 73 distinct content promises. **21 (29%) have everything they need available now.** **24 (33%) have real supporting material with a specific named element still to source** — and for several, the available material is raw, restricted, or unverified data rather than publishable content. **28 (38%) have no current source.**

Two patterns recur. Wherever a page promises financial support, technology transfer, and capacity building together, the financial material is reliably present and the other two are not — on several pages independently, which points to what is tracked rather than to how any single page was written. And for raw climate science content, checking publications alone suggested a complete absence, while the fuller check against the dataset catalog found historical climate grids and downscaled projections that do exist, as restricted national-grid raw data rather than as the finished trend figures the pages describe.

Two findings connect back to Section 5. Narrative and explanatory pages — background, policy summaries, case studies — are in reasonable shape overall. Pages designed as live data features such as dashboards, maps, and calculators have little structured material behind them, including pages counted as covered by a document discussing the topic in prose. This is Gap 6 appearing on the web layer. And the impact-based warning service needs a placement decision on the site as well as a build.

---

## 7. The Institutional Gap

Read together, these eleven gaps point to something beyond the volume of data held. Very little currently moves through a shared, repeatable connection. It moves through one person asking another, case by case. That thread runs through the share of the catalog available only on request, the absence of a recourse when an agency declines to share, the uncertain timeline for releasing disaster records, and the manual compilation behind the international report.

What the workshop and interviews describe is a coordinating role that no organization currently holds — between the agencies producing data, the teams building services on it, and the people using it at the end.

Stakeholders were consistent that they do not expect DCCE simply to produce more data or to operate more storage. They expect DCCE to take up three roles:

- **Standard setter**, defining the technical norms — metadata standards, risk methodology — that let data from different sources work together.
- **Data authenticator**, providing the endorsement step that gives a dataset standing to be cited in a funding decision or a policy.
- **Science-to-decision facilitator**, connecting scientific data to the specialist knowledge needed to turn it into something an engineer, a bank, or a local planner can act on.

Closing these gaps rests on that role as much as on the data work itself.

---

## 8. Decisions Awaiting a Determination

These gaps close on a decision rather than on further analysis.

- **Scope of the non-financial loss record.** Of mental health, biodiversity, and cultural heritage, only biodiversity currently has supporting material. Whether the near-term build covers biodiversity alone, with the other two named as later work, is open.
- **Standing of the commissioned loss methodology as the official calculation manual.** A strong candidate that has not been confirmed.
- **Dataset classification for licensing.** A prerequisite for sharing a substantial share of the catalog.
- **Whether to build on or replace the existing policy monitoring platform.**
- **Placement of the impact-based warning service on the site**, given it is operational rather than informational.
- **Whether the catalog's recorded formats describe current delivery or an intended target**, which is worth confirming before planning work that assumes structured data.

---

## 9. Outside the Scope of This Report

- **A stocktake of DCCE's data products** — ownership, business metadata, and compliance classification for a shortlist of priority assets. This remains to be done.
- **A maturity assessment of DCCE's overall data architecture**, benchmarked against established data platform models. This suits a later stage, once the platform has a form to assess.
- **How the system is built, integrated, and connected to other platforms.** These are questions for the implementation phase, once the requirements in this report and its companion documents are settled.

---

## Appendix — Internal Traceability

*(Project-internal reference; not required for the findings above.)*

- **Structure.** Follows the analytical spine of the submitted draft `5.3.8` (demand → supply → numbered gaps → per-service application → institutional conclusion), extended with the website layer, the two later use cases, and the decisions and scope sections. Gap numbering 1–8 preserved from `5.3.8`; gaps 9–11 added here.
- **Section 3 statistics.** Recomputed from `data_catalog_v4.csv` (260 rows) using `cdm_sub_domain`, `spatial_resolution`, `access_rights_dataset`, `endorsement_status`, and `validation_flag`. Supersedes the equivalent figures in D-044, which were computed against catalog v3 under a different domain taxonomy. Resolution figures differ from D-044's 70%/26% split because v4 records 23% of entries with resolution unstated.
- **5km downscaling detail** (Section 3, Gap 2): from `5.3.8`.
- **Gaps 1–8** (Section 4): carried from `5.3.8`, refreshed against v4 figures. Gaps 9–11 derived from WP2, WP6, and the v4 recount.
- **Service blockers** (Section 5): from the WP6 Service Business Narratives (D-071), all 8 services plus the BTR pipeline section. Service-to-gap mapping in the Section 5 table extends `5.3.8`'s equivalent table to nine rows.
- **Service 9 signal detail** (122 items) and **Service 4 signal detail** (6 items): from the WP2 Data Domain Highlight draft.
- **Service 4 build-requirement detail** (four elements: REQ-012, REQ-049, REQ-050, REQ-051): from the Service 4 / DRD reconciliation.
- **Section 6**: from `2026-08-10-WP4-Content-Source-Gap-Analysis-Report.md` (D-061), the finished audience-facing version — 21/24/28 of 73 — not the earlier working draft, which carries superseded totals.
- **Section 7**: three institutional roles carried from `5.3.8`'s conclusion.
- **Supersession.** This report supersedes D-044 (`รายงานการวิเคราะห์ช่องว่างข้อมูลและข้อเสนอแนะเชิงนโยบาย_v5.0.md`) in full, and supersedes `5.3.8` as the current gap analysis. Both are retained on disk unmodified.
