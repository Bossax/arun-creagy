# Panel 02 Visual Plan: The Belém Adaptation Indicators Catalog (Hybrid Layout)

## 1. Composition & Reading Direction
* **Format & Size**: 60 × 160 cm vertical roll-up banner.
* **Dominant Reading Path**: Two-column visual grid. Left column covers the Thematic sectors (Stream A), and the right column covers the Dimensional policy stages (Stream B). The eye flows down each column, ending at the central QR Code Action Card at the bottom.
* **Layout Grid (4 Horizontal/Vertical Zones)**:
  ```mermaid
  graph TD
      Header[Zone 1: Header - Catalog Intro] --> Columns[Zone 2 & 3: Dual Column Grid]
      Columns --> LeftCol[Left Column: 7 Thematic Cards 9a-g]
      Columns --> RightCol[Right Column: 4 Dimensional Cards 10a-d]
      LeftCol --> QRCard[Zone 4: Bottom - Styled QR Code Action Block]
      RightCol --> QRCard
  ```

---

## 2. Visual Elements & Content Mapping

### Zone 1: Header (Top 15% height)
* **Visual Role**: Contextualize the indicators and guide usage.
* **Elements**:
  - Title: Bilingual title matching Panel 1 typography in Sovereign Dark (`#0b2e25`).
  - Intro card: Brief explanation of the 59 indicators in DCCE Forest Teal (`#105040`).

### Zone 2 & 3: Dual Column Summary Cards (Middle 65% height)
* **Visual Role**: Summarize what each target theme measures and provide sample indicators.
* **Left Column: Thematic Outcome Cards (7 Cards)**:
  - 7 distinct cards corresponding to Target 9(a) through 9(g).
  - Each card contains:
    - **Header**: Target code (e.g. `Target 9(a)`) + Sector name (EN/TH) in Sovereign Dark.
    - **Summary Text**: Concise description of what the sector measures.
    - **Sample indicator block**: Colored pill showing 1 key indicator example (code + EN/TH title) in Marine Jade (`#14856b`).
* **Right Column: Dimensional Process Cards (4 Cards)**:
  - 4 distinct cards corresponding to Target 10(a) through 10(d).
  - Matches the structure of the thematic cards (Target header, summary text, and sample indicator pill).
* **Styling & Color-Coding (DCCE Palette Tints)**:
  - Cards use a soft, desaturated tint of the core palette:
    - *Thematic cards (Water, Food, Health, Ecosystems)*: Soft teal background tint (98% lightness of core color) and Sage Gray (`#789890`) thin outline.
    - *Dimensional cards (Assessment, Planning, Implementation, MEL)*: Light slate background tint and Sage Gray (`#789890`) thin outline.

### Zone 4: QR Code Action Block (Bottom 20% height)
* **Visual Role**: Provide immediate digital access to the full, un-truncated database.
* **Elements**:
  - Centered visual card spanning both columns with a light Sage Gray background fill.
  - Left side of card: Large, high-contrast, vector-styled QR Code (mocking the URL of the project's [evidence_map.md](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/lab/visual_design/projects/2026-07-22_gga-indicators-rollups/00_project/evidence_map.md)).
  - Right side of card: Bold bilingual call-to-action in DCCE Forest Teal (`#105040`) ("Scan to access the full 59-indicator reference catalog / สแกนเพื่อเข้าถึงสารบัญตัวชี้วัดฉบับเต็ม").

---

## 3. Colors & Typography (Design System Tokens)
* **Palette & Contrast**:
  - Inherits the design tokens (DCCE Forest Teal, Sovereign Dark, Mint White, Marine Jade, Sage Gray) defined in [00_project/design.md](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/lab/visual_design/projects/2026-07-22_gga-indicators-rollups/00_project/design.md).
  - Uses very soft, desaturated HSL light-tints of the core color for card backgrounds to guarantee that the body text remains highly readable.
* **Typography**:
  - Matches Panel 1 (Inter or Roboto). Title sizes: 72pt. Summary card headers: 28pt. Card body and sample text: 16–18pt.

---

## 4. Accessibility, Risk & Verification
* **Density Control**: By replacing the raw text of all 59 indicators with concise summaries and sample pills, we keep the total text count per card under 40 words, preventing overcrowding.
* **QR Code Scannability**: Ensure the QR code has a quiet zone (white border) and high contrast (black on white) for easy scanning with mobile devices at 1 m distance.
* **Editable Content**: Keep all card headers, summary text, and sample indicators fully editable in vector layers outside the graphic backgrounds.
