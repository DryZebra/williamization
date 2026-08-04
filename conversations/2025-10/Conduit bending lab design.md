---
type: Conversation
title: "Conduit bending lab design"
description: "I need a conduit bending lab that's kind of as complex as it can get for math. I want them to design 360 degrees of bend into a conduit, do all the ma"
resource: "68f3b9a8-d6bc-832f-90a2-f59ea0da8538"
timestamp: "2025-10-18T16:39:03.059Z"
tags: ["gpt-5"]
---

# Conduit bending lab design

## User

I need a conduit bending lab that's kind of as complex as it can get for math. I want them to design 360 degrees of bend into a conduit, do all the math to achieve a specific shape and they need to give me all the marks on a single conduit such that at the end it's perfect lengths on every leg and perfect angles on every bend. Can you design a homework assignment like this?

## Assistant



## Assistant



## Assistant



## Assistant

Heck yes—this is a great capstone lab. Here’s a self-contained assignment that forces them to plan, compute, and bend exactly **360°** on a single stick, with tight tolerances and full math.

# Conduit Bending Capstone — 360° on One Stick

## The mission
Using **one 10-ft stick of ¾″ EMT**, design and bend a conduit that fits the 3D path below **without any cuts** and with the **sum of all bend angles = 360°**. You must compute every mark, angle, spacing, shrink, gain, and developed length. Finished piece must meet all dimensions and clearances.

### The required path (coordinate spec)
Start from Box A and end at Box B. Treat the conduit centerline as the path.

- **Datum:** Factory end of the stick = 0.00″ mark. All layout marks are measured from this end.
- **Box A (start):** Surface-mount box on a wall. Conduit must **stub up 12.0″** from the floor into the bottom KO of Box A (center of KO is **12.0″ above finished floor** and **2.0″ out** from the wall to the conduit centerline).
- From Box A, run **horizontally 36.0″** (centerline) along the wall, then perform a **rolling offset** that raises the conduit **6.0″ up** and **8.0″ right (out from wall)** to bypass an obstruction. After the offset, continue **24.0″** straight in the new line of travel.
- Next, cross a pipe with a **three-bend saddle** over a **4.0″ obstruction height** (measured to required clearance at conduit centerline). After the saddle, continue **18.0″** straight.
- Finally, turn to enter Box B using a **segmented 90° bend** (4-shot) around the corner to a perpendicular wall and land into Box B’s side KO. The center of Box B KO is **48.0″ above floor** and **2.0″ off the perpendicular wall** (to conduit centerline). The horizontal distance from the end of the straight section before the segmented bend to the Box B wall is **22.0″**.

### Bend set (angles must total exactly 360°)
Use exactly these bends (order as placed in the path above):

1. **Stub-up 90°** into Box A. (90°)
2. **Rolling offset:** two equal legs, each **30°**. (60° total)
3. **Three-bend saddle:** outer legs **30°**, center **60°**. (120° total)
4. **Segmented 90°:** **4 shots × 22.5° = 90°** total, entering Box B.

**Grand total = 90 + 60 + 120 + 90 = 360°.**

> You may NOT add or change bends. All four groups must be present with the stated angles.

---

## What you must determine **before** layout
You must **measure and document** the following for the exact bender you’ll use (no guessing/Internet charts—verify on your tool):

1. **Bender take-up** for a ¾″ EMT stub-up 90° (inches).
2. **Centerline radius (CLR)** of your shoe for ¾″ EMT (inches).  
   - Method: mark two tangent points on a test 90°, measure chord and arc, solve radius; or use manufacturer spec if engraved on the shoe—but still verify with a quick check.
3. **Star/arrow positions** relative to center of bend (how your specific shoe wants you to place marks).

Attach your measurement method and raw notes.

---

## Formulas you must use (show the work)

> Use exact trig (degrees), carry at least 3 decimals in calc, and round layout marks only at the end to **1/16″**.

**A. Offsets (single-plane)**  
For a two-bend offset with bend angle θ and required offset height \(h\):

- **Multiplier:** \(M(θ)=\dfrac{1}{\sin θ}\)  
- **Shrink per offset:** \(S(θ)=h\,(1-\cos θ)\) (subtract from the straight between bends)  
- **Spacing (center-to-center):** \(h \cdot \cot θ\)

**B. Rolling offsets (true 3D)**
Given rise \(r\) and lateral shift \(s\):

- **True offset:** \(H=\sqrt{r^{2}+s^{2}}\)  
- Choose angle θ (here θ = 30° on each leg).  
  - **Rolling spacing:** \(H \cdot \cot θ\)  
  - **Rolling shrink:** \(H\,(1-\cos θ)\) (applies along the original run direction)

