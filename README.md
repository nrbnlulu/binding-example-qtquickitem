### tested on:
- Python 3.10.4
- ubuntu 22.0.4 wayland

### requirements
- $HOME/Qt/6.3.1/gcc_64/lib/libicu exists and installed by qt installer.
- Python

### run the script to reproduce:
`source setup.sh`

### The error you should get is:
```console
ERROR: conanfile.py (components/0.0.1): Error in build() method, line 52
        self.run(f"cd pyside-setup &&  python setup.py install --qtpaths={str(qtpaths)} --build-tests --ignore-git --parallel=8")
        ConanException: Error 1 while executing cd pyside-setup &&  python setup.py install --qtpaths=/home/nir/.conan/data/qtbase/6.3.1/qt/everywhere/package/104607a54e9359271f3fb11915c98c044cb110c7/bin/qtpaths --build-tests --ignore-git --parallel=8
```

