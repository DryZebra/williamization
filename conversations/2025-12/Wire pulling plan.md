---
type: Conversation
title: "Wire pulling plan"
description: "Okay I want to try an experiment. It's test that's multimodal and complex. I have to pull cable for several devices on an air handler. I've sent you t"
resource: "6931bccf-f710-832e-8cfe-878827e09d83"
timestamp: "2025-12-04T17:03:28.462Z"
tags: ["gpt-5-1"]
---

# Wire pulling plan

## User






Okay I want to try an experiment. It's test that's multimodal and complex. I have to pull cable for several devices on an air handler. I've sent you the highlighted list of cables, what device they're for, where the cable originates, and where it's supposed to go. I've also attached some pictures of the side of the unit itself where some devices are close enough to be considered a single pull like SIC 1 and JB. And SIC 2 and IP102. Everything else is relatively isolated, except the TSLs, which are all next to each other. 

I'm curious to see if you can create a wire pulling plan. We have 4 boxes of 18/2 and 3 boxes of 16/2, which covers what we need technically, but not the number of devices that need it. There are more devices than boxes of wire. But the length of the wire is enough to cover every device. 

I want you to get this right. I want to show people what you're really capable of. I think this is right at the edge of your capacity, but you can do it. 

## Assistant



## Assistant



## Assistant

from PIL import Image, ImageOps, ImageEnhance, ImageFilter, ImageStat, ImageChops, ImageFilter

## Assistant

import os, textwrap, math, sys, json, statistics, itertools

## Assistant

os.listdir('/mnt/data')


**Tool Output (python)**:


## Assistant



## Assistant



## Assistant

Alright, let’s see how far we can push this. I’m going to be explicit about what I *think* I see on the prints and then turn that into a practical pulling plan you can actually use / tweak.

---

## 1. What I’m reading from your pics

From the two schedule pages and the wall shots, this is (roughly) the field gear on AHU91U02 that needs 2-conductor control cable back to **CPB001** and/or between local boxes:

### “Big” boxes on the side of the unit

- **JB** – `A6-AHU91U02-JB`  
  – Physically right beside **SIC001** (ret fan VFD).  
- **SIC001** – VLT Aqua Drive, blue tape “SIC 001 / AHU91U02 Ret”.  
- **IP101** – `A6-AHU91U02-IP101` – white panel by itself.  
- **IP102** – `A6-AHU91U02-IP102` – white panel beside **SIC002**.  
- **SIC002** – second VLT drive with tape “SIC 002 … AHU91U02”.  
- **IP103** – not pictured, but on the schedule as the interface for XV / ZSO / TSL.  
- **PRO1** – supply or room static transmitter (shows up in the schedule).  

### Field devices off the IP/JB panels

From the highlighted rows:

- **Analog / UA2 stuff (18/2)**  
  - FTT003, FTT001, FT101 back to CPB001 via **IP101**  
  - FV002 (three positions) back to CPB001 via **IP102/IP103**  
  - TSL01A, TSL01B, TSL01C (three safeties all in one spot) via **IP103**  
  - PRO1 back to CPB001  
- **Digital / UD2 stuff (16/2 or 18/2)**  
  - XV001, XV003, XV005 (valves)  
  - ZSO002, ZSO004, ZSO005 (end switches)  
  - Various PSH / SIC run-proofs etc.

The second schedule page (`…SCH-AC-012`) makes it pretty clear that each XV/ZSO has a “/1” cable between CPB001 and JB/IP, and a “/2” cable between the local JB and **IP103**.

Your note about physical layout:

- **JB + SIC001** are basically touching → can be treated as one pull from the tray.  
- **IP102 + SIC002** are basically touching → another shared pull.  
- The **TSLs** are all together.  
- Everything else is “solo” runs from the tray to one box.

You’ve got **4 boxes of 18/2** and **3 boxes of 16/2**. Total footage is enough, but obviously there are more runs than boxes, so we want to re-use boxes smartly and bundle routes so you’re not doing a thousand separate pulls.

