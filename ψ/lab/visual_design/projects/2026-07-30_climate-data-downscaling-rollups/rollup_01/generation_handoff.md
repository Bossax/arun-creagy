# Stage 3 Generation & Layout Handoff — Roll-up 01
**Roll-up 01: ข้อมูลฉายภาพการเปลี่ยนแปลงสภาพภูมิอากาศ (Climate Projection Data & Scenarios)**

---

## 1. Handoff Purpose & Layout Authority

This document provides the complete layout, typesetting, and image-generation specification for **Roll-up 01**.
- **Layout Authority**: `rollup_01/layout_prototype.html`
- **Typesetting Copy Authority**: `rollup_01/layout_text_th.md`
- **Design System Authority**: `00_project/DESIGN.md`
- **Aspect Ratio**: `1:2.5` (80 cm x 200 cm physical vertical banner).

---

## 2. Shared Style-Lock Block (Copy Verbatim into Prompts)

```text
[STYLE-LOCK BLOCK]
Style: Modern educational editorial infographic, flat vector construction, bold simplified silhouettes, clean geometric forms, thick dark outlines (#0A369D), solid fills with subtle tonal shading.
Palette: Primary Egyptian Blue (#0A369D), Sapphire Sky (#4472CA), Glaucous (#5E7CE2), Baby Blue Ice (#92B4F4), Pale Sky (#CFDEE7), White (#FFFFFF).
Tone: Authoritative public information, clean, professional, scientific.
Avoid: Text, letters, numbers, photo-realism, 3D rendering, dark sci-fi glows, complex gradients, cluttered backgrounds, unverified maps.
Background: Isolated clean vector element on white or transparent background.
```

---

## 3. Vector Element Extraction Plan (Canva Reusable Assets)

### **Element 01 (`V01-01`): Scenario Branching Spectrum Diagram**
- **Canva Placement**: Zone A / Zone C (Projection uncertainty visual proof).
- **Element Role**: Show 3 diverging pathway arrows from a shared present-day origin branching into 3 socio-economic futures (SSP1-2.6 green route, SSP2-4.5 blue route, SSP5-8.5 dark blue route).
- **Prompt**:
  ```text
  [STYLE-LOCK BLOCK]
  Subject: Minimalist infographic vector diagram showing a single timeline arrow branching into three distinct socio-economic scenario pathways. The top branch is light blue with a leaf icon, the middle branch is sapphire blue with a steady line, and the bottom branch is dark egyptian blue with an upward curve. Flat vector, thick dark outlines (#0A369D), clean geometry, isolated on white background, no text, no numbers.
  ```

### **Element 02 (`V01-02`): 5 Sector Decision Badges**
- **Canva Placement**: Zone B (Decision application grid).
- **Element Role**: 5 distinct flat vector icons representing Thai public sector planning domains.
- **Prompts**:
  1. *Water Resources*:
     ```text
     [STYLE-LOCK BLOCK]
     Subject: Flat vector icon of a water drop and reservoir dam wall. Primary Egyptian Blue (#0A369D) outlines, Sapphire Sky (#4472CA) fill. Clean geometry, isolated on white background, no text.
     ```
  2. *Agriculture*:
     ```text
     [STYLE-LOCK BLOCK]
     Subject: Flat vector icon of a rice stalk and sun. Egyptian Blue (#0A369D) outlines, Glaucous (#5E7CE2) and Baby Blue Ice (#92B4F4) fills. Clean geometry, isolated on white background, no text.
     ```
  3. *Infrastructure*:
     ```text
     [STYLE-LOCK BLOCK]
     Subject: Flat vector icon of a city building silhouette and flood protection barrier. Egyptian Blue (#0A369D) outlines, Sapphire Sky (#4472CA) fill. Clean geometry, isolated on white background, no text.
     ```
  4. *Disaster Preparedness*:
     ```text
     [STYLE-LOCK BLOCK]
     Subject: Flat vector icon of a protection shield with a weather radar pulse. Egyptian Blue (#0A369D) outlines, Glaucous (#5E7CE2) fill. Clean geometry, isolated on white background, no text.
     ```
  5. *Policy & Investment*:
     ```text
     [STYLE-LOCK BLOCK]
     Subject: Flat vector icon of a bar chart ascending into a green adaptation leaf badge. Egyptian Blue (#0A369D) outlines, Sapphire Sky (#4472CA) fill. Clean geometry, isolated on white background, no text.
     ```

### **Element 03 (`V01-03`): Spatial Scale Grid Contrast Graphic**
- **Canva Placement**: Zone B (Scale gap illustration).
- **Element Role**: Illustrate a 100km coarse GCM grid box zoom-in transitioning into a high-resolution 5km fine grid box over a simplified Thailand map silhouette.
- **Prompt**:
  ```text
  [STYLE-LOCK BLOCK]
  Subject: Infographic vector diagram illustrating scale translation. A large coarse grid square (100km) zooming in through a magnifying lens into a dense high-resolution 5km grid mesh over a subtle Thailand map silhouette. Egyptian Blue (#0A369D) outlines, Sapphire Sky (#4472CA) and Pale Sky (#CFDEE7) fills, isolated on white background, no text, no coordinates.
  ```

---

## 4. Typesetting & Assembly Guide (Canva Instructions)

1. **Canvas Setup**: Set Canva custom canvas dimensions to `800px x 2000px` (or `80cm x 200cm` print dimensions at 300 DPI).
2. **Background & Safe Zones**:
   - Top Header Block (`0px` to `400px` height): Apply gradient fill from Egyptian Blue (`#0A369D`) to Deep Navy (`#062266`).
   - Body Section (`400px` to `1850px` height): Slate light surface (`#F1F5F9`).
   - Footer Bar (`1850px` to `2000px` height): Dark Slate (`#0F172A`).
3. **Text Copy**: Paste text line-by-line directly from `rollup_01/layout_text_th.md`.
4. **Font Styling**: Use `Sarabun` or `Kanit` for Thai text; `Outfit` for English badge chips (`CMIP6`, `GCM`, `SSP Scenarios`).
5. **Asset Placement**: Position extracted vector assets (`V01-01`, `V01-02`, `V01-03`) in their respective designated container slots.
