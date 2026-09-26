"""
Tests for motion_pipeline.py. Values independently verified with a
reference implementation before being written here.
"""
import pytest

from motion_pipeline import (
    count_raw_high_runs,
    debounce_motion,
    pipeline_latency_ms,
    meets_latency_target,
)


def test_count_raw_high_runs_simple():
    assert count_raw_high_runs([1, 0, 1, 1, 0, 1]) == 3


def test_count_raw_high_runs_no_motion():
    assert count_raw_high_runs([0, 0, 0, 0]) == 0


def test_debounce_motion_filters_flickers_keeps_real_events():
    signal = [1,0,1,0,0,1,1,1,1,1,0,0,1,0,0,0,0,0,1,1,1,1,1,1,0,1,0]
    assert debounce_motion(signal, 4, 3) == [5, 18]


def test_debounce_motion_no_events_when_all_flickers():
    signal = [1, 0, 1, 0, 1, 0, 1]
    assert debounce_motion(signal, 4, 3) == []


def test_debounce_motion_single_long_event():
    signal = [0, 0, 1, 1, 1, 1, 1, 0, 0]
    assert debounce_motion(signal, 4, 2) == [2]


def test_pipeline_latency_ms_sums_all_three_stages():
    assert pipeline_latency_ms(150, 800, 400) == 1350


def test_meets_latency_target_under_default():
    assert meets_latency_target(1350) is True


def test_meets_latency_target_over_default():
    assert meets_latency_target(2500) is False


def test_meets_latency_target_custom_threshold():
    assert meets_latency_target(1800, target_ms=1500) is False
