import os
import urllib.request
import sqlite3

# Apontando para o seu repositório de DADOS que terá o Actions
DB_URL = "https://raw.githubusercontent.com/MurilooPrDev/DucKEsploitDB/main/data/duck_base.db"
LOCAL_PATH = os.path.expanduser("~/.duckesploit/duck_base.db")

def sync_and_connect():
    os.makedirs(os.path.dirname(LOCAL_PATH), exist_ok=True)
    
    try:
        # Check remote size (HEAD request)
        req = urllib.request.Request(DB_URL, method='HEAD', headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            remote_size = int(response.headers.get('Content-Length', 0))

        # Sync if size differs or doesn't exist
        if not os.path.exists(LOCAL_PATH) or os.path.getsize(LOCAL_PATH) != remote_size:
            print("[*] Synchronizing sacred database with DucKEsploitDB...")
            urllib.request.urlretrieve(DB_URL, LOCAL_PATH)
            print("[V] Sync complete.")
        
    except Exception as e:
        if os.path.exists(LOCAL_PATH):
            print(f"[!] Offline or Sync failed. Using cached arsenal.")
        else:
            print(f"[X] Critical: Could not fetch database from GitHub. {e}")
            return None

    return sqlite3.connect(LOCAL_PATH)
