---
type: Conversation
title: "Privacy Battery Optimization Guide"
description: "I factory reset my pixel 8xl. I've disabled most of the permissions but I want it to be as stock as possible, but as privacy focused and battery effec"
resource: "68320dc2-00d8-8003-ad98-63bcc13231b2"
timestamp: "2025-05-24T18:28:42.859Z"
tags: ["gpt-4o"]
---

# Privacy Battery Optimization Guide

## User

I factory reset my pixel 8xl. I've disabled most of the permissions but I want it to be as stock as possible, but as privacy focused and battery effective as possible. I just want to use my phone, and I don't want it pinging 5i392038573i2o2 networks all the time and killing battery. 

## Assistant



## Assistant

Here’s a clean, privacy-respecting, and battery-optimized setup for your freshly reset Pixel 8 XL. Think of it as **stock+**—mostly stock, but with a few trims and tweaks:

---

### **1. Core Goals**
- **Battery-efficient**
- **Privacy-focused**
- **Minimal background junk**
- **Still usable day-to-day**

---

### **2. Basic System Settings**
**Battery & Performance**
- Settings > Battery > Adaptive Battery → ON  
- Settings > Display > Smooth Display → OFF  
- Settings > Location > Wi-Fi scanning & Bluetooth scanning → OFF  
- Settings > Network > Adaptive Connectivity → OFF (optional—this toggles 5G but can save battery)

**Privacy**
- Settings > Privacy > Usage & Diagnostics → OFF  
- Settings > Privacy > Ads > "Delete advertising ID"  
- Settings > Google > Personalize using app data → OFF  
- Settings > Google > Device connections → Turn off anything unused

---

### **3. Network Pings & Data Drain**
- **Developer Options > Mobile data always active** → OFF  
- **Developer Options > Background process limit** → At most 4  
- Disable **Nearby Share** and **Google Cast**

---

### **4. App Control**
- Uninstall/disable:
  - Google One
  - Digital Wellbeing
  - YouTube (if unused, or switch to YouTube Vanced/revanced)
  - Google Podcasts (deprecated)
  - Google TV
- Install a firewall like **NetGuard** or **RethinkDNS** (no root needed) to monitor/block suspicious connections.

---

### **5. App Alternatives (Optional but Recommended)**
| Purpose         | Stock App        | Privacy Alternative      |
|----------------|------------------|--------------------------|
| Maps           | Google Maps      | Organic Maps / Magic Earth |
| Browser        | Chrome           | Firefox + uBlock Origin  |
| Messaging      | Google Messages  | Simple SMS Messenger     |
| YouTube        | YouTube          | NewPipe / ReVanced       |
| Email          | Gmail            | FairEmail / ProtonMail   |
| Weather        | Google Weather   | MeteoLibre / Geometric Weather |
| Assistant      | Google Assistant | NONE – turn it off entirely |

---

### **6. Final Cleanup**
- **Disable Digital Wellbeing, Tips, and Pixel Tips**: They keep waking the system.  
- Settings > Apps > Special app access > Battery Optimization → Set all to **Optimized** or **Restricted** except messaging and navigation.

---

### **7. Optional Light Debloating (No Root Needed)**
Use ADB to remove system bloat:
```bash
adb shell pm uninstall -k --user 0 com.google.android.apps.wellbeing
adb shell pm uninstall -k --user 0 com.google.android.apps.tachyon
adb shell pm uninstall -k --user 0 com.google.android.apps.subscriptions.red
```
Let me know what you want to keep and I’ll give you the full list.

---

If you'd like, I can walk you through each of these steps interactively. Want to start with firewall setup or ADB debloat?

## User

Too much. I want to keep it mostly stock. Keep stuff like smooth display on and all that. Just stop the constant spying without interrupting my normal daily stuff. 

## Assistant

Got it. You want **stock feel**, **no spying**, and **good battery**, without disabling features like Smooth Display or breaking anything. Here’s a minimal, clean setup that hits that balance:

---

### **1. Google Account Tweaks**
- **Settings > Google > Ads > Delete advertising ID**
- **Settings > Google > Personalize using app data → OFF**
- **Settings > Google > Location Sharing & Timeline → OFF**

---

### **2. Privacy Settings (Safe to Change)**
- **Settings > Privacy**
  - Usage & Diagnostics → **OFF**
  - Nearby devices → **OFF**
  - Microphone & Camera access (global toggle) → Leave ON unless you want tighter control

---

### **3. Disable Background Noise (No Apps Needed)**
- **Settings > Location**
  - Wi-Fi Scanning → OFF  
  - Bluetooth Scanning → OFF  
- **Settings > Network & Internet > Private DNS** → Set to `dns.adguard.com` (AdGuard DNS = stops tracking domains system-wide, no apps needed)

---

### **4. App Permissions**
Go to **Settings > Apps > See all apps > [Google apps like Photos, Play Services, etc.]**
- Turn off location, microphone, and contacts if not essential
- Especially limit:
  - **Google Play Services** – no location, no body sensors, no SMS
  - **Google App** – disable microphone & location unless you use Assistant

---

### **5. Optional App to Monitor Without Breaking Anything**
- Install **RethinkDNS** (free on Play Store)
  - Blocks trackers at DNS level  
  - No root  
  - Doesn’t interfere with daily phone usage  
  - Choose the "Standard" blocking list

---

You’ll still get everything that makes the Pixel feel like a Pixel, but it won’t leak as much data or waste as much battery.

Want me to give you a quick step-by-step for RethinkDNS setup next? Or just a checklist you can tick through?

## User

This seems about right. The less stuff being "reported" the less it sends it off the less it keeps my phone awake. 

## Assistant

Exactly—less reporting = less background activity = longer battery life and less spying. You’re aiming for the **quiet Pixel** setup: still smart, still smooth, but not a little narc in your pocket.

Here’s a **quick checklist** you can work through in 10 minutes:

---

### **Quick Privacy + Battery Checklist (No Breaking Anything)**

#### **Google Settings**
- [ ] Settings > Google > Ads > **Delete advertising ID**
- [ ] Settings > Google > Personalize using app data → **OFF**
- [ ] Settings > Google > Location Sharing & Timeline → **OFF**

#### **Location & Scanning**
- [ ] Settings > Location > Wi-Fi scanning → **OFF**
- [ ] Settings > Location > Bluetooth scanning → **OFF**

#### **Privacy Settings**
- [ ] Settings > Privacy > Usage & Diagnostics → **OFF**
- [ ] Settings > Privacy > Nearby devices → **OFF**

#### **Private DNS**
- [ ] Settings > Network & Internet > Private DNS → **dns.adguard.com**

#### **App Permissions (Only Once)**
- [ ] Settings > Apps > See all apps > Google App → Deny microphone if you don’t use Assistant
- [ ] Settings > Apps > See all apps > Google Play Services → Deny location

#### **(Optional but Worth It)**
- [ ] Install **RethinkDNS** from Play Store  
    - Choose “Standard” blocking list  
    - Enable firewall & DNS  
    - Forget about it—it just works

---

That’s it. Now your Pixel isn’t talking behind your back as much, and you’ll likely see battery life improve too.

Want me to save this checklist as a Google Keep note you can open on your phone?

