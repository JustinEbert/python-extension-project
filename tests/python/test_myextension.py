import math

import myextension


def test_sim_value_returns_finite_float() -> None:
    # Test at a few sample times
    for t in [0.0, 0.3, 1.0, 2.5, 5.0, 7.7, 10.0]:
        v = myextension.sim_value(t)
        # It should be a Python float
        assert isinstance(v, float)
        # It should be finite
        assert math.isfinite(v)
        # And within the expected amplitude bounds (±1.0 ± small epsilon)
        assert -1.05 <= v <= 1.05


def test_sim_value_varies_over_time() -> None:
    # Sample at uniform intervals
    samples = [myextension.sim_value(i * 0.2) for i in range(20)]
    # Although random, we expect some variability:
    # not every sample should be exactly the same
    assert len(set(samples)) > 1


def test_sim_value_cycle_reset_behavior() -> None:
    # We know period is between 0.5 and 1.5s, so sim_value(t) = 0 at t=0
    # and again roughly at t=period. We can check that within 0.4–1.6s it crosses zero.
    zeros = []
    for t in [i * 0.1 for i in range(1, 17)]:  # from 0.1s to 1.6s
        v = myextension.sim_value(t)
        if abs(v) < 0.01:  # near zero
            zeros.append(t)
    # Expect at least one near-zero crossing in that window
    assert zeros, f"No zero crossings found in [0.1,1.6]s, got values {[myextension.sim_value(i * 0.1) for i in range(1, 17)]}"
