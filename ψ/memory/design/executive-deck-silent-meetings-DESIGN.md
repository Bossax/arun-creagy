# Executive Deck — Silent Meetings

A high-end, dual-mode design system for corporate leadership presentations. The aesthetic is quietly authoritative — editorial serif display type, generous white space on light slides, and a rich navy atmosphere on dark transition slides. Sky-blue accents convey clarity and precision.

## Overview

**Mood:** Boardroom confidence. Information-dense but never cluttered. Every pixel justifies its presence.  
**Audience:** C-level and senior leadership.  
**Slide variants:** Light (content slides) + Dark (section/title slides).

---

## Colors

### Brand Palette

| Token     | Hex       | Role                                              |
|-----------|-----------|---------------------------------------------------|
| Primary   | `#0284c7` | Sky blue — key accents, icons, borders, CTAs      |
| Primary Light | `#38bdf8` | Bright blue — headings on dark, highlights    |
| Amber     | `#f59e0b` | Warm amber — secondary highlights, warnings       |
| Emerald   | `#34d399` | Success states, positive data                     |

### Light Slide Palette

| Token          | Hex       | Role                                        |
|----------------|-----------|---------------------------------------------|
| Background     | `#f8fafc` | Slide canvas — cool off-white               |
| Surface        | `#ffffff` | Card / tile surfaces                        |
| Surface Raised | `#f1f5f9` | Table headers, subtle fill                  |
| Border         | `#e2e8f0` | Dividers, card borders                      |
| Border Strong  | `#cbd5e1` | Stronger separators                         |
| Text Primary   | `#0f172a` | Headlines, body text on light               |
| Text Secondary | `#475569` | Paragraphs, body copy                       |
| Text Muted     | `#94a3b8` | Captions, metadata, subtitles               |

### Dark Slide Palette

| Token          | Hex       | Role                                        |
|----------------|-----------|---------------------------------------------|
| Background     | `#0f172a` | Dark slide canvas — deep navy               |
| Surface        | `#1e293b` | Cards on dark, elevated areas               |
| Surface Raised | `#334155` | Hover/active on dark                        |
| Border Dark    | `#334155` | Subtle dark borders                         |
| Text Primary   | `#f8fafc` | Headings on dark slides                     |
| Text Secondary | `#94a3b8` | Body copy on dark                           |
| Text Muted     | `#64748b` | Tertiary info on dark                       |

### Semantic Colors

| Token   | Hex       |
|---------|-----------|
| Success | `#34d399` |
| Warning | `#f59e0b` |
| Error   | `#f87171` |
| Info    | `#38bdf8` |

---

## Typography

### Font Stack

| Role             | Font                                      |
|------------------|-------------------------------------------|
| Display/Headings | Lora, Georgia, 'Times New Roman', serif   |
| UI/Body          | 'Plus Jakarta Sans', Inter, sans-serif    |

*Load via Google Fonts: `Lora:ital,wght@0,400;0,700;1,400` and `Plus+Jakarta+Sans:wght@400;500;600;700`*

### Type Scale

| Level        | Font              | Size   | Weight | Line Height | Usage                            |
|--------------|-------------------|--------|--------|-------------|----------------------------------|
| Hero         | Lora              | 56px   | 700    | 1.15        | Title slide main headline        |
| Section H2   | Lora              | 52px   | 700    | 1.2         | Section transition headline      |
| Slide Title  | Lora              | 38px   | 700    | 1.2         | Content slide title (left-bordered) |
| H3 Card      | Lora              | 24px   | 600    | 1.3         | Card/tile headings               |
| H3 Table     | Plus Jakarta Sans | 20px   | 700    | 1.3         | Timeline, schedule headings      |
| Body Large   | Plus Jakarta Sans | 17px   | 400    | 1.6         | Main bullet points               |
| Body         | Plus Jakarta Sans | 16px   | 400    | 1.6         | Default body / table cells       |
| Body Small   | Plus Jakarta Sans | 15px   | 400    | 1.6         | Chart summaries, captions        |
| Caption      | Plus Jakarta Sans | 14px   | 400    | 1.5         | Card sub-text, schedule cards    |
| Label        | Plus Jakarta Sans | 13px   | 700    | 1.4         | Time tags, chips, overlines      |
| Subtitle     | Plus Jakarta Sans | 20px   | 400    | 1.5         | Title slide sub-headline         |

