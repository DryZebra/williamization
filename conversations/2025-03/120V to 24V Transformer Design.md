---
type: Conversation
title: "120V to 24V Transformer Design"
description: "If I'm trying to make a 120v to 24v ac transformer in this theory simulator, what do I need to input for the values of resistance on each side and hen"
resource: "67d58eab-3d30-8003-98ef-c63205e4cd78"
timestamp: "2025-03-15T14:40:42.857Z"
tags: ["gpt-4o"]
---

# 120V to 24V Transformer Design

## User


If I'm trying to make a 120v to 24v ac transformer in this theory simulator, what do I need to input for the values of resistance on each side and henries for the primary? I want to power an LED. 

[Attachment: file-BSFHGQCWvSaDSuwdS8RXBh](/assets/file-BSFHGQCWvSaDSuwdS8RXBh-0981f9ed-a93d-495f-9fcd-031efcdb2d646393580399257273495)


## Assistant



## Assistant

To design a **120V to 24V AC transformer** in your circuit simulator, you need to adjust the following parameters:

### **1. Turns Ratio (N)**
The turns ratio (N) is calculated as:
\[
N = \frac{V_{\text{primary}}}{V_{\text{secondary}}} = \frac{120V}{24V} = 5
\]
So, set **N = 5** in the transformer settings.

---

### **2. Inductance Values**
For an ideal transformer, inductance should be chosen based on the impedance requirements of your circuit. Since you're powering an **LED**, the inductance values don't need to be extremely high, but they should be sufficient to ensure good coupling.

- **Primary Inductance (L_PRI)**: A good starting point is **10 H to 100 H** for 60Hz AC mains operation.
- **Secondary Inductance (L_SEC)**: Since the turns ratio is **5**, the secondary inductance should be:
  \[
  L_{\text{sec}} = \frac{L_{\text{pri}}}{N^2} = \frac{10H}{25} = 0.4H
  \]
  So, if **L_PRI = 10H**, set **L_SEC = 0.4H**.

---

### **3. Resistance Values**
The resistance values represent the winding resistance of the transformer. They should be small but realistic to model real-world losses.

- **Primary Resistance (R_PRI):** **0.5Ω to 10Ω** (depends on wire gauge and winding length)
- **Secondary Resistance (R_SEC):** Since resistance scales with turns squared,
  \[
  R_{\text{sec}} = \frac{R_{\text{pri}}}{N^2}
  \]
  If **R_PRI = 1Ω**, then **R_SEC = 1Ω / 25 = 0.04Ω**.

---

### **Final Values to Input**
- **Turns Ratio (N):** **5**
- **L_PRI:** **10H** (or try 50H for better coupling)
- **L_SEC:** **0.4H** (or try 2H if L_PRI is 50H)
- **R_PRI:** **1Ω** (adjustable from 0.5Ω to 10Ω)
- **R_SEC:** **0.04Ω** (scales with primary resistance)

This setup should work for a theoretical transformer simulation to step down **120V AC to 24V AC**. Since you're powering an LED, make sure to rectify and regulate the output voltage accordingly!

## User


I'm trying to setup my lab but I need this voltage source to be compatible with the transformer to power the 24v LED. What inputs do I put here?

![Attachment: file-C27VBvyFibDGFUmPxqyn6e](/assets/file-C27VBvyFibDGFUmPxqyn6e-1000006447.jpg)


## Assistant

To ensure that your **voltage source** is compatible with the **transformer** for stepping down to **24V AC** and ultimately powering your LED, follow these settings:

### **Voltage Source Parameters**
1. **Amplitude**: **120V RMS** is the standard for AC mains, but **this setting may be using peak voltage instead of RMS**.  
   - If it takes **RMS voltage**, leave it at **120V**.  
   - If it takes **peak voltage**, set it to **~170V**, because:
     \[
     V_{\text{peak}} = V_{\text{RMS}} \times \sqrt{2} \approx 120V \times 1.414 \approx 170V
     \]
   - **Check the simulator's documentation** to confirm whether it expects RMS or peak voltage.

2. **Frequency**: **60 Hz** (correct for North American AC power).  

3. **DC Offset**: **0V** (AC power has no DC offset).  

4. **Phase**:  
   - Set this to **0°** if this is your main AC source.  
   - If you have multiple sources, adjust accordingly for phase synchronization. **180° is unnecessary unless creating a second out-of-phase source**.

5. **Waveform Shape**: **Sine** (correct, as AC mains is a sinusoidal waveform).

---

### **Additional Considerations**
- **Transformer Compatibility:** Ensure the transformer is correctly set with a **5:1 turns ratio** to step down from **120V AC to 24V AC**.
- **LED Powering:** If your LED requires DC, you need a **rectifier** and a **filter capacitor** to convert **24V AC to ~24V DC**.
- **LED Current Limiting:** LEDs require **a resistor or a proper driver** to prevent excessive current.

Would you like help with **designing the rectifier circuit** for your LED?

