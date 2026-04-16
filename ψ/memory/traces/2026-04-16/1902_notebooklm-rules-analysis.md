---
query: "issues with notebooklm-rules skill past experience"
target: "Arun_Creagy"
mode: "deep"
timestamp: 2026-04-16 19:02
friction_score: 0.6
coverage: [oracle, files]
confidence: "high"
---

# Trace: notebooklm-rules skill issues and history

**Target**: Arun_Creagy
**Mode**: deep | **Friction**: 0.6 | **Confidence**: high
**Time**: 2026-04-16 19:02

## Oracle Results
Results were retrieved after examining learning notes covering Feb–Apr 2026.

## Files Found
- ψ/memory/learnings/2026-04-08_notebooklm-source-fidelity-and-parameter-discipline.md
- ψ/memory/learnings/2026-03-02_keep-notebooklm-mcp-skills-narrowly-scoped-feed-p.md
- ψ/memory/learnings/2026-04-09_notebooklm-mcp-timeouts-fixed-by-increasing-serv.md

## Friction Analysis
**Score**: 0.6 — Slightly buried. The knowledge is highly fragmented across several technical troubleshooting notes and process disciplines.
**Coverage**: [oracle, files]
**Goal check**: Yes, these findings accurately reflect both the technical reliability issues and the process-discipline requirements for successful NotebookLM usage.

## Summary: notebooklm-rules Skill Analysis

### 1. Past Experience & Performance
*   **The "Reliability Ceiling"**: The skill faced severe performance bottlenecks where automated interaction was consistently slower than the client's timeout window. Early efforts were marred by frequent "Request timed out" errors, leading to high user frustration until environmental variables were tuned.
*   **The "Abstraction Penalty"**: Early attempts to bundle the entire research workflow into the skill led to "scope creep," making the skill brittle and hard to maintain. The breakthrough was decoupling the research orchestration (Question → AI Tools → NotebookLM Upload) from the skill itself.

### 2. Technical & Process Issues
*   **Timeout sensitivity**: Automation tasks (like uploading or extracting) often trigger timeouts. The fix involves disabling stealth features and significantly increasing BROWSER_TIMEOUT in the MCP server configuration.
*   **Source Fidelity (The "Faithfulness" Trap)**: The skill often assumed the AI knew which sources were inside a notebook. The system required a hard "Title Resolution Step" to force the agent to probe the notebook for real source titles before attempting extractions.
*   **Parameter Implicitness**: A recurring issue was letting the session implicit context dictate notebook_id or session_id. The rules were updated to mandate explicit parameter passing for every single call to prevent data binding errors.

### 3. Improvements & Future Strategy
*   **Fail-Fast Guardrails**: The current rule-set prioritizes "Fail-Fast" behavior; if the source list cannot be verified, the task stops immediately rather than producing "superficial" (and unreliable) output.
*   **Atomic Extractions**: Shifted the pattern from "bulk research" to "atomic extraction"—questioning specific, verified fragments of a single source rather than the whole notebook at once.
*   **Config Hardening**: Moving away from default "stealth" modes to optimized "performance" modes (higher typing speed, disabled human-mimicry delays) to stay within the MCP heartbeat window.