---

## Spacing

| Property                    | Value                        |
|-----------------------------|------------------------------|
| Base unit                   | 8px                          |
| Scale                       | 4, 8, 12, 16, 20, 24, 30, 40, 60, 80 |
| Slide padding               | 60px top/bottom, 80px left/right |
| Card padding — standard     | 30px                         |
| Card padding — schedule     | 20px                         |
| Section gap — two-column    | 40px                         |
| Tile gap                    | 24px                         |
| Bullet margin               | 16px                         |

---

## Border Radius

| Token   | Value | Usage                                   |
|---------|-------|-----------------------------------------|
| Small   | 4px   | Chips, tags, table cells                |
| Medium  | 8px   | Buttons                                 |
| Default | 12px  | Cards, tiles, image wrappers            |
| Large   | 16px  | Slide container itself                  |
| Full    | 9999px| Pill badges, round icons                |

---

## Shadows

| Level      | CSS Value                                              | Usage                      |
|------------|--------------------------------------------------------|----------------------------|
| Card       | `0 4px 12px rgba(15, 23, 42, 0.03)`                   | Default cards/tiles         |
| Slide      | `0 20px 40px rgba(0, 0, 0, 0.4)`                      | Slide container drop shadow |
| Image      | `0 4px 12px rgba(15, 23, 42, 0.05)`                   | Image wrappers              |
| Icon Bg    | —                                                      | Icon tinted background      |

**Glow (dark slides only):**
- Primary glow: `radial-gradient(circle at 15% 15%, rgba(56,189,248,0.15) 0%, transparent 50%)`
- Amber glow: `radial-gradient(circle at 85% 85%, rgba(245,158,11,0.1) 0%, transparent 50%)`

---

## Slide Layouts

### 1. Title Slide (Dark)
- Background: `#0f172a`
- Full-bleed dark canvas with subtle radial glow
- H1 Lora 56px bold, color `#f8fafc`
- Accent word in headline: `#38bdf8`
- Subtitle: Plus Jakarta Sans 20px, color `#94a3b8`

### 2. Section Transition (Dark)
- Background: `#0f172a`
- Centered layout — `max-width: 800px; margin: auto`
- Decorative HR: 80px wide, 4px tall, `#38bdf8`, centered
- H2 Lora 52px, color `#f8fafc`
- Subtitle: 20px, `#94a3b8`

### 3. Content Slide (Light)
- Background: `#f8fafc`
- Top slide title with left border accent: `5px solid #38bdf8`, padding-left 15px
- Content area grows to fill remaining space, vertically centered
- Subtle radial glow background decoration (blue top-left, amber bottom-right)

### 4. Two-Column (Light)
- `grid-template-columns: 1fr 1fr; gap: 40px`
- Tiled variant: each column in a white card with border, radius 12px

### 5. Tile Grid (Light)
- `display: flex; gap: 24px; align-items: stretch`
- Each tile: white bg, border `#e2e8f0`, radius 12px, padding 30px
- Icon container: 64×64px, bg `#f0f9ff`, radius 12px, icon color `#0284c7`

### 6. Highlight Number (Light)
- Two-column: left column has giant number (Lora 120px, `#0284c7`) + label
- Divider: `2px solid #e2e8f0` on right of number column

### 7. SCQA Table (Light)
- Full-width table, radius 12px, overflow hidden, `border: 1px solid #e2e8f0`
- `th`: bg `#f1f5f9`, color `#0f172a`, bold, width 25%, font-size 18px
- `td`: vertical-align top, body 16px `#475569`
- Last row: no border-bottom

