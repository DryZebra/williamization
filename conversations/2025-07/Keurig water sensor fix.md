---
type: Conversation
title: "Keurig water sensor fix"
description: "I have an older Keurig and the fill water light is always on. I tried just shorting the switch by cutting the wires and tying them together. It didn't"
resource: "68790af4-7820-8003-aad9-1b22c4c28ab6"
timestamp: "2025-07-17T14:48:22.790Z"
tags: ["gpt-4o"]
---

# Keurig water sensor fix

## User

I have an older Keurig and the fill water light is always on. I tried just shorting the switch by cutting the wires and tying them together. It didn't work. But when I short the two terminals with my screw driver, it magically works. 

My theory is that there's a some resistance somewhere needed. 

## Assistant



## Assistant

You're almost certainly correct that the Keurig's water level sensor circuit expects a **certain resistance** (or voltage drop), not just a dead short.

Here’s what’s likely going on and how you can fix it:

---

### 🔧 The Technical Explanation:

Most older Keurigs use a **conductivity-based water level sensor**:
- It measures the **resistance** (or conductance) between two metal probes.
- If there's water in the reservoir, the water itself conducts a tiny current between the probes.
- If you cut the wires and short them directly, you're giving **zero resistance**—which may be outside the expected operating range, so the board assumes there's an error or no water.
- But when you touch the terminals with a screwdriver, your body and the screwdriver introduce a small resistance or capacitance, tricking the circuit into reading it as valid.

---

### ✅ The Fix:

You can simulate the correct sensor reading with a **resistor**.

1. **Use a resistor in place of the switch**.
   - Try something in the **10kΩ to 100kΩ** range as a starting point.
   - You can test different values by temporarily bridging the wires with resistors and seeing when the light turns off.

2. **Wiring tip**: Strip the two wires you previously tied together and insert the resistor between them.

3. **Secure it**: Use electrical tape or heat shrink tubing once you’ve found the right resistance.

---

### 🧪 How to Find the Right Resistance:

- Start with a **10kΩ resistor**.
- If that doesn’t work, try **higher values** (e.g., 22k, 47k, 100k).
- The goal is to simulate the resistance of water—not a short circuit.

---

If it works, you've just bypassed a failed water level sensor with about 10 cents in parts.

Let me know your model number if you'd like help finding a schematic or exact spec.

