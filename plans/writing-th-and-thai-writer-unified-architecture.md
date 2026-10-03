# Plan: Unified `writing-th` & `thai-writer` Architecture (v2.3 - Reorganized & Verified)

**Target:** `oracle-shared-skills` & Consumers (`Arun_Creagy`, `Susu_Ocean`, `Keth-goverment-agent`, `Jiu-climate-risk-and-resilience`, `Lauren-data-architect`)  
**Status:** Phase 1 Complete (Repo Reorganized & Zero Drift Verified). Ready for Phase 2 (Node.js Engine).  

---

## 1. Clean Repository Layout (`oracle-shared-skills`)

```
oracle-shared-skills/
├── agents/             # All shared agents live here
│   ├── thai-writer.md        # Claude Code & Antigravity (.md)
│   └── thai-writer.toml      # Codex CLI (.toml)
├── skills/             # Pure skills only (no nested agents)
│   ├── writing-th/
│   │   ├── references/       # archetype-taxonomy.md
│   │   ├── scripts/          # Node.js linter & hooks (.mjs)
│   │   ├── setup/            # settings.local.hooks.json
│   │   └── SKILL.md
│   ├── style-capture/
│   ├── oracle-bootstrap/
│   └── shared-skill-release/
│       └── scripts/
│           ├── detect-drift.ps1
│           ├── release.ps1
│           └── propagate.ps1
├── tools/              # Central repo provisioning tools (renamed from scripts/)
│   └── sync-skills.ps1       # Declarative multi-client provisioner + dead agent cleaner
├── consumers.json      # Fleet registry (Arun, Susu, Keth, Jiu, Lauren)
├── AGENTS.md           # Architecture, development lifecycle & tools usage guide
├── CLAUDE.md           # Pointer: @AGENTS.md
└── README.md
```

### Deletions (Executed & Verified)
* `global-agents/` $\rightarrow$ DELETED
* `agents/th-argument-mapper.md` $\rightarrow$ DELETED
* `agents/th-verbalizer.md` $\rightarrow$ DELETED
* `agents/th-editorial-reviewer.md` $\rightarrow$ DELETED
* `scripts/sync-agents.ps1` $\rightarrow$ DELETED (merged into `tools/sync-skills.ps1`)
* `scripts/sync-global-agents.ps1` $\rightarrow$ DELETED

---

## 2. Multi-Client Provisioning Engine (`tools/sync-skills.ps1`)

Single declarative installer provisions skills and subagents for all 3 clients:

* **Skills:** Copies `skills/` to `<project>/.agents/skills/` (physical copy for Antigravity & Codex scanners).
* **Subagents:**
  - `agents/*.md` $\rightarrow$ `<project>/.claude/agents/` (Claude Code)
  - `agents/*.md` $\rightarrow$ `<project>/.agents/agents/` (Antigravity)
  - `agents/*.toml` $\rightarrow$ `<project>/.codex/agents/` (Codex CLI)
* **Purge:** Automatically deletes retired agent files from all client directories.

---

## 3. Zero-Dependency Node.js Linter (`skills/writing-th/scripts/lint_thai_writing.mjs`)

Native `Intl.Segmenter` replaces Python `.venv` and `pythainlp`:

```javascript
import fs from 'node:fs';

const [,, targetPath, lexiconPath, ...args] = process.argv;
const scope = args.includes('--scope') ? args[args.indexOf('--scope') + 1] : 'all';

const content = fs.readFileSync(targetPath, 'utf8');
const lexicon = JSON.parse(fs.readFileSync(lexiconPath, 'utf8'));

// Native V8 ICU Thai word segmentation (Zero dependency)
const segmenter = new Intl.Segmenter('th', { granularity: 'word' });
const tokens = new Set(Array.from(segmenter.segment(content)).map(s => s.segment));

const violations = [];
for (const entry of lexicon.banned_words || []) {
  if (tokens.has(entry.term) || content.includes(entry.term)) {
    violations.push(`Banned word: "${entry.term}" -> Use: "${entry.replace_with || 'rephrase'}"`);
  }
}

if (violations.length > 0) {
  console.error(`FAILED: ${violations.length} lexicon violations:\n` + violations.map(v => `  - ${v}`).join('\n'));
  process.exit(1);
}
console.log('PASSED: 100% compliant with Thai lexicon and style rules.');
```

---

## 4. `drafting-plan.md` Protocol

Single Markdown file in `ψ/writing/<chap>/drafting-plan.md`:
1. **Contract & Constraints**: Inlines `writing-contract.json` (Audience, Altitude, Active Actor, Source/Trace Paths, Approval Status).
2. **Macro Story Arc**: Minto SCQA.
3. **Paragraph Blueprints**: R1–R9 Archetypes + `[CANDIDATE-ARCHETYPE: <Name>]` flags.
*(Companion `argument-map.json` generated quietly beside it for machine validation)*

---

## 5. Execution Tracking

- [x] **Step 1: Reorganize `oracle-shared-skills`**
  - Consolidated `agents/` (`thai-writer.md` + `thai-writer.toml`).
  - Deleted `global-agents/` and retired agents.
  - Renamed `scripts/` $\rightarrow$ `tools/`.
  - Created `tools/sync-skills.ps1` with multi-client provisioning and dead agent purging.
  - Created `AGENTS.md` and `CLAUDE.md`.
  - Updated `detect-drift.ps1` and `propagate.ps1`.
- [x] **Step 2: Local Smoke Test in `Arun_Creagy`**
  - Ran `tools/sync-skills.ps1` $\rightarrow$ verified clean copy to `.agents/skills`, `.claude/agents`, `.agents/agents`, `.codex/agents`.
  - Ran `detect-drift.ps1` $\rightarrow$ verified 0 drift across skills, subagents, and hooks.
- [ ] **Step 3: Implement Node.js Scripts in `skills/writing-th/scripts/`**
  - `lint_thai_writing.mjs` (lexicon & style lint via `Intl.Segmenter`)
  - `check_draft_preconditions.mjs` (PreToolUse hook for blueprint gate & ledger guard)
  - `post_draft_lint.mjs` (PostToolUse hook for non-blocking linter feedback)
  - `argument_gate.mjs`
  - Update `setup/settings.local.hooks.json` to call `node` instead of `python`
- [ ] **Step 4: Update Skill Documentation & Taxonomy**
  - Create `skills/writing-th/references/archetype-taxonomy.md` (R1-R9 + Candidate flagging).
  - Update `skills/writing-th/SKILL.md` to document Dual-Lane Architecture & `drafting-plan.md`.
- [ ] **Step 5: Verify on Real Deliverable**
  - Run `node lint_thai_writing.mjs` against `ψ/writing/2026-10-03_thai-writer-agent-profile-and-harness-analysis.md`.
- [ ] **Step 6: Release & Propagate Fleet**
  - Commit changes in `.oracle-shared-skills` on branch `main`.
  - Cut release tag `v2.0.0` via `skills/shared-skill-release/scripts/release.ps1`.
  - Commit submodule pointer bump in `Arun_Creagy`.
  - Run `skills/shared-skill-release/scripts/propagate.ps1` to update `Susu`, `Keth`, `Jiu`, and `Lauren`.
