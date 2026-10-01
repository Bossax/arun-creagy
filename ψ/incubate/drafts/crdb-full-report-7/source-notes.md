# Source notes — บทที่ 7 argument map (Stage 1)

Traceability sidecar for `argument-map.json`. Keeps file locators, paragraph
positions, and judgment calls out of the argument map itself per the
contract's evidence policy.

## Source files read (text extracted, embedded chart images stripped)

- `ψ/incubate/DCCE/CRDB/output/03_Data_Product_Inventory/Section1.5-final-report-5.3.4.md` — product inventory summary. Read via a stripped copy with all `data:image/...` payloads replaced by `[IMAGE-DATA-STRIPPED]`; the stripped copy was written to and read from the session scratchpad only, never saved back into the project tree.
- `ψ/incubate/DCCE/CRDB/output/03_Data_Product_Inventory/Section3.5-final-report-5.3.5.md` — baseline dataset inventory summary. Same stripping method.
- `ψ/incubate/drafts/crdb-full-report-4.2/draft.md` — MVD design (used in full, no tables reproduced in the map).
- `ψ/incubate/drafts/crdb-full-report-4.3/draft.md` — MVD pilot (used in full).
- `ψ/incubate/drafts/crdb-full-report-6/Chapter6-report.md` — recommendations (§6.1–6.3, used with exclusions below).

## Number mismatches found — resolved in favour of the two inventory files

| File | Old figure | Figure used |
|---|---|---|
| `Chapter6-report.md`, §6.2, recommendation 2 paragraph ("บัญชีข้อมูลของแพลตฟอร์มมี 260 ชุดข้อมูลที่รอการรับรอง...") | 260 datasets | 246 datasets (per `Section3.5-final-report-5.3.5.md`). The argument map does not carry this 260 figure into any unit or payload; recommendation 2's grounds/claim in `crdb7-05` describe the workforce-capacity argument without citing a dataset count at all, since the underlying count is stale and the source itself notes the workforce assessment "ยังไม่มีเอกสารสำรวจโครงสร้างกำลังคนของกรม สส. รองรับ" (no workforce survey backs it). |

No other numeric conflicts were found between 4.2/4.3 and the two inventory files (4.2/4.3 do not restate the inventory counts).

## Statements left out of Chapter 6 and why

1. **"มากกว่าหนึ่งในสาม" (more than one-third) concentration claim, §6.2 recommendation 4** — the claim that the five named partner agencies (TMD, GISTDA, กรม ปภ., National Statistical Office, สศช.) hold "more than one-third of the entire data catalogue" is not carried into the argument map. It is very likely computed against the stale 260-dataset figure (or an even older platform-wide catalogue count) rather than the verified 246-dataset baseline inventory, and cannot be independently recomputed from the two Boss files as instructed ("ห้ามคำนวณตัวเลขใหม่"). The map keeps only the five agency names as the target of recommendation 4 (`crdb7-05`), without any concentration percentage.
2. **Recommendation-3 product/service naming, §6.2 vs §6.3** — the same five priority products/services are named slightly differently in the two sections: §6.2 lists "แผนที่ภัยและการเปิดรับภัย" and "ดัชนีความเสี่ยงจากการเปลี่ยนแปลงสภาพภูมิอากาศ"; §6.3 lists "แผนที่ภัยและการเปิดรับ" and "ดัชนีความเสี่ยงด้านภูมิอากาศ" for the same two items. The argument map (`crdb7-05` payload) avoids both variant names and only names the two items whose wording is stable across both sections — the spatial risk database and the disaster loss-and-damage statistics service (plus the A-BTR service, also stable) — flagging this naming drift here for Boss/Stage 2 to confirm which wording the writer should use if the two remaining products are named in prose.
3. **§6.1 lifecycle percentages and 8-item list, §6.2 governance-tier detail, §6.3 8-item roadmap** — used at summary level only (phase percentages, item counts, short/medium-term groupings); the map does not reproduce the full 8-item supporting-information list content, the full 8-item roadmap task wording verbatim, or the detailed duties of each of the 4 governance tiers, per the target altitude ("ไม่ลงรายละเอียดวิธีการและไม่ทวนตาราง").
4. **§6.2 recommendation 3, "บริการที่ 3, 5, 6 และ 8" deferred-service discussion** and the io/agile process narrative around it — left out as implementation detail below this chapter's summary altitude; the map keeps only that recommendation 3 sets contract scope around five priority products/services plus a shared data catalogue under an agile framework with two-plus cycles and a mid-contract test milestone.

## Judgment calls for Boss to check at Stage 2

- Whether the two "stable-naming" product/service labels used in `crdb7-05`'s payload (spatial risk database; disaster loss-and-damage statistics service) are an acceptable substitute for naming all five products/services, given the naming drift in point 2 above.
- Whether omitting the "more than one-third" concentration claim from recommendation 4 (point 1 above) is the right call, versus asking Boss to confirm the figure against the current 246-dataset catalogue so it can be reinstated with a corrected number.
- Confirm the gap wording in `crdb7-02` (content gap / technical gap) is used only once across the whole chapter, as the contract requires — Stage 3 should not restate it in 7.2 or 7.3.
