---
type: Conversation
title: "Line side inquiry"
description: "What does it mean if a transformer has 0 ohms continuity on the load side?"
resource: "67d19513-89bc-8003-8e80-d59219df800d"
timestamp: "2025-03-12T14:12:40.263Z"
tags: ["gpt-4o"]
---

# Line side inquiry

## User

What does it mean if a transformer has 0 ohms continuity on the load side?

## Assistant



## Assistant

If a transformer shows **0 ohms** continuity on the **load side**, it typically indicates a **short circuit** in the secondary winding. This could be caused by:

1. **A direct short between secondary windings** – The insulation between windings has failed, creating a direct electrical connection.
2. **A shorted output connection** – The wiring or load connected to the transformer has a short.
3. **A failed component in the circuit** – If the transformer is connected to a circuit, a downstream component (such as a diode, capacitor, or load device) could be shorted.
4. **Burned or melted windings** – If the transformer has overheated, the wire insulation could have melted, causing the windings to make direct contact.
5. **Testing method

## User

What about in the line side?

## Assistant



## User

Continue

## Assistant

If a transformer shows **0 ohms** continuity on the **line side** (primary winding), this could indicate several potential issues:

### **Possible Causes of 0 Ohms on the Line Side**
1. **Primary winding shorted** – The insulation between the windings has failed, causing the turns to short together. This would likely result in excessive current draw and possible overheating.
2. **Internal short to ground** – If the primary winding is shorted to the transformer core, it could create a dangerous fault condition.
3. **Damaged winding connections** – A manufacturing defect or physical damage might cause the windings to touch, creating a direct short.
4. **Testing Error** – If you're measuring continuity with a multimeter, the winding resistance should be **low but not zero** (usually a few ohms). If you see **0 ohms**, check the meter's probes, battery, or use a more precise resistance measurement setting.
5. **Magnetic Saturation Effects (Unlikely with a Multimeter)** – If you're testing with an energized circuit, an inrush condition could momentarily appear as very low resistance.

### **What It Should Be**
- A healthy primary winding should show some resistance, typically in the **ohms to tens of ohms** range, depending on the transformer size.
- If you're seeing **0 ohms**, it strongly suggests a **short circuit**, and energizing the transformer in this condition could lead to a blown fuse, tripped breaker, or catastrophic failure.

Would you like help troubleshooting this further?

## User

So if I have continuity on my transformer, it's likely shorted and bad? If I'm taking a continuity reading in the line side of an AC transformer, what kind of reading SHOULD I see?

## Assistant

### **Does Continuity on a Transformer Mean It's Bad?**
Not necessarily. A transformer is **just a coil of wire**, so you should expect some continuity (a closed circuit) when testing the **primary (line side)** and **secondary (load side)** windings. However, if your meter shows **0 ohms** (a dead short), that **could indicate a problem**.

---

### **What Should You See When Testing the Line Side?**
- **A healthy transformer** should show **some resistance**, typically in the range of:
  - **Small transformers**: A few ohms (1–50Ω)
  - **Larger transformers**: Tens to hundreds of ohms (50Ω–500Ω)
  - **High-voltage transformers**: Hundreds to thousands of ohms (500Ω+)
- **If your meter beeps for continuity but also shows a resistance value**, that's normal.

---

### **What If You Get 0 Ohms or a Beep with No Resistance Reading?**
- If your meter shows **0 ohms or very close to it** (like 0.1Ω), that could mean:
  - **Shorted primary winding** (bad transformer)
  - **Shorted turns inside the winding** (will cause overheating and high current draw)
  - **Incorrect meter setting** (some meters beep for low resistance but still have a measurable value)
- **Check by using the resistance (Ω) setting instead of just continuity.**

---

### **How to Properly Test the Transformer?**
1. **Set your multimeter to Ohms (Ω), not just continuity.**
2. **Measure across the primary winding (line side).**
   - Expect some resistance (1Ω to 1000Ω depending on transformer size).
   - If it reads **0Ω or very close**, the winding is likely shorted.
3. **Measure across the secondary winding (load side).**
   - This should also show some resistance, typically lower than the primary.
   - If it reads **0Ω**, there may be a short.
4. **Check for shorts to ground.**
   - Place one probe on the core or frame and the other on each winding.
   - **There should be NO continuity.** If you get a reading, there’s an internal short.

---

### **Summary**
- **Continuity itself is normal** for a transformer.
- **0Ω on the primary is bad** → Possible shorted winding.
- **Some resistance (not zero) is expected** → A good transformer should show **a few ohms to hundreds of ohms** depending on size.
- **Use the Ohms setting, not just continuity** → Beeping alone doesn’t confirm a short.

Would you like help determining the expected resistance for a specific transformer?

## User


Is this right?

![Attachment: file-MQqDyGnVSzdg36xA6i3NmC](/assets/file-MQqDyGnVSzdg36xA6i3NmC-1000006428.jpg)


## Assistant

Yes, based on the image, your multimeter is reading **0 ohms** (0Ω) on the primary (line side) of the transformer. 

### **What This Means**
- **0Ω indicates a short circuit.** This is not normal for a transformer’s primary winding, which should have **some resistance** (typically a few ohms to hundreds of ohms, depending on size).
- **Possible issues:**
  1. **Internal short in the winding** – The insulation may have failed.
  2. **Shorted wiring or terminals** – Double-check for any physical short across the terminals.
  3. **Testing on a connected circuit** – Ensure the transformer is disconnected from the rest of

## User

Well it's actually reading 3.0 ohms

## Assistant



## User

Well it's actually reading 3.0 ohms

## Assistant



