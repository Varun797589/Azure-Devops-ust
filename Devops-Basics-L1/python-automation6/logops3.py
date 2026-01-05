import os

LOG_FILE = "app.log"

print("Scanning logs for ERROR...")

if not os.path.exists(LOG_FILE):
    print(f"Log file '{LOG_FILE}' not found. Creating an empty log file.")
    with open(LOG_FILE, "w") as f:
        pass

with open(LOG_FILE, "r") as f:
    for line in f:
        if "ERROR" in line:
            print(line.strip())

print("Log scan complete.")

