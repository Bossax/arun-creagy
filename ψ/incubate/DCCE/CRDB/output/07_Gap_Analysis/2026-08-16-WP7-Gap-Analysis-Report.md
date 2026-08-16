# What's Missing to Build Thailand's National Climate Adaptation Information Platform

**Date:** 16 August 2026

## Purpose

Thailand's planned national climate adaptation platform is meant to do two things at once: hold the country's climate and disaster data in a governed, trustworthy way, and present that data to the people who need it — planners, engineers, banks, policymakers — through a website. Those are genuinely different jobs. A website can look finished while the data behind it is thin, restricted, or doesn't exist at all; and well-governed data is worthless to a user who can't find or understand it. This report looks at both, for everything the platform is meant to do, and asks the same question throughout: what's missing, and why.

This is meant to be the one place to read that picture in full — not a summary that sends the reader chasing four other documents for the details. It replaces an earlier version of this same exercise, written in June, which covered the same ground with an older map of the country's data holdings and an earlier version of the platform's own service list. Everything in that June report has been re-checked here against the current data catalog and the current, more detailed set of services; where the two agree, that's noted; where the picture has changed, this report explains why.

The rest of this report is organized in six parts: what the country's underlying data currently looks like as a whole (Section 1); what's blocking each of the platform's planned services or reporting duties specifically, one at a time (Section 2); what's missing from the website itself, as content (Section 3); the same findings regrouped by what *kind* of gap they are, since that shapes what fixing each one actually takes (Section 4); the handful of decisions nobody has made yet that several of these gaps are actually waiting on (Section 5); and what this report deliberately did not try to answer (Section 6).

---

## Section 1 — The State of the Underlying Data

Thailand's central catalog for this platform currently lists **260 datasets**, drawn from across government. This section asks: as a body of raw material, is it ready to build a trustworthy climate information service on top of?

### Nothing in the catalog has been formally certified yet

Every single one of the 260 entries — all of them — is still recorded as a draft, not yet formally verified or endorsed. This isn't a comment on data quality; some of these datasets are genuinely solid, well-maintained records from agencies like the Thai Meteorological Department. It's a comment on process: there is currently no step in which a dataset gets checked, signed off, and marked as an official, citable reference. Nothing has been through it yet. A related, quieter finding: none of the 260 are marked as belonging to Thailand's "high-value dataset" open-data tier either — a classification question nobody has worked through for this catalog.

### Ownership is concentrated in a handful of agencies

Half of the catalog's holdings sit with just six organizations: the Thai Meteorological Department (37 datasets), DCCE itself (26), the Geo-Informatics and Space Technology Development Agency (17), the Department of Disaster Prevention and Mitigation (15), and the National Statistical Office and the Office of the National Economic and Social Development Council (14 each). This matters for two reasons: it means a small number of coordination relationships, if made to work well, would unlock a large share of the catalog — but it also means the platform's dependability rests heavily on a handful of external partners' own data practices, not DCCE's.

### The catalog leans toward hazard science and away from who and what is exposed

Broken down by subject: **72 datasets (28%) describe vulnerability** — who and what is at risk — and **68 (26%) describe exposure** — where people, buildings, and assets actually are. The rest is split between the physical climate signals that feed hazard models (49 datasets, 19%) and processed hazard products themselves like flood or drought maps (36, 14%), with a small remainder covering loss-and-damage records, composite risk indices, and a few other categories. Read together, hazard-related data of some kind — either the raw physical drivers or the finished hazard products — makes up roughly a third of the catalog, close to what the June review found, but split here across two more specific categories than before. What hasn't changed since June: the catalog is still noticeably thinner on the exposure and vulnerability side — the human and asset picture — than it looks once every hazard-related entry is added up.

### Most of the catalog isn't fine-grained enough for real project decisions

