---
type: Conversation
title: "Transformer Wiring Rubric"
description: "I'm trying to create a rubric for my students doing a final exam where they're supposed to teach me how to wire a transformer (480 delta to 208 wye). "
resource: "68431e2c-5df4-8003-a65b-4fddfaa34710"
timestamp: "2025-06-07T12:36:31.043Z"
tags: ["gpt-4o"]
---

# Transformer Wiring Rubric

## User

I'm trying to create a rubric for my students doing a final exam where they're supposed to teach me how to wire a transformer (480 delta to 208 wye). I want them to demonstrate knowledge of 3 phase power, transformation via winding ratios, and the difference between delta and wye, how to read a transformer nameplate, and how to physically wire it. 

## Assistant



## Assistant

Great. Here's a clear, structured rubric for evaluating your students' ability to teach you how to wire a 480V delta to 208V wye transformer. I've broken it into 5 key categories, with each worth up to 20 points, totaling 100 points:

---

## **Final Exam Rubric: Teaching Transformer Wiring (480Δ to 208Y)**

### **1. Understanding of 3-Phase Power (20 points)**
| Criteria | Points |
|---|---|
| Explains 3-phase voltage relationships clearly (line-to-line vs. line-to-neutral) | 5 |
| Describes rotation and phase sequence (A-B-C or C-B-A) and why it matters | 5 |
| Identifies unbalanced loads, harmonics, or other potential issues in 3-phase systems | 5 |
| Answers basic troubleshooting questions or scenarios correctly | 5 |

---

### **2. Transformation Principles and Winding Ratios (20 points)**
| Criteria | Points |
|---|---|
| Correctly explains turns ratio and voltage transformation (e.g., 480 to 208 phase-to-phase, 120 phase-to-neutral) | 10 |
| Connects primary and secondary voltage relationship to winding connections | 5 |
| Demonstrates understanding of kVA ratings and how to size/load a transformer | 5 |

---

### **3. Delta vs. Wye Configuration (20 points)**
| Criteria | Points |
|---|---|
| Describes physical and schematic differences between delta and wye | 5 |
| Explains why delta is used for primary and wye for secondary in this case | 5 |
| Identifies the location of the neutral and its function in wye configuration | 5 |
| Describes grounding and bonding implications for each side | 5 |

---

### **4. Nameplate Interpretation (20 points)**
| Criteria | Points |
|---|---|
| Accurately reads primary/secondary voltages, kVA, impedance, wiring diagram | 10 |
| Identifies correct tap settings, temperature rise, and phase rating | 5 |
| Uses the nameplate to justify their wiring decisions | 5 |

---

### **5. Physical Wiring Demonstration or Description (20 points)**
| Criteria | Points |
|---|---|
| Accurately describes or shows primary side wiring (3 hot wires into delta) | 5 |
| Accurately describes or shows secondary side wiring (4 wires: A, B, C, N) | 5 |
| Describes correct grounding (XO to ground, bonding at first disconnect, etc.) | 5 |
| Shows correct labeling, torqueing, and safety steps | 5 |

---

### **Optional Bonus (Up to +5 points)**
- Discusses inrush current, derating for harmonics, or code requirements (e.g., NEC Article 450)
- Adds real-world application examples (e.g., school building, panelboards)
- Demonstrates exceptional clarity, confidence, or instructional skill

---

Let me know if you want this adapted into a printable sheet or modified for hands-on vs. oral exam balance.

## User

Now I need a rubric for a final exam board on which they need to have a transformer connected on H1 and H2, X1 and X4 need to connect to the coil of a relay, X2 and X3 need to be jumpered together, and the H1 and H2 120v neeed to be in parallel with two 120v lights that are wired through the normally open and normally closed of the relay. The relay coil is controlled by a switch that will show the state by changing lights.

## Assistant

Perfect. Here's a **clear and detailed rubric** for assessing a **final exam board wiring project**, based on the criteria you described. This rubric focuses on **functional wiring, understanding of circuit behavior, safety, and demonstration of relay logic** through lighting.

---

## **Final Exam Rubric: Relay-Controlled Lighting with Transformer Board**
**Total: 100 points**

---

