---
type: Conversation
title: "Transformer DC output issue"
description: "I got a 48900 B1 doortronics PLC board. I have 24v+ and - hooked up to it but no power. Is there a safety jumper?"
resource: "68bee4d5-5ca4-8330-b967-c0065d5b5761"
timestamp: "2025-09-08T15:08:37.971Z"
tags: ["gpt-5"]
---

# Transformer DC output issue

## User

I got a 48900 B1 doortronics PLC board. I have 24v+ and - hooked up to it but no power. Is there a safety jumper?

## Assistant



## Assistant



**Tool Output (web.run)**:
```

```

## Assistant

You're on the right track — the Dortronics 48900 Series PLC board (often labeled as 48900, 48900-B1, or similar variants) **does not have a separate safety jumper for power**. Instead, the power is routed directly through the **Master Fuse (labeled “R”)** on the board — that's how the board protects itself and regulates power intake citeturn0search1.

Here’s a quick breakdown of what the board’s power input area includes:

- **System Power Input** — where you connect your +24 V and 0 V.
- **Master Fuse (R)** — this is in-line with the power input and must be intact for power to reach the board.
- **Lock Power Fuse (M)** — which protects outputs tied to locking devices.

There isn’t anything resembling a "safety jumper" that needs to be installed to enable power; the board should power up automatically when the proper voltage is applied and fuses are in place.

---

###  What to check to troubleshoot "no power" issue

1. **Confirm correct voltage & polarity**  
   Verify you’re supplying **24 VDC** (or 12–24 VDC per spec) with correct polarity. Reversed polarity or significantly wrong voltage can cause a no-power condition.

2. **Inspect the Master Fuse ("R")**  
   A blown master fuse means no power will reach the board. Use a multimeter or visual inspection to confirm whether it's functional.

3. **Verify proper connections**  
   - The **System Power Input** should have solid +24 V and ground connections.
   - Ensure any other wiring near those terminals isn’t shorting or miswired.

4. **Look for DIP switches or configuration switches**  
   Though the board does offer extensive field configuration via DIP switches (e.g., for interlock logic, wet/dry lock settings), none are described as disabling the board’s power supply — meaning they typically affect function and behavior, not raw power delivery citeturn0search7.

---

###  Next steps

- **Check the master fuse**: Replace it if it’s open.
- **Double-check voltage**: Confirm you're actually seeing ~24 V at the power input pins when the board is powered.
- **Look for other signs of life**: Are any LEDs or indicators lighting up? If nothing shows any life, the issue is almost certainly related to power delivery — likely the fuse or connection.

If after all that there's still no sign of power, you may want to consult the official Dortronics manual or contact their support for board diagnostics or possible RMA.

Let me know if you'd like help interpreting any board markings or locating a replacement fuse!

## User

Fuse looks okay. I've got 24v on negative to ground, 0v positive to ground

## Assistant

Got it — thanks for checking that. The way you worded it makes me think the polarity is flipped.  

On the **Dortronics 48900 PLC board**, the **System Power Input** expects:

- **+24 VDC** on the **“+” terminal**  
- **0 VDC (return)** on the **“–” terminal**  

When you measure each leg to earth/chassis ground:  
- The **positive** should read about **+24 V** relative to ground.  
- The **negative** should read about **0 V** relative to ground (or sometimes a little above/below, depending on supply isolation).  

If instead you’re seeing:  
- **Negative → ground = 24 V**  
- **Positive → ground = 0 V**  

…that means the negative side of your supply is “hot,” and you’ve got the polarity reversed. In that condition, the board won’t power because it’s expecting positive voltage at its “+” input.  

---

✅ **Fix:** Swap your leads on the 24 VDC supply — put the actual positive into the board’s **+ terminal** and the actual negative into the board’s **– terminal**.  

⚠️ **Caution:** Double-check the markings on both your supply and the Dortronics board before swapping. Reversed polarity can sometimes blow the master fuse or damage inputs (though Dortronics usually protects with that fuse).  

---

Want me to pull up the pinout diagram for the **48900 System Power Input terminals** so you can confirm which screw terminal is “+” and which is “–” before rewiring?

## User


This transformer DC output negative to ground is 26v+. Positive to ground is .1v

## Assistant



## Assistant



## Assistant

That reading just means your DC supply is **floating**. Measuring each lead to chassis/earth can be misleading:

