import tkinter as tk
import backend_functions as hf
import constants as const
import database
from components.pop_ups.show_status_pop_up import ShowPopUp

class StatusPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent) # Inheritance parent data
        self.controller = controller
        self.parent = parent
        # region Current status page

        self.connected_devices = []
        for device in database.response.data:
            if device['state'] == "Connected":
                self.connected_devices.append(device)

        self.curent_status_frame = hf.config_frame(parent, 1, 4, 1, True, 1, 0, True, const.MIDGROUND_COLOR)
        self.dashboard_label = hf.create_label(parent=self.curent_status_frame, message="Connected devices", pos_x=0, pos_y=0, bg_color=const.MIDGROUND_COLOR)
        self.current_status_frame_data = [self.curent_status_frame, const.MIDGROUND_COLOR, 2, 0]
        self.current_status_device_data = [(
            ("label", [device['name']], [const.BACKGROUND_COLOR]),
            ("button", ["Veiw Sensor", lambda d = device: self.show_sensor_info(d)], [const.MIDGROUND_COLOR])
        ) for device in self.connected_devices] # Data is stored with a type and info
        self.display_device_data = hf.map_elements(self.current_status_frame_data, self.current_status_device_data)
        # endregion

    def show_sensor_info(self, current_device):
        self.pop_up = ShowPopUp(hf.config_root(self.parent), self, current_device)