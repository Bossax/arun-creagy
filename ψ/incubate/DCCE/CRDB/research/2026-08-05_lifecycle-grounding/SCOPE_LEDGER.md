# Scope Ledger — CRDB Lifecycle Grounding, Phase B

This file is the single source of truth for what is settled and what is open in this research. Both
Claude and agy must check against it before acting: Claude before drafting any query pack, agy before
executing one and before writing second-opinion feedback.

## Settled Findings (closed — do not re-query, do not re-open)

1. **LDM is a delivered artifact, not a pending architecture choice.** LDM = a logical data model for
   the Loss & Damage sub-domain, already produced. No centralized/federated/semantic paradigm
   decision is pending for it; that three-paradigm framing (from Phase A, iteration-1/2/3) does not
   apply to LDM and must not be revisited.
2. **"Data Management Framework" = the broad sense.** Governance + architecture + metadata + master
   data, not day-to-day operational data management. Confirmed by CRDB's phase placement (below);
   there is no physical system yet for the narrow sense to apply to.
3. **Phase placement is fixed.** CRDB = Planning + Requirement Analysis + Design phases of the DSDLC
   (7-phase model: Planning, Requirement Analysis, Design, Development, Testing, Deployment,
   Maintenance). TOR70 = Development + Testing + Deployment + Maintenance.
4. **CRDB's role is fixed.** Data architect + information architect + business analyst. Not system
   architect, not software engineer — that is TOR70's contractor's role.
5. **DCCE's 3-step handoff process is fixed** (from the Strategic Alignment Deck, accepted by DCCE):
   (a) prioritize use cases and produce Functional Specifications for TOR70 to build, (b) define
   minimum website content scope for TOR70, (c) review and certify the governance framework for
   adoption.

Source for all five: `ψ/incubate/DCCE/CRDB/inbox_source/The Enterprise Data System Development
Lifecycle.md`, `ψ/incubate/DCCE/CRDB/output/00_Strategy_Reports/2026-06-11-Strategic-Alignment-Deck-Final.md`,
`ψ/incubate/DCCE/CRDB/inbox_note/2026-06-11-Meeting-with-Director-Toey-Reflection.md`.

## Approved Research Areas

**Iteration 4 (closed — synthesized, agy feedback appended):**
1. What does a complete, well-formed business-requirements package look like for enterprise-data-
   platform software development specifically? Standard components, and what "good" looks like for
   each.
2. How does such a package get organized/sequenced across two split engagements (pre-build
   blueprint/requirements phase, then a downstream build phase) so the first's output is directly
   usable as the second's input?
3. What distinguishes a requirements package ready to support a fixed-price vendor build from one
   that isn't?
4. At a surface level: how do use-case prioritization, service/content design, and governance
   framework certification fit into this package?

**New sub-finding from iteration 4 (agy second-opinion correction — treat as settled going forward):**
NFRs split into **System NFRs** (index strategy, node sizing — TOR70's job) and **Business NFRs**
(data-freshness SLAs, regulatory compliance thresholds, uptime for critical pipelines — CRDB's job,
to be captured directly in the blueprint, not deferred as "raw material" for TOR70 to build an NFR
doc from later). This refines, not contradicts, Settled Finding 3 (CRDB = Planning/RA/Design; TOR70 =
Development onward) — Business NFRs are a Design-phase output CRDB must produce, System NFRs remain
TOR70's.

**Iteration 5 (active, approved by Boss 2026-08-05):**
1. Business NFRs for a data platform — what specifically counts as a business (not system) NFR in
   this domain, and what form CRDB should capture them in.
2. Functional Specification structure for a single prioritized use case — concrete detail/granularity
   level.
3. Use-case prioritization methodology — adapting a criticality-scale/top-N scoping rule to DCCE's 8
   named products.
4. Data Contract + Assumption Log structure — what these artifacts typically contain (surfaced by agy
   as the standard mitigation for the "ambiguous adjectives" fixed-price failure mode).
5. Technical/business content vs. procurement boundary — where CRDB's deliverable content should stop
   and TOR70's procurement/SOW should start.

**Candidate areas for iteration 6 — not yet approved, held back as lower-urgency, draft only after
iteration 5's findings and Boss's explicit sign-off:**
- Asset-type governance / differentiated metadata standards (content vs. data vs. service assets).
- RACI matrix construction practice for data-management lifecycle processes.
- Data governance committee design (committee vs. single owner role, mandate/chair structure).
- Governance-framework certification/adoption checklist.
- Asset lifecycle operational model (create → approve → publish → track → archive).
- Sitemap-as-lifecycle-spine / content governance (lowest priority — not meaningfully surfaced in
  iteration 4; confirm with Boss it's still wanted before drafting).

## Explicitly Out of Scope (any iteration)

- **Line-agency partnership / R&D data-sharing strategy.** Public-sector relationship strategy, not
  something the two research notebooks (requirements-engineering / data-architecture literature) will
  meaningfully answer. This is Boss's own strategic judgment call, not a research question — do not
  query it, do not synthesize findings toward it.

## How to Use This File

- **Claude**, before writing any `iteration-N/01_query_pack.md`: check each question against Settled
  Findings and Out of Scope. Do not draft a question that re-opens a settled item or touches an
  out-of-scope topic.
- **Agy**, before querying an iteration's pack: cross-check each question against this file. If one
  conflicts, do not query it — append a `## Agy Scope Flag` section to that `01_query_pack.md`
  explaining the conflict, and wait for Claude to revise rather than executing it.
- **Agy**, during the second-opinion pass on `02_synthesis.md`: check that no conclusion restates a
  Settled Finding as if it were still open, and that no new tangent outside the Approved Research
  Areas has been introduced. Flag both in the `## Agy Second-Opinion Feedback` section.
- This file is updated by Claude only, after each iteration's synthesis is finalized and Boss has
  approved the next iteration's scope — never mid-iteration.