Almost half the catalog (47%) is recorded at province level — useful for national strategy, not for deciding where to build a drain or how high to set a seawall. Only 16% is recorded at a genuinely local grain — sub-district, municipality, village, or a specific monitoring point. A further **23% has no resolution recorded at all**, which is its own finding: for close to a quarter of the catalog, nobody currently knows how fine- or coarse-grained the data actually is without opening the file directly. That gap in the catalog's own record-keeping is arguably as much of a problem as the resolution numbers themselves.

### Most of the catalog is locked behind a request, not open for reuse

**82% of the catalog is marked Restricted** at the dataset level, and even the metadata describing what a dataset contains is Restricted for 68% of entries — meaning a user often can't even read a clear description of a dataset without first requesting access to it. This is the one number from the June review that holds up almost exactly against the current catalog.

*A caveat on data format:* the June review characterized much of the catalog as locked in PDF or spreadsheet form, hard to process automatically. The catalog's own format field tells a more structured-looking story — half of all entries are recorded as CSV, with PDF-only entries a small minority. It isn't clear from the catalog record alone whether this field describes what a dataset is actually delivered as today, or an intended/target format that hasn't been realized yet for every entry. This is worth a direct spot-check before anyone plans work around it — recorded as an open question in Section 5, not resolved here.

---

## Section 2 — What's Blocking Each Planned Service

The platform's service concept was built from real conversations with the government agencies, banks, engineers, and planners who'd actually use it. Nine distinct services or duties came out of that process. Each one is presented here on equal footing, in the order they were originally conceived — this section is a diagnosis of what's blocking each one, not a ranking of which matters most; deciding what to build first is a separate, later decision, not something this report tries to settle.

For two of these nine — the disaster loss-and-damage service, and Thailand's international climate reporting duty (its Biennial Transparency Report, "BTR") — a much more detailed check has already been done: every individual piece of information those two need was checked one by one against the catalog. The other seven have only been checked at the level of "what's the blocker," not signal by signal. That's simply because the detailed check hasn't been run for them yet, not a judgment that they matter less.

### Thailand's international climate reporting duty (the BTR)

Thailand has a standing obligation to report its climate adaptation progress internationally on a fixed cycle, using indicators that are supposed to be comparable across reporting rounds. Today, producing that report means several people manually pulling numbers from spreadsheets held by different agencies, without a shared way to check that "avoided losses" or "adaptation coverage" means the same thing to everyone contributing a number. The final figures in the report are difficult to trace back to their source once compiled. Four structural problems sit underneath this: gaps in the underlying data and shared definitions, poor coordination between the agencies who each hold a piece of the picture, limited resourcing for the compilation work itself, and no consistent way to monitor or report progress in the first place.

This is the one duty, alongside disaster loss-and-damage below, where the underlying information need was broken down into its individual pieces and checked one by one — 122 distinct pieces of information in total, everything from indicator definitions to specific figures the report is expected to cite. Of those 122, roughly half already have something real behind them in the catalog — a genuine dataset or figure that matches what's being asked for, sometimes needing further work to reach the standard the report requires, sometimes ready as-is. The other roughly half came back with nothing at all. Six further cases are genuinely ambiguous and need a person to make a judgment call, not more data-hunting: chief among them, whether a dataset DCCE already tracks under a different name is in fact the same "resilience index" the reporting framework refers to — nobody has confirmed either way yet.

Where the no-matches cluster is telling: it's rarely raw hazard data that's missing. It's the *calculated* figures the report actually needs to cite — return periods, scenario-specific probability estimates, the specific loss-and-damage assessment methodology the international reporting standard expects, financial stress-test results. The raw ingredients often exist somewhere in the catalog; the arithmetic and methodology that turns them into a reportable number does not.

### Recording the true cost of past disasters

Government relief and recovery spending today doesn't add up to a real picture of what disasters actually cost the country economically over time — only what was paid out, which isn't the same thing. Financial institutions want a validated national economic loss record they can build stress-test scenarios on; the same record could name the true value of past damage to justify future protective investment.

