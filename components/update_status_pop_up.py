import tkinter as tk
import backend_functions as hf
import constants as const
import ghost_device_data

class UpdatePopUp(tk.Frame):
    def __init__(self, parent, controller, device):
        super().__init__(parent) # Inheritance parent data
        self.controller = controller
        print(device["device_name"])
        self.system_status_frame = hf.config_frame(parent, 1, 4, True, 2, 0, True, const.MIDGROUND_COLOR)
        self.status_label = hf.create_label(parent=self.system_status_frame, message="Status: Stable connection", pos_x=0, pos_y=2, bg_color=const.BACKGROUND_COLOR)
