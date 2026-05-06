# MVP-1 — Stakeholder Fit & Traceability Analysis (Evidence-Grounded)

**Scope**: This note consolidates the “evidence-grounded stakeholder–MVP traceability analysis” for **MVP-1**, cross-checking:

- MVP-1 definition and service levels in the **v2 service prototype card**, and
- a *small, relevant subset* of stakeholder interview summary notes (only those that evidence MVP-1’s beneficiaries, current experience, and concrete use cases),

into a single, workshop-usable reference.

---

## 1) MVP-1 (latest working definition)

From the current v2 service prototype card, MVP-1 is framed as a **Policy Briefing Service** (a “Briefing Generator”):

- **Product objective**: Turn “gridded climate data” into a **policy briefing** that a province can act on.
- **Core concept**: An automated **Briefing Generator** translating technical gridded data into a short **Strategic Briefing** linked to practical impacts and priorities.
- **Level 1 (Pragmatic)**: Tactical Narrative / Scoping
  - **Mechanism**: proxy trends + pre-written vulnerability modules.
  - **Output**: 2-page **Provincial Risk Narrative** (prioritization focus).
  - **Decision support value**: “Which districts / issues should we prioritize this decade?”
  - **Action**: policy scoping, regional prioritization.
- **Level 2 (Ideal)**: Technical Design / Climate Allowance
  - **Mechanism**: higher-resolution analysis matched to infrastructure/asset context.
  - **Output**: engineering-ready **Climate Allowance** guidance (e.g., “+0.5m freeboard”, “+20% drainage capacity”).
  - **Decision support value**: “What safety margins must we apply in design/specs?”
  - **Action**: engineering specification, site design.

Reference: [`mvp_grounded_dummies_v2_narrative_cards.md`](ψ/incubate/DCCE/CRDB/output/consultation_workshop/mvp/mvp_grounded_dummies_v2_narrative_cards.md:23)

---

## 2) Stakeholder experience today (the “translation gap” is real)

MVP-1 is justified when the lived experience is not “retrieve and use climate inputs”, but instead **hunt + interpret + translate + justify**.

### 2.1 Local planners need *localized* hazard projections for budget planning, but must “hunt”

- DLA reports that for hazard data, LAOs must *hunt for information themselves* (e.g., DDPM/TMD) and that local governments “desperately need localized hazard projections” to plan annual budgets.
  - Evidence: [`Interview Summary - DLA.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20DLA.md:1)

### 2.2 Technical planners / regulators are missing climate-adjusted design inputs (rainfall; heat at fine scale)

- DPT identifies “climate-change-adjusted rainfall projection gap” as urgent; historical rainfall is no longer sufficient for drainage and flood-planning work. They also note that below provincial scale they effectively do not yet have usable heat data.
  - Evidence: [`Interview Summary - DPT.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20DPT.md:1)

### 2.3 Sector policy units need *authoritative, accepted* long-term projection data to justify decisions upstream (budget allocators)

- OTP states an urgent requirement for DCCE to provide authoritative long-term climate forecast data (esp. hydrological projections) for reuse across ministries; and that they want support communicating the necessity of worst-case scenario planning to budget allocators.
  - Evidence: [`Interview Summary - OTP.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20OTP.md:1)

### 2.4 Local/provincial implementers face a “wait for disaster” budgeting loop (need defensible, decision-ready evidence)

- UDDC describes a “wait for disaster” budgeting loop (post-disaster relief is fundable; proactive adaptation is difficult). They explicitly request authoritative DCCE risk maps that local governments can use as proof to justify proactive adaptation budgets.
  - Evidence: [`Interview Summary - UDDC.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20UDDC.md:1)

---

## 3) Beneficiaries (who benefits, at which MVP-1 service level)

### 3.1 Level 1 (Pragmatic) — “Provincial Risk Narrative” (2-page scoping brief)

**Direct beneficiaries (primary fit):**

- **LAOs / local planners and budget preparers** (via DLA role): need localized hazard projections + an easy-to-digest evidence pack that can be used for annual budget justification and prioritization.
  - Evidence: [`Interview Summary - DLA.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20DLA.md:1)

- **Provincial/regional planners and implementers working under “prove it to budget allocators” constraints** (e.g., local actors described through UDDC experience): benefit from a narrative that converts climate inputs into legible “why this matters / where to target” logic.
  - Evidence: [`Interview Summary - UDDC.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20UDDC.md:1)

**Partial / indirect beneficiaries (boundary note):**

