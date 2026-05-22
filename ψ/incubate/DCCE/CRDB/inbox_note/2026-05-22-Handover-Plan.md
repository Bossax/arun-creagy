This diagram illustrates the workflow and responsibilities following the handover of project deliverables, moving from design to actual implementation. It maps specific project deliverables to key roles and actions during two main phases: **Requirement Analysis** and **Design**.

Here is a detailed breakdown of the diagram:

### 1. Project Deliverables (สิ่งที่ ส่งมอบในโครงการ CRDB)

The left side features a dark blue stacked block listing the 6 main deliverables being handed over:

1. Dataset and Information Product Inventories
    
2. Business Requirements – Use Case Inventory
    
3. Conceptual Data Model
    
4. Logical Data Model for Loss and Damage
    
5. Data Governance Framework
    
6. Sitemap
    

### 2. Requirement Analysis Phase (DCCE Check Points)

The middle light-green column represents the **Requirement Analysis** phase, which acts as checkpoints managed by specific roles:

- **Product Owner:** Uses deliverables 1 and 2 to define user requirements for the core products and services.
    
- **Data Owner:** Uses deliverable 5 to certify and approve roles and responsibilities.
    
- **Product Owner:** Uses deliverable 6 to lock in the initial website specifications.
    

### 3. Design Phase (การออกแบบเชิงระบบ)

The light-blue column on the right outlines the **Design** phase, where specific specialists take action based on the analyzed requirements:

- **UX/UI Designer:** Designs the actual products and services. This role collaborates directly with the Product Owner's defined requirements and the Data Architect.
    
- **Data Architect:** Handles the technical data structure. They use deliverables 1, 3, and 4 to design the physical schema, design the data system, and define data ingestion formats.
    
- **Subject Matter Expert (SME):** Takes the locked website specifications from the Product Owner to develop the actual content for the website.
    

### 4. Key Persona Icons

At the bottom, the diagram defines three categories of stakeholders involved in this process, represented by distinct icons:

- **Climate Expert** (Scientist icon)
    
- **IT Specialist** (Person with laptop icon, seen on UX/UI and Data Architect roles)
    
- **Policy Maker** (Green circular logo, seen on Product Owner, Data Owner, and SME roles)


---

This second diagram maps the exact same 6 project deliverables but focuses on the next sequential transition: moving from the **Design** phase into the actual **Implementation** phase.

Here is the detailed breakdown of how the responsibilities shift in this part of the workflow:

### 1. Design Phase (การออกแบบเชิงระบบ)

In this middle light-blue column, the technical and subject matter experts collaborate to finalize system blueprints based on the deliverables:

- **UX/UI Designer:** Designs the products and services (connected from Deliverables 1 & 2), passing their structural layouts directly down to the Data Architect.
    
- **Subject Matter Expert (Climate Expert/Policy Maker):** Develops the processing logic (พัฒนาตรรกะการประมวลผล). They work closely with the UX/UI designs and technical specs.
    
- **Data Steward (Climate Expert/Policy Maker):** Certifies data quality and data availability (รับรองคุณภาพและการมีอยู่ของข้อมูล), feeding this validation straight into the system architecture.
    
- **Data Owner (Policy Maker):** Approves the content format (รับรองรูปแบบเนื้อหา) originating from the website content (เนื้อหาเว็บไซต์).
    
- **Data Architect:** Acts as the central hub in this phase. They take input from the UX/UI designs, Data Stewards, and Data Owners to define the overall big picture of the data system (กำหนดภาพรวมของระบบข้อมูล).
    

### 2. Implementation Phase (สู่การสร้างจริง)

The purple column on the far right represents the technical build, where the finalized blueprints from the Design phase are handed over to the development team:

- **Data Engineer:** Takes the system overview from the Data Architect to design and build the actual data pipelines (ออกแบบ data pipeline).
    
- **Software Engineer:** Uses the architecture and UX/UI blueprints to develop the core system (พัฒนาระบบ).
    

### Key Differences from the First Diagram

While the first diagram focused on **Requirement Analysis $\rightarrow$ Design** (setting up specs and physical schemas), this second diagram focuses on **Design $\rightarrow$ Implementation**.

It introduces specific technical execution roles like the **Data Steward** (to ensure data quality before building), the **Data Engineer** (for pipelines), and the **Software Engineer** (for system coding), while shifting the Data Architect's role from writing individual schemas to defining the macro system architecture.