cmake_minimum_required(VERSION 2.8.12)
project(PackageTest CXX)

find_package(quazip REQUIRED)

add_executable(example example.cpp)

target_link_libraries(example quazip)

# CTest is a testing tool that can be used to test your project.
# enable_testing()
# add_test(NAME example
#          WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
#          COMMAND example)
