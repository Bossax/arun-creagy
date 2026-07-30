# Design System — Climate Data Downscaling Roll-ups
**Project Design System Specification & Visual Style Lock**

---

## 1. Core Visual Identity & Style Lock

### 1.1 Reference Alignment (`reference.jpg`)
The visual language captures an authoritative public-information infographic style:
- **Construction**: Flat vector construction with bold, simplified silhouettes and clean geometric forms.
- **Line & Stroke**: Thick dark outlines (`#0A369D`) providing crisp separation between visual elements.
- **Fills & Shading**: Solid fills with subtle, restrained tonal shading for slight dimensional layering.
- **Character**: Informative, clean, public-sector appropriate, avoid generic decorative clutter or sci-fi glows.

---

## 2. Color Palette & Design Tokens

### 2.1 Approved Brand Palette

| Token Name | Hex Code | HSL Value | Usage Role |
|---|---|---|---|
| `--color-primary-dark` (Egyptian Blue) | `#0A369D` | `hsl(222, 88%, 33%)` | Primary headers, heavy stroke lines, primary contrast cards. |
| `--color-primary-mid` (Sapphire Sky) | `#4472CA` | `hsl(220, 56%, 53%)` | Secondary headers, section dividers, active badge fills. |
| `--color-accent-blue` (Glaucous) | `#5E7CE2` | `hsl(227, 68%, 63%)` | Accent highlights, key metrics, directional flow arrows. |
| `--color-blue-light` (Baby Blue Ice) | `#92B4F4` | `hsl(219, 83%, 76%)` | Container backgrounds, table headers, secondary callout fills. |
| `--color-blue-soft` (Pale Sky) | `#CFDEE7` | `hsl(204, 35%, 86%)` | Panel section backgrounds, subtle grid lines, card borders. |

### 2.2 Neutral & Surface Tokens

| Token Name | Hex Code | Usage Role |
|---|---|---|
| `--color-surface-white` | `#FFFFFF` | Main card backgrounds, high-contrast readable text containers. |
| `--color-text-main` | `#0F172A` | Primary body text (Slate 900) for maximum legibility on print. |
| `--color-text-muted` | `#475569` | Secondary text, captions, metadata tags (Slate 600). |
| `--color-border-subtle` | `#CBD5E1` | Dividers, card borders, subtle grid lines. |

---

## 3. Typography System

### 3.1 Font Family Stack
- **Thai Primary**: `'Sarabun'`, `'Kanit'`, or `'Noto Sans Thai'`, sans-serif.
- **English / Technical Terms**: `'Outfit'`, `'Inter'`, or `'Roboto'`, sans-serif.

### 3.2 Type Scale (Scalable for Physical Banner Proportions)

| Scale Level | Font Size (CSS rem / pt) | Line Height | Font Weight | Applied Elements |
|---|---|---|---|---|
| `display-1` | `3.5rem` (~56pt) | `1.1` | `bold` (700) | Banner Main Title |
| `heading-1` | `2.25rem` (~36pt) | `1.2` | `bold` (700) | Major Section Headers |
| `heading-2` | `1.5rem` (~24pt) | `1.3` | `semi-bold` (600) | Card Sub-headers, Product Names |
| `body-large` | `1.125rem` (~18pt) | `1.5` | `regular` (400) | Lead Paragraphs, Insight Summary |
| `body-main` | `0.95rem` (~15pt) | `1.5` | `regular` (400) | Section Body Copy, Table Cells |
| `caption` | `0.8rem` (~13pt) | `1.4` | `medium` (500) | Technical Badges, Source Anchors |

---

## 4. Grid Architecture & Layout System

### 4.1 Banner Dimensions & Safe Zones
- **Aspect Ratio**: `1:2.5` (Standard physical roll-up banner 80 cm x 200 cm).
- **Top Hardware Safe Zone**: Top 10% (Reserved for DCCE Logo & Series Title).
- **Bottom Hardware Safe Zone**: Bottom 8% (Reserved for DCCE Partner Marks & Source Notes).
- **Side Margins**: `5%` left/right padding to prevent banner edge clipping.

### 4.2 Module Layout Stack
Each banner is structured into **3 vertical reading zones**:
1. **Zone A (Top)**: Hero Statement & Projections vs. Forecasts / Scale Gap.
2. **Zone B (Middle)**: Core Mechanism Diagram / Comparison Matrix (Downscaling / Products).
3. **Zone C (Bottom)**: 6-Field Insight Card & 5-Element Decision Framework.

---

## 5. Component Library Standards

### 5.1 Technical Badges & Chips
- **Container**: Border-radius `6px`, padding `0.25rem 0.75rem`.
- **Style**: Egyptian Blue border (`#0A369D`), Pale Sky background (`#CFDEE7`), bold text.

### 5.2 Insight Card Container
- **Container**: White surface (`#FFFFFF`), 2px solid border (`#4472CA`), border-radius `12px`.
- **Shadow**: `0 10px 25px -5px rgba(10, 54, 157, 0.1)`.
- **Header Strip**: Egyptian Blue background (`#0A369D`), white bold text.

### 5.3 Comparison Tables
- **Header Row**: Baby Blue Ice (`#92B4F4`), dark text (`#0F172A`), bold centered text.
- **Alternating Rows**: White (`#FFFFFF`) and Pale Sky (`#CFDEE7`).
- **Cell Borders**: 1px solid `#CBD5E1`.

---

## 6. Canva Asset Extraction Rules (Stage 5 Prep)

When generating individual vector iconography elements for Canva assembly:
1. **Style Lock Prompt Block**: Copy exact palette tokens (`#0A369D`, `#4472CA`) and style description ("Flat vector infographic, bold outlines, solid fills, clean geometry, isolated on transparent background").
2. **Prohibited Elements**: No text, no pseudo-data numbers, no synthetic map coordinates.
