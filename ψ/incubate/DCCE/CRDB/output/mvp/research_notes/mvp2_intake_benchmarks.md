# MVP-2 (Intake) Benchmarking: Real-World Relatives

## 1. Identified Relatives
*   **EM-DAT**: Uses standardized inclusion criteria (e.g., 10+ fatalities) as a "hard filter" for data integrity.
*   **UNDRR DELTA / Sendai Monitor**: Focuses on "Globally Agreed Definitions" to normalize sectoral data.
*   **FEMA Hazus**: A platform for loss assessment that bridges raw hazard data with impact models.

## 2. Design Patterns (Level 1 vs Level 2)
| Feature | Level 1: Simple Triage | Level 2: Automated Impact |
|---------|------------------------|---------------------------|
| **Verification** | Manual "Reliability Flags" (Expert Audit) | Automated Cross-Check with Hazard Maps |
| **Quarantine** | Manual "Pending Review" status | Auto-Quarantine of statistical outliers |
| **Normalizing** | Manual mapping to common impact types | Automated schema-matching (DCAT/STAC) |

## 3. Confidence Score: 3/5
**Rationale**: While major databases like EM-DAT exist, their *internal* manual triage workflows are not publicly documented in detail. We have enough to hypothesize a "Level 1" workflow based on institutional audit patterns, but the "Level 2" automation logic is more specific to advanced GIS platforms (FEMA).
