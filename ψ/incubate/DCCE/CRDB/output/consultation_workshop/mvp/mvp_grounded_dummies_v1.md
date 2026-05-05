
# CRDB MVP "Grounded Dummies": Service Level Alternatives

This document presents the technical scope for the 4 MVPs, contrasting **Level 1 (Pragmatic/Actionable)** with **Level 2 (Ideal/Integrated)**.

---

## MVP-1: The Policy Briefing Service (The Exporter)
*Grounded in UKCP & Climate-ADAPT patterns.*

### Box 1: The Pain Point
Local planners have "Grid Data" but no "Narrative." They cannot explain to a Governor *why* a 12km grid shift matters for a specific provincial policy.

### Box 2: The Concept
A "Briefing Generator" that turns raw gridded projections into 2-page **Strategic Narratives**.

### Box 3: The User Journey (The Trade-off)
*   **Level 1: Tactical Scoping**: Generates a **Provincial Risk Narrative** (textual trends + proxy vulnerability indicators). *Action: Policy Scoping & Regional Prioritization.*
*   **Level 2: Technical Design**: Generates a **Local Climate Allowance Report** (e.g., "+20% Rainfall safety margin for drainage"). *Action: Engineering Specification & Site Design.*

---

## MVP-2: The Climate-Disaster Pipeline (The Intake)
*Grounded in Strategic Data Reuse of DDPM/CRI data.*

### Box 1: The Pain Point
Disaster data is owned by DRM agencies (DDPM) and focused on "Relief Budgets." Climate planners cannot see the **long-term frequency shifts** needed to justify adaptation.

### Box 2: The Concept
A pipeline that **re-indexes** scattered disaster statistics across different agencies (relief costs, affected households, agricultural damage compensation) onto **Climate Timescales (30+ years)**.

### Box 3: The User Journey (The Trade-off)
*   **Level 1: The Clean Triage**: Filter out non-climate events (earthquakes). Join relief budget tables with hazard frequency. *Action: Identify "High-Cost Climate Hotspots" for budget advocacy.*
*   **Level 2: The Impact Schema**: Automated correlation between climate drivers (return periods) and economic loss. *Action: Quantify "Climate-Driven" economic damage.*

---

## MVP-4: The Uncertainty Data Shield (The Interpreter)
*Grounded in IPCC Lexicon & NOAA Readiness Tiers.*

### Box 1: The Pain Point
The "Fear of Misuse." Planners use high-uncertainty model spreads to make site-specific decisions they weren't designed for.

### Box 2: The Concept
A "Labeling System" that translates statistical variance into **Decision Readiness Labels**.

### Box 3: The User Journey (The Trade-off)
*   **Level 1: Readiness Labels**: Traffic light system (Green = Suitable for Scoping; Red = Consultation Required). *Action: Guided decision-making for administrators.*
*   **Level 2: The Statistical Shield**: Interactive "Fan Charts" and probability spreads for advanced users. *Action: Technical risk-buffer calculation.*


---

## MVP-3: The Endorsed Data Inventory (The Catalog)
*Grounded in NOAA & Copernicus Curation patterns.*

### Box 1: The Pain Point
"Search Bar Fatigue." Technical officers find 50 versions of "Rainfall" and don't know which one is the **Official DCCE Version** for their sector.

### Box 2: The Concept
A **Curated Gallery** that explicitly tags datasets as **"Endorsed for Sector X."**

### Box 3: The User Journey (The Trade-off)
*   **Level 1: The Endorsed Gallery**: A "Top 10" list of pre-vetted datasets with "Badge of Trust." *Action: Fast-track data selection for non-experts.*
*   **Level 2: The Federated Discovery**: A full DCAT/STAC metadata search across international and local nodes. *Action: Deep research for technical modelers.*

