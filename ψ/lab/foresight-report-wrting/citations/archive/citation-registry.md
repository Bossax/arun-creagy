# Foresight 2590 – Canonical Citation Registry (Template)

> One row per *canonical* source used in the foresight report and its supporting artifacts.

Use this file as the single source of truth for bibliographic information. `SRC_ID` values from this table should be reused in:

- [ψ/lab/foresight-report-wrting/citations/artifact-paragraph-source-map.md](ψ/lab/foresight-report-wrting/citations/archive/artifact-paragraph-source-map.md)
- [ψ/lab/foresight-report-wrting/citations/report-claim-evidence-map.md](ψ/lab/foresight-report-wrting/citations/archive/report-claim-evidence-map.md)

## Table 1 – Canonical sources

Append rows as new sources are accepted into the evidence base.

**Column guidance**

- `SRC_ID` – Stable ID, e.g. `SRC-TH-LAW-2542-EDU`, `SRC-UNICEF-2024-YOUTH-SOUTH`, `SRC-LOCAL-INTERVIEW-ORPHANS-FGD1`.
- `Short_Label` – Brief human-readable label used in internal notes.
- `Full_Citation_APA_Style` – Target-format citation text (Thai or English as appropriate).
- `Source_Type` – e.g. `law`, `report`, `article`, `dataset`, `book`, `thesis`, `policy-doc`, `interview`, `transcript`.
- `Year` – Publication year (or year of data collection for some datasets).
- `Primary_Access_Path` – File path under `ψ/` or an external URL.
- `Local_Language` – `th`, `en`, or mixed; helpful for later drafting choices.
- `Notes` – Any remarks on reliability, usage constraints, or relevance.



| SRC_ID                       | Short_Label                                         | Full_Citation_APA_Style                                                                                            | Source_Type   | Year | Primary_Access_Path                                                                                                     | Local_Language | Notes                                                                                                                                                                                        |
| ---------------------------- | --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ------------- | ---- | ----------------------------------------------------------------------------------------------------------------------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SRC-EXAMPLE-TH-LAW-EDU-2542  | Thai Education Act 2542                             | *[Example placeholder] พระราชบัญญัติการศึกษาแห่งชาติ พ.ศ. ๒๕๔๒.* ราชกิจจานุเบกษา.                                  | law           | 1999 | ψ/path/to/source-or-url                                                                                                 | th             | Replace this example row with real entries.                                                                                                                                                  |
| SRC-MEMO-VULN-SBP-2026       | Child and youth vulnerability memo SBPs             | *Child and youth vulnerability in Thailand’s southern border provinces* [internal analytical memo].                | internal-memo | 2026 | ψ/lab/foresight-report-wrting/artifacts/source/Child and Youth Vulnerability in Thailand’s Southern Border Provinces.md | en             | Deep-research synthesis on conflict, identity, institutional trust, and youth vulnerability in the southern border provinces; primary internal evidence for Draft 2 signals chapter framing. |
| SRC-MEMO-LEARN-PATHWAYS-2026 | Learning pathways memo SBPs                         | *Learning pathways and education trajectories in Thailand’s southern border provinces* [internal analytical memo]. | internal-memo | 2026 | ψ/lab/foresight-report-wrting/artifacts/source/Learning Pathways.md                                                     | en             | Analytical memo on learning pathways and education trajectories; core evidence for life-course trends and opportunity structures.                                                            |
| SRC-MEMO-LIVELIHOODS-2026    | Livelihoods and opportunity structures memo SBPs    | *Livelihoods and opportunity structures in Thailand’s southern border provinces* [internal analytical memo].       | internal-memo | 2026 | ψ/lab/foresight-report-wrting/artifacts/source/Livelihoods in the Deep South.md                                         | en             | Analytical memo on household economy, labour markets, and livelihoods; core evidence for economic vulnerability patterns across the life course.                                             |
| SRC-MEMO-BELONGING-2026      | Belonging, identity, and cultural capital memo SBPs | *Belonging, identity, and cultural capital in Thailand’s southern border provinces* [internal analytical memo].    | internal-memo | 2026 | ψ/lab/foresight-report-wrting/artifacts/source/Belonging, identity, and cultural capital.md                             | en             | Analytical memo on belonging, identity, and cultural capital; core evidence for institutional trust and identity-related vulnerability patterns.                                             |

