---
query: "writing-th friction"
target: "Arun_Creagy"
mode: deep
timestamp: 2026-09-28 11:27
---

# Trace: writing-th friction

**Target**: Arun_Creagy
**Mode**: deep. Oracle smart search returned only early-June learnings (vector index down, FTS only), so the trace escalated to a read-only dig over retrospectives, `/fyi` logs, diff-evidence, and git.
**Time**: 2026-09-28 11:27
**Purpose**: groundwork for the `thai-writer` global agent (round 1) and the later `writing-th` v7 redesign (round 2).

## Oracle Results
- `ψ/memory/learnings/2026-06-24_crdb-5.2-naturalization-style-lessons.md`: let rhythm, transitions, and noun choice make prose feel authored.
- `ψ/memory/learnings/2026-06-27_crdb-writing-workflow-best-practice.md`: a list of rules was not enough, and the same classes of correction recurred.
- `ψ/memory/learnings/2026-07-03_rrr_preservation-first-thai-editing.md`: preservation is a hard boundary, because detail carries the argument.

## Friction ledger

### 1. The full pipeline was forced onto small jobs
- A pure polish of §3.1 was blocked by `check_draft_preconditions.py` and worked around by renaming the file to `polished-*.md`, a trick "every session rediscovers". See `retrospectives/2026-09/01/15.44_crdb-3.1-pure-p-polish-and-lint-gate-fix.md:20,50`.
- Polish was moved out to qwen and came back with 4 meaning drifts. See `retrospectives/2026-09/01/08.31_rrr_crdb-ch2-2.2-r-reclassification-and-lane-split.md:23`.
- A translation job ran a "reduced harness" because the schema has no translate mode. See `retrospectives/2026-09/11/15.52_gga-targets-thai-translation.md:57`.
- The §5.1 language fix was done by hand after a full run failed Stage 5. See `retrospectives/2026-09/25/22.06_crdb-5-1-language-fix-and-5-1-5-content-fidelity.md:10`.
- Revising an existing draft requires rebuilding its argument map, because drafts are "frozen" until then. See `references/revision-mode.md:10-15`.
- Boss routinely waives Stage 2: "pre-approve every stage, will read at Stage 5". See `retrospectives/2026-09/25/09.00…:13` and `2026-08/29/20.42…:14`.

### 2. Cost and quota
- 15 subagents used about 183.5k tokens for 5 sections. See `retrospectives/2026-08/29/20.42…:77,88` and the post-mortem at `23.27_harness-fidelity…:17-35`.
- 3 Explore agents ran before Stage 0, then verbalizers hit HTTP 429. There was no quota visibility. See `retrospectives/2026-08/29/22.56_crdb-ch4-revision-mode-and-quota-burn.md:19,26,62`.
- The execution-tier table added as a fix grew the spec and restored nothing. See `retrospectives/2026-08/29/23.44_writing-th-execution-tier-upgrade.md:31-33`.

### 3. Hook and tooling bugs
- The draft hook resolves relative paths against the launch directory, so it blocked a subagent's writes twice. See `retrospectives/2026-09/25/00.30_crdb-5-1-inventory-reanalysis-and-hook-bug.md:24`.
- The lint hook points at a venv that doesn't exist, so the advisory always errors. See `retrospectives/2026-09/25/22.06…:12,41`.
- `warrant_trace.py` gives always-fail noise on Thai. See `retrospectives/2026-09/02/00.13…:44`.