The good news here is real progress: national economic planners commissioned a university-led research effort to build exactly this kind of methodology, aligned with the international standards this kind of loss accounting is supposed to follow. That work, focused first on agricultural losses, is due to run through mid-2026, and has already produced a first estimate — cumulative disaster loss and damage of roughly ฿1.62 trillion between 2006 and 2024. This project has begun aligning its own approach to recording disaster losses with that emerging methodology, though it's worth being direct about the current status: it's a promising candidate for one part of what this service needs — a formal calculation manual — not a confirmed match yet. Someone still needs to check that connection properly rather than assume it (see Section 5).

With a plausible methodology finally in view, the blocker has shifted from "how do we calculate this" to "do we have the data to calculate it with." Disaster-agency records currently capture who was affected, how many people, and how much relief was paid — but not a monetary damage figure, not a sector-by-sector or provincial breakdown, and with a real ambiguity buried in the numbers: a recorded zero sometimes means nothing happened, and sometimes just means nobody recorded it. Getting the more detailed records released also raises a genuine privacy question, since some of them are household-level, and nobody yet knows how long that release process might take.

Of the six specific figures this service needs, three already have real data behind them somewhere in the catalog. The other three turned out not to be missing-data problems at all: they're requests for better *accuracy*, for adopting an international disclosure practice, and for financial stress-testing capability — process and methodology asks that no dataset alone could satisfy, however complete the catalog eventually gets.

Beyond the historical record itself, this service's design already names four specific things the finished product needs to include: a national economic loss database, a public-facing dashboard of that history, a record of losses that don't show up on a balance sheet at all (below), and the calculation manual discussed above. All four were flagged as blocked for the same reason — the methodology didn't exist yet to build them on. That's now closing, per the above, but three of the four are still waiting on the data-access questions in this section, and the manual is still waiting on the methodology-candidacy question in Section 5.

**One category inside this service deserves its own callout: losses that aren't financial at all** — harm to mental health, to biodiversity, and to cultural heritage. Of those three, only biodiversity currently has any supporting material behind it. The emerging national loss-and-damage methodology is economic-loss-focused and doesn't reach into this territory at all. Whether the finished service should scope down to biodiversity alone, or explicitly flag mental health and cultural heritage as future work, is a real open decision — see Section 5.

### A certified, trustworthy home for official climate data

Stakeholders' single most common complaint about Thailand's climate data landscape is fragmentation — no one, including DCCE internally, has ever had a complete picture of what the department itself holds, let alone the rest of government. There's no consistent way today to tell a dataset that's been checked and endorsed apart from one that hasn't.

The platform's planned certified-data catalog — deliberately a separate thing from DCCE's existing general-purpose open-data system, built specifically for the kind of trust and sourcing information a climate dataset needs — currently has only a starting seed of content, with its real scope still undecided. Section 1's finding that every catalog entry is still a draft is the sharpest version of this same problem: not one dataset examined so far has a named person or office responsible for keeping it accurate and current, and any agency can currently decline to share what it holds with no real recourse. A related, still-open decision: nobody has settled how these datasets should be classified for licensing purposes, which is a prerequisite for sharing many of them at all (Section 5).

### Risk information fine-grained enough to act on

Banks assessing loan risk and infrastructure planners both say the same thing: province-level risk scores are close to useless for a real decision. They need to know flood depth and duration for a specific plot of land, not a single number for an entire province.

Two separate structural problems sit behind this. First, DCCE's existing risk index is built with the province as its basic unit from the very start of the calculation — the number can't be taken apart and rebuilt at a finer grain after the fact, because the province-level boundary is baked into the method itself. Second, the index's underlying calculation multiplies and normalizes several inputs into one final score, which means the calculation can't be run in reverse to recover the finer-grained detail that went into it, even where that detail technically exists somewhere upstream. Fixes have been identified — more detail could be pulled out of the country's 77 provincial risk-reduction plans, and municipal boundary data could be reworked to support this — but both are waiting on a decision to actually resource that work, not on anything technical.

