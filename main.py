"""
This file is responsable for the initation of the project with all
of the important links bettwen componets. THe files first responsability
is project intiation where it runs the inital script for drawing up the 
root. From there the file reaches out to its children for futher suport
leveredging its overviewing nature for syncing.
"""

import tkinter as tk
import backend_functions as hf # hf stands for helper functions I chnaged the file name and never switched hf
from components import nav_bar, main_page, status_page, update_page, footer


class CommandApp:
    """
    This class is the parent of all other classes conecting all of the components togther
    so they can comunicate efectivly without forming spagit code with cross links and import
    loops.
    """
    def __init__(self, parent):
        """
        Initiates all of the sub components. Tabs chanage
        bettwen pages, the nav bar and the footer stay constant
        bettwen pages. The tabs work with a tkrise aprouch where
        they stack ontop of eachother.
        """
        self.parent = parent
        # creating child objects
        self.nav_bar = nav_bar.NavBar(parent, self)
        self.main_page = main_page.MainPage(parent, self)
        self.status_page = status_page.StatusPage(parent, self)
        self.update_page = update_page.UpdatePage(parent, self)
        self.footer = footer.Footer(parent, self)

        # Tabs for the sync function
        self.tabs = [
            self.main_page, self.status_page, self.update_page
        ]

        self.set_page(self.main_page.dashbord_frame) # Sets page to main page on start


    def set_page(self, current_page: tk.Frame):
        """
        This fucntion is responsable for switching bettwen
        pages where depending on the nav button sleected it will
        shift the page forwards infornt of the others hding the 
        others.
        """
        current_page.tkraise()

    def sync_all_pages(self):
        """
        This Function sycs all of the pages together for when adding
        and removing devices on the main menu. By bringing the logic up
        a level it insures that import loops and poor coding practices are
        avoided.
        """
        for page in self.tabs:
            page.sync() # polymorhirisum at its finnest coming in clutch this took me 2 hours to figgure out btw yeah realy annoying when your tierd
        


if __name__ == "__main__":
    """Main."""
    root = tk.Tk()
    root.title("Node Managment System")
    root.withdraw()
    
    comand_app = CommandApp(hf.config_root(root)) # Configs the comand app
    root.mainloop()
