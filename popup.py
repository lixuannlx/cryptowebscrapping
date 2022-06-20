import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()

ROOT.withdraw()
#the input dialog
USER_INP = simpledialog.askstring(title="Bitcoin Address",
                            prompt="What's your bitcoin transaction address?")

print(USER_INP)