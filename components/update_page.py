"""THis file is responsable for rendering and managing the state
updating page on the UI. This page speciphicly focuses on providing
a conection bettwen the user and the nestesed layer of the database
where it starts to get into more particuler components.
"""

import tkinter as tk
import backend_functions as hf
import constants as const
import database
from components.pop_ups.update_status_pop_up import UpdatePopUp

class UpdatePage(tk.Frame):
    """
    This is the bluprint that holds the main canvas and a helpfull lable.
    The canvas is what holds the futher elements for each deives but by having
    the canvas a fixed size is insured.
    """
    def __init__(self, parent, controller):
        """
        Initalises the label and the canvas with the adaptive
        elemets so the user can iteract with them
        """
        super().__init__(parent) # Inheritance parent data
        self.controller = controller
        self.parent = parent

        self.update_status_frame = hf.config_frame(parent, 1, 4, 1, True, 1, 0, True, const.MIDGROUND_COLOR) # Main frame
        self.sync()

    def sync(self):
        """
        This function is resposable for keeping the invidual elements
        of the page all up to date by givving one call to update
        everything wutout having to utalise configure witch is highly
        bloated.
        """
        for widget in self.update_status_frame.winfo_children(): # Destroys old widgets
            widget.destroy()

        self.connected_devices = []

        for device in database.response.data:
            if device['state'] == "Connected":
                self.connected_devices.append(device)

        # Creating new widgets to replace the old ones
        self.dashboard_label = hf.create_label(parent=self.update_status_frame, message="All devices", pos_x=0, pos_y=0, bg_color=const.MIDGROUND_COLOR)
        self.update_status_frame_data = [self.update_status_frame, const.MIDGROUND_COLOR, 2, 0]
        self.update_device_data = [(
            ("label", [device['name']], [const.BACKGROUND_COLOR]),
            ("button", ["Update Sensor", lambda d = device: self.show_sensor_dashboard(d)], [const.MIDGROUND_COLOR])
        ) for device in self.connected_devices] # Data is stored with a type and info
        self.display_device_data = hf.map_elements(self.update_status_frame_data, self.update_device_data)


    # functions
    def show_sensor_dashboard(self, current_device):
        """
        This function is responsable for creating the sensor dashboard
        with all fo the truly interactive elements.
        """
        new_window = hf.config_root(self.parent) 
        self.pop_up = UpdatePopUp(new_window, self, current_device["id"])
