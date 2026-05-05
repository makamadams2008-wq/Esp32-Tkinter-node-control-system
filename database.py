"""
Connects the Supabase database to the code for exchangment
of data. The database holds the data of 5 devices with a
range of devices in two tables "Devices" and "Components"
"""


from supabase import create_client # Imports the exsternal libary

url = "https://dvukxjndnkoqvjqpueqa.supabase.co" # Location of database
key = "sb_publishable_MTMJMC0SHyjp0qxjPjRwcA_W-cZaxcI" # Key of database

supabase = create_client(url, key) # Initiates the database

response = supabase.table("Devices").select("*, Components(*)").execute() # Forms inital data

def fetch_data():
    """ 
    This function is responsable for keeping all the
    dat up to date so when I update a value somwhere it
    updates everwhere. Anywhere this fucntion is called
    the database responce is being quaried.
    """
    global response # Not amazing but couldent find anything better please chanage
    query = supabase.table("Devices").select("*, Components(*)").execute()
    response = query
