import tkinter as tk
import backend_functions as hf
import constants as const
import database
from tkinter import messagebox

class UpdatePopUp(tk.Frame):
    
    def __init__(self, parent_root, controller, device_id):
        super().__init__(parent_root) # Inheritance parent data
        self.controller = controller
        self.parent_root = parent_root

        # Grabs new data
        database.fetch_data()
        for device in database.response.data:
            if device['state'] == "Connected" and device["id"] == device_id:
                self.device = device
        
        self.outputs_label = hf.create_label(parent=parent_root, message="Outputs", pos_x=0, pos_y=0, bg_color=const.BACKGROUND_COLOR)

        
        self.led_frame = hf.config_frame(parent_root, 1, 2, 1, True, 1, 0, True, const.MIDGROUND_COLOR)
        self.leds_label = hf.create_label(parent=self.led_frame, message="Leds", pos_x=0, pos_y=1, bg_color=const.MIDGROUND_COLOR)
        
        self.leds = []
        self.update_led_frame_data = [self.led_frame, const.MIDGROUND_COLOR, 2, 0]
        self.update_led_data = []

        for element in self.device['Components']:
            if element["type"] == "LED": self.leds.append(element)

        for index, component in enumerate(self.leds):
            print(f"Front end: {component['value']}")
            self.update_led_data.append((
            ("label", [f"{component["name"]}"], [const.MIDGROUND_COLOR]),
            ("radio", ["Toggle light", ["On", "Off"], component["value"], lambda c = component["name"], i = index: self.on_led_update(c, i)], [const.BACKGROUND_COLOR])
            ))
        self.led_data, self.list_of_var = hf.map_elements(self.update_led_frame_data, self.update_led_data)
       
        self.motor_label = hf.create_label(parent=parent_root, message="Motor", pos_x=0, pos_y=3, bg_color=const.MIDGROUND_COLOR)
        self.set_motor_direction_input = hf.create_entry(parent=parent_root, message="Please pick a motor direction in digrees", func=self.on_motor_update, pos_x=0, pos_y=4, bg_color=const.MIDGROUND_COLOR)

        self.name_confirmation_button = tk.Button(parent_root, text="-- Exit --", bg=const.BACKGROUND_COLOR, fg=const.ACCENT_COLOR, command=self.exit_window, font=const.FONT_STATS)
        self.name_confirmation_button.grid(row=5, column=0, sticky="nsew")

    def on_motor_update(self):
        database.fetch_data()
        print(self.set_motor_direction_input.get())
        try:
            input_value  = float(self.set_motor_direction_input.get())
            if input_value < 0 or  input_value > 360:
                messagebox.showerror("Invalid Input", f"Please insure your value is bettwen 0 and 360!")
            else:
                database.supabase.table("Components").update({"value": str(self.set_motor_direction_input.get())}).match({"name": "Main Motor", "device_id": self.device["id"]}).execute()
        except:
            messagebox.showerror("Invalid Input", f"Please insure your value is a number with no units!")
    
    def on_led_update(self, led, index):
        database.fetch_data()
        print(led, index)
        database.supabase.table("Components").update({"value": self.list_of_var[index].get()}).match({"name": led, "device_id": self.device["id"]}).execute()
    
    def exit_window(self):
       self.parent_root.destroy()