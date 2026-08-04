---
type: Conversation
title: "Parallel breakers safety advice"
description: "Assuming two different sources, does this work?"
resource: "68837517-9d48-8331-ad08-a1aa2bdcc58a"
timestamp: "2025-07-25T12:33:24.185Z"
tags: ["gpt-4o"]
---

# Parallel breakers safety advice

## User


Assuming two different sources, does this work?

## Assistant



## Assistant

Short answer: **No, this setup is dangerous and not code-compliant** — even if the two 30A breakers are from different 240V sources, paralleling them like this to create a "60A" feed **is not safe or allowed**.

---

### Here's why:

#### 🔴 **1. Breakers are not designed to be paralleled**
- Standard circuit breakers (like the 30A ones shown) are not rated to share current across poles.
- You can't assume that each breaker will carry exactly 30A and "add up" to 60A. If one trips, the other will suddenly be forced to carry 60A on its own — well beyond its limit.

#### ⚠️ **2. Phase synchronization is critical**
- Even if the voltage is 240V on both feeds, **they must be phase-synchronized** if you're paralleling them.
- Unless these are **grid-synchronized inverters or generators**, the two 240V sources may be slightly or completely out of phase. That causes:
  - Massive circulating currents.
  - Voltage surges.
  - Breaker damage, fire, or equipment destruction.

#### 🧯 **3. NEC forbids this unless specific equipment is used**
- **NEC 705.12(B)** covers parallel power sources, and only allows it with proper overcurrent protection, synchronization, and equipment rated for parallel operation (like solar inverters, paralleling-rated transfer switches, or generator paralleling gear).
- What you’ve drawn is **not a safe or legal way to create a 60A circuit**.

---

### ✅ If you actually need 60 amps:

