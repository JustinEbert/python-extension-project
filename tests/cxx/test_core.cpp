#include <iostream>
#include "myextension/myextension.hpp"

int main() {
    // Reset and run one step
    myextension::initialize();
    auto res = myextension::step(1.0f);

    // Check that delta_mass is positive
    if (res.delta_mass > 0.0f) {
        std::cout << "✔ Test passed: delta_mass = " 
                  << res.delta_mass << std::endl;
        return 0;
    }
    else {
        std::cerr << "✘ Test FAILED: delta_mass = " 
                  << res.delta_mass << std::endl;
        return 1;
    }
}
