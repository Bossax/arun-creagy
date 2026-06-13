# Revised Pillar 2 Execution Plan: "Layer 0" Service Protocols

## Strategic Objective
Pivot the design of the 8 NCAIF climate services away from end-user dashboards/UI and toward **"Layer 0" foundational protocols**. The services will be defined as certified datasets, mathematical damage functions, and machine-readable APIs that external SaaS platforms, consultants, and line agencies can consume.

## Bounded Concrete Deliverables

To avoid open-ended "design" tasks, Pillar 2 will produce three bounded artifacts for the Alpha Service (Loss & Damage / Financial Decision Support):

### Deliverable 1: The "Layer 0" Data Dictionary & Schema
*   **What it is:** A strict tabular specification of the exact fields, data types, and update frequencies required to output a localized climate risk assessment.
*   **Why it's bounded:** It contains no wireframes or UI mockups. It is purely the JSON/CSV output schema that an agency or private firm would pull from DCCE via API.
*   **Target Completion:** End of Week 1.

### Deliverable 2: Localized Vulnerability Curve Library (V1)
*   **What it is:** A documented set of mathematical formulas (stage-damage functions) that convert physical hazards (e.g., 1m flood depth) into economic loss (e.g., % structural damage).
*   **Why it's bounded:** Instead of a generic "report," this is a catalog of formulas (e.g., referencing the Komolafe models for Chao Phraya buildings or Copernicus models for rice crops) that DCCE officially adopts for risk translation.
*   **Target Completion:** Week 2.

### Deliverable 3: System-Design API Handoff Protocol
*   **What it is:** A 3-page technical brief defining exactly what the next software contractor must build to host the data (database specs, API endpoint structures, query parameters like `?lat=` and `?lon=`).
*   **Why it's bounded:** It clearly draws the line between DCCE's responsibility (the science and the data) and the vendor's responsibility (the cloud infrastructure and API gateway).
*   **Target Completion:** Week 3.

## Execution Steps
1.  **Extract Parameters:** Pull the specific data requirements from the Seed Community use cases (e.g., NESDC's need to separate relief spending from true economic loss).
2.  **Draft Schema:** Write the data dictionary (Deliverable 1) that fulfills those parameters.
3.  **Map Formulas:** Attach the recognized mathematical damage curves (Deliverable 2) to the hazard parameters.
4.  **Seal the Protocol:** Package these into the API Handoff (Deliverable 3) for Director Toey to review as the tangible "Service Detail."