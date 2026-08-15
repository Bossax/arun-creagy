# WP4 Non-Catalog Deliverable Business Narratives — DEL-1 and DEL-11

**Status**: Draft, pending review
**Date**: 2026-08-15

## Why this document exists

`2026-08-14-WP6-Service-Business-Narratives.md` justifies D-043's 8-service catalog — for each service, why it needs to exist, who needs it, what's blocking it. WP4's DRD (D-068) lists 14 build deliverables in its Appendix A. Most of them serve one of those 8 services and inherit that service's justification (DEL-2 serves Service 2, DEL-12 serves Service 4, and so on).

Two don't. **DEL-1 (Thailand Climatology Dashboard, REQ-033)** and **DEL-11 (Feedback platform, REQ-073)** sit fully outside the 8-service catalog. The DRD specifies what each one has to do — it isn't required to say why it should exist, and it doesn't. Without a narrative, both would ship as unjustified builds: real engineering work with no stated demand behind it, even though a checked source turns out to name that demand for each of them.

This document is that narrative, held to the same standard as the 8 services: every claim either cites an in-repo source or is marked as a judgment call.

---

## DEL-1 — Thailand Climatology Dashboard

DCCE holds over forty years of national rainfall and temperature grid data (1981–2023, assets `DCCE_2_1` and `DCCE_2_2`), but nothing today turns that history into a usable baseline. No trend statistics have been derived from it, and the grid's provenance — whether it's built from weather stations or reanalysis output — isn't recorded in the catalog. Anyone asking how Thailand's climate has actually shifted, at what pace and in what direction, has no computed answer to point to (DRD, REQ-033).

That question isn't specific to one service — it sits underneath several of them. Service 5 needs a historical baseline before it can say how much an engineering design value should shift for future conditions. Service 2's risk index needs consistent hazard-trend inputs. Service 6's early-warning thresholds only mean something measured against a known normal. Today each would have to derive its own version of that baseline separately, from the same restricted grids, at its own accuracy and its own baseline period. That's the exact failure mode DCCE's own platform planning already named as a risk worth guarding against — the same figure disagreeing across tools because it's computed more than once instead of in one shared layer, rather than the same indicator being computed once and reused (`01_Business_Objective_Platform_Rationale/2026-08-06-Business-Objective-Platform-Rationale.md`, §2b, success criterion #4).

DEL-1 is that shared layer. It derives climatological baselines and trend statistics for temperature and rainfall once, states a single consistent baseline period, and shows the uncertainty around each trend instead of a bare number — then surfaces that both as its own dashboard page and as an embedded view wherever another page needs it. The Slow-Onset Hazards Profile (DEL-4) already draws on the same backend (data spec `DS-02`) for its own trend view, which is the first working proof this dashboard's value isn't confined to its own page (DRD, Appendix A note; `2026-08-13-WP4-DRD-Deliverable-Asset-Mapping.md`).

Two things block it before any of that can ship. The source grids (`DCCE_2_1`, `DCCE_2_2`) are access-restricted and flagged unverified-baseline, so that restriction has to be resolved before a derived trend can be published from them %%not an issue. data can be accessed easily via DCCE. The question is more like what expertise is required to build the analytical layer of this product?%%. And the provenance gap — station-interpolated versus reanalysis — has to be confirmed, because that choice changes what the derived trend is actually measuring. Neither is a design decision; both are prerequisites the DRD names but doesn't resolve (DRD, REQ-033 "Done when"). 

---

## DEL-11 — Feedback platform

Nothing like this exists at DCCE today. An agency using the platform's data has no structured way to flag a problem, ask for a scope change, or confirm whether the data actually met its need — any of that happens informally, if it happens at all (DRD, REQ-073: "No structured feedback or service quality mechanism exists at DCCE today").

That gap isn't incidental — it's the specific thing standing between the platform's phase-1 ceiling and what it's meant to grow into. The platform's own rationale names two tiers of external user: advanced analysts who can already self-serve from pooled data, and less-advanced policy users limited to high-level tools and general content because nothing tailors the platform to their specific sector or area yet. The stated reason that tailoring hasn't happened is that it requires product maturation through user feedback and engagement, and that loop doesn't exist yet — named explicitly as a phase-1 ceiling, not a permanent one (`01_Business_Objective_Platform_Rationale/2026-08-06-Business-Objective-Platform-Rationale.md`, §2). DEL-11 is that loop. Without it, the ceiling on tailored, per-sector support has no path to lift, no matter how much new data or how many new services get added.

The DRD scopes it as a structured route for an agency to submit feedback tied to a specific dataset or page, with a named owner, a visible status, and aggregate reporting so a recurring problem becomes visible instead of being handled one submission at a time (data spec `DS-11`). It's explicitly new operational build, not a fill-in for existing content — DCCE has no service or system today that does any part of this job (DRD, REQ-073 note).

One more thing it may quietly resolve, worth naming even though it isn't confirmed anywhere as DEL-11's intended purpose: the platform's own planning leaves an adoption or usage metric — how many agencies are actively pulling from a product, how often — as a deliberately open question, with no source naming one and no invented number filling it in (`01_Business_Objective_Platform_Rationale/2026-08-06-Business-Objective-Platform-Rationale.md`, §2b). A working feedback platform is a plausible source for exactly that signal — submission volume and frequency by agency. That connection is this document's own observation, not something stated in the DRD or the rationale doc, and should be treated as a possibility to raise with Boss, not a settled scope item.
