"""This file is for the frontend tkinter aplication where the root lives
and all of the windows and frames asosiated with it. This file takes sorted
data from the superbase database and diplays it to the user."""

import tkinter as tk
import  helper_functions as hf
import constants as const


class ComandApp:
    def __init__(self, parent):
        self.tabs = []

        self.maindashboard = None


if __name__ == "__main__":
    """Main."""
    root = tk.Tk()
    root.title("Main Game")
    root.withdraw()
    
    comand_app = ComandApp(hf.config_root(root)) # Configs the comand app

    root.mainloop()
