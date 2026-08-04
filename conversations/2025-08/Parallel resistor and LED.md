---
type: Conversation
title: "Parallel resistor and LED"
description: "If I put a 10kohm resistor in parallel with a receptacle, will I be able to get 120v at a receptacle, and then not be able to power a 120V 5w LED ligh"
resource: "688d0b0a-a0b8-8325-b6f8-fb9ae10eed7a"
timestamp: "2025-08-01T18:48:56.839Z"
tags: ["gpt-4o"]
---

# Parallel resistor and LED

## User

If I put a 10kohm resistor in parallel with a receptacle, will I be able to get 120v at a receptacle, and then not be able to power a 120V 5w LED light?

## Assistant



## Assistant

Yes, you *will* still get **120V** at the receptacle (voltage will read normally), **but** a **10kΩ resistor in parallel** will **not** provide enough current to power even a 5W LED light — and that's *exactly the point* in many diagnostic or trick-circuit scenarios.

---

### Here's why:

#### 🔌 Voltage:
Putting a resistor in **parallel** with a receptacle doesn't change the **voltage** — the receptacle will still read **120V** on a multimeter because you're reading *potential difference*, not current-carrying ability.

#### 💡 Current draw of a 5W LED:
A 120V 5W LED light draws about:

\[
I = \frac{P}{V} = \frac{5W}{120V} \approx 0.042A \text{ (or 42mA)}
\]

#### 🧮 Current through 10kΩ resistor:
Ohm’s Law gives:

\[
I = \frac{V}{R} = \frac{120V}{10,000Ω} = 0.012A = 12mA
\]

That’s *not even close* to the 42mA needed. So the LED won’t light, or might flicker extremely dimly if it tries to bootstrap itself (many LEDs need more than just current — they need power with the right waveform and inrush support).

---

### ⚠️ This kind of setup shows up in:
- Open neutral diagnostics
- Phantom voltage cases (especially with digital voltmeters)
- Miswired switch loops
- Capacitively coupled ghost voltages in conduit

---

### 🧠 Summary:

- You’ll **read 120V**: ✅
- But can’t run a 5W LED light: ❌
- Because the **parallel resistor doesn’t provide enough current**.

Let me know if you’re testing a ghost voltage or designing a trick circuit — this is textbook behavior.

## User

Can this be applied to a transformer lesson somehow? Maybe with bonding in mind?

## Assistant

Absolutely — this can become an *excellent* transformer and bonding lesson, especially for **apprentices** or **journeymen** learning why **voltage presence ≠ usable power**, and how **bonding and return paths** make the difference between a circuit that *looks* energized and one that actually *works*.

---

### 🔧 LESSON CONCEPT:  
**“Voltage Without Bonding: The Ghost Circuit”**

---

### 🧠 Learning Objectives:
- Understand how a **120V reading** can exist *without* a complete circuit path.
- See how **bonding** ensures **return current** and **functional loads**.
- Learn how transformers, secondaries, and ground reference points interact.
- Understand why **you can’t trust voltage readings alone**.

---

### 🔩 Setup:
1. **Use a small isolation transformer** (e.g., 120V → 120V).
2. On the **secondary side**, wire a receptacle.
3. Add a **10kΩ resistor** across the hot and neutral terminals.
4. Leave the **neutral unbonded** (floating) — no connection to ground.

---

### 🧪 Demonstration 1 – No Bonding:
- Multimeter reads **~120V** at the receptacle.
- Plug in a **5W LED bulb** — it won’t light.
- Explain: “We have potential difference, but no *current path*. No neutral is bonded, so current can’t return — the bulb sees voltage, but it’s like a dammed river.”

---

### 🔌 Demonstration 2 – Bond Neutral:
- Now, bond the **transformer’s secondary neutral** to ground.
- LED lights up immediately.
- Show how the *same 120V* is now capable of **doing work** because we established a **reference and return path** via bonding.

---

### 🧱 Teaching Points:
- **Voltage ≠ Power** — without current flow, the system is useless.
- **Bonding** creates a stable reference and allows **unbalanced current** to return.
- **Ghost voltage** is common with digital meters — resistive or capacitive paths can *look real*, but can’t carry load.
- This is why **test loads** (like a solenoid tester or real light bulb) matter when troubleshooting.

---

### 🧰 Real-World Tie-Ins:
- Miswired panels where the neutral isn’t bonded (in subpanels or transformers).
- Equipment failure due to open bonding.
- Why electricians test with **load** and not just a multimeter.

---

### ⚡ Final Hook:
> “This is why we don’t just test for 120V — we test for **return paths**, **bonding**, and whether the **power can do work**. A live voltage is useless without a road home.”

Let me know if you want a script, lab worksheet, or student questions based on this. It's one of the best bonding demos you can do.

