#include "myextension/myextension.hpp"

#include <nanobind/nanobind.h>

namespace nb = nanobind;

NB_MODULE(myextension, m) {
    m.doc() = "MyExtension: deterministic sim_value sampler";

    // single shared sampler
    static myextension::Sampler sampler{12345u};

    m.def("seed",
          [] (uint32_t s) { sampler.seed(s); },
          "Reseed the sim_value sampler RNG",
          nb::arg("seed"));

    m.def("sim_value",
          [] (float t) { return sampler.sim_value(t); },
          "Generate a randomly varying sine at time t",
          nb::arg("t"));
}