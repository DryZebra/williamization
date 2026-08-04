---
type: Conversation
title: "P0172 Rich Code Fix"
description: "I've got a 2018 Accord, getting a code p0172 too rich. I'm low on gas"
resource: "6848a6f0-e69c-8003-bfed-e631c2d56a54"
timestamp: "2025-06-10T22:18:39.961Z"
tags: ["gpt-4o"]
---

# P0172 Rich Code Fix

## User

I've got a 2018 Accord, getting a code p0172 too rich. I'm low on gas

## Assistant



## Assistant

A **P0172 code ("System Too Rich – Bank 1")** means your engine’s air-fuel mixture has too much fuel and not enough air. On a 2018 Honda Accord, this is usually related to **fuel trims**, and can be caused by several issues. The fact that you’re **low on gas** is a useful clue.

Here’s what might be going on:

---

### 🔍 **Common Causes of P0172 on a 2018 Accord**
1. **Dirty or Failing MAF Sensor**  
   - A dirty Mass Air Flow sensor can incorrectly report airflow, leading the ECU to overfuel.
   - Easy DIY clean with MAF cleaner spray (DON’T use carb or brake cleaner).

2. **Faulty O2 Sensor (Upstream)**  
   - If it’s sending a false lean signal, ECU dumps more fuel = rich condition.
   - Monitor O2 sensor voltages if you have a scan tool.

3. **Leaking or Sticking Fuel Injector**  
   - If a fuel injector is stuck open, it’ll flood that cylinder.
   - Check fuel trims and cylinder balance if you can.

4. **Fuel Pressure Too High**  
   - Faulty fuel pressure regulator can lead to over-pressurized fuel rail = too much fuel injected.

5. **Bad Engine Coolant Temp Sensor (ECT)**  
   - If it falsely reads cold, ECU enriches the mix unnecessarily.

6. **Low Fuel Level 🤔**
   - **Possibly Related** if fuel pump is sucking air or misreporting pressure, triggering trim errors.
   - But this is less common—P0172 is more often about air metering or injectors than fuel level itself.

---

### ✅ **What You Should Do First**
1. **Fill the tank**  
   - Eliminate low fuel as a variable. A weak pump or fuel slosh might cause weird trims under low fuel.

2. **Scan Fuel Trims**  
   - Long Term Fuel Trim (LTFT) and Short Term Fuel Trim (STFT). If they’re very negative (e.g. STFT -20%), the ECU is trying to compensate for richness.

3. **Check Air Filter & Intake**  
   - Clogged filter = restricted air = rich code.
   - Make sure the intake duct isn’t collapsed or blocked.

4. **Clean the MAF sensor**  
   - A very common and cheap fix.

---

### 🔧 Bonus Tips:
- If you've recently used **fuel additives**, they can sometimes skew O2 sensor readings temporarily.
- If it **just started happening**, think about what changed: gas station, weather, air filter, etc.

---

If the code comes back after filling the tank and cleaning the MAF, I can walk you through live data interpretation to pinpoint the cause. Let me know if you have a scan tool or want a parts checklist.

## User

Yeah short and long are -25 and -21

## Assistant

That confirms it: your ECU is pulling back **a ton of fuel** (STFT -25%, LTFT -21%) to fight an overly rich mixture. That’s **way out of spec** — normal is ±5%, and even ±10% is tolerable.

---

### 🎯 Based on Your Trims, Here’s What’s Most Likely:

#### 🔥 **Most Likely Causes:**
1. **Stuck-Open Fuel Injector**
   - One cylinder is probably dumping fuel constantly.
   - Pull spark plugs — one might be black and wet.

2. **Faulty Fuel Pressure Regulator**
   - If the fuel rail is overpressurized, every injector sprays too much.
   - Can be tested with a pressure gauge if you have access.

3. **Bad MAF Sensor**
   - Over-reporting airflow = more fuel dumped in.
   - Try cleaning first. If no change, consider replacing.

