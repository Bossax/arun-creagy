# Interoperability and schema extraction for sharpening [`5.3.6`](ψ/incubate/DCCE/CRDB/inbox_source/CRDB%20-%20TOR.md:190)

**Source scope:** Extracted only from [`2026-01-23-A Comprehensive Analysis of Data Modeling, Interoperability, and Risk Assessment Frameworks.md`](ψ/incubate/DCCE/CRDB/inbox_source/2026-01-23-A%20Comprehensive%20Analysis%20of%20Data%20Modeling,%20Interoperability,%20and%20Risk%20Assessment%20Frameworks.md). No other source is analyzed in this artifact.

## 1. What this source contributes to the logic of [`5.3.6`](ψ/incubate/DCCE/CRDB/inbox_source/CRDB%20-%20TOR.md:190)

- The source does **not** provide a ready-made loss-and-damage form. Its value is narrower and more structural: it shows how an MVD should be designed so that disaster records can remain interoperable across hazard science, administrative reporting, and later analytical extensions.
- The strongest pattern in the source is that interoperability depends less on having one giant schema than on having:
  - stable identifiers
  - explicit entity relationships
  - controlled vocabularies / taxonomies
  - metadata and provenance fields that make later interpretation possible
  - extension logic that separates minimal intake from richer downstream models
- This sharpens the task in [`5.3.6`](ψ/incubate/DCCE/CRDB/inbox_source/CRDB%20-%20TOR.md:190): the argument should move from “compare standards and draft a form” to “derive a minimum interoperable event schema with traceable mappings into later analytical and reporting layers.”

## 2. Identifier logic

### Strongest extracted claims

- The source explicitly points to the use of **persistent identifiers** as a foundation of federated interoperability, including [`DOIs`](ψ/incubate/DCCE/CRDB/inbox_source/2026-01-23-A%20Comprehensive%20Analysis%20of%20Data%20Modeling,%20Interoperability,%20and%20Risk%20Assessment%20Frameworks.md:312) and [`ORCIDs`](ψ/incubate/DCCE/CRDB/inbox_source/2026-01-23-A%20Comprehensive%20Analysis%20of%20Data%20Modeling,%20Interoperability,%20and%20Risk%20Assessment%20Frameworks.md:312), as part of a linked “Climate Internet.”
- In the ontology examples, every meaningful datum is treated as an identifiable object in relation to other objects, not just as an unlabelled table cell. The [`SOSA`](ψ/incubate/DCCE/CRDB/inbox_source/2026-01-23-A%20Comprehensive%20Analysis%20of%20Data%20Modeling,%20Interoperability,%20and%20Risk%20Assessment%20Frameworks.md:77) pattern depends on distinguishable entities for feature of interest, observed property, sensor, and procedure.
- The source also shows identifier logic in pragmatic tabular systems: [`IAMC`](ψ/incubate/DCCE/CRDB/inbox_source/2026-01-23-A%20Comprehensive%20Analysis%20of%20Data%20Modeling,%20Interoperability,%20and%20Risk%20Assessment%20Frameworks.md:178) standardizes dimensions such as [`Model`](ψ/incubate/DCCE/CRDB/inbox_source/2026-01-23-A%20Comprehensive%20Analysis%20of%20Data%20Modeling,%20Interoperability,%20and%20Risk%20Assessment%20Frameworks.md:182), [`Scenario`](ψ/incubate/DCCE/CRDB/inbox_source/2026-01-23-A%20Comprehensive%20Analysis%20of%20Data%20Modeling,%20Interoperability,%20and%20Risk%20Assessment%20Frameworks.md:182), [`Region`](ψ/incubate/DCCE/CRDB/inbox_source/2026-01-23-A%20Comprehensive%20Analysis%20of%20Data%20Modeling,%20Interoperability,%20and%20Risk%20Assessment%20Frameworks.md:182), [`Variable`](ψ/incubate/DCCE/CRDB/inbox_source/2026-01-23-A%20Comprehensive%20Analysis%20of%20Data%20Modeling,%20Interoperability,%20and%20Risk%20Assessment%20Frameworks.md:182), and [`Unit`](ψ/incubate/DCCE/CRDB/inbox_source/2026-01-23-A%20Comprehensive%20Analysis%20of%20Data%20Modeling,%20Interoperability,%20and%20Risk%20Assessment%20Frameworks.md:182) so records can be interpreted consistently across models.

