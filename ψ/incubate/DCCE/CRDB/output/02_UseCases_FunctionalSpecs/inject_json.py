import json

p = "ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/P2_Hard_Dependencies_Inventory.json"
with open(p, "r", encoding="utf-8") as f:
    j = json.load(f)

new_ucs = [
    {
        "id": "UC-33",
        "agency": "MOTS",
        "use_case": "Tourism Resilience Info System",
        "service_id": "S04",
        "data_parameters": {
            "variables": ["Tourism Economic Vulnerability", "Loss & Damage Data", "Sensitivity Analysis"],
            "resolution": "Provincial/Destination",
            "return_periods": "Annual"
        },
        "triggers": ["Tourism Recovery Planning"],
        "technical_constraints": {
            "latency": "Annual",
            "format": "Economic Dashboard",
            "integration": "MOTS Data Center"
        },
        "source_anchors": ["G1-C3", "G1-C4"]
    },
    {
        "id": "UC-34",
        "agency": "DMCR",
        "use_case": "Real-time Marine Ecosystem Monitoring",
        "service_id": "S06",
        "data_parameters": {
            "variables": ["Sea Surface Temperature", "Coral Bleaching Alerts", "Water Quality Parameters"],
            "resolution": "Coastal Grids / Stations",
            "return_periods": "1yr historical / 30-day forecast"
        },
        "triggers": ["Marine Conservation Action", "Pollution Alerts"],
        "technical_constraints": {
            "latency": "Real-time",
            "format": "API/Dashboard",
            "integration": "DMCR Portal"
        },
        "source_anchors": ["G1-C10", "G3-C3"]
    },
    {
        "id": "UC-35",
        "agency": "PMUA",
        "use_case": "Learning Data Repository",
        "service_id": "S07",
        "data_parameters": {
            "variables": ["Area-based Planning Data", "Future Hazard Alerts"],
            "resolution": "Regional",
            "return_periods": "Strategic"
        },
        "triggers": ["Research Funding Allocation"],
        "technical_constraints": {
            "latency": "Annual",
            "format": "API",
            "integration": "PMUA Research Database"
        },
        "source_anchors": ["G2-C1"]
    },
    {
        "id": "UC-36",
        "agency": "ONWR",
        "use_case": "Integrated Water Management Projections",
        "service_id": "S06",
        "data_parameters": {
            "variables": ["Flood/Drought Forecasts", "Water Quality", "Economic Loss Assessment"],
            "resolution": "Basin Level",
            "return_periods": "Seasonal"
        },
        "triggers": ["National Water Command Center Directives"],
        "technical_constraints": {
            "latency": "Real-time/Seasonal",
            "format": "API / Source Code",
            "integration": "National Water Data Center"
        },
        "source_anchors": ["G3-C9"]
    },
    {
        "id": "UC-37",
        "agency": "TMD",
        "use_case": "Localized Flood Risk Maps",
        "service_id": "S06",
        "data_parameters": {
            "variables": ["Water Absorption Thresholds", "Localized Rainfall Peaks"],
            "resolution": "Sub-district",
            "return_periods": "Event-based"
        },
        "triggers": ["Early Warning Activation"],
        "technical_constraints": {
            "latency": "Real-time",
            "format": "SHP/GeoJSON",
            "integration": "TMD Warning System"
        },
        "source_anchors": ["G3-C10"]
    },
    {
        "id": "UC-38",
        "agency": "MD",
        "use_case": "Marine Infrastructure Risk Assessment",
        "service_id": "S05",
        "data_parameters": {
            "variables": ["Sea Level Rise (SLR) Projections", "Coastal Erosion Rates"],
            "resolution": "Port/Coastal Segment",
            "return_periods": "20-50 year Projections"
        },
        "triggers": ["Port Maintenance Regulations", "Infrastructure Budget Approval"],
        "technical_constraints": {
            "latency": "Decadal/5-Year Cycle",
            "format": "Risk Maps / Adaptation Manuals",
            "integration": "Marine Dept Asset Mgt"
        },
        "source_anchors": ["G4-C7"]
    },
    {
        "id": "UC-39",
        "agency": "HII",
        "use_case": "EEC Water Scarcity Planning Service",
        "service_id": "S06",
        "data_parameters": {
            "variables": ["Raw Water Sources", "Future Scarcity Projections"],
            "resolution": "EEC Industrial Zones",
            "return_periods": "Seasonal / 10-year"
        },
        "triggers": ["EEC Water Allocation Planning"],
        "technical_constraints": {
            "latency": "Monthly",
            "format": "Web Services / API",
            "integration": "HII Data Hub"
        },
        "source_anchors": ["G78-C1"]
    },
    {
        "id": "UC-40",
        "agency": "LDD",
        "use_case": "Ag-Sector Carbon & Recovery Support",
        "service_id": "S02",
        "data_parameters": {
            "variables": ["Plot-level Rainfall/Temp/Damage", "Soil Moisture", "Crop Impact"],
            "resolution": "Plot-level (Agricultural)",
            "return_periods": "Seasonal"
        },
        "triggers": ["Agricultural Recovery Policy", "Carbon Credit Verification"],
        "technical_constraints": {
            "latency": "Monthly",
            "format": "Dashboard / API",
            "integration": "LDD Agricultural Database"
        },
        "source_anchors": ["G78-C9", "G78-C10"]
    }
]

# Ensure we don't append duplicates if run twice
existing_ids = {uc["id"] for uc in j}
to_append = [uc for uc in new_ucs if uc["id"] not in existing_ids]

j.extend(to_append)

with open(p, "w", encoding="utf-8") as f:
    json.dump(j, f, indent=2, ensure_ascii=False)

print(f"Injected {len(to_append)} new use cases into JSON.")