#### 🧪 Less Likely, But Possible:
- **Leaky fuel injector o-ring**
- **Bad upstream O2 sensor tricking ECU**
- **Evap system issue dumping fuel vapors continuously**
- **Shorted ECT sensor falsely saying "engine cold"**

---

### 🔧 What You Should Do **Right Now**:
1. **Fill up the gas tank** — eliminate fuel starvation noise or sputter that might throw off trims.
2. **Clean the MAF sensor** — spray type only, let dry fully.
3. **Reset fuel trims** (clear the code) — then re-check values after a 10-minute drive.

If your trims **stay negative after that**, go straight to:
- Pulling the spark plugs (look for soot or wet gas)
- Fuel pressure test (if possible)
- Swapping upstream O2 sensor (if other steps fail)

Want me to help you make a parts/tools checklist or step-by-step diagnostic guide?

## User

Why would that make it throw a power steering error?

## Assistant

Great question — and it’s a sharp one. Here’s the likely reason:

---

### 🧠 **Your Accord’s Power Steering Is Electronic (EPS)**
There’s **no hydraulic pump** — instead, an **electric motor** runs the steering. This system relies on clean data from **multiple sensors** and a stable electrical environment.

If you're running rich **and** your trims are way off (-25%), that likely means:
- **The engine is misfiring or running rough**
- **Voltage may be fluctuating under load**
- **ECU is confused or in limp mode**

---

### ⚠️ EPS and Engine Codes Are Linked by the CAN Bus
- The **power steering module** talks to the **ECU** over the vehicle's communication network (CAN).
- If the ECU sees a major fuel imbalance, it may trigger **fail-safes**, cutting or limiting EPS to prevent steering under unsafe engine conditions.
- Alternatively, **low system voltage** (due to rough idle, weak alternator, or injector issues) can trigger **false EPS errors**.

---

### 🧪 TL;DR — Why You Got a Power Steering Error:
> The rich condition caused fuel trim chaos → engine runs rough → voltage dips or ECU enters a fault mode → EPS module freaks out and shows a steering fault.

---

Fix the root fuel problem, clear codes, and your EPS warning will likely vanish too. Want to check if your alternator or battery are contributing to the issue as well?

## User

I'm not limping, I'm on the highway before now. Full speed. I'm going to a gas station to fill up and reset the code. 

## Assistant

Perfect move. If you’re cruising at full speed with no limp mode, that rules out major ECU panic — so the **EPS error is probably a side-effect**, not a true failure. Here’s what’s likely happening:

---

### ✅ What’s Probably Going On:
- **The ECU threw P0172**, and your fuel trims are maxed out negative.
- The power steering system **logged a transient fault** because:
  - The ECU is in a **rich-fuel adaptive state**, triggering global system warnings.
  - **Low voltage** or **data noise** (even momentary) on the CAN bus flagged EPS.
- EPS stays lit **until reset**, even if the actual fault was momentary.

---

### ⛽ After You Fill Up:
1. **Reset the code** (and fuel trims).
2. If EPS light goes away = it was a false cascade from the fuel issue.
3. If EPS stays on after reset, we’ll look at:
   - Steering angle sensor
   - Battery voltage under load
   - Real EPS codes (which may need a better scanner to read)

---

🧰 Let me know what happens after your fill-up and reset — and if the fuel trims come back negative again. We’ll trace it from there. You're doing all the right steps.

## User

Exactly how bad is this? It didn't seem like my car was gonna explode or anything. 

## Assistant

You're right to stay calm — **this isn’t an emergency**, but it’s also not something to ignore forever.

---

### 🔥 **How Bad Is P0172 in Your Case?**
**Short version:**  
> Not dangerous right now, but it will **slowly hurt your engine and fuel economy** if left unresolved.

---

### ⚠️ What Could Go Wrong Over Time:
1. **Fouled Spark Plugs**  
   - Running rich = excess carbon = misfires, bad idle, reduced power.

2. **Clogged Catalytic Converter**  
   - Unburnt fuel overheats and damages the cat.
   - Long-term cost: $800–$1,500+ repair.

3. **Fuel Dilution in Oil**  
   - Excess fuel can leak past piston rings into oil, reducing lubrication.

