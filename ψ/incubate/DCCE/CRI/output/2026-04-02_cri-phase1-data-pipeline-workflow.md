## CRI Phase 1 Data Pipeline — Process View

This diagram focuses on the **process steps** you need to run, from pilot data to the final Impact / Fiscal Relief Index, matching [`plans/2026-04-02_cri-phase1-data-pipeline-plan.md`](plans/2026-04-02_cri-phase1-data-pipeline-plan.md).

```mermaid
flowchart TD

  I0[Pilot and updated datasets] --> P1

  P1[Process 1 Inventory and mapping of pilot datasets] --> P2

  P2[Process 2 Cleaning and harmonization of core tables] --> P3

  P3[Process 3 Build province year impact variables] --> P4

  P4[Process 4 Prepare denominators and aggregate table] --> P5

  I1[New spatial layers for dasymetric mapping] --> P5

  P5[Process 5 Construct exposure proxies] --> P6

  P6[Process 6 Constrained redistribution and dasymetric mapping] --> P7

  P7[Process 7 Apply gap flags and data quality rules] --> P8

  P8[Process 8 Register evidence and freeze analysis package] --> O1

  O1[Final Phase 1 impact index inputs]
```

