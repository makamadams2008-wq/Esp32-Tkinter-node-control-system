"""
This file is repsonsable for connecting the device information with the gernal
deives dashboard by prodiving a clear path for users to travle bettwen via adaptivly
creacted buttons.
"""
import tkinter as tk
import backend_functions as hf
import constants as const
import database
from components.pop_ups.show_status_pop_up import ShowPopUp

class StatusPage(tk.Frame):
    """
    The bluerpint for the adaptive Ui element, this blurpitnt is more of a cassing
    to alow for tkinter to work as exspected than somthing that would be used more
    than once.
    """
    def __init__(self, parent, controller):
        """
        Initialsises the canvas a dn a lable that alow for the flexable
        dynamic elements to stay clear and visual. THe incluaded scroll
        bar insures the user can never have too many devices conected at
        once.
        """
        super().__init__(parent) # Inheritance parent data
        self.controller = controller
        self.parent = parent

        self.curent_status_frame = hf.config_frame(parent, 1, 4, 1, True, 1, 0, True, const.MIDGROUND_COLOR)

        self.sync()

    def sync(self):
        """
        This function is resposable for keeping the invidual elements
        of the page all up to date by givving one call to update
        everything wutout having to utalise configure witch is highly
        bloated.
        """
        for widget in self.curent_status_frame.winfo_children(): # Destroys any old widgets to allow for once with more recent data
            widget.destroy()

        self.connected_devices = []
        for device in database.response.data:
            if device['state'] == "Connected":
                self.connected_devices.append(device)

        # Creating new elements to replace the old ones
        self.dashboard_label = hf.create_label(parent=self.curent_status_frame, message="Connected devices", pos_x=0, pos_y=0, bg_color=const.MIDGROUND_COLOR)
        self.current_status_frame_data = [self.curent_status_frame, const.MIDGROUND_COLOR, 2, 0]
        self.current_status_device_data = [(
            ("label", [device['name']], [const.BACKGROUND_COLOR]),
            ("button", ["Veiw Sensor", lambda d = device: self.show_sensor_info(d)], [const.MIDGROUND_COLOR])
        ) for device in self.connected_devices] # Data is stored with a type and info
        self.display_device_data = hf.map_elements(self.current_status_frame_data, self.current_status_device_data)

    def show_sensor_info(self, current_device):
        """
        This function is responsable for creating the sensor dashboard
        that displays all fo the data for each device.
        """
        new_window = hf.config_root(self.parent) 
        self.pop_up = ShowPopUp(new_window, self, current_device["id"])