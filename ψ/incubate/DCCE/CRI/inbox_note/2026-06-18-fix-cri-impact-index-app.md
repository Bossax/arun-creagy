
There are several actions I noticed you did wrong
1. You worked in the old directory `ψ\incubate\DCCE\CRI\data_system\output\cri_impact_app`. This directory is for a previous implementation of the app. You should have not touched it. You must create a new folder to put all the data and artifacts of this new app in the same place and revert the changes you made on irrelevant files 
2. function `render_sticky_header`  in `app.py` has done an ugly and incomprehensible layout
	1. the restatement of "Stage 3 landing page — methodology first, with the shell preserved for later analytics". This is like you talk to yourself. There are  other texts that you kinda mummer to yourself, exposing internal logic to the user interface.
	2. the 4 unclickable chips  of `SECTION_KEYS`. remove them
	3. "Global time period" does not make any sense. It should be "time period option
	4. what is the unclickable dropdown object `cri-selector-card`? remove it. it is not working and unnecessary.
	
3. In fact, the time period selection should be below the 4 tab chips. However, f possible, the time period selection shall be plot-wise. 
4. Rewrite or remove all the internal logic texts from the user interface. The examples are
	1. "## Methodology landing page"
	2. "This page explains the client-facing methodology in plain language. It summarizes what the index measures, where the data comes from, how the score is interpreted, and where the limits of the current release begin."
5. The tables can just show 3 columns; rank, name in Thai, and value
6. For each `rednder_*_page_function`, remove the page-wide callout block that gives overview information of the tab and also the 3 callout cards below.
7. make the description of each tab richer
8. remove the banner at the top of the page
9. since most tab have even numbers of maps, I want to make a pair of maps at the same level on the page. Each plot area takes half of the window width space. 
10. is it possible to make each plot has a toggle button to switch the time period options? if not, these 