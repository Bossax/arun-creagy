---
date: 2026-04-17 17:23
type: info
status: raw
significance: important
---
# DCCE Practice: Knowledge Assets and Media Synthesis

Current operational reality at DCCE regarding the creation of communication media, policy digests, and knowledge assets:

1. **Ad-Hoc Data Sourcing:** Staff frequently research data independently on the internet (e.g., current global temperatures, new climate laws) to produce media.
2. **Primary Outlet:** Facebook is often used as the main communication channel, rather than a structured national portal.
3. **The "Orphan Knowledge" Problem:** While media products cite data sources, the *structured data* behind these sources (the raw numbers, spreadsheets, GIS files) is almost never captured or stored centrally by DCCE.
4. **Consultant Dependency:** Consultants are routinely hired to produce media. They use their own curation and research methods, resulting in final outputs (PDFs, JPEGs) being submitted without the underlying data packages.

**Architectural Implication:**
This inconsistency requires a "Source Registration Protocol" to be sealed into the Enterprise Data Architecture (EDM). The EDM must model COMMUNICATION_ASSET alongside EXTERNAL_REFERENCE (for staff) and EVIDENCE_PACKAGE (for consultants) to ensure the provenance and raw data of published media are governed, even if the data is not fully hosted in the DCCE data lake.

Logged via /fyi