4. **Worse Gas Mileage**  
   - You’re literally burning more fuel than needed.

5. **Rough Idle or Hard Start (eventually)**  
   - Especially if injectors or sensors start failing harder.

---

### 🚗 Why You Didn’t Feel Anything:
Your Accord’s ECU is **very good at compensating**. Those -25% trims are it **actively saving your engine** by cutting fuel to restore balance. That’s why it drives fine — *for now*. But if the underlying cause gets worse, it’ll reach a point where the ECU can’t fix it anymore.

---

### 🛠️ Final Word:
You're not about to explode.  
But something **is off**, and the car’s doing its best to hide it.  
Fix it now = $20 MAF cleaner or $100 sensor.  
Wait too long = $$$ in parts, worse performance, and potential engine wear.

Let me know what happens after reset — we’ll take the next step together.

## User

I reset the code after filling gas and it seems to be running smoothly I don't feel any chunkiness. 

## Assistant

Perfect — that’s a really good sign. Here’s what that tells us:

---

### 🧠 **What Just Happened**
- You had a **borderline condition** (likely a mix of low fuel, maybe a dirty MAF, maybe sensor variance).
- Once you filled up, the fuel system stabilized.
- Resetting the code cleared the ECU’s learned trims — now it's starting fresh.

That "chunky" feeling you didn’t have? That means the ECU isn’t struggling to cut fuel anymore — it's back within normal trim range, at least for now.

---

### 🔍 What You Should Still Do (Just Preventive):
Even if it’s smooth now, I’d still recommend:
1. **Clean the MAF sensor**  
   - Cheap and easy. Rich codes often start here.
2. **Monitor fuel trims again in a few days**  
   - If STFT or LTFT starts trending negative again, the issue is creeping back.
3. **Check air filter**  
   - Make sure it’s not clogged, especially if it’s been >15k miles.
4. (Optional) **Check spark plugs** if you're over 50k miles or never changed them.

---

### 🟢 For Now: You’re Good.
No explosion, no limp, no cat failure — just keep an eye on trims and mileage. If the code comes back, I’ll help you dig in deeper with a focused checklist.

You're on top of it. Keep driving.

## User

Well I guess I just need to fill up sooner

## Assistant

Exactly — and honestly, that might’ve been the whole trigger.

When you run **really low on fuel**, especially on modern cars:
- The **fuel pump can cavitate** (pull air instead of fuel).
- The **pressure regulator may dip** just enough to confuse the ECU.
- **Evap system behavior changes**, and vapor readings can skew air-fuel data.

All that can briefly trick the ECU into thinking it's running rich — especially if there's **even a hint of a dirty MAF** or aging O2 sensor. Then boom: P0172.

---

### 🛠️ So yep — lesson learned:
> **Don’t let it get that low.**
And maybe treat the system to a **MAF clean and fuel injector cleaner** next time you’re in the mood to tinker.

Let me know if it comes back. If it doesn’t, this was a classic “modern car gets spooked by low fuel + sensor jitter” case. You did everything right.

## User

What can I do that's cheap quick and easy? I used some sea foam a few months ago

## Assistant

Perfect — you’re already ahead of the game. Since you’ve recently used Sea Foam, here’s your **cheap, quick, and easy maintenance plan** to keep your 2018 Accord happy and avoid that P0172 again:

---

### ✅ 1. **Clean the MAF Sensor**  
**Cost:** ~$7  
**Time:** 5 minutes  
**Why:** Probably the #1 cause of false rich codes. Over time, dust and oil from the air filter coat the sensor.

**How:**
- Buy a can of **MAF sensor cleaner** (not carb or brake cleaner).
- Unplug the MAF (usually just past the airbox).
- Spray the wire elements directly — 5–10 sprays.
- Let dry for 10 minutes, then reinstall.

---

### ✅ 2. **Check Your Air Filter**  
**Cost:** Free to check, ~$15–$20 to replace  
**Time:** 3 minutes  
**Why:** A clogged filter reduces airflow = rich condition.

