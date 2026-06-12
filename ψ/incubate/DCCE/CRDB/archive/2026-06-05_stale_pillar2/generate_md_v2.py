import json

json_file = 'ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/P2_Hard_Dependencies_Inventory.json'
md_file = 'ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/NCAIF_Use_Case_Traceability_Matrix_v2.0.md'

with open(json_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Sort data by service_id, then by UC ID
data.sort(key=lambda x: (x.get('service_id', 'S99'), x.get('id', '')))

# Group by Service
grouped_data = {}
for item in data:
    sid = item.get('service_id', 'Uncategorized')
    if sid not in grouped_data:
        grouped_data[sid] = []
    grouped_data[sid].append(item)

service_names = {
    "S01": "S01: National Authoritative Data Catalog & Discovery (SSOT)",
    "S02": "S02: Socio-Economic Vulnerability Analytics",
    "S03": "S03: Climate Investment ROI & Fiscal Planning",
    "S04": "S04: Climate Loss & Damage Assessment",
    "S05": "S05: Infrastructure Risk & Engineering Specifications",
    "S06": "S06: Multi-Hazard Monitoring & Early Warning",
    "S07": "S07: Policy Monitoring & NAP Compliance"
}

md_content = """# NCAIF Use Case Inventory: Human-Readable Traceability Matrix

**Status**: Definitive Index (Full Exhaustive List - Activity 1 & 2)
**Version**: 2.0 (Complete Forensic Merge)
**Date**: 2026-06-08
**Context**: This document provides the human-readable "Logic Bridge" between raw stakeholder interviews (Activity 1), consultation workshop outputs (Activity 2), and the final Service Intelligence Report (v4.3). It contains all 40 validated Use Cases.

---

## 1. Parent Files & Lineage
To maintain **Institutional Sovereignty**, every entry in this matrix is derived from:
1.  **Technical Basis**: `Pillar_02_UseCases_FunctionalSpecs_Technical_Specification_v4.0.md`
2.  **Evidence Base 1 (Interviews)**: `user_use_case_raw.md` 
3.  **Evidence Base 2 (Workshop)**: `activity2_master_analysis.md`
4.  **Source of Truth**: `P2_Hard_Dependencies_Inventory.json` (The technical master list).

---
"""

for sid in sorted(grouped_data.keys()):
    group_name = service_names.get(sid, f"Service Group: {sid}")
    md_content += f"\n## {group_name}\n\n"
    md_content += "| UC ID | Agency | Use Case / Decision Moment | Key Technical Specs | Source Anchors |\n"
    md_content += "| :--- | :--- | :--- | :--- | :--- |\n"
    
    for item in grouped_data[sid]:
        uc_id = item.get('id', '')
        agency = item.get('agency', '')
        use_case = item.get('use_case', '')
        
        # Format tech specs
        vars = ", ".join(item.get('data_parameters', {}).get('variables', []))
        res = item.get('data_parameters', {}).get('resolution', '')
        tech_specs = f"{res}; {vars}"
        
        anchors = ", ".join([f"`[{a}]`" for a in item.get('source_anchors', [])])
        
        md_content += f"| **{uc_id}** | **{agency}** | {use_case} | {tech_specs} | {anchors} |\n"

md_content += "\n---\n*NCAIF Forensic Traceability Matrix — ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/NCAIF_Use_Case_Traceability_Matrix_v2.0.md*\n"

with open(md_file, 'w', encoding='utf-8') as f:
    f.write(md_content)

print("v2.0 Markdown Matrix generated successfully.")
