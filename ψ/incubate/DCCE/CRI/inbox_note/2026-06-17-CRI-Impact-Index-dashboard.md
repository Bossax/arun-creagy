
# Phase 1 - minimum system architecture decisions
## 1.1 decide how to host this web app for online access

The demo of CRI impact index metrics is shown in `C:\Users\sitth\OracleWorkspace\Arun_Creagy\ψ\incubate\DCCE\CRI\data_system\script\analysis_notebooks\cri_phase_1_demo.ipynb`. I want to build a web app that is hosted online for my client to use it. The traffic will be small, like 10 people looking at the same time. I want to host it without charge. 


## 1.2 decide what file type should all the metrics are prepared
The original data is in csv format. These files are read by the demo notebook. However, for a web app, should these original files be pre-processed and saved in a specific format that speeds up the responsiveness of the web app?

## 1.3 decide UI
to achieve the design template described in [[ψ/memory/resonance/coral-stay-DESIGN|coral-stay-DESIGN]], decide which framework to be used to build the interface. also consider the requirements in Phase 2: user interface requirement below.


# Phase 2: User Interface requirements

## 2.1 Methodology section
The web landing page is the methodology page. This page explain
1. the equations of the metrics and cri score
2. the description of the original datasets
	1. this lineage must not mention the file names or any system internal references
	2. it must state data owners of these datasets, their original forms, temporal coverage, description of the data etc.
	3. it discusses limitations of the datasets like the selection of affected household
	4. It must state what this web app includes

## 2.2 Time period selection
1. 2560-2567: this time period will show the plots of the average data between 2060 and 2567
2. 2567: this option shows the plots of the year-2567 data slice
This time period selection will be available
## 2.3 CRI tab
on top of the time period selection, there will be 
- 6 individual cri metrics: presented in grids
- CRI score: one single map
every plot has a table below it which shows the top 10 highest and lowest provinces

## 2.4 tambon level human impact tab
this tab a plow shows 2maps
- death
- affected household
of climate related hazards
The default plot is the whole country picture 
the plot is overlaid with provincial boundaries 

there is a dropdown menu to select a province to zoom in. 
the plot will have 2 tables below to show the top ten provinces, or tambon if it is a provincial zoom in plot, with highest deaths, and affected households (separate tables)

## 2.5 Heat mortality tab
basically sum of death and injured data columns of each province
The plot has a table below it which shows the top 10 highest and lowest provinces


