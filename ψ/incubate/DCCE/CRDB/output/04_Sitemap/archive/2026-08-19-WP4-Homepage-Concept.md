# NCAIF Homepage Concept — Router, Not Info Page

**Date**: 19 August 2026
**Status**: DRAFT — for discussion, not yet locked
**Context**: WP4 Sitemap. Written after noticing the current structure (`ncaif_sitemap_nodes.csv`, `NCAIF_Detailed_Sitemap_v8.md`) nests "Executive Overview" (1.1, containing 1.1.1 and 1.1.2) as a child section *of* the homepage (1) rather than as a sibling page. That nesting makes Home read as a long-form info article with a search box in the middle, not a front door.
**Relates to**: `2026-06-04-NCAIF-Sitemap-v5-Design-Decisions.md` (the locked IA principles this concept tries to satisfy), `2026-08-13-WP4-Node-Content-Storyboard-and-Synthesis-Guide.md` (current per-page storyboards for 1.1.1 / 1.1.2 / 1.2, readiness 2/5, 3/5, 2/5)

---

## The problem with the current structure

`SIT-1` (Home) has two children: `SIT-1.1` (Executive Overview — itself parent to 1.1.1 and 1.1.2) and `SIT-1.2` (Area Search). Structurally this means the homepage's job *is* to deliver the national risk narrative — IPCC framework definitions, physical-vs-transition risk, hotspot synthesis, NAP summary — with a search tool sitting in the middle of it.

Two consequences follow directly from that structure:

- The homepage inherits the readiness of its two weakest pages on the entire site (1.1.1 at 2/5, 1.1.2 at 3/5 per the Node Content Storyboard). The front door can't open until the least-ready content is finished.
- A returning user with a specific job — check budget evidence, look up a province, find a working measure — has to scroll past a climate-science explainer every visit to get anywhere.

## Reframing: what should a homepage do

Boss's framing: the homepage should make clear what the website offers and prioritize UX, not front-load information the user didn't come for. That points at a **router**, not an **info page** — a distinction worth naming explicitly since v8's structure picked info-page by default (by nesting, not by decision).

This also resolves the earlier "is Home the same as Overview" question: if Home routes, then Overview becomes its own destination page, not a section balanced on top of the homepage. They stop overlapping because they do different jobs.

## Four archetypes considered

| # | Archetype | What Home shows | Strongest case | Cost |
|---|---|---|---|---|
| A | Info page | Full national risk narrative, search box embedded | Matches "Mandate-First" IA principle most literally — national narrative gets the front door | Front page inherits the site's two lowest-readiness pages; repeat visitors re-read the same explainer every time |
| B | Router / hub | Short hero, search, zone/service cards, latest updates | Matches the v5 lock's own words — *"The Homepage remains clean with 3 primary entry routes"* | Says little about climate itself on first look; can read thin for a national portal without support from a companion panel |
| C | Live status dashboard | Current hazard season, latest DDPM events, 7-sector index, data freshness | Matches A-PLAT's model; strongest reason to return weekly | Needs an operational data feed nobody has committed to; DDPM's pipeline is one-way, unverified against ground truth — a live homepage broadcasts that weakness constantly |
| D | Search-first | Large search box, almost nothing above the fold | Matches how most users actually arrive ("is my province at risk") | Abandons the national narrative; 1.2's own storyboard confirms sub-province data doesn't exist yet, so most searches return province-level fallbacks |

## Recommendation: B, with a thin slice of A

A short homepage carrying the search, the service-routing cards, and one condensed national context panel (a few summary cards plus the disaster-history chart) — while the full 1.1.1 and 1.1.2 explainers move to their own page, one level below Home instead of nested under it.

This satisfies both halves of the v5 lock at once (clean homepage *and* the national narrative stays visible, just condensed) rather than picking one over the other, and it removes the readiness bottleneck from the front door — Home can ship once the search and cards work, independent of when the climate-science explainer content is finished.

## Homepage — objective, functions, and conceptual design

This is a concept, not a detailed design. It states what the homepage is *for* and what it must *do* — the visual layout, card wording, and interaction design are next-project scope, owned by the SW developer/UX designer working from this concept.

**Objective.** The homepage exists to get any user to the right place fast, and to make legible in one screen what the platform as a whole offers — without requiring the user to read the national risk narrative first. It is a front door, not a briefing.

**Functions the homepage must perform:**

