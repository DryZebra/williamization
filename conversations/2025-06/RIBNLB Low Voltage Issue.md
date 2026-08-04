---
type: Conversation
title: "RIBNLB Low Voltage Issue"
description: "I have a RIBNLB fire alarm relay system and it's only outputting 14v from output the \"low limit\" output. What's going on? It's supposed to be 24v acco"
resource: "683ee4a7-d474-8003-ad2a-2832b52ed513"
timestamp: "2025-06-03T12:34:08.012Z"
tags: ["gpt-4o"]
---

# RIBNLB Low Voltage Issue

## User


I have a RIBNLB fire alarm relay system and it's only outputting 14v from output the "low limit" output. What's going on? It's supposed to be 24v according to the manual. 

![Attachment: file-3kzwZA6h1fytCwJzJRzCdH](/assets/file-3kzwZA6h1fytCwJzJRzCdH-196.jpg)


## Assistant



## Assistant

You're dealing with a **RIBNLB** relay board (by Functional Devices), which is often used in **fire/smoke integration**—especially in HVAC systems. If you're only getting **14VDC** from a terminal that's supposed to output **24VDC**, here are the likely causes and how to troubleshoot:

---

### 🔎 1. **Power Supply Issue**
- **Measure incoming voltage** to the RIBNLB board (usually 24VAC or 24VDC input depending on model).
- If the **input voltage** is low, the **output will also sag**. For example, if a 24VAC transformer is overloaded or failing, you might only get 14–16VDC after rectification.

#### ✅ Check:
- Input voltage to the board
- Transformer rating and actual output under load
- Fuse (if present)

---

### 🔎 2. **Load Dragging Voltage Down**
- The output may **read low due to excessive load** or even a **partial short** downstream.
- If you're measuring 14V with the load connected, try disconnecting the **wire going to the "LOW LIMIT" device** and remeasure.

#### ✅ Check:
- Output voltage **with the wire disconnected**
- Resistance between the "LOW LIMIT" output wire and ground
- Device at the other end of that wire (e.g., VFD input, DDC, or indicator)

---

### 🔎 3. **Relay Contact Damage or Oxidation**
- These boards often use dry contacts (SPDT). If the contacts are damaged, you might get **voltage drop across the contacts**, especially under load.

#### ✅ Check:
- Voltage **across the closed relay contact terminals** — if there's a voltage drop here (>0.5V), your relay is failing.
- Try manually triggering the relay and verify continuity.

---

### 🔎 4. **Wiring or Termination Issues**
- Loose terminal screws, corrosion, or poorly stripped wires can all create high-resistance connections and voltage drop.

#### ✅ Check:
- Reseating the wire
- Tightening the screw terminal
- Checking for oxidation or burned terminal

---

### 🔎 5. **Ground Reference Error**
- If you're measuring with a **poor or floating ground**, especially in DC circuits, it can give misleading voltages.

#### ✅ Check:
- That you're using a **common ground** for your voltmeter.
- Try measuring between the output terminal and board ground, then between the same terminal and chassis ground.

---

### Quick Diagnostic Steps:
| Step | Action |
|------|--------|
| 1 | Measure board input voltage |
| 2 | Measure output with and without load |
| 3 | Test continuity across relay contacts |
| 4 | Inspect terminal connections |
| 5 | Try a known good load |

---

Would you like to walk through these steps together with a voltmeter, or do you have any readings already?

## User

Every output is 13v to ground

## Assistant



## Assistant

If **every output on your RIBNLB is only showing ~13–14VDC to ground**, **none reaching 24V**, that strongly suggests a **systemic issue**, not just a single faulty relay or load. Here's a focused breakdown:

---

## 🔥 Your Core Issue:
**Your board is being underpowered or not powered correctly.**

---

### ✅ Step-by-Step Troubleshooting

#### **1. Check Power Input to RIBNLB**
- The RIBNLB requires either:
  - **24VAC**, or  
  - **24VDC**, depending on the model.
- Measure **across the input terminals** (not to ground).
  - You should see **~24VAC or 24VDC**.
  - If you're only seeing ~13V here, then your transformer or power source is at fault.

#### **2. Check the Label on Your RIBNLB**
- There are variants:
  - **RIBNLB** – accepts 24VAC/DC input.
  - **RIBNLB-2**, **RIBNLB-3** – may have different wiring or control voltages.
- The correct input wiring is critical — double-check whether the board is actually getting **what it expects**.

#### **3. Identify If It's Getting AC But You’re Measuring DC**
- If you’re feeding it 24VAC but your meter is on DC, it’ll often show around 13–16VDC due to half-wave rectification or internal draw.
- Switch your multimeter to **AC** and test again.

