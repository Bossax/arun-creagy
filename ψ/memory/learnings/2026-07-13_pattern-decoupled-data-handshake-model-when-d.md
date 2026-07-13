---
id: learning_2026-07-13_pattern-decoupled-data-handshake-model-when-d
type: learning
title: ### Pattern: Decoupled Data-Handshake Model
concepts: [decoupling, data-engineering, handshake-model, python]
tags: [decoupling, data-engineering, handshake-model, python]
created: 2026-07-13
indexed_at: 2026-07-13T05:42:43.967Z
updated_at: 2026-07-13T05:42:43.967Z
hash: sha256:64dca1dfc5ba54894e02e3013bd8918a08d16c7a19a24867c644fbbeee3985be
source: d68d5b2f-7f13-4460-bea2-956ded2d64ee
project: bossax/arun_creagy
arra_id: learning_2026-07-13_pattern-decoupled-data-handshake-model-when-d
arra_type: learning
arra_concepts: [decoupling, data-engineering, handshake-model, python]
arra_created: 2026-07-13T05:42:43.967Z
---

# ### Pattern: Decoupled Data-Handshake Model

### Pattern: Decoupled Data-Handshake Model
When designing AI-orchestrated compilation loops, avoid hardcoding large data dictionaries inside the Python compilers. Instead, decouple the data into external JSON/CSV mapping files and write a simple local CLI orchestrator (e.g. using `agy --print`) to scan for missing rows and backfill them iteratively. This maintains script portability, allows easy debugging of metrics, and prevents code modification overhead when data updates.

---
*Added via Oracle Learn*
