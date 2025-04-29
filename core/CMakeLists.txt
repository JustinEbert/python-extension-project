add_library(myextension_core
  src/myextension.cpp
)

target_include_directories(myextension_core PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>
)

set_target_properties(myextension_core PROPERTIES
  PUBLIC_HEADER include/myextension/myextension.hpp
)