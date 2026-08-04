---
type: Conversation
title: "Global religion percentages chart"
description: "Can you find the percentages of every religion in the world (feasible)? Make a pie chart showing them with the most recent statistics."
resource: "6895f8c6-be5c-8325-9bfd-ece04759f22e"
timestamp: "2025-08-08T17:03:51.340Z"
tags: ["gpt-5"]
---

# Global religion percentages chart

## User

Can you find the percentages of every religion in the world (feasible)? Make a pie chart showing them with the most recent statistics. 

## Assistant



## Assistant



## Assistant



**Tool Output (web.run)**:
```

```

## Assistant



**Tool Output (web.run)**:
```

```

## Assistant



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



## Assistant



**Tool Output (python)**:


## Assistant

Here’s a clean pie chart of global religious affiliation using the most recent **comprehensive, open** dataset (Pew Research Center’s 2015 global estimates, published 2017). I also put the numbers in a little table for you in case you want to copy them.

If you want me to chase down the **newest** (e.g., 2020–2025) estimates from the World Religion Database / Status of Global Christianity, I can browse and update this—but those are often behind paywalls or summarized in reports. Want me to go hunting?

## User

Can you make the same chart, but do it based on billionaires only?

## Assistant



## Assistant



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



**Tool Output (web.run)**:
```

```

## Assistant



## Assistant



## Assistant



**Tool Output (python)**:


## Assistant



**Tool Output (python)**:


## Assistant

Here you go—pie chart of **billionaires by religion** using the best-available public snapshot (often attributed to Wealth-X from the mid-2010s):

[Download the PNG](sandbox:/mnt/data/billionaires_by_religion_pie.png)

Quick heads-up on sources/limits:
- A **current, public** religion breakdown for *all* billionaires doesn’t really exist. Wealth-X/Altrata track this in their database, but the free census reports don’t show religion tables. citeturn5search2turn5search10  
- The exact percentages used here (Christian **66.2%**, Hindu **9.3%**, Jewish **6.5%**, Muslim **6.3%**, Other/unspecified **11.7%**) are widely quoted online as coming from a Wealth-X study, but the original table isn’t publicly hosted; you’ll mostly find secondary references. Treat this as a **historical snapshot/approximation**, not today’s precise distribution. citeturn5search6

If you want something **more up-to-date**, I can:
1) build an **approximate 2025 view** by sampling the latest Forbes billionaire list and tagging religions where people have publicly stated affiliations (it’ll have gaps + uncertainty), or  
2) pull paywalled **Altrata** data if you have access and we can chart it exactly.

Your call—want me to do option 1 and show method + confidence notes, or keep this snapshot?

## User

Can you do the same chart but married homeowners?

## Assistant



## Assistant



## Assistant

That one’s tricky. There isn’t a reliable **global** dataset that cross-tabs *religion × marital status × homeownership*. Most public stats only do one or two of those at a time, and the big global sources (Pew, WRD, UN) don’t track housing tenure.

I can still make this happen if we narrow scope. Pick one:

- **United States** (best options): I can use a public survey like the Cooperative Election Study (CES) or GSS to compute “% of *married homeowners* by religion” and chart it.  
- **UK (England & Wales)**: 2021 Census includes religion + tenure + marital status; I can pull ONS tables.  
- **Another country** you care about (if their census reports those three together).

Which country/region should I use? If you want the US, I’ll fetch the latest microdata and build the pie chart with clear notes on uncertainty.

## User

Let's do USA

## Assistant



## Assistant



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



## Assistant



**Tool Output (python)**:


## Assistant



**Tool Output (python)**:


## Assistant



**Tool Output (python)**:


## Assistant

I made you a U.S. **married homeowners by religion** pie chart (best-available public data).  
[Download the PNG](sandbox:/mnt/data/us_married_homeowners_by_religion_prri2016.png)

How I built it (transparent math):
- Source: PRRI’s **“America’s Changing Religious Identity”** report (uses 2016 data). It includes:  
  - each group’s *population share* (e.g., white evangelical 17%, white mainline 13%, white Catholic 11%, etc.), citeturn2view1  
  - *homeownership rates* by group (e.g., white Catholic 78%, white evangelical 75%, unaffiliated 54%, Jewish 69%, Muslim 36%, etc.), citeturn1view0turn2view2  
  - *marriage rates* by group (e.g., white evangelical 64%, white mainline 60%, Mormon 68%, Hindu 66%, unaffiliated 42%, etc.). citeturn1view0
- I estimated each slice as: **population share × married rate × homeowner rate**, then normalized to 100%. (PRRI doesn’t publish the exact “married AND homeowner” cross-tab; this is a reasonable approximation.)

Caveats:
- Two tiny buckets (“other/mixed-race Protestant” and “other non-Christian”) needed small assumptions because PRRI doesn’t give all cross-tabs; they contribute very little to the total.
- This is 2016-era; if you want **2023–24**, Pew’s new RLS exists but I’m not seeing tenure (own/rent) published yet.

Want me to:
- swap this to a **bar chart** ranked by share,  
- or rebuild it with a newer microdata source if we can find a public survey that asks **religion + own/rent + marital status** for 2022–2024?

