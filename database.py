import time
from supabase import create_client

url = "https://dvukxjndnkoqvjqpueqa.supabase.co"
key = "sb_publishable_MTMJMC0SHyjp0qxjPjRwcA_W-cZaxcI"
supabase = create_client(url, key)
response = supabase.table("Devices").select("*, Components(*)").execute()

def fetch_data():
    global response # I am well awear this is not right but coreners must be cut
    query = supabase.table("Devices").select("*, Components(*)").execute()
    response = query