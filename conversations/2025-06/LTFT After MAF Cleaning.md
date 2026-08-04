---
type: Conversation
title: "LTFT After MAF Cleaning"
description: "The trim on my live data is still floating around -14% after using the MAF cleaner (2018 accord)"
resource: "684c329d-65c8-8003-8efe-26c3aa1e3686"
timestamp: "2025-06-13T14:16:25.070Z"
tags: ["gpt-4o"]
---

# LTFT After MAF Cleaning

## User

The trim on my live data is still floating around -14% after using the MAF cleaner (2018 accord)

## Assistant



## Assistant

If your long-term fuel trim (LTFT) is still hovering around **-14%** after cleaning the MAF sensor on your **2018 Honda Accord**, that means the ECU is consistently pulling fuel—suggesting the engine is running rich even after correction. A few thoughts to narrow it down:

---

### ✅ First, What You've Already Done:
- **Used MAF cleaner** — good first step.
- **Still seeing -14% LTFT** — consistently pulling fuel.

---

### 🔍 Possible Causes (Still Rich After MAF Cleaning):

#### 1. **Over-reporting MAF Sensor**  
Even after cleaning, if your MAF is **misreporting airflow**, the ECU will inject too much fuel.

- **Check live data**: At idle, your MAF should read around **2-3 g/s**. Higher = suspect.
- If possible, compare values at idle and 2500 RPM to expected airflow.

#### 2. **Leaking or Dirty Fuel Injector**
- A stuck or leaky injector can enrich a single cylinder, skewing trims.
- Check for misfires or rough idle (even if minor).

#### 3. **O2 Sensor Fault (Especially Front Sensor)**
- If the upstream O2 sensor is slow or biased rich, it could falsely cause negative trim.
- Graph the upstream sensor—does it switch rapidly between ~0.1V and ~0.9V at idle?
- If it’s stuck high (0.8-0.9V) or oscillates slowly, it might be the culprit.

#### 4. **Evap Purge Valve Stuck Open**
- Allows fuel vapors into the intake at the wrong time, enriching mixture.
- Test by pinching/plugging the line from the purge valve and seeing if trims improve.

#### 5. **Aftermarket/Dirty Air Filter or Intake Mods**
- Anything that disrupts airflow over the MAF sensor can cause incorrect readings.
- Return to OEM if you’ve modded intake.

---

### 🧪 Quick DIY Tests:

| Test | Tool Needed | Result |
|------|-------------|--------|
| MAF reading at idle | Live scanner | Should be ~2-3 g/s |
| Fuel pressure test | Gauge | See if pressure is too high |
| Upstream O2 voltage | Live scanner | Should switch ~1x/sec |
| Smoke test | Optional | Check for hidden vacuum leaks or evap system leaks |

---

### 🛠️ Next Best Step:
If MAF and O2 seem normal, and you've got no misfire codes or drivability symptoms, it may be safe to **clear the trims manually** (via scanner or battery reset), drive it through a full warm-up cycle, and recheck data. Sometimes trims take a bit to recalibrate after cleaning.

Let me know if you can share idle MAF readings, upstream O2 behavior, or fuel pressure — I’ll help walk through the numbers.

