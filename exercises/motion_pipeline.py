"""
Motion Pipeline -- fill in the four functions below.

The real logic behind the Motion & Notification Pipeline Simulator
tab: debouncing a noisy PIR signal into real motion events (the actual
fix for the "PIR false-triggers from sunlight/passing cars" Common
Mistake), and budgeting a detection pipeline's real latency against
the "must become a phone alert in under a couple of seconds" target
from this project's own Why This Was Built.

Run the tests as you go:  pytest exercises/test_motion_pipeline.py -v
All four start failing. Implement one function, re-run, watch it turn
green, move to the next.
"""


def count_raw_high_runs(signal):
    """Count every separate run of consecutive 1s in a raw PIR signal,
    with NO debouncing at all -- this is what a naive "notify on every
    HIGH reading" pipeline would fire on, flickers and real motion
    alike.

    >>> count_raw_high_runs([1, 0, 1, 1, 0, 1])
    3
    """
    # TODO: walk the signal; each time you see a 1 that isn't part of
    # a run you're already inside, count it, then skip past the rest
    # of that run.
    raise NotImplementedError


def debounce_motion(signal, min_high_samples, cooldown_samples):
    """Confirm a motion event only when the signal stays HIGH for at
    least min_high_samples consecutive samples -- a single-sample
    flicker from sunlight or a passing car never qualifies. After a
    confirmed event, skip cooldown_samples before looking for the next
    one, so one real motion doesn't get double-counted as it flickers
    near the end of its run. Returns the list of sample indices where
    each confirmed event started.

    >>> debounce_motion([1,0,1,0,0,1,1,1,1,1,0,0,1,0,0,0,0,0,1,1,1,1,1,1,0,1,0], 4, 3)
    [5, 18]
    """
    # TODO: walk the signal with index i. When signal[i] == 1, find the
    # full run length. If run_len >= min_high_samples, record i as a
    # confirmed event and jump i past the run PLUS cooldown_samples.
    # Otherwise just skip past the (too-short) run. When signal[i] == 0,
    # advance by 1.
    raise NotImplementedError


def pipeline_latency_ms(capture_ms, inference_ms, notify_ms):
    """The actual end-to-end latency budget: how long from a real
    motion event until a phone notification arrives, broken into the
    three real stages of the pipeline.

    >>> pipeline_latency_ms(150, 800, 400)
    1350
    """
    # TODO: return capture_ms + inference_ms + notify_ms
    raise NotImplementedError


def meets_latency_target(total_latency_ms, target_ms=2000):
    """Does the pipeline's total latency meet the "useful within a
    couple of seconds" target this project's own README sets?

    >>> meets_latency_target(1350)
    True
    >>> meets_latency_target(2500)
    False
    """
    # TODO: return total_latency_ms <= target_ms
    raise NotImplementedError
