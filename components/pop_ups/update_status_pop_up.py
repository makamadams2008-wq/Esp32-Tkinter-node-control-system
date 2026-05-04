import tkinter as tk
import backend_functions as hf
import constants as const

class UpdatePopUp(tk.Frame):
    def __init__(self, parent_root, controller, device):
        super().__init__(parent_root) # Inheritance parent data
        self.controller = controller
        print(device["device_name"])

        self.outputs_label = hf.create_label(parent=parent_root, message="Outputs", pos_x=0, pos_y=0, bg_color=const.BACKGROUND_COLOR)

        
        self.led_frame = hf.config_frame(parent_root, 1, 2, 1, True, 1, 0, True, const.MIDGROUND_COLOR)
        self.leds_label = hf.create_label(parent=self.led_frame, message="Leds", pos_x=0, pos_y=1, bg_color=const.MIDGROUND_COLOR)
        
        self.update_led_frame_data = [self.led_frame, const.MIDGROUND_COLOR, 2, 0]
        self.update_led_data = [(
            ("label", [f"{led_id}"], [const.MIDGROUND_COLOR]),
            ("radio", ["Toggle light",["On", "Off"],value, self.on_led_update], [const.BACKGROUND_COLOR])
            
        ) for led_id, value in device["components"]["outputs"]["leds_status"].items()] # Data is stored with a type and info
        self.led_data, self.list_of_var = hf.map_elements(self.update_led_frame_data, self.update_led_data)
       
        self.motor_label = hf.create_label(parent=parent_root, message="Motor", pos_x=0, pos_y=3, bg_color=const.MIDGROUND_COLOR)
        self.set_motor_direction_input = hf.create_entry(parent=parent_root, message="Please pick a motor direction in digrees", func=self.on_motor_update, pos_x=0, pos_y=4, bg_color=const.MIDGROUND_COLOR)

    def on_motor_update(self):
        print(self.set_motor_direction_input.get())
        pass
    
    def on_led_update(self):
        print(self.list_of_var[0].get())
        pass
