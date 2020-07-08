from conans import ConanFile, CMake, tools
from conans.errors import ConanInvalidConfiguration
import os.path


class QuaZipConan(ConanFile):
    name = "quazip"
    version="0.9.1"
    license = "LGPL-2.1, zlib/png"
    url = "https://github.com/vaerizk/quazip"
    homepage = "https://github.com/stachenov/quazip"
    description = "A C++ wrapper for Gilles Vollant's ZIP/UNZIP package (AKA Minizip) using Qt library"
    topics = ("quazip", "conan-recipe")

    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {
        "shared": True,
        "zlib:shared": False
    }

    generators = "cmake_paths"
    exports_sources = "*"
    no_copy_source = True

    def configure(self):
        if self.settings.os != "Windows":
            raise ConanInvalidConfiguration("Only windows is supported at the moment")

    def build_requirements(self):
        self.build_requires("cmake/[>3.0.0]")

    def requirements(self):
        self.requires("qt/[5.12.7]@bincrafters/stable", private=False)
        self.requires("zlib/1.2.11", private=False)

    def build(self):
        cmake = CMake(self)
        cmake.definitions["VERSION"] = self.version
        cmake.definitions["CMAKE_TOOLCHAIN_FILE"] = os.path.join(self.build_folder, "conan_paths.cmake")
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
