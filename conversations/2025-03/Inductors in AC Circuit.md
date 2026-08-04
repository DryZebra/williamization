---
type: Conversation
title: "Inductors in AC Circuit"
description: "Can you explain why Connecting additional inductors in an AC series circuit will cause the circuit current to decrease?"
resource: "67d47c63-f040-8003-93d9-3a4641a009ce"
timestamp: "2025-03-14T18:59:04.680Z"
tags: ["gpt-4o"]
---

# Inductors in AC Circuit

## User

Can you explain why Connecting additional inductors in an AC series circuit will cause the circuit current to decrease? 

## Assistant



## Assistant

Yes! In an **AC series circuit**, adding more inductors will increase the total **inductive reactance (\(X_L\))**, which in turn **reduces the circuit current**. Here's why:

### 1. **Inductive Reactance Increases**
   - The opposition to current flow in an inductor is called **inductive reactance**, given by the formula:
     \[
     X_L = 2\pi f L
     \]
     where:
     - \( f \) = frequency of the AC supply
     - \( L \) = inductance of the inductor

   - When additional inductors are connected **in series**, the total inductance (\(L_{total}\)) **adds up**:
     \[
     L_{total} = L_1 + L_2 + L_3 + \dots
     \]
     - This causes \(X_L\) to increase, making it harder for current to flow.

### 2. **Total Impedance Increases**
   - The total impedance (\(Z\)) of the circuit consists of resistance (\(R\)) and inductive reactance (\(X_L\)):
     \[
     Z = \sqrt{R^2 + X_L^2}
     \]
   - Since \(X_L\) increases with added inductors, the total impedance increases.

### 3. **Current Decreases (Ohm’s Law for AC Circuits)**
   - Ohm’s Law for an AC circuit is:
     \[
     I = \frac{V}{Z}
     \]
     where:
     - \( I \) = circuit current
     - \( V \) = applied voltage
     - \( Z \) = total impedance

   - Since \(Z\) increases, the **current \(I\) decreases**.

### **Conclusion**
Adding more inductors in an AC **series** circuit increases inductive reactance, raising the total impedance and thus **reducing the current flow** according to Ohm’s Law.

