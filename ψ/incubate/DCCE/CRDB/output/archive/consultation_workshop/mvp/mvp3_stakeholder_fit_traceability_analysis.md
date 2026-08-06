# MVP-3 — Stakeholder Fit & Traceability Analysis (Evidence-Grounded)

**Scope**: This note consolidates the “evidence-grounded stakeholder–MVP traceability analysis” for **MVP-3**, cross-checking:

- MVP-3 definition and service levels in the **v2 service prototype card**,
- a *small, relevant subset* of stakeholder interview summary notes (only those that evidence the “official/endorsed dataset” pain, beneficiaries, and what “endorsed” must mean operationally), and
- the canonical NCAIF mapping for **baseline verification / clearinghouse**.

into a single, workshop-usable reference.

---

## 1) MVP-3 (latest working definition)

From the current v2 service prototype card, MVP-3 is framed as a **Data Inventory for Risk and Impact Assessment** (a curated inventory / “gallery”):

- **Product objective**: Solve “search fatigue” by turning many datasets into a **curated, endorsed set** that people can trust.
- **Pain point**: Users find many versions of “rainfall/temperature/etc.” and face **decision paralysis**; they need to know what is **official/endorsed** for their sector and reporting.
- **Core concept**: A curated inventory that organizes datasets by **sectoral use case** and includes visible **DCCE validation / endorsement**.
- **Level 1 (Pragmatic) — Endorsed Gallery (Curation)**
  - **Mechanism**: “Top 10 per sector” pre-vetted list + recommended use notes.
  - **Output**: endorsed dataset page (what it is, what it’s for, limitations).
  - **Decision support value**: “Which dataset should we use for official reporting / planning this month?”
  - **Action**: fast selection by non-experts; consistent reporting.
- **Level 2 (Ideal) — Federated Discovery (Integration)**
  - **Mechanism**: federated search/API bridge + full lineage metadata (DCAT/STAC-like).
  - **Output**: professional discovery tool with traceability.
  - **Decision support value**: “Which dataset is fit-for-purpose given method/coverage/lineage?”
  - **Action**: deep technical modeling; cross-sector consistency.

Reference: [`mvp_grounded_dummies_v2_narrative_cards.md`](ψ/incubate/DCCE/CRDB/output/consultation_workshop/mvp/mvp_grounded_dummies_v2_narrative_cards.md:87)

---

## 2) Stakeholder experience today (finding “official” datasets is not a solved problem)

MVP-3 is justified when the lived experience is not “discover the official dataset and apply it”, but instead **hunt + compare + reconcile + worry about liability**.

### 2.1 Decision paralysis from conflicting baselines (“verification gap”)

- NXPO explicitly describes a national **verification gap**: there is no standardized, unified baseline for climate data; agencies collect the same points but generate different numbers; and “no single agency has the authority—or the courage—to verify and declare a single source of truth.”
  - Evidence: [`Interview Summary - NXPO.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20NXPO.md:47)

- FTI similarly frames the problem as a **clearinghouse + verification** gap: hazard/water data comes from too many uncoordinated agencies; they need DCCE (or a central body) to verify and declare a **single source of truth** so users know what to trust for planning.
  - Evidence: [`Interview Summary - FTI.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20FTI.md:44)

### 2.2 “Search fatigue” and missing metadata turn discovery into phone calls

- MSDHS reports there is **no central data catalog**; staff waste time hunting across websites; and datasets often lack technical metadata / data dictionaries, forcing them to **call source agencies** just to understand how to interpret data.
  - Evidence: [`Interview Summary - MSDHS.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20MSDHS.md:30)

### 2.3 “Endorsed” is partly a governance/liability control problem

- NXPO describes a “culture of accountability” where officials are terrified to publish predictive data; if wrong, the agency/individual faces severe backlash, which **paralyzes** data sharing. They suggest shifting liability away from individuals via locked/automated systems.
  - Evidence: [`Interview Summary - NXPO.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20NXPO.md:55)

Interpretation for MVP-3: “endorsed” must be **operationally defined** (who signs off, what review cycle, what disclaimers) so staff can publish recommendations without personal risk.

---

## 3) Definition: what “endorsed” must mean operationally (minimum viable governance)

The MVP-3 card explicitly prompts: “What does ‘endorsed’ mean operationally?” and “What minimum metadata is required for trust?”

