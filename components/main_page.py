"""
This file is responsable for managing the main page. The main page
holds all of the deives, for this version you can simplay togle on
and off devices with buttons witch is this fiels core functonality.
"""

import tkinter as tk
import backend_functions as hf
import constants as const
import database


class MainPage(tk.Frame):
    """
    The mainpage has dynamicly created elements using the map
    function, these elemets are dpendant on the quity of devices
    avalable in the database. The core of the mainpage is a canvas
    with a scroll bar that has small frames isnide of it.
    """
    def __init__(self, parent, controller):
        """Initates the varables and elements requred for the adptive layout."""
        super().__init__(parent) # Inheritance parent data
        self.controller = controller
        # Region Main dashboard page
        self.dashbord_frame = hf.config_frame(parent, 1, 4, 1, True, 1, 0, True, const.MIDGROUND_COLOR)
        self.sync()

    def sync (self):
        """
        This function is resposable for keeping the invidual elements
        of the page all up to date by givving one call to update
        everything wutout having to utalise configure witch is highly
        bloated.
        """

        # Destroys any old widgests that could be precent
        for widget in self.dashbord_frame.winfo_children():
            widget.destroy()

        # Creates the new elemets to replace the old widgets with new data
        self.dashboard_label = hf.create_label(parent=self.dashbord_frame, message="All devices", pos_x=0, pos_y=0, bg_color=const.MIDGROUND_COLOR)

        self.dashboard_device_frame_data = [self.dashbord_frame, const.MIDGROUND_COLOR, 2, 0]
        self.dashboard_device_genral_data = [(
            ("label", [device['name']], [const.BACKGROUND_COLOR]),
            ("button", [device['state'], lambda d = device: self.toggle_conectivity(d)], [const.MIDGROUND_COLOR]),
        ) for device in database.response.data] # Data is stored with a type and info

        self.display_devices = hf.map_elements(self.dashboard_device_frame_data, self.dashboard_device_genral_data)

    
    def toggle_conectivity(self, current_device):
        """Calls the sync_all_pages method from the parent class and togles the conection state to adapt the rest of the UI as it oly shows connected devices."""

        # Flips conection state
        if current_device['state'] == "Connected":
            database.supabase.table("Devices").update({'state': "Disconnected"}).match({"id": current_device["id"]}).execute()
        else:
            database.supabase.table("Devices").update({'state': "Connected"}).match({"id": current_device["id"]}).execute()

        database.fetch_data()
        self.controller.sync_all_pages() # Updates the rest of the Ui to reflect changes
