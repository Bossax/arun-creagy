# Learning: The Semantic Prerequisite Pattern
**Category**: Data Architecture | Methodology
**Date**: 2026-05-27
**Tags**: [Glossary, CDM, EAR Catalog, Semantic Drift, Procurement Shield]

## Pattern
In complex data modeling projects involving multiple "Pillars," the **Semantic Master (Pillar 4 Glossary)** must be seeded before the **Logical Backbone (Pillar 5 CDM)** can be sealed. 

## Key Principles
1. **The ID Anchor**: Every entity in a Conceptual Data Model (CDM) must map to a unique `Term_ID` in the Business Glossary. This ensures that the "Technical Shape" of an object (Table/Entity) is bound to its "Business Intent" (Definition).
2. **Boundary Hardening**: Differentiate between "Domain Entities" (Real-world objects like Hazards/Assets) and "System Entities" (Implementation objects like Infographics/CMS Pages). Domain entities belong in the CDM; system entities belong in the CMS or a separate Metadata Catalog.
3. **Acceptance Gate Enforcement**: Use the Technical Specification to enforce prerequisites. If the spec requires a Term ID for entity acceptance, do not bypass it—pivot to seeding the glossary first.

## Why it works
This pattern prevents **Semantic Drift**, where different stakeholders or vendors interpret technical terms differently. By enforcing the "Glossary-First" approach, the project creates a "Logical Shield" that protects the client from contractor "logic invention" during the implementation phase. It ensures that the final data system is both scientifically rigorous and functionally relevant to the user journey (Sitemap).

## Implementation Example
- **Trigger**: Identifying that Pillar 5 entities lacked official definitions.
- **Evidence**: Tech Spec Section 1.1 (Requirement for P4_Term_ID).
- **Action**: Harvesting 22 terms from Sitemap v4 and Pillar 2 Use Cases; seeding Pillar 4.
- **Outcome**: A "Sealable" Pillar 5 EAR Catalog with zero semantic ambiguity.
