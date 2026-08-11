# Designing the National Climate Adaptation Information Framework: From Rationale to Ready-to-Build Content

**Date:** 11 August 2026

## Executive Summary

The National Climate Adaptation Information Framework (NCAIF) is Thailand's planned national platform for climate-adaptation information — a single place where policymakers, technical specialists, and eventually the public can find the country's climate risk data, adaptation plans, and the tools to act on them. This report explains three things in sequence: why the platform is being built the way it is, how its page-by-page structure was reached and why that structure is the right one, and — now that the structure is fixed — how much of its planned content the Department of Climate Change and Environment (DCCE) can already build from today.

The short version of that last part: close to 30% of the platform's planned content is genuinely ready to source right now. A further third has real material behind it but is missing something specific the page promises, and just under 40% has nothing at all yet. None of that is a criticism of the design — it's the honest starting point for planning what gets built first, what gets negotiated for, and what gets written from scratch.

## Why NCAIF Exists

The case for NCAIF rests on two problems, at two different depths, that are easy to mistake for one problem.

The surface problem is a communication gap: Thailand doesn't currently have a central, modern place where the public and technical users alike can find climate-adaptation information in a usable form. Data and reports exist, but they're scattered across agency websites, PDFs, and systems that were never designed to talk to each other or to a general audience.

The deeper problem, underneath that, is a governance gap: there has never been a systematic accounting of what climate-adaptation data Thailand actually has, who owns each piece, and where the real gaps are. This matters because it changes what "fixing" the surface problem actually requires. A dashboard built directly on top of scattered, ungoverned data doesn't solve the communication problem — it just gives the fragmentation a nicer interface. Anyone who has seen a public data portal that looks polished but is quietly broken underneath — stale numbers, dead links, inconsistent figures for the same statistic in two different places — has seen this failure mode play out.

NCAIF is designed as two layers for exactly this reason: a data platform (the governance and inventory work underneath) and a web platform (the site itself, sitting on top of it). The web platform is what a visitor sees; the data platform is what keeps it honest. Skipping straight to the web platform is the shortcut that produces the broken-portal failure mode this project is trying to avoid.

One caveat worth stating plainly: the framing above draws on the project's current working rationale document, which is itself still a preliminary draft rather than a finished, agreed statement — worth treating as the clearest current thinking, not as settled fact. It also currently frames the platform's first phase around a narrower audience of policymakers and technical specialists, with a broader public-facing version coming later once the foundation is in place.

## From Data to Sitemap: How the Site's Structure Was Built

Getting from "we need a platform" to an actual page-by-page sitemap took several passes, each correcting something the last one got wrong.

**The starting inputs.** The design process began by looking outward before looking inward: benchmarking how other countries have built similar platforms — Japan's A-PLAT, Germany's Klimadapt, and the European Union's Climate-ADAPT portal — to understand what a mature climate-adaptation information site actually needs to do. That external view was then grounded in Thailand's own reality through stakeholder workshops, where the specific things different agencies and users actually need to do with this information were captured as concrete use cases — not "policymakers need climate data" in the abstract, but specific statements like "a named agency uses a named type of information to make a named decision, under a named constraint." Because a raw list of individual use cases (dozens of them, each narrow and agency-specific) is too fragmented to design a site around, they were clustered by what data they need, how they analyze it, and what they're trying to accomplish, into a smaller set of eight reusable services — things like a certified climate-data repository, high-resolution spatial risk analytics, and finance-and-budget decision support. Those eight services became the throughline that later versions of the sitemap were built and checked against.

**Building and re-testing the structure.** The sitemap itself went through eight full revisions. Early versions were closer to a generic climate-information-portal template; each subsequent version was tested against actual user personas — a policymaker, a scientist, a community co-producer — walked through realistic tasks, to find where the structure caused confusion or dead ends, and against DCCE's actual holdings, to check that the structure wasn't just clean on paper but buildable from what the department actually has. The current baseline is the result of that repeated testing, not a first draft.

**The principles the final structure follows.** Along the way, the design settled on five explicit rules that shaped the final shape of the site, and it's worth naming them because they explain *why* the structure looks the way it does, not just *what* it looks like:

- **Lead with the national mandate, not user silos.** The temptation with a multi-audience platform is to split the top-level navigation by user type — a section for policymakers, a section for scientists, a section for the public. Benchmarking against other countries' portals showed this consistently causes what's best described as "portal drift": users self-sort into their own silo and never see the parts of the story that live outside it. Instead, the top level of the site follows the national adaptation narrative itself — the shared story of the country's climate risk and its response to it — with different audiences finding their own entry points inside that shared structure rather than being separated from the start.
- **Never publish a risk claim without its context.** Sensitive material — a future flood-risk map, for instance — is never presented as a standalone number or image. Every such piece is structurally paired with the methodology and limitations behind it, and with the adaptation options it points toward, so a risk finding is never disconnected from either the science that produced it or the action it should prompt.
- **Add depth by layering, not by cutting.** Stakeholder feedback pulled in two directions at once — some wanted the site kept simple, others wanted full scientific depth preserved. Rather than resolving that by deleting content to please one side, the site handles it by sequencing: a simple, accessible entry point at the top level, with the full scientific detail available one click deeper for anyone who wants it. Nothing gets cut to make the homepage simpler.
- **Serve real needs directly, not through more sections.** Not every distinct need gets its own place in the navigation. Private-sector and ESG-reporting users, for example, are served through a homepage service card and direct, machine-readable data access — a functional answer to their need — rather than a dedicated section that would add navigational weight for a narrower audience.
- **Keep access differences a matter of process, not secrecy.** Some data is public and visual; some raw datasets require registration before download. That distinction is handled openly — visible, explained, and consistent — rather than by hiding gated content from view entirely.

**The resulting structure.** The current sitemap has five top-level sections, and each one earns its place and its position for a specific reason tied to the principles above:

1. **Home** gives every visitor — regardless of who they are — the simple, national-level entry point: an executive overview of the country's climate risk, plus a way to search by area. This is the "mandate-first" principle in its most direct form.
2. **The Policy Maker Information Center** comes next because it's the platform's primary institutional audience today: national climate situation, area and sector risk profiles, and the policy, legal, and financial tools this audience needs, presented at a level of simplicity appropriate to that role.
3. **The Adaptation Knowledge Cycle** is where the platform's full scientific depth lives — climate science, risk and vulnerability analysis, planning and implementation, and monitoring and evaluation, organized to follow the actual cycle of how adaptation work happens rather than being scattered by document type. This is the "layer, don't cut" principle: nothing here is a simplified version of anything upstream; it's the same information at full depth, one level down.
4. **Tools & Services** surfaces the platform's technical and interactive capabilities — the data catalog, visualization and analytics tools, and links out to other data sources — as a first-class destination rather than something buried inside other sections, directly answering the "serve real needs directly" principle for technical users.
5. **News & Contact** closes the structure with the platform's ongoing institutional presence — announcements, updates, and how to reach the people behind it.

That structure — agreed and treated as fixed for the current phase of work — is what the rest of this report checks against reality.

## Checking the Sitemap Against Reality: What DCCE Can Build From Today

With the sitemap's structure settled, the next question is a practical one: for everything that structure promises to show, does DCCE already have the material to build it, or does that material still need to be created?

Answering that meant checking every page's content against two things DCCE already has: its broader inventory of everything it publishes or operates digitally — publications, datasets, live systems, and media, numbering in the hundreds of items — and, for pages that need to be genuinely interactive or data-driven (dashboards, maps, indices), a separate, more focused catalog of DCCE's actual datasets.

**How the check worked.** The process ran in four passes, each one catching something the previous pass missed.

First, every page in the sitemap was broken down into what it specifically promises to show — not "this page covers adaptation finance" but every individual thing that page claims it will display, since a single line in the site design often bundles several distinct promises together (a page might promise financial tracking, technology-transfer tracking, and capacity-building tracking all in one sentence). That produced 73 specific, individually-checkable promises across the platform's 31 content-bearing pages.

Second, each of those 73 promises was checked against DCCE's broader inventory for anything genuinely relevant — not just topically adjacent, but actually usable as a starting point.

