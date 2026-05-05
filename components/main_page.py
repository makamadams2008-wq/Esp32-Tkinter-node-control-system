import tkinter as tk
import backend_functions as hf
import constants as const
import database

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent) # Inheritance parent data
        self.controller = controller
        # region Main dashboard page
        self.dashbord_frame = hf.config_frame(parent, 1, 4, 1, True, 1, 0, True, const.MIDGROUND_COLOR)
        self.sync()

    def sync (self):
        for widget in self.dashbord_frame.winfo_children():
            widget.destroy()

        self.dashboard_label = hf.create_label(parent=self.dashbord_frame, message="All devices", pos_x=0, pos_y=0, bg_color=const.MIDGROUND_COLOR)

        self.dashboard_device_frame_data = [self.dashbord_frame, const.MIDGROUND_COLOR, 2, 0]
        self.dashboard_device_genral_data = [(
            ("label", [device['name']], [const.BACKGROUND_COLOR]),
            ("button", [device['state'], lambda d = device: self.toggle_conectivity(d)], [const.MIDGROUND_COLOR]),
        ) for device in database.response.data] # Data is stored with a type and info

        self.display_devices = hf.map_elements(self.dashboard_device_frame_data, self.dashboard_device_genral_data)

    
    def toggle_conectivity(self, current_device):
        if current_device['state'] == "Connected":
            database.supabase.table("Devices").update({'state': "Disconnected"}).match({"id": current_device["id"]}).execute()
        else:
            database.supabase.table("Devices").update({'state': "Connected"}).match({"id": current_device["id"]}).execute()

        database.fetch_data()
        self.sync()