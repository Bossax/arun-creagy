# Use Cases to Services: Conceptual Model

## Purpose

This note captures the conceptual relationship between **use cases** and **services** in the CRDB / NCAIF Pillar 2 workstream. It explains the implicit logic behind the transition from stakeholder use cases to the 8 key climate information services.

## Relevant seal chain

| Layer       | Relevant entry                                                                                                                                                                                         | Meaning                                                                                                                                              |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Evidence    | [`E-051`](../../../CRDB-Evidence-Registry.md:84), [`E-052`](../../../CRDB-Evidence-Registry.md:85), [`E-056`](../../../CRDB-Evidence-Registry.md:89), [`E-057`](../../../CRDB-Evidence-Registry.md:90) | Raw use-case extraction, service synthesis, failure of arbitrary use-case lists, and later service-level gap-analysis chain.                         |
| Trigger     | [`T-032`](../../../CRDB-Trigger-Log.md:65), [`T-033`](../../../CRDB-Trigger-Log.md:66)                                                                                                                 | The project discovered that loose use-case lists were arbitrary, then moved toward service-platform and data-gap logic.                              |
| Change      | [`CH-025`](../../../CRDB-Change-Log.md:61), [`CH-026`](../../../CRDB-Change-Log.md:62)                                                                                                                 | Pivot from arbitrary markdown lists to purpose-first, machine-readable service intelligence; then service baseline to policy-facing data-gap report. |
| Deliverable | [`D-043`](../../../CRDB-Deliverable-Map.md:71), [`D-044`](../../../CRDB-Deliverable-Map.md)                                                                                                            | Sealed 8-service intelligence package, then service-level data-gap policy report.                                                                    |

The important point is that [`D-043`](../../../CRDB-Deliverable-Map.md) is not merely a nicer report. It is the resolved abstraction layer after the project judged earlier use-case lists as too fragmented.

## How this project understands use cases

The clearest definition appears in [`2026-05-09-honest-feedback-on-previous-work-to-collect-comprehensive-use-cases-of-climate-data.md`](../../inbox_note/2026-05-09-honest-feedback-on-previous-work-to-collect-comprehensive-use-cases-of-climate-data.md):

> A use case is the pure use of climate and non-climate information to achieve a specific goal.

In this model, a use case is not:

- a dataset request,
- a platform module,
- a generic “need,”
- a service name,
- or a user persona.

A use case is a **decision-purpose statement** grounded in an actor’s actual work. It contains:

1. the goal or pain point,
2. the required data or information products,
3. the most relevant functional group.

Examples in [`2026-05-09-honest-feedback-on-previous-work-to-collect-comprehensive-use-cases-of-climate-data.md`](../../inbox_note/2026-05-09-honest-feedback-on-previous-work-to-collect-comprehensive-use-cases-of-climate-data.md) are phrased as practical uses: estimate economic loss, run stress testing, identify vulnerable groups during emergencies, and find official datasets.

The use-case unit is therefore close to:

> Actor X uses climate and non-climate information Y to make decision Z under constraint C.

## What services are in this model

Services are a higher-level abstraction created by clustering many use cases.

The process is described in [`บทสรุปความต้องการใช้งานบริการข้อมูลสารสนเทศด้านภูมิอากาศ_v6.md`](บทสรุปความต้องการใช้งานบริการข้อมูลสารสนเทศด้านภูมิอากาศ_v6.md):

1. process interviews and workshop comments,
2. identify purposes for using information,
3. collect the data and product formats needed to achieve those purposes,
4. understand decision processes, expected service formats, and obstacles,
5. build an inventory of use cases,
6. group use cases by similar data type, analysis pattern, presentation format, and purpose,
7. synthesize service types that respond to each use-case group.

The same report makes the crucial conceptual jump in [`บทสรุปความต้องการใช้งานบริการข้อมูลสารสนเทศด้านภูมิอากาศ_v6.md`](บทสรุปความต้องการใช้งานบริการข้อมูลสารสนเทศด้านภูมิอากาศ_v6.md:15): the 8 services are not tied to sector-specific wishes or individual datasets. They are designed so their principles, workflow, components, and purpose can apply across sectors.

So services are not “things stakeholders asked for” one by one. Services are:

> reusable institutional capabilities that DCCE can provide repeatedly across multiple user groups and decision contexts.

## Relationship between use cases and services

The implicit model is:

```text
interview / workshop statement
→ specific use case
→ clustered use-case family
→ reusable service platform
→ data / method / governance requirements
→ gap analysis and implementation roadmap
```

The technical specification expresses the same model operationally. Phase 1 extracts all use cases with originating agencies, decision moments, institutional pain points, and hard specs in [`Pillar_02_UseCases_FunctionalSpecs_Technical_Specification_v5.0.md`](Pillar_02_UseCases_FunctionalSpecs_Technical_Specification_v5.0.md). Phase 2 blends the inventory into services by technical function, not agency name, in [`Pillar_02_UseCases_FunctionalSpecs_Technical_Specification_v5.0.md`](Pillar_02_UseCases_FunctionalSpecs_Technical_Specification_v5.0.md). Phase 3 productizes the result into a service intelligence report in [`Pillar_02_UseCases_FunctionalSpecs_Technical_Specification_v5.0.md`](Pillar_02_UseCases_FunctionalSpecs_Technical_Specification_v5.0.md).

This means:

