---
type: Conversation
title: "Reset EXOS router login"
description: "How do I reset the username and password for an EXOS router?"
resource: "68eb9bef-3b28-8332-8ec4-b0480c0bce8e"
timestamp: "2025-10-12T12:17:08.210Z"
tags: ["gpt-5"]
---

# Reset EXOS router login

## User

How do I reset the username and password for an EXOS router?

## Assistant



## Assistant



## Assistant



**Tool Output (web.run)**:
```

```

**Tool Output (web.run)**:
```

```

## Assistant



**Tool Output (web.run)**:
```

```

**Tool Output (web.run)**:
```

```

## Assistant



## Assistant

Short answer: there are two ways — (A) change the account from an existing admin session, or (B) recover/reset the box with console access if **all** admin passwords are lost. Read the quick steps below and the exact commands/examples after that.

# If you still have an admin login
1. SSH/console into the switch and run the account command to change a password:
   - To change an existing user’s password:
     ```
     configure account <username> password
     ```
     (you’ll be prompted to type and confirm the new password). citeturn0search5
   - If you can’t change the password because you don’t know it for that user, delete and recreate it:
     ```
     delete account "olduser"
     create account <role> newuser
     password:
     reenter password:
     ```
     Example: `delete account "testaccount"` then `create account admin testaccount`. citeturn0search3

# If you have lost all admin passwords (password recovery / factory default)
You must use a serial console (local console cable) and BootROM method:

1. Connect a serial console to the switch console port (USB-to-serial / RJ45 console cable as appropriate). Terminal settings:
   - Baud: **9600** (most EXOS models)
   - Exceptions (X465 / X590 / X690 / X870 and Universal 5320/5420/5520/5720): **115200**.
   - Data bits 8, parity none, stop bits 1, flow control XON/XOFF. citeturn1search2turn1search4

2. Power-cycle the switch and when prompted **press & hold the spacebar** to enter BootROM / bootstrap. At the `BootRom>` prompt run:
   ```
   config none
   boot
   ```
   That boots the switch with a default (no-config) selection so you can log in with default credentials. citeturn0search2turn0search14

3. After boot you should be able to log in with the default account (usually `admin` with no password — press Enter). Create a new admin account or recreate/change passwords as needed:
   ```
   create account admin myadmin
   password:
   reenter password:
   ```
   Or delete the old account and recreate. citeturn1search8turn0search3

# Important notes & cautions
- Some EXOS versions/models and BootROM versions behave slightly differently; if you see a grub menu instead of BootROM prompts follow the model-specific prompts (the docs cover Summit X870 and others). citeturn0search2turn0search9  
- Restoring to default/booting `config none` **can** affect how the running config is loaded — always try to back up the config first if you still have access. If you are unsure, contact Extreme Support before proceeding. citeturn0search4turn0search2
- If the console keypress to enter BootROM doesn’t work, try unplug/replug power, try different terminal emulators, and double-check the baud for your exact model (some universal models use 115200). citeturn1search1turn1search4

---

If you tell me your exact model (example: Summit X460-24t, 5320-48P, X870, etc.) I’ll give the exact baud to use and the step-by-step command sequence tailored to that model (and note any model quirks).

## User



This is the router

## Assistant

Excellent — the label shows that your router is a **Calix GigaSpire BLAST GS5229XG**, not an Extreme EXOS switch.  
Here’s exactly how to reset the **username and password** for this Calix router:

---

### 🧠 1. Default login credentials
On the sticker:
```
IP Address: 192.168.1.1  
User / Password: admin / D46eb97c
```
That’s the **default local login** for the web interface.

To use it:
1. Connect a computer or phone to the router’s Wi-Fi SSID (also printed on the label).  
2. Open a browser and go to **http://192.168.1.1**.  
3. Log in with:
   - **Username:** `admin`  
   - **Password:** the one printed on the sticker (e.g., `D46eb97c`).

---

### 🔑 2. If you can still log in and just want to change the password
Once logged in:
1. Go to **Maintenance → Admin Settings** (sometimes under *System → User Settings*).  
2. Enter the old password, then the new one twice.  
3. Save and reboot if prompted.

If your ISP supplied the router, this menu might be locked out; in that case you must call them or use the Calix CommandIQ app.

---

### 🌀 3. If you’ve forgotten the password or can’t log in
Use the **hardware reset** button:

1. Find the small **reset pinhole** on the back or bottom of the router.  
2. With the router powered on, **press and hold for 10–15 seconds** (use a paperclip).  
3. Wait until the LEDs blink or the unit restarts.  
4. The router will boot back up with **factory defaults**, including:
   - Wi-Fi SSID and password printed on the label.
   - Admin login reset to `admin / [printed password]`.

Then reconnect and log in at `192.168.1.1` with those defaults.

---

### 🧰 4. Optional (if your ISP manages it)
Some Calix routers are provider-locked. If the admin login doesn’t work even after reset, the provider has remote management enabled. You’ll need to call their support to have them unlock or reset the local admin credentials.

---

Would you like me to tell you **which mobile app or URL** your ISP likely uses for this specific GigaSpire BLAST model (for remote login via smartphone)?

