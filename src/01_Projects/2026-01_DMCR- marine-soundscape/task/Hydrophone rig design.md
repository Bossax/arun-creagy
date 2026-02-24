---
type: task
status:
  - In-progress
project:
start date: 2026-02-01
due date: 2026-03-01
---
# Overview: Mooring vs Tripod

|**Feature**|**Current "Stealth Tube" (Mooring)**|**Proposed "Stealth Tripod" (Lander)**|
|---|---|---|
|**Stability**|**Poor:** Sways with every wave (Inverted Pendulum).|**Excellent:** Rigidly fixed to seabed.|
|**Acoustics**|**Risk:** Flow noise & Strumming from rope.|**Superior:** No moving parts; precise sensor elevation.|
|**Entanglement**|**High:** Vertical rope catches debris/nets.|**Low:** Low profile, nothing to snag.|
|**Theft**|**Medium:** Can float to surface if cut.|**Low:** Stays on bottom; harder to spot.|
|**Deployment**|**Complex:** Requires adjusting rope length for tide.|**Simple:** Drop it and leave it.|

---

# Decision Log (Accepted from [[01_Projects/2026-01_DMCR- marine-soundscape/source/Comprehensive Engineering Report - Multi-Criteria Analysis and Design Specification for Shallow Water Hydrophone Rigs in Coral Reef Ecosystems.md|MCA Report]])

## Design Architecture Decision

- **Selected Architecture:** **Articulated Tripod (Lander)** (highest MCA score 4.05). This design best balances stability, acoustic fidelity, environmental stewardship, and deployability.
- **Rejected Alternatives:**
  - **Gravity Base (Sled/Block):** Excessive footprint, higher flow noise, sliding risk on reef slope.
  - **Helical/Pinned Anchor:** Strong but invasive and operationally complex for diver deployment.

## Criteria Weighting (AHP)

- **Structural Integrity:** 35%
- **Acoustic Performance:** 25%
- **Environmental Compatibility:** 20%
- **Operational Efficiency:** 20%

## Governing Environmental/Acoustic Constraints

- **High-energy shallow reef flow:** Drag-dominated regime (high KC). Minimize projected area and drag coefficient.
- **Flow-noise risk:** Turbulent boundary layer causes pseudo-sound below 100 Hz. Sensor must be elevated and/or shielded.
- **Benthic protection:** No chain scour. Point-contact only; avoid smothering live coral.

# Design Specification Snapshot (Reef-Sentry)

## Geometry

- **Base:** Equilateral triangle, **1.5 m** side length.
- **Total Height:** **1.2 m**.
- **Leg Angle:** **45–60°** from horizontal.

## Stability & Leveling

- **Adjustable Legs:** Telescopic/threaded extensions for leveling on uneven reef.
- **Articulated Foot Pads:** ~**100 mm** diameter, ball-and-socket with high-friction elastomer or **spike bolts** (~10 mm) for mechanical interlock.

## Materials & Corrosion Control

- **Primary Frame:** **316L Stainless Steel** (passivated welds).
- **Avoid:** Aluminum in contact with SS (galvanic risk) unless fully isolated.
- **Isolation Hardware:** **Delrin/HDPE** clamps and washers between sensor housing and frame.

## Acoustic Integration

- **Vibration Isolation:** **Bungee/shock-cord** suspension of hydrophone to decouple frame vibration.
- **Flow Shield:** Porous **ballistic nylon** or **open-cell foam (30–60 PPI)** cage around sensor to cut low-frequency flow noise.

## Ballast & Handling

- **Hollow Legs:** Transport empty; **fill in situ** with sand/lead shot for required submerged weight.
- **Safety Factors:** Design for **SF ≥ 1.5** against sliding and overturning under fouled condition (increased C_d and D).

## Deployment & Recovery

- **Diver Deployment:** Use **lift bag** for recovery; avoid manual heavy lifting.
- **Optional Diver-Less Recovery:** Acoustic release + pop-up buoy (future upgrade).

# Specific mechanical adjustments that are likely need to perform on-site

comparing how the **Mooring (Stealth Tube)** and the **Tripod (Lander)** handle them.

### 1. Vertical Adjustment (Sensor Height)

- **The Goal:** Position the hydrophone slightly above the highest nearby coral head to avoid "Acoustic Shadowing", while staying below the wave energy zone.

|**Feature**|**Mooring (Stealth Tube)**|**Tripod (Lander)**|
|---|---|---|
|**Adjustment Mechanism**|**Rope Length.** You cut the rope or adjust a knot/clamp to change the distance between the anchor and the tube.|**Mast Height.** You extend a central vertical pipe (the mast) upwards from the tripod base.|
|**Field Difficulty**|**Very Low.** Cutting rope is instant. You can even adjust it underwater if you use a sliding knot (like a taut-line hitch) before locking it.|**Medium.** Requires a "Telescoping" design (a smaller pipe sliding inside a larger one) secured with a through-bolt or pin.|
|**Precision**|**Low.** Even if you set the rope to 1.5m, currents will push the buoy over, reducing effective height (Pythagorean theorem). The sensor "bobs" in the current.|**High.** The sensor stays exactly where you pin it (e.g., 1.5m). It does not dip or sway.|
|**Winner**|**Tripod.** For scientific data, fixed geometry is superior. You can design a central PVC mast with pre-drilled holes every 10cm for rapid height selection on the boat.||

### 2. Footprint & Leveling (Seabed Interaction)

- **The Goal:** Ensure the rig sits flat and stable on an uneven reef or sand patch without tipping over.

|**Feature**|**Mooring (Stealth Tube)**|**Tripod (Lander)**|
|---|---|---|
|**Adjustment Mechanism**|**None Needed (Self-Leveling).** The anchor block sits however it lands. The buoyancy of the tube pulls the system vertical automatically.|**Leg Length/Angle.** You must adjust individual leg lengths to compensate for uneven ground (e.g., one leg on a rock, two on sand).|
|**Field Difficulty**|**Zero.** The physics of buoyancy handles leveling for you. This is the mooring's biggest advantage.|**High.** A fixed tripod will wobble on uneven ground. You need **articulated feet** or **adjustable legs** (like camera tripod legs) to get it level.|
|**Risk**|**Dragging.** If the anchor isn't heavy enough or the footprint is too small, the whole system slides.|**Toppling.** If not leveled, a current can tip the tripod over.|
|**Winner**|**Mooring.** It is "set and forget" regarding the seabed angle. A tripod requires careful placement by a diver.||

### 3. Ballast Tuning (Weight Adjustment)

- **The Goal:** Adding enough weight to resist drag forces (currents/waves) without making it too heavy to lift.

| **Feature**              | **Mooring (Stealth Tube)**                                                                                                                               | **Tripod (Lander)**                                                                                                          |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **Adjustment Mechanism** | **Anchor Size.** You must cast the concrete block _before_ you get on the boat. Changing weight on-spot means adding loose weights (danger of clanking). | **Hollow Legs.** You can bring empty PVC legs and fill them with sand, lead shot, or chain _on the boat_ or even underwater. |
| **Field Difficulty**     | **Hard.** You are committed to the 40-50kg block you made. If it's too light, you're in trouble.                                                         | **Easy.** You can fine-tune stability by adding/removing weight inside the tubes.                                            |
| **Winner**               | **Tripod.** Hollow PVC structures allow you to transport a light frame and "ballast down" on site using local sand or lead diving weights.               |                                                                                                                              |
