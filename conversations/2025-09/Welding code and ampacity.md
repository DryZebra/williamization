---
type: Conversation
title: "Welding code and ampacity"
description: "Concerning a welder drawing 13.9A and article 240, is installing a 14 awg on 30A breaker legal per the code? Does 13.9 not violate the 80% rule? Or do"
resource: "68d66440-647c-832a-8a11-57105a32abb2"
timestamp: "2025-09-26T10:03:18.933Z"
tags: ["gpt-5"]
---

# Welding code and ampacity

## User

Concerning a welder drawing 13.9A and article 240, is installing a 14 awg on 30A breaker legal per the code? Does 13.9 not violate the 80% rule? Or does that only apply to the breaker since it's double the ampacity?

## Assistant



## Assistant

Good question — this gets into the way welders are treated as a **special case** in the NEC. Let’s break it down:

---

### 1. Normal Rule (Article 240 and 310)
- **14 AWG copper** normally has an ampacity of **15A** (Table 310.16).
- Standard overcurrent protection (240.4(D)(3)) would limit 14 AWG to a **15A breaker**.
- The “80% rule” you’re thinking of comes from 210.20(A) / 215.3: branch-circuit OCPD can’t be loaded more than 80% for *continuous loads* unless the device is rated 100% at that load.

So under normal branch-circuit rules, a 14 on 30A would **not** be allowed.

---

### 2. Welders Are Special (Article 630)
- **Article 630** covers arc welders.  
- 630.11 lets you size **conductor ampacity at less than the rated primary current**, because welders have a duty cycle (not continuous like a motor).  
- 630.12 allows the **overcurrent device to be as large as 200%** of the conductor ampacity.  
- The logic: welding machines have inrush and irregular load profiles, so the code explicitly allows **smaller conductors with larger breakers** as long as the math follows 630.

So the breaker doesn’t have to strictly follow 240.4(D), because **630 modifies 240**.

---

### 3. Your Case (13.9A nameplate)
- If the welder input is **13.9A at duty cycle**, the minimum conductor ampacity per 630.11 can be calculated (usually *rated primary current × duty-cycle factor*). Often that comes out lower than nameplate.  
- With that, a **14 AWG conductor** could be code-legal on a **30A breaker**, if the calculation under Article 630 justifies it.  
- The “80% rule” doesn’t apply the way it does to general-purpose loads, because welders are not considered continuous in the same sense. The breaker oversizing is permitted *precisely so it won’t nuisance-trip*.  

---

### 4. Practical Answer
- **Yes**, a 14 AWG on a 30A breaker can be legal **if installed under Article 630** rules for welders.  
- **No**, the 13.9A doesn’t violate the 80% rule in this context — that rule applies to continuous loads on general-purpose branch circuits, not specially treated loads like welders.  
- What matters is following 630.11 (conductor sizing) and 630.12 (OCPD sizing).  

---

👉 If you’d like, I can walk through the exact 630.11 duty-cycle table math with your welder’s duty cycle % to show precisely whether 14 AWG is acceptable in your case. Do you know the **duty cycle percentage** listed on the nameplate?

