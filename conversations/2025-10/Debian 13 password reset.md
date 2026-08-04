---
type: Conversation
title: "Debian 13 password reset"
description: "I forgot my Debian 13 username and password"
resource: "68fbf4a8-ab74-8329-a513-45e12ab51160"
timestamp: "2025-10-24T21:55:06.676Z"
tags: ["gpt-5"]
---

# Debian 13 password reset

## User

I forgot my Debian 13 username and password 

## Assistant



## Assistant

If you forgot both your **username** and **password** on Debian 13, you can still recover access if you have **physical access** to the machine. Here’s how to reset them safely:

---

### 🧰 Step 1 — Access the GRUB menu
1. Reboot your system.  
2. As soon as you see the **GRUB** boot screen, press **`e`** to edit the boot entry.  
3. Find the line that begins with `linux` and ends with something like `quiet splash`.  
4. At the end of that line, append this:
   ```
   init=/bin/bash
   ```
5. Press **Ctrl + X** or **F10** to boot.

---

### 🧭 Step 2 — Gain write access
Once you’re dropped into a root shell:
```bash
mount -o remount,rw /
```

---

### 🔍 Step 3 — Find your username
You can list all users:
```bash
cat /etc/passwd
```
Look for lines ending with `/home/<username>` — that `<username>` is usually your login.

---

### 🔑 Step 4 — Reset the password
Replace `<username>` with the name you found:
```bash
passwd <username>
```
You’ll be prompted to enter a new password twice.

If you want to **create a new user** instead:
```bash
adduser newuser
usermod -aG sudo newuser
```

---

### 🔁 Step 5 — Reboot
When you’re done:
```bash
exec /sbin/init
```
or just run:
```bash
reboot -f
```

---

### 🧹 Optional: disable root auto-login
Once you’re back in, make sure you remove the `init=/bin/bash` line from GRUB (it was temporary and doesn’t persist by default).

---

Would you like me to walk you through how to recover **only your username** (without changing passwords) or to **fully reset both username and password** automatically via GRUB script?

## User

Pressing e isn't working it just goes to the login screen

## Assistant

Got it — that means your system is booting too fast into the graphical login and **not showing the GRUB menu** at all.  
We’ll need to **force the GRUB menu to appear** before you can reset anything.  

Here’s what to do step by step:  

---

### 🧭 **Option 1 — Force GRUB to appear**
Try this first:

1. **Reboot your computer.**
2. As soon as the screen goes black after BIOS (the manufacturer logo), **hold down the `Shift` key** if you’re on a **BIOS (Legacy)** system, or **tap `Esc` repeatedly** if you’re on **UEFI**.
3. If timed right, you’ll get the **GRUB boot menu** (usually black with white text).

If that doesn’t work the first time, try again — the timing can be tricky.

---

### ⚙️ **Option 2 — Temporarily force GRUB to show on boot**
If Option 1 doesn’t work after a few tries, we’ll use a **live USB** to modify the GRUB configuration.

#### Step 1. Boot from a Debian or Ubuntu live USB
Insert a USB drive with Debian/Ubuntu and select “Try Debian” (not Install).

#### Step 2. Find your root partition
In the terminal:
```bash
sudo fdisk -l
```
Look for a partition like `/dev/sda2` or `/dev/nvme0n1p2` labeled as `Linux filesystem`.

#### Step 3. Mount your system
```bash
sudo mount /dev/sdXY /mnt
```
(Replace `sdXY` with your Linux root partition.)

#### Step 4. Enable GRUB editing permanently
Edit the GRUB config file:
```bash
sudo nano /mnt/etc/default/grub
```
Find this line:
```
GRUB_TIMEOUT_STYLE=hidden
```
and change it to:
```
GRUB_TIMEOUT_STYLE=menu
GRUB_TIMEOUT=10
```
Save with **Ctrl+O**, then **Ctrl+X**.

#### Step 5. Update GRUB
Chroot into your system and update GRUB:
```bash
sudo mount --bind /dev /mnt/dev
sudo mount --bind /proc /mnt/proc
sudo mount --bind /sys /mnt/sys
sudo chroot /mnt
update-grub
exit
sudo umount /mnt/{dev,proc,sys}
sudo umount /mnt
```
Then reboot:
```bash
sudo reboot
```

---

After rebooting, the GRUB menu should appear, and you can use the earlier **`init=/bin/bash`** steps to reset your password.

---

Would you like me to give you the **exact live USB commands** for the “reset password without GRUB” method (you can directly mount your Debian partition and reset your password that way too)? It’s actually a bit faster if you already have a Debian or Ubuntu USB handy.