### 8. Schedule Grid (Light)
- `grid-template-columns: repeat(3, 1fr); gap: 20px`
- Schedule card: white bg, `border-left: 4px solid #0284c7`, radius 12px, padding 20px
- Time tag chip: bg `#f0f9ff`, color `#0284c7`, font-size 13px, uppercase, letter-spacing 0.5px
- Accent variant: border-left `#34d399`, chip bg `#ecfdf5`, chip color `#059669`

### 9. Bar Chart (Light)
- Bar container: `display: flex; align-items: center; gap: 20px`
- Label: 240px wide, right-aligned, bold
- Bar track: bg `#e2e8f0`, radius 8px, height 40px
- Fill — danger: `linear-gradient(90deg, #f87171, #dc2626)`
- Fill — warning: `linear-gradient(90deg, #fbbf24, #d97706)`
- Fill — success: `linear-gradient(90deg, #34d399, #059669)`
- Fill text: white, bold 14px, right-padded 15px

### 10. Timeline (Light)
- Horizontal layout, 4 items at 22% width each
- Center line: 4px, `#e2e8f0`
- Node: 24px circle, white bg, `border: 5px solid #0284c7`
- Odd items: content above center line; even items: below

### 11. Bleed Image Right (Light)
- `grid-template-columns: 1fr 1fr; padding: 0`
- Left: content with 60px/80px padding, vertically centered
- Right: full-height image (720px), `object-fit: cover`

### 12. Q&A / Closing (Dark)
- Centered, `margin: auto`
- H2 Lora 64px, color `#f8fafc`
- Closing line: Plus Jakarta Sans 18px, bold, color `#38bdf8`

---

## Components

### Slide Container

- `width: 1280px; height: 720px` — fixed 16:9 ratio
- `border-radius: 16px`
- `box-shadow: 0 20px 40px rgba(0,0,0,0.4)`
- `overflow: hidden`
- `padding: 60px 80px`

### Slide Title Bar

Every content slide uses a left-bordered title:
- Font: Lora 38px bold
- `border-left: 5px solid #38bdf8; padding-left: 15px`
- Color light: `#0f172a` / Color dark: `#f8fafc`
- Margin bottom: 30px

### Bullet List

- `list-style: none; padding: 0`
- Item padding-left: 35px (room for icon)
- Icon: FontAwesome, positioned absolute left, color `#0284c7`
- Body: Plus Jakarta Sans 17px, line-height 1.6, color `#475569`
- Spacing between items: 16px

### Tile / Card

- Background: `#ffffff`
- Border: `1px solid #e2e8f0`
- Radius: 12px
- Padding: 30px
- Box shadow: `0 4px 12px rgba(15,23,42,0.03)`
- Icon wrapper: 64×64, bg `#f0f9ff`, radius 12px
- H3: Lora 24px, color `#0f172a`
- Paragraph: 16px, color `#475569`

### Schedule Card

- Background: `#ffffff`
- Border: `1px solid #e2e8f0` + `border-left: 4px solid #0284c7`
- Radius: 12px
- Padding: 20px
- Time tag: pill, bg `#f0f9ff`, color `#0284c7`, 13px uppercase bold
- H3: Plus Jakarta Sans 18px bold, color `#0f172a`
- Body: 14px, `#475569`

---

## Do's and Don'ts

1. **Do** use Lora for all headings — the serif gives authority and editorial weight.
2. **Do** limit each light content slide to one primary layout pattern — don't mix chart + tile + table.
3. **Do** alternate dark section slides between content slide groups for visual rhythm.
4. **Don't** use more than two accent colors per slide — sky blue is primary, amber only for emphasis.
5. **Do** keep the slide canvas fixed at 1280×720px — this ensures pixel-perfect PDF export.
6. **Don't** place body text smaller than 14px — readability at projection scale is paramount.
7. **Do** use the left-border slide title on every light content slide for visual consistency.
8. **Don't** exceed 4-6 bullet points per slide — cognitive load kills focus.
9. **Do** use FontAwesome solid icons (fa-solid) exclusively — they read at distance.
10. **Don't** skip the radial glow backgrounds — they add depth without distraction.
