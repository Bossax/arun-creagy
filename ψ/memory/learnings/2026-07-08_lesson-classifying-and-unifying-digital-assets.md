---
id: learning_2026-07-08_lesson-classifying-and-unifying-digital-assets
type: learning
title: # Lesson: Classifying and Unifying Digital Assets via Data Governance Semantics
concepts: [metadata-governance, csv-parsing, data-dictionary, dcce]
tags: [metadata-governance, csv-parsing, data-dictionary, dcce]
created: 2026-07-08
indexed_at: 2026-07-08T14:25:20.448Z
updated_at: 2026-07-08T14:25:20.448Z
hash: sha256:f00af304240bdd77b2023e67164c88e6ed8b3cddb1db3d36409a1f00243a503f
source: rrr: Unified Database Compilation
project: github.com/sitth/arun_creagy
arra_id: learning_2026-07-08_lesson-classifying-and-unifying-digital-assets
arra_type: learning
arra_concepts: [metadata-governance, csv-parsing, data-dictionary, dcce]
arra_created: 2026-07-08T14:25:20.448Z
---

# # Lesson: Classifying and Unifying Digital Assets via Data Governance Semantics

# Lesson: Classifying and Unifying Digital Assets via Data Governance Semantics

When compiling an organization-wide digital asset catalog from multiple heterogeneous sources (like a web sitemap and a CKAN data catalog), avoid conflating logical formats with governance classifications. 

## The Resolution: Two-Layer Hierarchy
To build a clean, scalable metadata database, implement a two-layer classification split:
1. **Asset Type (Governance Status)**: Defines the logical class of the resource and who owns it:
   - `Data Product`: Packaged, user-facing offerings designed for reuse (systems, interactive dashboards).
   - `Data Asset`: Managed data resources owned, governed, and maintained internally.
   - `Knowledge Asset`: Human-readable context, synthesis, or know-how (reports, manuals, SOPs, multimedia).
2. **Format Type (Physical File Representation)**: Defines the actual storage structure:
   - `Dataset` (CSV, XLSX, SHP, database).
   - `Document` (PDF, Word, PPTX).
   - `Web Application` (interactive web portals).
   - `YouTube Video` (multimedia tutorials).

## Implementation Rules
- Dynamically parse catalog files using RFC-4180 state-machine parsing to survive embedded newlines and quotes.
- Enforce strict validation rules (e.g., `Data Asset` must map to `Dataset` format; a PDF registered in the data catalog must be reclassified as a `Document` under `Knowledge Asset` rather than treated as a raw data asset). This prevents the \"Data Availability\" vs \"Content Readiness\" illusion.

---
*Added via Oracle Learn*
