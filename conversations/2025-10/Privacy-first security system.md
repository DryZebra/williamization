---
type: Conversation
title: "Privacy-first security system"
description: "I need to establish a home security system with two way communication that isn't connected to the spy networks. I just mean no software as a service, "
resource: "68f01adc-f14c-832b-8058-038d493b8bb4"
timestamp: "2025-10-15T22:18:57.875Z"
tags: ["gpt-5"]
---

# Privacy-first security system

## User

I need to establish a home security system with two way communication that isn't connected to the spy networks. I just mean no software as a service, no subscription models, no databases and ai enhanced moments. 

## Assistant



## Assistant



## Assistant



## Assistant

Nice — doable. Below I’ll give you a practical, privacy-first plan you can implement today (no SaaS, no cloud, no subscriptions, no third-party databases, no AI). I’ll include recommended hardware choices, an internal network design, concrete software options (all open or self-hostable), a step-by-step setup plan, and hardening tips so the system stays local and private.

Summary (one line)
Run everything on your LAN (cameras → local NVR or server, two-way audio via SIP/PBX), block device internet access, and use a VPN (WireGuard) for any remote access — no cloud at all.

# What you’ll build (high level)
1. Local video capture: PoE IP cameras that support RTSP/ONVIF → local NVR or PC running ZoneMinder / MotionEye / Shinobi / Synology Surveillance Station.  
2. Two-way voice/video: SIP-capable door/intercom or camera (speaker+mic) registered to a local PBX (Asterisk or FreePBX) → make and receive calls from phones/softphones on your LAN or via WireGuard VPN.  
3. Network: VLANs for IoT, firewall rules blocking outbound from cameras, separate management host for NVR/PBX, and WireGuard for secure remote access.  
4. Storage: local disk (RAID or single drive with encrypted backups) — no cloud backups unless you self-host them on your own offsite server.  
5. Optional UI: Home Assistant (local only) for automation and unified control — but you can skip it if you want minimal attack surface.

# Recommended components (roles — buy brands/models that allow disabling cloud features and provide RTSP/ONVIF)
- Cameras: PoE IP cameras with RTSP and ONVIF. Prefer models where cloud features can be disabled and firmware is documented. If you want absolute control: analog CCTV cameras + local NVR (BNC → NVR) — truly local.  
- PoE switch: managed PoE switch (8–16 ports) so cameras get power + you can isolate ports into VLANs.  
- NVR/Server: small headless server or NAS (Synology/QNAP that supports Surveillance Station) OR a mini-ITX PC to run ZoneMinder/Shinobi/Frigate. CPU depends on camera count/codec.  
- PBX server: same or separate small server (Asterisk/FreePBX/Issabel). A Raspberry Pi 4/Zero 2 W can run a small Asterisk for a couple devices; for many endpoints use a heavier box.  
- SIP door/intercom: SIP-capable doorphone (or any SIP phone/hardphone) — registers to your PBX and supports speaker/mic. If your cameras have built-in speaker/mic and support SIP or ONVIF audio, you can use those.  
- Client devices: SIP softphone apps (Linphone, Bria, Mobile softphones) or hardware SIP phones inside the LAN.  
- Router/firewall: router that supports VLANs and firewall rules (pfSense/OPNsense recommended), or a good consumer router with VLAN capabilities.  
- VPN: WireGuard (self-host) on the router or separate VPN server for remote encrypted access.  
- Storage: local NAS or HDD(s). Consider RAID1 for redundancy. Keep encrypted offsite backups (optional and self-hosted).

# Software options (all local / self-hostable)
- NVR / camera recording:
  - ZoneMinder (Linux) — mature, local-only if you block outbound.  
  - Shinobi — lightweight, modern UI.  
  - MotionEye / Motion — simple.  
  - Synology Surveillance Station (if using Synology NAS) — local.  
  - Frigate (if you want object detection locally — but that is “AI” on-device; skip if you explicitly want no AI).  
- PBX / two-way audio:
  - Asterisk (very flexible), FreePBX (GUI for Asterisk), or OpenSIPS / Kamailio (if you have heavy load).  
- Home automation / UI (optional):
  - Home Assistant (can run completely offline).  
- VPN:
  - WireGuard (recommended), OpenVPN (older).  
- Camera discovery/control:
  - ONVIF clients and RTSP players (VLC, or the NVR software).

# Network design (text diagram)
Internet <—> Router/Firewall (pfSense/OPNsense)  
 │  
 ├─ WAN (internet)  
 ├─ LAN VLAN (management + your phones)  
 ├─ IOT VLAN (cameras, SIP doorphone) — **BLOCK all outbound** except NTP/optional internal DNS  
 └─ SERVICES VLAN (NVR, PBX, NAS) — only allow required ports from LAN/IOT; allow WireGuard in/out for remote clients

Key rule: cameras and IoT live on a VLAN with no direct internet access. Devices that must communicate externally (never a camera ideally) are either manually controlled or blocked.