- **Sector policy units** (e.g., OTP) that need a reusable narrative framing to support communication upstream (but they may still require their own technical models for sector-specific analysis).
  - Evidence: [`Interview Summary - OTP.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20OTP.md:1)

### 3.2 Level 2 (Ideal) — “Climate Allowance” (engineering/design-ready guidance)

**Direct beneficiaries (primary fit):**

- **Technical regulators / integrators in built environment and infrastructure planning** (e.g., DPT): need climate-adjusted design inputs that can be applied as safety margins or planning parameters.
  - Evidence: [`Interview Summary - DPT.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20DPT.md:1)

- **Sector infrastructure planners** (e.g., OTP): benefit when allowance-style guidance is accepted and repeatable across ministries (so they do not need to rebuild bespoke projection logic each time).
  - Evidence: [`Interview Summary - OTP.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20OTP.md:1)

**Boundary note (what Level 2 is *not*):** Level 2 is about **design guidance and allowances** (decision-ready engineering inputs), not a promise of full asset-level probabilistic modelling for every sector.

---

## 4) Use cases answered by MVP-1

### 4.1 Canonical cluster mapping (NCAIF)

MVP-1 maps primarily to the use-case cluster:

- **Policy and budget briefing** (e.g., UC-03 provincial/LAO budget justification; policy-maker overviews)
  - Primary users: policy makers; provincial planners; budget officers
  - Related MVP(s): **MVP-1 (Briefing Pack Generator)** and **MVP-3 (Recommended Dataset Registry)**

Reference: [`2026-03-25-5.2.3-NCAIF-Use-Case-Mapping.md`](ψ/incubate/DCCE/CRDB/output/2026-03-25-5.2.3-NCAIF-Use-Case-Mapping.md:7)

### 4.2 Concrete MVP-1 use cases (operationalized)

**UC-A — 2-page Provincial Risk Narrative for prioritization (Level 1)**

- Convert gridded/proxy climate trends into a narrative usable for **decadal prioritization** (districts/issues).
- Use pre-written vulnerability modules to keep production time low while maintaining comparability across provinces.
- Primary decision: “Which districts / issues should we prioritize this decade?”

Evidence anchor (product definition): [`mvp_grounded_dummies_v2_narrative_cards.md`](ψ/incubate/DCCE/CRDB/output/consultation_workshop/mvp/mvp_grounded_dummies_v2_narrative_cards.md:23)

Evidence anchor (need for localized projections + budget justification): [`Interview Summary - DLA.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20DLA.md:1)

**UC-B — Evidence pack for proactive adaptation budgeting under audit constraints (Level 1 → Level 2 bridge)**

- Provide an “authoritative risk map + justification narrative” that helps local actors move from “post-disaster only” to defensible **proactive** proposals.
- Primary decision: “Can we justify a proactive adaptation budget request before damage is visible?”

Evidence anchor: [`Interview Summary - UDDC.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20UDDC.md:1)

**UC-C — Climate allowance guidance for planning / design standards (Level 2)**

- Translate climate-adjusted projections (e.g., rainfall extremes) into allowance-style parameters that can be used in drainage/flood planning and related built-environment guidance.
- Primary decision: “What safety margins must we apply in design/specs?”

Evidence anchor (need for climate-adjusted rainfall projections): [`Interview Summary - DPT.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20DPT.md:1)

---

## 5) What to call this analysis

Suggested label(s):

- **Evidence-grounded stakeholder–MVP traceability analysis** (most precise)
- **Stakeholder needs → MVP fit mapping** (short)
- **Persona/use-case mapping for MVP-1** (workshop-friendly)

---

## 6) Design guardrails (to prevent scope drift)

1. **Do not describe MVP-1 Level 1 as “full climate modelling.”** Level 1 is intentionally a *translation/scoping* product (proxy trends + narrative modules), not a technical modelling platform.
   - Anchor: [`mvp_grounded_dummies_v2_narrative_cards.md`](ψ/incubate/DCCE/CRDB/output/consultation_workshop/mvp/mvp_grounded_dummies_v2_narrative_cards.md:23)

2. **Do not promise that MVP-1 alone resolves “data trust / endorsed baseline” governance.** If the briefing relies on a baseline being “official,” MVP-1 must be paired with the registry/endorsement logic in MVP-3.
   - Anchor (mapping): [`2026-03-25-5.2.3-NCAIF-Use-Case-Mapping.md`](ψ/incubate/DCCE/CRDB/output/2026-03-25-5.2.3-NCAIF-Use-Case-Mapping.md:7)

3. **Level 2 should not be presented as universal, sector-complete engineering design standards.** Evidence shows different sectors need high-resolution, sector-specific inputs; MVP-1 Level 2 should be framed as *allowance guidance for targeted decisions*, with explicit applicability limits.
   - Anchor (sector need for authoritative projections + communication to budget allocators): [`Interview Summary - OTP.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20OTP.md:1)
   - Anchor (built-environment technical need for climate-adjusted rainfall projections): [`Interview Summary - DPT.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20DPT.md:1)
