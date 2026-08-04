---
type: Conversation
title: "Heat pump efficiency explained"
description: "Explain this to me, if my heat pump won't work under 40 and it uses emergency heat, but my house is insulated well enough to stay above 68 unless the "
resource: "69325063-d0d0-8325-a566-9765d4298091"
timestamp: "2025-12-05T03:29:30.169Z"
tags: ["gpt-5-1"]
---

# Heat pump efficiency explained

## User

Explain this to me, if my heat pump won't work under 40 and it uses emergency heat, but my house is insulated well enough to stay above 68 unless the outside temperature drops below 40. What's the point?

## Assistant



## Assistant

Here’s the clean, material explanation without contractor-speak:

### **Your heat pump *does* work below 40 — it just becomes stupidly inefficient.**

A heat pump doesn’t *stop* at 40°F. It just becomes:

- **slower**
- **weaker**
- **more expensive per BTU**
- **riskier for the compressor if it runs constantly**

So what the system does is simple:

### **Below ~40°F, the heat pump could *still* keep your house above 68…  
…BUT it would have to run nonstop, burn electricity like crazy, and strain the compressor.**

That’s why manufacturers program the system to switch or supplement with **emergency/auxiliary heat**, which is:

- electrically heated coils  
- inside your air handler  
- effectively a giant toaster

This protects the compressor and keeps the house warm without running the pump into the ground.

---

## **But why does it feel pointless if insulation keeps your house above 68 until 40°F anyway?**

Because you’re thinking in terms of *temperature*.  
The system is thinking in terms of **load** and **equipment stress**.

Your home’s insulation slows heat loss — that’s great.  
But your system still has to *replace* whatever heat is leaking out.

Below 40°F:

- Outdoor coils ice more often  
- The unit must run defrost cycles  
- Performance drops sharply  
- Coefficient of performance dips under 2.0  
- The chance of wearing out the compressor spikes  

Your house might “stay” warm, but the **heat pump is working too hard** to maintain that setpoint.

---

## **So what’s the point of emergency heat?**

### **1. Protect your compressor in cold temps.**  
Running a heat pump below ~40° for long stretches is like towing a trailer up a mountain in 3rd gear.

### **2. Maintain stable indoor temperature without cycling/icing problems.**

### **3. Provide “oh sh*t backup” if the pump fails or freezes.**

### **4. Give you guaranteed heat even if defrost cycles kick in repeatedly.**

---

## **So the real answer is this:**
**Your insulation slows the need for heat.  
Emergency heat guarantees *you have* heat when the heat pump can’t efficiently supply it.**

Your insulation ≠ your heating system.  
One slows heat loss.  
The other replaces heat loss.

They cooperate, not replace each other.

---

If you want, I can break down how to force-balance your system so it uses WAY less emergency heat — like adjusting:

- droop settings  
- compressor lockout  
- aux heat lockout  
- defrost cycle frequency  
- thermostat logic  

Just tell me what thermostat/air handler you have.

## User


What does this setting do?

## Assistant

This one **does NOT control when the heat pump switches to emergency heat** and it does NOT control outdoor lockout.

This screen is **only** defining the *allowed temperature range* the thermostat will let you set manually.

### **What this setting actually does**
It limits the thermostat’s **setpoint range** during heating mode.

- The **lower bound** (45°F) = the coldest temperature the ecobee will *allow you to set your heat to*.  
  (So you can’t accidentally set heat to 40° or turn it off and freeze the pipes.)

- The **upper bound** (79°F) = the hottest temperature you can manually set your heat to.

That’s it.

### **What it does NOT affect**
❌ When AUX heat kicks in  
❌ When the heat pump shuts off  
❌ Efficiency  
❌ Compressor lockout  
❌ Defrost cycles  
❌ Balance point settings  
❌ Adaptive recovery  
❌ Heat pump vs. strip heat logic

This is basically an **“idiot guard rail”** to prevent someone from setting the thermostat to 90°, or 40°, or something stupid.

---

## If you want to control when AUX heat comes on, **that’s a different menu**:
Ecobee →  
**Settings → Installation Settings → Thresholds → Auxiliary Heat Settings**

Key settings there:

### **1. Aux Heat Max Outdoor Temp (aka “compressor lockout temp”)**
- This controls when the heat pump is *locked out* and strips take over.
- If yours is set to 40°F, that explains your situation.

### **2. Compressor Min Outdoor Temp**
- Below this temp, the heat pump shuts off to protect itself.

### **3. Aux Heat Stage 1/2 Delay**
- How long the heat pump tries before allowing electric heat to supplement.

---

## If you want, send me screenshots of your “Thresholds” page
I’ll tell you **exactly how to configure it** so:

- your heat pump does the heavy lifting  
- emergency heat only kicks in when *actually* needed  
- you save electricity  
- the house stays warm without running the strips too early  

This is one of those settings where a few degrees = hundreds of dollars saved in winter.

