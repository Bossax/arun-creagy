# CBI Method Reconstruction and Alignment with CRI Phase 2

Purpose: Provide an academically explicit reconstruction of the Capacity-Based Index (CBI) design and compare it with the CRI Phase 2 methodology, as groundwork for integrating CBI into the capacity tagging dictionary.

Sources:
- CBI indicator manual: [`ψ/incubate/DCCE/CRI/inbox_source/2026-04-07-CBI_Indicator_Metadata-Ai-generated-P-Tik.md`](ψ/incubate/DCCE/CRI/inbox_source/2026-04-07-CBI_Indicator_Metadata-Ai-generated-P-Tik.md)
- Thailand CBI results report: [`ψ/incubate/DCCE/CRI/inbox_source/2026-04-07-Thailand_CBI_Report-AI-generated-P-Tik.md`](ψ/incubate/DCCE/CRI/inbox_source/2026-04-07-Thailand_CBI_Report-AI-generated-P-Tik.md)
- CRI Phase 2 core: [`ψ/incubate/DCCE/CRI/output/CRI Phase 2 Methodology.md`](ψ/incubate/DCCE/CRI/output/CRI%20Phase%202%20Methodology.md)
- Frameworks synthesis: [`ψ/incubate/DCCE/CRI/output/CRI_Urban_Resilience_Frameworks_Analysis.md`](ψ/incubate/DCCE/CRI/output/CRI_Urban_Resilience_Frameworks_Analysis.md)

---

## 1. CBI design reconstruction

### 1.1 Objective and scope

- **Objective:** Quantify **provincial climate resilience capacity** across 77 provinces as part of CRI Phase 2, focusing on ability to cope, adapt, and transform in response to climate risks.
- **Unit of analysis:** Province (77 provinces), using primarily **secondary/admin data** from line agencies, with supplementary surveys where necessary.
- **Use case:** Produce a **national capacity index** and league-table style results (overall CBI score, capacity class, regional comparisons, pillar averages) for policy-making and investment prioritization.

### 1.2 Conceptual frame

CBI adopts a 3×2 frame that mirrors the CRI Phase 2 conceptual design:

- **Pillars (3):**
  - Coping Capacity – short-term ability to respond to and manage immediate climate-related disasters.
  - Adaptive Capacity – medium-term ability to adjust systems and practices to reduce vulnerability.
  - Transformative Capacity – long-term ability to restructure systems and institutions for climate-resilient pathways.

- **Dimensions (2 per pillar):**
  - Asset – tangible resources (physical, financial, human) that enable climate response.
  - Process – institutional mechanisms, policies, planning, and governance processes that determine how assets are deployed.

This yields **6 sub-dimensions** (Coping-Asset, Coping-Process, Adaptive-Asset, Adaptive-Process, Transformative-Asset, Transformative-Process) and a total of **22 indicators**.

### 1.3 Indicator framework (22 indicators)

Each indicator is assigned:
- Code (CA1–TP3)
- Pillar (Coping/Adaptive/Transformative)
- Dimension (Asset/Process)
- Unit and direction (+/−)

High-level structure:

- **Coping – Asset (CA1–CA4):**
  - Emergency shelters per tambon.
  - Emergency disaster fund per 10,000 people.
  - Rescue equipment sets per tambon.
  - Emergency medical personnel per 10,000 people.

- **Coping – Process (CP1–CP4):**
  - Existence of disaster response/evacuation plans (binary).
  - Drill frequency (times/year).
  - Warning response time (hours, negative indicator).
  - Number of risk communication channels.

- **Adaptive – Asset (AA1–AA4):**
  - Early warning systems per district.
  - Recovery budget per 10,000 people.
  - Disaster insurance coverage (% of households).
  - Protective infrastructure (km per risk area).

- **Adaptive – Process (AP1–AP4):**
  - Existence of climate adaptation plan (binary).
  - Degree of climate data integration into development plans (1–5 scale).
  - Degree of community participation in planning (1–5 scale).
  - Public climate literacy (%).

