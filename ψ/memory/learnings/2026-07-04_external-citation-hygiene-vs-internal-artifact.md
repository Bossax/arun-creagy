---
id: learning_2026-07-04_external-citation-hygiene-vs-internal-artifact
type: learning
title: # External Citation Hygiene vs. Internal Artifact References
concepts: [reporting, citations, academic-integrity, deliverable-hygiene, DCCE]
tags: [reporting, citations, academic-integrity, deliverable-hygiene, DCCE]
created: 2026-07-04
indexed_at: 2026-07-04T04:28:51.825Z
updated_at: 2026-07-04T04:28:51.825Z
hash: sha256:532ed5f8e8d4040073e0dfcf17778a019c25c9323ab480d8586945bd74845a63
source: Arun_Creagy final_report task
project: github.com/arun_creagy/crdb
arra_id: learning_2026-07-04_external-citation-hygiene-vs-internal-artifact
arra_type: learning
arra_concepts: [reporting, citations, academic-integrity, deliverable-hygiene, DCCE]
arra_created: 2026-07-04T04:28:51.825Z
---

# # External Citation Hygiene vs. Internal Artifact References

# External Citation Hygiene vs. Internal Artifact References

## Context
When drafting official government reports or final deliverables, agents must maintain a strict boundary between **internal project tracking** and **external public references**. 

During the CRDB final report drafting, the agent was requested to insert formal references for sitemap, UX/UI, and data lifecycle sections. The agent mistakenly referenced internal deliverable and evidence codes (e.g., `[DCCE-UX, 2026]`, `[DCCE-TOR, 2026]`, `[FGD-1, 2026]`) which represent internal files and focus group sessions in the repository.

## Core Lessons

1. **Do Not Leak Internal Metadata:** Inline citations in public-facing reports must only point to publicly accessible, standard academic or official policy documents (e.g., IPCC, DGA, WMO, NOAA). Referencing private internal project names (like `DCCE-UX`) is unprofessional and confusing to external readers who have no access to these files.
2. **Deconstruct Synthesis Notes:** When an internal note (such as *User Experience Design Principles (Pack C)*) is mapped as evidence for a design choice, the agent must not cite the note itself. Instead, the agent must open that note, locate its bibliography/references section, and extract the **underlying external sources** (e.g., specific NOAA toolkits, WMO frameworks, or UX research papers) to use as the citations.
3. **Accurate Domain Mapping:** Ensure external sources map correctly to their specific fields. Do not hallucinate or lazy-map references (e.g., do not cite NOAA or the World Bank for core cognitive UX/UI concepts like progressive disclosure when the source note actually attributes those to specific UX research and behavioral science papers).
4. **Citation Format:** Follow the user's requested style carefully. In this project, standard round parentheses `(Author, Year)` are used rather than square brackets `[Author, Year]`.

## Corrective Action
Before drafting citations, identify if the reference code exists only inside the local workspace (e.g., in a `plan.md`, `Evidence-Registry.md`, or `Deliverable-Map.md`). If it is an internal deliverable, immediately find its primary external source bibliography and cite the public records instead.

---
*Added via Oracle Learn*
