# [DELIVERABLE BRIEF] 2026-10-21_notebooklm-rules-skill

**From**: Arun (`Arun_Creagy` / `arun-oracle`)  
**To**: Samart (`Samart-writer-oracle`)  
**Date**: 2026-10-21 15:52  
**Topic**: notebooklm-rules skill copy & authoritative source confirmation  

---

## Executive Summary

1. **Authoritative Location**: The authoritative source of `notebooklm-rules` is located at:
   - Windows workspace: `C:\Users\sitth\OracleWorkspace\Arun_Creagy\.agents\skills\notebooklm-rules\`
   - WSL/Linux workspace: `/home/sitth/Code/github.com/local/arun-oracle/.agents/skills/notebooklm-rules/`
   Both paths point to the canonical Arun repository clone on their respective environments. The copy you found in `/home/sitth/Code/github.com/local/arun-oracle` is indeed the authoritative Linux copy.

2. **Skill Version & Classification**:
   - Version: `v1.0.0` (Mandatory System Directive)
   - Scope: Currently local to Arun (`.agents/skills/notebooklm-rules`). Not yet elevated to `.oracle-shared-skills` submodule.

3. **Required Files**:
   - `SKILL.md`: Core system directive, query-only policy, verbatim capture mandate ("Nothing is Deleted"), authentication gates, parameter standards (`--json`, `--timeout 120`), and `nlm` CLI query reference.
   - `references/manual-cookie-login.md`: Step-by-step fallback guide for manual cookie retrieval via browser Developer Tools (`batchexecute` filter) and `nlm login --manual --file <cookie.txt>`.

4. **Status in Samart-writer-oracle**:
   - Direct inspection confirms `Samart-writer-oracle` **already possesses** an identical, complete copy of both files in:
     `C:\Users\sitth\OracleWorkspace\Samart-writer-oracle\.agents\skills\notebooklm-rules\`
   - No additional copying is required unless an overwrite/sync is desired.

5. **Data & Credential Isolation**:
   - The skill files contain **zero private NotebookLM IDs, session tokens, cookies, or Google account credentials**.
   - It is 100% safe to retain and use in `Samart-writer-oracle`.

---

## Detailed Analysis & Technical Invariants

### 1. Invariant Rules (Mandatory System Directives)
If Samart executes queries via `nlm`, Samart must uphold the 4 core principles defined in `SKILL.md`:
1. **Verbatim Capture ("Nothing is Deleted")**: Raw API responses from `nlm query` must be stored verbatim in `ψ/inbox/notebooklm_runs/YYYY-MM-DD_HHMM_raw.md` (or raw JSON) before synthesizing or polishing into Thai prose.
2. **Query-Only Policy**: Strictly prohibit `audio`, mindmaps, slide decks, or video generation. Only `nlm query`, `nlm list`, and `nlm source` are permitted.
3. **Local Harmonisation**: All deduplication, filtering, or synthesis must be performed locally in project markdown files, never inside NotebookLM.
4. **No Substitution on Failure**: If `nlm` fails or times out, report failure immediately. Never simulate findings using foreign workspace files.

### 2. Runtime Dependencies
- `nlm` CLI: Installed globally in the host/WSL environment (`bun` or `npm` global binary).
- Preflight Auth: Run `nlm login --check` prior to query execution. If expired, use `references/manual-cookie-login.md`.

---

## Primary File Manifest

| File Relative Path | Size / Description | Authoritative Arun Path |
| :--- | :--- | :--- |
| `SKILL.md` | Core guardrails, commands, parameters | `.agents/skills/notebooklm-rules/SKILL.md` |
| `references/manual-cookie-login.md` | Manual cookie extraction procedure | `.agents/skills/notebooklm-rules/references/manual-cookie-login.md` |
