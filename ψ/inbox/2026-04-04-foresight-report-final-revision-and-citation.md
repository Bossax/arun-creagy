The previous citation system is too complicated and does not actually work.

I want the report to properly cites data sources (inline citation and bibliography)

The sources  are in [[ψ/lab/foresight-report-writing/artifacts/source]]

The files are either deep research reports or project synthesis (through meetings, brainstorming, and workshop), or actual pdf files.

The deep research reports are created by Gemini deep research, which cites sources using superscripted numbers. When converted to md files, these numbers become normal text following the claims in the report. The reports always have a "Work Cited" section where the numbered list of sources is.

The previous drafting process made tracing the actual reference in a deep research report of the claim in the foresight report tricky. 

I am thinking that, first, we need to create mapping between the claims in the foresight report and the metadata of the deep research report. When matched deep research reports are determined, the actual source(s) that supports a specific claim can be traced more easily.

My proposal is

1. create a metadata database of the deep research reports, project synthesis, and direct sources as a citation library. 
2. the citation will be executed alongside human supervision
	1. you analyze the claims contained in a section
	2. you shortlist artifacts that could have supporting evidence of each claim
	3. you go through the artifacts in the short list one by one to identify the actual sources of each artifact that could support the claim
	4. you present the result to human. human review these sources and approve 
	5. you insert in line citations in the report draft and register the artifacts in report bibliography
3. Repeat the process throughout all sub-sections and chapters of the report