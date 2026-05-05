""" 
This file is responsable for the navbar witch is a static
element that depicts what page the user can see. This file
creates the navbar with three buttons.
"""

import tkinter as tk
import backend_functions as hf
import constants as const

class NavBar(tk.Frame):
    """
    A blueprint for the navbar whitch is a frame with threee buttons on it linking
    to the main dahsboard, current status, and update status pages.
    The navbar is the tieing link that alows for free clear flwo betwwen
    app states.
    """
    def __init__(self, parent, controller):
        """Initates the navbar elements soo they are clearly visable and interactive."""
        super().__init__(parent) # Inheritance parent data
        self.controller = controller

        self.navbar_frame = hf.config_frame(parent, 6, 1, 1, True, 0, 0, True, const.MIDGROUND_COLOR)

        # Dont mind the blanked out pages that is due to untyped routing
        nav_button_main_dashboard = tk.Button(self.navbar_frame, text="Main Dashboard", font=const.FONT_STATS, bg=const.BACKGROUND_COLOR, fg=const.ACCENT_COLOR, command= lambda: self.controller.set_page(self.controller.main_page.dashbord_frame) )
        nav_button_main_dashboard.grid(row=0, column=0, columnspan=2, sticky="nsew", padx="5px", pady="5px")

        nav_button_status = tk.Button(self.navbar_frame, text="Status", font=const.FONT_STATS, bg=const.BACKGROUND_COLOR, fg=const.ACCENT_COLOR, command= lambda: self.controller.set_page(self.controller.status_page.curent_status_frame) )
        nav_button_status.grid(row=0, column=2, columnspan=2, sticky="nsew", padx="5px", pady="5px")

        nav_button_update_state = tk.Button(self.navbar_frame, text="Update State", font=const.FONT_STATS, bg=const.BACKGROUND_COLOR, fg=const.ACCENT_COLOR, command= lambda: self.controller.set_page(self.controller.update_page.update_status_frame) )
        nav_button_update_state.grid(row=0, column=4, columnspan=2, sticky="nsew", padx="5px", pady="5px")