Evidence anchor (prompt): [`mvp_grounded_dummies_v2_narrative_cards.md`](ψ/incubate/DCCE/CRDB/output/consultation_workshop/mvp/mvp_grounded_dummies_v2_narrative_cards.md:111)

Grounded operational definition (MVP-3-compatible, not over-promising):

1. **Endorsed = DCCE publishes a recommendation for a specific use-context** (sector/use-case page), not a universal “best dataset.”
   - Anchor: MVP-3 organizes datasets by **sectoral use case** and recommends “Top 10 per sector”.
   - Evidence: [`mvp_grounded_dummies_v2_narrative_cards.md`](ψ/incubate/DCCE/CRDB/output/consultation_workshop/mvp/mvp_grounded_dummies_v2_narrative_cards.md:96)

2. **Endorsed = versioned + reviewable**: each endorsed dataset entry has a recommendation version/date and a review cycle (“last reviewed”, “next review”), so stakeholders can cite what was endorsed *at the time of decision*.
   - Governance pressure justification: fear/hesitancy to publish (liability) implies the endorsement must be bounded and auditable.
   - Evidence: [`Interview Summary - NXPO.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20NXPO.md:55)

3. **Endorsed = explicit “verification stance”**: endorsement must state whether DCCE is (a) verifying the numbers, (b) verifying method/metadata sufficiency, or (c) endorsing as “best available” pending further verification.
   - Justification: the “verification gap” is central; pretending everything is fully verified increases risk.
   - Evidence: [`Interview Summary - NXPO.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20NXPO.md:47)

4. **Endorsed requires minimum metadata for trust (Level 1 baseline)**:
   - Coverage (spatial/temporal)
   - Method/source (how produced)
   - Update frequency / revision expectations
   - Known limitations + “not for” statements
   - Contact / steward link (who to ask)
   - Justification: MSDHS’s experience shows that missing metadata forces phone calls and slows work.
   - Evidence: [`Interview Summary - MSDHS.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20MSDHS.md:30)

---

## 4) Beneficiaries (who benefits, at which MVP-3 service level)

### 4.1 Level 1 (Pragmatic) — Endorsed Gallery (Curation)

**Direct beneficiaries (primary fit):**

- **Policy + integrator roles needing “official baselines” to break paralysis** (e.g., NXPO-style system integrators): benefit from an endorsed shortlist that resolves “conflicting numbers” and clarifies what is acceptable for official use.
  - Evidence (verification gap / conflicting numbers): [`Interview Summary - NXPO.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20NXPO.md:47)

- **Sector users without deep metadata capacity** (e.g., MSDHS): benefit from a “use notes + limitations + definitions” page so discovery becomes “retrieve and use”, not phone calls.
  - Evidence (no central catalog; missing metadata forces calls): [`Interview Summary - MSDHS.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20MSDHS.md:30)

- **Private-sector planners needing “single source of truth” for planning** (e.g., FTI): benefit from a visible clearinghouse stance that indicates what is trusted enough for decision use.
  - Evidence: [`Interview Summary - FTI.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20FTI.md:44)

**Partial / indirect beneficiaries (boundary note):**

- **Sector technical planners** (e.g., OTP) who need authoritative projections annually: Level 1 helps them identify the endorsed baseline inputs quickly, but does not replace their sector-specific modeling.
  - Evidence (need for authoritative, accepted long-term data): [`Interview Summary - OTP.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20OTP.md:71)

### 4.2 Level 2 (Ideal) — Federated Discovery (Integration)

**Direct beneficiaries (primary fit):**

- **Advanced technical users who must evaluate fitness-for-purpose** (lineage/method/coverage), and need deeper traceability to resolve integration decisions.
  - Evidence anchor (Level 2 definition: federated search + full lineage metadata): [`mvp_grounded_dummies_v2_narrative_cards.md`](ψ/incubate/DCCE/CRDB/output/consultation_workshop/mvp/mvp_grounded_dummies_v2_narrative_cards.md:105)

**Boundary note (why Level 2 is “ideal”, not a default promise):**

- Level 2 implies federation/API bridges and rich metadata; stakeholders already struggle with basic cataloging/metadata, so Level 1 is the credible floor.
  - Evidence (catalog absence + missing data dictionaries): [`Interview Summary - MSDHS.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20MSDHS.md:30)

---

