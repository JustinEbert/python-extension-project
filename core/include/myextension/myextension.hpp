#pragma once

namespace myextension {

/// Result of one growth step.
struct GrowthResult {
    float delta_mass;
    float current_mass;
};

/// Reset simulation state.
void initialize();

/// Advance simulation by dt seconds.
GrowthResult step(float dt);

} // namespace myextension
