---
title: # Anti-Band-Aid Protocol: Structural Diagnostics Over Local Patches
tags: [troubleshooting, structural-integrity, anti-pattern, diagnostics, verification]
created: 2026-06-08
source: User Correction - Troubleshooting Laziness
project: github.com/oracleworkspace/arun_creagy
---

# # Anti-Band-Aid Protocol: Structural Diagnostics Over Local Patches

# Anti-Band-Aid Protocol: Structural Diagnostics Over Local Patches

**Trigger**: When a user points out a missing data point, omission, or anomaly in a generated artifact (e.g., "Why is LDD missing?").

**The Anti-Pattern (What to Avoid)**:
Do not assume the user's specific example is the *only* missing item. Do not offer a localized "patch" or "injection" (e.g., "I will manually add LDD") without understanding how it got lost. This is lazy, task-executor behavior that leads to structural rot.

**The Mandated Protocol (Arun's Rule)**:
1. **Halt and Acknowledge**: Treat the missing item as a symptom of a pipeline failure. 
2. **Trace the Boundary**: Identify the exact transformation step where the data dropped (e.g., Activity 1 vs. Activity 2 synthesis).
3. **Exhaustive Audit**: Query the source material to identify **ALL** casualties of that pipeline failure, not just the one the user spotted. 
4. **Structural Proposal**: Propose a fix to the *root pipeline/inventory*, ensuring all orphaned data is recovered simultaneously. Never patch the output; rebuild the source of truth.

---
*Added via Oracle Learn*
