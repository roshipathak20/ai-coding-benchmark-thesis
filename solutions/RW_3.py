# Task: Flask status API
# Create a small Flask application
# with endpoint "/status"
#
# The endpoint should return JSON:
# {"status":"ok"}
#
# Example:
# GET /status
# Response -> {"status":"ok"}

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/status", methods=["GET"])
def get_status():
    return jsonify({"status": "ok"})