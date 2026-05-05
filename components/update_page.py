import tkinter as tk
import backend_functions as hf
import constants as const
import database
from components.pop_ups.update_status_pop_up import UpdatePopUp

class UpdatePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent) # Inheritance parent data
        self.controller = controller
        self.parent = parent
        # region Update status page

        self.update_status_frame = hf.config_frame(parent, 1, 4, 1, True, 1, 0, True, const.MIDGROUND_COLOR)
        self.sync()

    def sync(self):
        for widget in self.update_status_frame.winfo_children():
            widget.destroy()

        self.connected_devices = []

        for device in database.response.data:
            if device['state'] == "Connected":
                self.connected_devices.append(device)

        self.dashboard_label = hf.create_label(parent=self.update_status_frame, message="All devices", pos_x=0, pos_y=0, bg_color=const.MIDGROUND_COLOR)
        self.update_status_frame_data = [self.update_status_frame, const.MIDGROUND_COLOR, 2, 0]
        self.update_device_data = [(
            ("label", [device['name']], [const.BACKGROUND_COLOR]),
            ("button", ["Update Sensor", lambda d = device: self.show_sensor_dashboard(d)], [const.MIDGROUND_COLOR])
        ) for device in self.connected_devices] # Data is stored with a type and info
        self.display_device_data = hf.map_elements(self.update_status_frame_data, self.update_device_data)
        # endregion

    # functions
    def show_sensor_dashboard(self, current_device):
        self.pop_up = UpdatePopUp(hf.config_root(self.parent), self, current_device["id"])
