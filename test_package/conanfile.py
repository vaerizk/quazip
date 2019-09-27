from conans import ConanFile, CMake, tools

import os

class QuaZipTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake_paths"

    def build(self):
        cmake = CMake(self)
        cmake.definitions["CMAKE_TOOLCHAIN_FILE"] = os.path.join(self.build_folder, "conan_paths.cmake")
        # Current dir is "test_package/build/<build_id>" and CMakeLists.txt is
        # in "test_package"
        cmake.configure()
        cmake.build()

    def imports(self):
        self.copy("*.dll", dst=str(self.settings.build_type), src="bin")

    def test(self):
        if not tools.cross_building(self.settings):
            os.chdir(str(self.settings.build_type))
            self.run(".%sexample" % os.sep)
