import sys
from cx_Freeze import setup, Executable
import os.path
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

# Dependencies are automatically detected, but it might need fine tuning.
additional_modules = []

build_exe_options = {"includes": additional_modules,
                      #"packages": [ "os", "shutil", "subprocess", "getpass", "time", "os.path"],
                     #"excludes": ['tkinter'],
                     "include_files": [
                         os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
                         os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
                         'bird.ico', 'assets/']}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="Save The Bird",
      version="1.0",
      description="Save The Bird",
      options={"build_exe": build_exe_options},
      executables=[Executable("Save-The-Bird.py", targetName='Save-The-Bird.exe',
			    icon='bird.ico',
			    copyright='Copyright (C) Rajender Kumar 2019', base=base)])