### Financial and budget justification for adaptation spending

Building infrastructure that can withstand a more volatile climate costs more than historical comparisons suggest it should, and government officials currently have no defensible way to explain that gap to auditors or budget reviewers.

This is, honestly, the single largest cluster of open questions found anywhere in this review. No accepted method exists yet for weighing the costs and benefits of a climate-resilience investment. No standard exists for tagging government spending as "climate-related" in the first place. No accepted way exists to calculate the value of losses that were *avoided* by making an investment — which is, awkwardly, often the main point being made to justify the investment. And no reference library exists connecting a given hazard to the physical damage it typically causes, which almost every one of these calculations would need as a building block. Separately, records of international climate finance and technology-transfer support show money moving, but essentially nothing about what capability or technology actually resulted from it. This service also needs direct research with the people who'd use it, since it isn't yet clear which specific figures different kinds of users would actually find convincing.

### Engineering-grade climate variables for infrastructure design

Engineering design standards — how much rainfall a drain is built to handle, how high a seawall needs to be — are still built on historical weather statistics that no longer reflect current climate volatility.

This one has been set aside deliberately for now, not attempted in the current phase. The specific technical variables this service needs — rainfall-intensity curves, runoff coefficients, peak flow rates, extreme temperature ranges, wind gust speeds, all adjusted for a changing climate — don't currently exist anywhere in DCCE's holdings, at any level of detail. DCCE's general risk index can't fill this gap either; it's built for broad hazard awareness, not the plot-level design curves an engineer actually needs. Closing it will take a sustained partnership with engineering specialists, not something a data-catalog fix can solve alone.

### Warnings that describe real-world impact, not just weather

Practitioners want a warning that tells them what to *do* — activate cooling shelters, estimate likely business disruption — not a bare number like a forecast temperature.

This is the most immature item on the list: the product doesn't exist in any form yet, and there's currently no page on the platform's site design that this service is even meant to occupy. The only related material found is a static diagram explaining, in general terms, how a hazard cascades into downstream impacts — informative, but not a working service. Where this content should actually live on the site is itself an unresolved question, since it's an operational tool, not a page of background reading, and the site's current structure doesn't have an obvious home for that distinction (see Section 3 and Section 5).

### Tracking whether adaptation policy is actually working

Policymakers need to see what's working, both to avoid wasting budget and to demonstrate real progress in international forums.

Unlike most of the items above, there's already a live system here: a national monitoring platform is currently collecting manually-entered progress data from eighteen government agencies across the national adaptation plan's six sectors. The open question isn't whether the data exists — it's whether this platform should build on that existing system, or replace it with something better designed, a decision nobody has made yet (see Section 5). Two smaller things remain genuinely unclear even about the existing system: whether it already has any built-in way of judging a technology's readiness level, and where individual project status is tracked at all — right now, that seems to live mostly in staff members' own knowledge, findable by asking someone directly rather than through any system. Worth flagging for scale: the existing platform currently holds only a couple hundred data rows a year, entered entirely by hand, with no automated data feed of any kind.

### Helping institutions use uncertain data with confidence

Banks and infrastructure planners are wary of using probabilistic climate projections for real decisions, worried about legal exposure if a projection turns out wrong — banks have been candid that they currently treat a flood *probability* map as though it were a flood *certainty* map, which is a real risk in itself.

This isn't a missing-data problem or a missing-page problem. It's a methodology and institutional-trust problem: uncertainty in a climate projection is still an unfamiliar concept to many of the people this service would serve, and building real institutional confidence in how to interpret it is a standalone piece of work, not something that can be folded into another service as a shared feature. A logical home for this content has been identified on the site, but nothing has been built there yet.

---

## Section 3 — What's Missing From the Website Itself

The platform's page-by-page site design is already finished and approved — that part of the work doesn't need repeating. What hadn't been checked until recently was whether the actual *content* each page promises already exists somewhere in DCCE's records, or still needs to be written or built from scratch.

