# NCAIF Sitemap vNext Plan

## Objective

Refine the NCAIF presented in FGD2 so it looks like the kind of website-platform DCCE officials expect, while preserving the underlying logic that makes the platform trustworthy and extensible.

This plan keeps the strengths of:

- [`ψ/incubate/DCCE/CRDB/National Climate Adaptation Information Framework.md`](National%20Climate%20Adaptation%20Information%20Framework.md)
- [`ψ/incubate/DCCE/CRDB/Artifact v1/NCAIF_Sitemap_Options.md`](NCAIF_Sitemap_Options.md)
- [`ψ/incubate/DCCE/CRDB/inbox/writing_notes/2026-03-11_FGD2_action_summary.md`](2026-03-11_FGD2_action_summary.md)

## Design stance to carry into the interim report

The recommended direction is a **user-journey-oriented NCAIF whose backbone is the adaptation cycle**.

This means:

- preserve the broad thematic topics from Option 1 because they are legible and policy-friendly
- preserve the FGD2 policy-maker block because it gives officials a recognizable "service area"
- make the adaptation cycle the main organizing logic for navigation and storytelling
- keep technical assets such as recommended baselines and spatial references embedded within workflow pages rather than promoted as the main public-facing identity
- show enough page detail that leaders can imagine a real platform, not just a concept diagram

## Recommended sitemap vNext

### Top-level navigation

1. Home
2. Data Management Center for Policy Makers
3. Adaptation Information by Cycle
4. Risk and Area Profiles
5. Adaptation Measures and Implementation
6. Knowledge, Tools, and Data Services
7. News, Updates, and About

## Drill-down sitemap

### 1. Home

- National climate adaptation overview
- Key climate risks and adaptation priorities
- Featured maps and insight cards
- Latest updates
- Quick entry by need
  - Understand risks
  - Plan adaptation action
  - Monitor adaptation progress
  - Access data services

### 2. Data Management Center for Policy Makers

Keep this block from FGD2 as a first-class section.

- Summary of risks by area and sector
  - National summary
  - Provincial profiles
  - Sector summaries
  - Executive briefing pack export
- Indicators
  - Disaster indicators and extreme events
  - Risk indicators
  - Adaptation progress indicators
  - Monitoring and evaluation indicators
- Status of national adaptation measures
  - National adaptation plan progress
  - Priority measures by sector
  - Implementation progress snapshots
- Data services for strategic planning
  - Hazard and vulnerability overlay tool
  - Spatial risk database
  - Scenario and planning support pages
  - Methodology and standards guidance

### 3. Adaptation Information by Cycle

This becomes the main navigation backbone.

- Climate and climate conditions
  - Climate drivers and trends
  - Historical observations
  - Future climate scenarios
  - Hazard overview pages
- Risks and impacts
  - Exposure and vulnerability
  - Risk assessments by sector
  - Risk assessments by area
  - Cascading impacts and cross-sector effects
- Loss and damage
  - Event overviews
  - Post-event impact assessment pages
  - Damage and loss summaries
  - Revision and update notes
- Adaptation planning
  - Adaptation planning guidance
  - Priority options and response pathways
  - Planning case examples
  - Budget justification packs
- Adaptation implementation
  - Ongoing projects and interventions
  - Who is doing what
  - Local and sector implementation examples
  - Implementation challenges and lessons
- Results and monitoring
  - Monitoring and evaluation framework
  - Outcome and progress dashboards
  - Adaptation effectiveness stories
  - Reporting resources

### 4. Risk and Area Profiles

- Provincial risk profiles
- Area-based summaries
- Sector-based risk pages
- Cross-area comparison views
- Printable briefing packs

This is where [`MVP-1`](ψ/incubate/DCCE/CRDB/NCAIF%20%E2%80%94%20Workflow%20patterns%20%2B%20MVP%20v3.md) is most visible to users.

### 5. Adaptation Measures and Implementation

- Adaptation options library
  - Nature-based solutions
  - Infrastructure and engineering
  - Governance and policy measures
  - Community-based approaches
- Good practices and case studies
- National and local implementation status
- Implementation support resources

### 6. Knowledge, Tools, and Data Services

This section contains technical support functions, but they are embedded as enabling services rather than the central brand of the platform.

- Data catalog and discovery
  - Browse datasets by theme
  - Browse datasets by sector
  - Browse datasets by area
  - Dataset pages with steward, cadence, access condition, and usage notes
- Strategic planning data services
  - Standard reference datasets inside relevant pages
  - Overlay and map services
  - Download and request services
