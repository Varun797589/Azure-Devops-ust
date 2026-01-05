
import os
import time

FOLDER = "./test_files"
DAYS = 1

os.makedirs(FOLDER, exist_ok=True)

now = time.time()
cutoff = now - DAYS * 86400

print("Scanning files...")
for file in os.listdir(FOLDER):
    path = os.path.join(FOLDER, file)
    if os.path.isfile(path):
        if os.stat(path).st_mtime < cutoff:
            print(f"Old file found: {file}")