### 4. Voice: what Boss keeps correcting (his words)
- "stop using this structure! explaining what it is not is 100% AI sounding" (`logs/info/2026-08-29_12-46_crdb-exec-summary-editing-points-audit.md:21`). Also: "why the negating structure is still here??" (`style/evidence/2026-08-30_15-27…:62`).
- "you always fluff with high-level unspecific abstraction instead of explicitly saying what it is" (`logs/info/2026-08-29_12-46…:23`).
- "the logic of this finding is light and very generic… the reader will say so what?" (`logs/info/2026-08-29_12-46…:25`).
- Other recurring corrections:
  - Self-narration (`retrospectives/2026-09/25/09.00…:18,44`).
  - Over-explaining (`evidence/2026-08-30_14-10…:33`).
  - Intensifiers such as อย่างชัดเจน (`evidence/…4.2…:64`).
  - Bullets folded into prose (`evidence/…4.2…:66`).
  - Compression by rigid frame (`retrospectives/2026-06/27/01.22_rewrite_failure.md:60`).
  - `grounds` compressed into claims (`logs/info/2026-09-01_08-44…:8`).
  - Method sections written as "fluent but empty prose" (`logs/info/2026-09-25_10-30…:14`).
- Tranche-2 item never built: "Move persona out of Stage 0 into a late voice pass" (`logs/info/2026-08-29_13-00_writing-th-harness-architecture.md:56`).

### 5. The voice layer was forgotten, not dropped
- `ψ/memory/resonance/writing-style-th.md` was loaded by the v1–v2 skill. It disappeared in the 2026-08-25 overhaul (`6f70d93`, STYLE_PACK_TH rename). No commit or retro records a decision to drop it.
- `writing_sample/` reaches only the Stage 5 reviewer, as `reference_samples` in about 13 CRDB contracts. The verbalizer loads only `prose-kernel.md`, a rules snapshot.

### 6. Other runtimes are live
- Antigravity edited §5.1 on 2026-09-25 (`3952a8f`, `50e37e3`).
- Codex ran §2.3.2–2.3.3 through Stage 5 on 2026-09-25 (`retrospectives/2026-09/25/09.01…:4`).
- Cross-runtime support still matters.

### What works
- Independent fresh-context Stage 5 review. It caught a garbled term that lint missed (`retrospectives/2026-09/11/15.52…:73`).
- A cold reader, which caught self-narration (`retrospectives/2026-09/25/09.00…:46`).
- Separate contexts for arguing, writing, and reviewing (`retrospectives/2026-09/25/09.01…:51`).
- The argument map for new synthesis (`inbox/2026-08-29_writing-harness-skill-architecture-analysis.md:106`).
- The zero-LLM lint.
- Churn: the skill was redesigned about 9 times in 6 months.

## Lexicon false positives (scan of 118 draft files, 2026-09-28)
- **ฉบับ → รายการ** (a rule for counting deliverables) fires on ฉบับที่ N, ทั้งฉบับ, ฉบับก่อนหน้า, ฉบับใดฉบับหนึ่ง, ฉบับทางการ, and รายงานฉบับกลาง/นี้. It also breaks 2 of the 24 lint fixtures.
- **ห่วงโซ่** fires on ห่วงโซ่ผลกระทบ (Impact Chain), which `writing-style-th.md` lists as a preferred noun.
- **ผลงาน** fires on ตรวจรับผลงาน, the procurement term.
- **ผู้จัดทำ** fires on ผู้จัดทำแผน (plan makers).
- The fixture "clean institutional prose" contains อย่างชัดเจน, which was banned on 2026-08-30. The fixture is stale.

## Actions taken (round 1)
- Built the `thai-writer` agent. Canonical at `.oracle-shared-skills/global-agents/thai-writer.md`, installed at `~/.claude/agents/`.
- Added a per-entry `exceptions` field to literal lexicon rules in `lint_thai_writing.py` and `validate_lexicon.py`, with the test `tests/test_lint_exceptions.py`.
- Created a stub `ψ/memory/style/voice-exemplars-th.md`, awaiting Boss's picks.

## Deferred (round 2)
- A two-lane `writing-th` router.
- Retire `th-verbalizer`, `prose-kernel.md`, `warrant_trace.py`, and the execution tiers.
- Scope the hook to full-lane contracts.
- Fix the hook's path handling and the stale lint venv path.
