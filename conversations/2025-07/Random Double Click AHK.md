---
type: Conversation
title: "Random Double Click AHK"
description: "write me an auto hot key that double clicks once randomly between 30 seconds and 1 minute"
resource: "68669af8-a684-8003-a201-2d730fd37dea"
timestamp: "2025-07-03T15:01:37.540Z"
tags: ["gpt-4o"]
---

# Random Double Click AHK

## User

write me an auto hot key that double clicks once randomly between 30 seconds and 1 minute

## Assistant



## Assistant

Here is a simple AutoHotkey (AHK) script that performs a **double-click** at a random interval between **30 seconds (30,000 ms)** and **1 minute (60,000 ms)**:

```ahk
#Persistent
SetTimer, DoDoubleClick, % RandomTime()

DoDoubleClick:
    Click 2  ; Double-click
    SetTimer, DoDoubleClick, % RandomTime()
return

RandomTime() {
    Random, rand, 30000, 60000  ; Generate random time between 30,000 and 60,000 ms
    return rand
}
```

### How it works:
- `#Persistent`: Keeps the script running.
- `SetTimer`: Schedules the `DoDoubleClick` label to run at the randomly chosen interval.
- `Click 2`: Performs a double-click at the current mouse position.
- `RandomTime()`: Custom function to generate a new random delay between 30 and 60 seconds each time.

### To use:
1. Install AutoHotkey from https://www.autohotkey.com/.
2. Save the script above into a `.ahk` file.
3. Double-click the file to run it.

Let me know if you want it to click at a specific screen location or only when a key is held!

## User

actually can you add a start and stop button? So I can press f1 to start it and f1 again to stop it

## Assistant

Absolutely! Here's the updated AutoHotkey script that lets you toggle the random double-clicking **on and off with `F1`**:

```ahk
toggle := false  ; Initial state is off
timerID := "DoubleClickLoop"

F1::
toggle := !toggle
if (toggle) {
    SetTimer, %timerID%, % RandomTime()
    ToolTip, Double-clicking started.
} else {
    SetTimer, %timerID%, Off
    ToolTip, Double-clicking stopped.
    SetTimer, RemoveTooltip, -1000
}
return

DoubleClickLoop:
Click 2
SetTimer, %timerID%, % RandomTime()
return

RandomTime() {
    Random, rand, 30000, 60000  ; Random time between 30,000 and 60,000 ms
    return rand
}

RemoveTooltip:
ToolTip
return
```

### What this does:
- Pressing `F1` starts the script (if it’s off) or stops it (if it’s running).
- A tooltip shows whether the double-clicking is active.
- The timer randomly re-schedules itself after each click.

Let me know if you'd like it to click in a certain window or location, or if you want a hotkey to exit the script entirely!

