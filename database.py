from supabase import create_client

url = "https://dvukxjndnkoqvjqpueqa.supabase.co"
key = "sb_publishable_MTMJMC0SHyjp0qxjPjRwcA_W-cZaxcI"
supabase = create_client(url, key)
response = supabase.table("Devices").select("*, Components(*)").execute()
print(response)