---
type: Conversation
title: "IT and electrical tasks"
description: "Can you give me a list of stuff I can do inside people's houses that's related to IT and electrical and the electrical side of HVAC (like tstat instal"
resource: "68f24b43-9024-8320-8e8e-c07a7b037140"
timestamp: "2025-10-17T13:59:20.131Z"
tags: ["gpt-5","gizmo"]
---

# IT and electrical tasks

## User

Can you give me a list of stuff I can do inside people's houses that's related to IT and electrical and the electrical side of HVAC (like tstat install for Nest products) without having an NC electrical license? Every single thing I'm allowed to do as an LLC. 

## Assistant



## Assistant



**Tool Output (web.run)**:
```

```

**Tool Output (web.run)**:
```

```

## Assistant

Hey — good question. I’m not a lawyer, so don’t take this as legal advice — always double-check with NC state law and your local city/county code. But I can walk you through how I see the boundaries (from what I found) and suggest things you *probably* can do (or push to do) as an LLC *before* you get a full electrical contractor license. Use this as a starting point, then run it past the state board / county inspectors.

---

## What NC law says (key constraints)

Here are some relevant NC statutes and rules that paint the legal boundary:

- Under NC law, “electrical contracting” means installing, maintaining, altering, or repairing wiring, devices, appliances or equipment. You can’t engage in that business without a license. citeturn0search11turn0search0turn0search13  
- The NC Board of Examiners of Electrical Contractors says that a license is required for wiring work (the part “beyond” the power supplier’s side) in many cases. citeturn0search1turn0search0  
- But there is an explicit **exemption** for *installation or servicing of electrical appliances or equipment which is cord-connected via a plug to a receptacle*, or servicing equipment supplied via wiring connected to a junction box (i.e. “appliance-level work”) citeturn0search1  
- Also, NC prohibits “offering to engage or engaging in electrical contracting without being licensed.” citeturn0search31  

What this boils down to: any work that touches “wiring systems” (i.e. altering circuits, installing fixed wiring, running new branch circuits, pulling new cables, installing junction boxes, etc.) is in the risky zone if you don’t have the proper license. But work that is limited to “appliances / equipment connected to existing receptacles / junction boxes” is more likely to be allowed under the exemption.

However — “allowed under exemption” is not guaranteed in every jurisdiction. Local city or county codes might impose stricter standards. Also, even if legally allowed, doing bigger electrical jobs without permit or inspection will raise red flags.

---

## What you *can more safely* do (or try to do) as an LLC without a full NC electrical license

Here’s a list of tasks related to IT, low-voltage, HVAC controls, and “appliance-level” electrical work that are more defensible under the exemption or are low-risk. Use this list as a menu you can push to your local code enforcement to confirm:

| Task | Why it’s safer / rationale | Caveats & checks you must make |
|---|---|---|
| **Thermostat / smart thermostat installation / replacement** (e.g. Nest, ecobee) | Usually involves low-voltage wiring (control wires) or swapping devices on existing wiring, not adding high-voltage lines. | Make sure you are *not* altering 240V or 120V main wiring. Confirm local HVAC or electrical inspectors allow replacing thermostats. |
| **Low-voltage wiring and devices** (e.g. Ethernet, data cable, coax, CCTV, doorbells, security systems) | These generally don’t count as “electrical contracting” in the same sense as power wiring. | Some jurisdictions treat some low-voltage systems more strictly; always check with local permitting. |
| **Network / structured cabling** (Cat 5e / Cat 6 / fiber) | Same as above — low-voltage, IT-side work. | Be careful if you run across panels, conduit, or call for power taps. |
| **Wi-Fi / mesh / router / switch installation, relocations** | These are pure IT tasks, no changes to fixed power wiring. | None, as long as you don’t touch fixed wiring. |
| **Surge protector / UPS system installation (plug-in, not hardwired)** | If it’s a plug-in or near plug-in (appliance-level) it may fall within the exemption. | Don’t hardwire it or tap into the fixed wiring unless licensed. |
| **Smart lighting / smart switch / smart plug installs, if on existing circuits** | Replacing existing switches/plugs (if allowed). | Avoid adding new wiring runs. Be careful with local codes: switching circuits, box fill, etc. |
| **HVAC control wiring / damper motors / zone control wiring** | These are often low-voltage and part of the control system, not the heavy power side. | Avoid going into blower motors, power wiring, or capacitor block connections. |
| **Alarm / fire / smoke detector systems (low-voltage)** | These are often treated under special “fire alarm / low-voltage” classes. | Some states require special restricted low-voltage license, check NC’s special-restricted classifications. citeturn0search4 |
| **Maintenance, troubleshooting diagnostics, minor repairs (on the “appliance side”)** | Like replacing fuses, replacing a damaged cord, swapping modules in a pre-existing system. | Do not modify or extend fixed wiring. |
| **Consulting, design, planning, site surveys, audits, documentation** | Doing the design and plan, cost estimates, diagrams – you're not doing the wiring yourself. | If you draw plans that specify unlicensed wiring changes, double-check that the client knows licensed work may be needed. |
| **Inspection prep, code compliance advice, client training** | You can help clients get ready for inspections, show them how to use systems. | Avoid stepping into the “install or repair wiring” domain. |