### **1. Transformer Wiring (20 points)**  
| Criteria | Points |
|---|---|
| H1 and H2 correctly connected to 120V line (with fuse or breaker if applicable) | 5 |
| X2 and X3 properly jumpered together (center tap creation) | 5 |
| X1 and X4 correctly wired to the relay coil | 5 |
| Transformer is bonded/grounded appropriately if required | 5 |

---

### **2. Relay Logic Wiring (20 points)**  
| Criteria | Points |
|---|---|
| Relay coil controlled by switch from X1–X4 leg, properly switching 120V | 5 |
| Switch functionally energizes/de-energizes the relay | 5 |
| Correct NO (Normally Open) and NC (Normally Closed) terminals used | 5 |
| Coil is protected (no shorting, fusing if needed) and labeled | 5 |

---

### **3. Lighting Circuit Function (20 points)**  
| Criteria | Points |
|---|---|
| 120V source (H1 and H2) correctly paralleled with relay-controlled lights | 5 |
| One light wired to NO, one to NC contact, showing opposite states | 5 |
| Lights change appropriately when switch is toggled (NO turns ON, NC turns OFF, and vice versa) | 5 |
| No flickering, buzzing, or miswiring present | 5 |

---

### **4. Circuit Behavior and Demonstration (20 points)**  
| Criteria | Points |
|---|---|
| Student clearly explains how the system works (transformer > relay > light logic) | 5 |
| Identifies each terminal and connection point on the relay | 5 |
| Explains why X2–X3 jumper is necessary (neutral reference for coil/load) | 5 |
| Correctly answers basic fault or failure scenarios (e.g. "What happens if the NO and NC are swapped?") | 5 |

---

### **5. Safety, Labeling, and Professionalism (20 points)**  
| Criteria | Points |
|---|---|
| Board is neat, organized, and wires are routed cleanly | 5 |
| Wires are stripped and terminated properly, not frayed or overexposed | 5 |
| All components labeled or otherwise easy to identify | 5 |
| No exposed live parts, all terminations tight and torqued | 5 |

---

### **Bonus (up to +5 points)**  
- Uses proper color codes (black for hot, white for neutral, etc.)
- Adds indicator lamp to show relay coil is energized
- Adds fuse protection, terminal blocks, or logical troubleshooting diagram

---

Let me know if you want this in a printable table or checklist version, or if you want a simplified version for students with accommodations.

## User

Since this is a wiring lab, 5 won't be necessary and we won't actually be plugging it in, I'll just be following the circuit by eye

## Assistant

Got it! Here's the **revised rubric** without the safety/demonstration category. This version is strictly focused on **wiring correctness, logic, and understanding**, assuming you’ll verify accuracy by visually tracing the circuit.

---

## **Final Exam Wiring Rubric: Transformer & Relay Board (No Power Applied)**
**Total: 80 points**

---

### **1. Transformer Wiring (20 points)**  
| Criteria | Points |
|---|---|
| H1 and H2 wired as the primary side of the transformer (120V input) | 5 |
| X2 and X3 correctly jumpered to form the neutral reference | 5 |
| X1 and X4 connected across the relay coil | 5 |
| Wiring is clean, terminals used correctly, and connections make logical sense | 5 |

---

### **2. Relay Coil Control Logic (20 points)**  
| Criteria | Points |
|---|---|
| Relay coil is in series with a switch between X1 and X4 | 5 |
| Switch is placed in a logical, functional location (not shorting or floating coil) | 5 |
| Correct understanding of coil polarity or winding direction if applicable | 5 |
| Wiring is traceable, and relay logic follows correct signal flow | 5 |

---

### **3. Light Circuit Wiring (20 points)**  
| Criteria | Points |
|---|---|
| H1 and H2 also feed the common of relay contacts for the lights (parallel source) | 5 |
| One 120V light correctly wired to the NO contact, the other to the NC contact | 5 |
| X2/X3 jumper used as return path (neutral) for the lights | 5 |
| Lights are clearly switched by relay state (in theory, based on layout) | 5 |

---

### **4. Circuit Logic and Understanding (20 points)**  
| Criteria | Points |
|---|---|
| Student can explain what each terminal and connection does | 5 |
| Can explain what happens when the switch is toggled (light behavior) | 5 |
| Describes correct current path for relay coil and light circuits | 5 |
| Can predict effects of miswiring (e.g., missing jumper, swapped NO/NC) | 5 |

---

Let me know if you'd like a **score sheet version** or a **student-facing checklist** to go along with it.

