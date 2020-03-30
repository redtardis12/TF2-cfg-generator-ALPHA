import cx_Freeze
import sys
import matplotlib

base = 'Win32GUI'

executables = [cx_Freeze.Executable('main.py', base=base, icon='icon.ico')]

cx_Freeze.setup(
    name = 'main',
    options = {"build.exe": {"packages": ["tkinter", "matplotlib"], "include_files": ["icon.ico"]}},
    version = "0.0.3",
    description = "AlPHA v0.0.3",
    executables = executables
)