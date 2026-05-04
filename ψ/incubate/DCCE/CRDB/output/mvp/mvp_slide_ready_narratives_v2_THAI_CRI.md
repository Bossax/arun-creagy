
# CRDB MVP Master Narratives: Anchored in Thailand CRI Context

This document provides the "Original Material" for workshop slides, specifically grounded in the transition from **Track 1 (Ex-post Risk)** to **Track 2 (Action-oriented Resilience)** as defined in the Thailand Climate Resilience Index (CRI) methodology.

---

## MVP-1: The Policy Briefing Service (The Exporter)
**The Narrative: Closing the "Granularity Mask" Gap**

### 1. The Story
Current Thai spatial risk maps operate at the **Provincial scale**. However, as noted in CRI Phase 1, this "smooths out" local hotspots and masks intra-provincial variability. A Governor might see their province is "Amber," but they don't know which specific **Local Administrative Organizations (LAOs)** are actually underwater. 

### 2. The Solution: Contextualizing the Grid
This service takes the high-resolution 12km climate grids and "unmasks" them for the planner. It translates "Spatial Risk" into **Administrative Readiness**.

### 3. Service Level Trade-offs
*   **Level 1: The Tactical Narrative (Scoping)**:
    *   **Logic**: Uses existing Provincial rankings to generate a "District-level Scoping Note."
    *   **Action**: Allows a Governor to prioritize which districts need deep-dive resilience assessments.
*   **Level 2: The Technical Design **
    *   **Logic**: Integrates Local Performance Assessment (LPA) data with 12km rainfall projections.
    *   **Action**: Provides specific engineering safety margins for municipal infrastructure projects.

---

## MVP-2: The Climate-Disaster Pipeline (The Intake)
**The Story: The "Quiet Nudge" from Relief to Resilience**

### 1. The Narrative
Thailand's disaster data (from DDPM) is currently focused on **"Track 1" metrics**: deaths, affected people, and relief fund spending (e.g., the 9,000 Baht per household flood relief). This data is "Ex-post"it only looks backward at what we spent to survive.

### 2. The Solution: Strategic Data Reuse (The Bridge)
This MVP doesn't ask DDPM to change their work. Instead, it **reframes their disaster statistics onto a Climate Timeline**. By plotting "Relief Fund Spending" against "Hazard Frequency" over 30 years, we turn a "DRM Record" into a **"Climate Signal."**

### 3. Service Level Trade-offs
*   **Level 1: The Pragmatic Bridge (Strategic Triage)**:
    *   **Mechanism**: Join DDPM relief budget tables with hazard frequency records. Filter for climate events.
    *   **Outcome**: A visualization showing **"Accumulated Climate Tax"**�the long-term cost of reactive relief in specific provinces.
    *   **Action**: **The Quiet Nudge.** By demonstrating the *value* of this analysis, we nudge DDPM to improve their data granularity without making it a "governance demand."
*   **Level 2: The Impact Schema (Resilience Accounting)**:
    *   **Mechanism**: Automated correlation between climate return periods and sectoral losses (Agri/Health).
    *   **Outcome**: A predictive model of **Resilience Gaps**. (e.g., "Provinces with low LPA scores see 40% higher relief costs for the same hazard intensity.")
    *   **Action**: Justifies shifting national budgets from **Relief (Track 1)** to **Adaptation (Track 2)**.

---

## MVP-3: The Endorsed Data Inventory (The Catalog)
**The Story: Defining the "Canonical Truth" for Thailand**

### 1. The Narrative
With multiple versions of climate data circulating (CRI Phase 1, DCCE Risk Maps, International Models), Thai technical officers suffer from "Source Confusion." They don't know which data is **Endorsed** for official National Plans or Provincial budget requests.

### 2. The Solution: The "Badge of Trust"
This MVP provides a **Curated Directory** of assets that are "Official" for specific sectors. It solves the **"Trust Gap"** identified in the CRI Phase 1 audit.

### 3. Service Level Trade-offs
*   **Level 1: The Endorsed Gallery**: A pre-vetted list of "The Top 5" datasets for Thai Agriculture, Water, and Health.
*   **Level 2: The Federated Discovery**: A full technical catalog linking local DCCE nodes with international data stores.

---

## MVP-4: The Uncertainty Data Shield (The Interpreter)
**The Story: "Decision Readiness" for Non-Experts**

### 1. The Narrative
Non-expert officials (e.g., Provincial Treasurers) often take model projections as "Absolute Truth." This leads to the **misuse of data** for site-specific engineering that the models weren't designed for.

### 2. The Solution: The Readiness Label
Borrowing from the **IPCC Confidence Lexicon**, this MVP adds a "Readiness Layer" to Thai climate data. It tells the user: "This data is High Confidence for **Regional Scoping**, but Low Confidence for **Bridge Engineering**."

### 3. Service Level Trade-offs
*   **Level 1: Readiness Labels**: A traffic light system (Green/Amber/Red) indicating the **Administrative Weight** the data can support.
*   **Level 2: The Statistical Shield**: Technical "Fan Charts" showing the probabilistic range of future Thai climate scenarios.

