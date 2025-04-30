find_package(Python COMPONENTS Interpreter Development REQUIRED)
find_package(nanobind CONFIG REQUIRED)

nanobind_add_module(myextension
  myextension_py.cpp
)

target_link_libraries(myextension PRIVATE myextension_core)

install(TARGETS myextension
    RUNTIME DESTINATION ${PYTHON_SITEARCH}   # .pyd on Windows
    LIBRARY DESTINATION ${PYTHON_SITEARCH}   # .so on Linux/macOS
    MODULE DESTINATION ${PYTHON_SITEARCH}    # for MODULE targets
)