That check broke the site design down into 73 distinct, specific content promises — not just "does this page have a topic," but every individual thing a page claims it will show, checked one by one against DCCE's full digital inventory (391 items: publications, datasets, live tools, and media) plus, for the more data-driven pages, the same 260-item dataset catalog discussed in Section 1.

The result: **21 of the 73 (29%) are genuinely ready to build from today.** A further **24 (33%) have some real material behind them, but are missing a specific piece the page promises** — and for a meaningful share of those, the "real material" that does exist is raw, access-restricted, or unverified data, not something a writer could simply pick up and publish. The remaining **28 (38%) have nothing at all** — no dataset, report, or existing page speaks to them.

A pattern worth naming, since it recurs in more than one place on the site: wherever a page promises information on financial support, technology transfer, *and* capacity-building together, DCCE's records reliably cover the financial piece well — but technology-transfer and capacity-building tracking are consistently missing, on more than one page independently. That's not a coincidence; it points to a real, structural blind spot in what DCCE currently tracks, not a one-off content gap. The same pattern shows up with raw climate science data — checking against publications alone made this look like a total blank, but the fuller check against the dataset catalog found that real (if raw, access-restricted, national-grid-resolution) climate data and future-projection datasets do exist behind several of these pages. They're not ready to publish as trend charts today, but they're not a from-scratch build either.

Two structural findings connect directly back to Section 2. First, most of what currently exists to support the site is narrative and explanatory material — background, policy summaries, case studies — which is in reasonably good shape overall. Pages that are meant to be live, data-driven features — dashboards, interactive maps, calculators — have almost nothing structured behind them yet, even on pages nominally "covered" by a document that discusses the topic in prose. Second, the impact-warning service described in Section 2 doesn't just lack a built product — it doesn't have a clear place on the current site structure to live, since it's meant to be operational rather than informational, and the site's current sections weren't designed with that distinction in mind.

---

## Section 4 — The Shape of These Gaps

Read one at a time, the findings in Sections 1–3 look like a long, unconnected list. Grouped by *kind*, a smaller number of real patterns emerge — and the kind of gap matters, because each kind needs a different fix. A missing dataset needs someone to go collect it; a missing decision needs someone to make a call; neither is solved by more analysis.

**Data that doesn't exist anywhere yet.** No dataset, no record, nothing to point to. This covers roughly half of the BTR's 122 information needs, all of the engineering design variables (rainfall-intensity curves, runoff coefficients, and the rest), the damage-relationship library the financial-justification service needs, and 28 of the website's 73 content promises.

**Data that exists but isn't ready to use.** This is the single largest category by volume, and the one Section 1's catalog statistics describe directly: 82% of the whole catalog is access-restricted, and literally every entry is still in unverified draft status. The same pattern shows up service by service — the disaster-loss records have the right subject but the wrong shape (no monetary breakdown, ambiguous zeros), the spatial-risk index has real data locked behind a calculation that can't be reversed, and a meaningful share of the website's 24 "partial" content gaps turn out, on inspection, to be real but raw, restricted, or unverified data rather than something ready to publish.

**No agreed method exists to turn the numbers into an answer.** The raw data may be sitting right there, but nobody has built or agreed on the calculation that turns it into what's actually needed. The financial-justification service is the starkest case — four separate missing methods at once (cost-benefit, avoided-loss, spending classification, damage relationships). The BTR's missing figures are mostly this too: return periods and scenario probabilities that need calculating, not collecting. The disaster-loss service's calculation manual sits right on the edge of this category — a strong candidate exists, just not yet confirmed.

**No decision has been made about ownership, classification, or which system to build on.** Not a technical gap at all. The certified-catalog's licensing-classification question, the policy-monitoring platform's build-versus-consolidate question, and the non-financial-loss scope question all belong here — each one is genuinely just waiting for someone to decide.

**The product itself hasn't been started.** Only one service is really in this category — the impact-based warning service has no build and no settled place on the site to live.

