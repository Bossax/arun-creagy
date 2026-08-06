
# CRDB MVP Master Narratives: Slide-Ready Technical Scoping

This document provides the "Original Material" for creating workshop slides. Each MVP is framed with a **Narrative Story**, **Technical Logic**, and **Empirical Proof** to ensure presenter confidence.

---

## MVP-1: The Policy Briefing Service (The Exporter)
**The Story: From "Data Chaos" to "Strategic Clarity"**

### 1. The Narrative
In the current state, a Local Government planner receives a "Grid Map" showing a 2-degree temperature rise. For them, this is abstract noise. They cannot translate "2 degrees in a 12km grid" into a request for a new coastal defense wall or a change in agricultural zoning. There is a **"Narrative Gap"** between the climate science and the administrative action.

### 2. The Solution: The Automated Briefing Generator
This service acts as a "Translator." It takes the technical gridded data and automatically wraps it in a **Strategic Briefing**. It tells the planner: "In your province, this temperature shift is consistent with a 20% increase in flash-flood risk, which historically costs your local economy X million Baht."

### 3. Service Level Trade-offs
*   **Level 1: The Tactical Narrative (Scoping)**:
    *   **Mechanism**: Uses regional "Proxy Trends" and pre-written vulnerability modules.
    *   **Outcome**: A 2-page briefing focused on **Prioritization**. (e.g., "Which 3 districts are most at risk this decade?")
    *   **Action**: Enables **Policy Scoping** and high-level budget requests.
*   **Level 2: The Technical Design (The Climate Allowance)**:
    *   **Mechanism**: High-resolution downscaling matched to specific local infrastructure assets.
    *   **Outcome**: An engineering-ready report with **Climate Allowances**. (e.g., "Build this bridge 0.5m higher to survive 2050 floods.")
    *   **Action**: Enables **Engineering Specification** and site-specific construction design.

### 4. Empirical Proof (The Confidence)
*   **UKCP (UK Met Office)**: Successfully uses the "Summary Briefing" model to bridge national projections to 12km local grids.
*   **Climate-ADAPT (EU)**: Uses sector-specific "Overview Reports" to ensure policy makers don't have to be climate scientists to act.

---

## MVP-2: The Climate-Disaster Pipeline (The Intake)
**The Story: Turning "Relief Data" into "Resilience Advocacy"**

### 1. The Narrative
Currently, the **Department of Disaster Prevention and Mitigation (DDPM)** collects massive amounts of data, but it is "locked" in a **Relief Mindset**. They track how many blankets were given out and how much relief budget was spent. This data is **scattered and under-utilized**. For a climate planner at DCCE, this is a goldmine of evidence�if it can be re-indexed.

### 2. The Solution: Strategic Data Reuse
This MVP isn't a new "collection" tool; it is a **Re-Indexing Engine**. It reaches into the DDPM "Relief Tables" and pulls out the human and economic cost of climate events (ignoring earthquakes or accidents). It then plots these costs over a **30+ Year Climate Timescale**.

### 3. Service Level Trade-offs
*   **Level 1: The Pragmatic Join (Triage)**:
    *   **Mechanism**: Manually join "Relief Budget" tables with "Hazard Frequency" data. Filter for climate-only events.
    *   **Outcome**: A dashboard showing **"Climate-Cost Hotspots"**�where repeated low-level floods are draining the national budget.
    *   **Action**: Nudges DDPM to improve their data schema while giving DCCE the data to justify **Adaptation Spending** over "Disaster Relief."
*   **Level 2: The Automated Impact Schema**:
    *   **Mechanism**: Automated correlation between climate return periods (Intensity) and economic damage (Loss).
    *   **Outcome**: A predictive model of **Climate-Driven Loss**. (e.g., "If intensity increases by 10%, relief costs will rise by 40%.")
    *   **Action**: Quantifies the **Economic ROI** of adaptation projects.

### 4. Empirical Proof (The Confidence)
*   **EM-DAT & UNDRR**: While they focus on DRM, the **World Weather Attribution (WWA)** methodology proves that linking specific impacts to climate trends is the only way to move policy. We are building the "Data Bridge" between these two worlds.

