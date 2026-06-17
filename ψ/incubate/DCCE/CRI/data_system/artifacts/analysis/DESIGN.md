# CRI Web App — Canonical Design Template

## Purpose

This file is the canonical design template for the CRI web app.

It adapts the warmth, friendliness, and rounded hospitality feel of [`coral-stay-DESIGN.md`](../../../../../../memory/design/coral-stay-DESIGN.md:1) into a climate-risk analytics product.

This is a **starter design specification**, not a final visual lock. It is intended to be stable enough for implementation while remaining easy to iterate.

---

## 1. Design intent

The app should feel:

- warm, trustworthy, and approachable
- analytical without feeling bureaucratic
- map-first, but not cold or overly technical
- polished enough for client demonstration
- lightweight enough to support dense information layouts

The Coral Stay design language contributes:

- coral-led primary actions
- warm dark text
- soft surfaces
- rounded cards and controls
- spacious layout rhythm

The CRI app adaptation adds:

- stronger support for map panels and metric grids
- clearer hierarchy for methodology vs analytics
- more restrained use of decorative elements
- more consistent table and legend treatments

---

## 2. Design principles

1. **Warm authority**
   - The interface should feel credible and data-driven without becoming harsh or institutional.

2. **Map first, explanation close**
   - Every visualization should have nearby legend, title, and ranking support.

3. **Readable density**
   - The interface can be information-rich, but spacing and typography must prevent clutter.

4. **One action color**
   - Coral is reserved for primary actions, active states, and selected tabs.

5. **Surface, not chrome**
   - Use cards and panels to group content instead of heavy borders or strong separators.

6. **No visual ambiguity between narrative and analytics**
   - Methodology sections should feel editorial.
   - Analytics sections should feel instrumental.

---

## 3. Visual token baseline

### 3.1 Colors

Derived from [`coral-stay-DESIGN.md`](../../../../../../memory/design/coral-stay-DESIGN.md:6).

- `--color-primary`: `#FF5A5F`
- `--color-primary-hover`: `#E04E52`
- `--color-secondary`: `#00A699`
- `--color-neutral`: `#767676`
- `--color-background`: `#FFFFFF`
- `--color-surface`: `#F7F7F7`
- `--color-text-primary`: `#222222`
- `--color-text-secondary`: `#717171`
- `--color-border`: `#DDDDDD`
- `--color-success`: `#008A05`
- `--color-warning`: `#E07912`
- `--color-error`: `#C13515`

### 3.2 Product-specific usage rules

- Coral is for:
  - active tab state
  - primary CTA buttons
  - selected period chip
  - important emphasis only
- Teal is for:
  - positive confirmation
  - “validated” or “ready” states
- Dark text is the default reading color.
- Maps must use their own analytical palettes and must not be recolored into the Coral brand palette.

---

## 4. Typography

Derived from [`coral-stay-DESIGN.md`](../../../../../../memory/design/coral-stay-DESIGN.md:20).

### 4.1 Font families

- Display: **Nunito Sans**
- Body: **DM Sans**
- Code / technical labels if needed: **JetBrains Mono**

### 4.2 Application hierarchy

- Hero page title: 42–48px, Nunito Sans, weight 800
- Section title: 28–32px, Nunito Sans, weight 700
- Tab title / map card title: 20–22px, Nunito Sans, weight 700
- Subheading: 16–18px, DM Sans, weight 600
- Body: 14–16px, DM Sans, weight 400
- Table header / label: 12px, DM Sans, weight 600, uppercase tracking
- Helper text: 12–13px, DM Sans, secondary text color

### 4.3 Typography rules

- Never use pure black.
- Use generous line-height in methodology prose.
- Keep map-card titles short and stable.
- Use consistent numeric formatting in tables and legends.

---

## 5. Layout system

### 5.1 Page frame

- Max width: 1280px
- Desktop side padding: 40px
- Mobile side padding: 24px
- Major section gap: 48px
- Related content gap: 24px

### 5.2 Global structure

The app should follow this frame:

1. sticky top navigation
2. page intro / page title band
3. global time-period selector
4. primary tab navigation
5. page content area

### 5.3 Grid behavior

- CRI metric cards: 2-column desktop grid, 1-column tablet/mobile fallback
- Methodology sections: single readable column with optional side callouts
- Ranking tables: stack below each map card, not beside it in the first version

---

## 6. Core surfaces and components

### 6.1 Navigation

