# Conceptual Design & Vision: The "Guided Synthesis" CRDB Platform

## 1. The Core Paradigm Shift
The platform must pivot from a traditional "Data Portal" (which risks becoming a "Portal Trap"—a static, rarely updated list of files) to a **"Guided Synthesis Engine."** It is built on the reality that DCCE's target audience (policymakers, local planners) has low data literacy but requires high-confidence, actionable insights. The default user experience is "I need a clear answer," not "I want to explore raw data."

## 2. The 60/40 Hybrid Strategy
*   **60% Synthesis & Translation:** The platform acts as a "Knowledge Broker." It ingests complex climate data and outputs human-readable narratives, policy briefs, and actionable recommendations.
*   **40% Trust & Guardrails:** When users do interact with data, the platform enforces strict metadata standards, promotes "official" baselines, and implements hard guardrails against data misuse.

## 3. Key UX & Architectural Patterns

### A. Question-First Navigation (Intent-Driven)
Instead of a search bar for datasets, the home screen is framed around user intents:
*   *“What climate risks matter for my province?”*
*   *“What adaptation options are available for the agricultural sector?”*
*   *“Where are the official baseline datasets for national reporting?”*
This prevents users from being overwhelmed by unstructured catalogs.

### B. Automated Briefing Packs (Operationalizing MVP-1)
The primary output of the platform is not a CSV or a map layer, but a **3–5 page auto-generated Policy Brief**.
*   **Components:** Executive summary, key risks (top 3–5), recommended actions, and a basic evidence panel.
*   **Exportable:** PDF, PowerPoint, or Word outline, ready for management meetings.

### C. Plain-Language "Evidence Labels" & Guardrails (Operationalizing MVP-4)
To prevent the misuse of probabilistic climate data (a major risk for low-literacy users), every chart and dataset features mandatory "Evidence Labels":
*   **Confidence Level:** High / Medium / Low with a one-sentence explanation.
*   **Appropriate Use Warning:** E.g., *"Good for strategic provincial planning. NOT suitable for designing drainage pipe diameters."*

### D. The "Endorsed Baselines" Registry (Operationalizing MVP-3)
A highly visible, curated registry of "Official" datasets that have been validated by inter-agency committees (e.g., TMD, ONEP, DCCE). This solves the persistent problem of different departments using conflicting numbers for the same climate hazard.

### E. Action Cards & Starter Packages
Instead of raw lists of adaptation measures, the platform provides "Action Cards" (e.g., "Urban Tree Planting" instead of "Nature-Based Cooling Intervention"). It offers "Starter Packages" bundled by sector and region to help planners prioritize interventions based on cost, feasibility, and impact.

## 4. The "Data Lake" Runway (Backend Future-Proofing)
While the frontend is strictly curated for non-technical users, the backend must be built on a **Decoupled Data Space Architecture** (aligning with DCAT 3.0 and OGC APIs). 
*   **Why?** This prevents vendor lock-in and ensures that as DCCE’s internal data literacy and capacity mature, the platform can seamlessly transition into a full Data Lake capable of supporting advanced analytical pipelines and AI-driven modeling, without needing to rebuild the entire system.

## 5. Next Steps for TOR Translation
With this vision established, the TOR redlines will logically follow:
1.  **Mandating Domain Expertise:** Requiring the vendor to supply Climate Science experts to build the "Synthesis" logic (the Action Cards, Briefing Packs), not just IT developers.
2.  **Decoupled Architecture:** Forcing the strict separation of the "Frontend Explainer" from the "Backend Data Space."
