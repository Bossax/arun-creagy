import os

source_path = "ψ/archive/2026-06-05_stale_pillar2/NCAIF_Service_Intelligence_Report_v4.3.md"
dest_path = "ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/NCAIF_Service_Intelligence_Report_v5.0.md"

with open(source_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update Headers & Versioning
text = text.replace("# NCAIF Service Intelligence Report (v4.3)", "# NCAIF Service Intelligence Report (v5.0)")
text = text.replace("Version: 4.2 (Inclusive Service Synthesis - Merge Release)", "Version: 5.0 (Methodology-Driven Synthesis & Complete Merge)")
text = text.replace("Date: 2026-06-05", "Date: 2026-06-08")
text = text.replace("NCAIF) v4.3 represents", "NCAIF) v5.0 represents")

# 2. Emphasize Sector-Agnostic Methodology in Exec Summary
text = text.replace("By anchoring every service module in a specific **Institutional Scenario**", "This version strictly enforces a **Sector-Agnostic, Methodology-Driven Architecture**. By anchoring every service module in a specific **Institutional Scenario**")

# 3. Update S02 Name & Common Core
text = text.replace("### S02: Socio-Economic Vulnerability Analytics", "### S02: Exposure & Vulnerability Analytics")
text = text.replace(
    "*   **The Common Core**: Integration of physical hazard data with socio-economic indicators at the block level.",
    "*   **The Common Core**: Methodology-driven spatial overlay integration of physical hazard data with cross-sectoral exposure indicators (human, agricultural, and economic) at high-resolution spatial units."
)

# 4. Update S06 Name & Common Core
text = text.replace("### S06: Multi-Hazard Monitoring & Early Warning", "### S06: Real-Time Threshold Monitoring")
text = text.replace(
    "*   **The Common Core**: Near real-time monitoring of environmental thresholds to support operational decision-making.",
    "*   **The Common Core**: Sector-agnostic, near real-time API telemetry tracking environmental and operational thresholds to support rapid disaster, health, and slow-onset natural resource decision-making."
)

# 5. Update S01 Common Core to emphasize sector neutrality
text = text.replace(
    "*   **The Common Core**: A foundational platform for discovery and metadata standardization, ensuring a \"Single Source of Truth\" across national repositories (NSO, DCCE, ONWR).",
    "*   **The Common Core**: A foundational, sector-neutral methodology for metadata federation and discovery, ensuring a \"Single Source of Truth\" across all national repositories (NSO, DCCE, ONWR)."
)

# 6. Update Traceability footer
text = text.replace("*NCAIF Pillar 2 Synthesis v4.3 — ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/NCAIF_Service_Intelligence_Report_v4.3.md*", "*NCAIF Pillar 2 Synthesis v5.0 (Forensic 40-UC Merge) — ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/NCAIF_Service_Intelligence_Report_v5.0.md*")

with open(dest_path, "w", encoding="utf-8") as f:
    f.write(text)

print("v5.0 Report successfully generated using sector-agnostic framing.")
