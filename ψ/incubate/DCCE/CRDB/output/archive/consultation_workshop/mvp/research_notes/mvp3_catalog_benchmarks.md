# MVP-3 (Catalog) Benchmarking: Real-World Relatives

## 1. Identified Relatives
*   **NOAA NCEI**: Uses "Climate Data Records (CDRs)" as the authoritative label.
*   **Copernicus CDS**: Curates via "Application Guides" and "Interactive Atlases" (e.g., CMIP6 for Policy, CORDEX for Engineering).
*   **NASA Earthdata**: Uses "EOSDIS Common Metadata" to signify authoritative status.

## 2. Design Patterns (Level 1 vs Level 2)
| Feature | Level 1: Curated Directory | Level 2: Federated Service |
|---------|---------------------------|---------------------------|
| **Curation** | "Recommended for Sector X" labels | Full Metadata Search (DCAT/STAC) |
| **Access** | Pre-packaged Download Bundles | Live API / OGC Web Services |
| **Trust Signal** | "Official Government Record" Badge | Versioned, Traceable Lineage |

## 3. Confidence Score: 4/5
**Rationale**: Strong relatives found (NOAA/Copernicus). The "Official" badge pattern is common. However, the "Level 1" (simple curated directory) is often overshadowed by the complex "Level 2" catalogs; we need to simplify this for the workshop.