**C. Three-bend saddle (outer legs β, center α = 2β)**
Given obstacle height \(h\) (to conduit centerline plus clearance):

- **Standard choice here:** β = 30°, α = 60°.  
- **Outer-to-center spacing:** \(h \cdot \cot β\) (from first outer to center, and center to second outer—symmetric)  
- **Total saddle shrink along run:** \(2\,h\,(1-\cos β)\)

**D. Segmented bend (n-shot 90°)**
Let total \(Θ=90°\), shots \(n=4\), so per-shot angle \(\phi=Θ/n=22.5°\).

- **Mark spacing (chord approximation along centerline):**  
  \(c \approx 2\,\text{CLR}\,\sin(\phi/2)\) (between shot centers)
- **Developed arc length check:** \(L_{\text{arc}} = \dfrac{π}{2}\cdot \text{CLR}\) (exact for 90°; use this to verify your cumulative chords ≈ arc length)

**E. 90° gain (for layout sanity checks)**
For any 90° made on CLR \(R\), the **gain** compared to a sharp corner is:
\[
\text{Gain}_{90} = 2R\left[\,\tan\!\left(\frac{90°}{2}\right) - \frac{\pi}{4}\,\right]
= 2R\,(1 - \tfrac{\pi}{4}) \approx 0.4292\,R
\]
Use this to reconcile straight-run legs vs developed lengths around the segmented 90° (and to cross-check your back-to-back geometry if you sanity-test alternatives).

---

