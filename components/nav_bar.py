import tkinter as tk
import backend_functions as hf
import constants as const

class NavBar(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent) # Inheritance parent data
        self.controller = controller
        # region Navbar
        self.navbar_frame = hf.config_frame(parent, 6, 1, 1, True, 0, 0, True, const.MIDGROUND_COLOR)

        nav_button_main_dashboard = tk.Button(self.navbar_frame, text="Main Dashboard", font=const.FONT_STATS, bg=const.BACKGROUND_COLOR, fg=const.FOREGROUND_COLOR, command= lambda: self.controller.set_page(self.controller.main_page.dashbord_frame) )
        nav_button_main_dashboard.grid(row=0, column=0, columnspan=2, sticky="nsew", padx="5px", pady="5px")

        nav_button_status = tk.Button(self.navbar_frame, text="Status", font=const.FONT_STATS, bg=const.BACKGROUND_COLOR, fg=const.FOREGROUND_COLOR, command= lambda: self.controller.set_page(self.controller.status_page.curent_status_frame) )
        nav_button_status.grid(row=0, column=2, columnspan=2, sticky="nsew", padx="5px", pady="5px")

        nav_button_update_state = tk.Button(self.navbar_frame, text="Update State", font=const.FONT_STATS, bg=const.BACKGROUND_COLOR, fg=const.FOREGROUND_COLOR, command= lambda: self.controller.set_page(self.controller.update_page.update_status_frame) )
        nav_button_update_state.grid(row=0, column=4, columnspan=2, sticky="nsew", padx="5px", pady="5px")
        # endregion
