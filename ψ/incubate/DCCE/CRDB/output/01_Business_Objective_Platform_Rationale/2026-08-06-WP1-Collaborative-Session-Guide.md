---
type: draft
status: preliminary
version: 1
created: 2026-08-06
project:
  - DCCE_CRDB
---

> [!note] Purpose
> This is a facilitation tool, not a deliverable. It defines what an *ideal* Business Objective / Platform Rationale document should answer, maps that against what `2026-08-06-Business-Objective-Platform-Rationale.md` currently answers, and turns the gaps into an ordered set of guided questions for a collaborative session with Boss. Nothing here is sealed or final.

# 1. What an Ideal Business Objective / Platform Rationale Should Answer

A document at this altitude earns its place as "the thing Gap Analysis and Recommendations get scored against" only if it answers all of the following — not just describes the evidence around them:

| # | Question | Why it matters |
|---|---|---|
| 1 | **Problem** — one merged, falsifiable problem statement | Two parallel "why"s left unresolved means downstream work (Item 6/8) has no single target to score against |
| 2 | **Why now** — what forces this timing; cost of inaction | Distinguishes "nice to have" from "must ship this sprint"; grounds urgency for Recommendations' budget ask |
| 3 | **Who it serves** — named primary segment(s) as real personas (role + job + context), plus explicit exclusions | Role-title lists copied from procurement text aren't personas; a PM (or CRDB itself) can't design against a list of job titles |
| 4 | **Vision / desired end-state** — qualitative description of "working" | Without this, "done" has no shape; Item 7 (Gap Analysis) has nothing to gap-check against |
| 5 | **Success criteria** — measurable signals (adoption, data quality/freshness, staff self-sufficiency, etc.) | Turns vision into something checkable; without it no one can later say whether the platform succeeded |
| 6 | **Scope boundary** — explicit in/out; relation to TOR70's build scope and to future phases | CRDB and TOR70 already split Planning/Design vs. Build; this doc should state where the governance-capability layer and public-dashboard layer sit relative to each other — one product in phases, or two products sharing a data layer |
| 7 | **Constraints** — governance, budget, procurement, legal, inherited from the TORs | Keeps Recommendations grounded in what's actually contractually/legally possible |
| 8 | **Ownership / decision rights** — who owns which call (Data Owner, Data Steward, Director-level sign-off) | Without named owners, every open question stays open indefinitely |
| 9 | **Risks / what's lost without it** | Already the strongest section of the current draft |
| 10 | **Dependencies** — what has to exist or be true first | E.g., the domain-ownership governance framework (July 2 focus group) has to mature before certain claims can be finalized |
| 11 | **Phasing** — MVP vs. deferred, and the trigger for moving to the next phase | Resolves "what do we build first," which the PM-lens review found the current draft couldn't answer |
| 12 | **Open decisions log** — named list of unresolved calls, owner, target date | Makes "still open" tractable instead of scattered as inline flags |

# 2. Gap Map — Current Draft vs. Ideal

Against `2026-08-06-Business-Objective-Platform-Rationale.md` as it stands now:

| # | Question | Status | Notes |
|---|---|---|---|
| 1 | Problem | **Partial** | Two altitudes named and explained, deliberately not merged (Section 1) |
| 2 | Why now | **Not answered** | July 2 governance-framework fact hints at timing but "cost of inaction" isn't stated |
| 3 | Who it serves | **Answered** | Section 2 — two primary personas (sectoral/area-based policymakers-authorities, split by sophistication; DCCE staff/analysts) with jobs and "without it" baselines, plus secondary personas named explicitly (leadership, academics, budget officials); explicit phase-1 ceiling (no tailored per-sector/area support yet) stated |
| 4 | Vision / end-state | **Answered** | Section 2b — two-level vision: long-term (full 8-catalog) and phase-1 (FGD3's 5-section site structure + 5 products) |
| 5 | Success criteria | **Answered** | Section 2b — long-term outcomes (FGD3 Slide 25) + 7 checkable phase-1 criteria; adoption/usage metric deliberately left open, noted as a side item rather than dropped |
| 6 | Scope boundary | **Answered** | Section 2a — one platform, phased; phase-1 = 5 products + website content + Data Hub foundation; A-BTR named as a separate mandate-compliance category; catalog item 3 explicitly excluded (feasibility) |
| 7 | Constraints | **Answered** | Section 2c — DB-admin role resolved to a functional definition (CMS/content-administration); governance dependency resolved to CRDB's own existing 2-phase roadmap (Proposed-governance-plan-to-DCCE.md), pace left to DCCE |
| 8 | Ownership / decision rights | **Answered** | Section 5's open-decisions table — every remaining item has a named owner (CRDB or DCCE, with specific work groups where applicable) |
| 9 | Risks / what's lost | **Answered** | Section 3 is solid, TOR-traceable |
| 10 | Dependencies | **Answered** | Section 2c — governance is an incremental dependency (Phase 1: standards/roles/committee/inventory; Phase 2: catalog live/TOR embedding/external agreements/policy expansion), Phase 1 named as the minimum bar for Section 2b's success criteria to be checkable |
| 11 | Phasing | **Answered** | Section 2a — MVP = phase-1 scope above; catalog items 5–8 deferred; no phase-2 trigger defined, and that absence is the answer — CRDB's role is to propose trigger options, not decide one |
| 12 | Open decisions log | **Answered** | Section 5's open-decisions table; a standalone artifact was considered and deliberately skipped as unnecessary given the short remaining list |

# 3. Guided Questions for the Collaborative Session

Ordered so early answers reframe later ones. Each question is written to extract a **decision**, using the concrete unresolved items already on record — not to re-elicit information already captured in the TOR-grounded draft.

## A. Scope & Phasing — RESOLVED (2026-08-06) ✅

1. ~~Is the governance-capability layer... one product delivered in phases, or two products sharing a data layer?~~ **Resolved:** one platform (the Data Hub), one long-term 8-service catalog (Strategic Alignment Deck, Slide 16), delivered in phases. Not two competing products.
2. ~~What specifically is in scope for phase 1?~~ **Resolved:** three parts — (a) 5 core products: 3 existing analytical tools (Spatial Risk DB, Hazard/Exposure Map, CRI) mapping to catalog item 2, disaster-loss-statistics mapping to catalog item 4, and A-BTR as a separate internal mandate-compliance service (UNFCCC Biennial Transparency Report obligation, not part of the 8-catalog); (b) general climate-adaptation website content; (c) the Data Hub itself as foundational infrastructure. Catalog item 3 (financial/budget decision-support) is explicitly excluded from phase 1 — feasibility too low, no methodology/dataset exists yet; to be named in Item 8 (Recommendations) as a future item, not silently dropped.
3. ~~What's the trigger condition for moving to the next phase?~~ **Resolved:** no trigger is defined anywhere (TOR, decks, or this session), and that's the real answer — phase-2 timing (catalog items 5–8) depends on DCCE's own internal decision-making. CRDB's role is to **propose** trigger options (contract/procurement timing, governance-framework maturity, demand signal, budget cycle) — not decide one.

*Full writeup folded into `2026-08-06-Business-Objective-Platform-Rationale.md`, Section 2a.*

## B. Vision & Success Criteria — RESOLVED (2026-08-06) ✅

4. ~~In one sentence, what does "this platform is working" look like?~~ **Resolved:** two levels — long-term platform vision (full 8-catalog, DCCE's core information/knowledge mandate) and a concrete phase-1 implementation vision anchored to FGD3's own proposed 5-section site structure plus the 5 core products, each named with a specific user job.
5. ~~What measurable signal would tell you the governance-capability gap has closed?~~ **Resolved:** governance framework formally ratified (not just FGD3 room-accepted) + a quality-defined baseline inventory (completeness/accuracy/timeliness, not raw count) + metadata coverage extended to non-analytical assets (PDFs/web content/infographics, closing DCCE's own internal-metadata-project gap) + DGA Open Data Standard compliance.
6. ~~What measurable signal would tell you the public-dashboard/comms gap has closed for phase-1?~~ **Resolved:** staff self-sufficiency (no-code updates), cross-tool data consistency (no metric drift between the 3 enhanced existing tools), A-BTR's mandate use case measurably reducing manual reporting effort, disaster-loss-statistics available on demand. Adoption/usage metric explicitly deferred — DCCE's call, not CRDB's to invent.

*Full writeup folded into `2026-08-06-Business-Objective-Platform-Rationale.md`, Section 2b.*

## C. Personas & Who It Serves — RESOLVED (2026-08-06) ✅

7. ~~Of CRDB-TOR §3's institutional list, which 2–3 are the *primary* persona(s) for phase 1?~~ **Resolved:** all of CRDB-TOR §3's institutional list is in phase-1 scope (academics/experts already benefit from the data catalog and existing analytical tools), but two personas are primary by design: sectoral/area-based policymakers-authorities (primary external) and DCCE staff/analysts (primary internal). DCCE leadership, academics/experts, and budget/project-screening officials are secondary — served, not the design target.
8. ~~For that primary persona, what's the specific job... and what do they do today instead?~~ **Resolved:** sectoral/area-based authorities use the platform to inform high-level planning — risk screening and prioritization of where deeper study is warranted — plus building conceptual grounding in the adaptation cycle. This splits by sophistication: advanced users self-serve the newly-pooled datasets; less-advanced users use existing high-level tools and info content to understand, learn, and inspire policy frameworks. Explicit phase-1 ceiling, stated not implied: the platform cannot yet deliver tailored, granular per-sector/area support — that needs a user-feedback/engagement loop that hasn't happened. Without it today: no pooled authoritative dataset location, ad hoc studies with no prioritization signal, scattered sources, no shared conceptual vocabulary. DCCE staff/analysts' job/baseline was already anchored via Section 2b's self-sufficiency criterion.

*Full writeup folded into `2026-08-06-Business-Objective-Platform-Rationale.md`, Section 2.*

## D. Constraints & Dependencies — RESOLVED (2026-08-06) ✅

9. ~~The database-administrator role's scope is unclear from TOR70's text (§5.4.14)...~~ **Resolved:** it's inferred, not named — combining §5.4.14's RBAC/permission-matrix requirement with §5.5's CMS mandate (per `TOR70-development-of-climate-adaptation-databse-comments.md`). Functionally it's a CMS/content-administration role, not literal database-infrastructure administration. Still open (org-assignment, not TOR-text): which specific DCCE role/person holds it.
10. ~~Beyond the domain-ownership framework, what else has to exist or be decided...~~ **Resolved, deliberately partial:** no complete list can be given with confidence — governance pace is DCCE's own call. What CRDB can and does propose: its own already-drafted 2-phase governance roadmap (`Proposed-governance-plan-to-DCCE.md`, the same one FGD3 Slide 23 references) — Phase 1 (0–6mo: standards, roles, committee, inventory) as the minimum bar for Section 2b's success criteria to be checkable, Phase 2 (1yr+: catalog live, TOR embedding, external agreements, policy expansion) as outward-facing and not a phase-1-platform dependency. Framed explicitly as incremental rollout, not one-time installation.

*Full writeup folded into `2026-08-06-Business-Objective-Platform-Rationale.md`, Section 2c and Section 3's revised DB-admin note.*

## E. Ownership & Open Decisions — RESOLVED (2026-08-06) ✅

11. ~~Who owns the call on Question A.1 (one product/two products)...~~ **Resolved:** CRDB's synthesis call, informally backed by Director Toey via her acceptance of the Strategic Alignment Deck. Optional explicit re-confirmation with her recommended since it reframes Section 1, but not required to treat A.1 as settled.
12. ~~Should this session produce a consolidated open-decisions log...~~ **Resolved:** a standalone artifact was considered and deliberately skipped — with only 7 remaining items (2 CRDB-owned synthesis tasks, 4 DCCE-owned decisions, 1 optional confirmation), a table inside Section 5 carries the same information without a separate file to maintain.

*Full writeup folded into `2026-08-06-Business-Objective-Platform-Rationale.md`, Section 5's open-decisions table.*

---

**All five guided-question groups (A–E) are now resolved and documented.** What remains outside this facilitation guide's scope: CRDB's own synthesis work (merging Section 1's problem statement, prioritizing the appendix's ~13 needs) and DCCE's own pending decisions (adoption metric, phase-2 trigger, governance-committee ratification, DB-admin role assignment) — all tracked in the rationale doc's Section 5 table, not here.