- Methodology and standards
  - How risk is defined
  - How adaptation is categorized
  - Indicator methods
  - How to interpret climate projections and uncertainty
- Glossary and learning resources

This is where [`MVP-3`](ψ/incubate/DCCE/CRDB/NCAIF%20%E2%80%94%20Workflow%20patterns%20%2B%20MVP%20v3.md) and [`MVP-4`](ψ/incubate/DCCE/CRDB/NCAIF%20%E2%80%94%20Workflow%20patterns%20%2B%20MVP%20v3.md) live, but as embedded support layers, not as the platform’s headline identity.

### 7. News, Updates, and About

- News and events
- Recent publications
- About the platform
- Partner agencies
- Contact and feedback

## Visible MVP placement

### [`MVP-1`](ψ/incubate/DCCE/CRDB/NCAIF%20%E2%80%94%20Workflow%20patterns%20%2B%20MVP%20v3.md)

- Surface through policy-maker summaries, provincial profiles, sector pages, and budget justification pages
- User-facing form is the exportable briefing pack, not the backend workflow

### [`MVP-2`](ψ/incubate/DCCE/CRDB/NCAIF%20%E2%80%94%20Workflow%20patterns%20%2B%20MVP%20v3.md)

- Surface under indicators and loss-and-damage pages
- User-facing form is disaster indicators, event summaries, post-event assessment pages, and versioned updates

### [`MVP-3`](ψ/incubate/DCCE/CRDB/NCAIF%20%E2%80%94%20Workflow%20patterns%20%2B%20MVP%20v3.md)

- Embed inside policy-maker services, dataset detail pages, and planning workflows
- Present as recommended or standard reference datasets inside context, not as a separate top-level destination

### [`MVP-4`](ψ/incubate/DCCE/CRDB/NCAIF%20%E2%80%94%20Workflow%20patterns%20%2B%20MVP%20v3.md)

- Embed in climate scenario, hazard, and methodology pages
- Present as guidance for interpretation, limitations, and appropriate use

## Stable vs flexible sitemap rules

### Stable backbone

These should remain stable across revisions:

- adaptation cycle structure
- policy-maker service block
- core topic families
  - climate conditions
  - risks and impacts
  - loss and damage
  - adaptation planning
  - adaptation implementation
  - results and monitoring
- existence of data services, methodology, glossary, and updates sections

### Flexible elements

These can evolve over time:

- specific sectors
- hazard subtopics
- named tools and dashboards
- case studies and featured stories
- agency collections
- indicator sets
- special campaign pages and homepage features

## Sitemap change process

### Change types

1. Minor content change
   - add or revise a subpage
   - update labels for clarity
   - add a new case study, tool page, or featured dataset page

2. Structural extension
   - add a new subtopic under an existing adaptation-cycle branch
   - add a new sector page or thematic collection

3. Backbone change
   - change top-level navigation
   - rename or remove adaptation-cycle branches
   - move the policy-maker block out of its current role

### Governance rule

- minor content change can be approved by the section owner or steward
- structural extension should be reviewed by the CRDB/NCAIF coordinating team
- backbone change should require explicit DCCE leadership review because it changes how the platform is understood

## Interim-report framing to use

The interim report should describe NCAIF as:

> a user-journey-oriented national adaptation information platform, structured around the adaptation cycle and supported by policy-maker service pages, curated risk summaries, implementation knowledge, and embedded data services.

And it should explicitly state:

- the sitemap shown in FGD2 remains valid as the seed structure
- the revised version deepens page detail to make the platform legible and implementation-ready
- technical functions such as recommended baselines, standards, uncertainty guidance, and dataset metadata are embedded within use-oriented pages so the platform remains approachable for non-technical users

## Execution checklist for [💻 Code](.roomodes)

- [x] Update [`ψ/incubate/DCCE/CRDB/National Climate Adaptation Information Framework.md`](National%20Climate%20Adaptation%20Information%20Framework.md) with the vNext sitemap narrative
- [x] Add a new section containing the 2 to 3 level drill-down sitemap
- [x] Add a stable vs flexible sitemap rule section
- [x] Add the sitemap change process section
- [x] Revise wording so recommended baselines and spatial references are embedded, not platform-defining
- [x] Make sure the policy-maker block from FGD2 remains intact and prominent
- [x] Align the interim-report narrative with [`ψ/incubate/DCCE/CRDB/inbox/writing_notes/2026-03-11_FGD2_action_summary.md`](2026-03-11_FGD2_action_summary.md)
