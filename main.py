"""This file is for the frontend tkinter aplication where the root lives
and all of the windows and frames asosiated with it. This file takes sorted
data from the superbase database and diplays it to the user."""

import tkinter as tk
import backend_functions as hf
import constants as const
import database
from components import nav_bar, main_page, status_page, update_page, footer


class CommandApp:
    def __init__(self, parent):
        # creating child objects
        self.parent = parent
        self.nav_bar = nav_bar.NavBar(parent, self)
        self.main_page = main_page.MainPage(parent, self)
        self.status_page = status_page.StatusPage(parent, self)
        self.update_page = update_page.UpdatePage(parent, self)
        self.footer = footer.Footer(parent, self)

        self.tabs = [
            self.main_page, self.status_page, self.update_page
        ]

        self.maindashboard = None
        self.set_page(self.main_page.dashbord_frame) # Sets page to main page on start


    def set_page(self, current_page: tk.Frame):
        current_page.tkraise()

    def sync_all_pages(self):
        for page in self.tabs:
            page.sync() # polymorhirisum at its finest coming in clutch
        


if __name__ == "__main__":
    """Main."""
    root = tk.Tk()
    root.title("Main Game")
    root.withdraw()
    
    comand_app = CommandApp(hf.config_root(root)) # Configs the comand app
    root.mainloop()
    