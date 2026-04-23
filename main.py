"""This file is for the frontend tkinter aplication where the root lives
and all of the windows and frames asosiated with it. This file takes sorted
data from the superbase database and diplays it to the user."""

import tkinter as tk
import  helper_functions as hf
import constants as const


class CommandApp:
    def __init__(self, parent):
        self.tabs = []
        self.maindashboard = None

        # region Navbar Elements
        self.navbar_frame = hf.config_frame(parent, 6, 1, True, 0, 0, True )

        confirmation_button = tk.Button(parent, text="Confirm", font=const.FONT_STATS, bg=const.BACKGROUND_COLOR, fg=const.FOREGROUND_COLOR, command=func)
        confirmation_button.grid(row=2, column=0, columnspan=4, sticky="nsew")

        # endregion

        # Dashbord Element
        self.dashbord_frame = hf.config_frame(parent, 6, 6, True, 0, 1, True )

        # System status Elements
        self.system_status_frame = hf.config_frame(parent, 6, 2, True, 0, 2, True )


if __name__ == "__main__":
    """Main."""
    root = tk.Tk()
    root.title("Main Game")
    root.withdraw()
    
    comand_app = CommandApp(hf.config_root(root)) # Configs the comand app

    root.mainloop()
