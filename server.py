from flask import Flask, jsonify
from jobs import get_jobs

app = Flask(__name__)

@app.route("/")
def home():
    return "HireX API is live!"

@app.route("/jobs")
def jobs():
    jobs_list = get_jobs()  # Fetch all jobs
    return jsonify(jobs_list)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