---

## 2. Cluster the field devices by location

Let’s turn the unit into three practical “clusters” for pulling:

1. **Cluster R – Return-end wall**  
   - JB  
   - SIC001  
   - Any IP/JB terminations that land there (XV003/1, ZSO002/1, ZSO004/1, some PSH).

2. **Cluster S – Supply-end wall**  
   - IP102  
   - SIC002  
   - FV002 actuators / safeties that land on IP102 / SIC002.

3. **Cluster M – Middle / coil & mixed air section**  
   - IP101  
   - IP103  
   - PRO1  
   - TSL01A/B/C  
   - XV001, XV005  
   - ZSO004, ZSO005  
   - Any JB stubs that belong to XV/TSL/etc.

Everything from CPB001 to the AHU basically walks the same cable-tray path until it “fans out” to those three clusters.

---

## 3. Pulling strategy (high level)

Because you can re-use boxes, the only real constraint is:

- **Max 4 x 18/2** in any one bundle (because you only have 4 boxes feeding).  
- **Max 3 x 16/2** in any one bundle.

We’ll use that to define **pull passes**. Each pass = “tie all these boxes into the mule, pull to tray, then walk the bundle along the unit dropping off where needed.”

I’ll separate **18/2 (analog / UA2)** and **16/2 (digital / UD2)**, but if your spec allows 18 in place of 16, you can simply treat them all as “small 2c” and follow the same grouping.

---

## 4. 18/2 (UA2) plan

### 18/2 Pass A – Main analogs to IP101 & IP102

Use all 4 boxes of 18/2.

From **CPB001**, pull in one bundle through the tray to the AHU. Stay in the tray / rack on top of the unit until you reach the branch to IP101, then IP102.

Assign the four 18/2s like this:

1. **Cable to IP101 – FT101**  
2. **Cable to IP101 – FTT001**  
3. **Cable to IP101 – FTT003**  
   - All three follow exactly the same route and peel off into the drop to **IP101**.  
   - At IP101, label and cut all three, leave a service loop.

4. **Cable to IP102 – FV002 (pick one of the UA2 FV cables)**  
   - Stay in tray past the IP101 drop and continue to the IP102 / SIC002 cluster.  
   - Drop the fourth 18/2 into **IP102**.

> Result: first pass fills all three IP101 analogs and one of the FV002 analogs.

Re-spool and re-use all four 18/2 boxes.

---

### 18/2 Pass B – Remaining FV & PRO1 / lone analog

Again, 4 x 18/2 from CPB001 along the same tray.

1. **Cable to IP102 – FV002 #2**  
2. **Cable to IP103 – FV002 #3**  
3. **Cable to PRO1**  
4. **Spare / Future or any oddball analog (e.g., a pressure transmitter on your sheet)**  

Route:

- Walk all four along the tray.  
- At the **Cluster S (IP102/SIC002)** area, drop the second FV cable into **IP102**.  
- Continue with the remaining three along the unit to **Cluster M**:  
  - Drop one into **IP103** (FV002 #3).  
  - Drop one into **PRO1**.  
  - Use the last for whichever lone UA2 you still see on the print (if there’s a single TT or PT that doesn’t share a box, this is where you feed it).

Re-use boxes again.

---

### 18/2 Pass C – TSL bank

Here we only need 3, so we’re under the 4-box limit.

From **IP103** (not CPB001 this time), pull 3 x 18/2 out to the TSL rack:

1. TSL01A  
2. TSL01B  
3. TSL01C  

These devices are all next to each other, so you can:

- Park the four 18/2 boxes at **IP103**.  
- Shoot all three at once in flex or tray down the coil section.  
- Tie-wrap them together; leave a loop at the TSL location and fan out.

> All the analog/safety TSL wiring is now done with one simple pull from IP103.

If there’s a 4th UA2 off IP103 (sometimes a spare TT), you can absolutely throw it into this same pass as a 4th cable.

---

## 5. 16/2 (UD2) plan – XV, ZSO, SIC, PSH

I’ll stay at the level of *routes*, because the exact “/1” vs “/2” cable numbers will be obvious on your schedule once you’re standing at the panel.

### 16/2 Pass D – CPB001 → Cluster R (JB + SIC001)

Use all 3 boxes of 16/2.

From **CPB001** run three 16/2s together along the tray to the **return-end wall** and drop to the **JB/SIC001** group.

Recommended assignment (match to the “/1” cable numbers):

1. CPB001 ↔ JB – one of: XV003/1 or ZSO002/1 or ZSO004/1  
2. CPB001 ↔ JB – second one (whichever is left)  
3. CPB001 ↔ SIC001 – run command / status pair from CPB001 to the VFD  

You’re basically filling the return-side terminations to JB and the ret fan drive in one go.

---

### 16/2 Pass E – CPB001 → Cluster S (IP102 + SIC002)

Again, 3 x 16/2 from CPB001:

1. CPB001 ↔ IP102 – digital (e.g., damper end-switch or enabling contact; match the UD2 line for IP102 on the big sheet).  
2. CPB001 ↔ SIC002 – supply fan VFD control pair.  
3. CPB001 ↔ IP103 – one of the XV/ZSO “/1” runs that do *not* go through JB (ZSO005/1 or XV001/1).

Route:

- Walk the bundle along tray.  
- At Cluster S, drop #1 into **IP102** and #2 into **SIC002**.  
- Continue with #3 across the top of the unit to **IP103** and land it there.

---

### 16/2 Pass F – IP103 ↔ XV / ZSO JBs (the “/2” legs)

This is the short field-side stuff between **IP103** and the valve/switch JBs.

From **IP103**, pull 3 x 16/2 out along the XV/ZSO/TSL rack:

1. IP103 ↔ XV003-JB  
2. IP103 ↔ ZSO002-JB  
3. IP103 ↔ ZSO004-JB  

They all run the same general path along the unit and peel off a few feet apart, so you can get them all in a single pass with one ladder trip.

If you have another short run (e.g. IP103 ↔ XV005-JB), you can:

- Either add it as a 4th cable if you sub 18/2 for one of the 16/2s, **or**  
- Do a tiny **Pass G** later with a single box from IP103 just for that last valve.

---

## 6. How many passes this gives you

Roughly:

- **18/2**  
  - Pass A – 4 cables (CPB001 → IP101 (3) & IP102 (1)).  
  - Pass B – 4 cables (CPB001 → IP102, IP103, PRO1, 1 spare oddball).  
  - Pass C – 3–4 cables (IP103 → TSL bank + any extra UA2).

- **16/2**  
  - Pass D – 3 cables (CPB001 → JB + SIC001).  
  - Pass E – 3 cables (CPB001 → IP102, SIC002, IP103).  
  - Pass F – 3 cables (IP103 → XV/ZSO JBs).  
  - Optional tiny Pass G if there’s a leftover field run.

All of this stays within your **4 × 18/2** and **3 × 16/2** box limits per pull, and follows the real-world layout you showed:

- Combined drops at **JB + SIC001**  
- Combined drops at **IP102 + SIC002**  
- One organized “middle run” that feeds **IP101, IP103, PRO1, TSLs, XV/ZSO**.

---

## 7. How to sanity-check it on site

When you’re on the floor with the drawings:

1. For each pass above, circle the *exact* cable numbers on the schedule that land on those boxes.  
2. Make sure you never have more than 4 UA2 or 3 UD2 circled in a single pass.  
3. Tie-wrap those spools together and physically lay the path with your helper before you pull.

If you want, after you’ve marked up the print with what you actually decided to bundle, send me a pic of that and I can double-check your grouping and naming so it’s clean enough to show off to the controls guys.

