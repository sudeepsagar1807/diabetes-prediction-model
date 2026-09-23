import os
import pickle
import numpy as np
from flask import Flask, request, jsonify, render_template

# Create Flask application
app = Flask(__name__)

# Get the directory where app.py is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load the trained machine learning model
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")

with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No input data received"}), 400

        # Convert input values to float
        float_features = [float(x) for x in data.values()]

        # Convert features into NumPy array
        features = np.array(float_features).reshape(1, -1)

        # Make prediction
        prediction = model.predict(features)[0]

        # Convert prediction into readable result
        result = "Diabetic" if prediction == 1 else "Non-Diabetic"

        return jsonify({
            "result": result
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)