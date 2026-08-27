# Harness Artifact Schemas v1.0

Both artifacts are UTF-8 JSON files stored beside the isolated draft. Paths may
be absolute or repository-relative. Timestamps use ISO 8601.

## `writing-contract.json`

```json
{
  "schema_version": "1.0",
  "profile": "executive-summary",
  "transformation_mode": "synthesis",
  "audience": "DCCE executives and policy owners",
  "decision_use": "Understand the national information gap and approve the blueprint direction",
  "section_job": "Establish the problem, governing response, and decision value",
  "target_altitude": "Five-minute executive read; findings and implications, not full methods",
  "inclusions": ["three information-use failures", "web/data platform distinction"],
  "exclusions": ["slide locators", "per-platform literature review", "section roadmap"],
  "evidence_policy": "Use verified facts in prose; keep internal locators in the traceability sidecar",
  "required_concepts": ["findability", "trust", "usable form"],
  "terminology": {"first_mention": "โครงสร้างข้อมูลด้านการปรับตัวต่อการเปลี่ยนแปลงสภาพภูมิอากาศ", "short_form": "โครงสร้างข้อมูลฯ"},
  "required_structures": ["four-question table", "figure placeholder for development process"],
  "source_paths": ["path/to/source.md"],
  "reference_samples": ["path/to/approved-sample.md"],
  "approval": {"status": "approved", "approved_by": "Boss", "approved_at": "2026-08-28T01:00:00+07:00"}
}
```

Required profiles are `executive-summary`, `report`, `article`, or `letter`.
Required modes are `rewrite`, `synthesis`, or `new`. Every listed key is
required; lists and terminology may be empty only when the contract explains why
through the corresponding prose field. `approval.status` must be `approved`
before review or merge.

## `editorial-review.json`

Create the initial file with `editorial_gate.py prepare`; do not type hashes by
hand.

```json
{
  "schema_version": "1.0",
  "rubric_version": "5.0.0",
  "draft_sha256": "generated",
  "contract_sha256": "generated",
  "profile": "executive-summary",
  "reviewer_mode": "independent",
  "assurance": "standard",
  "reviewer": "reviewer identifier",
  "reviewed_at": "2026-08-28T01:30:00+07:00",
  "dimensions": {
    "section_job": {"verdict": "pass", "evidence": "Opening and conclusion perform the approved job."},
    "audience_decision_value": {"verdict": "pass", "evidence": "..."},
    "evidence_payload": {"verdict": "pass", "evidence": "..."},
    "causal_logic": {"verdict": "pass", "evidence": "..."},
    "reader_facing_appropriateness": {"verdict": "pass", "evidence": "..."},
    "terminology_agency": {"verdict": "pass", "evidence": "..."},
    "source_fidelity": {"verdict": "pass", "evidence": "..."},
    "form_readability": {"verdict": "pass", "evidence": "..."},
    "altitude": {"verdict": "pass", "evidence": "..."},
    "headline_conclusion": {"verdict": "pass", "evidence": "..."},
    "findings_over_process": {"verdict": "pass", "evidence": "..."}
  },
  "findings": [
    {"severity": "minor", "location": "paragraph 3", "issue": "Local repetition", "status": "accepted", "disposition": "Flag for human review"}
  ],
  "mechanical_reviews": [
    {"message": "[PARENTHETICAL] exact linter message", "disposition": "Official term retained for traceability"}
  ],
  "verdict": "pass"
}
```

Allowed finding statuses are `resolved`, `accepted`, and `unresolved`.
Critical or major findings must be `resolved`. Mechanical review messages must
match the current linter output exactly; merge checks coverage.

