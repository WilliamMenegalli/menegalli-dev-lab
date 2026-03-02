import sqlite3
from datetime import datetime

#Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('baby_tracker.db')
c= conn.cursor()

#Create tables if they don't exist
c.execute('''
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT NOT NULL,
    timestamp DATETIME NOT NULL
);
''')
conn
from datetime import datetime

#Contadores

diapers_wet = 0
diapers_dirty = 0
diapers_mixed = 0
feedings = 0
naps = 0

events = [] #each item will be a dictionary with type and date

while True:
    print("\n=== Baby Tracker ===")
    print("1 - Add diaper")
    print("2 - Add feeding")
    print("3 - Add nap")
    print("4 - Show summary")
    print("5 - Exit")

    choice = input("Choose an option: ")
    if choice == "1":
        print("Choose diaper type:")
        print("a - Wet")
        print("b - Dirty")
        print("c - Mixed")
        dtype = input("Type: ")
        timestamp = datetime.now()

        if dtype == "a":
            diapers_wet += 1
            timestamp = datetime.now()
            c.execute("INSERT INTO events (type, timestamp) VALUES (?, ?)", ("diaper_wet", timestamp))
            conn.commit()
            events.append({"type": "diaper_wet", "time": timestamp})
            print(f"Wet diaper added at {timestamp.strftime('%H:%M')}")
        elif dtype == "b":
            diapers_dirty += 1
            timestamp = datetime.now()
            c.execute("INSERT INTO events (type, timestamp) VALUES (?, ?)", ("diapers_dirty", timestamp))
            conn.commit()
            events.append({"type": "diapers_dirty", "time": timestamp})
            print(f"Dirty diaper added at {timestamp.strftime('%H:%M')}")
        elif dtype == "c":
            diapers_mixed += 1
            timestamp = datetime.now()
            c.execute("INSERT INTO events (type, timestamp) VALUES (?, ?)", ("diapers_mixed", timestamp))
            conn.commit()
            events.append({"type": "diapers_mixed", "time": timestamp})
            print(f"Mixed diaper added at {timestamp.strftime('%H:%M')}")
        else:
            print("Invalid diaper type.")

    elif choice == "2":
        feedings += 1
        timestamp = datetime.now()
        events.append({"type": "feeding", "time": timestamp})
        print(f"Feeding added at {timestamp.strftime('%H:%M')}")

    elif choice == "3":
        naps += 1
        timestamp = datetime.now()
        events.append({"type": "naps", "time": timestamp})
        print(f"Nap added at {timestamp.strftime('%H:%M')}")

    elif choice == "4":
        today = datetime.now().date()
        today_events = [e for e in events if e["time"].date() == today]
        print("\n--- Today's Summary ---")
        print(f"Diapers - Wet:{diapers_wet}, Dirty: {diapers_dirty}, Mixed: {diapers_mixed}")
        print(f"Feedings:{feedings}")
        print(f"Naps: {naps}")
        print("\nEvent Log:")
        for e in today_events:
            print(f"{e['time'].strftime('%H:%M')} - {e['type']}")

    elif choice == "5":
        print("Exiting Baby Tracker...")
        break

    else:
        print("Invalid option. Try again.")
