import myextension

def test_step_returns_positive_delta():
    myextension.initialize()
    result = myextension.step(2.5)
    assert hasattr(result, "delta_mass")
    assert result.delta_mass > 0

def test_multiple_steps_accumulate():
    myextension.initialize()
    deltas = [myextension.step(1.0).delta_mass for _ in range(5)]
    # Every step should produce the same positive delta_mass
    assert all(d > 0 for d in deltas)
    # Optionally, check they’re consistent
    assert len(set(deltas)) == 1
