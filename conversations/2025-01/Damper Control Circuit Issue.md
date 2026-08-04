---
type: Conversation
title: "Damper Control Circuit Issue"
description: "Why isn't this circuit working?"
resource: "6799016d-19b0-8003-92aa-6c3d0ce8d785"
timestamp: "2025-01-28T16:13:40.240Z"
tags: ["o1"]
---

# Damper Control Circuit Issue

## User


Why isn't this circuit working?

![Attachment: file-3PM83QB3kP7Y9KTkReoKxc](/assets/file-3PM83QB3kP7Y9KTkReoKxc-1000005798.jpg)


**Tool Output (a8km123)**:
```

```

## Assistant

A quick way to see what’s wrong is to trace where the damper‐control relay coil actually gets its **24 V and return**.  In the snippet you posted, both sides of the “AHU SMOKE DAMPER COMMAND” (R‐4) coil end up on the same 24 V leg (TB AC) instead of one side going to **24 V L** and the other to **24 V N**.  In other words, there’s **no complete path** for current through that relay coil.  

Most often, this happens because the neutral leg was never landed on the other side of the coil, or because the fire‐alarm interlock contact was mis‐wired so that you don’t actually get a return to neutral.  Once you fix the wiring so that R‐4 really goes **from** 24 V L **through** the relay coil **to** 24 V N (with any interlock contacts in series), the damper command circuit will work.

