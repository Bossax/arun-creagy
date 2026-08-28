# Plan — Diagnose Boss's edits to exec-summary 1.2–1.4, capture style, score the three agents

## Context

Three executive-summary sections were drafted by three different AI agents on 2026-08-28, each through the `writing-th` v5 harness, each passing its editorial gate at standard assurance:

| Section | Drafting agent | Draft file | Receipt verdict |
|---|---|---|---|
| 1.2 | **Claude** | `ψ/incubate/drafts/crdb-exec-summary-1.2/02_th_draft.md` | pass, 4 accepted minor |
| 1.3 | **Antigravity** | `ψ/incubate/drafts/crdb-exec-summary-1.3/02_th_draft.md` | pass, 0 findings |
| 1.4 | **Codex** | `ψ/incubate/drafts/crdb-exec-summary-1.4/section-1.4-draft.md` | pass, 0 findings |

Boss has now hand-edited all three in the working tree. Every gate said "pass"; Boss still made 35 insertions / 36 deletions and left ~12 inline `%%...%%` complaints. That gap — between what the harness certifies and what Boss accepts — is the thing worth learning from, and this is the first time three different models can be compared on the same brief, same harness, same day.

Two outputs are wanted: **the style Boss actually prefers**, captured durably, and **a comparative read on how the three agents performed**.

Scope decisions already made:
- **Diagnose only.** No draft is edited. The `%%` comments stay where they are; Boss resolves them.
- **One merged Style-Pack**, not three.
- **One comparative scorecard**, not three separate reports.

## Approach

Three read-only subagents in parallel (one per section) each produce a single structured observation file. I then merge, run the promotion gate, and write the two deliverables.

### Working directory

New, isolated: `ψ/incubate/analysis/2026-08-28_exec-summary-1.2-1.4-review/`

```
obs-1.2.md                    written by subagent A (Claude's draft)
obs-1.3.md                    written by subagent B (Antigravity's draft)
obs-1.4.md                    written by subagent C (Codex's draft)
STYLE-OBSERVATIONS-MERGED.md  written by me
PERFORMANCE-SCORECARD.md      written by me
```

---

## Phase A — three diagnostic subagents, in parallel

Each subagent is told: **you may write exactly one file, `obs-1.X.md`. Do not touch the draft, the contract, the receipt, or anything under `ψ/memory/`.**

### Inputs handed to each subagent

- Committed draft: `git show HEAD:<path>` — the AI's output
- Working-tree draft: the same path — Boss's edited version
- `writing-contract.json` and `editorial-review.json` from its folder
- Evidence sidecar where one exists (1.2 and 1.4 have one; **1.3 has none** — that is itself a finding)
- `ψ/memory/style/STYLE_PACK_TH.md` and `ψ/memory/style/LEXICON_TH.json` — so each candidate can be marked *new* vs *already covered*
- §4 and §10 of the approved plan: `ψ/incubate/DCCE/CRDB/output/final_deliverable/แผนการเขียนบทที่ 1 รายงานฉบับสมบูรณ์และรายงานฉบับย่อสำหรับผู้บริหาร.md`

### Fixed schema for `obs-1.X.md`

**1. Edit inventory.** Every changed span, quoted before/after in Thai verbatim, sorted into exactly one bucket:

| Bucket | Meaning |
|---|---|
| `STYLE` | same claim, Boss preferred a different way of saying it → candidate rule |
| `TERMINOLOGY` | term swap → candidate lexicon entry |
| `SUBSTANCE` | Boss changed, added, or cut the claim itself → agent got the content wrong |
| `COMMENT` | a `%%...%%` annotation → a complaint, never a style rule |
| `TYPO` | Boss's own typing slip → **quarantined, never a rule** |

The `TYPO` bucket is mandatory and is the single most important guard here. Boss's edits introduced real typing slips — `ข้อมูเ`, `ปนะมวลผล`, `ส่วนแรกคือคือ`, `ค่อนข้าวกว้าง`, `ไม่สารมารด`, `เป้นต้นแบบ`, `มียทบาท`, `รักษคุณภาพ`, `แต่ล่ะ`, `พลตฟอร์ม`, `ปรากฎ`. Without this bucket the pack would learn `แต่ล่ะ` over `แต่ละ` as a preference. Each subagent lists the typos it finds in its own section and marks them excluded from rule extraction.

**2. Candidate style rules.** Each with: banned form, preferred form, reason, proposed `kind` (`literal` | `regex` | `structural`), proposed `scope`, and whether `STYLE_PACK_TH.md` already covers it. No promotion decisions at this stage — subagents propose, they do not promote.

**3. Gate-escape analysis.** For each of the 11 executive-summary dimensions the receipt marked `pass`, ask: did Boss's edits contradict that verdict? This is the diagnostic core — e.g. 1.2's receipt passed `causal_logic`, yet Boss wrote `%%it is not the cause. it is evidence ! poor causal relationship%%` and `%%still bad logic. I deleted it%%` on that exact dimension.

**4. Performance assessment** of the source agent, on fixed comparable metrics:

- **Edit density** — changed paragraphs / total paragraphs, *and* changed characters / total characters. Both are required: raw line counts mislead badly here because 1.2 is 27 KB and 1.3 is 7.7 KB, and one Thai "line" is a whole paragraph.
- **Severity mix** — the `SUBSTANCE` : `STYLE` ratio. A high `SUBSTANCE` share means the agent got the content wrong, not merely the wording.
- **Contract compliance** — did it deliver every `required_structures` item?
- **Receipt honesty** — did its own review find what Boss found, or did it certify past the problem?
- Top 3 failure patterns, top 2 genuine strengths.

### Known asymmetries the subagents must report rather than smooth over

