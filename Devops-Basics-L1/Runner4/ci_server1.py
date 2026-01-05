
#  python ci_server.py

from flask import Flask, jsonify

app = Flask(__name__)

job_queue = [
    {"id": 1, "task": "echo Hello from CI"},
    {"id": 2, "task": "echo Build completed"}
]

@app.route("/api/jobs/pull", methods=["GET"])
def pull_job():
    if job_queue:
        return jsonify(job_queue.pop(0))
    return jsonify({}), 204   # No job

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