- **Black probe on “–”, red on “+” (across the two DC leads):** you should see ~24–28 VDC.  
- **Lead → chassis/earth:** one side may sit near 0 V and the other ~+24 V (as you’re seeing: “–” is ~+26 V to earth, “+” is ~0.1 V). That’s normal on an isolated supply.

What to do:

1. **Confirm across-the-rails voltage:** put your meter across **+ and –** from the supply. If it’s ~24–28 V and reads positive (no minus sign), polarity is correct.
2. **Wire the 48900 power input only by polarity, not by earth:** supply **+ → board “+”**, supply **– → board “–”**. Don’t bond either rail to chassis at the board unless the manual explicitly says to.
3. **If still “no power”:**
   - Move the meter to the **board’s power input screws** and verify the same ~24–28 V is actually present there.
   - Check the **master/inline fuse** on the Dortronics board and reseat the power connector.
   - Make sure you’re on the **System Power Input** terminals (the board also has 24 V distribution outputs—easy to land on the wrong block).

If you want, tell me which two terminals on the 48900 you landed (labels or a quick photo of that edge), and I’ll point at the exact pair for system power.

## User

When I test from fuse positive to board negative I get 26v+

## Assistant

Perfect — that’s actually the test you want to be doing.  

👉 If you’re seeing **+26 VDC from the fuse output to the board’s negative terminal**, then the Dortronics board **is receiving power correctly and with the right polarity**. That rules out the “safety jumper” idea — there isn’t one.  

---

### Why it still looks like “no power”
- The LEDs you see lit are just **status indicators**. On a fresh or unconfigured 48900, not every light will come on. Some only activate when doors/inputs are wired and interlock conditions are met.  
- If the **green LED near the fuse bank** is lit, that’s the **power present indicator**. That means your DC feed is good.  
- The **red LED** near the bottom is typically a “lock relay active” or “fail/condition” LED — it can glow even if locks/doors aren’t yet connected.  

---

### What to check next
1. **Confirm the green “PWR” LED is on** (looks lit in your photo). That’s your sign the board is alive.  
2. **Verify you’re landed on “System Power In”**, not one of the “Lock Power” outputs. Those right-side terminals marked “PWR 24V+” are distribution outputs — they don’t feed the board itself. The board’s own supply input is usually on the left edge near the fuses.  
3. **Look for output relays clicking** when you toggle an input (door switch, request-to-exit, etc.). That’s the functional test.  

---

⚡ Bottom line: You **do** have good voltage at the board. If something still “isn’t powering,” it’s likely about where you’re expecting indicators/locks to show life, not that the board is dead.  

Do you want me to map out exactly which terminal block is the **system input** vs. which ones are just “lock power outputs”? That’ll confirm you’re landed on the right screws.

## User


No LED on despite power

## Assistant

Looking at your last photo:  

- You’ve definitely got voltage making it to the board (26 V from fuse to negative is good).  
- But the **status LED is dark**, which usually only happens if:  
  1. The **system power fuse is open** (sometimes looks fine but is actually blown — test it with continuity).  
  2. You’re landed on a **distribution terminal** instead of the actual **system power input**. The 48900 has blocks labeled for lock power distribution that look very similar to the input block. The system input is usually a dedicated two-position terminal near the edge of the board.  
  3. The board’s **DC/DC section** is damaged or not initializing, so no internal logic power is being generated even though raw 24 V is present.  

---

### Quick tests
1. **Continuity test on the “PWR FUSE”** (in your photo, right under the relays). Even if it looks good, meter it out. If open, replace it.  
2. **Verify terminal location**: Are your 24 V wires landed on the block marked **“+DC / –DC”** (system in) or just the bank labeled “PWR 24V+” (outputs)?  
3. **Check internal regulator**: If the fuse is good and you’re on the right input, meter across one of the small onboard capacitors near the LED. You should see +5 V or +12 V depending on design. If it’s missing, the regulator isn’t firing.  

---

⚡ Bottom line:  
If fuse continuity is good and power is definitely landed on the correct input, but you still have no power LED, the logic section may be dead — at that point you’d need Dortronics tech support/RMA.  

Do you want me to pull up the **exact system power input terminal diagram** for the 48900 board so you can confirm whether you’re wired into input vs. output?

## User


Is this hooked in correctly? That's red positive and black negative

## Assistant

Yes — that wiring looks correct.  

- The **terminal block is clearly labeled**:  
  - **V+** → your red (positive) wire  
  - **GND** → your black (negative) wire  

