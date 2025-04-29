#include <nanobind/nanobind.h>
#include <myextension/myextension.hpp>

namespace nb = nanobind;
using namespace nb::literals;

NB_MODULE(myextension, m) {
    m.doc() = "Python extension scaffolding";

    m.def("initialize", &myextension::initialize,
          "Reset simulation state");

    m.def("step", &myextension::step,
          "Advance by dt seconds", "dt"_a);

    nb::class_<myextension::GrowthResult>(m, "GrowthResult")
      .def_ro("delta_mass", &myextension::GrowthResult::delta_mass);
}
