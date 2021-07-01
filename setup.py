#setup.py
import sys, os
from cx_Freeze import setup, Executable

__version__ = "1.1.0"

include_files = ["assets", "save"]
excludes = ["matplotlib.tests", "numpy", "pygame"]
packages = ["os", "math", "random","OpenGL", "json", "time", "tkinter"]

setup(
    name = "The Mummy",
    description='my lovely game',
    version=__version__,
    options = {"build_exe": {
    'packages': packages,
    'include_files': include_files,
    'excludes': excludes,
    'include_msvcr': True,
}},
executables = [Executable(
    script="game.py",
    base="Win32GUI",
    icon="mummy.ico"
    )]
)