# Agent Context

@mandates/00-principles.md
@mandates/01-system.md
@mandates/02-identity.md
@mandates/03-brain-structure.md
@mandates/04-deployment-rules.md

---

# CRITICAL MANDATES

## NotebookLM MCP Rule Constraint (NON-NEGOTIABLE)
1. **Query-Only Restriction**: You are **strictly prohibited** from using NotebookLM for generating podcasts (audio), mindmaps, slides, video, or quizzes. The active toolset is restricted exclusively to text query and source management (`notebook_query`, `notebook_get`, `notebook_list`, and `source_add`).
2. **Verbatim Capture (Nothing is Deleted)**: You **must** save all raw responses from NotebookLM `notebook_query` verbatim into a timestamped file under a `notebooklm_runs/` directory in the repository before making any local edits or analysis.
3. **Mandatory Execution**: All steps, workflows, and gates in the `notebooklm-rules` skill (`SKILL.md`) are strict system mandates, not suggestions. You **must** verify auth status, check the notebook ID config, and pass the source-fidelity gate prior to executing any queries.


