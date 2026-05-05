"""
Resposable for managing the data flow and display of the show stats pop up.
The pop up is an adaptive element that displays the current data from the database so the
user can easly understand there interaction with the sesnosrs from the UI.
"""

import tkinter as tk
import backend_functions as hf
import constants as const
import database


class ShowPopUp(tk.Frame):
    """
    Create the pop up window that displys the information for the user. The information
    is all the different sesnor inputs with a value and unit
      """

    def __init__(self, parent_root, controller, device_id):
        """
        Iinitate the required information for the user including the data name, value,
        unit and the oprppate tittle.
        """
        super().__init__(parent_root) # Inheritance parent data
        self.controller = controller # Parent
        self.parent_root = parent_root 

        database.fetch_data() # Gets new relvant data
        for device in database.response.data:
            if device['state'] == "Connected" and device["id"] == device_id:
                self.device = device

        self.pop_up_label = hf.create_label(parent=parent_root, message="All data", pos_x=0, pos_y=0, bg_color=const.ACCENT_COLOR)

        self.frame_data = [parent_root, const.MIDGROUND_COLOR, 2, 0]

        self.lables = []
        for component in (self.device['Components']):
            self.lables.append((
            ("label", [f"{component["name"]} :  {component["value"]} {component["unit"]}"], [const.MIDGROUND_COLOR]),
            ))
        
        self.led_data, self.list_of_var = hf.map_elements(self.frame_data, self.lables) # Itirates over lables 

        