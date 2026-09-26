# Exercises — Motion Pipeline

A hands-on companion to Lessons 1 and 2 in the interactive tour: the real debounce logic that turns a
noisy PIR signal into confirmed motion events, and the real latency-budget math behind "must become a
phone alert in under a couple of seconds to be useful at all."

## Setup

```bash
# from this exercises/ folder
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install pytest
```

## Run the tests

```bash
pytest -v
```

You'll see 8 failing tests — every function in `motion_pipeline.py` currently raises
`NotImplementedError`.

## What to do

Open `motion_pipeline.py`. Implement in this order:

1. `count_raw_high_runs` — what a naive, no-debounce pipeline would notify on: every flicker.
2. `debounce_motion` — the actual fix: require a sustained HIGH run, plus a cooldown after each
   confirmed event.
3. `pipeline_latency_ms` — the real end-to-end latency budget, stage by stage.
4. `meets_latency_target` — whether that budget actually meets the "useful within a couple of seconds"
   target.

## When you're done

All 8 tests passing means you have the real logic behind two of this project's own Common Mistakes:
tuning out PIR false-triggers, and keeping the notification pipeline fast enough on a Zero-class board
to actually be useful.
