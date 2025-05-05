#pragma once

#include <random>
#include <cmath>

namespace myextension {

// Stateful sampler for sim_value
class Sampler {
public:
    Sampler();

    // Given time t, returns amplitude * sin(normalized phase)
    float sim_value(float t);

private:
    float cycle_start_;
    float period_;
    float amp_;
    std::mt19937 rng_;
    std::uniform_real_distribution<float> period_dist_;
    std::uniform_real_distribution<float> amp_dist_;
};

} // namespace myextension