---

### 🧠 Likely Culprits
| Cause | What to Check |
|-------|----------------|
| ⚡ Undersized/Failing Transformer | Measure the transformer output **under load** and **no load** |
| ❌ Wrong Wiring (AC fed to DC-only board, or vice versa) | Confirm the model supports your input |
| 🔌 Bad Connection at Terminals | Check all input screw terminals |
| 🧃 Internal Fault (Burned diode, regulator, etc.) | If input is good but outputs are all low, board may be damaged |

---

### 📍 What's Most Likely?
If all outputs are 13V, your RIBNLB is likely only receiving ~13V on the input side. **Measure the input voltage across the incoming terminals (not to ground).** Report what you see there.

Want to send a picture of the power input wiring too? I can confirm if it’s correct.

## User

The negative terminals also get 13v to ground? It's all AC

## Assistant

Got it — **that’s the key detail**: you're feeding it **24VAC**, but both the **“hot” and “common” sides** are measuring ~13V to ground.

---

### ⚡ Here's What That Means:

**AC voltage is center-balanced**, meaning:
- In a 24VAC system (floating or center-tapped), each leg will often show **~12–14V to ground**, and **~24V across the two terminals**.
- This is **totally normal** and doesn't mean there's a problem *yet*.

But:

---

### ❗ The Real Test:
**Measure across the actual input terminals (hot to common).**
- You should get **~24VAC**.
- If you're still only getting ~13V **across the terminals**, then the transformer is weak or overloaded.

---

### ✅ Checklist:

| What to Measure | Normal Result | Problem If |
|-----------------|----------------|------------|
| **Hot to Common** (input) | ~24VAC | <18–20V → Bad transformer or load |
| **Hot to Ground** | ~12V | — |
| **Common to Ground** | ~12V | — |
| **Relay Output (NO or NC to COM)** | 0V (open) / 24V (closed) | 13V → Input sag or load issue |

---

### 🧪 Final Test:
Disconnect the **load wires** from one of the outputs (e.g., "Low Limit").  
Then:
- **Manually trigger the relay** if needed.
- Measure across the NO/COM or output terminals.

If voltage jumps to 24V or close, then:
- The **load was dragging voltage down** — possibly a short, overload, or wrong input type (e.g., trying to power a DC-only device with AC).

---

### 🔧 If Still Stuck
Send:
1. A picture showing where the transformer connects to the RIBNLB.
2. Voltage reading **across the transformer secondary**.
3. Label on your RIBNLB — confirm if it’s the **AC-compatible** model.

You're very close to solving this. Most likely it’s either:
- A **weak transformer**, or
- A **miswired input**, or
- A **low impedance device drawing too much** on the output.

## User

There's 0v across the terminals

## Assistant

Zero volts **across the input terminals** of your RIBNLB board (hot to common)? Then the issue is 100% upstream — the board isn’t getting any usable power.

---

## ✅ Summary:
> **Problem**: Your RIBNLB is outputting ~13V everywhere  
> **Diagnosis**: It’s not actually getting 24VAC — it’s getting **nothing**

---

## 🔍 What's Happening?

You’re measuring:
- ~13V **hot to ground**
- ~13V **common to ground**
- But **0V across hot to common**

This usually means:
- You're seeing **phantom or capacitive voltage** on the wires (common when they're not under load)
- The transformer **isn’t supplying voltage across the two legs**
- Or **one leg is open**, like a blown fuse or broken wire

---

## 🛠️ Next Steps:

### 1. **Trace the Source**
- Find the **transformer** that feeds this board.
- Measure **its secondary terminals** directly (not just what's arriving at the board).
  - You should see **24–28VAC** there.
- If you do → the wiring between the transformer and RIBNLB is broken.
- If you don’t → transformer is **dead**, **switched off**, or **fused**.

---

### 2. **Check for Hidden Disconnects**
- Look for:
  - Tripped circuit breakers
  - Blown inline fuses
  - Loose terminal blocks or spade connections
  - Control board switches or jumpers

---

### 3. **Inspect Wire Path**
- Confirm the wire from transformer is really reaching the correct RIBNLB terminals.
  - It’s easy to land on the wrong side of a terminal block.
- Use continuity test (with power off!) from transformer to board.

---

### 🧠 Final Clue:
That weird 13V is likely just **induced voltage** — floating on the line due to nearby energized wires. It **looks real**, but the second you load it, it disappears. That’s why your output is limp, and why your measurements don’t add up across terminals.

---

Would you like to identify the transformer and check its output directly next? Feel free to send a pic of it and I’ll help trace it.

