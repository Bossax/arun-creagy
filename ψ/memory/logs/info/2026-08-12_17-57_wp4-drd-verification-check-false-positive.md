---
date: 2026-08-12 17:57
type: info
status: raw
significance: neutral
---

While generating the WP4 Developer-Ready Design Requirements Specification (`04_Sitemap/2026-08-12-WP4-Developer-Ready-Design-Requirements-Specification.md`) and its companion CSVs, one verification check reported FAIL. The failure was in the check itself, not in the delivered document or data.

**The check**

```python
ok(sum(1 for d in ds if 'UNKNOWN' in d['maintainer'] or 'assigned' in d['maintainer'])==11,
   'no data spec claims a maintainer it does not have')
```

This counted how many of the 11 data specification sheets had a `maintainer` field containing the literal substring `UNKNOWN` or `assigned`, and expected all 11 to match.

**Why it failed**

Three of the eleven specs (DS-04, external agency data; DS-05, no dataset behind the page yet; DS-08, a compilation task) correctly use `maintainer = "Not applicable"` rather than `UNKNOWN` or `To be assigned`, since "who maintains it" isn't a meaningful question for those three. `"Not applicable"` contains neither search substring, so the check counted 8 instead of 11 and printed FAIL.

**What was actually true**

All 11 maintainer values were honest and correctly differentiated: `UNKNOWN` (5), `Not applicable` (3), `To be assigned` (3). No spec claimed a maintainer it couldn't back up. The data was fine; the check's string-matching was too narrow to recognize a third valid "we don't know" phrasing.

**Fixed 2026-08-12.** Rewrote the check against a set of three honest-unknown markers instead of two hardcoded substrings, saved as `verify_data_specs.py` in scratchpad rather than left as a disposable inline command. Re-run confirms all 11 pass: `{'UNKNOWN': 5, 'Not applicable': 3, 'To be assigned': 3}`.

**Why this is worth keeping**

A pattern worth watching for in future self-written verification scripts: a check that greps for a fixed set of "acceptable unknown" markers will false-positive whenever the content legitimately uses a synonym the check didn't anticipate. When a check fails, read the actual values before assuming the deliverable is wrong — the check itself is also a piece of just-written code and can be the buggy part. Also worth noting: this file's first draft misquoted its own counts (said UNKNOWN was 7, actually 5) — a reminder to verify numbers against source rather than recall, even in a note about verifying numbers.

Related: [[project-crdb-wp4-drd-tiering]] (memory), the WP4 DRD five-tier plan itself.

Logged via /fyi
