---
type: Conversation
title: "Lutron controller troubleshooting 277V"
description: "Can you tell me what model this is of lutron lighting controller? I've got 277v at source but the light isn't on and it's not working."
resource: "683b0f0a-3ca8-8003-aa05-51e2922b943e"
timestamp: "2025-05-31T14:44:52.075Z"
tags: ["gpt-4o"]
---

# Lutron controller troubleshooting 277V

## User


Can you tell me what model this is of lutron lighting controller? I've got 277v at source but the light isn't on and it's not working. 

![Attachment: file-5ezyk4btFbJpjgU6ojAf3R](/assets/file-5ezyk4btFbJpjgU6ojAf3R-97.jpg)


## Assistant



## Assistant

This is a **Lutron GRX-CI-RS232** or **Lutron GP (Grafik Eye) series** controller enclosure, commonly used in **Lutron Grafik Eye QS** or **Lutron GRAFIK 4000** systems. The exact model of the control board inside the enclosure is not printed visibly in the photo, but here’s how you can narrow it down:

---

### 🔍 Based on the visible information:
- The label says **"LUTRON TYPE 1 ENCLOSURE"** and **"UL LISTED Industrial Control Panel Enclosure"**.
- The board has multiple zones (marked ZONE 1, ZONE 2, etc.) with relays, which suggests it's a **GRX-RPM-4U** or **GP panel** zone controller.
- It has a Lutron-style terminal block and low-voltage control terminals.

---

### ⚠️ Troubleshooting your issue:
You said:
> “I've got 277V at source but the light isn't on and it's not working.”

Here are steps to check:

1. **Verify Input Power:**
   - Ensure **277V is present at the LINE terminal** on the relay board using a multimeter.
   - Check **neutral and ground continuity** if applicable.

2. **Check Low Voltage Control Signal:**
   - This unit relies on **control wiring** (likely from a processor or keypad).
   - If there's no control signal coming in (from a Lutron processor like a GP or QS unit), the relays will not activate.

3. **Look for status LEDs:**
   - Each zone relay usually has an LED indicating activation. If none are on, either:
     - The unit isn’t powered properly.
     - Or it’s not receiving control input.

4. **Test Relay Manually:**
   - If you're familiar with the device, some have **manual test/program buttons** at the bottom row labeled "Input / Option / Program." You might be able to **force a relay ON** for test purposes using those.

5. **Double check circuit labeling and wire terminations:**
   - Especially with 277V, double-check you’re not on an unconnected zone or a miswired terminal.

---

### How to find the model number:
Look at:
- The **side or inside of the door** of the panel.
- Or on the **PCB silkscreen** for a part number like `RPM-4U`, `GP4`, `QS`, etc.

---

If you can provide:
- A close-up photo of the **label on the side of the board**.
- Or the **Lutron processor/control module** that sends signals to this board,

I can identify it exactly and help further troubleshoot.

## User

It has a blue cover

## Assistant

Thank you — that helps a lot.

A **Lutron lighting controller with a blue cover** on the relay modules is most likely from the **Lutron GP (GRAFIK Power) Series**, specifically one of these:

---

### 🔷 **Model: Lutron GP Panel with RPM-4U Modules**

- **GP panels** are designed for lighting control in commercial environments.
- They use **RPM (Remote Power Module)** relays like the **RPM-4U** (4-zone universal relay).
- The **blue plastic cover** is a distinctive feature of **RPM series** modules.

---

### 📋 From what your image shows:
- 4 blue-covered relays labeled Zone 1 to Zone 4 → **RPM-4U**
- Labeled terminals and option/program buttons → typical of GP panel interface boards.
- Enclosure with UL listing, industrial style → matches GP system.

---

### ✅ So the full system you're looking at is likely:
> **Lutron GP Panel** with **RPM-4U** modules, controlled via a GRAFIK Eye 4000 or QS processor.

---

### ⚠️ If 277V is present but lights aren't turning on:
Here’s a specific checklist for this setup:

1. **Verify Power to Relay Board:**
   - Measure voltage **line to neutral**, **line to ground**, and **neutral to ground**.
   - Confirm the control board’s transformer is operational (small black/blue module on the left side).

2. **Relay Status LEDs:**
   - Each blue-covered module has **tiny LEDs**—are any lit when the system should be on?

3. **Test Button Activation:**
   - On the bottom row of the control board, **press and hold the "Input" or "Program" button** for a zone. Many GP panels let you toggle a relay manually this way.

4. **Check Communication Cable:**
   - The panel must receive low-voltage commands from a controller via a **GRX link** or **QS link** (twisted pair, usually blue/white and blue).

5. **Look for Fault LEDs:**
   - Some models have a fault indicator near the transformer—check for blinking red lights.

---

### Want to confirm exactly?
If you can send a picture of the **blue label on the side of the relays**, I can give you the exact model number.

Would you like a wiring diagram or test procedure for GP panels with RPM-4U modules?

## User

We found it. The pre installed emergency power jumper that pushes all attached lights to max and ignores dim input

## Assistant

Ah — that makes perfect sense. You're dealing with a **Lutron GP panel (or RPM module)** wired for **emergency lighting**, and that jumper is the culprit.

---

### 🔧 What the Emergency Jumper Does:
- When the **emergency power sense input** is active or the jumper is in place, the system **forces all zones to full ON**, bypassing any dimming or control signals.
- This is a **life safety feature**: in a power loss scenario (with generator/emergency backup power), the lights go full bright.

---

### ✅ What You Likely Saw:
- **277V present**, but no dimming → jumper tells the panel it’s in emergency mode.
- **No control via QS/GRX link** → the panel ignores them in this mode.

---

### 🧠 Fix:
- **Remove the emergency jumper** (usually a small plastic shunt on a terminal block labeled EMERGENCY or EDR).
- Confirm that the **emergency input terminals are either open or properly controlled** by a real emergency circuit.
- Once cleared, the controller will resume normal operation and obey dimming levels.

---

### ⚠️ Reminder:
If this panel *is* wired to emergency power, make sure you’re still compliant with **local life safety codes** before disabling that jumper. In some jurisdictions, it must remain in place unless you have UL924-listed override equipment or a UL-approved method of detecting normal vs. emergency power.

---

Nice work tracking that down — it's a sneaky one if you're not expecting it. Want me to sketch a quick diagram of how this jumper works in the RPM context?