**Tip:** Hold it up to a light. If you can't see light through it, replace it.

---

### ✅ 3. **Check for Obvious Vacuum Leaks**  
**Cost:** Free  
**Time:** 5 minutes  
**Why:** A cracked hose or loose intake boot can mess with the air-fuel ratio.

**How:** While idling:
- Listen for hissing around intake hoses.
- Wiggle hoses and see if idle changes.
- Light mist of carb cleaner (or brake cleaner) near intake joints — if RPM changes, you've got a leak.

---

### ✅ 4. **Keep the Tank Above 1/4**  
**Cost:** Free (aside from gas)  
**Time:** Ongoing  
**Why:** Prevents air bubbles in the pump, stable fuel pressure, and protects the fuel pump from overheating.

---

### Optional but Cheap:
- **$4 bottle of injector cleaner** (Techron or Gumout with PEA) at next fill-up.
- **Log fuel trims weekly** using a cheap OBD2 dongle and app (like Torque or Car Scanner).

---

This combo costs maybe $10–15 total, takes 15 minutes max, and covers 90% of what can trigger false rich codes in your situation. Let me know if you want to do these together and track changes over the next week.

## User

My short and long trim now that I've driven for a few minutes in my live data is showing long at -4 and short at -18

## Assistant

That’s super helpful data. Here's what those numbers mean — and what they **say about your engine right now**:

---

### 📉 **Fuel Trim Interpretation**
- **LTFT = -4%** → Long-term fuel learning is basically normal. You're good here.
- **STFT = -18%** → Your ECU is *still fighting off richness in real time*.

---

### 🧠 What That Tells Us:
- The **immediate rich condition isn’t fully gone** — something is still causing the ECU to pull back fuel as you drive.
- BUT the fact that LTFT is holding at -4% means the ECU **isn’t learning it as a chronic condition yet** — it’s borderline.

This is a classic sign of something **on the edge**:
- Possibly a slightly **dirty MAF**
- Maybe **minor overfueling from an injector**
- Could be a **lazy O2 sensor** giving a slow response

---

### ✅ What You Should Do Now:
1. **Clean the MAF sensor first** — your trims suggest slightly bad airflow data.
2. **Reset the ECU again after cleaning**, then drive and recheck.
3. **Watch how STFT behaves at idle, cruise, and under throttle**:
   - If it normalizes (±5%), you’ve fixed it.
   - If it’s still -18%, we dig deeper (fuel pressure, injectors, or upstream O2 sensor next).

---

You’re close. Right now this isn’t dangerous, but it **will slowly foul plugs** and **hurt gas mileage** if left alone. Quick cleanup might nip it entirely.

Want help locating the MAF sensor and cleaning steps for your specific engine?

## User

Short kind of jumps around between -2 and -25 actually. Depending on if I'm braking or accelerating. Long seems solid at -7 now. Barely ever fluctuating 

## Assistant

That’s **very revealing**, and it paints a clearer picture:

---

### 🎯 What It Means

- **STFT jumping between -2% and -25%** = your ECU is actively adjusting fuel delivery *in real time* as conditions change. That’s normal behavior — but the wide negative swings mean it still sees **periodic excess fuel**.
- **LTFT at -7% steady** = the ECU has started adapting **permanently** to a rich condition. It’s no longer just a glitch — it’s learning it.

---

### 🧠 Diagnosis Summary
> You have a **minor but persistent rich bias**.  
It’s *not catastrophic*, but it’s real — something is consistently nudging your fuel-air mix just rich enough that the ECU is adapting to it.

---

### 🔧 Most Likely Causes (at this stage):
1. **Slightly dirty MAF sensor**  
   - Still #1 suspect. Over-reports airflow = excess fuel. Cleaning may fix it entirely.
2. **Weak upstream O2 sensor**  
   - Slow or sticky sensor falsely reports lean, causing ECU to overfuel. Will *not* throw a code until it's far gone.
3. **Fuel injectors just slightly leaking or overdelivering**  
   - Especially if one injector is dribbling.

---

