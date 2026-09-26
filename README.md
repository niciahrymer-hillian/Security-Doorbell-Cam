# Security-Doorbell-Cam

### A Pi-based camera + motion sensor + notifications — build the thing a commercial smart doorbell is, and keep the footage on your own hardware instead of a vendor's cloud.

![Chain K](https://img.shields.io/badge/Chain%20K-64748B?style=for-the-badge) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue?style=for-the-badge)](LICENSE-GPL) [![License: AGPL v3](https://img.shields.io/badge/License-AGPLv3-blue?style=for-the-badge)](LICENSE-AGPL)

[🎮 Interactive Tour](docs/interactive/index.html) · [📋 Cheat Sheet](docs/CHEATSHEET.pdf) · [📖 Full Lesson](docs/LESSON.pdf) · [🔗 Resources](docs/RESOURCES.pdf) · [📖 Lesson Plan](docs/LESSON_PLAN.md)

<!-- SCREENSHOT PLACEHOLDER: docs/screenshots/overview.png -->

Real-hardware build with an emulation/planning-first path. Part of **Chain K — Hardware & Systems
Foundations**. Builds on **Raspberry-Pi-Tinkering**'s GPIO/camera basics; reuses audio skills from
**Cyberdeck-Cellular-And-Media** and waterproofing from **Walkie-Talkie-Build**.

## What this is

A commercial smart doorbell is a camera, a PIR sensor, a speaker/mic, and a subscription that ships
your footage to someone else's server. Building the same thing means the footage stays on hardware you
control, and it puts a real face on "computer vision" and "push notifications" — not as abstractions,
but as a motion event that has to become a phone alert in under a couple of seconds to be useful at
all. The four lessons build the real edge-computing pipeline in order: camera and motion sensing first
(and the debounce logic that actually fixes PIR false triggers), then the notification pipeline and its
real latency budget, then two-way audio without feedback, then local storage retention and
weatherproofing camera vs. PIR differently. Debounce a real noisy PIR signal and budget a real
notification latency in the **Motion & Notification Pipeline Simulator** tab before it's your own front
door generating false alerts.

## Prerequisites

| Requirement | Notes |
|---|---|
| A modern browser | Chrome, Firefox, Safari, or Edge — the interactive tour is a single HTML file, no install |
| Python 3.8+ (for the exercises) | Check with `python3 --version` |
| A Raspberry Pi + camera + PIR sensor (optional for the tour/exercises) | Only needed for a real build — the tour and exercises need nothing but a browser and Python |

## Items Needed

- [ ] A Raspberry Pi — see [Hardware Buying Guide](#hardware-buying-guide-what-to-look-for--red-flags) below (Zero 2 W for snapshots/motion, Pi 4/5 for real-time streaming)
- [ ] An official Pi Camera Module (real driver support, unlike generic clones)
- [ ] A PIR motion sensor with adjustable sensitivity/delay
- [ ] A small speaker + electret mic, if adding two-way audio
- [ ] A weatherproof enclosure, if mounting outside
- [ ] Nothing else required for the tour or exercises — just a browser and Python

## Quick Start

1. **Open the interactive tour.** Double-click `docs/interactive/index.html` — no server, no build step.
2. **Work Lesson 1 (Camera & motion detection)**, then open the **Motion & Notification Pipeline
   Simulator** tab's debounce panel and regenerate a few noisy signals.
3. **Do the skeleton-code exercise.**
   ```bash
   cd exercises
   python3 -m venv .venv && source .venv/bin/activate
   pip install pytest
   pytest -v
   ```
   You'll see 9 failing tests. Open `exercises/motion_pipeline.py` and implement the four functions —
   full instructions in [`exercises/README.md`](exercises/README.md).
4. **Work Lesson 2 (Edge pipeline & notifications)**, then try a heavy inference value in the
   Simulator's latency panel and watch the pipeline miss its target.
   > ⚠️ **You may get stuck here:** if your real pipeline misses its latency target, check which stage
   > is actually slow before "fixing" one that isn't — a faster network connection won't help if
   > inference is the real bottleneck.
5. **Work Lesson 3 (Two-way audio)** if adding an intercom feature, and mock up speaker/mic placement
   before finalizing your enclosure.
6. **Work Lesson 4 (Storage & weatherproofing)**, and set a retention limit before your first real
   outdoor test.
7. **Then the Quiz**, then Flashcards/Match/Pop Quiz for review.
8. **Check the Report Card tab** any time. Click **Print / Save as PDF** to keep a dated copy in `docs/`.

## Exercise Overview

| # | Lesson | Concept | Motion & Notification Pipeline Simulator tie-in |
|---|---|---|---|
| 1 | Camera & motion detection | PIR debounce, cooldown | The debounce panel — filter flickers, confirm events |
| 2 | Edge pipeline & notifications | Latency budgeting | The latency panel — capture/inference/notify |
| 3 | Two-way audio | Feedback, physical separation | *(hands-on build — no simulator panel)* |
| 4 | Storage & weatherproofing | Rolling retention, camera vs. PIR sealing | *(hands-on build — no simulator panel)* |

**Learning path:**
```
Lesson 1 (camera & motion)  →  Lesson 2 (pipeline & notify)  →  Lesson 3 (audio)  →  Lesson 4 (storage & weatherproofing)
        ↓                                ↓
   Debounce panel                  Latency panel
        ↓                                ↓
              exercises/ (motion_pipeline.py)
                        ↓
        Quiz → Flashcards/Match/Pop Quiz → Report Card
```

## Hardware Buying Guide (What to look for & red flags)

**Parts list:** a Raspberry Pi (Zero 2 W is enough for motion detection + snapshots; a Pi 4/5 if you want
real-time video streaming too), an official Pi Camera Module, a PIR motion sensor, a small speaker +
electret mic if adding two-way audio, and a weatherproof enclosure if mounting outside (see
**Walkie-Talkie-Build**'s waterproofing section — the same pattern applies).

**What to look for:** the official Camera Module has far better driver support than generic clones; a
wide field-of-view lens version matters more for a doorbell (close, wide angle) than the standard one.

**Red flags:** generic "spy camera" modules with no documented interface to the Pi, and PIR sensors with
no adjustable sensitivity/delay (you'll want to tune both — default settings trigger constantly on
passing cars or blowing leaves).

**Common failure points:** PIR false-triggers from sunlight/heat sources or moving foliage (tune
sensitivity and add a debounce delay in software), notification latency if the detection pipeline is too
heavy for a Zero-class board, and — if mounted outside — the same condensation/sealing issues every
outdoor build in this chain has to solve.

## Wiring Diagrams

**Core build, with the solar variant called out.** Pi reads the camera over CSI, the PIR sensor on a GPIO
pin, and drives speaker/mic for two-way audio; the solar branch (dashed, yellow) replaces wall power —
panel → charge controller (low-voltage cutoff) → battery → Pi's 5V USB-C in. Real-time streaming (Pi 4/5)
draws meaningfully more continuous power than snapshot-only (Zero 2 W), which changes how the solar side
needs to be sized:

![Doorbell cam wiring diagram](docs/diagrams/wiring.svg)

**Weatherproof mount, cross-section.** The camera sits behind a sealed clear window (never tinted — kills
night IR), but the PIR sensor's fresnel lens has to stay physically exposed (just gasket-ringed) since it
needs direct IR line-of-sight — it can't go behind acrylic the way the camera can:

![Doorbell cam weatherproof enclosure diagram](docs/diagrams/waterproof-enclosure.svg)

## Parts & Pricing

Pulled from the chain-wide [Hardware Shopping List](../HARDWARE_SHOPPING_LIST.md#security-doorbell-cam) —
check there for current links; prices drift. **Budget/Mid/Luxury are the same tiers the shopping list calls
Budget/Mid/Premium.**

| Item | Budget | Mid | Luxury |
|---|---|---|---|
| Board | Pi Zero 2 W, ~$15–35 (snapshots/motion only) | Same | Pi 4, ~$55–75 — real-time video streaming |
| Camera | Generic Pi-compatible clone (~$10) | [Official Camera Module 3, ~$25](https://www.raspberrypi.com/products/camera-module-3/) — real driver support | [Camera Module 3 Wide, ~$35](https://www.amazon.com/Raspberry-Pi-Camera-Module-Wide/dp/B0BRY757NX) — 120° FOV, better doorbell framing |
| Motion sensor | Basic PIR module (~$8–10) | Same, adjustable sensitivity/delay pots | — (already the right pick at every tier) |
| **Solar power** *(optional variant)* | Generic 5–10W panel + basic controller (~$25–30) | Panel + controller **with low-voltage cutoff** (~$35–40) | Adafruit/Victron-class controller (~$20–40) + battery sized for Pi 4 streaming draw |
| **Weatherproof mount** *(optional variant)* | Generic project box + shared cable gland kit + clear acrylic window | [TICONN IP67 junction box, ~$25](https://www.amazon.com/TICONN-Waterproof-Electrical-Junction-Enclosure/dp/B0B87THLGC) | [Adafruit flanged weatherproof enclosure, ~$15–20](https://www.adafruit.com/product/3931) — glands pre-installed |

Running total, core build: **~$33–55 budget (Zero 2 W) → up to ~$110–135 luxury (Pi 4 + wide camera)**. Add
the solar and weatherproof rows for the full outdoor-mounted version — genuinely the more common way this
project actually gets built, since a doorbell cam mounted indoors isn't watching a door.

## Why This Matters (Industry Application)

This is a real, complete edge-computing pipeline in miniature: sensor trigger → local inference/decision →
notification — the same shape as industrial and retail computer-vision deployments, just small enough to
build and fully understand yourself.

## Topics Covered

| Area | What this project covers |
|------|--------------------------|
| Camera modules | Interfacing and capturing from the Pi Camera |
| Motion detection | PIR sensors and tuning false-trigger rate |
| Notifications | Getting an event to your phone quickly |
| Audio | Two-way speaker/mic for a real intercom feature |
| Storage | Local footage retention instead of a cloud subscription |
| Weatherproofing | Mounting a camera/electronics outside safely |

## How This Connects

Chain K (Hardware & Systems Foundations). Builds on **Raspberry-Pi-Tinkering**'s GPIO/camera basics;
reuses audio skills from **Cyberdeck-Cellular-And-Media** and waterproofing from **Walkie-Talkie-Build**.

## Project Layout

```
Security-Doorbell-Cam/
├── docs/
│   ├── interactive/index.html   # tour: lessons, quiz, flashcards, match, pop quiz, motion/notification simulator, report card
│   ├── LESSON_PLAN.md           # short build-plan reference
│   ├── LESSON.pdf               # the full written lesson, printable
│   ├── CHEATSHEET.pdf           # one-page recap, printable
│   ├── RESOURCES.pdf            # further-reading links, printable
│   └── diagrams/                # wiring.svg + waterproof-enclosure.svg
├── exercises/
│   ├── motion_pipeline.py       # skeleton — implement the 4 functions
│   ├── test_motion_pipeline.py
│   └── README.md
└── README.md                    # this file
```

---
Dual licensed — [GPL v3](LICENSE-GPL) and [AGPL v3](LICENSE-AGPL).
