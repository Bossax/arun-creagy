---
title: When transitioning draft artifacts (like CSV glossaries) into database-ready for
tags: [Data Engineering, Automation, Semantic Consistency, Curation]
created: 2026-05-28
source: rrr: REPO
---

# When transitioning draft artifacts (like CSV glossaries) into database-ready for

When transitioning draft artifacts (like CSV glossaries) into database-ready formats ("hardening"), automated processes must treat manual user curation as immutable. Automation must only target the *gaps*. When merging files, the user-edited file must be defined as the absolute base. AI-generated data should only be injected into explicitly empty fields or newly defined metadata columns (like `CDM_Entity_Link` or `Semantic_Owner`), never overwriting populated primary content fields. Furthermore, parsing CSV data via raw text inspection is highly error-prone ("sparse data blindness"); missing columns must be audited systematically rather than visually to avoid "hallucinating" completeness.

---
*Added via Oracle Learn*
