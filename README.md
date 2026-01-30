# TechStax GitHub Webhook Service

Flask-based webhook receiver that captures GitHub events
(PUSH, PULL_REQUEST, MERGE), stores minimal data in MongoDB,
and displays activity via a polling UI.

## Run Locally
pip install -r requirements.txt
python app.py

MongoDB must be running locally or provided via MONGO_URI.
