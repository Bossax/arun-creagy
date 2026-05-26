---
project:
  - DCCE_CRDB
tags:
  - workshop
  - analysis
  - normalization
---

# 2026-05-26_functional-intent-over-semantic-matching

## Lesson

When normalizing stakeholder demands against a predefined framework (like a Use Case Menu), prioritize matching the **functional intent** of the request over the **semantic wording** or **delivery mechanism**. 

If a stakeholder asks for an "API providing engineering design parameters for road construction," and the existing menu has a use case for "Disaster risk impact on transport infrastructure," the request maps to the *existing* use case. It is not a "New Use Case" just because the menu didn't explicitly say "API" or "Engineering standards." 

## Context

During the analysis of the CRDB Activity 2 Workshop outputs, I initially flagged highly technical stakeholder requests (e.g., APIs for water scarcity, resilient engineering parameters) as "New Use Cases" because the original Use Case Menu was written using softer, policy-oriented language (e.g., "Planning for transport infrastructure"). This led to an over-count of New Use Cases (11 instead of 6).

After an audit by the host, I re-anchored the analysis to the *canonical* definitions of the menu items. This revealed that the stakeholders were not rejecting the original design; they were validating it (77% alignment) but demanding a shift in the delivery mechanism—from "Dashboards" (Library mindset) to "APIs and Raw Parameters" (Utility mindset).

## Application

1. **Find the Anchor First**: Never attempt to map data to a numbered taxonomy (e.g., "Use Case 1.1") without first locating and reading the canonical definition of that taxonomy.
2. **Look Past the Delivery Ask**: Separate *what* the user wants to achieve (the use case) from *how* they want it delivered (the format). 
3. **Hardening vs. Novelty**: Recognize that a request for higher resolution or better format is a "Hardening" requirement for an existing use case, not a "Novel" use case.