import os
import sys

# The path of the Python script file
script_path = os.path.abspath(sys.argv[0])

# Path to the Startup folder
startup_folder = os.path.join(os.environ["APPDATA"], "Microsoft\\Windows\\Start Menu\\Programs\\Startup")

# Shortcut file path in the Startup folder
shortcut_path = os.path.join(startup_folder, "myscript.lnk")

# Create shortcuts using the pywin32 library
from win32com.client import Dispatch
shell = Dispatch('WScript.Shell')
shortcut = shell.CreateShortCut(shortcut_path)
shortcut.TargetPath = script_path
shortcut.WorkingDirectory = os.path.dirname(script_path)
shortcut.Save()
