---
date: 2026-10-02 00:40
type: info
status: raw
significance: interesting
---

# Knowledge Isolation & Oracle Splitting: Process Design, Execution, and Skill Blueprint

Reflecting on the complete multi-session lifecycle of splitting the monolithic **Arun_Creagy** Oracle into specialized Oracles (**Jiu** for Climate Risk & Resilience, and **Lauren** for Enterprise Data Architecture & UX). This cycle establishes the architectural foundation for an upcoming skill (e.g., `/oracle-split` or `/isolate-domain`).

---

## 1. Context & Motivation

As an Oracle workspace matures, cognitive saturation occurs:
1. **Context Window Contamination**: When multiple complex domains (e.g., CRI statistical calculations, CRDB enterprise data governance, and national policy writing) coexist in one Oracle, agent searches become cluttered with conflicting jargon, disparate schemas, and massive irrelevant file trees.
2. **Filesystem and Tooling Bloat**: Deep build trees (e.g., Python `.venv`, bundled PyInstaller distributions, GeoJSON layers) inflate directory scans, slowing down search tools and causing timeout failures.
3. **Divergent Lifecycles**: A data modeling project requires different reasoning cadences and tools than an ongoing policy drafting project.

Separating a sub-domain into an independent, focused Oracle restores cognitive sharpness and operational agility.

---

## 2. Core Process Design Principles

1. **Zero-Loss Asymmetric Safety (Staging Before Deletion)**
   - Never perform an in-place "cut and paste".
   - The parent workspace remains 100% intact while knowledge is extracted and staged into the child Oracle (`ψ/active/incoming_<slug>/`).
   - The parent retains custody until the child independently proves it has ingested, organized, and verified the domain.

2. **Knowledge Artifacts vs. Tooling/Build State**
   - A knowledge split must migrate **evidence, schemas, decisions, catalogs, and documentation**.
   - It must explicitly reject or segregate local virtual environments (`.venv`), temporary scripts, experimental debug notebooks, and bundled application binaries (`dist/`). Tooling is ephemeral; domain models are durable.

3. **Verifiable Provenance over Lossy Summarization**
   - Every staged asset must be recorded in a master manifest with SHA-256 checksums, byte counts, and relative source paths.
   - Integrity must be provable across the boundary without manual guesswork.

4. **The Selective Rescue Gate**
   - A specialized domain often contains foundational literature or cross-cutting standards (e.g., disaster risk frameworks, national data standards, historical casualty datasets) that are valuable to the parent Oracle beyond the retiring project.
   - Retirement must include an explicit human-in-the-loop audit to rescue generalizable assets before triggering deletions.

5. **Cold Archiving vs. Complete Annihilation**
   - In accordance with [`03-brain-structure.md`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/.agents/mandates/03-brain-structure.md), retired project containers must be moved from `ψ/incubate/` to `ψ/archive/`, retaining project registers, evidence logs, and unmigrated core notes rather than being completely destroyed.

---

## 3. The Actual End-to-End Execution Cycle

The CRI/CRDB split unfolded across 5 distinct phases over 3 sessions:

```
[Phase 1: Discovery & Tiers] ──> [Phase 2: Staging & Handshake] ──> [Phase 3: Child Verification Gates]
                                                                                │
[Phase 6: Archive & Repack]  <── [Phase 5: Parent Retirement Gate] <────────────┘
```

### Phase 1: Domain Scoping & Multi-Tier Curation (Session 2026-09-30)
- Explored parent holdings and categorized target domain knowledge into functional tiers (e.g., upstream standards, canonical schemas, UX interaction specs, enterprise architecture, decision heuristics, catalogs).
- Filtered out unconstrained directory traversals (e.g., skipping deep mirrored vendor trees in `ψ/learn/`).

### Phase 2: Staging & Onboarding Handshake
- Scripted staging (`stage_crdb_to_lauren.py`, CRI packaging) into child Oracle trees (`Jiu/` and `Lauren/`).
- Generated `MANIFEST.md` with SHA-256 hashes and delivered onboarding guidance files to the children's `ψ/inbox/`.

### Phase 3: Autonomous Verification (The 3 Child Gates in Jiu)
Before authorizing retirement in Arun, Jiu established 3 verification gates:
- **Gate 1 (Safe External Preservation):** Backed up byte-level snapshots to external storage (`D:\cri-migration`, 1,048 files, 1,035 MB).
- **Gate 2 (Answer Quality Audit):** Jiu executed a 33-question evaluation across English, Thai, and challenge prompts to prove grounding with zero false premises accepted.
- **Gate 3 (Live Rehash Verification):** Re-verified candidate paths against Arun's live directory (`trace_origins.py --check-candidates` -> 897 matched byte-for-byte).