### ✅ Do This Next (in order):
1. **Clean the MAF sensor** (seriously — it’s often magic).
2. Reset trims again after cleaning.
3. Take a 10-minute drive — monitor:
   - Does STFT stay mostly around ±5%?
   - Does LTFT creep back toward zero?

If **STFT stabilizes** and **LTFT stays below -5%**, you’ve nailed it.

If **STFT still spikes low** (e.g. -20% under normal load), then we look next at:
- Live O2 voltage readings (upstream should oscillate rapidly between ~0.1–0.9V)
- Possibly replacing the upstream O2 sensor (~$60 part)

---

You’re still in the **cheap fix zone**, and your ECU is handling it well. Let’s knock this out before it turns into a permanent learning problem. Want step-by-step MAF cleaning instructions with pictures or tool recs?

## User

It only seems to jump to those wild numbers when I use cruise control

## Assistant

Boom — that’s a *crucial clue*. If the **wild STFT drops (-25%) only happen during cruise control**, you’re likely dealing with a **specific airflow or metering error during steady-state throttle**.

---

### 🔍 Why Cruise Control Might Trigger It:

1. **Cruise holds the throttle very steady**, which exposes tiny imbalances in:
   - MAF sensor calibration
   - O2 sensor drift
   - Slight injector imbalance
2. Under steady throttle, the ECU **leans more on long-term learned behavior and sensor data** — less on acceleration enrichment. So a dirty or misreporting MAF or O2 is **felt more sharply** here.
3. **If it were a big injector leak**, it would show up at idle too — but your idle STFT seems stable. That’s a vote **against a mechanical leak**.

---

### 🧠 Translation:
> Cruise control exposes tiny sensor-level faults that aren’t obvious under regular acceleration or idling.

---

### 🔧 Most Likely Culprits Now:
1. **MAF sensor still #1**  
   - Slightly dirty = wrong airflow at steady RPM.
   - Easy fix. Cleaning this often completely eliminates cruise-triggered STFT spikes.

2. **Upstream O2 sensor drifting**  
   - If it’s slow or reporting lean when it shouldn't, the ECU dumps fuel.
   - Cruise relies on this sensor *heavily* — more so than under acceleration.

---

### ✅ What You Should Do:
1. **Clean the MAF sensor ASAP**  
   - $7 fix. If that doesn’t work…
2. **Watch upstream O2 voltage in live data during cruise**  
   - Should *rapidly switch* between 0.1V and 0.9V
   - If it lingers near 0.1V = false lean = rich correction = possible bad O2

3. **Consider a new upstream O2 sensor**  
   - Especially if cleaning MAF doesn’t fix it. ~$60 part.

---

Let me know if you want exact instructions for MAF cleaning on your engine or help checking O2 voltages. You're real close to solving this one.

## User

In a autolink al319 where can I see the voltage?

## Assistant

Great question — the **Autel AutoLink AL319** is a solid little code reader, but unfortunately it’s **not designed to show live O2 sensor voltages directly**. It’s a basic tool meant for:

- Reading/clearing codes
- Showing freeze frame data
- Basic live data like RPM, fuel trims, coolant temp

**However** — depending on firmware and menu version, you might be able to get O2 data as part of the live data stream:

---

### 📱 How to Check (if supported):
1. **Plug in the AL319**
2. Go to **Live Data**
3. Select **View Data Stream**
4. Look for a line labeled:
   - `O2S11` (O2 Sensor Bank 1 Sensor 1) → this is your upstream sensor
   - `O2S12` is downstream
5. If it shows:
   - **Volts** (e.g., 0.1V to 0.9V) — you're in luck
   - **Millivolts** (e.g., 100–900 mV) — same thing
   - If it only says "Rich/Lean/Ready" — it’s limited mode

---

### 🔧 What You Want to See:
- Upstream (`O2S11`) sensor should **rapidly bounce between ~0.1V and ~0.9V**, switching multiple times per second.
- If it's **stuck low (~0.1–0.3V)** = false lean → ECU adds fuel → P0172.
- If it’s **slow to switch** (e.g. 1–2 times per second or less), it’s probably going bad.

