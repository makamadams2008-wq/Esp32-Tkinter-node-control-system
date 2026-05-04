import tkinter as tk
import backend_functions as hf
import constants as const
import ghost_device_data

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent) # Inheritance parent data
        self.controller = controller
        # region Main dashboard page
        self.dashbord_frame = hf.config_frame(parent, 1, 4, 1, True, 1, 0, True, const.MIDGROUND_COLOR)
        self.dashboard_label = hf.create_label(parent=self.dashbord_frame, message="All devices", pos_x=0, pos_y=0, bg_color=const.MIDGROUND_COLOR)

        self.dashboard_device_frame_data = [self.dashbord_frame, const.MIDGROUND_COLOR, 2, 0]
        self.dashboard_device_genral_data = [(
            ("label", [element['device_name']], [const.BACKGROUND_COLOR]),
            ("label",[f"Status: Conected"], [const.MIDGROUND_COLOR]),
        ) for element in ghost_device_data.devices] # Data is stored with a type and info
        self.display_devices = hf.map_elements(self.dashboard_device_frame_data, self.dashboard_device_genral_data)
        # endregion
