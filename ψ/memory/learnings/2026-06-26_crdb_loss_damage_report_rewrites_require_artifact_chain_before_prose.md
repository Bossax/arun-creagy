# Learning: CRDB loss-and-damage report rewrites require artifact-chain hardening before prose drafting

## Pattern

For expert-facing Thai report sections that combine institutional workflow, international methodology, and target data architecture, direct prose drafting is too early unless the supporting artifact chain is already hardened. The reliable sequence is: raw evidence capture, methodology distillation, comparative analysis, target technical design, source-availability review, gap analysis, execution plan, outline approval, and only then full prose rewrite.

## Why it matters

When the prose is drafted before the artifact chain is complete, the draft tends to borrow prestige from language rather than from evidence. This creates several recurring failures: inflated claims, confused boundaries between operational reporting and analytical assessment, conflation of compensation with loss, and vague architecture explanations that sound persuasive but collapse under audit.

## What worked

- Build methodology artifacts first, such as [`DaLA_methodology_report.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/DaLA_methodology_report.md:1), [`DDPM_PDNA_methodology_report.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/DDPM_PDNA_methodology_report.md:1), and [`comparative_analysis_DaLA_DesInventar_PDNA.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/comparative_analysis_DaLA_DesInventar_PDNA.md:1).
- Translate those findings into a target architecture before final drafting via [`Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:1).
- Test the design against actual source availability using [`DDPM_data_review_from_CRI_project.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/DDPM_data_review_from_CRI_project.md:1) and [`DDPM_CRI_to_CRDB_MVD_gap_analysis.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/DDPM_CRI_to_CRDB_MVD_gap_analysis.md:1).
- Use an outline-stop control before drafting final prose.

## General rule

For high-stakes report rewrites, do not ask “Can I write this section now?” until you can answer a harder question first: “Do I already have a fully connected evidence-to-design chain strong enough that the prose is merely the last translation step?”

If the answer is no, continue building artifacts instead of drafting.
