import tkinter as tk
import backend_functions as hf
import constants as const
import ghost_device_data

class UpdatePopUp(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent) # Inheritance parent data
        self.controller = controller
        print(f"The pop up should show up now")
