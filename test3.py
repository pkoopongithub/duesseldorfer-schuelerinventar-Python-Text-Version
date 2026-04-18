import requests

API_BASE_URL = "https://paul-koop.org/api/"

print("1. Login testen...")
resp = requests.post(API_BASE_URL + "api_login.php", 
                     json={"username": "gast", "password": "gast"})
print(f"Status: {resp.status_code}")
data = resp.json()
print(f"Antwort: {data}")

if data.get('userID'):
    user_id = data['userID']
    session = data['session']
    print(f"\n2. Profile abrufen mit userID={user_id}")
    
    headers = {'X-User-ID': str(user_id), 'X-Session': session}
    resp2 = requests.get(API_BASE_URL + "api_profiles.php", headers=headers)
    print(f"Status: {resp2.status_code}")
    profiles = resp2.json()
    print(f"Anzahl Profile: {len(profiles) if isinstance(profiles, list) else 'Fehler'}")
    print(f"Erstes Profil: {profiles[0] if profiles else 'keine'}")
else:
    print("Login fehlgeschlagen!")
