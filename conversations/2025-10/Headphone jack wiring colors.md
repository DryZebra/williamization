---
type: Conversation
title: "Headphone jack wiring colors"
description: "Looks like headphone jacks are black white yellow green and bare is that right?"
resource: "68eed6b1-4cd0-8325-b1ae-226722699863"
timestamp: "2025-10-14T23:07:55.037Z"
tags: ["gpt-5"]
---

# Headphone jack wiring colors

## User

Looks like headphone jacks are black white yellow green and bare is that right?

## Assistant



## Assistant

Almost! Here’s the typical color code breakdown for **headphone jack wiring** — assuming you’re looking at a **TRRS (Tip-Ring-Ring-Sleeve)** or similar audio cable:

### 🎧 Standard 3.5mm TRRS Headphone Plug (4-pole)
| Wire Color | Signal | Function |
|-------------|---------|-----------|
| **Green**   | Left audio (L) | Left channel sound |
| **Red** or **White** | Right audio (R) | Right channel sound |
| **Yellow** or **Blue** | Microphone | Mic input |
| **Bare / Copper / Black** | Ground | Common return for all |

---

### 🧠 Key Notes
- **Black and white** sometimes replace red and green on older or cheaper headphones.  
- **Yellow** isn’t always used — some cables use **blue** or **red** for the mic instead.  
- **Bare copper** (or sometimes **black**) is **ground** — always confirm with a multimeter continuity test before soldering or crimping.

If you tell me what kind of jack or cable you’re wiring (e.g., “4-pole TRRS to 3 wires,” “aux cord,” “gaming headset with mic,” etc.), I can give you the exact match for your setup.

## User

Isee the white I had was a string to strip. It looks like red black green yellow and bare

## Assistant



## Assistant

Perfect — that helps a lot.  
If your headphone cable has **red, black, green, yellow, and bare (copper)** wires, here’s almost certainly what you’re looking at:

| Wire Color | Signal | Function |
|-------------|---------|-----------|
| **Red** | **Right audio** | Right speaker/channel |
| **Green** | **Left audio** | Left speaker/channel |
| **Yellow** | **Microphone** | Mic input (if your headset has one) |
| **Black** | **Ground (mic ground)** or **common return** | Sometimes mic or shared ground depending on design |
| **Bare / Copper** | **Main ground** | Common shield or return for audio channels |

---

### ⚙️ To Confirm
Use a **multimeter in continuity mode**:
1. Plug in the jack and touch one probe to each ring/tip/sleeve contact.
2. Touch the other probe to each wire to see which one matches.
   - **Tip** → Left (likely green)  
   - **First ring** → Right (likely red)  
   - **Second ring** → Ground (bare or black)  
   - **Sleeve (closest to cable)** → Mic (yellow)

---

### 🧠 Pro Tip
- If both **black and bare** are present, **bare** is usually the true ground/shield, while **black** is mic ground or secondary shielding.  
- Many modern TRRS headsets (CTIA standard) tie the **mic ground** and **audio ground** together internally, so you can usually connect both black and bare to the same ground point if needed.

Would you like me to draw you a labeled wiring diagram for this color setup to make soldering or repairing easier?

## User



It's RAZR it got chewed up by a mouse or something and my neighbor gave it to me for free since I'm an electrician. I got some butt splicers and I'm thinking about reattaching a 3.5

## Assistant

Nice — yeah, that’s definitely a **Razer headset cable**, and you’re totally right that those color codes can look confusing because they use *enameled micro-wires* instead of normal PVC-insulated copper.

From your photos, that looks like the **Razer Kraken/BlackShark-style TRRS** headset cable — they usually follow this pattern:

| Wire Color | Function | Connection on 3.5 mm TRRS plug |
|-------------|-----------|--------------------------------|
| **Red** | Right audio | **Ring 1** |
| **Green** | Left audio | **Tip** |
| **Yellow** | Microphone | **Sleeve (closest to cable)** |
| **Bare copper** | Common ground | **Ring 2** |
| **Black** | Sometimes mic shield or extra ground (can be tied together with bare)** | **Joined to ground** |

---

### 🔧 Wiring steps

1. **Scrape or burn off enamel**:  
   Each colored strand is *enameled*, not plastic-coated. Carefully burn the tips with a lighter or soldering iron until they look silvery, then tin them with solder so you get clean connections.

2. **Confirm channel mapping**:  
   Before crimping or soldering the TRRS plug, use a **multimeter** to check continuity between each ring/tip and the wire you think it matches. (Some older Razer models swap tip/ring for Apple vs. Android standards, but you can swap later if left/right are reversed.)

3. **Connect to your new TRRS jack** (CTIA standard):
   - **Tip** → Green (Left)  
   - **Ring 1** → Red (Right)  
   - **Ring 2** → Bare (Ground)  
   - **Sleeve** → Yellow (Mic)  
   - **Black** (if present) → Tie to bare ground

4. **Crimp or solder**, insulate with heat-shrink, and test before final assembly.

---

Would you like me to make you a simple color-coded diagram showing exactly where each of those five wires goes on a TRRS jack (CTIA pinout)? It’ll make it a lot easier to wire cleanly.

## User

I don't want to get fancy with it. Do I have to solder? Is there no crimp style? Screw style? I don't care about bulkiness

## Assistant

Totally fair — you **don’t have to solder** if you don’t want to. There are a few solid *no-solder* ways to reattach a 3.5 mm plug that’ll hold up fine for testing or even daily use:  

---

### 🔌 1. Use a screw-terminal TRRS plug  
They exist, and they’re perfect for what you’re describing.  
- Search **“3.5 mm TRRS screw terminal plug”** (male).  
- Inside, you’ll see four tiny screw clamps labeled **L / R / G / MIC**.  
- Just strip or burn off the enamel from each wire, twist it tight, and screw it down.  
- Then tie a zip-tie or tape around the strain-relief area to keep the cable from yanking loose.  
✅ *No soldering, re-usable, slightly bulky but clean.*

---

### 🧰 2. Use small **butt connectors / crimp sleeves**  
Since you already have butt splicers:  
- Cut a short length of normal audio cable with a **known-good 3.5 mm plug** (like an old aux cord).  
- Strip both sides.  
- Match **green→left**, **red→right**, **yellow→mic**, **bare→ground**.  
- Crimp, tape or heat-shrink.  
✅ *Bulky but works perfectly; quick and dirty repair.*

> ⚠️ Those headphone wires are enamel-coated “litz” wires, so before crimping you **must** scrape or burn off the lacquer — otherwise the metal inside won’t make contact.

---

### 🧱 3. Terminal block or wire-nut method (super-temporary)  
If you just want to *hear* if the speakers still work,  
use a small 4-position terminal block or even tiny wire nuts, match colors, and clamp down.  
✅ *Bulkiest but zero tools required.*

---

If you want to keep it permanent *and* clean without solder, I’d go with **Option 1 (screw-terminal plug)**. They cost about $5–8 and make these repairs easy forever — just strip, insert, tighten, done.

Want me to link you a good example of the exact TRRS screw-terminal plug that’ll fit your Razer headset wiring?

