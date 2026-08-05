# Style Edit Evidence: NCAIF-Institutional
- **Date**: 2026-08-05 16:44 +07:00
- **Source Mode**: `Direct User Correction` (user flagged specific unnatural terms in rendered output; corrections applied in-place across `ψ/incubate/DCCE/CRDB/.timeline-th/curated-events.json` — no git diff or two-file pair available since the file is untracked, so this evidence log reconstructs the before/after pairs from the edit operations directly)
- **File Path**: [[ψ/incubate/DCCE/CRDB/.timeline-th/curated-events.json]]
- **Context**: CRDB project timeline synthesis (`timeline-th` skill), same institutional register as the main report body

---

## 1. Concrete Diff Highlights

| Original / Committed | Human Corrected | Typology |
| :--- | :--- | :--- |
| `จุดยืนสถาปัตยกรรมแบบรวมศูนย์แคตตาล็อก` / `ล็อกจุดยืน...` | `กำหนดสถาปัตยกรรมข้อมูลแบบรวมศูนย์แคตตาล็อก` | Abstract-Noun Scaffolding Removed |
| `ประตูหลัก` (literal "front door") | `โครงสร้างหลัก` | Metaphor-Translation Removed |
| `"Blueprint-as-a-Shield"` (quoted English strategy name) | plain Thai description of what the strategy does (deliver a strong, complete inception package) | English Jargon / Branded-Name Elimination |
| `จุดตัดเวลา` | `เส้นตาย` | Literal Translation → Natural Idiom |
| `ผู้สนับสนุนโครงการ` (generic "project sponsor") | `กรม สส.` | Generic Role Noun → Named Institutional Actor |
| `ที่ขยายผลได้` | `ที่ปรับขยายได้ในอนาคต` | Awkward Modifier → Natural Phrasing |
| `ปิด[deliverable]` (e.g. `ปิดผังเว็บไซต์`, `ปิดพจนานุกรมกลาง`, `ปิดชุดข้อมูลบริการ`, `ปิดรอบสัมภาษณ์`, `ปิดแบบร่างเวิร์กช็อป`) used to mean "completed" | `สรุป[deliverable]` (or a more accurate concrete verb) | Completion-Verb Naturalization |
| `ปิดงาน` (describing a ledger's `Sealed` status) | `ผนึก` | Terminology Precision — matches this system's own `/seal` vocabulary rather than either the banned `ปิด` or the generic `สรุป` |

---

## 2. Tone and Style Shift

* **Dropping "stance"/"gate" abstractions**: `จุดยืน` (stance) and `ประตูหลัก` (front door) are English-concept metaphors translated literally into Thai nouns. Thai institutional prose states the decision or function directly instead of naming an abstract position.
* **No quoted English strategy/brand names**: `"Blueprint-as-a-Shield"` is a project-internal English label. Audience-facing Thai should describe what the strategy *does*, not carry the English branding through quotation marks — this generalizes the existing "Parenthetical Anchor" rule (Section 5 of the pack) from acronyms/schema-names to strategy names as well.
* **Named institutional actor over generic role noun**: `ผู้สนับสนุนโครงการ` is accurate but vague; `กรม สส.` (the department's own shorthand) is what a person inside this project would actually write — this is the same typology as the existing `DCCE` → `กรมฯ` rule, just for a different generic-role phrase referring to the same actor.
* **`ปิด` overused as a generic completion verb**: applied to sitemaps, glossaries, service datasets, interview rounds, workshop drafts — none of these are being "closed/shut," they're being finished, finalized, or summarized. `สรุป` (or a concrete verb naming what actually happened — "จัดทำ...ครบ", "แปลง...เป็น") reads naturally where `ปิด` reads like a literal translation of "close out." The one legitimate exception is a ledger's actual `Sealed` status, which has its own established Thai term in this system (`ผนึก`, from `/seal`) — that is a terminology-precision fix, not a naturalization fix, and should not collapse into `สรุป` either.

---

## 3. Candidate Rules

* **Rule 1 (No Abstract-Noun Scaffolding for Decisions)**: Do not name a decision via an abstract positional noun (`จุดยืน`, `จุดตัด`). State the decision or deadline directly (`กำหนด...`, `เส้นตาย...`).
* **Rule 2 (No Metaphor-Translation for Institutional Roles)**: Avoid literal English metaphors translated into Thai nouns (`ประตูหลัก` for "front door/gateway"). Name the actual function (`โครงสร้างหลัก`, `ศูนย์กลาง...`).
* **Rule 3 (No Quoted English Strategy Names)**: Project-internal English branding/codenames (`"Blueprint-as-a-Shield"`) should not appear in quotes in audience-facing Thai — describe the strategy's actual mechanism instead.
* **Rule 4 (Named Actor Over Generic Role)**: When a generic role noun (`ผู้สนับสนุนโครงการ`) refers to one specific, already-known institutional actor, use that actor's real Thai shorthand (`กรม สส.`) instead.
* **Rule 5 (`ปิด` Is Not a General Completion Verb)**: Reserve `ปิด` for the specific, established meaning of closing/sealing a ledger entry (or use `ผนึก` for that per this system's own `/seal` vocabulary). For "finished producing X," use `สรุป` or a concrete verb naming the actual action, never `ปิด[deliverable]`.

---

## 4. Anti-regression note
- Do **not** reintroduce `จุดยืน`/`จุดตัด` as decision-naming nouns — state the decision directly.
- Do **not** carry a project's internal English strategy codename into Thai prose in quotes, even once, even as a memorable label.
- Do **not** use `ปิด` as a stand-in for "we finished making X" — reserve it for actual ledger-sealing status (or use `ผนึก`), otherwise use `สรุป`/a concrete verb.
