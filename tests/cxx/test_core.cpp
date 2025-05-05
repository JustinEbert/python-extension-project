#include "myextension/myextension.hpp"

#include <iostream>
#include <algorithm>
#include <cmath>
#include <limits>

int main() {
    myextension::Sampler sampler;

    bool success = true;
    float max_val = -std::numeric_limits<float>::infinity();
    float min_val =  std::numeric_limits<float>::infinity();

    // Sample from t=0 to t=10s in 0.01s steps
    for (int i = 0; i <= 1000; ++i) {
        float t = i * 0.01f;
        float v = sampler.sim_value(t);

        // Check for finite output
        if (!std::isfinite(v)) {
            std::cerr << "✘ Non‑finite value at t=" << t << ": " << v << "\n";
            success = false;
            break;
        }

        max_val = std::max(max_val, v);
        min_val = std::min(min_val, v);
    }

    // The amplitude is randomized between 0.1 and 1.0,
    // so |v| should never exceed ~1.0 + small float error.
    constexpr float kTolerance = 0.05f;
    if (max_val > 1.0f + kTolerance || min_val < -1.0f - kTolerance) {
        std::cerr << "✘ Values out of expected bounds: ["
                  << min_val << ", " << max_val << "]\n";
        success = false;
    }

    if (success) {
        std::cout << "✔ sim_value() outputs finite values within ±1.05 over [0,10]s\n";
        return 0;
    } else {
        return 1;
    }
}
