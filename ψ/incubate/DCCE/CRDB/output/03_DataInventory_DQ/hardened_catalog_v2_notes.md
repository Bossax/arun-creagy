# Hardening Notes: Data Catalog v2 (Pillar 3)

This document tracks the surgical edits and decisions made to transform `data_catalog_v2.csv` into a procurement-ready baseline.

## 1. Domain Alignment Audit
- **Field**: `ขอบข่ายข้อมูล Domain`
- **Decision**: Renamed to `ช่วงเวลาข้อมูล time_horizon`.

## 2. Sub-Domain Realignment
- **Field**: `ขอบข่ายข้อมูลย่อย Sub_Domain`
- **Decision**: Rename to `ขอบข่ายข้อมูล domain`. Values will be mapped/cleaned to align with CDM Domains (e.g., Physical Climate, Risk Assessment) where possible, or kept as thematic categories.

## 3. Metadata Cleanup
- **Decision**: 
    - `maintainer` / `steward`: Default to `owner_org`.
    - `update_frequency`: Mark as `Unknown` if empty.

## 4. Governance Defaults (Procurement Shield)
- **Field**: `endorsement_status` -> `Baseline-Draft`.
- **Field**: `validation_flag` -> `Unverified-Baseline`.
- **Note**: `canonical_boundary_id` dropped per user request.

## 6. Header Consolidation & Clean-up
- **Master Access Field**: Use `accessible_condition` (DGA standard). Drop/Merge `Access_Level (2)`.
- **Master Remarks Field**: Use `หมายเหตุ Remarks`. Merge content from `หมายเหตุ Remarks (2)` into this field if not empty.
- **CDM Integrity**: Keep `ชื่อประเภทข้อมูล Data_Entity` as the primary link to CDM entities.
- **Source Distinction**: 
    - `Source_Type`: Website, Report, API (The 'How').
    - `data_source`: The actual name of the dataset/package (The 'What').

## 7. Execution: Batch Transformation (v3)
- **Source**: `data_catalog_v2.csv`
- **Output**: `data_catalog_v3.csv`
- **Status**: READY FOR EXECUTION.