### Implication for the MVD

- The MVD should assume that **every event record needs a persistent event identifier**.
- It should also preserve foreign-key style identifiers for the main referenced entities, at minimum:
  - administrative geography code
  - hazard classification code
  - reporting organization / source record id
  - version or revision id
- If the form does not preserve stable identifiers, then later crosswalks to Sendai, DDPM internal reports, or sector extensions become brittle manual reconciliation rather than true interoperability.

## 3. Event/entity structure

### Strongest extracted claims

- The source repeatedly favors **entity-based modeling** over flat undifferentiated reporting.
- Under [`SOSA`](ψ/incubate/DCCE/CRDB/inbox_source/2026-01-23-A%20Comprehensive%20Analysis%20of%20Data%20Modeling,%20Interoperability,%20and%20Risk%20Assessment%20Frameworks.md:77), a datum becomes meaningful only when linked to:
  - [`Feature of Interest`](ψ/incubate/DCCE/CRDB/inbox_source/2026-01-23-A%20Comprehensive%20Analysis%20of%20Data%20Modeling,%20Interoperability,%20and%20Risk%20Assessment%20Frameworks.md:79)
  - [`Observed Property`](ψ/incubate/DCCE/CRDB/inbox_source/2026-01-23-A%20Comprehensive%20Analysis%20of%20Data%20Modeling,%20Interoperability,%20and%20Risk%20Assessment%20Frameworks.md:81)
  - [`Sensor`](ψ/incubate/DCCE/CRDB/inbox_source/2026-01-23-A%20Comprehensive%20Analysis%20of%20Data%20Modeling,%20Interoperability,%20and%20Risk%20Assessment%20Frameworks.md:83)
  - [`Procedure`](ψ/incubate/DCCE/CRDB/inbox_source/2026-01-23-A%20Comprehensive%20Analysis%20of%20Data%20Modeling,%20Interoperability,%20and%20Risk%20Assessment%20Frameworks.md:85)
- The source also highlights event-driven architectures in [`WIS 2.0`](ψ/incubate/DCCE/CRDB/inbox_source/2026-01-23-A%20Comprehensive%20Analysis%20of%20Data%20Modeling,%20Interoperability,%20and%20Risk%20Assessment%20Frameworks.md:54), especially publish-subscribe notification logic and “notify and retrieve” exchange patterns rather than monolithic store-and-forward records.
- In risk modeling, the source shows that data systems commonly distinguish at least the following conceptual entities:
  - [`Hazard`](ψ/incubate/DCCE/CRDB/inbox_source/2026-01-23-A%20Comprehensive%20Analysis%20of%20Data%20Modeling,%20Interoperability,%20and%20Risk%20Assessment%20Frameworks.md:108)
  - [`Exposure`](ψ/incubate/DCCE/CRDB/inbox_source/2026-01-23-A%20Comprehensive%20Analysis%20of%20Data%20Modeling,%20Interoperability,%20and%20Risk%20Assessment%20Frameworks.md:108)
  - [`Vulnerability`](ψ/incubate/DCCE/CRDB/inbox_source/2026-01-23-A%20Comprehensive%20Analysis%20of%20Data%20Modeling,%20Interoperability,%20and%20Risk%20Assessment%20Frameworks.md:108)
- The knowledge-graph examples further reinforce that interoperable systems separate entities and relationships, e.g. [`Hazard`](ψ/incubate/DCCE/CRDB/inbox_source/2026-01-23-A%20Comprehensive%20Analysis%20of%20Data%20Modeling,%20Interoperability,%20and%20Risk%20Assessment%20Frameworks.md:102) impacts an exposure unit, which links to an economic activity and then to a social impact.

### Implication for the MVD

- The MVD should not be framed as one flat “loss and damage row.”
- The minimum interoperable structure implied by the source is closer to:
  1. **Event** entity
  2. **Location** entity
  3. **Hazard** classification entity
  4. **Impact observation** entity or repeating group
  5. **Source / procedure** entity
- At minimum, the event record should be able to link one event to multiple impact observations, because human impact, asset impact, and sectoral impact are conceptually different observed properties even when reported in one form.
- This matters for DDPM because a single undifferentiated total prevents later separation of hazard occurrence, measured impact, valuation basis, and reporting method.

## 4. Crosswalk logic across standards

### Strongest extracted claims

