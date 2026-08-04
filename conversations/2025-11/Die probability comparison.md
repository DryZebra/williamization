---
type: Conversation
title: "Die probability comparison"
description: "Say I have 6 die, each with the following percent chance on landing on 1: 66.7%, 46.2%, 46.2%, 46.2%, 36.8%, 26.7% The last die could also be 27.3% Th"
resource: "69291b7f-10c8-832f-8631-f0de70ee9e41"
timestamp: "2025-11-28T11:38:37.439Z"
tags: ["gpt-5-1"]
---

# Die probability comparison

## User

Say I have 6 die, each with the following percent chance on landing on 1: 66.7%, 46.2%, 46.2%, 46.2%, 36.8%, 26.7% 

The last die could also be 27.3% 

The same die have the percentage chance of landing on 5: 6.7%, 0, 10.5%, 26.7%

The last die could also be 18.2%. 

The goal is to roll as many points as possible. 1 = 100. 5= 50. 

Rolling 3x1s is 1000 points. Each additional 1 is an extra 1000 points. 4x1= 2000, 5x1 = 3000, 6x1 = 4000. 

Rolling 3xt is 500 points. Each additional 5 is an additional 500 points. 

My question is about the last die. This is very petty, but which is preferable? 27.3%@1+18.2%@5 or 26.7%@1+26.7%@5?

## Assistant



## Assistant



## Assistant

from itertools import product

p1 = [0.667, 0.462, 0.462, 0.462, 0.368]
p5 = [0.067, 0.0,   0.105, 0.267, 0.0  ]

def expected_value(last_p1, last_p5):
    p1_all = p1 + [last_p1]
    p5_all = p5 + [last_p5]
    ev = 0.0
    # states: for each die result: 0=other, 1=1, 2=5
    for outcomes in product([0,1,2], repeat=6):
        prob = 1.0
        n1 = 0
        n5 = 0
        for i,res in enumerate(outcomes):
            if res==1:
                prob *= p1_all[i]
                n1 += 1
            elif res==2:
                prob *= p5_all[i]
                n5 += 1
            else:
                prob *= (1 - p1_all[i] - p5_all[i])
        if prob==0:
            continue
        # score calculation
        score = 0
        # ones
        if n1>=3:
            score += 1000 + (n1-3)*1000
        else:
            score += n1*100
        # fives
        if n5>=3:
            score += 500 + (n5-3)*500
        else:
            score += n5*50
        ev += prob*score
    return ev

ev_A = expected_value(0.267, 0.267)
ev_B = expected_value(0.273, 0.182)
ev_A, ev_B, ev_A-ev_B

**Tool Output (python)**:


## Assistant



## Assistant

p1 = [0.667, 0.462, 0.462, 0.462, 0.368]
p5_zero = [0,0,0,0,0]

def expected_value_generic(last_p1, last_p5, p5_list):
    p1_all = p1 + [last_p1]
    p5_all = p5_list + [last_p5]
    ev = 0.0
    from itertools import product
    for outcomes in product([0,1,2], repeat=6):
        prob = 1.0
        n1 = n5 = 0
        for i,res in enumerate(outcomes):
            if res==1:
                prob *= p1_all[i]
                n1 += 1
            elif res==2:
                prob *= p5_all[i]
                n5 += 1
            else:
                prob *= (1 - p1_all[i] - p5_all[i])
        if prob==0: 
            continue
        score = 0
        if n1 >= 3:
            score += 1000 + (n1-3)*1000
        else:
            score += n1*100
        if n5 >= 3:
            score += 500 + (n5-3)*500
        else:
            score += n5*50
        ev += prob*score
    return ev

evA0 = expected_value_generic(0.267,0.267,p5_zero)
evB0 = expected_value_generic(0.273,0.182,p5_zero)
evA0, evB0, evA0-evB0

**Tool Output (python)**:


## Assistant



## Assistant

evA_die = 0.267*100 + 0.267*50
evB_die = 0.273*100 + 0.182*50
evA_die, evB_die

**Tool Output (python)**:


## Assistant



## Assistant

1.21493416908163*100

**Tool Output (python)**:


## Assistant



## Assistant

baseline = expected_value_generic(0,0,p5)
baseline

**Tool Output (python)**:


## Assistant



## Assistant

979.9279-761.021176455152, 978.7130-761.021176455152

**Tool Output (python)**:


## Assistant



## Assistant

1.215/218.9067

**Tool Output (python)**:


## Assistant



## Assistant



## Assistant

Short answer: **26.7% on 1 and 26.7% on 5 is (very slightly) better** than 27.3% on 1 and 18.2% on 5.

