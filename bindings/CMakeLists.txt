find_package(Python COMPONENTS Interpreter Development REQUIRED)
find_package(nanobind CONFIG REQUIRED)

nanobind_add_module(myextension
  myextension_py.cpp
)

target_link_libraries(myextension PRIVATE myextension_core)

install(TARGETS myextension
  RUNTIME DESTINATION .    # .pyd on Windows → <venv>/Lib/site-packages/
  LIBRARY DESTINATION .    # .so/.dylib on Unix → <venv>/lib/pythonX.Y/site-packages/
)