## 5) Use cases answered by MVP-3

### 5.1 Canonical cluster mapping (NCAIF)

MVP-3 maps directly to the canonical use-case cluster:

- **Baseline verification and clearinghouse** (UC-10 and related governance items)
  - Primary users: DCCE central data/governance roles; NXPO; cross-agency integrators
  - Related MVP(s): **MVP-3 (Recommended Baseline Registry)** and **MVP-4 (Uncertainty guidance and publishing standard)**

Reference: [`2026-03-25-5.2.3-NCAIF-Use-Case-Mapping.md`](ψ/incubate/DCCE/CRDB/output/2026-03-25-5.2.3-NCAIF-Use-Case-Mapping.md:10)

### 5.2 Concrete MVP-3 use cases (operationalized)

**UC-A — “Endorsed baseline shortlist” to break decision paralysis (Level 1)**

- Provide a “Top N per sector/use-case” endorsed shortlist with use notes + limitations.
- Primary decision: “Which dataset should we use for official reporting / planning this month?”
- Evidence anchor (pain + objective): [`mvp_grounded_dummies_v2_narrative_cards.md`](ψ/incubate/DCCE/CRDB/output/consultation_workshop/mvp/mvp_grounded_dummies_v2_narrative_cards.md:90)
- Evidence anchor (conflicting numbers / verification gap): [`Interview Summary - NXPO.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20NXPO.md:47)

**UC-B — “Minimum viable dataset page” that prevents interpretation errors (Level 1)**

- Each endorsed dataset page includes minimum metadata (coverage/method/update/limitations/contact) so users don’t need informal calls to interpret meaning.
- Primary decision: “Is this dataset interpretable and safe to reuse for this use-case?”
- Evidence anchor (missing metadata/data dictionary forces calls): [`Interview Summary - MSDHS.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20MSDHS.md:30)

**UC-C — “Traceability-first discovery for advanced users” (Level 2)**

- Provide federated discovery and lineage metadata so advanced users can assess fit-for-purpose across method/coverage/lineage.
- Primary decision: “Which dataset is fit-for-purpose given method/coverage/lineage?”
- Evidence anchor (Level 2 concept): [`mvp_grounded_dummies_v2_narrative_cards.md`](ψ/incubate/DCCE/CRDB/output/consultation_workshop/mvp/mvp_grounded_dummies_v2_narrative_cards.md:105)

---

## 6) What to call this analysis

Suggested label(s):

- **Evidence-grounded stakeholder–MVP traceability analysis** (most precise)
- **Stakeholder needs → MVP fit mapping** (short)
- **Persona/use-case mapping for MVP-3** (workshop-friendly)

---

## 7) Design guardrails (scope drift prevention)

1. **Do not describe MVP-3 Level 1 as a full “federated search platform.”** Level 1 is explicitly a curated, endorsed gallery (“Top 10 per sector” + use notes), not an integration-heavy discovery system.
   - Anchor: [`mvp_grounded_dummies_v2_narrative_cards.md`](ψ/incubate/DCCE/CRDB/output/consultation_workshop/mvp/mvp_grounded_dummies_v2_narrative_cards.md:99)

2. **Do not claim “endorsed = single source of truth for all users” without defining verification stance and review cycle.** Evidence shows the core problem is conflicting numbers + fear of accountability; endorsement must be bounded, versioned, and auditable.
   - Anchor (verification gap): [`Interview Summary - NXPO.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20NXPO.md:47)
   - Anchor (accountability fear): [`Interview Summary - NXPO.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20NXPO.md:55)

3. **Do not expand MVP-3 into “owning all datasets.”** A viable national model may be a clearinghouse that links to external sources rather than hosting/copying everything.
   - Anchor (clearinghouse/shopping mall model): [`Interview Summary - NXPO.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20NXPO.md:62)

4. **Do not promise that MVP-3 alone resolves uncertainty interpretation.** MVP-3 can expose limitations and metadata; standardized uncertainty interpretation belongs with MVP-4 guidance.
   - Anchor (canonical mapping: MVP-3 pairs with MVP-4 for clearinghouse + publishing standard): [`2026-03-25-5.2.3-NCAIF-Use-Case-Mapping.md`](ψ/incubate/DCCE/CRDB/output/2026-03-25-5.2.3-NCAIF-Use-Case-Mapping.md:10)
