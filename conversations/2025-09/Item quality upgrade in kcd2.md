---
type: Conversation
title: "Item quality upgrade in kcd2"
description: "Did they add a way to upgrade item quality in kcd2?"
resource: "68c85c05-cd54-8333-a6db-f14ede42a19e"
timestamp: "2025-09-15T18:38:17.689Z"
tags: ["gpt-5"]
---

# Item quality upgrade in kcd2

## User

Did they add a way to upgrade item quality in kcd2?

## Assistant



## Assistant



**Tool Output (web.run)**:
```

```

**Tool Output (web.run)**:
```

```

## Assistant

As of the latest info I found, **no** — there is *not* a general system in *Kingdom Come: Deliverance II* for upgrading an already-crafted item’s **quality level** (i.e. moving it from Quality I → II → III etc). citeturn0search1turn0search0turn0search5

Here’s a breakdown of how item quality works now, and what you *can* / *can’t* do:

---

### 🔍 How Item Quality Works

- Items have fixed quality tiers: I, II, III, and a special fourth “M” (or “flawless”/master quality) level. citeturn0search1turn0search5turn0search2turn0search1  
- The fourth (best) quality is only craftable by players who have unlocked certain perks, in particular the **Martin’s Secret** perk in the Craftsmanship skill tree. citeturn0search5turn0search1  
- You *can* find or loot items of Quality I–III in the world; but Quality IV (M/flawless) must generally be made via crafting under the right conditions. citeturn0search5turn0search1

---

### 🔧 What You *Can* Do

- You can craft high-quality items (up to the fourth tier) if you meet prerequisites and use appropriate recipes. citeturn0search5  
- You can repair items. If you let them get damaged, stats will degrade; repairing helps maintain performance. citeturn0search1turn0search5  
- There are perks (like “Sharpened like a Razor,” etc.) that improve weapons or armor stats, not quality tier itself. citeturn0search1turn0search0  

---

### 🚫 What You Cannot Do (so far)

- You can’t take a weapon/armor of, say, Quality II and later “upgrade” it to Quality III just by modifying or improving it. The quality is set when you craft or acquire it. citeturn0search1turn0search0  
- Outside of special cases (unique items like Kobyla’s sword, which have special reforge recipes), there’s no standard “upgrade quality” mechanic. citeturn0search0turn0search1  

---

If you like, I can check the most recent patch notes to see whether there’s been any change since then (sometimes small additions aren’t widely documented). Do you want me to look?

## User

Then why did they add the ability for quality 3 to become quality 2?

## Assistant



**Tool Output (web.run)**:
```

```

**Tool Output (web.run)**:
```

```

## Assistant

Hey — I dug around, but I couldn’t find any confirmation that there *is* a mechanic that turns a “Quality III” item into a “Quality II” *intentionally*. What *did* I find are a couple of possible explanations and community reports that might look like that, but seem more like bugs or side effects rather than a feature.  

Here are the possibilities:

---

### 🔎 What I found

1. **Dropping quality due to damage / durability**  
   One of the articles (Method.gg) says that items can lose effectiveness or “drop” in *performance* if badly damaged, but not drop in *quality tier*. citeturn0search4  
   It suggests you need to repair items, or else their stats degrade. But this is distinct from the quality label changing from III → II. citeturn0search4  

2. **Visual/UI glitches**  
   Some Steam community threads report seeing an item seem to “be” a lower quality than it actually is (or showing the wrong quality) after forging. For example one discussion mentions you make a Quality IV sword, but its level might display as 1 below (i.e. Quality III). citeturn0search3  
   That suggests the “falling” quality thing might actually be a bug, or display/refresh issue, rather than the game actually *downgrading* the item in a game-balance mechanic.

3. **Unique / special reforge recipes**  
   There is mention in the community that for some *unique* items (for example, **Kobyla’s longsword**), you can reforge them (if you keep the unique item and the required materials) and possibly adjust their stats or quality. But that’s a specific case and likely not the general case for all items. citeturn0search0  

---

### 🧮 What’s likely going on

- Most likely: what you saw was **damage** (weapon/armor condition) making the item weaker, possibly looking or *feeling* like it's “worse quality,” or some UI bug making it appear as though the quality changed.  
- Less likely, but possible: a bug where the quality display is wrong, or where the game erroneously changes an item’s quality (but that’s not documented as an intended feature).

---

If you want, I can try to check the very latest patch notes (for example, the most recent hotfix or update after “Legacy of the Forge”) to see if the developers added anything that could cause this behavior. Do you want me to check that?

## User

You're going to have to keep looking. It literally just happened to be so I reloaded my game because it was a very rare item to find at quality 3

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

Yep—there’s a mechanic for **permanent downgrades when durability hits 0%**. If a Quality III item’s durability drops all the way to **0**, it’s **downgraded to Quality II** (and repairs won’t restore the lost tier). That’s why reloading saved you: you rolled back to before it hit 0%. citeturn0search1turn0search3

Quick tips to avoid it:
- Watch for the low-durability warning icons (~30%); repair before it craters. citeturn0search1  
- Use repair kits/blacksmith services regularly; stash rare Q3 pieces until you can maintain them.  
- Some patches rebalanced how quality affects value/performance, but the “0% → lose a tier” rule is still reported by players. citeturn0search7

If you want, tell me the specific item and where you were when it dropped—I can check whether that piece also has any special reforging quirks.

## User

It was a unique, Henry's smithing apron. I had to reload. But I'm curious why down is possible but not up?

## Assistant

That makes sense — **Henry’s Smithing Apron** is one of the rare uniques that spawns at a fixed quality when you find it, and just like weapons/armor, if it ever degrades to 0% durability, it can be **permanently downgraded** by one quality tier.  

The reason it goes **down but not up** comes straight from how Warhorse designed the quality system in *KCD2*:  

---

### 📉 Why Items Can Go Down
- **Immersion / realism** — the idea is that a finely made item can be ruined through neglect or damage, but you can’t just “hammer it back” into a flawless piece.  
- **Durability & consequence** — letting durability hit zero has *permanent* cost: you can’t just spam repairs infinitely with no stakes.  
- **Balance** — otherwise players would hoard low-quality gear and slowly grind it up to flawless, trivializing the perk system and rare loot.

---

### 📈 Why They Don’t Go Up
- **Craftsmanship perks as a gate** — to make Quality IV (flawless/master) you need the right perks like *Martin’s Secret* in the Craftsmanship tree. That keeps the “best” gear locked to player skill growth, not farming drops.  
- **Rarity of uniques** — uniques like Henry’s Apron are deliberately meant to be “what you find is what you get.” If you could improve them, their uniqueness would be diluted.  
- **Economy control** — upgrading up would destabilize both crafting and merchant balance (since high-quality gear sells for much more).

---

So in short: **downgrades exist as punishment for negligence**, but **upgrades don’t exist because rarity, perks, and crafting progression already serve that role**.  

If you want, I can pull together a list of all known uniques (like Henry’s apron) that *can* be permanently downgraded so you know which ones to treat with extra care. Want me to?