- The source shows interoperability as a **mapping problem across heterogeneous but related schemas**, not as perfect uniformity.
- [`WIS 2.0`](ψ/incubate/DCCE/CRDB/inbox_source/2026-01-23-A%20Comprehensive%20Analysis%20of%20Data%20Modeling,%20Interoperability,%20and%20Risk%20Assessment%20Frameworks.md:54) relies on open standards from [`OGC`](ψ/incubate/DCCE/CRDB/inbox_source/2026-01-23-A%20Comprehensive%20Analysis%20of%20Data%20Modeling,%20Interoperability,%20and%20Risk%20Assessment%20Frameworks.md:58) and [`W3C`](ψ/incubate/DCCE/CRDB/inbox_source/2026-01-23-A%20Comprehensive%20Analysis%20of%20Data%20Modeling,%20Interoperability,%20and%20Risk%20Assessment%20Frameworks.md:58), with queryable metadata through [`OGC API - Records`](ψ/incubate/DCCE/CRDB/inbox_source/2026-01-23-A%20Comprehensive%20Analysis%20of%20Data%20Modeling,%20Interoperability,%20and%20Risk%20Assessment%20Frameworks.md:62).
- [`WCMP`](ψ/incubate/DCCE/CRDB/inbox_source/2026-01-23-A%20Comprehensive%20Analysis%20of%20Data%20Modeling,%20Interoperability,%20and%20Risk%20Assessment%20Frameworks.md:64) shows that discovery metadata itself can be standardized in web-native formats like [`GeoJSON`](ψ/incubate/DCCE/CRDB/inbox_source/2026-01-23-A%20Comprehensive%20Analysis%20of%20Data%20Modeling,%20Interoperability,%20and%20Risk%20Assessment%20Frameworks.md:64).
- The source treats controlled vocabularies and ontologies as the mechanism that makes cross-domain mapping possible. [`ENVO`](ψ/incubate/DCCE/CRDB/inbox_source/2026-01-23-A%20Comprehensive%20Analysis%20of%20Data%20Modeling,%20Interoperability,%20and%20Risk%20Assessment%20Frameworks.md:92) is useful precisely because it normalizes environmental terms into a queryable hierarchy rather than leaving each source to name things ad hoc.
- The discussion of the [`GGA`](ψ/incubate/DCCE/CRDB/inbox_source/2026-01-23-A%20Comprehensive%20Analysis%20of%20Data%20Modeling,%20Interoperability,%20and%20Risk%20Assessment%20Frameworks.md:223) is blunt about comparability: without a **controlled vocabulary** for terms like resilient practices, country reporting becomes non-comparable and global aggregation becomes invalid.
- The [`IAMC`](ψ/incubate/DCCE/CRDB/inbox_source/2026-01-23-A%20Comprehensive%20Analysis%20of%20Data%20Modeling,%20Interoperability,%20and%20Risk%20Assessment%20Frameworks.md:178) example adds a warning: text hierarchies can support exchange, but when the meaning of a hierarchy is only implicit in strings, ambiguity remains during data integration.

### Implication for the MVD

- The MVD should be designed with an explicit **crosswalk layer**, not just fields.
- The strongest interoperable pattern suggested by the source is:
  - one internal event schema
  - one internal controlled hazard vocabulary
  - one mapping table to external standards / indicators
  - one metadata layer declaring what each field means, in what unit, and by what method it was derived
- For [`5.3.6`](ψ/incubate/DCCE/CRDB/inbox_source/CRDB%20-%20TOR.md:190), the comparison across IPCC, Sendai, and other standards should therefore be argued as a **semantic crosswalk exercise**, not merely as a side-by-side checklist.

## 5. Minimum metadata and provenance expectations

### Strongest extracted claims

- The source is explicit that authoritative climate data requires metadata on **spatial and temporal resolution, uncertainty estimates, and provenance** in the [`ECV`](ψ/incubate/DCCE/CRDB/inbox_source/2026-01-23-A%20Comprehensive%20Analysis%20of%20Data%20Modeling,%20Interoperability,%20and%20Risk%20Assessment%20Frameworks.md:33) framework.
- Under [`SOSA`](ψ/incubate/DCCE/CRDB/inbox_source/2026-01-23-A%20Comprehensive%20Analysis%20of%20Data%20Modeling,%20Interoperability,%20and%20Risk%20Assessment%20Frameworks.md:77), provenance is not optional decoration; it is part of the meaning of an observation because the reading is linked to sensor characteristics and observation procedure.
- The source says semantic annotation with rigorous provenance is critical to distinguish true signals from artifacts, and to assess dataset “fitness for purpose.”
- The finance and adaptation sections reinforce this pattern. For medium-likelihood adaptation activities, the record must carry a **climate rationale** linking the activity to an identified risk, rather than leaving the adaptation claim implicit.

