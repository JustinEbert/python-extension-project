#include "myextension/myextension.hpp"

#include <corecrt_math_defines.h>

namespace myextension {

Sampler::Sampler(uint32_t seed)
  : cycleStart(0.0f),
    periodDist(0.5f, 1.5f),
    ampDist(0.1f, 1.0f),
    rng(seed)
{
    // initialize the first cycle
    period    = periodDist(rng);
    amplitude = ampDist(rng);
}

void Sampler::seed(uint32_t s) {
    rng.seed(s);
    cycleStart = 0.0f;
    period     = periodDist(rng);
    amplitude  = ampDist(rng);
}

float Sampler::sim_value(float t) {
    // advance through any full cycles
    while (t >= cycleStart + period) {
        cycleStart += period;
        period      = periodDist(rng);
        amplitude   = ampDist(rng);
    }
    // compute normalized phase in [0, 2π)
    float theta = 2.0f * static_cast<float>(M_PI) *
                  (t - cycleStart) / period;
    return amplitude * std::sin(theta);
}

} // namespace myextension