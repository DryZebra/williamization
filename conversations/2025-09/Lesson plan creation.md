---
type: Conversation
title: "Lesson plan creation"
description: "Utilizing the following screenshots, create a lesson plan for 2 days to cover 11 hours total through primarily classroom discussion and example proble"
resource: "68bb0bc0-be20-8325-8822-f95186749ea4"
timestamp: "2025-09-06T12:07:34.373Z"
tags: ["gpt-5-instant","gizmo"]
---

# Lesson plan creation

## User










Utilizing the following screenshots, create a lesson plan for 2 days to cover 11 hours total through primarily classroom discussion and example problems. Bundle all of it in a single document that could be handed to an instructor, scrolled through and on first glance be able to lead this 11 hour classroom discussion that naturally leads to these conclusions. 

The lesson should begin with a small review on how to "memorize" the code book. I'll be using the pneumonic of assigning thumb numbers to words, and mapping those words to choice chapters. 

This is my method: 

1, gun, general of the army, Chapter 1 General. 

2, shoe, strings and container, wiring and protection 

3, tree, a tree made of conduit and MC, chapter 3 wiring and protection 

4, door, typical, equipment for general use

5, hive full of different buildings like a hospital and bees dressed up. Special locations. 

6. Sticks, magic wands that power equipment. Speciality equipment. 

7. Heaven. Special place. Special conditions. 

8. Gate. Gated community. Communications. 

9. Chapter 9 tables lmao

## Assistant



## Assistant

Got it, Ezra. I’ll build you a **2-day, 11-hour discussion lesson plan** that an instructor could pick up and run with immediately. It will:  

* Start with your **mnemonic code-book review method**.  
* Flow naturally through the **9 lessons** shown in your screenshots (OCPD purpose, categories, ratings, breakers, fuses, sizing, taps, fault current, SCCR).  
* Rely on **discussion, NEC references, and example problems** rather than lecture.  
* End with students reaching the listed **learning objectives** themselves.  

---

# **Lesson Plan: Overcurrent Protection & Fault Current (NEC 2023)**  
**Total Duration: 11 Hours (2 Days)**  
**Delivery Mode:** Classroom discussion, guided problem-solving, NEC referencing practice.  

---

## **Day 1 (5.5 Hours)**  

### **0. Intro & Review – Memorizing the Code Book (30 min)**  
* Demonstrate thumb-number mnemonic:  
  - 1 gun → Chapter 1 General  
  - 2 shoe → Wiring & Protection  
  - 3 tree → Wiring Methods & Materials  
  - 4 door → Equipment for General Use  
  - 5 hive → Special Occupancies  
  - 6 sticks → Special Equipment  
  - 7 heaven → Special Conditions  
  - 8 gate → Communications  
  - 9 tables → Chapter 9 Tables  
* Group activity: each student invents their own silly image to link number & chapter.  
* Quick “find it fast” race using NEC index + mnemonic.  

---

### **1. Purpose of Overcurrent Protection & Types of Overcurrents (Lesson 1) (1 hr)**  
* **Discussion prompts:**  
  - What happens when current exceeds conductor ampacity?  
  - Difference between overload, fault current, short circuit, and ground fault.  
* **Example problem:** Calculate % of overload when a 20A branch circuit carries 28A continuously.  
* Tie to **safety & arc-flash hazard prevention**.  

---

### **2. OCPD Categories (Lesson 2) (1 hr)**  
* **Group brainstorm:** List where they’ve seen fuses vs. breakers in the field.  
* Introduce **branch-circuit, feeder, service OCPDs**, and supplementary protectors.  
* **Hands-on classification exercise:** Pass around images of breakers & fuses. Students classify whether they are service, feeder, or branch-circuit protection.  

---

### **3. OCPD Ratings (Lesson 3) (1 hr)**  
* **Key discussion:**  
  - Voltage rating, ampere rating, interrupting rating.  
  - Why interrupting rating is life-or-death.  
