---
type: Conversation
title: "Fire alarm timing settings"
description: "I'm going to be fire alarm timing testing on several dozen of these types of units. I'm going to have to adjust dip switches I think to accomplish thi"
resource: "68b844ce-f3d8-8323-a2e7-ece9866f712f"
timestamp: "2025-09-03T13:43:28.264Z"
tags: ["gpt-5","gizmo"]
---

# Fire alarm timing settings

> **System**:
> 
> 
> [Attachment (Missing from Backup): 2022-IBEW-Constitution_copy.pdf]
> [Attachment (Missing from Backup): 2025-Policy-Brief-Full.3.21.25_copy.pdf]
> [Attachment (Missing from Backup): CBA_553_2025_2027_copy.pdf]
> [Attachment (Missing from Backup): current recovery 2025.pdf]
> 

## User



I'm going to be fire alarm timing testing on several dozen of these types of units. I'm going to have to adjust dip switches I think to accomplish this? Can you find the settings and how to change the timing for these so I don't embarrass myself if we find one out of time?

**Tool Output (file_search)**:


**Tool Output (file_search)**:


**Tool Output (file_search)**:


**Tool Output (file_search)**:


**Tool Output (file_search)**:


**Tool Output (file_search)**:
```

Please remember to search the user's documents if an answer to their question is not contained in the above snippets. You cannot mclick into this file- if needed, you can use msearch to search it for additional information.

```

## Assistant



## Assistant

{"queries": ["fire alarm device dip switch timing settings", "how to adjust +dip switches on fire alarm notification appliances", "synchronization or timing settings for +fire alarm horns strobes", "fire alarm strobe/horn device +programming dip switches", "fire alarm notification appliance time adjustment"]}

**Tool Output (file_search)**:


## Assistant

{"queries": ["fire alarm device dip switch timing settings", "how to adjust +dip switches on fire alarm notification appliances", "synchronization or timing settings for +fire alarm horns strobes", "fire alarm strobe/horn device +programming dip switches", "fire alarm notification appliance time adjustment"], "intent": "answer user question", "source_filter": ["files_uploaded_in_conversation"]}

**Tool Output (file_search)**:


## Assistant

{"queries": ["fire alarm device dip switch timing settings", "how to adjust +dip switches on fire alarm notification appliances", "synchronization or timing settings for +fire alarm horns strobes", "fire alarm strobe/horn device +programming dip switches", "fire alarm notification appliance time adjustment"], "source_filter": ["files_uploaded_in_conversation"]}

**Tool Output (file_search)**:


## Assistant

I couldn’t find anything in the union documents you uploaded about fire alarm dip switch programming—those contracts only cover wages, tools, and working conditions.  

Here’s the deal for your fire alarm timing tests:  
- Those units (horn/strobe notification appliances) use **DIP switches** to set both **candela output** and **synchronization/timing**.  
- If one device is “out of time” with the rest, it usually means the **sync protocol** isn’t set the same (System Sensor, Gentex, Wheelock, etc. each have their own).  
- Typical DIP switch options include:  
  - **Switches for candela (15, 30, 75, 110, etc.)**  
  - **Switches for sync mode (None, System Sensor, Gentex, Wheelock, or SmartSync depending on brand)**  
  - **Some have a temporal 3-pulse vs. continuous horn setting**  

👉 You won’t usually adjust “time in seconds.” You set all devices to the same sync protocol and then the **fire alarm panel handles timing**. The DIP switches just tell the device how to behave when it gets the sync pulse from the panel.

To avoid embarrassment:  
1. Look up the exact manufacturer/model stamped on the back of the device.  
2. Pull the data sheet—it will have the DIP switch table.  
3. Make sure every device on the circuit is set the same way (same sync protocol, same horn pattern if required).  

Do you want me to pull the programming sheet for the exact make/model in your picture? That way I can give you the DIP switch positions directly instead of generic guidance.

## User

There mostly simplex wall mounted horn strobes. Can you find me the data sheets online?

## Assistant



**Tool Output (web.run)**:
```

```

## Assistant

Here’s what I found on Simplex horn-strobes (mostly TrueAlert wall-mount A/V):

---

###  1. Non-Addressable TrueAlert Horn-Strobe (like 4906 Series)

- **Strobe output selection**: Via a **physical jumper** behind the strobe housing. You can set it to **15, 30, 75, or 110 candela**. The jumper is visible and the selected value is flagged by a yellow tab you can see from the side. citeturn0search1turn0search9
- **Synchronization (timing)**: Uses **SmartSync two-wire control** or panel NACs supporting Simplex sync. These strobes automatically flash in sync (about 1 Hz) when hooked to a proper sync circuit—no DIP switch needed for timing. citeturn0search1turn0search9

---

###  2. Non-Addressable Free-Run vs. Synced Modes (4903/4904)

- Some TrueAlert units use **DIP switch SW1** to choose between:
  - **Free-Run** mode (strobe flashes at its own rate, around 1 Hz, whether or not other units sync),
  - or **Synchronous** mode (flashes coordinate with a sync module or compatible NAC).
