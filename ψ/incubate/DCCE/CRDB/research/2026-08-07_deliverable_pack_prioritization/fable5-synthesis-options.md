# Synthesis: CRDB Deliverable Pack for the Final 7 Days

**Date**: 2026-08-07 | **Inputs**: Agent A (Standards Architect) and Agent B (Pragmatic Delivery Lead) position papers

## Where they actually agree

Both papers accept the two priority use cases (A-BTR, disaster-loss-statistics) get full depth — STM, acceptance criteria, NFRs, the works. Both accept the Data Contracts / Reference Data precedent (defer to TOR70, don't relitigate). Both treat the "data platform" vs "data system" terminology fix as cheap and low-priority, riding along with WP10's existing sweep rather than earning its own pass. Neither disputes that Gap #2 (acceptance criteria) matters for the two locked use cases specifically.

## Where they load-bearingly disagree

It's not "how much to close" in the abstract — it's what DCCE's remaining review capacity is actually for. Paper A treats DCCE's sign-off as fast and cheap regardless of scope, so breadth is nearly free once the tables exist — the constraint is CRDB's authoring time, not DCCE's attention. Paper B treats DCCE's queue itself as the bottleneck (it names four already-stalled DCCE decisions as evidence) — meaning even well-built artifacts for 9 services will sit unread or get rubber-stamped without real scrutiny, so authoring them is optimizing the wrong constraint. That's the real fork: is DCCE's sign-off elastic or is it already saturated?

## My call

Paper B's reasoning is more compelling on the central question. Paper A's rebuttal ("the tables are built to make sign-off fast, not require expertise") answers a capacity-of-effort objection but doesn't answer a capacity-of-attention objection — DCCE stalling on four decisions *already in flight* is direct evidence their bottleneck is bandwidth, not table quality. Spending 7 days authoring NFR matrices for 9 services that then wait behind the same queue as the adoption-metric decision doesn't de-risk anything; it just produces more inventory. Paper A is right that undocumented ambiguity is a real renegotiation exposure — but Paper B's rebuttal on that exact point (named, owned, phased deferral is renegotiation-proof; silence is the risk, not disclosure) is the stronger legal/contractual argument, and it's the same logic DCCE already accepted for Data Contracts and Reference Data. Extending a precedent DCCE has already blessed is lower-risk than asking DCCE to newly absorb 9-service review load it hasn't shown capacity for.

That said, Paper A is right that going *all the way* to two-use-cases-only leaves real exposure on the other 7 services — "field-level detail" and "misinterpretation risk" aren't just rhetoric, they're what a fixed-price vendor exploits. The honest middle isn't a checklist split; it's picking a bounded extension of Paper B's logic that buys down the worst of that specific exposure without re-opening the DCCE bottleneck.

## Options

**1. "Two and Done" (pure Paper B).** WP2/WP3: STM + acceptance criteria for the 4-8 rows feeding the two priority use cases only. WP6(a): NFR matrix for those 2 services only. WP6(b): both Functional Specs full depth, Gap #2 fully closed. WP5: RACI stays prose, not tabled. WP10: Assumption Log at platform/governance level, explicitly logging the 4 stalled DCCE decisions as bottleneck evidence; terminology folded into WP10 sweep. WP8 gets 7 services + 250 rows + RACI-table + DAMA-6 as named, owned, phased TOR70 tasks. WP11 deck as-is.
- Day cost: ~3-4 days, leaving slack.
- Fully closes: gaps for 2 services. Defers: everything else, explicitly.
- Risk: if TOR70 or DCCE leadership expected *any* visible progress on the other 7 services, this reads as thin; the "disclosed deferral" argument only holds if WP8's task descriptions are genuinely concrete (named owner, phase, acceptance trigger) — a vague WP8 list undermines the whole renegotiation-proof claim.

**2. "Standards Architect, Unbounded" (pure Paper A).** Full breadth: STM + acceptance criteria for top-10 assets, NFR matrix for all 9 services, RACI as a formal table, project-level Assumption Log as a WP10 appendix, terminology fix riding along.
- Day cost: 6-7 days, essentially the whole runway, funded by compressing WP11 to a 6-8 slide deck and freezing WP4/WP8 scope.
- Fully closes: 3 critical + 3 recommended gaps at top-10-asset/9-service level. Defers: nothing new — WP8 as originally scoped stays thin.
- Risk: this bets the whole sprint on DCCE's sign-off being fast, which the four stalled decisions argue against; if DCCE can't turn around review in the remaining window, CRDB ends the sprint with more artifacts but the same stalled decisions, and WP11's exec deck gets squeezed to make room — a bad trade if the exec deck is what actually unsticks DCCE's queue.

**3. "Bounded Extension" (recommended middle, not a split-the-difference checklist).** Same as Option 1 for the two priority use cases (WP2/WP3 STM + acceptance criteria for 4-8 rows, WP6 NFR for 2 services, WP6(b) full Functional Specs). *Additionally*: extend STM + a lightweight (not full acceptance-criteria-table) risk flag to the top-10 assets across the other 7 services — one pass, one day, just enough to catch any asset-level landmine before handoff, not full field-level acceptance criteria. RACI stays prose (not tabled — that's Paper A's cheapest-to-defer item, no reason to spend WP5 time promoting it). Assumption Log stays platform-level per Paper B, but gets one added line item per deferred service naming what's NOT covered by the top-10 pass — closing Paper A's real objection (silent gaps) without re-litigating field-level depth. WP8 still carries the 7 services + 250 rows as named, phased TOR70 tasks. Terminology rides WP10 sweep.
- Day cost: ~5 days.
- Fully closes: 2 use cases at full depth, top-10-asset landmine-check for the other 7 services. Defers: field-level acceptance criteria and NFRs for 7 services/250 rows, RACI formalization — all named to TOR70.
- Risk: this is a judgment call on what counts as "just enough" — if the one-day top-10 pass surfaces real landmines, you may not have days left to fix them, only to disclose them; and it still consumes 2 more days than Option 1, days you don't get back if DCCE's queue clears and something urgent lands.

## Recommendation

I'd steer Boss toward Option 1, Two and Done — the four already-stalled DCCE decisions are hard evidence that authoring more artifacts this week doesn't buy faster sign-off, only faster building of a backlog; the marginal day saved is worth more sitting in reserve than in a top-10 landmine-check that Paper A's own logic already shows DCCE isn't positioned to review anyway. Push back if you think TOR70 or DCCE leadership needs visible motion across all 9 services regardless of review capacity — that's a real reason to take Option 3 instead.