* **Example problem:**  
  - A 240V panel fed by 10kA available fault current. Would a breaker with 5kA interrupt rating be acceptable? (No).  
* NEC references: 110.24, 408.6, 240.4.  

---

### **4. Types of OCPDs – Circuit Breakers (Lesson 4) (1 hr)**  
* **Discussion:** Mechanical vs. electronic trip units. Thermal-magnetic curves.  
* Show time-current curve example (manufacturer data sheet).  
* **Example problem:**  
  - A motor branch circuit requires short-circuit protection. Which type of breaker fits? (Motor-rated breaker).  
* Group exercise: students explain why inspection/testing is required after a breaker clears a fault.  

---

### **5. Types of OCPDs – Fuses (Lesson 5) (1 hr)**  
* **Discussion:** Dual-element vs. fast-acting fuses, time-delay, high-speed.  
* **Example problem:**  
  - Why is a dual-element fuse used on a motor branch circuit? (Allows inrush without nuisance trip).  
* Activity: Match fuse classes (J, R, L, etc.) to real-world applications.  

---

## **Day 2 (5.5 Hours)**  

### **6. Practical Guidelines for OCPD Ampere Rating Sizing (Lesson 6) (1 hr 15 min)**  
* **Discussion:** Conductor ampacity vs. OCPD rating. Continuous vs. non-continuous load.  
* **Example problems:**  
  - Size an OCPD for 40A continuous load. (40 × 125% = 50A → next standard 50A).  
  - Compare with NEC Table 240.6.  
* Group whiteboard exercise: assign loads, students size OCPDs.  

---

### **7. Special Conductor Protection – Taps (Lesson 7) (1 hr 15 min)**  
* **Discussion:** Why taps exist (cost, practicality). Common use: luminaire circuits, feeders, busway.  
* Break down NEC 240.21(A–H).  
* **Example problem:**  
  - 12 AWG tapped from 20A circuit → legal? (Yes, with conditions).  
  - Transformer secondary taps → calculate OCPD.  

---

### **8. Calculation of Available Fault Current (Lesson 8) (1 hr 30 min)**  
* **Discussion:** Why fault current calculation matters. Tie back to interrupting ratings.  
* **Step-by-step example:** Calculate available fault current at a transformer secondary (use reference tables).  
* **Small group activity:** Each group solves a different sample fault current calc, then presents solution.  

---

### **9. Panelboards, Switchboards, Switchgear SCCR – NEC 408.6 (Lesson 9) (1 hr 15 min)**  
* **Discussion:**  
  - Why SCCR must be ≥ available fault current.  
  - OSHA & NEC 110.10 compliance.  
* **Example problem:**  
  - Available fault current = 22kA. Equipment SCCR = 14kA. What must be done? (Replace or re-rate).  
* Wrap up with field marking requirements (date + calculation).  

---

### **10. Closing Review & Discussion (30 min)**  
* Recap major objectives:  
  - Purpose of OCPDs, types, categories, ratings.  
  - Sizing rules & taps.  
  - Fault current calculations & SCCR requirements.  
* “Jeopardy-style” review game:  
  - Teams answer code-based questions, must cite NEC article.  
* Assign: Read NEC 240 and highlight key exceptions.  

---

# **Instructor Notes**  
* Keep NEC books in hand – every problem solved by **finding and citing the article**.  
* Encourage storytelling: ask apprentices for field experiences with tripped breakers, blown fuses, or mis-sized panels.  
* Emphasize **safety first** – link every technical detail back to arc-flash, fire prevention, or equipment protection.  

---

👉 On first glance, this doc lets an instructor walk into class, follow the timeline, and know exactly how to guide discussion and problems for 11 total hours across 2 days.  

Would you like me to also **build out a set of sample problems with full NEC references** (ready to hand to students), or just keep this as an instructor’s guide?

