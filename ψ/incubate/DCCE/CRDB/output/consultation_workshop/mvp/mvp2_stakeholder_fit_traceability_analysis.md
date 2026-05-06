# MVP-2 — Stakeholder Fit & Traceability Analysis (Evidence-Grounded)

**Scope**: This note consolidates the “evidence-grounded stakeholder–MVP traceability analysis” for **MVP-2**, cross-checking:

- MVP-2 definition and service levels in the **v2 prototype card**, and
- stakeholder interview summary notes (DDPM, NESDC, DLA, MSDHS, TBA, NSO)

into a single, workshop-usable reference.

---

## 1) MVP-2 (latest working definition)

From the current v2 service prototype card, MVP-2 is framed as **Climate Disaster Statistics** (the “Intake”):

- A **re-indexing pipeline** that takes disaster / relief statistics and joins them to hazard/context to support **climate-timescale** reasoning (30+ years) and Loss & Damage use.
- **Level 1 (Pragmatic)**: initial data integration → hotspot/cost ranking dashboard.
- **Level 2 (Ideal)**: standardized impact schema → climate-driven loss model and sectoral loss profiles.

Reference: [`mvp_grounded_dummies_v2_narrative_cards.md`](ψ/incubate/DCCE/CRDB/output/consultation_workshop/mvp/mvp_grounded_dummies_v2_narrative_cards.md)

---

## 2) Stakeholder experience today (historical impact/damage + event statistics)

### 2.1 The experience is “hunt + interpret + reconcile”, not “retrieve and use”

**Pattern A — Discoverability friction (catalog/metadata absent):**

- MSDHS reports no central catalog; staff waste time hunting across websites; missing metadata/data dictionaries forces phone calls to source agencies to understand meaning.
  - Evidence: [`Interview Summary - MSDHS.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20MSDHS.md)

**Pattern B — Data exists but is optimized for relief operations, not climate-loss evidence:**

- DDPM’s reporting chain is one-way (LAO → district → province → central). Province QC exists, but central cannot ground-truth.
- Known “lag/noise” and category errors drive a request for screening/AI cleaning.
  - Evidence: [`Interview Summary DDPM.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20DDPM.md)

**Pattern C — Credibility gap: “relief payouts” do not represent “true loss”:**

- NESDC’s major pain: DDPM statistics reflect compensation payouts rather than true economic damage, missed opportunity days, and cascading disruptions.
  - Evidence: [`Interview Summary - NESDC.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20NESDC.md)

**Pattern D — Workarounds (proxy overlays and reconstruction):**

- NSO overlays population/agriculture/establishment baselines onto DDPM disaster areas to estimate affected volumes (fusion by overlay rather than a unified impact schema).
  - Evidence: [`Interview Summary - NSO.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20NSO.md)

---

## 3) Beneficiaries (who benefits, at which MVP-2 service level)

### 3.1 Direct beneficiaries

**DDPM operators / provincial QC / data stewards**

- **Benefit**: reliability flags + screening discipline that matches the known “lag/noise” intake reality.
- **Best-fit level**: **Level 1** (pragmatic) is immediately actionable.
- Evidence: [`Interview Summary DDPM.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20DDPM.md)

**NESDC (macroeconomic planning + Loss & Damage framework users)**

- **Benefit**: separates “relief payout” from “true loss” logic; provides a path to standardized economic loss accounting.
- **Best-fit level**: **Level 2** (impact schema / loss modeling).
- Evidence: [`Interview Summary - NESDC.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20NESDC.md)

**DLA / LAOs (local planning + budget justification)**

- **Benefit**: “hotspot ranking / accumulated cost” evidence that is legible and reusable for local budget narratives.
- **Best-fit level**: **Level 1** (dashboard + ranking) is most immediately useful.
- Evidence: [`Interview Summary - DLA.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20DLA.md)

**MSDHS (vulnerable group targeting + disaster response coordination)**

- **Benefit**: reduces hunt/interpret burden; improves historical event layers that MSDHS already uses for overlays.
- **Best-fit level**: **Level 1** for operational overlays; **Level 2** only if impact schema becomes granular by subgroup.
- Evidence: [`Interview Summary - MSDHS.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20MSDHS.md)

### 3.2 Partial / indirect beneficiaries (boundary note)

**Banks / TBA member banks**

- They already procure DDPM data and need standardized baselines and better interpretability.
- MVP-2 can provide supporting “event-loss evidence”, but it is **not** the core product for asset-level probabilistic hazard modeling.
- Evidence: [`Interview Summary - Thai Bankers' Association.md`](ψ/incubate/DCCE/CRDB/output/Interview%20summary%20notes/Interview%20Summary%20-%20Thai%20Bankers%27%20Association.md)

---

## 4) Use cases answered by MVP-2

### 4.1 Canonical cluster mapping (NCAIF)

MVP-2 maps primarily to the use-case cluster:

- **Post-event impact and loss assessment** (UC-01 / UC-09 style patterns)
  - Primary users: DDPM, NESDC, DCCE analysts
  - Related MVP(s): **MVP-2 + MVP-3**

Reference: [`2026-03-25-5.2.3-NCAIF-Use-Case-Mapping.md`](ψ/incubate/DCCE/CRDB/output/2026-03-25-5.2.3-NCAIF-Use-Case-Mapping.md)

### 4.2 Concrete MVP-2 use cases (operationalized)

**UC-A — Event/impact record with reliability flags**

- Intake DDPM-style event statistics.
- Apply “pending review / reliability flags” to represent data confidence.
- Preserve revision history so users can cite a version.

**UC-B — “Relief payout vs true loss” crosswalk for Loss & Damage**

- Keep relief compensation figures as *one* variable.
- Add a structure that can host estimated economic loss (direct + indirect) distinctly.

**UC-C — Long-term climate-disaster hotspot evidence for prioritization**

- Re-index event statistics to reveal long-run accumulation patterns.
- Provide a “where to target programmes” basis for planning and advocacy.

---

## 5) What to call this analysis

Suggested label(s):

- **Evidence-grounded stakeholder–MVP traceability analysis** (most precise)
- **Stakeholder needs → MVP fit mapping** (short)
- **Persona/use-case mapping for MVP-2** (workshop-friendly)

---

## 6) Design guardrails (to prevent scope drift)

1. MVP-2 Level 1 should not be described as a fully automated national pipeline unless the operating model is explicitly agreed.
2. MVP-2 outputs must carry **quality signals** (flags, revision history) so users do not mistake noisy operational data as stable historical truth.
3. MVP-2 should avoid promising asset-level bank-grade risk modeling; direct that to foundational layers + endorsement + uncertainty guidance.

