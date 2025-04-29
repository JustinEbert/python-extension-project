#pragma once

namespace myextension {

/// Result of one growth step.
struct GrowthResult {
    float delta_mass;
    // …extend with more fields as needed…
};

/// Reset simulation state.
void initialize();

/// Advance simulation by dt seconds.
GrowthResult step(float dt);

} // namespace myextension
