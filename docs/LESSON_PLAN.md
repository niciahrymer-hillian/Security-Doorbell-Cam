# 📖 Lesson Plan — Security-Doorbell-Cam

> **Chain K — Hardware & Systems Foundations** | A Pi-based camera + motion sensor + notifications —
> build the thing a commercial smart doorbell is, and keep the footage on your own hardware instead of
> a vendor's cloud.

## What This Project Is

A commercial smart doorbell is a camera, a PIR sensor, a speaker/mic, and a subscription that ships
your footage to someone else's server. Building the same thing means the footage stays on hardware you
control, and it puts a real face on "computer vision" and "push notifications" — not as abstractions,
but as a motion event that has to become a phone alert in under a couple of seconds to be useful at
all. The four lessons build the real edge-computing pipeline in order: camera + motion sensing first,
then the notification pipeline and its latency budget, then two-way audio, then local storage and
weatherproofing.

## Learning Objectives

By the end I can:

1. Interface a Pi Camera and a PIR sensor, and debounce a noisy PIR signal into real, confirmed motion
   events instead of false triggers.
2. Design a detection pipeline and budget its real end-to-end latency against a "useful within a
   couple of seconds" target.
3. Wire two-way audio (mic + speaker) for a real intercom feature without feedback.
4. Set up local footage retention with a real rolling-storage policy, and weatherproof an
   outdoor-mounted build correctly.

## Software You Will Use

- `picamera2` (or `libcamera`) for capturing from the Pi Camera.
- `RPi.GPIO` or `gpiozero` for reading the PIR sensor.
- A push-notification service (e.g. NTFY, Pushover, or a simple webhook) for phone alerts.
- MotionEyeOS or a custom retention script for local footage storage.

## Build Order

1. Interface the camera and PIR sensor; capture a test snapshot on motion with no debouncing yet —
   observe how often it fires on sunlight, passing cars, or blowing leaves.
   🔗 [Pi My Life Up — Raspberry Pi Motion Sensor using a PIR Sensor](https://pimylifeup.com/raspberry-pi-motion-sensor/)
2. Add a debounce + cooldown filter in software and tune sensitivity/delay until false triggers drop
   to near zero without missing real motion.
3. Wire up notifications and measure your actual end-to-end latency from motion to phone alert; budget
   each pipeline stage until you're reliably under ~2 seconds.
   🎥 [Real Time Motion Notifications with Raspberry Pi 5 and NTFY](https://www.youtube.com/watch?v=VFAqYllWhm0) (BMonster Laboratory)
4. Add two-way audio (mic + speaker) if building the full intercom feature; keep the amp/speaker
   physically separated from the mic to avoid feedback.
   🔗 [Fast Video Doorbell / Intercom on Raspberry Pi](https://www.instructables.com/Fast-Video-Doorbell-Intercom-on-Raspberry-Pi/) (Instructables)
5. Set up local footage retention with an automatic rolling-storage policy (max size or max days)
   rather than letting the SD card fill up; if mounting outside, apply the weatherproofing pattern from
   Walkie-Talkie-Build.
   🔗 [MotionEyeOS](https://motioneyeos.org/)

## Common Mistakes to Avoid

- PIR false-triggers from sunlight/heat sources or moving foliage — tune sensitivity and add a
  debounce delay in software.
- Notification latency if the detection pipeline is too heavy for a Zero-class board.
- Condensation/sealing issues if mounted outside — the same problem every outdoor build in this chain
  has to solve.
- Letting local footage fill the SD card with no retention policy, instead of a rolling max-size or
  max-days limit.
- Running the speaker/amp too close to the mic in a small enclosure, causing audio feedback.

## Check Your Understanding

The quiz covers debounce logic and why it's the real fix for PIR false triggers, end-to-end latency
budgeting math, why audio feedback happens, storage retention policy reasoning, and the specific
weatherproofing distinction between the camera (can go behind a sealed window) and the PIR sensor
(needs direct exposure).

## Why This Matters (Industry Application)

This is a real, complete edge-computing pipeline in miniature: sensor trigger → local
inference/decision → notification — the same shape as industrial and retail computer-vision
deployments, just small enough to build and fully understand yourself.

## Reflection Questions

- What's the actual tradeoff between debouncing aggressively (fewer false alerts) and missing brief,
  real motion events?
- Why does this project count as "a real edge-computing pipeline in miniature," and what would change
  about it if you scaled it to 50 doorbells instead of 1?