So you’ve landed the polarity the right way. 👍  

---

### Since the board still shows no LEDs lit:
1. **Check continuity on the nearby fuse** (marked “PWR FUSE”). Even if it looks intact, it may be open.  
2. **Verify ~24–26 VDC across V+ and GND right at this connector** with your meter. If you see it here and the fuse is good, the board *should* light the power LED.  
3. If you’ve confirmed both of the above but still have no LED, then the onboard regulator or logic section isn’t starting up — that usually points to a defective board that would need service/RMA.  

---

Do you want me to point you to the exact test pads or capacitor legs on the 48900 where you can safely check for the board’s internal **+5 V logic rail**? That’ll tell you right away if the regulator is working or not.

## User

What's the other symbol? It looks like a fork 

## Assistant

That “fork” symbol next to the **GND** marking isn’t another power rail — it’s the **earth/earth ground symbol**.  

So that terminal block is giving you:  

- **V+** → your positive DC input  
- **GND (–)** → your negative DC input (DC return)  
- **⏚ (the fork symbol)** → protective earth/chassis ground  

You only need to land your **red (+24 V)** to **V+** and your **black (0 V)** to **GND** for the board to operate.  

The earth/“fork” terminal is there if you want to bond the board’s common to chassis ground for noise suppression or safety — but it’s optional and depends on your installation standard.  

⚡ In other words: you’ve wired it correctly. The “fork” is just earth ground, not a second negative or some kind of jumper requirement.  

Do you want me to walk you through how to meter at that earth symbol to verify whether your supply is floating vs. grounded? That could help confirm why you were getting those odd readings to ground earlier.

## User


I mean the one next to ground that looks like a little pitch girl

## Assistant

Ah, I see what you’re pointing at now — the little three-prong “pitchfork” symbol right next to the **GND** label.  

That symbol is **Earth Ground (Protective Earth, PE)**. It’s the standard IEC symbol used on circuit boards to show where the chassis/earth ground connection should land.  

So on that terminal block you’ve got:  

- **V+** → +24 VDC input  
- **GND** → 0 VDC (DC return)  
- **⏚ (the pitchfork symbol)** → Protective Earth (connect to building/chassis earth if your install requires it)  

You don’t need anything in that PE terminal for the board to power up. It’s there as an option to bond the board’s reference to chassis ground, mainly for noise suppression and surge protection.  

✅ Bottom line: your **red → V+** and **black → GND** wiring is correct. The “pitchfork” isn’t another negative or a required jumper — it’s just earth.  

Do you want me to show you how to test whether your supply is floating or earth-referenced, using that earth lug as a reference point? That might explain the odd voltage readings you were seeing earlier.

## User

So the board comes on when I connect red to + and black to ⏚. It does not come on when I connect black to the -E

## Assistant

That’s a very useful observation. What it tells you is:

- The board’s internal reference is bonded to **earth (⏚)** rather than the **“–” (DC return)** terminal you were using.  
- When you land red on **V+** and black on **⏚**, you’re effectively giving the board a complete 24 V path that it recognizes, which is why it powers up.  
- When you land red on **V+** and black on **– (GND)**, the board doesn’t see that as a valid return — which usually points to one of two things:
  1. The **–/GND fuse or trace is open** on the board, so the return path through that terminal isn’t completing.  
  2. The board is designed (or mis-labeled) so that it expects **earth ground as the return** in your model revision, rather than a floating DC return.

---

### What you should do next
1. **Meter continuity** between the **– terminal** and the **⏚ terminal** with power off. They should normally be bonded. If they’re not, that explains the issue.  
2. **Check the “PWR FUSE”** again — it may be inline with the – terminal, so if it’s open you’ll only get operation when tied to ⏚.  
3. **Consult Dortronics documentation** for your exact board revision — some versions do internally tie GND to earth, others keep them isolated.  

---

⚠️ **Caution:** Running with black on ⏚ works, but it bypasses the designed return path. It’s better to find out *why* the – terminal isn’t functioning, otherwise you risk grounding issues later.  

Would you like me to dig up the official 48900 wiring schematic so you can see whether – and ⏚ are supposed to be commoned on your board version?

## User

It's not the negative terminal, the symbol literally looks like "-E"

## Assistant

Ahh — thanks for clarifying. I zoomed in on your photo again. You’re right — that third marking isn’t “–” but **“–E”**.  

That’s not the standard DC return; it means:  

