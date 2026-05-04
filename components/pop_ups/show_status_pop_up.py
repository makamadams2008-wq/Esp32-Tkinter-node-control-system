import tkinter as tk
import backend_functions as hf
import constants as const
import ghost_device_data


class ShowPopUp(tk.Frame):
    def __init__(self, parent_root, controller, device):
        super().__init__(parent_root) # Inheritance parent data
        self.controller = controller

