# Raw Extraction: ART06_Species_Protected_Areas
- **Source**: 6-Vulnerability to climate change of species in protected areas in Thailand
- **Date Extracted**: 2026-06-23

```json
{
  "metadata": {
    "source_filename": "6-Vulnerability to climate change of species in protected areas in Thailand",
    "extracted_at": "2026-06-23T08:59:31Z",
    "notebook_id": "crdb-tor-5-5-climate-risk-arti"
  },
  "core_hypothesis": "Climate change will substantially alter species richness, suitable habitat, and conservation risk across Thailand's protected areas, and current protected-area configurations alone may be insufficient without stronger ecological connectivity and adaptive management.",
  "sections_outline": [
    "Results",
    "Data completeness and representativeness",
    "Changes in the availability of suitable habitat for individual species",
    "Impacts on species in protected areas",
    "Projected changes in conservation status of species",
    "Discussion",
    "Management recommendations",
    "Methods",
    "Study area",
    "Environmental data",
    "Species occurrence data",
    "Species distribution modeling",
    "Assessment of climate change impacts",
    "Data availability",
    "References",
    "Acknowledgements",
    "Author contributions"
  ],
  "tables_and_figures": [
    {
      "id": "Table 1",
      "title": "Numbers of species and location records used in the analyses for each taxonomic group from localities below and above 250 m above sea-level, and the percentage of the land area in each altitudinal belt protected.",
      "focus": "Spatial coverage and representativeness of biodiversity records across taxa, altitude bands, and protected land share."
    },
    {
      "id": "Table 2",
      "title": "Estimated maximum species richness (per km2) and the total area with the highest richness level for each region of Thailand for the present and projected for 2070, using three earth system models and two RCPs.",
      "focus": "Current and projected regional species richness patterns under multiple climate models and emissions scenarios."
    },
    {
      "id": "Table 3",
      "title": "The extent of suitable habitat for species within protected areas in Thailand currently and projected for 2070 for five taxa using three earth system models and two RCPs.",
      "focus": "Current and future suitable habitat inside protected areas across five taxonomic groups."
    },
    {
      "id": "Table 4",
      "title": "Current and projected 2070 conservation statuses of the modeled species.",
      "focus": "Current versus projected future conservation-status distributions across IUCN-style threat categories."
    },
    {
      "id": "Figure 1",
      "title": "Thailand: location and protected area system, showing the protected area complexes used for management (DNP 2019).",
      "focus": "Geographic layout of Thailand's protected area system and management complexes."
    },
    {
      "id": "Figure 2",
      "title": "Maps of (a) the six regions of Thailand used in the text, and (b–f) species occurrence locations used in the analyses for each major taxon.",
      "focus": "Regional geography and spatial distribution of species occurrence records by taxon."
    },
    {
      "id": "Figure 3",
      "title": "Spatial patterns of predicted species richness levels for each major taxon under current conditions.",
      "focus": "Baseline spatial distribution of species richness across major taxa."
    },
    {
      "id": "Figure 4",
      "title": "Projected changes in suitable habitat by 2070 (a) without and (b) with dispersal to newly suitable habitat for species in five taxa with three earth system models and two RCPs.",
      "focus": "Projected habitat loss, stability, and expansion by taxon under different dispersal assumptions and climate scenarios."
    }
  ],
  "extracted_evidence": [
    {
      "evidence_id": "E01",
      "topic": "Study scope and biodiversity-climate risk framing",
      "description": "The paper evaluates how projected climate change may alter species richness, habitat suitability, and conservation risk for multiple taxa in Thailand's protected areas, with emphasis on adequacy of current conservation configurations.",
      "metrics_mentioned": ["2070", "RCP2.6", "RCP8.5", "three earth system models", "protected areas", "species richness", "suitable habitat", "conservation status"],
      "citations": ["Core Research Hypothesis / Major Research Questions", "Methods", "Discussion"]
    },
    {
      "evidence_id": "E02",
      "topic": "Data completeness and representativeness bias",
      "description": "The analysis is constrained by uneven taxonomic and spatial coverage, with records concentrated in protected areas and poorer coverage for many lowland, small-bodied, and difficult-to-detect species, especially among amphibians, reptiles, bats, insectivores, rodents, and treeshrews.",
      "metrics_mentioned": ["minimum 10 unique occurrence records", "12% of reptiles included", "16% of amphibians included", "<250 m", ">250 m"],
      "citations": ["Data completeness and representativeness", "Table 1", "Figure 2", "Results: Data completeness and representativeness", "Introduction"]
    },
    {
      "evidence_id": "E03",
      "topic": "Environmental and modeling architecture",
      "description": "Species distribution modeling combines topography, soil pH, vegetation, and eight bioclimatic variables with three Earth System Models under RCP2.6 and RCP8.5, using Maxent outputs converted to binary presence-absence maps and evaluated with the continuous Boyce Index.",
      "metrics_mentioned": ["altitude", "slope", "aspect", "soil pH", "8 bioclimatic variables", "CNRM-CM5", "GFDL-CM3", "HadGEM2-ES", "10% cumulative logistic threshold", "continuous Boyce Index >0.5"],
      "citations": ["Environmental data", "Species distribution modeling", "Assessment of climate change impacts", "Methods"]
    },
    {
      "evidence_id": "E04",
      "topic": "Projected species richness change by region and taxon",
      "description": "Maximum species richness is projected to decline for all taxa overall, with the sharpest losses for mammals and broad declines for birds and plants, especially under RCP8.5, while amphibians and reptiles show projected increases in some model- and region-dependent cases.",
      "metrics_mentioned": ["1x1 km grid cell", "31 amphibians", "49 reptiles", "60 mammals", "440 birds", "458 plants", "North", "Northeast", "Central", "East", "South", "Western", "RCP2.6", "RCP8.5"],
      "citations": ["Changes in projected species richness under climate change", "Table 2", "Figure 3", "Step 2B"]
    },
    {
      "evidence_id": "E05",
      "topic": "Habitat suitability change under dispersal assumptions",
      "description": "Projected habitat outcomes differ strongly by dispersal assumption: under no dispersal, many mammals, birds, and plants lose large shares of suitable habitat, especially under RCP8.5, while under unlimited dispersal amphibians and reptiles more often show net expansion and mammals remain predominantly contracting.",
      "metrics_mentioned": ["no dispersal", "unlimited dispersal", "mammals 1–11% total habitat loss", "mammals 26–65% lose >50%", "birds 1–8% total habitat loss", "plants 1–5% total habitat loss", "reptiles 0% total habitat loss", "amphibians 0% total habitat loss"],
      "citations": ["Changes in the availability of suitable habitat for individual species", "Figure 4", "Step 2C"]
    },
    {
      "evidence_id": "E06",
      "topic": "Protected area performance under climate change",
      "description": "Current protected areas contain unequal shares of suitable habitat across taxa and are projected to become less effective for mammals, birds, and plants by 2070, while amphibians and reptiles show broader increases inside many protected areas and complexes.",
      "metrics_mentioned": ["mammals 43%", "plants 37%", "birds 37% or 26%", "reptiles 22%", "amphibians 17%", "mammals inside PAs -26% to -38% under RCP8.5", "59–82% of PAs decline under RCP2.6", "69–77% of PAs decline under RCP8.5"],
      "citations": ["Impacts on species in protected areas", "Table 3", "Step 2D", "Figure 1"]
    },
    {
      "evidence_id": "E07",
      "topic": "Conservation status deterioration by 2070",
      "description": "Climate-driven habitat loss substantially increases projected threat levels by 2070, with overall threatened species rising from 11% at present to 35% under RCP2.6 and 54% under RCP8.5, including projected extinctions concentrated in mammals, birds, and plants under high emissions.",
      "metrics_mentioned": ["11% current threatened", "35% under RCP2.6", "54% under RCP8.5", "11 projected extinctions under RCP8.5", "1 primate", "6 bird species", "4 plant species"],
      "citations": ["Projected changes in conservation status of species", "Table 4", "Step 2E"]
    },
    {
      "evidence_id": "E08",
      "topic": "Adaptation and management recommendations",
      "description": "The authors recommend strengthening protected area complexes, ecological corridors, south-to-north and low-to-high altitude connectivity, assisted migration, and long-term monitoring through permanent altitudinal transects to help species respond to climate change.",
      "metrics_mentioned": ["17 forest complexes", "three marine complexes", "south-to-north connectivity", "low-to-high altitude connectivity", "multiple decades"],
      "citations": ["Management recommendations", "Figure 1", "Step 2F"]
    }
  ],
  "limitations_and_uncertainties": [
    {
      "issue": "Species distribution models are sensitive to actual niche truncation caused by habitat loss and hunting, and to apparent niche truncation caused by data limitations.",
      "citation": "Abstract"
    },
    {
      "issue": "Niche truncation may overestimate vulnerability for some mammal and plant species, while data limitations may underestimate threats to forest-dependent amphibians and reptiles.",
      "citation": "Abstract"
    },
    {
      "issue": "Accurate locality data for most taxa other than birds is very incomplete and is concentrated mainly in protected areas.",
      "citation": "Introduction"
    },
    {
      "issue": "Vertebrate data coverage reflects detectability bias, with many smaller species inadequately surveyed; few bats, no insectivores, and incomplete rodent and treeshrew coverage are represented.",
      "citation": "Results: Data completeness and representativeness"
    },
    {
      "issue": "Projected responses for some individual species may reflect data limitations more than true climate-change vulnerability.",
      "citation": "Results: Data completeness and representativeness"
    },
    {
      "issue": "Correlative SDMs assume that current location data represents the full climate space in which each species can live as part of a community.",
      "citation": "Discussion"
    },
    {
      "issue": "Bias toward existing protected areas and exclusion of neighboring-country records from Myanmar and Laos create artificial cut-offs that may influence model projections.",
      "citation": "Discussion"
    },
    {
      "issue": "Dispersal ability is highly uncertain, so the study brackets outcomes using two extreme assumptions: no dispersal and unlimited dispersal.",
      "citation": "Discussion"
    },
    {
      "issue": "The models omit important processes including fire regime, direct ecophysiological effects of rising carbon dioxide, rare climatic extremes, and secondary effects on predator-prey relations and mutualists.",
      "citation": "Discussion"
    },
    {
      "issue": "Future projections assume temperature and precipitation change while topography, soil, and vegetation remain stable, so the analysis represents the impacts of climate alone.",
      "citation": "Methods"
    },
    {
      "issue": "Soil phosphorus data of useful accuracy and spatial resolution is unavailable for Thailand, and the mechanistic basis by which tropical climates filter species distributions is still weakly understood.",
      "citation": "Methods"
    },
    {
      "issue": "Climate-only extinction risk assessments omit non-climatic factors and unpredictable interactions, so they should not be used in isolation for conservation planning.",
      "citation": "Methods"
    }
  ]
}
```