---

### Quick intuition (ignoring triples for a moment)

Treat the last die by itself, with just the base values:

- Option A: **26.7% 1, 26.7% 5**  
  - EV ≈ \(0.267 \times 100 + 0.267 \times 50 = 26.7 + 13.35 = 40.05\) points

- Option B: **27.3% 1, 18.2% 5**  
  - EV ≈ \(0.273 \times 100 + 0.182 \times 50 = 27.3 + 9.1 = 36.4\) points

So before we even think about triples, the “26.7% & 26.7%” die gives you about **3.65 more points per roll** of that die.

The bump from 1s (0.6 percentage points) is small, while the loss of 5s (8.5 percentage points) is big, and 5s still score.

---

### With your full 6-die setup and triples

If we plug in all six dice with the probabilities you gave:

- 1s: 66.7%, 46.2%, 46.2%, 46.2%, 36.8%, (26.7 **or** 27.3)  
- 5s paired as: 6.7%, 0%, 10.5%, 26.7%, 0%, (26.7 **or** 18.2)

and score using your rules  
- singles: 1 = 100, 5 = 50  
- triples and up:  
  - 3+ ones: 1000 for 3, +1000 for each extra 1  
  - 3+ fives: 500 for 3, +500 for each extra 5  

then the **expected total score per 6-die roll** comes out roughly as:

- With **26.7% 1 / 26.7% 5** on the last die: **≈ 979.9 points**
- With **27.3% 1 / 18.2% 5** on the last die: **≈ 978.7 points**

So even *including* the bonus from triples (where the extra 1-chance *could* have helped), the more balanced **26.7% / 26.7%** version still wins by about **1.2 points per full roll** of all six dice.

That’s tiny, but if you’re being petty and min-maxing:  
👉 **Take the 26.7% on 1 and 26.7% on 5.**

## User

All the 46.2% die actually have a 0% chance of landing on 5. I could swap all 3 out for a 26.7%@1 and 26.7%@5. 

## Assistant



## Assistant

import itertools, math, statistics, random

**Tool Output (python)**:


## Assistant

from itertools import product

def ev_for_config(dice):
    # dice: list of (p1,p5) for each die
    # outcomes for each die: 0=other,1=1,2=5
    ev = 0.0
    n = len(dice)
    for outcome in product([0,1,2], repeat=n):
        prob = 1.0
        for i, o in enumerate(outcome):
            p1,p5 = dice[i]
            if o==1:
                prob *= p1
            elif o==2:
                prob *= p5
            else:
                prob *= (1-p1-p5)
        if prob==0:
            continue
        n1 = sum(1 for o in outcome if o==1)
        n5 = sum(1 for o in outcome if o==2)
        # score for ones
        if n1<=2:
            score1 = 100*n1
        else:
            score1 = 1000*(n1-2)
        # score for fives
        if n5<=2:
            score5 = 50*n5
        else:
            score5 = 500*(n5-2)
        ev += prob*(score1+score5)
    return ev

base_dieA = (0.667,0.067)
die46 = (0.462,0.0)
dieE = (0.368,0.105)
die267 = (0.267,0.267)
die273_182 = (0.273,0.182)
die267_267 = (0.267,0.267)

# Case: original interpretation maybe
config_orig_last_267 = [base_dieA, die46, die46, die46, dieE, die267_267]
config_orig_last_273_182 = [base_dieA, die46, die46, die46, dieE, die273_182]

ev_orig_267 = ev_for_config(config_orig_last_267)
ev_orig_273_182 = ev_for_config(config_orig_last_273_182)
ev_orig_267, ev_orig_273_182

**Tool Output (python)**:


## Assistant



## Assistant

config_swapped_last_267 = [base_dieA, die267_267, die267_267, die267_267, dieE, die267_267]
config_swapped_last_273_182 = [base_dieA, die267_267, die267_267, die267_267, dieE, die273_182]

ev_swapped_267 = ev_for_config(config_swapped_last_267)
ev_swapped_273_182 = ev_for_config(config_swapped_last_273_182)
ev_swapped_267, ev_swapped_273_182

**Tool Output (python)**:


## Assistant



## Assistant

# Focus on just 3 dice scenario to see effect: three dice being A,B,C.
def ev_for_config_simple(dice):
    return ev_for_config(dice)

# Compare triple 46.2 vs triple 26.7 alone (no other dice)
ev_3_46 = ev_for_config_simple([die46,die46,die46])
ev_3_267 = ev_for_config_simple([die267_267,die267_267,die267_267])
ev_3_46, ev_3_267

**Tool Output (python)**:


## Assistant



## Assistant

p=0.462
q=1-p
from math import comb
dist=[]
for k in range(4):
    prob = comb(3,k)*(p**k)*(q**(3-k))
    dist.append((k,prob))
dist

**Tool Output (python)**:


## Assistant



## Assistant

p=0.267
q=1-p
dist=[]
from math import comb
for k in range(4):
    prob = comb(3,k)*(p**k)*(q**(3-k))
    dist.append((k,prob))
dist

**Tool Output (python)**:


## Assistant

dist=[(0,0.393832837),
(1,0.430368489),
(2,0.15676451100000002),
(3,0.019034163000000003)]
ev1 = sum(prob*(100*k if k<=2 else 1000*(k-2)) for k,prob in dist)
ev1

**Tool Output (python)**:


## Assistant



## Assistant

ev5 = sum(prob*(50*k if k<=2 else 500*(k-2)) for k,prob in dist)
ev5

**Tool Output (python)**:


## Assistant



## Assistant



## Assistant

Nice, this makes the picture a lot clearer.

### 1. Comparing the single-die options

Let’s look at **one die at a time**, ignoring triples for a moment:

- A **46.2% on 1, 0% on 5** die:  
  - EV ≈ \(0.462 \times 100 = 46.2\) points per roll.

- A **26.7% on 1, 26.7% on 5** die:  
  - EV ≈ \(0.267 \times 100 + 0.267 \times 50 = 26.7 + 13.35 = 40.05\).

So **even before** we think about triples, each 46.2%–on–1 die is already about **6.1 points better** than the 26.7/26.7 die.

And remember, **1s are always worth twice as much as 5s** (100 vs 50), and triples of 1s are *also* worth twice as much as triples of 5s (1000 vs 500). So the system is heavily biased toward **more 1s, not more 5s**.

---

### 2. With triples included (3 dice only)

To show how strong those 46.2% 1-dice really are, look at just **three dice by themselves**:

#### Three 46.2%–on–1 dice (no 5s)

For each die, \(p(1) = 0.462\). For 3 dice, the chance of getting k ones is:

- k = 0: 15.6%  
- k = 1: 40.1%  
- k = 2: 34.4%  
- k = 3: 9.9%

Using your scoring (100 per 1, but 3 ones = 1000):

- 0 ones → 0  
- 1 one → 100  
- 2 ones → 200  
- 3 ones → 1000  

Expected value ≈  
\(0.401 \cdot 100 + 0.344 \cdot 200 + 0.099 \cdot 1000 \approx 207.6\) points.

#### Three 26.7%/26.7% dice

Now each die has \(p(1)=p(5)=0.267\). For **ones** alone, expected score ≈ 93.4 points.  
For **fives** alone (same probabilities, but 50/500 scoring), expected score ≈ 46.7 points.

Total ≈ **140.1** points from the three dice.

So:

- **3× (46.2% on 1, 0% on 5)** → ~**207.6** points  
- **3× (26.7% on 1, 26.7% on 5)** → ~**140.1** points  

Those high-1 dice are **massively better** once you include the bonus for 3+ ones.

That’s just with those 3 dice. In your full 6-die pool, they’re *even better*, because they combine with the 66.7% and 36.8% 1-dice to hit 3+, 4+, 5+, 6+ ones more often.

---

### 3. So should you swap the three 46.2% dice?

**No. Absolutely don’t.**

Swapping **three 46.2%/0% dice** for **three 26.7%/26.7% dice** would *lower* your total expected score pretty significantly. You’d be:

- Losing a lot of 1s (which are the real moneymakers),
- Gaining some 5s that are worth half as much and have weaker triple bonuses.

So, for maximizing points:

> 👉 **Keep all three 46.2%-on-1, 0%-on-5 dice. They’re way better.**

---

### 4. What about the *last* die: (27.3%, 18.2%) vs (26.7%, 26.7%)?

With your corrected info (the 46.2% dice really have 0% on 5), the trade-off on the last die is very close. Roughly:

- 27.3% on 1 / 18.2% on 5 → slightly more 1s, fewer 5s  
- 26.7% on 1 / 26.7% on 5 → slightly fewer 1s, more 5s

Because your setup is already stacked with strong 1-dice, the **extra 1%–ish of 1s** on the 27.3% die edges out the extra 5s by a *tiny* margin when you factor in triples. It’s a very small difference, but:

> 👉 With the corrected dice, the last die being **27.3% on 1 and 18.2% on 5** is *slightly* preferable.

But the big, non-petty conclusion:

- **Do not replace the 46.2% 1-dice. Those are your monsters.**

