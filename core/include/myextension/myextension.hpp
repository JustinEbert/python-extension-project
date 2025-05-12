#pragma once

#include <random>
#include <cmath>

namespace myextension {

class Sampler {
public:
    /// Construct with an explicit RNG seed (default 12345 for deterministic runs)
    explicit Sampler(uint32_t seed = 12345u);

    /// Reseed the sampler mid-run (also resets the cycle start)
    void seed(uint32_t s);

    /// Sample the value at time t
    float sim_value(float t);

private:
    float cycleStart;    ///< start time of the current cycle
    float period;        ///< length of the current cycle in seconds
    float amplitude;     ///< amplitude for the current cycle

    std::mt19937 rng;    ///< random‐number engine
    std::uniform_real_distribution<float> periodDist;  ///< [0.5, 1.5]s
    std::uniform_real_distribution<float> ampDist;     ///< [0.1, 1.0]
};

} // namespace myextension
