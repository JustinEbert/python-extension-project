#include <cassert>
#include "myextension/myextension.hpp"

int main() {
    // Reset and run one step
    myextension::initialize();
    auto res = myextension::step(1.0f);

    // Check that delta_mass is positive
    assert(res.delta_mass > 0.0f);

    return 0;
}
