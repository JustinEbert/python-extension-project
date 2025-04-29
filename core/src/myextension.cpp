#include "myextension/myextension.hpp"

namespace myextension {
static float total_mass = 0.0f;

void initialize() {
    total_mass = 0.0f;
}

GrowthResult step(float dt) {
    constexpr float k = 0.1f;
    float delta = k * dt;
    total_mass += delta;
    return { delta };
}

} // namespace myextension