Use the sticky navigation behavior from [`coral-stay-DESIGN.md`](../../../../../../memory/design/coral-stay-DESIGN.md:48), adapted for analytics.

- Height: about 72–80px
- White background
- Subtle shadow on scroll
- Left: product/app title
- Center or secondary row: period selector / tab nav depending on viewport
- Right: optional info/help actions

### 6.2 Cards

Map cards are the dominant UI primitive.

- White surface
- 12px radius
- 1px border in `#DDDDDD`
- Level 1 shadow by default
- 16–24px internal padding
- Title at top
- legend under title or attached to map
- table below map

### 6.3 Buttons

- Primary: coral fill, white text
- Secondary: transparent or white fill with dark border
- Ghost: text-only
- Minimum touch target: 48px height

### 6.4 Chips / selectors

Use pill chips for:

- time-period toggle
- optional province filter badges
- small status indicators

Active chip:

- coral background
- white text
- no border

Inactive chip:

- white or surface background
- dark text
- 1px border

### 6.5 Inputs

Province selector, search, or future filters should follow the Coral Stay input treatment:

- 48px height
- 8px radius
- 1px border
- focused state with stronger outline/border

### 6.6 Tables

Tables should feel lighter than enterprise dashboards.

- white card-contained surface
- strong header row
- 12–14px body text
- subtle row separators
- right-align numeric columns
- no dense spreadsheet look

---

## 7. Analytics-specific design rules

### 7.1 Maps

- Keep base UI neutral so map palettes remain readable.
- Map legend must always be visible.
- Map title must include metric name and current period meaning when needed.
- Map container should not be visually noisy.

### 7.2 Legends

- Place close to the map, preferably directly beneath or above it.
- Use compact labels.
- Avoid oversized legend chrome.

### 7.3 Ranking tables

- Each map gets its own ranking table area.
- Use explicit section labels such as:
  - `Top 10 provinces`
  - `Bottom 10 provinces`
- For tambon zoom mode, labels must shift to tambon grain.

### 7.4 Empty and loading states

- Loading states should use calm placeholders, not spinners everywhere.
- Empty states should explain why no data appears.
- Never render a broken blank map card with no text.

---

## 8. Screen-by-screen starting pattern

### 8.1 Methodology landing page

Should feel editorial and trustworthy.

Use:
- larger page title
- short intro paragraph
- section cards or clean content bands
- limitation callouts in softer surface cards

Avoid:
- dashboard-style density
- raw technical references

### 8.2 CRI tab

Should feel analytical and scannable.

Use:
- 2-column metric card grid
- full-width or visually emphasized CRI score card
- consistent map card template across all 7 cards

### 8.3 Tambon human-impact tab

Should feel drill-down oriented.

Use:
- prominent province selector
- strong relationship between national map and zoomed detail
- stable dual-map structure for deaths and affected households

### 8.4 Heat tab

Should feel simple and focused.

Use:
- two parallel cards or stacked cards for deaths and injured
- identical structure for easier comparison

---

## 9. Initial implementation tokens for frontend

Suggested frontend token groups:

- `brand.primary`
- `brand.primaryHover`
- `brand.secondary`
- `surface.base`
- `surface.subtle`
- `text.primary`
- `text.secondary`
- `border.default`
- `radius.sm`
- `radius.md`
- `radius.lg`
- `radius.pill`
- `shadow.card`
- `shadow.overlay`
- `font.display`
- `font.body`

This is enough to start implementation before later refinement.

---

## 10. Design constraints for the first build

1. Do not attempt a bespoke data-viz visual identity yet.
2. Do not heavily animate maps or panels.
3. Do not use coral to encode risk magnitude.
4. Do not overload the first version with floating widgets or sidebar filters.
5. Do not design methodology and analytics as if they are separate products.

---

## 11. What can evolve later

This file is intentionally starter-grade. The following may evolve after first implementation:

- exact map card composition
- responsive tab behavior
- table density rules
- hover interactions
- province selector styling
- typography tuning
- chart/legend refinement

The first priority is coherence and implementability, not perfection.

---

## 12. Instruction to builders

When implementing the first version:

1. Follow this file as the app-specific canonical design template.
2. Refer back to [`coral-stay-DESIGN.md`](../../../../../../memory/design/coral-stay-DESIGN.md:1) when a component behavior is not fully specified here.
3. If a design decision conflicts with readability of maps or ranking tables, prioritize analytical readability while staying visually within this design family.