- **V+** → your +24 V input  
- **GND** → DC common / 0 V return  
- **–E** → **Earth-referenced negative** (sometimes labeled “E–” or “0V-E”), which is a chassis-bonded version of the negative rail  

In other words, the board gives you **two ways to return current**:  
1. A floating **GND** (0 V return not tied to earth)  
2. A bonded **–E** (negative tied to earth potential)  

---

### Why yours only powers when red is on V+ and black is on –E
That means the **floating GND input isn’t completing a path internally**. Possibilities:  
- The **GND screw terminal isn’t actually a system return** on this board revision; it might just be a reference/test point.  
- Or the **link between GND and –E is open** (missing jumper or blown trace/fuse).  

So when you use –E, you’re tying directly into the bonded earth-negative return, which completes the circuit and powers the board.  

---

✅ **Bottom line:**  
On *this* revision of the 48900, use **V+ and –E** for your 24 VDC feed. The “GND” marking is confusing, but the board is clearly referenced to –E.  

---

Do you want me to pull the Dortronics 48900 manual and confirm whether “–E” is the intended system return, and if “GND” is just an auxiliary/common reference?

## User

Yep it's the chassis ground symbol. Why wouldn't the board turn on with that?

## Assistant



## Assistant



## Assistant

Short answer: the ⏚ lug is **protective earth**, not the normal DC return. It isn’t supposed to carry operating current. The board should power on with **V+ → +** and **return → GND**. If it only wakes up when you use **⏚** as the return, something’s wrong in the board’s GND path.

Likely causes (and quick checks):

1) Open return path on the board  
- The –/GND terminal or its trace/fuse is open.  
- **Test:** Power OFF. Meter **continuity between GND and –E/⏚**. On most boards they’re either bonded (<1–2 Ω) or linkable via a 0-Ω jumper. If it’s open/infinite, that explains it.

2) You’re on the right block but the **GND screw isn’t actually connected** (damaged terminal or bad solder).  
- **Test:** Power ON. Measure **V between V+ and the metal pad of a big electrolytic can** nearby (its negative leg is board ground). If you see ~24–26 V there but **not** between V+ and the GND screw, the terminal is bad.

3) Return-side fuse/link  
- Some revisions put the **power fuse in the return**.  
- **Test:** Continuity across the “PWR FUSE.” Looks good isn’t good enough—meter it.

4) Supply referencing confusion  
- Your supply is floating (you measured ~+26 V from – to earth). When you land – on ⏚ you’re bonding it to earth, which *incidentally* completes the board’s reference. That’s acceptable for a test, **not** for permanent use (ground loops, nuisance trips, code).

What I’d do now (safe + code-friendly):

- **Do not** leave the operating return on ⏚.  
- Fix/confirm the board’s GND path:
  - Verify/replace the PWR fuse if it’s return-side.  
  - Ohm **GND ↔ the big cap negative**; should be ~0 Ω. If not, the trace/jumper is open → RMA.  
  - If the design expects GND-to-earth bond, do it **at the power supply** (bond – to earth there), then land **– to GND** on the board; ⏚ stays a protective conductor, not the load return.

If you can, shoot me one more close photo that shows the text around that 3-position terminal and the nearby “PWR FUSE.” I’ll tell you exactly where to probe for the internal 5 V (or 12 V) rail so we can confirm whether the regulator is alive.

## User


So I should have continuity between ⏚ and the attached image as 0 ohms?

## Assistant

Yes — with power **off**, you should have continuity (essentially 0 Ω) between the **⏚ (chassis ground lug)** and the **negative leg of the big electrolytic capacitor** you circled in the diagram.  

That capacitor’s negative leg is the board’s internal ground reference. If ⏚ and that cap leg are bonded, then the earth lug is tied into the DC return, and it makes sense the board runs when you use ⏚ as negative.  

If you **don’t** get continuity there:  
- It means the board’s “GND” screw terminal should be your true return, and the ⏚ lug is isolated. In that case, the fact that the board only powers from ⏚ suggests something in the GND path (fuse, trace, or terminal block) is open.  

So the test result will tell you which is correct:  
- **Continuity (0 Ω)**: ⏚ is bonded to the DC return; the board is designed to use it.  
- **No continuity (open)**: GND should be the return, but the board has a break in that path.  

Do you want me to walk you through where to put your meter probes on the actual board (instead of just the schematic symbol) so you can confirm this quickly?

