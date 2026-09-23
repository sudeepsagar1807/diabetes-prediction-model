import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

flask_app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@flask_app.route('/')
def home():
    return render_template("index.html")

@flask_app.route('/predict', methods=['POST'])
def predict():

    data = request.get_json()


    float_features = [float(x) for x in data.values()]
    features = np.array(float_features).reshape(1, -1)


    prediction = model.predict(features)[0]
    result = "Diabetic" if prediction == 1 else "Non-Diabetic"


    return jsonify({"result": result})

if __name__ == '__main__':
    flask_app.run(debug=True)