### Minimum metadata fields implied for the MVD

- The MVD should preserve, at minimum, the following metadata / provenance fields for each key reported impact:
  - reporting source / institution
  - source document or source record reference
  - observation or reporting date
  - event date or event period
  - geographic resolution
  - unit of measure
  - method / procedure used
  - uncertainty, confidence, or estimate-status flag
  - revision / validation status
- If DDPM wants an MVD that can later support national synthesis, these fields are not “nice to have.” They are the minimum conditions for preventing ambiguous totals from being re-used as if they were comparable evidence.

## 6. Interoperability constraints relevant to DDPM and the proposed MVD

### Strongest extracted constraints

- The source repeatedly shows that **physical systems and administrative systems use different organizing logics**. For example, hydrological risk may be organized by sub-basin while response systems work by province or municipality. This means interoperability cannot assume one geography fits every use case.
- It also shows a persistent tension between **global standardization** and **hyper-local granularity**. Standardization supports aggregation and comparison; local detail supports operational usefulness. The MVD has to sit between these two pressures.
- The source states that adaptation data suffers from a “missing middle”: many systems have high-level hazard projections and high-level project lists, but lack the spatial socio-economic linkage needed to connect them. This is relevant because a DDPM intake form that captures only event totals may reproduce the same gap.
- Another constraint is semantic ambiguity: without controlled vocabularies, categories cannot be aggregated reliably. The [`GGA`](ψ/incubate/DCCE/CRDB/inbox_source/2026-01-23-A%20Comprehensive%20Analysis%20of%20Data%20Modeling,%20Interoperability,%20and%20Risk%20Assessment%20Frameworks.md:236) example is the clearest warning.
- The [`IAMC`](ψ/incubate/DCCE/CRDB/inbox_source/2026-01-23-A%20Comprehensive%20Analysis%20of%20Data%20Modeling,%20Interoperability,%20and%20Risk%20Assessment%20Frameworks.md:185) discussion adds a second warning: even when a format looks standardized, hidden ambiguity persists if hierarchy and meaning are carried only in text labels.

### Practical implication for DDPM

- DDPM should not aim for one universal field called “loss and damage” and assume this is interoperable.
- A workable MVD should instead preserve at least these separations:
  - hazard occurrence vs. impact observation
  - human impacts vs. asset impacts vs. service disruptions
  - measured count vs. estimated monetary value
  - raw local category vs. mapped standard category
  - reported fact vs. derived estimate
- The source supports a restrained architecture: a minimal core schema plus explicit mappings and provenance is more interoperable than a large form with mixed concepts and unclear semantics.

## 7. Focused note on how this source should change the argument structure of [`5.3.6`](ψ/incubate/DCCE/CRDB/inbox_source/CRDB%20-%20TOR.md:190)

- The current task in [`5.3.6`](ψ/incubate/DCCE/CRDB/inbox_source/CRDB%20-%20TOR.md:190) should be argued less as a search for the “best standard form” and more as a **schema-design problem under interoperability constraints**.
- The argument should be re-ordered along this logic:
  1. international standards differ because they are built for different analytical units and purposes
  2. therefore the CRDB should define a minimum internal event schema rather than copy any one standard wholesale
  3. that schema must preserve identifiers, entity separation, controlled vocabularies, and provenance
  4. interoperability should be achieved through crosswalk tables and metadata declarations, not by collapsing concepts into a single field set
  5. the proposed MVD should be judged by whether DDPM can capture it rapidly **and** whether DCCE can later map it into broader reporting and analytical frameworks
- The strongest structural claim extractable from this source is that **interoperability is achieved by explicit semantics and provenance, not by superficial field similarity**.
- Therefore, this source should push [`5.3.6`](ψ/incubate/DCCE/CRDB/inbox_source/CRDB%20-%20TOR.md:190) toward defending a **minimal but semantically disciplined MVD**, not a comprehensive form that over-promises comparability.
