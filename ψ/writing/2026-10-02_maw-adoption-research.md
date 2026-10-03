# Bringing maw into the Arun Workflow: The Conductor Pattern

Research report & adoption roadmap, 2 October 2026. Prepared for Boss.

---

## Executive Summary & Core Verdict

The goal is to transition Arun Creagy from a noisy, cluttered monolith containing 8 months of cross-project history into a **modular, multi-oracle architecture**:
* **Arun is the Project Conductor & Workbench**: Holds project context, handles day-to-day drafting, and is allowed to be messy.
* **Domain Specialists (Keth, Jiu, Lauren) are Permanent Knowledge Vaults**: Hold clean, curated, reusable knowledge (Thai civil service/institutions, climate risk/resilience, and enterprise data architecture).
* **Obsidian is the Human Inspection Gate**: Boss supervises closely, reviewing structured Markdown artifacts on disk without having to manually switch terminals or copy-paste between sessions.

We evaluated three workflows. The optimal adoption path is **Workflow 2 (The Conductor Pattern via Targeted MAW)**, where Arun dispatches domain inquiries to background specialists via `maw hey`, specialists execute against their isolated databases and write findings to `ψ/inbox/`, and Boss reviews them in Obsidian.

---

## 1. How the Work Has Run Since February (Historical Evidence)

Mining ~430 retrospectives, 200 handoffs, and surviving Claude/Antigravity transcripts from February to October 2026 revealed eight persistent patterns:

1. **One Big Project, High Switching Overhead**: CRDB/NCAIF accounts for 50–75% of sessions. Days frequently switch across multiple sub-topics. Roughly 50% of sessions begin with a `/recap` or re-anchoring step.
2. **Rework is Chronic**: ~100 retros mention rewriting or re-deriving deliverables. Loss-and-damage models (DaLA/PDNA) were re-derived 5 times in June; capacity dictionaries went through 5 revisions; procurement and governance lessons were re-documented 4+ times.
3. **Domain Specialists Exist but Were Not Asked**: Keth has possessed OPDC/Budget Bureau M&E notes and a 417-agency database (`bureaucrazy.sqlite`) since 21 September. Yet in the 22 September Sub-law TOR session, Arun fell back on web search and a failed internal search because no bridge to Keth existed.
4. **Manual Cross-Oracle Routing Causes Severe Latency**: Cross-oracle exchange ran exclusively via manual file drops. The CRI retirement hand-over from Arun to Jiu took **~34 hours**, waiting on Boss at every hop to manually open and prompt each session.
5. **Sub-agents Suffer Compliance Bias & Context Tax**: 49 retros record sub-agent friction: scope drift, shallow roleplay ("compliance bias" where subagents agree with Arun's draft rather than auditing it), lossy context compression (51KB drafts compressed to 4KB), and high token burns.
6. **Retrieval in Arun Has Been Noisy**: Stacking 8 months of mixed domain notes in Arun degraded vector and keyword search relevance.
7. **Tooling & Maintenance Overhead**: 20–25% of sessions were spent debugging tool configs, migrations, and MCP connections. Any multi-agent solution must pay for itself without creating a maintenance sink.

---

## 2. Infrastructure Inventory & Tool Realities

Checked on the host machine as of 2 October 2026:

| Component | Current State | Operational Assessment |
| :--- | :--- | :--- |
| **`maw` in WSL (Ubuntu)** | v26.5.21 installed in Ubuntu distro | Present. Needs configuration (`maw.config.json`). |
| **Engine Agnosticism** | `maw` is CLI/engine-agnostic | **Does NOT require Claude Code in WSL.** Can drive `codex`, `agy` (Antigravity), or custom CLI/scripts via `commands.default`. |
| **Oracle Workspaces** | `/mnt/c/Users/sitth/OracleWorkspace/` | Visible directly from WSL. No redundant WSL-side git clones needed. |
| **Memory Containers** | Jiu (47784) & Lauren (47785) running | `oracle-arun-creagy` and `oracle-keth` are currently powered off. They are **not broken**; they simply need `docker start`. |
| **Specialist MCP Access** | Configured per oracle | Arun can be granted read-only MCP access to Keth, Jiu, and Lauren for fast vector search. |
| **`/talk-to` Skill** | Installed | Supports `--inbox` and `--maw`. Needs a standard `ψ/contacts.json`. |

### Critical Technical Findings
1. **`oracle_thread` is Not a Task Queue**: In `oracle-v2` (`engine/src/forum/handler.ts`), posting to a thread automatically returns the first 300 characters of the top vector hit and sets status to `answered`. It does not notify or spawn an active agent.
2. **`oracle_ask` is Extractive Only**: Without `ORACLE_ASK_LLM` environment variables configured in Docker, `oracle_ask` extracts text snippets but does not run an LLM synthesis step.
3. **`/talk-to --inbox` vs `--maw`**: Writing to `ψ/inbox/` drops a file into a mailbox, but nobody is home until Boss opens the session. Adding `maw` rings the doorbell, triggering the specialist in tmux.

---

## 3. The Three Workflows Compared

| Dimension | **Workflow 1: No MAW (Manual Router)** | **Workflow 2: Conductor + Targeted MAW** | **Workflow 3: Full MAW Swarm (Ceiling)** |
| :--- | :--- | :--- | :--- |
| **Interaction Model** | Single-agent Arun. Lookups via MCP. Tasks dropped as inbox files. Boss manually opens specialist sessions. | **Conductor Pattern**: Boss works in **one pane** with Arun. Arun dispatches deep tasks to specialists via `maw hey`. | Multi-agent swarm: team charters, resident tmux panes, scheduler, feed, and web UI. |
| **Human Role During Hand-off** | **Switchboard Operator**: Manually switch terminal windows, prompt the specialist, wait, copy/switch back. | **Reviewer**: Stay in Arun. Inspect the specialist's generated Markdown report in **Obsidian**. | Multi-pane supervisor: monitoring multiple active terminal panes and prompts. |
| **Turnaround Latency** | **Hours to Days** (historical average: 34h). | **Minutes** (autonomous background execution). | Minutes. |
| **Setup Cost** | ~1.5 hours (MCP config + inbox conventions). | ~2 hours (MCP config + WSL `maw.config.json` pointing to Windows repos). | 1–3 tooling sessions + upgrading `maw` and maintaining team YAMLs. |
| **Token & Quota Cost** | Lowest. | Moderate (targeted; specialist panes wake only on demand and sleep). | High (resident panes loading context, periodic scheduler polling). |
| **Memory Isolation** | High (Boss manually curates). | **High**: Clean boundary. Specialist writes report to `inbox/`; Boss reviews in Obsidian before any permanent learning. | Risk of cross-pane context pollution if session history is continued. |
| **Verdict** | Too slow; leaves Boss as human router. | **Recommended target**: Fast, modular, supervised via Obsidian. | Overkill; unnecessary maintenance overhead. |

---

## 4. Addressing Boss's Key Questions & Design Principles

### Q1: "I thought I use maw in one pane?"
* **Resolution**: You **do** use `maw` from one pane. The earlier draft incorrectly assumed you would sit in multiple tmux panes babysitting agents. Under the Conductor Pattern, Arun is your single conversational workbench. Arun calls `maw hey <oracle> "..."` in the background. You never leave Arun’s window.

### Q2: "Can't oracles send answers back and forth?"
* **Resolution**: **Yes.** That is the fundamental reason to use `maw`. Instead of Boss manually copy-pasting questions and answers between windows, Arun dispatches a prompt ticket, the specialist runs its analysis, and the specialist writes the answer directly back to `Arun_Creagy/ψ/inbox/from-<oracle>/` (or sends a return message). The round-trip is automated.

### Q3: "Containers exited with code 255 - why?"
* **Resolution**: The containers (`oracle-arun-creagy` and `oracle-keth`) were simply not powered on after system reboot. They are not crashed; they just need `docker start oracle-arun-creagy oracle-keth`.

### Q4: "Why add guardrail lines to `AGENTS.md`?"
* **Resolution**: 
  1. *In Arun's `AGENTS.md`:* Reminds Arun to ask Keth/Jiu/Lauren for domain theory instead of wasting hours re-deriving loss models or Thai laws.
  2. *In Specialists' `AGENTS.md`:* Prevents specialists from ingesting Arun's messy project drafts into their clean, permanent memory vaults.
  * *Refinement:* Rather than bloating `AGENTS.md` with bureaucratic rules across every repo, this boundary can be cleanly enforced inside the dispatch prompt template itself.

### Q5: "Can't I run `maw` without Claude? How about Codex or Antigravity (`agy`)?"
* **Resolution**: **Yes.** `maw` is completely engine-agnostic. In `maw.config.json`, the `commands.default` field can invoke `codex`, `agy`, or custom CLI scripts. You do not need to install Claude Code in WSL.

### Q6: "What is the role of the `/ask-oracle` (or `/talk-to`) skill?"
* **Resolution**: It acts as the **Workbench Dispatcher & Router**:
  1. **Intent Classification**: Evaluates if the question is a fast factual lookup (routes to read-only MCP) or deep reasoning/audit (routes to `maw hey`).
  2. **Prompt Packaging**: Packages the question with strict bounds (question, background context, allowed files, output format) so the specialist does not need clarifying turns.
  3. **Inbox Retrieval**: Monitors and presents the completed response file from `ψ/inbox/from-<oracle>/` back to you and Arun.

---

## 5. The Conductor & Inspection Architecture

```
                        ┌──────────────────────────────┐
                        │          Boss (You)          │
                        │   • Sets high-level goals    │
                        │   • Reviews in Obsidian      │
                        │   • Approves final output    │
                        └──────────────┬───────────────┘
                                       │ Interactive Dialogue
                                       ▼
                        ┌──────────────────────────────┐
                        │      Arun (The Conductor)    │
                        │   • Project Execution Lead   │
                        │   • Holds project context    │
                        │   • The "Messy Workbench"    │
                        └──────────────┬───────────────┘
                                       │ maw hey (Under the hood)
            ┌──────────────────────────┼──────────────────────────┐
            ▼                          ▼                          ▼
┌───────────────────────┐  ┌───────────────────────┐  ┌───────────────────────┐
│         Keth          │  │          Jiu          │  │        Lauren         │
│  Gov & Bureaucracy    │  │  Climate Resilience   │  │   Data Architecture   │
│  (bureaucrazy.sqlite) │  │  (CRI & Risk Models)  │  │   (CDM / LDM Vault)   │
└───────────┬───────────┘  └───────────┬───────────┘  └───────────┬───────────┘
            │                          │                          │
            └──────────────────────────┼──────────────────────────┘
                                       │ Structured Markdown Output
                                       ▼
                        ┌──────────────────────────────┐
                        │       Obsidian Vault         │
                        │  (ψ/inbox/from-<oracle>/...) │
                        │  • Inspected & verified by Boss│
                        └──────────────────────────────┘
```

### The Two-Lane System
1. **Lookup Lane (Fast & Read-Only)**:
   * Used for quick factual questions (e.g., *"What is the citation for มาตรา 158?"*).
   * Arun queries the specialist's Docker memory container directly via read-only MCP tools (`oracle_search`, `oracle_read`).
   * No background agent is woken; zero tmux overhead.
2. **Request Lane (Deep Synthesis & Reasoning)**:
   * Used when domain analysis or database execution is required (e.g., *"Query bureaucrazy.sqlite and evaluate our M&E platform proposal against OPDC agency mandates"*).
   * Arun formats a request and dispatches it via `maw hey <oracle>`.
   * The specialist wakes up in its own workspace, executes with its local tools, writes the resulting Markdown report to `Arun_Creagy/ψ/inbox/from-<oracle>/`, and shuts down.
   * Boss inspects the report in **Obsidian**.
   * Arun integrates the verified findings into the project deliverable.

---

## 6. Step-by-Step Test Instructions (Workflow 2 Smoke Test)

Follow these precise steps to validate Workflow 2 end-to-end.

### Phase 1: Pre-Flight Environment Setup

1. **Power on Oracle Docker Containers (in Windows PowerShell)**:
   ```powershell
   docker start oracle-arun-creagy oracle-keth
   docker ps --filter "name=oracle-"
   ```
   *Verify that `oracle-arun-creagy`, `oracle-keth`, `oracle-jiu`, and `oracle-lauren` are all status `Up`.*

2. **Configure `maw` & Link Oracles in WSL Ubuntu**:
   `maw` scans for repos under `~/Code/github.com/<org>/<repo>` containing a `ψ/` folder. In your WSL Ubuntu terminal, run these exact commands:
   ```bash
   # Create the maw config pointing default runner engine to agy
   mkdir -p ~/.config/maw
   echo '{"host":"local","port":3456,"commands":{"default":"agy"}}' > ~/.config/maw/maw.config.json

   # Link your Windows OracleWorkspace repos into maw's expected discovery path
   mkdir -p ~/Code/github.com/local
   ln -s /mnt/c/Users/sitth/OracleWorkspace/Keth-goverment-agent ~/Code/github.com/local/keth
   ln -s /mnt/c/Users/sitth/OracleWorkspace/Jiu-climate-risk-and-resilience ~/Code/github.com/local/jiu
   ln -s /mnt/c/Users/sitth/OracleWorkspace/Lauren-data-architect ~/Code/github.com/local/lauren
   ln -s /mnt/c/Users/sitth/OracleWorkspace/Arun_Creagy ~/Code/github.com/local/arun
   ```

3. **Discover & Verify Your Fleet**:
   In WSL Ubuntu, trigger the discovery scan:
   ```bash
   # Scan and cache all local oracles
   maw oracle scan

   # Verify the active fleet is registered
   maw oracle ls
   ```
   *Verify that `local/keth`, `local/jiu`, `local/lauren`, and `local/arun` appear in the output with their `ψ/` badges.*

---

### Phase 2: Smoke Test Execution (The Sub-law TOR Query)

* **Objective**: Have Arun query Keth to resolve the DCCE vs. TMD statutory database authority question from the 22 September Sub-law TOR session without Boss manually opening Keth's repo.

1. **Dispatch from Arun (or WSL Terminal)**:
   Run the task dispatch:
   ```bash
   maw hey local:keth "Perform a statutory audit: Under the draft Climate Change Act Chapter 12 and current Thai bureaucratic mandates, what is the exact database authority boundary between DCCE and the Thai Meteorological Department (TMD)? Check bureaucrazy.sqlite and existing governance notes. Output your findings as a structured brief to /mnt/c/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/inbox/from-keth/2026-10-02_tmd-authority-test.md"
   ```

2. **Autonomous Background Run**:
   * Keth receives the prompt in its dedicated tmux session.
   * Keth queries `bureaucrazy.sqlite` and its internal knowledge base.
   * Keth formats the brief and saves it directly to:
     `C:\Users\sitth\OracleWorkspace\Arun_Creagy\ψ\inbox\from-keth\2026-10-02_tmd-authority-test.md`

3. **Human Inspection Gate in Obsidian**:
   * Open **Obsidian** in the `Arun_Creagy` vault.
   * Navigate to `ψ/inbox/from-keth/2026-10-02_tmd-authority-test.md`.
   * **Review Criteria**:
     - Did Keth cite specific laws/mandates accurately?
     - Did Keth answer without asking unnecessary clarifying questions?
     - Is the output clear and ready for Arun to incorporate?

4. **Loop Closure in Arun**:
   * Return to Arun's session.
   * Arun reads `ψ/inbox/from-keth/2026-10-02_tmd-authority-test.md`.
   * Arun summarizes the key findings and drafts the TOR clause.

---

### Phase 3: Success Criteria & Decision Gate

The test passes if:
1. **Zero Session Hops**: Boss did not have to open a separate terminal window, cd into `Keth-goverment-agent`, or prompt Keth manually.
2. **Turnaround Time < 5 Minutes**: Keth's report is generated and ready in Obsidian in under 5 minutes (compared to the historical 34-hour manual round-trip).
3. **Domain Rigor**: The answer reflects Keth's deep civil service lens rather than a generic web summary.
4. **Zero Memory Contamination**: A `git status` check in `Keth-goverment-agent` confirms that Keth did **not** commit Arun project drafting artifacts into its permanent memory vault.

If all criteria pass, Workflow 2 is verified as the standard multi-oracle operational model for the Arun Creagy workbench.