1. **State what the platform is**, in enough words that a first-time visitor understands the offer before doing anything else.
2. **Let a user search their own area** directly, without navigating through a section first — this is the one piece of Zone 1's original content that stays on the homepage, since it's an action, not an explainer.
3. **Route by task.** Give the user a small number of task-oriented shortcuts into the site, so someone with a specific job doesn't have to first learn the site's section structure to get there. What the exact set of tasks/labels should be is next-project design work — this concept only establishes that the function exists and why (see debate below).
4. **Signal the country context exists, without delivering it.** A thin, current-feeling strip of headline numbers that point into the full Country Overview page rather than substituting for it — enough to establish the platform is live and grounded in real data, not enough to make the homepage into an info page again.
5. **Signal the platform is maintained.** Recently updated datasets or pages, so a returning user sees the system has a pulse.
6. **Offer a way out to help.** A visible path to feedback/data-quality reporting for a user who hits a dead end.

None of these functions are new information — they were present in the four-archetype comparison and the original band list — this section restates them as objective+function pairs so the next project can design against intent rather than against literal band copy.

## Task-based routing vs. the sitemap sections — are they competing?

This was raised directly and is worth resolving as a stated design principle, not leaving implicit.

**The tension:** the sitemap's sections (Home, Country Overview, Policy Maker Center, Adaptation Cycle, Tools & Services, News & Contact) are themselves supposed to answer "what can this site do for me" — that's what the locked v5 IA decision means by organizing the top level around the national mandate. A homepage that also offers task-based shortcuts is presenting a second, parallel answer to the same question, organized around user tasks instead of sections. Followed carelessly, this produces two competing mental models on one page, and can duplicate a section's own entry point (e.g., a "look up my area" shortcut sitting next to the area-search field that already does the same thing).

**The resolution this concept takes:** task-based routing and the section structure are not alternatives — they are two different altitudes serving two different moments. The task shortcuts are a **fast path for the common cases**; the section structure (surfaced through persistent site-wide navigation, see below) is the **complete, structurally honest map** for everything else. They only genuinely compete if the next-project design lets them drift apart — task shortcuts must be understood as curated entry points *into* the existing section structure, not an independently invented second taxonomy, and any shortcut that duplicates a homepage element already on the page (like area search) should be treated as a defect, not a feature.

## Global navigation — how a user reaches all sections, including Country Overview

This concept was originally missing an answer to "where can the user see the other sections?" — task-based shortcuts on the homepage only cover a handful of common jobs; they were never meant to be the only way to reach every section, and Country Overview in particular has no natural task-shortcut home (browsing the national risk picture isn't phrased as a task the way "look up my area" is).

**Objective.** Every section of the site — including ones with no homepage shortcut — must be reachable from anywhere on the site, not just from the homepage.

**Function.** A persistent, site-wide navigation element (e.g. a header menu) listing all top-level sections by name: Home, Country Overview, Policy Maker Center, Adaptation Cycle, Tools & Services, News & Contact. This is the fallback and the complete map; the homepage's task shortcuts are the accelerant on top of it, not a replacement for it. Detailed placement/interaction (menu bar, drawer, footer sitemap, etc.) is next-project design work — this concept only establishes that it must exist and what it must list.

## Structural change this implies

`SIT-1.1` (currently Executive Overview, parent of 1.1.1/1.1.2) stops being a child of Home and becomes its own top-level-adjacent section — **ภาพรวมประเทศ (Country Overview)** — a sibling of Home, not nested under it. `SIT-1.2` (Area Search) stays on the homepage itself, since it's an action, not content.

Net page count for the zone is unchanged (the same three content pieces exist, just re-parented), but the "3 PAGES (1.1.1 – 1.2)" badge on the current sitemap-overview slide deck (`ncaif-sitemap-overview.html`, Zone 1 card) needs updating once this is decided, since it currently implies all three live under Home.

## Decisions confirmed

1. The national-context strip's draft/unverified figures are not this concept's problem to resolve — flagging them, and designing how they're shown, is left as a requirement for the next project's SW developer/UX designer. This document hands over the concept, not the resolved data question.
2. Re-parenting of 1.1.1/1.1.2 out from under Home is confirmed. They move into the new Country Overview section.

## Open question remaining

Does the "guidance / action" third entry route from the v5 lock (National Situation / My Area / **Guidance**) need reviving as a first-class homepage function, or is it sufficiently covered by task-based routing (function 3 above) plus the persistent navigation? Not yet answered.
