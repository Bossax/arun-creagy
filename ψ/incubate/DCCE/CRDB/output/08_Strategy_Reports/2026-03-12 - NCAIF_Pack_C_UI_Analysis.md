# Pack C Only Analysis — UI and Information Architecture Contribution to NCAIF

## Purpose

Isolate what **Pack C alone** contributes to NCAIF refinement, without mixing in product-reality constraints from Pack A or TOR/interim-report constraints from Pack B.

Primary source:
- [`ψ/incubate/DCCE/CRDB/inbox_source/2026-03-12 - User Experience Design Principles for National Climate Change Adaptation Information Services.md`](ψ/incubate/DCCE/CRDB/inbox_source/2026-03-12%20-%20User%20Experience%20Design%20Principles%20for%20National%20Climate%20Change%20Adaptation%20Information%20Services.md)
## Scope of this report

This report answers only:
1. What UI and IA principles does Pack C recommend
2. What kinds of navigation and page structures does Pack C favor
3. What anti-patterns does Pack C warn against
4. How Pack C should shape the presentation layer of NCAIF

This report does **not** decide:
- whether a feature is technically real in Phase 1
- whether a feature is inside TOR scope
- whether DCCE already has the required data or tools

Those questions belong to Pack A and Pack B.

## Executive summary

Pack C pushes NCAIF toward a **narrative, user-centered, low-friction interface architecture**. Its strongest contribution is not the invention of new content categories, but the **reorganization of how users discover and move through them**. This direction is consistent with the deep-research note’s synthesis of climate-service UX, especially around information scent, narrative workflows, and user-interface platforms (Climate-ADAPT, n.d.; World Bank, n.d.; World Meteorological Organization, n.d.).

The most important Pack C message is:
> a national climate adaptation platform should not behave like an internal government website or a raw data repository. It should behave like a guided public-facing decision-support environment with strong information scent, shallow top-level navigation, progressive disclosure, and clear separation between data-discovery and task-oriented tools.

## Core contributions from Pack C
### 1. Strong information scent must govern labels and navigation

Pack C argues that users navigate by following cues that feel likely to lead to their goal. This comes from its use of Information Foraging Theory and the concept of information scent, where headings, labels, and click cues determine whether users continue or abandon the search path ("The scent of a site," n.d.). This means NCAIF labels should:

- use plain, outcome-oriented wording
- reduce jargon at first contact
- help users predict what a click will produce
- avoid technical headings that bury practical value

### Contribution to NCAIF

NCAIF should prefer labels like:

- Understand Climate Risks
- Compare Provincial Risk Profiles
- Find Adaptation Measures
- Download Data

over labels that feel academic, internal, or method-first.

### 2. Shallow top-level navigation is preferable to deep hierarchy

Pack C warns that deep hierarchies weaken information scent, create backtracking, and trigger decision fatigue; it also cites transaction-log patterns showing that deep navigation trees create looping and abandonment behaviors in complex information spaces ("Exploring User Navigation," n.d.; "Finding Unexpected Navigation Behaviour," n.d.). Users should not need many clicks through broad, abstract menus to reach useful outputs.

### Contribution to NCAIF

NCAIF should:

- keep top-level navigation short
- avoid very large drop-down trees
- rely on curated entry points and exemplars
- use lateral linking between related content instead of forcing users back up the hierarchy

### 3. Matrix navigation is better than one rigid taxonomic tree

Pack C highlights benchmark platforms that allow users to enter from multiple vectors, using Climate-ADAPT as the clearest example of matrix taxonomy rather than a single rigid tree (Climate-ADAPT, n.d.).

- by sector
- by geography
- by knowledge resource type
- by policy need

### Contribution to NCAIF

NCAIF should support multiple entry logics, such as:

- by adaptation-cycle step
- by province or area
- by sector
- by tools and data services

This means the sitemap should not be purely linear or purely bureaucratic.

### 4. Tools and data catalogs should be separated in the front-end

This is one of Pack C’s clearest architectural contributions.

Pack C argues that data catalogs and interactive tools serve different personas, cognitive objectives, and navigation paradigms, even if they should share an integrated backend foundation. This is aligned with general data-discovery logic and with the World Bank CCKP pattern of separating repository-like data access from narrative and profile-oriented synthesis (Microsoft Security, n.d.; Domo, n.d.; World Bank, n.d.). Specifically:
- raw data catalogs serve technical users doing open-ended exploration
- interactive tools serve users wanting rapid, task-specific insight
- mixing both into one navigation environment raises cognitive load for everyone

### Contribution to NCAIF

NCAIF front-end navigation should distinguish between:

- **Interactive tools / dashboards / maps**
- **Data catalog / download / APIs / dataset discovery**

but these should still be contextually linked.

### 5. Progressive disclosure is mandatory for complex climate information

Pack C stresses that users should see immediate value first, and detailed methods or advanced controls later, tying this directly to cognitive load, processing fluency, and the need to reduce perceived difficulty at first contact (Make it Clear, n.d.; Userflow, n.d.; The Decision Lab, n.d.).

### Contribution to NCAIF

Pages should be layered like this:

1. immediate answer or summary
2. key chart, map, or interpretation
3. optional drill-down
4. methodology, caveats, and metadata

This implies that NCAIF pages should not open with dense text, large metadata tables, or full model explanations.

### 6. Narrative-driven IA is not decoration; it is a core function

Pack C treats storytelling as a structural principle. It explicitly points to guided resilience workflows and case-based storytelling, including the U.S. Climate Resilience Toolkit and the World Bank CCKP, as proof that users move more easily from hazard awareness to risk understanding to action when the platform is organized narratively (U.S. Climate Resilience Toolkit, n.d.; World Bank, n.d.).

