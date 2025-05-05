#include "myextension/myextension.hpp"

#include <nanobind/nanobind.h>

namespace nb = nanobind;

NB_MODULE(myextension, m) {
      m.doc() = "MyExtension: sim_value sampler";
  
      m.def("sim_value",
          [] (float t) {
              // a static local inside the lambda is fine
              static myextension::Sampler sampler;
              return sampler.sim_value(t);
          },
          "Generate a randomly varying amplitude & period sine at time t",
          nb::arg("t"));
  }
  