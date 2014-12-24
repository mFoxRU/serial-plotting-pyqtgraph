__author__ = 'CLTanuki'
import sys
try:
    from cx_Freeze import setup, Executable
except ImportError:
    from setuptools.command import easy_install
    easy_install.main(["cx_Freeze"])
    from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
files = [('C:\\Python\\2.7\\Lib\\site-packages\\scipy\\special\\_ufuncs.pyd', '_ufuncs.pyd'),
         ('C:\\Python\\2.7\\Lib\\site-packages\\scipy\\special\\_ufuncs_cxx.pyd', '_ufuncs_cxx.pyd')]
build_exe_options = {"packages": ['scipy', 'scipy.special._ufuncs_cxx', 'scipy.special._ufuncs', 'numpy', 'pyqtgraph', 'PyQt4'],
                     "include_files": files}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="serplot",
      version="0.1",
      description="Serial Port Plotting app",
      # options={"build_exe": build_exe_options},
      executables=[Executable("serplotgui.py", base=base)])