# 2026-05-22 — CRDB 9‑Pillar Tech Spec Revision Plan

## 0) Objective

Bring **all CRDB technical specifications** and their cross-links into a consistent **TOR-direct 9‑pillar framing**:

- Pillar numbering in headings and filenames matches the new directory taxonomy under [`ψ/incubate/DCCE/CRDB/output/`](ψ/incubate/DCCE/CRDB/output:1).
- No remaining references to pre-restructure folders (e.g. `04_Inventory_Mapping`, `08_Strategy_Reports`).
- LDM scope is correctly framed as **data model + rules + templates** (no implied “math engine” unless explicitly separately defined).
- Canonical navigation/index/ledgers point to the new locations.

## 1) Current findings (confirmed)

### 1.1 Mis-numbered titles / mismatched pillar naming

- Pillar 1 spec file title still says “Pillar 4”:
  - [`ψ/incubate/DCCE/CRDB/output/01_Sitemap_InterfaceMapping/Pillar_01_Sitemap_InterfaceMapping_Technical_Specification.md`](ψ/incubate/DCCE/CRDB/output/01_Sitemap_InterfaceMapping/Pillar_01_Sitemap_InterfaceMapping_Technical_Specification.md:1)

- Pillar 7 spec contains internal text drift (“Pillar 6…”) and still references old spec paths:
  - [`ψ/incubate/DCCE/CRDB/output/07_Governance_RACI/Pillar_07_Governance_Technical_Specification.md`](ψ/incubate/DCCE/CRDB/output/07_Governance_RACI/Pillar_07_Governance_Technical_Specification.md:5)
  - Broken old-path references in integration section:
    - [`ψ/incubate/DCCE/CRDB/output/07_Governance_RACI/Pillar_07_Governance_Technical_Specification.md`](ψ/incubate/DCCE/CRDB/output/07_Governance_RACI/Pillar_07_Governance_Technical_Specification.md:64)

### 1.2 Anchor doc still contains scope/naming contradictions

- “Deterministic Math Engine” still appears in the pillar table for P6:
  - [`ψ/incubate/DCCE/CRDB/output/00_Strategy_Reports/2026-05-20_CRDB-8-Pillar-Inception-Package-Anchor.md`](ψ/incubate/DCCE/CRDB/output/00_Strategy_Reports/2026-05-20_CRDB-8-Pillar-Inception-Package-Anchor.md:70)

- Several spec links in the anchor use filenames that don’t exist (example: glossary link uses `Pillar_04_...` while file is `Pillar_02_...`).
  - Same anchor file section: [`2026-05-20_CRDB-8-Pillar-Inception-Package-Anchor.md`](ψ/incubate/DCCE/CRDB/output/00_Strategy_Reports/2026-05-20_CRDB-8-Pillar-Inception-Package-Anchor.md:92)

### 1.3 Pillar 2 has artifacts but lacks a pillar wrapper spec

- Pillar 2 folder contains use-case artifacts, but there is no dedicated `Pillar_02_*_Technical_Specification.md` wrapper file.
  - Folder: [`ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/`](ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs:1)

## 2) Target end-state (definition of done)

1. **One tech spec per pillar** (P1–P9), with:
   - correct pillar number in the H1 heading,
   - correct “pillar name” in the H1 heading,
   - no internal references to old pillar numbering.
2. **Anchor doc** points to the correct tech specs and uses correct pillar naming.
3. **Governance and cross-pillar references** point to the new file locations.
4. **Index + ledgers** updated:
   - [`ψ/incubate/DCCE/CRDB/output/CRDB-Execution-Architecture-Index.md`](ψ/incubate/DCCE/CRDB/output/CRDB-Execution-Architecture-Index.md:1)
   - [`ψ/incubate/DCCE/CRDB/CRDB-Change-Log.md`](ψ/incubate/DCCE/CRDB/CRDB-Change-Log.md:1)
   - plus any remaining `output/<old>` paths.

## 3) Execution sequence (safe + auditable)

### Step A — Freeze the canonical pillar names (single source of truth)

Use the directory names under [`ψ/incubate/DCCE/CRDB/output/`](ψ/incubate/DCCE/CRDB/output:1) as the operational ground truth:

01. `01_Sitemap_InterfaceMapping`
02. `02_UseCases_FunctionalSpecs`
03. `03_DataInventory_DQ`
04. `04_Glossary`
05. `05_CDM_EARCatalog`
06. `06_LDM_LossDamage_DataModel`
07. `07_Governance_RACI`
08. `08_RefData_Matrix`
09. `09_BuildingBlocks`

