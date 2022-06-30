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
Traceback (most recent call last):
  File "/home/nir/Desktop/issues/binding-example-qtquickitem/build/pyside-setup/setup.py", line 78, in <module>
    setup_runner.run_setup()
  File "/home/nir/Desktop/issues/binding-example-qtquickitem/build/pyside-setup/build_scripts/setup_runner.py", line 240, in run_setup
    self.run_setuptools_setup()
  File "/home/nir/Desktop/issues/binding-example-qtquickitem/build/pyside-setup/build_scripts/setup_runner.py", line 313, in run_setuptools_setup
    setup(**kwargs)
  File "/home/nir/Desktop/issues/binding-example-qtquickitem/venv/lib/python3.10/site-packages/setuptools/__init__.py", line 87, in setup
    return distutils.core.setup(**attrs)
  File "/home/nir/Desktop/issues/binding-example-qtquickitem/venv/lib/python3.10/site-packages/setuptools/_distutils/core.py", line 148, in setup
    return run_commands(dist)
  File "/home/nir/Desktop/issues/binding-example-qtquickitem/venv/lib/python3.10/site-packages/setuptools/_distutils/core.py", line 163, in run_commands
    dist.run_commands()
  File "/home/nir/Desktop/issues/binding-example-qtquickitem/venv/lib/python3.10/site-packages/setuptools/_distutils/dist.py", line 967, in run_commands
    self.run_command(cmd)
  File "/home/nir/Desktop/issues/binding-example-qtquickitem/venv/lib/python3.10/site-packages/setuptools/dist.py", line 1229, in run_command
    super().run_command(command)
  File "/home/nir/Desktop/issues/binding-example-qtquickitem/venv/lib/python3.10/site-packages/setuptools/_distutils/dist.py", line 986, in run_command
    cmd_obj.run()
  File "/home/nir/Desktop/issues/binding-example-qtquickitem/build/pyside-setup/build_scripts/main.py", line 238, in run
    _install.run(self)
  File "/home/nir/Desktop/issues/binding-example-qtquickitem/venv/lib/python3.10/site-packages/setuptools/command/install.py", line 72, in run
    orig.install.run(self)
  File "/home/nir/Desktop/issues/binding-example-qtquickitem/venv/lib/python3.10/site-packages/setuptools/_distutils/command/install.py", line 670, in run
    self.run_command('build')
  File "/home/nir/Desktop/issues/binding-example-qtquickitem/venv/lib/python3.10/site-packages/setuptools/_distutils/cmd.py", line 313, in run_command
    self.distribution.run_command(command)
  File "/home/nir/Desktop/issues/binding-example-qtquickitem/venv/lib/python3.10/site-packages/setuptools/dist.py", line 1229, in run_command
    super().run_command(command)
  File "/home/nir/Desktop/issues/binding-example-qtquickitem/venv/lib/python3.10/site-packages/setuptools/_distutils/dist.py", line 986, in run_command
    cmd_obj.run()
  File "/home/nir/Desktop/issues/binding-example-qtquickitem/build/pyside-setup/build_scripts/main.py", line 432, in run
    self.build_extension(ext)
  File "/home/nir/Desktop/issues/binding-example-qtquickitem/build/pyside-setup/build_scripts/main.py", line 892, in build_extension
    raise DistutilsSetupError(f"Error pseudo installing {extension}")
setuptools._distutils.errors.DistutilsSetupError: Error pseudo installing pyside-tools
Traceback (most recent call last):
  File "/home/nir/Desktop/issues/binding-example-qtquickitem/build/pyside-setup/setup.py", line 78, in <module>
    setup_runner.run_setup()
  File "/home/nir/Desktop/issues/binding-example-qtquickitem/build/pyside-setup/build_scripts/setup_runner.py", line 296, in run_setup
    raise RuntimeError(msg)
RuntimeError: 
setup.py invocation failed with exit code: 1.


setup.py invocation was: /home/nir/Desktop/issues/binding-example-qtquickitem/venv/bin/python setup.py install --qtpaths=/home/nir/.conan/data/qtbase/6.3.1/qt/everywhere/package/104607a54e9359271f3fb11915c98c044cb110c7/bin/qtpaths --build-tests --ignore-git --parallel=8 --internal-build-type=pyside6

ERROR: conanfile.py (components/0.0.1): Error in build() method, line 52
        self.run(f"cd pyside-setup &&  python setup.py install --qtpaths={str(qtpaths)} --build-tests --ignore-git --parallel=8")
        ConanException: Error 1 while executing cd pyside-setup &&  python setup.py install --qtpaths=/home/nir/.conan/data/qtbase/6.3.1/qt/everywhere/package/104607a54e9359271f3fb11915c98c044cb110c7/bin/qtpaths --build-tests --ignore-git --parallel=8
```