- **Option 1**: Install a proper **60A breaker and wire** rated for 60A (like #6 Cu THHN).
- **Option 2**: Use **dual 30A circuits separately** if they’re powering separate loads.
- **Option 3**: Use a **paralleling-rated transfer switch or panel** with equipment designed for load balancing and fault isolation.

---

### Summary:
- 🛑 **Don't parallel breakers or sources like this**.
- 🔥 It’s unsafe and a serious fire/equipment hazard.
- ⚖️ NEC does not allow it without specific, rated equipment.
- 💡 Instead, upsize to a proper 60A feed if that's what you need.

Let me know what you’re trying to power — I can help you design a safe solution.

## User

Sorry, I forgot context. I was explaining to my students that if you took a single stranded #12, and while it was live, split the end in half and then reattached it later, each "half" of the wire has "half" the total amperage moving across the wire because of the way amperage stays the same in parallel, but kirchovs law mandates that what returns to source must equal what left source and so at the other end of the wire where they come back together, it's also 10A. 

So one of my students drew this.

Having never done this highly dangerous and illegal action, I never thought about it. I know that from a *single* source, like a 240 source using A and B phase in a balanced load, 30+30=30 because of the alternations of the current. 

## Assistant

Ahh — now that context changes everything. Thank you. That actually becomes a **fantastic teachable moment**, both about **Kirchhoff’s Current Law (KCL)** and **why “30 + 30” doesn’t always equal 60 in power systems**.

Let’s walk through it clearly:

---

### 🔧 The Original Teaching (Single Source, Split Conductor)
You're right:
- If you take a single #12 wire carrying 10A and physically **split the conductor into two strands**, current will divide **based on resistance** (roughly equally if identical) — say 5A/5A.
- **Kirchhoff’s Current Law (KCL)** says:
  - The **sum of currents entering a node = sum leaving**.
  - So at the split: 10A in → 5A + 5A → 10A out when recombined.
- It’s *still one circuit*, just with a branching path.
- So this is a **parallel path**, but **not a parallel source**.

Great illustration of how amperage “splits” but doesn’t “double.”

---

### 🔌 The Student’s Drawing (Two Breakers, Two Sources)

This is where it goes off the rails a bit. The student seems to think:

> “If one 30A breaker feeds 30A, and I parallel another one just like it, I now get 60A!”

And your instinct is correct to hesitate.

### Here’s why this is **wrong**:
- **They are not feeding one wire from one source and splitting it**, like in your example.
- They are attempting to **parallel two different sources** (even if they’re on the same panel and phase).
- Unlike your single-wire split, there’s no guarantee the two breakers share current evenly — **because each breaker is tied to its own internal protection and impedance path**.
- Worse, if they’re on separate **phase legs**, it could become a **240V short**.

---

### 🔥 Critical Distinctions:

| Situation | Description | Result |
|----------|-------------|--------|
| **Single wire, split physically** | One circuit path split into multiple strands | Safe if conductors sized correctly (like using 2x #12 to carry 20A) |
| **Two sources (even if both 240V)** | Paralleling different breakers/wires | Unsafe without synchronizing equipment |
| **240V multiwire branch circuit (MWBC)** | Shared neutral, 2 hots (A/B) | 30A max (not 60A) because currents alternate, canceling in the neutral |

---

### 👷‍♂️ So how do you explain it to students?

> **“Amperage doesn't add when you're paralleling *sources* — it only adds when you're splitting *paths* in the same circuit.”**

Use this analogy:
> “Imagine water pipes: If you have one pipe and split it into two equal hoses, the flow splits. But if you try to hook up two fire hydrants to the same hose from different sides, without knowing the pressure and timing? You’ll get a blowout.”

---

### Bonus Teaching Tool — How to Drive It Home

Ask:
> “What happens if one of these 30A breakers trips, but the other doesn't?”

Let them realize:
- Now you have **all 60A trying to go through one 30A breaker**.
- Or worse — a **floating voltage differential** between sources.

---

### Conclusion

Your instinct and method were spot-on. Your student’s drawing is:
- **An intuitive leap**, but
- **A dangerous one**, and
- **A perfect teaching opportunity**.

If you want, I can draw you a corrected version of the concept — same wire, split, recombined — versus the parallel breaker misconception. Let me know.

## User

Go further into the 240v phase short. Let's assume we did build this. We've got 2 240v sources, A phase of source 1 and B phase of source 2 are under breaker1. A phase of source 2, and B phase of source 1 are under breaker2. Now obviously that's an issue, but there's no short yet. 

When the A phase of source 1 meets the A phase of source 2, what is going to happen assuming it's connected to a 60A piece of equipment and this is theoretical, so everything is ideal meaning exactly 240v. RMS at all times and 60A. 

## Assistant

You're asking the right question, and this is *the* moment where a lot of electricians (and even some engineers) get their wires crossed, pun fully intended. Let's walk through it like professionals on a whiteboard with a calm, systematic breakdown.

---

### 🧠 Setup Recap — The “Crossed-Phase Parallel Feed” Experiment

You said:
- **Breaker 1**: A₁ and B₂ (A phase from source 1, B phase from source 2)
- **Breaker 2**: A₂ and B₁ (A phase from source 2, B phase from source 1)
- **Loads** are tied together, trying to act like one 240V, 60A device
- **Assume all RMS voltages = 240V**, all timing perfect

So in a perfect world:
- A₁ = A₂ = 240V (but from different sources)
- B₁ = B₂ = 240V (but from different sources)
- You're trying to run a 240V load across the breaker pairings

---

### ⚡ The Key Problem: **Different Sources ≠ Same Reference**

Even if both sources are “240V,” what matters is:
- Are the **phase angles** aligned?
- Are the **neutral and ground references** truly identical?
- Is there a **shared timing reference** (like in grid-tied systems)?

Your assumption is: *“Everything is 240V RMS and balanced.”* That’s fine *per source*, but when you tie **A₁ and A₂ together** and **B₁ and B₂ together**, you're assuming those phases are *identical in phase and voltage*, down to the microsecond.

---

### 🧨 What Happens When You Tie Phases from Separate Sources?

#### 🔁 Best case: **Slight mismatch**
- Say A₁ is 240V at 0°, A₂ is 240V at 2° (slight drift)
- You now have **a voltage delta between A₁ and A₂**
- That delta causes a **circulating current** *between sources*
- Since there's minimal impedance, **the wire becomes the load**
- Large, uncontrolled current will flow — **not through the 60A load**, but **between breakers and sources**, likely tripping one or both, or melting conductors

#### ⚡ Mid case: **Out-of-phase but not inverted**
- If the phase angle is 90° off, you’ll get:
  - A pulsing voltage differential
  - Result: High-frequency circulating currents, massive waveform distortion
  - Destruction of sensitive equipment and harmonic chaos

#### 🔥 Worst case: **180° out-of-phase (mirror image)**
- A₁ is 240V at 0°, A₂ is 240V at 180°
- When you tie them together? You’ve made a **direct short across 480V** potential
- Instant arc, **breaker explosion** if impedance is low enough

---

### 📐 Let's Math It for the 180° Case

Let:
- A₁(t) = 240V * sin(ωt)
- A₂(t) = 240V * sin(ωt + π) = −240V * sin(ωt)

Then:
- Voltage between A₁ and A₂ = A₁(t) − A₂(t) = 240V * sin(ωt) − (−240V * sin(ωt)) = **480V * sin(ωt)**

That’s a **480V AC short across your conductor**. The same applies to B₁ and B₂. If you're lucky, your breakers trip. If you're not, someone dies.

---

### 🤯 But Wait: Even If Phase Is Matched…?

Even if you got **two inverters** perfectly synchronized (like in off-grid solar), you'd still **never parallel them this way** without a **paralleling controller**:
- You need **current-sharing logic**, which allocates load dynamically
- Otherwise, one source might “push” while the other is “dragging,” creating internal resistance faults or overloading feedback

---

### 🧪 Summary

| Case | Result |
|------|--------|
| **Perfect phase match, identical RMS, synced clock** | Still dangerous due to uncontrolled load-sharing, no trip coordination |
| **Slight phase drift (realistic)** | Circulating currents, trip or melt |
| **Moderate mismatch** | Harmonics, potential failure |
| **180° phase flip** | ***480V short***, instant breaker trip, possible explosion |

---

### 🛑 Moral of the Story

**Two 240V sources ≠ one 60A source.**  
Even if voltages match, **phase, frequency, timing, and impedance paths** must match exactly — and without a **paralleling controller**, you're playing Russian roulette with 480V.

---

Let me know if you want a simulation setup (LTSpice or Multisim style) or a classroom-safe analog demo for students to *see* why parallel sources are dangerous.

## User

Assuming a 2° phase difference, what's the impedance value created and how much heat/explosion are we talking assuming #10 wires in use (for the 30A loads on each phase.)

## Assistant

Excellent question — let’s quantify this. You’re describing a **2° phase difference between two 240 V RMS AC sources**, tied together with #10 AWG conductors (carrying up to 30 A each). We’re going to calculate:

1. The **differential voltage** across the paralleled phases (due to the 2° mismatch)  
2. The **effective impedance** of the wire  
3. The **circulating current** that flows  
4. The **power dissipation (heat)** in the wires  
5. Whether it would likely trip breakers or cause failure

---

## ⚙️ Step-by-Step Breakdown

### 1. 🌀 **Differential voltage at 2° phase shift**

Two sinusoidal waveforms:

- Source 1: \( V_1(t) = 240\sqrt{2} \sin(\omega t) \)
- Source 2: \( V_2(t) = 240\sqrt{2} \sin(\omega t + 2^\circ) \)

The instantaneous **voltage difference** is:

\[
\Delta V(t) = V_1(t) - V_2(t) = 240\sqrt{2} \left[\sin(\omega t) - \sin(\omega t + 2^\circ)\right]
\]

Using trig identity:

\[
\sin(a) - \sin(a + \theta) = -2 \sin(\theta/2) \cos(a + \theta/2)
\]

So:
\[
\Delta V(t) = -2 \cdot 240\sqrt{2} \cdot \sin(1^\circ) \cdot \cos(\omega t + 1^\circ)
\]

- \( \sin(1^\circ) \approx 0.01745 \)
- Peak differential voltage:  
  \[
  V_{\text{peak}} = 2 \cdot 240\sqrt{2} \cdot 0.01745 \approx 11.85 \text{ V peak}
  \]
- RMS differential voltage:  
  \[
  V_{\text{RMS}} = \frac{V_{\text{peak}}}{\sqrt{2}} \approx \frac{11.85}{\sqrt{2}} \approx 8.38 \text{ V RMS}
  \]

---

### 2. 📏 **Impedance of #10 wire**

We’ll use **DC resistance** since the frequency is low (60 Hz) and wire is short.

- Resistance of #10 copper = ~1.24 Ω / 1000 ft
- Assume 50 feet each way → 100 feet round trip
- Resistance \( R = 1.24 \times \frac{100}{1000} = 0.124 \,\Omega \)

Let’s assume wire is purely resistive (good first-order approximation).

---

### 3. ⚡ **Circulating current**

\[
I = \frac{V_{\text{RMS}}}{R} = \frac{8.38}{0.124} \approx 67.6 \text{ A RMS}
\]

**That’s huge.** This current flows **purely between the two sources**, not into the load.

---

### 4. 🔥 **Power dissipated (heat in wires)**

\[
P = I^2 R = (67.6)^2 \cdot 0.124 \approx 568 \text{ watts}
\]

- That’s ***568 watts of continuous heat*** dumped into the wire from just the phase mismatch.
- That’s more than a toaster. In **#10 wire**, this will **rapidly overheat**.
- **PVC insulation maxes out around 75–90°C**; you’ll hit that in ***seconds***.

---

### 5. 💥 **Trip or burn?**

- **No load is even drawing current yet**, and you’ve already:
  - Overdrawn both 30 A breakers by ~2×
  - Melted wire insulation
  - Created a **localized fire hazard**
- In reality, this kind of current ***will trip both breakers***, but not instantly. Breakers tolerate short overloads — long enough for heat damage.

If one breaker trips and the other doesn't, the full mismatch current **flows through a single wire and source**, creating ***asymmetrical backfeed*** into the other system — which could trip that source’s internal protection or cook its transformer winding.

---

## 🚨 Summary Table

| Value | Estimate |
|-------|----------|
| Phase delta | 2° |
| RMS mismatch voltage | 8.38 V |
| #10 Cu impedance (100 ft) | 0.124 Ω |
| Circulating RMS current | **67.6 A** |
| Wire heating (I²R) | **568 W** |
| Time to danger | **Seconds** |

---

### 🧠 Conclusion

Even a **tiny 2° mismatch** between "identical" 240 V sources results in:
- **Dead-short-like currents**
- **Massive heat**
- **Trip risk or fire**
- **Zero load benefit**

This isn't a theoretical concern — **this is exactly why paralleling sources without synchronizers is a code violation**.

Let me know if you want to do this same analysis for a generator + utility mismatch or inverter + inverter — each one fails in its own way.

