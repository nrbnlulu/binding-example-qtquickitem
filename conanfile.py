from conans import ConanFile, CMake, paths
from pathlib import Path
CWD = Path.cwd()
icu_libs = Path.home() / 'icu_libs'


class RegexConan(ConanFile):
    name = "components"
    version = "0.0.1"
    # settings = "os", "arch", "compiler", "build_type"
    generators = "cmake_find_package", "virtualenv"
    requires = \
        "qtmultimedia/6.3.1@qt/everywhere", \
        "qtwayland/6.3.1@qt/everywhere", \
        "qtdeclarative/6.3.1@qt/everywhere", \
        "qtbase/6.3.1@qt/everywhere", \
        "qt5compat/6.3.1@qt/everywhere", \
        
    def package_info(self):
        self.env_info.CLANG_INSTALL_DIR = str(Path.cwd())
        self.env_info.use_always_short_paths = True
        self.env_info.LD_LIBRARY_PATH += str(icu_libs)


        
    def build_requirements(self):
        if not (CWD / "libclang").exists():
            self.run("wget https://download.qt.io/development_releases/prebuilt/libclang/libclang-release_100-based-linux-Rhel7.6-gcc5.3-x86_64.7z")
            self.run("7z x libclang-release_100-based-linux-Rhel7.6-gcc5.3-x86_64.7z")
            self.run("rm libclang-release_100-based-linux-Rhel7.6-gcc5.3-x86_64.7z")
        if not icu_libs.exists():
            icu_libs.mkdir()
            self.run("cp $HOME/Qt/6.3.1/gcc_64/lib/libicu* $HOME/icu_libs")            


    def export_sources(self):
        # -> copies all .cpp files from working dir to a "source" dir
        self.copy("*.cpp")
        # -> copies CMakeLists.txt from working dir to a "source" dir
        self.copy("CMakeLists.txt")

    def build(self):
        try:
            from PySide import QtCore
            assert QtCore.__version__ == "6.3.1"
        except ImportError:
            if not (Path(self.build_folder) / "pyside-setup").exists():
                self.run("git clone --recursive https://code.qt.io/pyside/pyside-setup")
                self.run("cd pyside-setup && git checkout 6.3.1")
            qtbase = self.deps_cpp_info['qtbase']
            qtpaths = Path(qtbase.bin_paths[0]) / 'qtpaths'
            self.run(f"cd pyside-setup &&  python setup.py install --qtpaths={str(qtpaths)} --build-tests --ignore-git --parallel=8")    
        # cmake = CMake(self)                # CMake helper auto-formats CLI arguments for CMake
        # cmake.configure()                  # cmake -DCMAKE_TOOLCHAIN_FILE=conantoolchain.cmake
        # cmake.build()                      # cmake --build .

    def package(self):
        ...
        # For CMake projects which define an install target, leverage it
        # cmake = CMake(self)
        # cmake.install()                    # cmake --build . --target=install
        # sets CMAKE_INSTALL_PREFIX = <appropriate directory in conan cache>