- **1.3 has no evidence sidecar** and a much thinner contract (2.4 KB vs ~12 KB), with a loose `evidence_policy`. Its clean receipt was produced by an *Antigravity* reviewer reviewing an *Antigravity* draft — the independence is questionable. A zero-finding receipt on a thin contract is not the same achievement as a zero-finding receipt on a strict one, and the scorecard must not treat it as such.
- **1.4 carries a contract-vs-plan conflict.** Its contract *requires* the 16/26/33 readiness metric in reader-facing text; Boss deleted that whole paragraph with `%%I think the plan states clearly that no gap analysis%%`. If the plan forbids gap analysis, the contract was wrong and Codex complied correctly with a bad instruction. That distinction decides whether this counts against Codex or against the contract author — the subagent must check the plan and say which.
- **Structural inconsistency across the three:** 1.2 uses bold-run subheads under `#`, 1.3 a bare `###` with no subheads, 1.4 `#` plus numbered `##` with figure placeholders and a table. This will surface at merge time regardless of style capture.

---

## Phase B — synthesis (me, no subagents)

### 1. Merge

Write `STYLE-OBSERVATIONS-MERGED.md`, deduplicating candidates across the three sections. The natural promotion signal: **a pattern Boss corrected in ≥2 of 3 independently-drafted sections is a rule; a pattern corrected once is a local edit.** Three parallel drafts of the same brief make this an unusually clean corpus for that threshold.

### 2. Run the promotion gate — do not bypass it

Per `style-capture` SKILL.md step 4b, using `.agents/skills/writing-th/scripts/register.py`:

```
register.py observe "<pattern>" --source <file> --fix "<preferred form>"   # once per sighting
register.py ready                                                          # what has earned promotion
```

Only what `ready` returns goes into the pack. Everything else stays in the register and waits — nothing is deleted. The one exception the skill itself allows is severity-first promotion (precedent: rule 40, 2026-08-27); if I use it, I label it as such in the capture-log entry rather than passing it off as threshold-earned.

### 3. Write the Style-Pack update

- New dated entry appended to `STYLE_PACK_TH.md` §9 Incremental Capture Log: `### 2026-08-28 — Style-pack upgrade from exec-summary 1.2–1.4 three-agent human review`. Bump `Samples Learnt` in the header.
- Typed entries into `LEXICON_TH.json`, each with `banned`, `preferred`, `reason`, `kind`, `scope` — and `pattern` for any `regex`. Anything that cannot be an exact string or a compiling regex is written `kind: structural`, never as an English description in `banned` (that no-op mistake killed three rules on 2026-08-05).
- Validate: `python .agents/skills/writing-th/scripts/validate_lexicon.py ψ/memory/style/LEXICON_TH.json`
- Close out: `register.py promoted "<pattern>"`
- Diff evidence per the skill: `ψ/memory/style/evidence/2026-08-28_<HH-MM>_TH_diff-evidence.md`

### 4. Write the scorecard

`PERFORMANCE-SCORECARD.md` — comparative table plus narrative:

| | Claude (1.2) | Antigravity (1.3) | Codex (1.4) |
|---|---|---|---|
| Edit density (¶ and char) | | | |
| SUBSTANCE : STYLE ratio | | | |
| Contract compliance | | | |
| Receipt honesty | | | |
| Dominant failure mode | | | |
| Genuine strengths | | | |

Plus a section on **what the harness cannot see** — patterns that cleared all 11 dimensions and still drew a complaint. That is the actionable half for improving the gate.

---

## Files this touches

**Created (new, isolated):**
- `ψ/incubate/analysis/2026-08-28_exec-summary-1.2-1.4-review/` — 5 files

**Modified — style memory only, and only via the `style-capture` maintenance path:**
- `ψ/memory/style/STYLE_PACK_TH.md` — append one capture-log entry, bump header
- `ψ/memory/style/LEXICON_TH.json` — add typed entries
- `ψ/memory/style/miss_register.db` — append observations
- `ψ/memory/style/evidence/2026-08-28_<HH-MM>_TH_diff-evidence.md` — new

These four are the **only** writes outside `ψ/incubate/`. `writing-th` invariant 5 permits style-memory writes solely through its own maintenance skill, which is `style-capture` — this is that invocation. If you would rather see the merged observations first and approve the pack write as a separate step, say so and I will stop after Phase B step 1.

## Explicitly not doing

- No edits to any of the three drafts — including no removal of the `%%` comments
- No regenerated receipts, no re-running the editorial gate, no re-review
- No merge into a destination report (the destination `final_deliverable/Executive Summary Report/` is still empty)
- No project-ledger writes — `seal` is not invoked
- No commits

## Verification

1. `git status` shows the three drafts still ` M` with byte-identical content to now — `git diff --stat` still reads `35 insertions(+), 36 deletions(-)`.
2. `python .agents/skills/writing-th/scripts/validate_lexicon.py ψ/memory/style/LEXICON_TH.json` exits clean.
3. `register.py ready` returns empty for every pattern written into the pack (each was closed with `promoted`).
4. `register.py stats` shows observation counts rose by the number of sightings recorded, and nothing was deleted.
5. Every rule in the new capture-log entry traces to a quoted before/after pair in one of the three `obs-1.X.md` files — no rule appears that a subagent did not evidence.
6. No typo from the quarantine list appears anywhere in `LEXICON_TH.json` as a `preferred` value.
7. `python .agents/skills/writing-th/tests/run_tests.py` still passes (the lexicon changed; the harness reads it).

## Open question for you

Section 1.4's contract required the 16/26/33 readiness figure that you deleted as "no gap analysis". If the plan does forbid it, the contract was written wrong — and I should say so in the scorecard rather than mark it against Codex. The subagent will check the plan and report which way it falls.
