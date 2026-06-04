Here are three climate data platform personas based on real-world use cases from Asian and European climate initiatives. They reflect the actual language these professionals use and outline how their goals directly shape a platform's Information Architecture (IA).

## 1. The Policy Maker: "The Budget & Risk Balancer"

_(Inspired by regional planners working with Asian Development Bank and local governments on flood/drought management)_

- **Profile:** Somchai, Provincial Planner for Water and Environment.
    
- **Intent:** He needs to justify budget requests for infrastructure like flood walls or water storage over the next 5 to 10 years. He is not a climate scientist; he needs to know the exact impacts on his region and the economic costs.
    
- **Real-World Language:** He talks about "resource allocation," "budget cycles," "local adaptation," "risk zones," and "reducing farmer costs." He wants actionable evidence, not raw data points.
    
- **Impact on Information Architecture:**
    
    - **High-level Dashboards:** The platform must offer a landing page summarizing key trends (e.g., "Flood risk up 15% in the central basin").
        
    - **Regional Filters:** He must be able to click on his specific province and immediately see a curated summary.
        
    - **Exportable Reports:** Needs one-click PDF or chart exports to drop directly into policy briefs for his superiors.
        
    - **Plain Language Design:** Navigation should use simple terms like "Extreme Heat Risks" rather than technical variable codes.
        

## 2. The Scientist: "The Data Miner"

_(Inspired by researchers and modelers using the European Copernicus Climate Change Service)_

- **Profile:** Dr. Clara, Climate Data Analyst and Modeler.
    
- **Intent:** She builds models to track extreme weather patterns and attribute them to climate change. She needs massive amounts of historical weather data and future projections to test her research.
    
- **Real-World Language:** She cares about "data fusion," "spatial resolution," "quality control," "uncertainty margins," and "API limits." She expects the data to be perfectly clean, properly sourced, and transparent.
    
- **Impact on Information Architecture:**
    
    - **Direct API Access:** The site needs a dedicated developer portal where she can copy code snippets to pull data directly into her Python or R scripts.
        
    - **Deep Catalog Layout:** A structured data catalog with advanced filters for variables (temperature, wind, moisture), timeframes, and file formats (like NetCDF or CSV).
        
    - **Rich Metadata:** Every dataset must link directly to its source documentation, error margins, and collection methods.
        

## 3. The Co-Producer: "The Translator"

_(Inspired by agricultural tech developers in Southeast Asia and India building tools for smallholder farmers)_

- **Profile:** Priya, Agronomist and Digital Advisory Lead.
    
- **Intent:** She takes raw climate data and turns it into practical text alerts for local farmers (e.g., "Delay planting by two weeks due to late rains"). She bridges the gap between the complex global data and the farmer standing in the field.
    
- **Real-World Language:** She focuses on "usable tools," "local context," "co-creation," "advisory alerts," and "crop yield." She needs to merge the platform's climate data with her own local farming calendars.
    
- **Impact on Information Architecture:**
    
    - **Sector-Specific Portals:** The site should have distinct sections like "Agriculture & Food" or "Water Management," rather than just a massive list of files.
        
    - **Derived Datasets:** She needs the platform to offer pre-calculated, useful metrics (like "soil moisture index" or "consecutive dry days") so she does not have to compute them from raw temperature data.
        
    - **Case Studies & Forums:** A community or "Use Cases" section showing how other developers have successfully built local tools using the platform's data.
        

### IA Strategy Summary

|**Persona**|**Primary Goal**|**Navigation Path**|**Key IA Feature**|
|---|---|---|---|
|**Somchai (Planner)**|Budget & policy decisions|Summaries → Regional Maps → Reports|Executive dashboard, easy exports|
|**Dr. Clara (Scientist)**|Accurate modeling & research|Data Catalog → Variables → API / Download|Technical metadata, API portal|
|**Priya (Co-Producer)**|Building local advisory tools|Sector Use Cases → Derived Data → Integration|Sector-specific hubs, pre-calculated indices|
