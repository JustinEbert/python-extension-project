#include "myextension/myextension.hpp"

#include <corecrt_math_defines.h>

namespace myextension {

Sampler::Sampler()
  : cycle_start_(0.0f),
    // initial period 0.5–1.5s, amplitude 0.1–1.0
    period_dist_(0.5f, 1.5f),
    amp_dist_(0.1f, 1.0f),
    rng_(std::random_device{}())
{
    period_ = period_dist_(rng_);
    amp_    = amp_dist_(rng_);
}

float Sampler::sim_value(float t) {
    // If we've advanced past the current cycle, start a new one
    while (t >= cycle_start_ + period_) {
        cycle_start_ += period_;
        period_       = period_dist_(rng_);
        amp_          = amp_dist_(rng_);
    }
    // compute angle in [0,2π]
    float theta = 2.0f * static_cast<float>(M_PI) * (t - cycle_start_) / period_;
    return amp_ * std::sin(theta);
}

} // namespace myextension