- **Use cases preserve stakeholder specificity.** They keep the actor, goal, pain, decision moment, and hard technical requirement.
- **Services remove accidental specificity.** They strip away agency-specific wording and turn repeated demand patterns into reusable DCCE capabilities.
- **Services must remain traceable back to use cases.** Otherwise they become consultant abstractions.
- **Use cases alone are too fragmented for procurement.** This is why [`E-056`](../../../CRDB-Evidence-Registry.md) records the failure of arbitrary use-case drafts and why [`CH-025`](../../../CRDB-Change-Log.md:61) pivots to canonical service platforms.

---
# :LiBrickWall:
## Concrete example: translating agency use cases into the Loss & Damage service

The business example in [`2026-06-12_crdb-loss-damage-business-service-example.md`](2026-06-12_crdb-loss-damage-business-service-example.md:1) shows the translation from multiple agency use cases into one reusable service wedge: **Loss and Damage Economic Impact Briefing Service**.

### Relevant agency use cases

The service does not begin with a generic report. It begins with several concrete stakeholder problems:

- **NESDC** needs to separate relief spending from true economic loss so macroeconomic reporting and budget logic do not confuse compensation with damage.
- **DDPM** needs a way to convert disaster records and physical damage into economic categories that can support policy and recovery decisions.
- **Budget and planning users** need a defensible briefing that can support investment, prioritization, and allocation under uncertainty.
- **Technical analysts** need a repeatable method for identifying the event, affected geography, loss categories, and unresolved assumptions.

These are different use cases because the decision moment, institutional actor, and intended outcome are different. But they cluster around the same service need.

### What is shared across those use cases

The shared demand pattern is not the agency name. It is the capability pattern:

- intake the event context,
- map the affected geography and sector,
- distinguish direct damage, indirect loss, relief spending, and uncertainty,
- translate physical impacts into economic language,
- produce a briefing that a decision-maker can use immediately,
- keep the method traceable to named data sources and owners.

That shared pattern is what becomes the service.

### The reusable service bundle

In the business example, the service package is intentionally repeatable:

1. event context brief,
2. loss-category mapping table,
3. proxy-value calculation template,
4. uncertainty / limitation note,
5. stewardship and metadata sheet.

This is the service. A specific output for one province or one event is merely an **instance** of the service.

### Why this is a service, not a one-off report

If DCCE produced only one customized memo for NESDC, that would still be a use-case response.

It becomes a service when the same core bundle can be reused for:

- another province,
- another agency,
- another disaster event,
- another reporting cycle,
- another budget or recovery decision.

So the service survives the customer change; the use case does not. The use case is the trigger. The service is the durable response architecture.

### Translation chain for the L&D example

```text
NESDC / DDPM / planning demand
→ event-specific use case
→ shared L&D need across agencies
→ Loss & Damage Economic Impact Briefing Service
→ event briefing instance with sources, categories, proxies, and uncertainty notes
→ decision support for budget / recovery / reporting
```

This is the exact logic behind the service-first model: many use cases become one service only after the shared capability has been extracted, named, and packaged.

## Important correction: services are not simply supply

It is too flat to say “use cases = demand” and “services = supply.” The actual model is more careful:

- Use cases are **empirical demand signals**.
- Services are **designed response patterns**.
- Data inventories are **supply reality**.
- Gap analysis compares **designed service requirements** against **actual data supply**.

This is what [`รายงานการวิเคราะห์ช่องว่างข้อมูลและข้อเสนอแนะเชิงนโยบาย_v5.0.md`](รายงานการวิเคราะห์ช่องว่างข้อมูลและข้อเสนอแนะเชิงนโยบาย_v5.0.md:47) does: it says NCAIF must treat services as bundles of capabilities, not merely a centralized data repository. The same report explains in [`รายงานการวิเคราะห์ช่องว่างข้อมูลและข้อเสนอแนะเชิงนโยบาย_v5.0.md`](รายงานการวิเคราะห์ช่องว่างข้อมูลและข้อเสนอแนะเชิงนโยบาย_v5.0.md:75) that the technical bottleneck is not gathering data alone, but transforming raw data into information that users can use to decide, design projects, and justify budgets.

The mature chain is:

```text
Use cases = evidence of what people are trying to do.
Services = reusable capability designs for helping them do it.
Data gap analysis = whether current datasets can actually support those services.
Governance = who owns, certifies, updates, and protects the service.
```

## How the project understands the 8 key services

The 8 services are not a direct list of “top 8 requests.” They are the result of abstraction.

They answer this question:

> What institutional service capabilities must DCCE build if these many scattered use cases are to be supported in a durable, cross-sectoral way?

That is why the services are phrased as broad capabilities:

- certified climate data repository,
- high-resolution spatial risk analytics,
- finance and budget decision evidence,
- historical loss and damage assessment,
- engineering design variables,
- multi-hazard impact-based early warning,
- adaptation policy monitoring, evaluation, and learning,
- uncertainty governance.

Each service can host many use cases. Each use case may also depend on more than one service. For example, a local budget-justification use case may require:

- Service 1 for endorsed baseline data,
- Service 2 for local risk resolution,
- Service 3 for budget evidence,
- Service 8 for uncertainty handling.

This is why services are better understood as **platform capabilities** than as individual features.

## Concise conceptual read

Use cases are **ground-truth decision situations**: concrete, actor-specific uses of climate and non-climate information to accomplish work.

Services are **DCCE’s reusable response architecture**: grouped, sector-agnostic capability bundles synthesized from many use cases, designed to be governable, procurable, and testable against actual data supply.

The relationship is translational, not merely hierarchical:

```text
Use cases keep the human and institutional reality intact.
Services translate that reality into something DCCE can own, govern, procure, and improve over time.
```

That is the structural integrity of the Pillar 2 service-intelligence logic.