### Step B — Create missing wrapper spec (Pillar 2)

Create:
- `02_UseCases_FunctionalSpecs/Pillar_02_UseCases_FunctionalSpecs_Technical_Specification.md`

Minimal contents:
- Purpose + scope boundary (“functional specs / click-path logic”),
- required artifact types (use-case inventory table + per-use-case spec),
- required schema fields (IDs, actors, triggers, inputs, outputs, dependencies),
- verification criteria.

### Step C — Rename tech spec files to match the 9 pillars (git mv)

Rename (and adjust heading inside each file):

- P3: rename
  - `03_DataInventory_DQ/Pillar_05_DQ_Framework_Technical_Specification.md`
  - → `03_DataInventory_DQ/Pillar_03_DataInventory_DQ_Technical_Specification.md`

- P4: rename
  - `04_Glossary/Pillar_02_Glossary_Technical_Specification.md`
  - → `04_Glossary/Pillar_04_Glossary_Technical_Specification.md`

- P5: rename
  - `05_CDM_EARCatalog/Pillar_01_CDM_Technical_Specification.md`
  - → `05_CDM_EARCatalog/Pillar_05_CDM_EARCatalog_Technical_Specification.md`

- P6: rename
  - `06_LDM_LossDamage_DataModel/Pillar_03_LDM_Logic_Technical_Specification.md`
  - → `06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md`

- P7: optionally rename for consistency
  - `07_Governance_RACI/Pillar_07_Governance_Technical_Specification.md`
  - → `07_Governance_RACI/Pillar_07_Governance_RACI_Technical_Specification.md`

Note: P1/P8/P9 filenames already match pillar numbers.

### Step D — Fix internal pillar numbering and scope language (content edits)

Mandatory edits:

- P1 spec: fix H1 from “Pillar 4” → “Pillar 1”.
- P7 spec: replace “Pillar 6” references with “Pillar 7”.
- Anchor doc: remove/replace “Deterministic Math Engine” language for P6.
  - Replace with “LDM (data model + rules + templates)” + explicit non-requirement of a computation engine unless separately defined.

### Step E — Heal cross-links (repo-wide pass)

Update references to:
- old folder names (`04_Inventory_Mapping`, `08_Strategy_Reports`, etc.)
- old spec filenames (`Pillar_05_*`, `Pillar_03_*`, etc.)

Primary files to update:
- [`ψ/incubate/DCCE/CRDB/output/00_Strategy_Reports/2026-05-20_CRDB-8-Pillar-Inception-Package-Anchor.md`](ψ/incubate/DCCE/CRDB/output/00_Strategy_Reports/2026-05-20_CRDB-8-Pillar-Inception-Package-Anchor.md:1)
- [`ψ/incubate/DCCE/CRDB/output/CRDB-Execution-Architecture-Index.md`](ψ/incubate/DCCE/CRDB/output/CRDB-Execution-Architecture-Index.md:1)
- [`ψ/incubate/DCCE/CRDB/CRDB-Change-Log.md`](ψ/incubate/DCCE/CRDB/CRDB-Change-Log.md:1)
- [`ψ/incubate/DCCE/CRDB/CRDB-Deliverable-Map.md`](ψ/incubate/DCCE/CRDB/CRDB-Deliverable-Map.md:1)
- [`ψ/incubate/DCCE/CRDB/CRDB-Evidence-Registry.md`](ψ/incubate/DCCE/CRDB/CRDB-Evidence-Registry.md:1)
- [`ψ/incubate/DCCE/CRDB/CRDB-Trigger-Log.md`](ψ/incubate/DCCE/CRDB/CRDB-Trigger-Log.md:1)

### Step F — Commit strategy

Use small commits so rollback is cheap:

1. `crdb: phase2 content shuffle (pillar moves)`
2. `crdb: add pillar2 tech spec wrapper`
3. `crdb: rename tech spec files to 9-pillar naming`
4. `crdb: heal links after 9-pillar rename`

## 4) Risk controls

- Use `git mv` for all renames (preserve history).
- After each step, run a repo search for the old tokens:
  - `04_Inventory_Mapping`
  - `08_Strategy_Reports`
  - `Deterministic Math Engine`
  - `Pillar_05_DQ_Framework_Technical_Specification`