- **Transformative – Asset (TA1–TA3):**
  - Green buffer areas (% of land area).
  - Climate resilience investment per 10,000 people.
  - Climate-resilient infrastructure (% of infrastructure stock).

- **Transformative – Process (TP1–TP3):**
  - Climate-informed zoning (binary yes/no).
  - Local economic transition plan (binary yes/no).
  - Climate innovation adoption (projects per province).

Each indicator has full metadata in the manual (definition, raw data, sources, collection frequency, limitations, current status).

### 1.4 Normalization and aggregation

CBI uses a straight **min–max normalization** per indicator to map values to [0, 1]:

- For **positive** indicators (higher = better):
  - Normalized = (X − Xmin) / (Xmax − Xmin)

- For **negative** indicators (lower = better, e.g. warning response time):
  - Normalized = (Xmax − X) / (Xmax − Xmin)

Aggregation follows **equal weighting**:

- Each pillar (Coping, Adaptive, Transformative) gets weight 1/3.
- Within a pillar, Asset and Process each get weight 1/2.
- Within a sub-dimension (e.g. Coping-Asset), indicators are averaged equally.
- Final score:
  - CBI = (Coping_score × 1/3 + Adaptive_score × 1/3 + Transformative_score × 1/3) × 100.

### 1.5 Classification

CBI maps the 0–100 score into four levels:

- Very Low: < 25
- Low: 25–50
- Moderate: 50–75
- High: ≥ 75

The national report then presents:
- National average and distribution across levels.
- Regional averages and disparities.
- Top 10 / bottom 10 provinces.
- Pillar-specific averages.

### 1.6 Inferred selection and design rationale

From structure and metadata, the indicator selection seems driven by:

- **Frame fit:** Must fill 3 pillars × 2 dimensions with a small, balanced set of indicators.
- **Admin data feasibility:** Data must be available or derivable for all 77 provinces from national systems (DDPM, MOPH, NSO, NESDC, DLA, etc.).
- **Institutional legibility:** Indicators should be intuitive for DCCE and provincial officials (funds, plans, drills, infrastructure, zoning, transition, innovation).
- **Simple aggregation:** Indicators must support min–max normalization and equal weighting without complex transformations.
- **Policy salience:** Coverage across DRM, planning, finance, infrastructure, community, and innovation, while avoiding controversial or hard-to-measure constructs (e.g. enforcement intensity, equity, political conflict).

---

## 2. Alignment with CRI Phase 2 methodology

### 2.1 Conceptual stance

**CRI Phase 2** (per [`CRI Phase 2 Methodology.md`](ψ/incubate/DCCE/CRI/output/CRI%20Phase%202%20Methodology.md)):
- Defines three capacity categories (Coping, Adaptive, Transformative) with a **process- and governance-first** emphasis.
- Uses a **Social-Ecological Systems (SES)** lens: systems, agents, institutions, feedbacks.
- Treats capacity profiles as **educational tools** to move DCCE from disaster-loss thinking to a staged capacity view.

**CBI:**
- Adopts the same labels as three pillars (Coping, Adaptive, Transformative) with an asset/process split.
- Mixes process/governance indicators with many **asset-heavy proxies**.
- Focuses largely on **state-centric, administrative capacities** (plans, budgets, infrastructure, zoning), with limited explicit SES/ecosystem detail beyond green buffers.

**Assessment:**
- CBI is **conceptually compatible** at the high level (its three pillars map directly onto CRI’s three capacity categories, with similar governance notions), but it is a **narrower, more admin-oriented slice** of the full SES-based capacity picture envisaged by CRI.

### 2.2 Measurement stance (two-speed vs single score)

CRI Phase 2:
- Explicit **two-speed design**:
  - Baseline proxies from existing admin data.
  - Target process/quality metrics as future measurement goals.
- Requires a **data-richness/confidence score (0–3)** per baseline indicator.
- Frames outputs as **profiles + gap diagnostics + data investment roadmap**, not just scores.

CBI:
- Uses a single, fixed set of 22 baseline indicators, all folded into one composite CBI score.
- No explicit Target metrics or data-richness dimension in the published method (though metadata hints at limitations and current status).
- Outputs a **national score and ranking**, plus some pillar breakdowns.

