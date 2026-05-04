import time
from supabase import create_client

url = "https://dvukxjndnkoqvjqpueqa.supabase.co"
key = "sb_publishable_MTMJMC0SHyjp0qxjPjRwcA_W-cZaxcI"
supabase = create_client(url, key)
response = supabase.table("Devices").select("*, Components(*)").execute()
for i  in range(len(response.data)):
    for j in range(len(response.data[i]['Components'])):
        # Notice the [0] added here:
        print(f"Device {i+1}: {response.data[i]['Components'][j]['name']} : {response.data[i]['Components'][j]['value']}")
        time.sleep(0.1)