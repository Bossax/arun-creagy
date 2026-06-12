import json
import re

# Load JSON
json_path = "ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/P2_Hard_Dependencies_Inventory.json"
with open(json_path, "r", encoding="utf-8") as f:
    j = json.load(f)

# Load Activity 2 concepts
txt_path = "ψ/incubate/DCCE/CRDB/output/consultation_workshop/activity2_master_analysis.md"
with open(txt_path, "r", encoding="utf-8") as f:
    txt = f.read()

concepts = re.findall(r"\| \*\*(G\d+-C\d+)\*\*\s+\|\s+(.*?)\s+\|\s+(.*?)\s+\|", txt)

# Extract JSON agencies and anchors
json_agencies = {uc["agency"] for uc in j}
json_anchors = {a for uc in j for a in uc.get("source_anchors", [])}

print(f"Total UCs in JSON: {len(j)}")
print(f"JSON Agencies: {json_agencies}\n")

missing_concepts = []
found_concepts = []

for c in concepts:
    c_id, c_agency, c_name = c
    c_agency = c_agency.strip()
    c_name = c_name.strip()
    
    # Check if the agency is covered in the JSON (either exact match, or mapping like 'สอวช.' -> 'NXPO')
    # Let's use a mapping dictionary for known Thai-EN aliases used in the project
    alias_map = {
        "สนข.": "OTP",
        "สป.ก.ท่องเที่ยวฯ": "MOTS",
        "สอวช.": "NXPO",
        "ทช.": "DMCR",
        "บพท.": "PMUA",
        "ทรัพยากรธรณี": "DMR",
        "เทศบาลฯ": "DLA", # Local admin
        "สมาคมธนาคารฯ": "TBA",
        "สสช. (NSO)": "NSO",
        "พม. (MSDHS)": "MSDHS",
        "สทนช. (ONWR)": "ONWR",
        "อต. (TMD)": "TMD",
        "อนามัย (DOH)": "DOH",
        "เจ้าท่า": "MD", # Marine Dept
        "สภาพัฒน์": "NESDC",
        "HII": "HII",
        "ONEP": "ONEP",
        "กรมโยธาฯ": "DPT",
        "LDD": "LDD",
        "UDDC": "UDDC",
        "N/A": "Unknown"
    }
    
    mapped_agency = alias_map.get(c_agency, c_agency)
    
    # Check if this agency exists in the JSON
    if mapped_agency in json_agencies:
        found_concepts.append((c_id, mapped_agency, c_name))
    else:
        missing_concepts.append((c_id, mapped_agency, c_name))

print("=== MAPPED AGENCIES IN JSON ===")
for fc in found_concepts:
    print(f"FOUND: {fc[0]} | {fc[1]} | {fc[2]}")

print("\n=== TRULY MISSING AGENCIES/CONCEPTS ===")
for mc in missing_concepts:
    print(f"MISSING: {mc[0]} | {mc[1]} | {mc[2]}")