Third, a second look caught a real blind spot in the first pass: when a page bundles several promises together, it's easy for the whole page to get marked "covered" the moment just one of those promises finds a match, even if the rest have nothing behind them at all. A page for recording climate losses that aren't purely financial — explicitly naming harm to mental health, biodiversity, and cultural heritage as three separate things — had been marked covered because one document happened to discuss biodiversity. Mental health and cultural heritage had nothing behind them at all. Every page that looked "covered" on the first pass was individually re-checked against its exact wording to catch this.

Fourth, for the pages that need to be genuinely interactive or data-driven — as opposed to pages that just need a well-written explanation — a stricter check was run against DCCE's separate dataset catalog specifically, because a relevant published document isn't the same thing as real, structured data that could power a live chart or map.

**What that found.** Of the platform's 73 specific content promises: **21 (29%) are fully covered** — real material exists for everything the page asks for. **24 (33%) are partially covered** — real material exists, but something specific the page promises is still missing, or the material that exists is raw, access-restricted data rather than something ready to use as-is. **28 (38%) have nothing at all** — no document, dataset, or system in DCCE's holdings speaks to them.

That fourth pass is worth a closer look, because it produced the single most instructive correction in this whole exercise. One page — a national tracker meant to show adaptation progress by sector and province — had its supporting evidence checked against the narrower, more focused dataset catalog and initially came back looking unsupported, because the specific dataset it depended on wasn't in that narrower catalog's extract. Checked instead directly against DCCE's own live, current data system, that same dataset turned out to be real, actively maintained, and tied to Thailand's official climate reporting — the original assessment was right all along. The lesson that carries forward from this: a narrower, curated extract of DCCE's holdings missing something is not the same as DCCE not having it, and that distinction matters most exactly where a check is being most careful.

**Where the gaps concentrate.** Looking at the platform's content section by section rather than page by page, a few patterns stand out. The section on adaptation planning and available measures — cost-benefit guidance, protection measures for vulnerable groups, a searchable library of adaptation options — is the weakest area of the entire site by a wide margin, with the large majority of its content promises having nothing behind them at all. This is the "planning and doing" layer of adaptation work, and DCCE's current holdings are heavily weighted toward "understanding the risk" instead. The section on climate drivers — raw weather-station data, satellite observations, downscaled climate projections — is the only part of the site with no fully-covered content at all, and what partial coverage does exist there is raw, access-restricted data rather than anything close to publishable; this is a case where the real fix is a data-sharing arrangement with the agencies that hold the underlying data, not more writing. The section on risk, vulnerability, and loss-and-damage analysis — the platform's analytical core — carries the largest single concentration of partially-covered content, where the specific missing piece differs from item to item and needs to be planned for individually rather than treated as one uniform gap.

A separate, complementary check of DCCE's data holdings — looking at how ready its underlying datasets are to power any information service at all, independent of this specific sitemap — found a similar story from a different angle: roughly a fifth of DCCE's dataset catalog is genuinely ready to use in a live service today, with the rest limited by access friction, resolution, or a lack of standardization. The two checks measure different things — one asks whether a specific page can be built, the other asks whether the underlying data is service-ready at all — but they point in the same direction.

## What Comes Next: Getting to Launch-Ready Content

The starting point for this project's next phase should be an honest one: the gap analysis above is a map of where content is ready, where it needs work, and where it doesn't exist — not a claim that everything can be solved the same way.

**Close the loop on this analysis first.** The correction described above — where a page's real coverage only became clear after checking the right source instead of the narrower extract — was caught and fixed for one item. But that fourth pass reclassified eight items in total, and only one of them (the tracker, described above) has actually been re-verified against DCCE's live data system. The other seven are still resting on the narrower, curated extract that the tracker case just proved can be incomplete:

- A national risk-summary index, moved from "nothing exists" to "real but unverified data exists"
- Historical extreme-weather statistics, moved the same way
- Climate-variable data (temperature and rainfall trends), moved the same way
- Downscaled future-climate projections, moved the same way
- Sea-level rise data, moved the same way
- A coastal-erosion index, where the supporting evidence got stronger but wasn't independently re-checked against the live system
- A loss-and-damage dashboard, where the supporting evidence got stronger the same way

