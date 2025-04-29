cmake_minimum_required(VERSION 3.18)
project(myextension LANGUAGES CXX)

# There seems to be an unsolvable at this time problem with vcpkg integrate install so hard setting this for now
include("C:/Program Files/Microsoft Visual Studio/2022/Community/VC/vcpkg/scripts/buildsystems/vcpkg.cmake")

# Enable testing
include(CTest)
enable_testing()

# Build core lib and Python extension
add_subdirectory(core)
add_subdirectory(bindings)
add_subdirectory(tests/cxx)