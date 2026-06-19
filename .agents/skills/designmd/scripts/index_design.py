import sys
import os
import json
import re

def extract_metadata(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract Title (H1)
    title_match = re.search(r'^# (.*)', content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else os.path.basename(file_path)

    # Extract Overview/Description
    # Look for Overview section or first paragraph
    overview_match = re.search(r'## Overview\n\n(.*?)\n\n', content, re.DOTALL)
    if not overview_match:
        # Fallback: get text after title but before next header
        overview_match = re.search(r'^# .*?\n\n(.*?)\n\n##', content, re.DOTALL)
    
    description = overview_match.group(1).strip() if overview_match else "No description available."
    
    # Extract Colors for Vibe analysis
    colors_match = re.search(r'## Colors\n\n(.*?)\n\n##', content, re.DOTALL)
    colors = colors_match.group(1).strip() if colors_match else ""

    # Basic Vibe mapping (Keywords to be expanded by LLM during skill execution)
    tags = []
    if "green" in colors.lower() or "sage" in colors.lower(): tags.append("natural")
    if "navy" in colors.lower() or "dark" in colors.lower(): tags.append("authoritative")
    if "clean" in description.lower() or "minimal" in description.lower(): tags.append("lean")
    if "trustworthy" in description.lower() or "precision" in description.lower(): tags.append("official")

    return {
        "name": title,
        "filename": os.path.basename(file_path),
        "description": description,
        "vibe_tags": tags,
        "raw_path": file_path
    }

def update_registry(registry_path, new_entry):
    if os.path.exists(registry_path):
        with open(registry_path, 'r', encoding='utf-8') as f:
            registry = json.load(f)
    else:
        registry = {}

    registry[new_entry["filename"]] = new_entry

    with open(registry_path, 'w', encoding='utf-8') as f:
        json.dump(registry, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python index_design.py <design_file_path> <registry_json_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    registry_path = sys.argv[2]
    
    try:
        entry = extract_metadata(file_path)
        update_registry(registry_path, entry)
        print(f"Successfully indexed {entry['name']} to registry.")
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)