### Phase 4: Formal Return Signoff Notice
- Jiu issued formal intake memo [`2026-10-01_jiu-cri-migration-retirement-ready.md`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/inbox/2026-10-01_jiu-cri-migration-retirement-ready.md) to Arun's `ψ/inbox/`, cataloging 897 candidate files and 67 ambiguous files to remain untouched.

### Phase 5: Defensive Retirement Execution (Session 2026-10-01)
- **Rescue Step:** Scanned manifest for loss-and-damage / disaster risk sources. Boss selected 8 core files to keep in Arun (`loss23Y_DDPM.csv`, FEMA tech doc, Sendai terminology, etc.) and approved 887 for deletion.
- **Pre-Deletion Gate:** Ran PowerShell script computing on-the-fly SHA-256 hashes before each deletion (887 deleted, 0 mismatches, 0 errors).
- **Residual Discovery & Purge:** Audited unmanifested directory bloat, removing 28,918 `.venv` files, 288 MB `cri_deploy` outbox folder, and 43 pipeline data files.

### Phase 6: Archive Relocation & Version Control
- Moved the remaining 38 CRI files and project registers from `ψ/incubate/DCCE/CRI` to `ψ/archive/DCCE/CRI`.
- Committed deletions and archive move in Git across 2 commits (`85ca8ca1` and `b833a09c`).
- Ran `git gc --prune=now --aggressive`, consolidating the repository to a single 372 MiB packfile.

---

## 4. Results Achieved

1. **Cognitive Focus**: Jiu owns Climate Risk & Resilience; Lauren owns Data Architecture & CDM; Arun focuses on DCCE CRDB final reporting and national adaptation policy.
2. **Physical Hygiene**: Cleared >30,000 files and ~3.5+ GB of working tree bloat from Arun.
3. **Zero Knowledge Loss**: Every migrated asset is verified in Jiu/Lauren and backed up at `D:\cri-migration`; essential cross-cutting literature is preserved in Arun's `ψ/archive/`.
4. **Clean Active Incubate Tree**: `ψ/incubate/DCCE/` now contains solely the active `CRDB` project.

---

## 5. Blueprint for a Reusable Skill (`/oracle-split` or `/isolate-domain`)

If this workflow is codified into a standardized Oracle skill, the following improvements must be engineered:

### 1. Mandatory Directory-Level Pre-Flight Diff
* *Current Flaw:* The agent assumed the 897-file manifest accounted for the entire `ψ/incubate/DCCE/CRI/` folder, failing to detect 36,929 uncataloged build files in `data_system/` until the user flagged it.
* *Skill Requirement:* The skill must run an orphan scan up front:
  $$\text{Orphaned Files} = \text{Total Working Directory Files} - \text{Manifest Candidate Files}$$
  It must categorize orphans into: (a) build bloat (`.venv`, `dist/`), (b) uncataloged data, (c) project ledgers/notes.

### 2. Built-in Environment & Artifact Stripper
* Standardize automated pre-retirement rules that purge or ignore known noise before calculating hashes:
  `exclude = ['.venv', 'node_modules', '__pycache__', '.tmp.*', 'dist', 'build']`

### 3. Machine-Readable Handshake Protocol
* Instead of unstructured markdown memos in `ψ/inbox/`, use a schema-validated contract (`migration-contract.json` or `retirement-receipt.json`):
  ```json
  {
    "source_oracle": "Arun",
    "target_oracle": "Jiu",
    "domain": "dcce-cri",
    "gates": { "backup_verified": true, "qa_passed": true, "rehash_passed": true },
    "candidates_count": 897,
    "manifest_hash": "sha256:..."
  }
  ```
  This allows automated tool verification without human interpretation friction.

### 4. Interactive Selective Retention Filter
* The skill should automatically cluster retiring files by semantic domain and present an interactive selection UI (or categorized checklist) allowing the human to rescue cross-cutting references before deletion.

### 5. Integrated Git History Hygiene
* Since Git packfiles retain historical blobs even after working-tree deletion, the skill should include an automated advisory or optional automated execution of `git-filter-repo` to excise heavy migration targets from past commits.

---
Logged via /fyi
