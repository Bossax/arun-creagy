---
name: notebooklm-rules
description: MANDATORY DIRECTIVE - Enforces low-latency API-based nlm CLI query-only guardrails, source-fidelity gates, and verbatim raw response captures. MUST BE ADHERED TO WITHOUT EXCEPTION.
---

# NotebookLM CLI Rules

> [!IMPORTANT]
> **MANDATORY SYSTEM DIRECTIVE - NOT A SUGGESTION**
> All instructions, guardrails, and workflows defined in this skill are **strict system constraints**.
> Any agent invoking or interacting with NotebookLM in this workspace **MUST** execute queries exclusively via the `nlm` CLI tool.
> Failure to follow these rules constitutes a direct violation of the core agent safety mandate.

---

## 1. Core Principles (Strictly Mandatory)

1. **"Nothing is Deleted" (Verbatim Capture)**
   * **REQUIRED:** All raw responses from the `nlm` CLI must be saved **verbatim as-is** in the repository under a timestamped run directory (e.g., `ψ/inbox/notebooklm_runs/YYYY-MM-DD_HHMM_raw.md` or as JSON) before any formatting, translation, or cleanup occurs. This ensures a transparent, uncorrupted audit trail of source data.
2. **Query-Only Policy (Absolute Restriction)**
   * **BANNED:** Generating podcasts (`audio`), mindmaps, slide decks, or video overviews is strictly prohibited.
   * **RESTRICTION:** Use only CLI query and source management commands (`nlm query`, `nlm list`, `nlm source`).
3. **Local Harmonisation**
   * **REQUIRED:** Deduplication, data cleaning, or register updates must be performed **locally in the repository files**, never inside NotebookLM.
4. **No Substitution on Tool Failure (Strict Source-Fidelity)**
   * **REQUIRED:** If a CLI query fails or times out, the agent **MUST** immediately report the error and stop.
   * **BANNED:** Under no circumstances is the agent allowed to bypass a failed query by pulling from local files, general search, or other workspace files to simulate a successful query. Doing so violates the source-fidelity gate and introduces the risk of out-of-date or hallucinated information.

---

## 2. Parameter Discipline (Strictly Mandatory)

Every `nlm` command must specify the notebook and parameters explicitly to ensure non-interrupted, error-free execution:
*   **Notebook ID**: Always pass the exact UUID (e.g., `8bcbf9bb-fc5c-448a-839f-74a2d11b1a0e`) or its registered alias.
*   **JSON Flag**: Pass the `--json` option if downstream parsing of references or citations is required.
*   **Timeout**: Pass `--timeout 120` to guarantee a 2-minute API threshold.

---

## 3. Preflight Authentication Gate

If `nlm login --check` fails or returns an expired session error:
1. Report the authentication failure to the user.
2. Stop execution immediately.

---

## 4. Query-Focused Command Reference

Use the following reference to construct exact `nlm` CLI calls for research and extraction tasks:

### 4.1. Chatting with Notebook Sources
* **Command**: `nlm query notebook <notebook_id_or_alias> "<question>"`
* **Description**: Queries all or specific sources within the designated notebook.
* **Syntax Examples**:
  ```bash
  # Standard JSON query with timeout parameters
  nlm query notebook 8bcbf9bb-fc5c-448a-839f-74a2d11b1a0e "What is the data ingestion model?" --json --timeout 120

  # Contextual follow-up query using conversation ID
  nlm query notebook 8bcbf9bb-fc5c-448a-839f-74a2d11b1a0e "Can you elaborate on the second point?" -c "session-12345" --json

  # Targeted query restricted to specific source UUIDs
  nlm query notebook 8bcbf9bb-fc5c-448a-839f-74a2d11b1a0e "Extract rainfall projections" -s "11a228e1-7073-4e93-b306-db150f0e3a15,0bc4f075-947a-48bb-bfae-b370b8b34a24" --json
  ```

### 4.2. Generating Notebook AI Summaries
* **Command**: `nlm notebook describe <notebook_id>`
* **Description**: Retrieves high-level notebook summaries and suggested topics.
* **Syntax Example**:
  ```bash
  nlm notebook describe 8bcbf9bb-fc5c-448a-839f-74a2d11b1a0e --json
  ```

### 4.3. Generating Source AI Summaries
* **Command**: `nlm source describe <source_id>`
* **Description**: Returns an AI-generated summary of a single source document, including extracted keywords.
* **Syntax Example**:
  ```bash
  nlm source describe 11a228e1-7073-4e93-b306-db150f0e3a15 --json
  ```

### 4.4. Fetching Source Details
* **Command**: `nlm source get <source_id>`
* **Description**: Gets source metadata and details.
* **Syntax Example**:
  ```bash
  nlm source get 11a228e1-7073-4e93-b306-db150f0e3a15 --json
  ```
