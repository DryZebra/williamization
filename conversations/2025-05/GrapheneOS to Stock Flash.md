---
type: Conversation
title: "GrapheneOS to Stock Flash"
description: "What do I need to do to get my phone from graphene back to stock? Honestly the hiccups aren't worth it"
resource: "6831e57d-8fb8-8003-8e7a-238a13a2dc1b"
timestamp: "2025-05-24T15:28:14.980Z"
tags: ["gpt-4o"]
---

# GrapheneOS to Stock Flash

## User

What do I need to do to get my phone from graphene back to stock? Honestly the hiccups aren't worth it

## Assistant



## Assistant

To return your Pixel 8 XL from **GrapheneOS** to **stock Google firmware**, you'll need to completely wipe the device and flash the official factory image. It’s a straightforward process if you follow it carefully. Here's how to do it:

---

### **What You'll Need:**

1. A USB-C cable.
2. A computer (Linux, macOS, or Windows).
3. [Google’s Pixel Flash Tool](https://flash.android.com/) (web-based, works in Chrome or Edge).
4. USB debugging enabled on your phone (Settings > Developer options).
5. OEM unlocking enabled (Settings > Developer options) – **must be enabled unless your bootloader is still unlocked.**

---

### **Step-by-Step: Flash Back to Stock**

#### 1. **Backup Your Data**
Everything will be erased. Back up photos, contacts, etc. to your Google account or another storage location.

#### 2. **Enable Developer Options and OEM Unlocking**
- Go to Settings > About phone > Tap "Build number" 7 times.
- Go to Settings > System > Developer options.
- Enable **OEM unlocking** and **USB debugging**.

#### 3. **Unlock the Bootloader (if not already unlocked)**
If Graphene was installed, it's probably already unlocked. If not:
- Connect your phone to your PC.
- On your PC, run:
  ```
  adb reboot bootloader
  fastboot flashing unlock
  ```
- Confirm on the phone.

#### 4. **Use Google’s Pixel Flash Tool**
- Visit [flash.android.com](https://flash.android.com) in **Chrome or Edge**.
- Connect your phone via USB.
- Allow USB debugging when prompted on the phone.
- Select your device, pick the latest **stable** firmware.
- **Check “Wipe” and “Lock Bootloader”** (if you want a clean, locked, stock install).
- Click **Install** and follow instructions.

#### 5. **Let It Flash and Reboot**
- The process takes about 10–15 minutes.
- It will reboot to stock Android, as if brand new.

---

### **Afterward:**

- Sign in with your Google account.
- Re-enable any Google features (e.g., Play Protect, Google Pay).
- If you **locked the bootloader**, you’ll have full SafetyNet/Play Integrity compatibility again.

Let me know if you want help backing anything up, or keeping some privacy settings after reinstallation.