None of these are necessarily wrong — the tracker case could just as easily have gone the other way, and it didn't. But the honest position is that this analysis found one blind spot in its own method and fixed it in exactly one place. The same fifteen-minute check that resolved the tracker case — going to DCCE's live data system directly rather than trusting the narrower extract — should be repeated for these seven before anyone treats this report's numbers as the final word on what's build-ready. Until that's done, these seven items carry a bit more uncertainty than the rest of this report's findings, and that's worth knowing before committing a build schedule to them.

**Prioritize content work by what kind of gap it actually is, not just by count.** The weakest section — adaptation planning and measures — needs a dedicated content-production effort, and likely one that pulls in DCCE program staff directly rather than anything findable by searching an inventory, since it covers things like ongoing-project status and budget readiness that live in people's heads, not in documents. The climate-drivers section needs the opposite kind of effort entirely: formal data-access arrangements with the Meteorological Department, the Marine Department, and whoever holds the relevant modeling data, since no amount of writing produces a dataset that doesn't exist yet. The risk-and-vulnerability section needs neither of those as much as it needs careful, item-by-item planning, since its gaps are specific and varied rather than uniform.

**Separate genuinely new capabilities from content gaps.** A small number of items on the sitemap aren't missing content at all — they're missing operational capabilities DCCE doesn't currently have, like a live connection to external data portals, or a structured channel for user feedback on data quality. Budgeting and scheduling these as if they were content-writing tasks would badly underestimate what they actually require; they belong on a separate technical-build track.

**Feed this into the work already planned.** Detailed functional specifications are already being scoped for the platform's two current priority use cases, which will translate some of this report's findings into buildable detail. The recommendations and roadmap work that follows this phase is the right place to formally name the recurring gaps this analysis surfaced — technology-transfer tracking, budget tagging, cost-benefit methodology — as specific deferred work items rather than leaving them as loose findings. And the project's final packaging phase is where all of this gets cross-checked one more time against how the platform's story gets communicated to DCCE's leadership.

**The honest bottleneck.** Not every gap in this report closes with more writing. A meaningful share of what's currently missing depends on decisions and negotiations that sit with DCCE, not with this project's documentation work — data-sharing agreements with other agencies, and internal governance decisions about how the platform's data gets maintained going forward. Being clear about that distinction now is worth more than a report that implies content production alone will get this platform to launch-ready.

---

## Appendix: Source Documents

This report synthesizes findings already documented in detail elsewhere in the project. For anyone who needs to trace a specific claim back to its source:

- **Business rationale**: `01_Business_Objective_Platform_Rationale/2026-08-06-Business-Objective-Platform-Rationale.md`
- **Sitemap design principles**: `04_Sitemap/2026-06-04-NCAIF-Sitemap-v5-Design-Decisions.md`
- **Current sitemap baseline**: `04_Sitemap/NCAIF_Detailed_Sitemap_v8.md`
- **Use-case-to-service clustering**: `06_Use_Case_Demand_Analysis/2026-06-12_use-cases-to-services-conceptual-model.md` and `2026-06-15_NCAIF-Service-Enrichment-Roadmap.md`
- **Content-source gap analysis (narrative report)**: `04_Sitemap/2026-08-10-WP4-Content-Source-Gap-Analysis-Report.md`
- **Content-source gap analysis (full page-by-page detail)**: `04_Sitemap/2026-08-11-WP4-Node-Level-Deep-Dives.md` and `04_Sitemap/2026-08-10-WP4-Content-Source-Gap-Analysis.csv`
- **Complementary data-supply-readiness analysis**: `07_Gap_Analysis/รายงานการวิเคราะห์ช่องว่างข้อมูลเชิงโครงสร้างและประเด็นการดำเนินงานเชิงยุทธศาสตร์_v5.0.md`
- **Forward-looking work plan**: `plans/2026-08-06-crdb-final-sprint-implementation-plan.md`

This report is a plain draft, not a sealed deliverable — it has not been committed to the project's ledgers.
