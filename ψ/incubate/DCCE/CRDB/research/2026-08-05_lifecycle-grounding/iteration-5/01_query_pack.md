# Iteration 5 Query Pack — Business NFRs, Functional Specs, Prioritization, Data Contracts, Procurement Boundary

Phase B, iteration 5. Read `SCOPE_LEDGER.md` before querying — every question below has already been
checked against Settled Findings and Out of Scope; do not query beyond this list without Claude
revising it first. Note the new sub-finding logged from iteration 4 (Business NFRs vs. System NFRs) —
question 1 below builds directly on it.

## Notebook: Business requirement for SW development (`5133ef48-564c-40df-bdd1-142bb7e5bdf3`)

1. What specifically counts as a "business" non-functional requirement (as opposed to a system/ infrastructure NFR) for a data platform — e.g., data-freshness SLAs, regulatory compliance thresholds, uptime for critical pipelines — and in what form should a pre-build requirements package capture them (a thresholds table, narrative text, both)?
2. At the level of a single prioritized use case, what should a Functional Specification contain, and what level of detail/granularity is expected — enough to freeze scope for a fixed-price vendor build without over-specifying implementation?
3. What methodology is used to prioritize a list of candidate use cases or data products down to asmall "first wave" set — criteria, scoring approach, and how ties or disagreements betweenstakeholders are typically resolved?
4. What does a Data Contract (formalizing schema and quality expectations between a data producer andconsumer) typically contain, and what does an explicit Assumption Log (documenting assumptions madeduring requirements-gathering to bound vendor liability) typically look like in practice?
5. Where should the line sit between a data platform's technical/business requirements content and its procurement/contractual content (Statement of Work, cost, delivery schedule, acceptance procedures) — is there a standard checklist for what belongs on each side of that boundary?

## Notebook: Enterprise Data Architecture (`3adf8897-245c-43c6-aec9-8977f2aab2fb`)

1. What specifically counts as a "business" non-functional requirement (as opposed to a system/ infrastructure NFR) for a data platform, and in what form should a pre-build requirements packagecapture them?
2. At the level of a single prioritized use case or data domain, what should a Functional
   Specification / requirements artifact contain, and what level of detail is expected to support a fixed-price build?
3. What methodology is used to prioritize a set of candidate data products or domains down to a small "first wave" set for initial delivery — criteria and scoring approach?
4. What does a Data Contract typically contain in a data-governance context, and how does an Assumption Log or equivalent risk-bounding artifact typically get structured and maintained?
5. Where should the line sit between a data platform's technical/architectural requirements content and its procurement/contractual content — is there a standard practice for this boundary?
