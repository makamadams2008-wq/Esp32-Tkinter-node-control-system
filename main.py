"""This file is for the frontend tkinter aplication where the root lives
and all of the windows and frames asosiated with it. This file takes sorted
data from the superbase database and diplays it to the user."""

# Device name, Device ID, Componets
ghost_devices = [
    {"device_id": 1,"device_name": "device A", "components": ["Light", "Sound", "Vibration"]},
    {"device_id": 2,"device_name": "device B", "components": ["Sigma", "Beta", "Alpha"]},
    {"device_id": 3,"device_name": "device C", "components": ["Noob", "Pro", "Hacker"]},
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

        nav_button_main_dashboard = tk.Button(self.navbar_frame, text="Main Dashboard", font=const.FONT_STATS, bg=const.BACKGROUND_COLOR, fg=const.FOREGROUND_COLOR, command= lambda: self.set_page(self.dashbord_frame) )
        nav_button_main_dashboard.grid(row=0, column=0, columnspan=2, sticky="nsew", padx="5px", pady="5px")

        nav_button_status = tk.Button(self.navbar_frame, text="Status", font=const.FONT_STATS, bg=const.BACKGROUND_COLOR, fg=const.FOREGROUND_COLOR, command= lambda: self.set_page(self.curent_status_frame) )
        nav_button_status.grid(row=0, column=2, columnspan=2, sticky="nsew", padx="5px", pady="5px")

        nav_button_update_state = tk.Button(self.navbar_frame, text="Update State", font=const.FONT_STATS, bg=const.BACKGROUND_COLOR, fg=const.FOREGROUND_COLOR, command= lambda: self.set_page(self.update_status_frame) )
        nav_button_update_state.grid(row=0, column=4, columnspan=2, sticky="nsew", padx="5px", pady="5px")
        # endregion

        # region Main dashboard page
        self.dashbord_frame = hf.config_frame(parent, 1, 4, True, 1, 0, True, const.MIDGROUND_COLOR)
        self.dashboard_label = hf.create_label(parent=self.dashbord_frame, message="Main Dashboard", pos_x=0, pos_y=0, bg_color=const.MIDGROUND_COLOR)
        
        self.conencted_devices_frame_data = [self.dashbord_frame, const.MIDGROUND_COLOR, 2, 0]
        self.conencted_devices_label_data = [(
            ("label", element['device_name'], [const.BACKGROUND_COLOR]),
            ("label",f" Device ID: {element['device_id']}", [const.MIDGROUND_COLOR]),
            ("label",f" Components: {', '.join(element['components'])}", [const.MIDGROUND_COLOR]),
        ) for element in ghost_devices] # Data is stored with a type and info

        self.connected_devices = hf.map_elements(self.conencted_devices_frame_data, self.conencted_devices_label_data)
        # endregion

        # region Current status page
        self.curent_status_frame = hf.config_frame(parent, 1, 4, True, 1, 0, True, const.MIDGROUND_COLOR)
        # endregion

        # region Update status page
        self.update_status_frame = hf.config_frame(parent, 1, 4, True, 1, 0, True, const.MIDGROUND_COLOR)
        # endregion

        # region Overall status Footer
        self.system_status_frame = hf.config_frame(parent, 1, 4, True, 2, 0, True, const.MIDGROUND_COLOR)
        self.status_label = hf.create_label(parent=self.system_status_frame, message="Status: Stable connection", pos_x=0, pos_y=2, bg_color=const.BACKGROUND_COLOR)
        # endregion

        self.pages = [self.update_status_frame, self.curent_status_frame, self.dashbord_frame]
        self.set_page(self.dashbord_frame) # Sets page to main page on start
    # region Methods
    def set_page(self, current_page):
        for page in self.pages:
            if page == current_page:
                page.tkraise()
    # endregion

            

if __name__ == "__main__":
    """Main."""
    root = tk.Tk()
    root.title("Main Game")
    root.withdraw()
    
    comand_app = CommandApp(hf.config_root(root)) # Configs the comand app
    root.mainloop()
    
