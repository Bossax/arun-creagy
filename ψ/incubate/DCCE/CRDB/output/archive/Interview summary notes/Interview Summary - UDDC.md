**Date:** 5/3/2569 (March 5, 2026) 
**Interviewee Name/Title:** Deputy Director Adisak **Department:** Not explicitly specified (Executive level)
**Agency:** Urban Design and Development Center (UDDC)

### 1. Role and Responsibility of the Agency

- **Key duty and roles:** UDDC operates as an academic and practical implementation institute focusing on urban design, resilience building, and climate adaptation planning at the city and local levels.
    
- **Associated legal frameworks:** While not a regulatory body, they act as a core consortium partner working directly under National Steering Committees and Provincial Committees (chaired by provincial governors) to integrate climate adaptation into official provincial and local strategic plans.
    

### 2. Highlighted Key Projects

- **Urban Resilience Building and Nature-based Solutions (URBAN):**
    
    - _Status & Scope:_ Active. A 5-year project (2024-2028 / B.E. 2567-2571) funded by the International Climate Initiative (IKI) Germany.
        
    - _Inter-agency Consortium:_ Executed by a 6-agency consortium including the Department of Water Resources (DWR) as the political partner, IUCN (lead), ADPC, UN-Habitat, GIZ, and UDDC. Pilot areas are Chiang Rai and Surat Thani.
        
    - _Outputs & Integration:_ The project produces local climate risk/vulnerability assessments, spatial strategic plans, local wetland management plans, and local disaster prevention plans.
        
    - _Future Lifecycle:_ At the project's conclusion, all generated spatial data, models, and policy recommendations will be hosted on a central data platform (tentatively named something like "Urban Resilience Thailand") to feed back into national policy.
        

### 3. Current Workflow & Data Usage

- **Context and Hazard Scope:** The primary hazards modeled include floods, landslides/mudslides, sea-level rise/storm surges (specifically for Surat Thani), and droughts.
    
- **Data Sources:** They pull baseline land-use data from the Land Development Department (LDD) and hydrological/climate data from DWR, Royal Irrigation Department (RID), Office of the National Water Resources (ONWR), Thai Meteorological Department (TMD), and Hydro-Informatics Institute (HII / สสน.).
    
- **Modeling Techniques and Granularity:** Because national models lack local specificity, the project generates its own highly granular models.
    
    - _City-Level:_ A technical working group (ADPC, TMD, DDPM) runs SSP3 and SSP5 climate scenarios downscaled to the city level using 1-meter Digital Elevation Models (DEM) to map future flood inundation.
        
    - _Project/Intervention-Level:_ For designing specific Nature-based Solutions (NbS), they fly drones to capture 20-centimeter resolution data, creating detailed Digital Surface/Terrain Models (DSM/DTM) that identify tree canopies and specific biodiversity layers.
        
    - _Urban InVest Model:_ They use this external service model to evaluate the retention and drainage capacity of urban ecosystems.
        
- **Vulnerability & Cascading Impacts:** UDDC maps "double vulnerability"—intersecting physical climate hazard maps with socio-economic data to identify populations that become newly vulnerable due to their physical location (e.g., living in a flood path), even if they do not meet the traditional Ministry of Social Development and Human Security (MSDHS) poverty definitions.
    

### 4. Climate Data Needs & Gaps

- **Projections and Baselines:** Downscaling drought projections to the local level is exceedingly difficult compared to flood modeling because the baseline granular data for groundwater and water flow is practically non-existent or unrefined.
    
- **Standardizations:** There is massive data fragmentation. Thailand has over 60 agencies dealing with water, forcing researchers to hunt for station data across RID, ONWR, and HII platforms, which often contain disjointed station sizes and records.
    
- **Severe Budgeting & Policy Roadblocks:** * _The "Wait for Disaster" Budgeting Loop:_ Local governments cannot secure budgets for _proactive_ climate prevention or adaptation. The Bureau of the Budget and the State Audit Office (สตง.) typically only approve funds for post-disaster relief once the damage is physically visible.
    
    - _NAP Disconnect:_ The National Adaptation Plan (NAP) is too broad and top-down. Except for Bangkok, provinces lack "Local NAPs," making it incredibly difficult for local municipalities (เทศบาล) to align their local functional budgets with national climate goals.
        
- **Specific Requests for DCCE:** * Establish a "Single Source of Truth" data portal that unifies fragmented water data and standardizes baseline models (e.g., officially sanctioning which SSP models, Heat Indexes, or PM2.5 metrics the country should use).
    
    - Provide authoritative DCCE risk maps that local governments can use as definitive proof to justify proactive adaptation budgets to the Bureau of the Budget.
        
    - Design the platform with two tiers: raw, processable data (like CSVs/APIs) for researchers, and simplified dashboards for local city executives.
        

### 5. Next Steps & CRDB Integration

- **Map to Implementation Plan:** UDDC's struggle with over 60 fragmented water agencies and the need for processable raw data vs. executive dashboards directly validates the WP4 Data Catalog's tiered architecture and the urgency for a centralized data inventory.
    
- **Seed Use Cases for WP3 Conceptual Data Model (CDM):** * _Scenario 1:_ "Applying 1-meter DEM downscaled flood inundation models to design 20-cm resolution Nature-based Solutions (NbS) interventions in local wetlands.".
    
    - _Scenario 2:_ "Overlaying localized physical climate hazards with socio-economic status to redefine 'Double Vulnerability' for proactive local budget allocation.".
        
- **Planned Participation:** UDDC confirmed their willingness to participate in the upcoming post-Songkran April workshop to exchange knowledge on data application use cases with other data supply chain actors.