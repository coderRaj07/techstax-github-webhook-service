from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from datetime import datetime, timezone
from dotenv import load_dotenv
import os

load_dotenv()


app = Flask(__name__)

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
print("Mongo URI:", MONGO_URI)

client = MongoClient(MONGO_URI)
db = client.github_events
collection = db.events

def utc_now():
    return datetime.now(timezone.utc).strftime("%d %B %Y - %I:%M %p UTC")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/webhook", methods=["POST"])
def github_webhook():
    event = request.headers.get("X-GitHub-Event")
    payload = request.json

    if event == "push":
        doc = {
            "request_id": payload["after"],
            "author": payload["pusher"]["name"],
            "action": "PUSH",
            "from_branch": None,
            "to_branch": payload["ref"].split("/")[-1],
            "timestamp": utc_now()
        }

    elif event == "pull_request":
        pr = payload["pull_request"]
        action_type = payload["action"]

        action = "MERGE" if action_type == "closed" and pr["merged"] else "PULL_REQUEST"

        doc = {
            "request_id": str(pr["id"]),
            "author": pr["user"]["login"],
            "action": action,
            "from_branch": pr["head"]["ref"],
            "to_branch": pr["base"]["ref"],
            "timestamp": utc_now()
        }

    else:
        return jsonify({"message": "Event ignored"}), 200

    collection.insert_one(doc)
    return jsonify({"status": "stored"}), 201

@app.route("/events", methods=["GET"])
def get_events():
    data = list(collection.find({}, {"_id": 0}).sort("timestamp", -1).limit(20))
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
