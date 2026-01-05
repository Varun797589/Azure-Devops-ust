
#  python runner2.py


import time
import requests
import os

CI_SERVER = "http://127.0.0.1:8080"

while True:
    print("Runner polling for job...")

    r = requests.get(f"{CI_SERVER}/api/jobs/pull")

    if r.status_code == 200:
        job = r.json()
        print(f"Job received: {job['id']}")

        # Execute job
        os.system(job["task"])

    else:
        print("No job available")

    time.sleep(5)
