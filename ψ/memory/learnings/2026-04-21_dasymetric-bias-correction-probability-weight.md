# Learning: Dasymetric Bias Correction via Model C (Probability Weight)

## Context
During the disaggregation of TEI provincial casualties into Tambon-level hotspots, we identified that using population density alone as a spatial distributor (Model A) introduced a systemic bias. Safe but densely populated urban areas received high risk scores, while sparsely populated high-hazard areas were undervalued.

## Insight
Population is a proxy for **Exposure**, not **Risk**. To calculate true risk, disaggregation must be gated by **Probability**. 

The fundamental correction is the **Synthetic Hybrid (Model C)**:
$W_{risk} = Population \times (\sum Historical\_Hazard\_Events + \epsilon)$

This ensures that:
1. High-density zones with no hazard history are effectively masked or down-weighted.
2. Moderate-density zones with frequent hazards (the "True Hotspots") are highlighted.
3. The "Conservation of Total" is maintained by re-normalizing the hybrid weights.

## Application
Apply this "Probability Gating" to all human-centric pillars in the CRI. For future work:
- If granular hazard maps (e.g., return-period flood maps) are available, they should replace historical frequency as the probability weight.
- Always compare the "Exposure-only" vs. "Hybrid" results (The Rank Shift) to identify **Reporting Gaps** where hazards are known to exist but are missing from administrative statistics.

---
*Logged via /rrr*