### Contribution to NCAIF

NCAIF should feature:

- guided pathways
- briefing-pack style outputs
- case-based entry points
- narrative explainers that connect data to decisions

This supports the adaptation-cycle backbone and strengthens task-oriented use.

### 7. Case studies and concrete examples improve adoption

Pack C emphasizes social proof, case examples, and relatable stories as motivation mechanisms, linking them to behavioral concepts such as the framing effect, social proof, progressive disclosure, and the peak-end rule (The Decision Lab, n.d.; U.S. Climate Resilience Toolkit, n.d.).

### Contribution to NCAIF

NCAIF should not rely only on maps and datasets. It should include:

- good-practice examples
- place-based cases
- sector-specific stories
- practical explanation of why a user should trust and use a page

### 8. Trust requires transparency, but transparency must be staged

Pack C strongly supports showing provenance, methodology, uncertainty, and limitations, but not in a way that overwhelms the first interaction. Its recommendation is transparency through progressive disclosure rather than methodology-first page design (World Bank, n.d.; World Meteorological Organization, n.d.).

### Contribution to NCAIF

NCAIF should provide:

- visible but concise caveat and interpretation boxes
- expandable methods sections
- accessible data provenance links
- progressive disclosure for technical detail

## Pack C design principles that should directly shape NCAIF

### Recommended principles to adopt
1. Strong information scent
2. Short top-level navigation
3. Multiple entry routes
4. Front-end separation of tools and data catalogs
5. Progressive disclosure
6. Narrative and workflow-oriented page design
7. Case-based and geographically specific onboarding
8. Transparency with low-friction access
9. Feedback-loop orientation for future iteration

## Pack C anti-patterns

Pack C implicitly or explicitly warns against the following:

### 1. Bureaucratic mirror architecture
Do not organize the site based on the internal structure of DCCE, teams, or project work packages.

### 2. Deep academic hierarchy
Do not bury useful outputs under technical headings or many layers of submenus.

### 3. Mixed-mode confusion
Do not place raw data catalog experiences and decision-support tools into one undifferentiated interface path.

### 4. Metadata-first first impression
Do not make users confront dense tables, unresolved acronyms, or model language before they understand page value.

### 5. Static broadcast portal behavior

Do not treat the platform as a one-way information dump.

## Pack C implications for page archetypes

Based on Pack C alone, the most appropriate NCAIF page archetypes are:

1. **Landing pages**
   - short summaries
   - clear calls to action
   - multiple entry points by need

2. **Guided explainer pages**
   - hazard explainers
   - risk interpretation pages
   - adaptation-cycle overview pages

3. **Profile pages**
   - province or area pages
   - sector pages
   - brief decision-oriented summaries

4. **Task-oriented tool pages**
   - dashboard or map interfaces
   - guided use with clear outputs

5. **Support pages**
   - methodology
   - glossary
   - data source documentation
   - FAQs

## Pack C contribution to homepage logic

Pack C suggests that the homepage should not be a generic agency banner plus document links. It should behave as a guided entry surface, consistent with its broader argument for strong information scent, short top-level lists, and narrative entry pathways (Climate-ADAPT, n.d.; U.S. Climate Resilience Toolkit, n.d.).

### Homepage implications

The homepage should:

- introduce what the platform helps users do
- offer a small number of entry routes
- foreground decision-support and usability
- use highlighted maps, stories, or briefing routes
- avoid large undifferentiated menu blocks

## Pack C contribution to user journeys

Pack C strongly favors journey-based thinking, especially where users need guided workflows, stepwise discovery, and feedback loops rather than static broadcasting of information (World Meteorological Organization, n.d.; "User Selection and Engagement for Climate Services Coproduction," n.d.).

### Likely journey archetypes supported by Pack C

1. **Policy maker journey**
   - understand risks
   - compare places or sectors
   - access decision-ready summaries

2. **Planner or implementer journey**
   - find relevant place-based information
   - explore adaptation options
   - access briefing or supporting material

3. **Technical analyst journey**
   - start with tool or map
   - move to underlying data or methods
   - download or inspect deeper detail

## What Pack C alone would likely change in NCAIF

If we used only Pack C as a design lens, the most likely changes would be:

1. simplify and shorten the top navigation
2. create stronger landing pages and entry routes
3. separate tools from catalog/discovery in front-end navigation
4. add more guided explainer and profile pages
5. move technical detail into support layers
6. increase use of lateral linking and contextual calls to action
7. rely more on narrative framing and case-based onboarding

## What Pack C alone cannot decide

Pack C cannot tell us:

- whether a map feature is real today
- whether a dashboard belongs inside Phase 1
- whether a page is inside TOR deliverables
- whether an external system should be integrated, linked, or deferred

These decisions require combination with Packs A and B.

## Bottom line

Pack C contributes the **presentation logic** for NCAIF. Its evidence base is strongest on information scent, matrix taxonomy, catalog-versus-tool separation, progressive disclosure, narrative onboarding, and feedback-oriented user-interface platforms (Climate-ADAPT, n.d.; World Bank, n.d.; World Meteorological Organization, n.d.; Statsig, n.d.; Quantum Metric, n.d.).

It says the platform should be:

- easier to enter
- easier to understand
- more narrative
- more task-oriented
- less bureaucratic
- less catalog-shaped on the surface
- more explicit about the difference between tools, data, and support content

Its main value is not determining what NCAIF contains, but determining **how users should encounter it**.