**Assessment:**
- At measurement level, CBI corresponds to **one layer** of the CRI concept: the *baseline-proxy*, admin-data layer.
- It does **not implement** the two-speed or data-richness ideas; those need to be added around/above CBI if integrated.

### 2.3 Product stance (profile vs ranking)

CRI Phase 2:
- Intentionally avoids a simple ranking; emphasizes:
  - Multi-dimensional **capacity profiles**.
  - **Gap reports** and red-flag rules.
  - Educational narrative about Coping vs Adaptive vs Transformative.

CBI:
- Delivers a classic **index**:
  - Single CBI score per province.
  - Four capacity classes.
  - Top/bottom lists, regional comparisons.

**Assessment:**
- CBI’s product stance is **at odds** with the anti-ranking posture of CRI Phase 2.
- However, CBI can still serve as:
  - A **baseline capacity surface** to embed inside CRI’s profile visualizations and evidence maps.
  - A starting point for provincial conversations, provided CRI’s outputs clearly de-emphasize the single-number ranking.

### 2.4 Data and feasibility

Both CBI and CRI Phase 2:
- Rely on national admin data from DLA, DDPM, MOPH, NSO, NESDC, etc.
- Accept constraints of data poverty and missingness.

CRI Phase 2 additionally:
- Plans for **event-log-based Target metrics** where possible.
- Explicitly triangulates LPA with budgets, Sustainable City assessments, and site visits.

CBI:
- Fixes its design on what is currently measurable nationwide.
- Does not yet encode a future measurement roadmap.

**Assessment:**
- CBI is entirely consistent with CRI’s **baseline feasibility stance**, but lacks the explicit upgrade roadmap and QA mechanisms described in CRI Phase 2.

---

## 3. Academic acceptance criteria for CBI integration (draft)

From the CRI frameworks synthesis and methodology, we can derive criteria for integrating CBI into CRI without compromising academic robustness:

1. **Process/governance coherence:**
   - Indicators accepted into the tagging dictionary must support CRI’s process- and governance-oriented definition of capacity, not just physical stock counts.

2. **Two-speed compatibility:**
   - CBI indicators can be used as **Baseline proxies** but must be paired with Target metrics that represent process quality where theoretically appropriate.

3. **Data-quality transparency:**
   - Each adopted CBI indicator must carry an explicit **data-richness/confidence score (0–3)** and documented limitations, to avoid over-claiming precision.

4. **SES and cross-project fit:**
   - Indicators should be interpretable within SES framing and compatible with CRDB/BTR governance work (e.g. as operationalizations of governance, finance, data, or ecosystem-related levers).

5. **Product integrity:**
   - CBI scores and classes may be used as **contextual baselines**, but CRI outputs must remain profile-first and evidence-annotated, not reduced to the CBI composite score.

6. **Political and institutional defensibility:**
   - Where CBI indicators align with existing mandates and are already accepted by DCCE, integration can proceed with clear documentation; where they diverge conceptually (e.g. reinforce asset bias), they may be relegated to contextual status rather than becoming core indicators.

These criteria will be used in the crosswalk and tagging dictionary v2 to decide, for each CBI indicator, whether it should be:
- Adopted as a **Baseline proxy** for an existing concept.
- Elevated into a **new indicator concept** (if SES-relevant and previously missing).
- Treated as **supplementary context** only.

---

## 4. Next execution steps

With this reconstruction in place, the next steps in the integration plan are:

1. Build a **per-indicator crosswalk** (CA1–TP3) mapping each CBI indicator to:
   - Capacity tier, asset/process, governance function, SES relevance, and likely data-richness.

2. Use the acceptance criteria above to classify each indicator as Type A/B/C for integration into the tagging dictionary v2.

3. Draft [`ψ/incubate/DCCE/CRI/output/CRI_Capacity_Tagging_Dictionary_v2_CBI.md`](ψ/incubate/DCCE/CRI/output/CRI_Capacity_Tagging_Dictionary_v2_CBI.md) and a bridging method note once the crosswalk is complete.
