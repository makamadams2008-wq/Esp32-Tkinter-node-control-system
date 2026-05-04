import tkinter as tk
import backend_functions as hf
import constants as const
import ghost_device_data
from components.update_status_pop_up import UpdatePopUp

class UpdatePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent) # Inheritance parent data
        self.controller = controller
        self.parent = parent
        # region Update status page
        self.update_status_frame = hf.config_frame(parent, 1, 4, 1, True, 1, 0, True, const.MIDGROUND_COLOR)
        self.update_status_frame_data = [self.update_status_frame, const.MIDGROUND_COLOR, 2, 0]
        self.update_device_data = [(
            ("label", [element['device_name']], [const.BACKGROUND_COLOR]),
            ("button", ["Update Sensor", lambda e = element: self.show_sensor_dashboard(e)], [const.MIDGROUND_COLOR])
        ) for element in ghost_device_data.devices] # Data is stored with a type and info
        self.display_device_data = hf.map_elements(self.update_status_frame_data, self.update_device_data)
        # endregion

    # functions
    def show_sensor_dashboard(self, current_device):
        print(f"This should show the dashboard for sesnor id: {current_device["device_id"]}")
        self.pop_up = UpdatePopUp(hf.config_root(self.parent), self, current_device)
        pass
