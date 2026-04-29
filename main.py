"""This file is for the frontend tkinter aplication where the root lives
and all of the windows and frames asosiated with it. This file takes sorted
data from the superbase database and diplays it to the user."""

# Device name, Device ID, Componets
ghost_devices = [
    {"device_id": 1,"device_name": "device A", "components": ["Light", "Sound", "Vibration"]},
    {"device_id": 2,"device_name": "device B", "components": ["Sigma", "Beta", "Alpha"]},
    {"device_id": 3,"device_name": "device C", "components": ["Noob", "Pro", "Hacker"]},
]

import tkinter as tk
import  backend_functions as hf
import constants as const


class CommandApp:
    def __init__(self, parent):
        self.tabs = []
        self.maindashboard = None

        # region Navbar
        self.navbar_frame = hf.config_frame(parent, 6, 1, True, 0, 0, True, const.MIDGROUND_COLOR)

        nav_button_main_dashboard = tk.Button(self.navbar_frame, text="Main Dashboard", font=const.FONT_STATS, bg=const.BACKGROUND_COLOR, fg=const.FOREGROUND_COLOR, command= None )
        nav_button_main_dashboard.grid(row=0, column=0, columnspan=2, sticky="nsew", padx="5px", pady="5px")

        nav_button_status = tk.Button(self.navbar_frame, text="Status", font=const.FONT_STATS, bg=const.BACKGROUND_COLOR, fg=const.FOREGROUND_COLOR, command= None )
        nav_button_status.grid(row=0, column=2, columnspan=2, sticky="nsew", padx="5px", pady="5px")

        nav_button_update_state = tk.Button(self.navbar_frame, text="Update State", font=const.FONT_STATS, bg=const.BACKGROUND_COLOR, fg=const.FOREGROUND_COLOR, command= None )
        nav_button_update_state.grid(row=0, column=4, columnspan=2, sticky="nsew", padx="5px", pady="5px")

        # endregion

        # region Dashboard
        # region Dashbord Element
        self.dashbord_frame = hf.config_frame(parent, 1, 4, True, 1, 0, True, const.MIDGROUND_COLOR)
        self.dashboard_label = hf.create_label(self.dashbord_frame, 0, 0, "Main Dashboard")
        
        self.conencted_devices_frame_data = [self.dashbord_frame, const.FOREGROUND_COLOR, 2, 0]
        self.conencted_devices_label_data = [((element['device_id'], "lable", []), (element['device_name'], "label", [])) for element in ghost_devices] # Data is stored with a type and info
        print(self.conencted_devices_label_data)
        
        self.connected_devices = hf.map_elements(self.conencted_devices_frame_data, self.conencted_devices_label_data)
        # endregion
        # region System status Elements
        self.system_status_frame = hf.config_frame(parent, 1, 4, True, 2, 0, True, const.MIDGROUND_COLOR)
        self.status_label = hf.create_label(self.system_status_frame, 0, 2, "Status: Stable connection")
        # endregion
        # endregion

        # region Status Page


        # endregion
if __name__ == "__main__":
    """Main."""
    root = tk.Tk()
    root.title("Main Game")
    root.withdraw()
    
    comand_app = CommandApp(hf.config_root(root)) # Configs the comand app

    root.mainloop()
