# Plan: Global Synergetic PM v2.0 Migration

**Date**: 2026-04-13
**Author**: Arun Creagy & Susu Ocean Mao

## Goal
Promote the local "Synergetic PM v2.0" habit from the Susu_Ocean workspace to a **Global Family Habit** available across all workspaces (including Arun_Creagy).

## 1. Structural Alignment

### 1.1 Standardized Ledger Naming
Adopt the automated-friendly naming convention: **`LedgerName-ProjectName.md`**.
- `Trigger-Log-CRDB.md` (renamed from `CRDB-Trigger-Log.md`)
- `Deliverable-Map-CRDB.md` (renamed from `CRDB-Deliverable-Map.md`)
- `Evidence-Registry-CRDB.md` (renamed from `CRDB-Evidence-Registry.md`)
- `Change-Log-CRDB.md` (renamed from `CRDB-Change-Log.md`)

### 1.2 Atomic Skill Encapsulation
Move the shared `replace-md-table.ts` logic into a global utility or embed it inside each skill's directory.
- Each skill folder in `~/.gemini/skills/pm-*/` must be self-contained.
- Use `bun run <skill-path>/pm-*.ts` for execution to ensure environment-independent runs.

### 1.3 Command Dispatch Refactor
Update `pm-spark` and other composite skills to call the global slash-commands instead of local file paths.
- Call `/pm-trigger`, `/pm-commit`, and `/pm-catch` via the CLI bridge.

---

## 2. Implementation Sequence

### Phase 1: Local Refactoring (in Susu_Ocean)
- [ ] Refactor `replace-md-table.ts` into an internal module within each `pm-*` skill.
- [ ] Update `pm-spark.ts` to call slash-commands.
- [ ] Test the causal chain one last time locally on `Munnork-Soundscape-2026`.

### Phase 2: Global Installation
- [ ] Manually copy (or symlink) refactored skills from `Susu_Ocean/.gemini/skills/` to `C:/Users/sitth/.gemini/skills/`.
- [ ] Register the new skills in the global `~/.gemini/settings.json` or `.oracle-skills.json` if required.
- [ ] Verify global availability using `/help` or `/pm-spark`.

### Phase 3: Workspace Migration (Arun_Creagy)
- [ ] Rename existing CRDB ledgers to the new `LedgerName-CRDB.md` format.
- [ ] Execute `/pm-catch` on existing CRDB files to build the high-signal `Evidence-Registry-CRDB.md`.
- [ ] Create a "Spark" entry for the next CRDB workshop iteration to test the global causal chain.

---

## 3. Success Metrics
- **Atomicity**: PM skills work even if the `scripts/` folder is missing in a repo.
- **Traceability**: All CRDB evidence is anchored to a D/CH/T-ID.
- **Synchronization**: `plan.md` automatically updates whenever a `/pm-commit` or `/pm-spark` occurs.

---

## Next Action
Start **Phase 1: Local Refactoring** in the `Susu_Ocean` workspace.
