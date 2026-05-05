import tkinter as tk
import backend_functions as hf
import constants as const


class ShowPopUp(tk.Frame):
    def __init__(self, parent_root, controller, device):
        super().__init__(parent_root) # Inheritance parent data
        self.pop_up_label = hf.create_label(parent=parent_root, message="All data", pos_x=0, pos_y=0, bg_color=const.ACCENT_COLOR)
        self.controller = controller
        self.lables = []
        self.frame_data = [parent_root, const.MIDGROUND_COLOR, 2, 0]
        for component in (device['Components']):
            self.lables.append((
            ("label", [f"{component["name"]} : {component["value"]}"], [const.MIDGROUND_COLOR]),
            ))
        self.led_data, self.list_of_var = hf.map_elements(self.frame_data, self.lables)
        