---

### ❌ If AL319 Can't Show It:
If your unit doesn’t display voltage, you’ll need a cheap Bluetooth OBD2 scanner (~$10) like:
- **Veepeak**
- **BAFX**
- **OBDLink LX**

Then use an app like **Torque (Android)** or **Car Scanner (iOS/Android)**. You’ll get full sensor graphs and better trim visibility.

Let me know your engine type (1.5T or 2.0T?) and I’ll give you the MAF cleaning steps and a good sensor voltage you can expect.

## User

Sometimes it dips to 0.000v on o2s12 like when I'm going down hill

## Assistant

That’s a great observation — and perfectly normal for **O2S12**, which is your **downstream oxygen sensor** (after the catalytic converter).

---

### 📉 What It Means When O2S12 Reads 0.000V:

- **Downhill = fuel cut-off**  
  When you coast downhill (especially with cruise or foot off the gas), the ECU often cuts fuel entirely to save gas. With no fuel burning, the exhaust has no oxygen reactions — so the downstream sensor drops to **0.000V** or near it.

- **O2S12 is not used for fueling anyway**  
  The downstream sensor is **only there to monitor the catalytic converter's efficiency**, not to control fuel trim. So 0.000V during fuel cut is 100% expected.

---

### 🧠 What You Should Focus On Instead:
You want to monitor **O2S11** (Bank 1 Sensor 1), which is the **upstream sensor** — it actually **controls** the air-fuel mixture.

If you can’t get good live data from your current tool, I strongly recommend:
- A $10–$20 Bluetooth OBD2 adapter
- Free app like **Car Scanner** or **OBD Fusion**

You’ll get:
- Real-time graphs of O2S11 voltages
- Accurate STFT/LTFT values
- Easier tracking of when/why trims go negative

---

Let me know if you want a recommended scanner + app combo for your phone. Or, if you have your engine code (1.5T or 2.0T), I can walk you through cleaning the MAF and checking everything else cheap & fast. You're on the right track.

## User

Okay I found it. At idle o2s11(v) is at 2.2, sometimes as high as 2.4, as low as 2.1

## Assistant

Aha — that explains **everything.**

---

### ❌ **O2S11 (Upstream) Should Not Be at 2.2V**
That’s **way out of spec.** A normal upstream O2 sensor reads between **0.1V and 0.9V** (or 100–900 mV). It should *bounce rapidly* in that range at idle.

If you’re seeing **2.1–2.4V**:
- Your sensor is likely **not a standard narrowband** sensor — **or**
- The scan tool is **misinterpreting a wideband sensor’s output**

---

### 🧠 2018 Accord O2S11 = **Wideband Sensor**
That’s the key.

Your Accord uses a **wideband air-fuel ratio sensor**, not a simple narrowband O2 sensor. These work differently:
- They output a **simulated voltage**, not a raw oscillation
- Normal range is usually **1.4V to 3.3V**
- **~2.4V = stoichiometric** (perfect mix)
- **Below 2.4V = rich**, above = lean

So if your O2S11 is sitting at **2.2V at idle**, that means:
> The ECU sees a **rich condition**, and is trying to correct it.

---

### 🎯 What This Confirms:
- The upstream sensor **is functioning** — it’s detecting rich correctly.
- The engine **is running slightly rich**, even at idle.
- The ECU is **pulling fuel** (confirmed by STFT/LTFT) to compensate.

---

### ✅ You Are Now 95% Confirmed:
This is likely caused by:
1. A **slightly dirty MAF sensor** OR
2. A **minor injector over-delivery**, especially during cruise
3. Possibly **fuel pressure a bit high**, but less likely

---

### 🚀 Action Plan:
1. **Clean MAF sensor now**  
   - 5-minute job, costs ~$7  
   - Might resolve this entirely
2. **Clear trims again**
3. **Retest after 10–15 min of mixed driving**  
   - If O2S11 hovers closer to 2.4V = you’re back in balance
   - If it stays around 2.1–2.2V = still slightly rich

