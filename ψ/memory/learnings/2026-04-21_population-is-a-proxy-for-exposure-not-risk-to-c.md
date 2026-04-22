---
title: Population is a proxy for Exposure, not Risk. To calculate true risk in dasymetr
tags: [cri, dasymetric-mapping, bias-correction, spatial-disaggregation, probability-weighting]
created: 2026-04-21
source: rrr: Arun_Creagy
project: github.com/arun_creagy/cri-phase1
---

# Population is a proxy for Exposure, not Risk. To calculate true risk in dasymetr

Population is a proxy for Exposure, not Risk. To calculate true risk in dasymetric disaggregation, population density must be gated by Hazard Probability (using historical frequency or hazard maps). The fundamental correction is the Synthetic Hybrid: Weight = Population * (History + epsilon). This prevents safe, high-density urban areas from receiving artificial risk scores.

---
*Added via Oracle Learn*
