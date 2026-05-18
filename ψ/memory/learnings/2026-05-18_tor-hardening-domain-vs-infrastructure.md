# Learning: Hardening TORs - Domain vs. Infrastructure Separation

**Date**: 2026-05-18
**Context**: Reviewing the 25M THB National Climate Adaptation Database TOR.

## The Pattern
In large-scale government IT procurement, there is a recurring "Expertise Illusion" where a contractor's track record in **Infrastructure/Hardware** (e.g., IoT sensors, document management) is mistaken for **Domain Expertise** (e.g., climate risk modeling, environmental science).

## The Risk
Contractors with a "Document-Centric" or "Hardware-Centric" background (like Ditto PCL) will naturally lean toward building a **Static Portal** (DMS-style) rather than an **Enterprise Data System** (API-first). This results in:
1.  **Manual Ingestion Bottlenecks**: Designing systems for manual file uploads rather than automated harvesting.
2.  **Shallow Semantic Models**: Ignoring the complex relationships between climate hazards, exposure, and vulnerability in favor of a flat "Table of Files."

## The Correction (Hardening Strategy)
1.  **Pre-defined Domain Logic**: Do not let the contractor "invent" the conceptual model. Mandate the use of an existing **Conceptual Data Model (CDM)** and **User Journey (NCAIF)** as non-negotiable inputs.
2.  **Personnel Bifurcation**: Explicitly separate "Systems Engineering" roles from "Climate Domain" roles in the TOR. Mandate that domain leads must have published research or deep experience in the specific science (e.g., CMIP6 modelers), not just "IT management."
3.  **Decoupled Architecture**: Mandate a **Data Space** approach (Decoupled planes) to prevent monolithic vendor lock-in and ensure API-first interoperability.

## Concepts
#tor-review #governance #enterprise-data #climate-adaptation #contractor-fit
