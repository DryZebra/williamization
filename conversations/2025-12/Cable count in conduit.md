---
type: Conversation
title: "Cable count in conduit"
description: "E343571 18/2 AWG c21819805 cable how many can I legally fit into a 2\" trade size rigid conduit legally? It'll carry 24v."
resource: "6931a37c-ee10-832c-94d1-8b6a06bfcc49"
timestamp: "2025-12-04T15:09:03.660Z"
tags: ["gpt-5-1"]
---

# Cable count in conduit

## User

E343571 18/2 AWG c21819805 cable how many can I legally fit into a 2" trade size rigid conduit legally? It'll carry 24v. 

## Assistant



## Assistant



## Assistant



**Tool Output (web.run)**:
```

```

**Tool Output (web.run)**:
```
【turn0calculator0】 1 = 1
```

## Assistant



**Tool Output (web.run)**:
```

```

**Tool Output (web.run)**:
```

```

## Assistant



**Tool Output (web.run)**:
```

```

**Tool Output (web.run)**:
```

```

## Assistant



## Assistant



**Tool Output (web.run)**:
```

```

**Tool Output (web.run)**:
```

```

## Assistant



## Assistant



**Tool Output (web.run)**:
```

```

## Assistant



## Assistant

import math
area_cable = math.pi*(0.28/2)**2
area_cable

**Tool Output (python)**:


## Assistant



**Tool Output (python)**:


## Assistant



## Assistant

Short answer: **22 of those 18/2 cables in a 2" rigid, by NEC conduit fill.**

Here’s how that shakes out.

---

### 1. Get the actual cable OD

Your marking `E343571 18/2` lines up with a Windy City Wire TC-ER / PLTC style 18 AWG 2-conductor tray/control cable. The spec sheet for their 18/2 E343571 cable gives:  

> **Overall diameter ≈ 0.280" nominal** citeturn2search4  

So we’ll treat your cable as **0.280" OD**.

Cross-sectional area of one round cable:

\[
A_{\text{cable}} = \pi \left(\frac{0.280}{2}\right)^2 \approx 0.062 \text{ in}^2
\]

---

### 2. Conduit area (2" RMC) and allowed fill

From NEC Chapter 9, Table 4 for **2" RMC**:  

- **Total area (100%)** = 3.408 in²  
- **40% (over 2 conductors/cables)** = **1.363 in²** citeturn4view0  

NEC Chapter 9, Table 1 says when you have **more than 2 conductors/cables**, max fill is **40% of the raceway’s internal area**. This applies to multiconductor cables too; you just use the cable’s overall OD as if it were one big “conductor.” citeturn3search4  

---

### 3. Divide it out

\[
N_{\max} = \left\lfloor \frac{1.363}{0.062} \right\rfloor \approx \left\lfloor 22.1 \right\rfloor = 22
\]

So **code-wise for conduit fill, you can legally put 22 of those 18/2 cables in a 2" trade size rigid**.

---

### 4. A few practical notes

- That’s **theoretical max** based on *nominal* OD. Real cable could be slightly larger; if it’s a different manufacturer or construction than the spec I pulled, recheck the OD on that exact cut sheet.
- For 24 V control/FA/PLTC stuff, you still have to mind the applicable NEC article (likely 725/760/727 depending on use), but **conduit fill rules still apply**. citeturn2search4turn2search5  
- For pullability and future changes, a lot of folks will **stay well under 40%**—more like 25–30%—especially with soft jackets.

If you tell me how many you’re *thinking* of pulling and what the run looks like (length, bends), I can sanity-check whether it’s going to be miserable or reasonable in the field.