**Underneath most of the above, one structural theme repeats:** very little of this moves through a shared, automatic pipeline. It moves through one person asking another person, case by case. That's the connective thread between the catalog's 82% restricted-access rate, the BTR's missing derived figures, the certified-catalog's no-recourse problem when an agency declines to share, and the uncertain timeline for getting disaster records released. Even where the underlying data technically exists, turning it into something usable and timely still depends on an individual relationship, not a system.

---

## Section 5 — Decisions This Report Surfaces But Doesn't Make

A number of the gaps described above aren't waiting on more data collection or more analysis — they're waiting on a decision that only DCCE can make. Naming them clearly is this report's job; deciding them is not.

- **How to scope the non-financial-loss category.** Only biodiversity currently has real material behind it, out of the three categories (mental health, biodiversity, cultural heritage) the disaster-loss service is meant to cover. Should the near-term build scope down to biodiversity alone, with the other two explicitly named as future work?
- **Whether the emerging national loss methodology can serve as this platform's official calculation manual.** It's a strong-looking candidate, but nobody has formally confirmed the connection — someone needs to check it directly rather than assume it.
- **How datasets should be classified for licensing.** This is a prerequisite for sharing a meaningful share of the catalog at all, and nothing has been decided about how that classification should work.
- **Whether to build on the existing policy-monitoring platform or replace it.** The existing system works, after a fashion, but nobody has decided whether its current approach should be carried forward, rebuilt, or replaced outright.
- **Where the impact-warning service should live on the site**, given it doesn't fit the site's current informational-page structure.
- **Whether the data catalog's recorded format (mostly CSV) reflects what's actually delivered today**, or an intended format not yet realized for every entry — worth a direct spot-check before planning work that assumes the data is already structured.

---

## Section 6 — What This Report Doesn't Cover

This report deliberately leaves three things untouched:

- **A stocktake of DCCE's data *products*** (as opposed to raw datasets) — ownership, business metadata, and compliance classification for a shortlist of priority assets. No work has been done on this yet; it's a separate, still-unstarted piece of work, not folded into this report.
- **A formal maturity assessment of DCCE's overall data architecture** — how centralized or federated its governance is, how automated its metadata practices are, and similar questions, benchmarked against established data-platform models. An earlier plan for this report considered running that kind of assessment; on review, it didn't fit well, since DCCE's current state (largely manual coordination, no unified system yet) doesn't map cleanly onto a framework built to compare different *kinds* of already-built data platforms against each other. That question may still be worth answering in a future recommendations stage, framed narrowly, but it isn't part of this gap analysis.
- **Anything to do with how the eventual system gets built, integrated, or connected to other platforms** — those are questions for whoever builds this platform next, once the requirements in this report and its companion documents are finalized.

---

## Appendix — Internal Traceability

*(For project-internal use; not required reading for understanding the findings above.)*

- Catalog-level statistics (Section 1): recomputed directly from `data_catalog_v4.csv` (260 rows), superseding the same statistics as originally reported in the June 2026 report, which were built against an earlier catalog version (v3) with a different domain taxonomy.
- Service-level blockers (Section 2): drawn from the Service Business Narratives document (all 8 services + BTR pipeline section).
- BTR and disaster-loss-statistics signal-level detail (Section 2): drawn from the Data Domain Highlight technical draft (Track 1: 122 signals; Track 2: 6 signals).
- Disaster-loss-statistics build-requirement detail (Section 2): drawn from the Service 4 / Developer-Ready Design Requirements reconciliation (four requirements, three essential/one recommended, all blocked on methodology — now substantially resolved per the discussion above).
- Website content findings (Section 3): drawn from the WP4 Content-Source Gap Analysis Report (73 requirements: 21 full / 24 partial / 28 gap) — the finished, audience-facing version of that analysis, not its earlier internal working draft.
- This report supersedes the June 2026 Thai-language gap analysis in full. That earlier document is retained on disk, unmodified, as a historical record.