As you do more of this, build relationships with local electrical inspectors, trade associations, etc., so you understand exactly what your county / city allows.

---

## What you *should avoid* until you’re properly licensed

- Running new branch circuits (e.g. new 120V or 240V lines)  
- Pulling new cables beyond patchwork (i.e. major rewiring)  
- Touching load side of breaker panel or subpanel modifications  
- Installing or altering junction boxes (beyond accessory devices)  
- Hardwiring appliances or devices that should be plug-in  
- Any “wiring installation” broadly defined under NC law, insofar as it’s not exempt  
- Advertising yourself as doing “electrical contracting” if you’re unlicensed — that might violate the statute about “offering to engage” in contract work without a license. citeturn0search31turn0search11  

---

## Steps to make this solid / mitigate risk

1. **Talk to your local county / city inspectors or permit office** and get in writing (or via email) which specific tasks they consider “licensed electrical work” vs what they’ll allow under exemption.  
2. **Document everything in your contracts**, specifying exactly what you will and will not do (power wiring excluded, etc.).  
3. **Get general liability insurance** (and see if you need E&O) — if something goes wrong, you want protection.  
4. **Train heavily** in code, safety, and best practices — even if the law allows you to do something, doing it poorly can land you in trouble.  
5. **Eventually get that electrical license** — it's a gate that unlocks a lot more work and credibility.  

---

If you want, I can dig up *your specific county*’s rules (Hillsborough / Orange County, NC) and see exactly what’s permitted locally. Do you want me to do that for your area?

## User

What about, say, swapping a switch of one is broken?

## Assistant

That one — *replacing a broken light switch* — sits right on the edge of the law in North Carolina. Here’s how it breaks down:

---

### 🧠 The legal core
Under **NC General Statute §87-43**, *electrical contracting* includes *“installing, maintaining, altering, or repairing any wiring, devices, appliances, or equipment”* for electrical light, heat, or power.  
That means even swapping a switch is technically *repairing a device* that’s part of the fixed electrical system — and therefore, **requires a licensed electrical contractor** (or someone working under one).

So by the letter of the law:  
> 🔴 *No*, you cannot legally swap out a light switch in someone else’s house for pay **without** holding at least a Limited Electrical Contractor license or working under one.

---

### ⚙️ The practical reality
Now, in practice:

- **Homeowners** can do their own switch replacements on their own property (with or without a permit depending on jurisdiction).  
- **Handymen / LLCs** cannot legally do it for *hire*, even if it’s just “two screws and done.”  
- Inspectors usually won’t bother if you’re doing minor repair work as part of a larger IT / smart-home install — *but legally they could.*

---

### ⚖️ The safe workaround
If you want to stay 100% compliant while still monetizing the work:

1. **Offer “smart device installation”** only when the customer removes the switch themselves.  
   - You guide, label wires, advise which product fits.  
   - They reconnect or you supervise (like “consulting / assistive install”).  

2. **Partner with a licensed electrician** for simple call-outs.  
   - Many small electrical contractors *love* getting easy $75 jobs you hand them.  
   - You keep the IT, low-voltage, and smart-home side — they do the high-voltage swap.  

3. **Get your Limited Electrical Contractor license.**  
   - Costs under $200 to sit for the test, and opens the door to anything up to $50,000 jobs per project.  
   - You can then legally replace switches, outlets, breakers, light fixtures, etc.  

---

### ✅ Summary

| Task | Legal w/o license | Risk level | Notes |
|------|--------------------|-------------|-------|
| Replace broken light switch for homeowner | ❌ No | High | Counts as electrical contracting |
| Advise homeowner as they replace it | ⚠️ Maybe | Low | Advisory only, not physical wiring |
| Replace thermostat (low-voltage) | ✅ Usually | Low | Still confirm it’s under 50V |
| Replace smart plug or Wi-Fi switch (plug-in) | ✅ Yes | None | Not hardwired |
| Replace outlet or hardwired fixture | ❌ No | High | Needs license |

---

If you’d like, I can show you the **fastest path to the Limited Electrical Contractor license** — including cost, experience hours, and exam content — so you can legally do those simple switch and outlet swaps yourself. Want me to outline that?

