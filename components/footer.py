"""
This file creates the footer witch is on every page
of the wmain window. The foorter is a static element
that is meant to repercent future capabilites if I 
had mroe time.
"""

import tkinter as tk
import backend_functions as hf
import constants as const

class Footer(tk.Frame):
    """
    The footer element has one lable deisgned to rpeercent the current
    device sutabiltiy for conectivity by depictign the wifi.
    """
    def __init__(self, parent, controller):
        """Initialises the single lable as a child of the command aplication"""
        self.controller = controller
        super().__init__(parent) # Inheritance parent data
        # Overall status Footer
        self.system_status_frame = hf.config_frame(parent, 1, 4, 1, True, 2, 0, True, const.MIDGROUND_COLOR)
        self.status_label = hf.create_label(parent=self.system_status_frame, message="Status: Stable connection", pos_x=0, pos_y=2, bg_color=const.BACKGROUND_COLOR)