---

Let me know if you want a step-by-step MAF cleaning guide for your engine type (1.5T or 2.0T). You’re inches away from solving this.

## User

If I can't get to a parts store for a while, like until tomorrow evening, is there anything I can do in the meantime?

## Assistant

Absolutely — there are a few things you can do **right now**, without needing a parts store, to help stabilize the fuel trims until you can clean the MAF sensor tomorrow.

---

### ✅ **Quick Fixes You Can Do Today**

#### 1. **Disconnect & Reconnect the MAF Sensor**
**Why:** Forces a clean contact, and sometimes clears up minor voltage jitter.

- Engine off, key out.
- Unplug the MAF sensor.
- Check for corrosion or gunk on the pins (don’t scrape — just blow if needed).
- Plug it back in firmly.
- Start the engine and see if trims stabilize slightly.

---

#### 2. **Inspect the Air Intake**
**Why:** A cracked or loose intake boot can suck in unmetered air → trim chaos.

- Look between the airbox and throttle body.
- Check for:
  - Loose clamps
  - Cracks or splits
  - Vacuum lines knocked loose
- If you see anything loose, **tighten it** or temporarily tape a crack with electrical or duct tape.

---

#### 3. **Drive With a Lighter Foot**
**Why:** Cruise control exposes the trim issue. Driving gently under your own control lets the ECU adapt better.

- Avoid cruise control for now.
- Keep RPMs between 1500–2500 when possible.
- Coast gently when possible — don’t force engine braking unless needed.

---

#### 4. **Use High-Quality Gas (if you’re still near empty)**
**Why:** Cheap gas sometimes burns dirtier and worsens trim learning.

- Top off with name-brand fuel if you didn’t earlier (e.g. Shell, Exxon).
- Even 5 gallons of good gas can smooth out combustion quality for now.

---

### 🚫 What NOT to Do:
- Don’t use more Sea Foam or fuel additives right now — could skew trims more.
- Don’t disconnect the battery again unless you’re ready to clear all learning (and lose radio presets).

---

Want me to help you ID the MAF location and tools needed so you're ready to go tomorrow evening without delay? Just tell me if you have the 1.5L or 2.0L engine.

## User

I'm pretty sure it's the 1.5, this isn't the sport edition or anything

## Assistant

Perfect — then you’ve got the **1.5L turbocharged Earth Dreams engine** (L15B7). I’ll walk you through exactly what to do when you’re ready to clean the MAF sensor tomorrow, and what you can do right now to prep.

---

### 🔧 **MAF Sensor Location – 2018 Accord 1.5T**
- Look under the hood — find the **airbox** (big black box with the air filter).
- Follow the intake hose toward the engine.
- The **MAF sensor** is mounted **right after the airbox**, before the turbo inlet.
- It’s a small rectangular sensor with a **plug and two screws** (usually Torx T20 or Phillips).

---

### 🧼 **MAF Cleaning Checklist** (Tomorrow)
**What you need:**
- MAF cleaner spray (NOT carb/brake cleaner — that will destroy it)
- Torx T20 bit or small Phillips
- Safety: gloves + eye protection

**Steps:**
1. **Unplug the sensor**
2. **Unscrew it** from the intake (don’t drop it!)
3. **Hold it by the body** (don’t touch the wires inside)
4. Spray the **sensor wire or grid** thoroughly (5–10 sprays)
5. **Let it air dry** for 10 minutes — do NOT wipe
6. Reinstall and plug it back in

**Then:**
- Clear codes (if any)
- Drive ~10–15 mins, check STFT/LTFT again
- Watch O2S11 to see if it drifts toward **2.4V** (perfect)

---

### 🛠️ What You Can Do Tonight:
- **Pop the hood**
- **Find the MAF** and make sure it's not loose or oily
- **Inspect the intake duct** — especially the accordion-style rubber section — for cracks
- Make sure no rodents or leaves got inside the air filter box (seriously)

---

Let me know if you want a diagram or annotated photo of the MAF location for your exact engine — I can mock one up quickly. You're right on track.