- Default is **OFF → synchronous** mode. To change to free-run, flip the switch to **ON**. citeturn0search4

---

###  3. Addressable TrueAlert (IDNAC / ES models)

- These use **8-position DIP switches** labeled ADDR1 to assign a unique address on the SLC loop (1–127). DIP switches set the appliance address—timing still handled by the panel. citeturn0search0turn0search2turn0search8turn0search10
- Additional settings (on some models): DIP 8 may set type (ALARM vs ALERT), or color flash (white vs tinted) but nothing about timing. citeturn0search15

---

### TL;DR – What You Need for Timing Tests

| Scenario | What to Check / Set |
|------------|----------------------|
| **4906 Series (wall A/V)** | Ensure **strobe jumper** is set for desired candela (15, 30, 75, 110). Sync happens automatically if panel/NAC supports. |
| **4903/4904 Series (Free-Run vs Sync)** | Set **SW1 DIP** to OFF for **synchronous** (default), ON for **free-run**. |
| **Addressable units (IDNAC / ES)** | Set **ADDRESS via DIP switch**. Timing is managed by panel; no DIP related to sync needed. |

---

###  Next Step

- I didn't find a **single downloadable datasheet PDF** here, but the info above comes from multiple official Simplex documents and installation guides online.
- If you can take note of the **exact model number** (typically printed on the back or inside the housing—numbers like **4906-9127** for wall A/V red, or model prefixes like **4903, 4904**), I can fetch the specific PDF with the full DIP switch tables and settings.

Want me to track down a PDF for a model you’ve pulled? Just give me the exact number and I’ll fetch it for you—so you’re ready to set 'em correctly.

## User


I can't get them off the wall to look. Can you find the model from this picture?

## Assistant

Got it. From the picture, that’s a **Simplex TrueAlert wall-mount horn/strobe** (red, “FIRE” printed, clear lens). The grille style and font match the **4906 series** (specifically 4906-9127, 4906-9128, 4906-9130, etc.).  

That series is **non-addressable**, with the following features:  
- **Strobe candela** is set by a **slide jumper** visible from the side (no DIP switches). Choices are usually **15, 30, 75, or 110 cd**.  
- **Timing/synchronization** is not adjustable on the device. They’re designed for **Simplex SmartSync NACs** or compatible sync modules. The fire alarm control panel (or a sync module) handles timing.  
- The horn tone (temporal 3 or continuous) can be set depending on the model, but usually through the panel circuit type, not DIP switches.  

So if you’re testing timing:  
- Don’t worry about DIP switches—these units don’t have time settings.  
- Just make sure the panel is set to output **SmartSync** on that NAC, so they all stay synchronized.  
- If one is “out of time,” that usually means either it’s on a free-run NAC or it’s not wired to the sync-enabled circuit.  

👉 Would you like me to pull the official **Simplex 4906 installation sheet PDF** for you? That’ll give you the candela jumper diagram and wiring for sync.

## User

Yes please find me the official pdf. 

## Assistant



**Tool Output (web.run)**:
```

```

## Assistant

I tracked down the official Simplex PDF for the **4906-series TrueAlert wall-mounted horn/strobe** you showed in your photo. Here’s the installer sheet you need:

- **Simplex TrueAlert Multi-Candela Horn/Strobe (Wall-Mount A/V)** – model **4906-9127 (red FIRE)** — includes candela selection, wiring, and SmartSync sync info.citeturn0search1

  This PDF lays out:
  - How to install it on standard B-box or 4″ electrical box
  - How to set strobe intensity (15, 30, 75, or 110 cd)—via visible plug and yellow-flag jumper behind the lens
  - How SmartSync two-wire synchronization works with compatible fire panels or modulesciteturn0search1turn0search6

---

###  What’s in the PDF for Your Tests

- **Strobe Candela Selection**  
  You set the candela with a plug behind the lens—pull it out and slide the flag to the needed value (marked in black on yellow). It’s visible from the side so you can confirm it without taking the unit fully off.citeturn0search1

- **Synchronization (Timing)**  
  It flashes at **1 Hz**, in sync, when wired to a **SmartSync NAC** or module. There’s no DIP switch for timing—sync is handled by the panel or SmartSync Control Module.citeturn0search1turn0search6

- **Installation Tips**  
  Front-access wiring, mounting requirements, optional wire guards, color covers, and adapter skirts.citeturn0search1turn0search6

---

###  Quick Summary for Your Timing Check

| Task | What to Do |
|------|-------------|
| **Candela check** | Shine light on the side—look at yellow flag behind lens to confirm 15, 30, 75, or 110 cd. |
| **Sync check** | Make sure the NAC is SmartSync or uses a SmartSync module. If one unit is out of sync, likely it's not on the sync-enabled NAC. |
| **No DIP switch needed** | Timing isn't set on device—panel handles timing. |
| **Need instructions** | Use the PDF to guide candela changes and wiring checks. |

---

Let me know if you want me to pull the full downloadable PDF link or if you need instructions on other models—like ceiling A/V or IDNAC units.

