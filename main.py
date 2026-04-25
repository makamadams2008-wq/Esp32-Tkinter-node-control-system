"""This file is for the frontend tkinter aplication where the root lives
and all of the windows and frames asosiated with it. This file takes sorted
data from the superbase database and diplays it to the user."""
ghost_devices = ["device A","device B", "device C", "device D", "device D"]

import tkinter as tk
import  helper_functions as hf
import constants as const


class CommandApp:
    def __init__(self, parent):
        self.tabs = []
        self.maindashboard = None

        # region Navbar Elements
        self.navbar_frame = hf.config_frame(parent, 6, 1, True, 0, 0, True, const.MIDGROUND_COLOR)

        nav_button_main_dashboard = tk.Button(self.navbar_frame, text="Main Dashboard", font=const.FONT_STATS, bg=const.BACKGROUND_COLOR, fg=const.FOREGROUND_COLOR, command= None )
        nav_button_main_dashboard.grid(row=0, column=0, columnspan=2, sticky="nsew", padx="5px", pady="5px")

        nav_button_status = tk.Button(self.navbar_frame, text="Status", font=const.FONT_STATS, bg=const.BACKGROUND_COLOR, fg=const.FOREGROUND_COLOR, command= None )
        nav_button_status.grid(row=0, column=2, columnspan=2, sticky="nsew", padx="5px", pady="5px")

        nav_button_update_state = tk.Button(self.navbar_frame, text="Update State", font=const.FONT_STATS, bg=const.BACKGROUND_COLOR, fg=const.FOREGROUND_COLOR, command= None )
        nav_button_update_state.grid(row=0, column=4, columnspan=2, sticky="nsew", padx="5px", pady="5px")

        # endregion

        # region Dashbord Element
        self.dashbord_frame = hf.config_frame(parent, 1, 4, True, 1, 0, True, const.BACKGROUND_COLOR)
        nav_label = tk.Label(self.dashbord_frame, text="Main Dashboard", font=const.FONT_STATS, bg=const.MIDGROUND_COLOR, fg=const.FOREGROUND_COLOR)
        nav_label.grid(row=0, column=0, columnspan=1, sticky="nsew")
        
        self.conencted_devices_frame_data = [self.dashbord_frame, const.FOREGROUND_COLOR, 2, 0] 
        self.connected_devices = hf.map_elements(self.conencted_devices_frame_data, ghost_devices, "label")
        # endregion

        # System status Elements
        self.system_status_frame = hf.config_frame(parent, 6, 2, True, 0, 2, True, const.MIDGROUND_COLOR)
        # endregion


if __name__ == "__main__":
    """Main."""
    root = tk.Tk()
    root.title("Main Game")
    root.withdraw()
    
    comand_app = CommandApp(hf.config_root(root)) # Configs the comand app

    root.mainloop()