# Step-by-step quick start
1. **Plan VLANs + get pfSense/OPNsense** on your router or run on a spare box. Create at least 3 VLANs: LAN, IOT, SERVERS.  
2. **Buy PoE switch** and plug cameras into IOT VLAN ports. Configure switch to tag VLANs.  
3. **Install NVR software**: on a local server install ZoneMinder or Shinobi. Add camera RTSP streams (rtsp://camera-ip/stream). Configure retention and motion capture to local disk.  
4. **Install PBX**: On a server install Asterisk or FreePBX. Add extensions for each SIP phone/doorphone/camera (if camera supports SIP).  
   - Example minimal `sip.conf` style (Asterisk PJSIP syntax will be different; this is illustrative):
```ini
[1000]
type=friend
host=dynamic
secret=STRONGPASSWORD
context=from-internal
callerid="FrontDoor" <1000>
```
   - `extensions.conf` sample to ring your phone from doorphone:
```ini
[from-internal]
exten => 1000,1,Dial(SIP/1000,20)
exten => 1000,n,Voicemail(1000@default)
```
5. **Register devices**: Point door intercom or SIP-enabled camera to the PBX (use LAN IP), test two-way audio by calling extension from a softphone.  
6. **Block outbound**: On your firewall, deny outbound internet access from the IOT VLAN by default. Only allow NTP, DNS to your internal DNS, or nothing at all. This prevents cloud telemetry.  
7. **Remote access**: If you need remote access, **do not** open camera ports. Instead run WireGuard server on your router or a separate box and connect your phone/remote laptop via WireGuard to your LAN — then access the NVR/PBX UI locally over the VPN.  
8. **Logs & backups**: Save NVR config and PBX configs regularly to an encrypted backup that you keep offline or on your own offsite server.

# Camera advice & anti-spy checklist
- Choose cameras with RTSP/ONVIF support and a well-documented way to disable cloud features. If vendor hides options, avoid it.  
- Disable everything cloud: “cloud management,” “phone app pairing,” “remote access,” automatic firmware updates (you decide updates offline).  
- If camera firmware is opaque / pushes telemetry even when cloud is off — prefer analog cameras with a true local NVR or choose vendors known for local-first operation.  
- Block outbound at the firewall (IOT VLAN) — no DNS to external resolvers from IOT devices. Use an internal Pi-Hole if you want.  
- Consider physically disabling microphones/speakers if you don’t need audio on certain cameras.

# Two-way communication options (pick one)
1. **SIP Doorphone → Asterisk PBX** (recommended): doorphone registers to Asterisk; pressing door triggers a call to your phone/softphone; you speak two-way through SIP. Works over LAN and over WireGuard. Very controllable.  
2. **Camera built-in audio**: if camera supports two-way audio via RTSP/ONVIF, use the NVR to relay audio or use SIP if supported. Quality/latency varies.  
3. **Dedicated intercom + SIP phone**: hardware SIP intercom at the door + indoor SIP handset. Rugged and simple.

# Hardening & privacy rules (non-negotiable)
- Change default credentials on every device. Use unique, strong passwords.  
- Put cameras on isolated VLAN. Deny outbound internet for that VLAN.  
- Disable UPnP on router. Don’t use automatic port forwarding.  
- Use WireGuard VPN for any remote access. No direct port forwarding to cameras or PBX.  
- Keep NVR / PBX software patched, but update intentionally (download firmware manually after checking vendor changelog).  
- Use HTTPS for any web UIs (generate and install your own cert; Let’s Encrypt is a CA but requires internet; for purely local use you can use self-signed certs and install them on your clients).  
- Audit logs periodically and keep backups of configuration in an encrypted vault (USB/offline).  
- Physical security: hide/lock NVR and networking gear. Cameras placed out of tamper range if possible.

# Example minimal topology and software pairing (small system)
- 4× PoE IP cameras (RTSP/ONVIF) → PoE switch (IOT VLAN).  
- Mini-ITX server: 8GB RAM, ZoneMinder + local HDD for recordings (SERVERS VLAN).  
- Raspberry Pi 4: Asterisk for PBX (SERVERS VLAN). SIP handset(s) on LAN VLAN.  
- pfSense router: VLANs, WireGuard server, firewall rules.  
- SIP doorphone at front door (IOT VLAN) registered to Asterisk. Cameras have outbound blocked.

# Downsides / tradeoffs you should know
- Local-only means you must manage the system: firmware updates, backups, monitoring. No vendor help/remote portal.  
- If you want remote mobile push notifications without cloud, you’ll need to build your own push or use VPN to view footage — push notifications usually require cloud. (If you insist on push, you can self-host a push gateway, but that’s extra complexity.)  
- Some consumer cameras are cloud-first; truly private local operation requires careful model selection or analog solutions.

# If you want a minimal shopping list to start
- Managed PoE switch (8 port)  
- 2–4 PoE IP cameras (RTSP/ONVIF capable) **— check that cloud can be disabled**  
- Small server for NVR (mini-ITX or used desktop) or Synology NAS  
- Raspberry Pi 4 (for PBX) or same server for Asterisk (if you want fewer devices)  
- pfSense/OPNsense capable router (or appliance)  
- SIP door intercom (SIP-capable)  
- WireGuard client app on your phone

# Final nitty-gritty (practical setup notes)
- When adding cameras to ZoneMinder/Shinobi: use RTSP with username/password over LAN (no HTTPS in RTSP; rely on LAN security + VLAN). Record at lower FPS/higher compression if you want longer retention.  
- For Asterisk, register softphone with SRTP if supported to encrypt audio on LAN; otherwise rely on VPN for remote encryption.  
- Make a `hosts` or internal DNS entry for NVR/PBX so you can reach them by name over the VPN without exposing them.

---

If you want, I can:
- produce a **short shopping list** with three suggested camera models and two PoE switch options that are known to work well for local use (I’ll pick only models that let you disable cloud features), **or**  
- generate a **concise pfSense + WireGuard firewall rule set** and an example **Asterisk pjsip.conf / extensions.conf** that will let a SIP doorphone call your phone over the LAN/VPN.

Tell me which of those (shopping list vs config snippets) you want and I’ll spit out the exact parts/config — fully local, no cloud.

