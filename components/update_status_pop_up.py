import tkinter as tk
import backend_functions as hf
import constants as const
import ghost_device_data

class UpdatePopUp(tk.Frame):
    def __init__(self, parent_root, controller, device):
        super().__init__(parent_root) # Inheritance parent data
        self.controller = controller
        print(device["device_name"])

        self.outputs_label = hf.create_label(parent=parent_root, message="Outputs", pos_x=0, pos_y=0, bg_color=const.BACKGROUND_COLOR)

        
        self.led_frame = hf.config_frame(parent_root, 1, 2, True, 1, 0, True, const.MIDGROUND_COLOR)
        self.leds_label = hf.create_label(parent=self.led_frame, message="Leds", pos_x=0, pos_y=1, bg_color=const.MIDGROUND_COLOR)
        
        self.motor_frame = hf.config_frame(parent_root, 1, 2, True, 2, 0, True, const.MIDGROUND_COLOR)
        self.motor_label = hf.create_label(parent=self.motor_frame, message="Motor", pos_x=0, pos_y=0, bg_color=const.MIDGROUND_COLOR)
        self.set_motor_direction_input = hf.create_entry(parent=self.motor_frame, message="Please pick a motor direction in digrees", func=self.on_update, pos_x=0, pos_y=1, bg_color=const.MIDGROUND_COLOR)

    def on_update(self):
        print(self.set_motor_direction_input.get())
        pass
        
