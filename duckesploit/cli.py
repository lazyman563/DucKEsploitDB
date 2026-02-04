import argparse
from .core.db import sync_and_connect

BANNER = "--- DUCKESPLOIT CLI ---"

def main():
    print(BANNER)
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--search", help="Search term")
    args = parser.parse_args()

    if args.search:
        conn = sync_and_connect()
        if conn:
            cursor = conn.cursor()
            query = "SELECT id, platform, description FROM exploits WHERE description LIKE ?"
            cursor.execute(query, (f'%{args.search}%',))
            results = cursor.fetchall()
            
            for r in results:
                print(f"ID: {r[0]} | {r[1]} | {r[2]}")
            conn.close()

if __name__ == "__main__":
    main()