## Layout requirements & tolerances
- **All layout marks** must be measured from the factory end (0.00″), listed in ascending order, and labeled by bend (e.g., “Stub-up center @ xx.xx″,” “Rolling #1 @ …,” etc.).  
- **Angles:** within **±1°** of spec.  
- **Linear dims:** within **±1/8″** at each control point (heights, wall offsets, run lengths).  
- **Clearance over the 4.0″ obstruction**: **≥ 4.0″** at conduit centerline after spring-back (verify physically).  
- **No kinks, no ovaling beyond normal.**  
- **No cuts.** One continuous stick.

---

## What to turn in (deliverables)

1. **Bend Map (one page):**
   - A table with columns: **#**, **Feature**, **Angle(s)**, **From 0.00″ to Mark (in)**, **Between-marks (in)**, **Notes (arrow/star/center)**.
   - A simple schematic (not to scale) that labels each bend and straight segment with the intended post-bend dimensions.

2. **Calculation Packet:**
   - Your measured **take-up** and **CLR** (with method).  
   - Step-by-step trig for:  
     - Rolling offset true offset \(H\), spacing, shrink.  
     - Saddle spacing and shrink.  
     - Segmented 90° per-shot spacing \(c\) and shot count; arc-length check vs. \((\pi/2)\,R\).  
     - Global **developed length** check (sum of straights + all arcs) ≤ 120″ stick, **with margin**.  
     - **Spring-back plan** (your chosen over-bend per angle based on a test coupon and your EMT; document your assumed spring-back per shot).

3. **QA Checklist (completed after bending):**
   - Actual vs. design measurements at each checkpoint:
     - Stub height to Box A center (12.0″)  
     - Post-rolling offset rise (6.0″) and shift (8.0″)  
     - Straight runs (36.0″, 24.0″, 18.0″) minus applicable shrinks (show measured)  
     - Saddle clearance ≥ 4.0″ (centerline)  
     - Segmented 90° landing: alignment to Box B KO center (48.0″ AFF, 2.0″ off wall, 22.0″ approach)  
   - Angle readings (digital angle finder) at each leg.

4. **One photo** of the finished piece aligned to a chalk-line grid (or tape-measure setup) showing key dimensions.

---

## Step-by-step design outline (how they should proceed)

1. **Measure your tool:** determine take-up and CLR. Record.
2. **Plan the sequence from 0.00″ end** in the order used in the path (stub-up first). Reserve enough straight from the factory end for the **stub-up 90°** using take-up. Compute where the 90° center must be to hit **12.0″** height at Box A.
3. **Lay out the 36.0″ run** from the 90° tangent. Account for any shrink/gain interactions (sanity check with gain formula).
4. **Rolling offset (30°/30°):**
   - Compute \(H=\sqrt{6^2+8^2}\).  
   - Compute spacing \(H\cot 30°\) and shrink \(H(1-\cos 30°)\).  
   - Place marks for the two 30° bends; subtract rolling shrink from the straight between the offset legs.
5. **Add the 24.0″ run** from the second rolling tangent; adjust for the rolling shrink already taken.
6. **Three-bend saddle (30°–60°–30°):**
   - Compute outer-to-center spacing \(h\cot 30°\) with \(h=4.0″\) (remember to use **clearance to conduit centerline**).  
   - Compute saddle shrink \(2h(1-\cos 30°)\).  
   - Place three marks: outer-1, center, outer-2 with equal spacing.
7. **Add the 18.0″ run** from the last saddle tangent.
8. **Segmented 90° (4 shots of 22.5°):**
   - Compute per-shot center spacing \(c=2R\sin(22.5°/2)\).  
   - Mark 4 shot centers at spacing \(c\).  
   - Check that your final outlet center will land **22.0″** away at the perpendicular wall and **48.0″** AFF with the **2.0″** off-wall center. Use the 90° gain and the wall setback to verify landing geometry before bending.
9. **Spring-back plan:** Decide over-bend targets (e.g., +2–3° on 30° legs, +3–4° on 60°, +1–2° on each 22.5° shot) based on your test coupon; record intent and actuals.
10. **Bend in order, re-checking after each stage.** Correct minor errors by slight re-shots only if within tolerance.

---

## Grading rubric (100 pts)

- **Tool characterization (10 pts):** Clear, measured take-up & CLR with method.
- **Math correctness (30 pts):** Proper use of multipliers, spacing, shrink, gain, segmented chords; clean, traceable calc.
- **Bend map quality (10 pts):** Unambiguous marks from 0.00″, labels match field work.
- **Execution accuracy (40 pts):** All final dims within tolerance; angles within ±1°; clean work (no kinks/flattening).
- **QA evidence (10 pts):** Completed checklist + photo proof on a grid.

Bonus (up to +5): neatness, clever sanity checks, or an error-budget table that anticipates spring-back and cumulative tolerance.

---

## Safety & shop constraints

- Eye protection, gloves when appropriate.
- Use a **digital angle finder** and at least two tape measures for buddy checks.
- No cuts, no couplings. One stick only.
- If you blow a piece, **attach the post-mortem** (where the math or sequence went wrong).

---

## Instructor answer key (what you’ll prep)

- Provide students a one-page sheet with the path geometry and this bend set (angles fixed).
- Have a reference CLR and take-up measured on **your** shop shoes (to check their numbers are plausible but still allow variance if they used a different shoe).
- Prepare a quick “sanity” solution with:
  - Rolling offset: \(H=\sqrt{6^2+8^2}=10.000″\) (nice!)  
    - For 30°: \(\cot 30° = \sqrt{3} \approx 1.73205\) → spacing \(= 10.000 \times 1.73205 = 17.320″\)  
    - Shrink \(= 10.000 \times (1-\cos 30°) = 10.000 \times (1-0.86603)=1.3397″\)
  - Saddle (β = 30°, \(h=4.0″\)): spacing each side \(= 4.0 \times 1.73205 = 6.928″\); total saddle shrink \(= 2 \times 4.0 \times (1-0.86603)=1.071″\)
  - Segmented 90° (n=4, \(\phi=22.5°\)):  
    - If your measured **R** (CLR) = e.g. **6.00″** (shop example), then per-shot spacing \(c = 2R\sin(11.25°) = 12 \times 0.19509 = 2.341″\)  
    - Arc length check: \(L=\frac{\pi}{2}R=1.5708\times 6.00=9.425″\); 4 chords sum ≈ \(4\times 2.341 = 9.364″\) (close; acceptable for layout with center marks and shoe geometry)

*(Keep these private; hand out only if you want to spot-check.)*

---

If you want, I can drop this into a printable PDF with a bend-map table template and a pre-made QA checklist.

## User

Now without the complexity, create the assignment sendable in a text message. So it has to contain just the bends and the fact that it needs to be written as marks on a straight conduit. 

## Assistant



## Assistant



## Assistant

Here’s a version you can paste as a single text:

**Conduit Lab (SMS ver.)**  
On ONE 10′ stick of ¾″ EMT, lay out **all bend marks from the factory end** (0.00″) and bend **exactly 360° total** in this order:

1) **Stub-up 90°**  
2) **Rolling offset**: **30° + 30°**  
3) **Three-bend saddle**: **30° – 60° – 30°**  
4) **Segmented 90°**: **4 shots × 22.5°**

Turn in: a simple list of your marks (distance from 0.00″ to each bend center/arrow/star), labeled by bend, plus the final angles you hit. One continuous stick; no cuts. Angles must match the sequence above.

