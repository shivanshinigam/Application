from flask import Flask, request, jsonify
import numpy as np

application = Flask(__name__)

def calculate(numbers):
    arr = np.array(numbers)
    return {
        "mean": float(arr.mean()),
        "sum": float(arr.sum())
    }

@application.route("/", methods=["GET"])
def home():
    return "API is running"

@application.route("/calculate", methods=["POST"])
def calculate_api():
    data = request.get_json()
    numbers = data.get("numbers", [])
    return jsonify(calculate(numbers))

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5001)
