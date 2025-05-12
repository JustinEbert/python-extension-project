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


def test_sim_value_is_reproducible() -> None:
    # fixed seed
    SEED = 123456
    # sample times
    times = [i * 0.1 for i in range(20)]

    myextension.seed(SEED)
    first = [myextension.sim_value(t) for t in times]

    myextension.seed(SEED)
    second = [myextension.sim_value(t) for t in times]

    # they must be exactly the same
    assert first == second, f"Outputs differ: {first} vs {second}"
