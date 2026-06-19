---
name: designmd
version: 1.0.0
description: Search, match, and retrieve DESIGN.md templates based on the "intended feel" (e.g., futuristic, authoritative, lean). Use this skill to explore local memory or the designmd.ai gallery to find the right visual style for a project.
---

# designmd — Design System Finder

This skill helps find the right visual style for a project by matching your desired "intended feel" against a local library and the designmd.ai gallery.
- **Persistence**: Templates are stored in Global Memory and indexed in `REGISTRY.json`.

## 1. Search Workflow

### Step 1: Local Memory Search
Search the local library first using the **Registry** to avoid reading every file.
- **Action**: `read_file("ψ/memory/design/REGISTRY.json")`
- **Logic**: Match the project's "Intended Feel" against the `description` and `vibe_tags` in the registry. 
- **Response**: If a match is found, present it and explain *why* it fits the desired style.

### Step 2: Online Gallery Search
If no local match fits the specific requirement, search the website.
- **Logic**: Translate the desired feel into search keywords (e.g., "modern security dashboard").
- **Action**: `powershell.exe -NoProfile -Command "designmd search '<feel_query>' --limit 5"`

### Step 3: Downloading & Auto-Indexing
When downloading a new kit, index it immediately so it is added to the registry. **Use the original kit name (e.g., creator-kit-name) for the filename.**
```bash
powershell.exe -NoProfile -Command "$env:DESIGNMD_API_KEY = '<KEY>'; designmd download <creator/kit-name> -o ψ/memory/design/<creator-kit-name>.DESIGN.md"
powershell.exe -NoProfile -Command "python .agents/skills/designmd/scripts/index_design.py ψ/memory/design/<creator-kit-name>.DESIGN.md ψ/memory/design/REGISTRY.json"
```

## 2. In-Session Execution
When a template is selected for active development:
1.  **Direct Read**: `read_file("ψ/memory/design/<creator-kit-name>.DESIGN.md")`.
2.  **Constraint**: Apply the design tokens (Colors, Spacing, Typography) to the generated code.
3.  **Efficiency**: Do not repeat or summarize the design spec unless requested.

## 3. Style Examples
- **Official/Authoritative**: Deep blues, serif headers, generous padding (e.g., "Verdana Health").
- **Lean Startup**: High contrast, vibrant accents, minimal borders, rounded corners.
- **Futuristic/High-Density**: Dark mode, neon accents, monospaced fonts, tight grids (e.g., "Command Center").
- **Natural/Calm**: Sage greens, warm neutrals, soft shadows, open space.
