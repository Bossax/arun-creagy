# CRI Data Dictionary

This document serves as the canonical reference for the metadata structures used in the CRI Phase 1 project. It formalizes the definitions, data types, and roles of columns across the core dimensions.

---

## 1. Categorical Metadata (Dimensions)

### 1.1 Hazard Type (`dim_hazard_type`)
**Role**: Captures the raw hazard labels from individual sources (BMA, DDPM, TEI) and provides a unique identifier for each source-specific hazard terminology.

| Column Name | Data Type | Nullable | Role | Definition | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `hazard_type_id` | integer | No | PK | Surrogate identifier for a source-specific hazard type. | Same Thai label may appear in multiple rows when source differs. |
| `hazard_code` | string | No | - | Working hazard code used in the model (e.g., FLOOD, DROUGHT). | BMA hazards use generic codes; DDPM use source-prefixed codes. |
| `hazard_name_from_source` | string | No | - | Hazard label exactly as represented in the source dataset. | Preserves original source terminology (Thai). |
| `source` | string | No | - | Agency or dataset source (e.g., BMA, DDPM, TEI). | Used to separate source-specific definitions. |
| `source_filename` | string | No | - | Name of the source file from which the hazard was extracted. | Lineage/Traceability field. |
| `is_active` | boolean | No | - | Flag indicating whether the hazard type is currently active. | Useful for future deprecation without history deletion. |

### 1.2 Canonical Hazard (`dim_hazard_canonical`)
**Role**: Provides the standardized, cross-agency alignment for hazards. This is the primary key used for comparative analysis and final index calculations.

| Column Name | Data Type | Nullable | Role | Definition | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `canonical_hazard_id` | integer | No | PK | Unique identifier for canonical hazard. | Surrogate key. |
| `canonical_hazard_code` | string | No | Unique | Stable code for hazard (e.g., FLOOD). | Used as the primary analysis key. |
| `canonical_hazard_name_en` | string | No | - | Standard English name of the hazard. | - |
| `canonical_hazard_name_th` | string | No | - | Standard Thai name of the hazard. | - |
| `hazard_group` | string | Yes | - | Broad classification (e.g., hydrological, meteorological). | - |
| `definition` | string | Yes | - | Formal canonical definition of the hazard. | Critical for multi-agency harmonization. |
| `inclusion_note` | string | Yes | - | Specific descriptions of what is included in this category. | e.g., Seasonal river overflow. |
| `exclusion_note` | string | Yes | - | Specific descriptions of what is excluded. | e.g., Flash floods treated separately. |
| `is_active` | boolean | No | - | Active record flag. | - |
| `review_status` | string | No | - | Validation status (draft / reviewed / approved). | - |
| `review_note` | string | Yes | - | Reviewer comments or pending clarifications. | - |

---

## 2. Spatial Metadata

### 2.1 Location Master (`dim_location_master`)
**Role**: The "Gold Spine" of the project, defining the relationship between Provinces, Districts, and Tambons.

| Column Name | Data Type | Nullable | Role | Definition |
| :--- | :--- | :--- | :--- | :--- |
| `location_id` | string | No | PK | Surrogate key (often 6-digit DOPA code). |
| `subdistrict_code` | string | No | Unique | Official 6-digit DOPA Tambon code. |
| `district_code` | string | No | - | Official 4-digit DOPA District code. |
| `province_code` | string | No | - | Official 2-digit DOPA Province code. |
| `province_name_th` | string | No | - | Standard Thai province name. |
| `tambon_name_th` | string | No | - | Standard Thai sub-district name. |

## 3. Gold Fact Tables (Empirical Impact)

### 3.1 DDPM Tambon Impact (`fact_ddpm_tambon_impact_climate`)
**Role**: Canonical sub-district level empirical impact signals derived from DDPM village-level records.

| Column Name | Data Type | Role | Definition | Notes |
| :--- | :--- | :--- | :--- | :--- |
| `subdistrict_code` | string | PK | 6-digit DOPA Tambon code. | Join key for Gold Spine. |
| `affected_households_sum` | float | Metric | Total households affected (B.E. 2560–2567). | Primary impact proxy. |
| `affected_people_sum` | float | Metric | Total people affected (B.E. 2560–2567). | - |
| `deaths_sum` | float | Metric | Total casualties (B.E. 2560–2567). | - |
| `avg_yoy_change` | float | Metric | Mean year-over-year change in affected households. | - |
| `pct_national_*` | float | Score | National Percentile Rank (0-100) for each metric. | Calculated across all Tambons. |

### 3.2 DDPM Provincial Impact Score (`fact_ddpm_province_impact_climate`)
**Role**: Aggregated provincial-level impact scores used for national benchmarking.

| Column Name | Data Type | Role | Definition | Notes |
| :--- | :--- | :--- | :--- | :--- |
| `province_code` | string | PK | 2-digit DOPA Province code. | - |
| `province_name_th` | string | - | Standard Thai province name. | - |
| `impact_score_minmax` | float | Score | Min-max normalized score (0.0-1.0). | Derived from aggregated tambon impacts. |
| `admin_gap_flag` | boolean | QA | Triggered when Damage > 0 but Relief = 0. | Marked as "Insufficient Data". |

---

## 4. Administrative Protocols

- **DOPA Spine**: All spatial joins MUST use the 6-digit `subdistrict_code` from `dim_location_master`.
- **Temporal Window**: Phase 1 Gold tables are locked to B.E. 2560–2567.
- **Null Handling**: Metric nulls are treated as `0.0` for ranking; missing DOPA codes are purged to the `qa` directory.
