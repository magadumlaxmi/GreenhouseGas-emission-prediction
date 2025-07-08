from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import os

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS

# Load ML model and encoders
model = joblib.load("models/ghg_model.pkl")
industry_encoder = joblib.load("models/industry_encoder.pkl")
substance_encoder = joblib.load("models/substance_encoder.pkl")

# Root route (GET)
@app.route('/')
def home():
    return "✅ Welcome to the Greenhouse Gas Emission Prediction API! Use /predict (POST) to get predictions."

# Prediction route
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return "✅ GHG Emission Prediction API is live. Use POST method to get predictions."

    try:
        data = request.get_json()

        # Extract features and encode
        features = [
            industry_encoder.transform([data["Industry Code"]])[0],
            industry_encoder.transform([data["Industry Name"]])[0],
            substance_encoder.transform([data["Substance"]])[0],
            data["DQ_Reliability"],
            data["DQ_Temporal"],
            data["DQ_Geographical"],
            data["DQ_Technological"],
            data["DQ_DataCollection"]
        ]

        # Make prediction
        prediction = model.predict([features])[0]
        return jsonify({"predicted_emission_factor": round(float(prediction), 3)})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Run the app on dynamic Render port
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
