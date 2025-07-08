
from flask import Flask, request, jsonify
import joblib
import numpy as np

# Load model and encoders
model = joblib.load("models/ghg_model.pkl")
le_industry = joblib.load("models/industry_encoder.pkl")
le_substance = joblib.load("models/substance_encoder.pkl")

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    try:
        features = [
            le_industry.transform([data['Industry Code']])[0],
            le_industry.transform([data['Industry Name']])[0],
            le_substance.transform([data['Substance']])[0],
            data['DQ_Reliability'],
            data['DQ_Temporal'],
            data['DQ_Geographical'],
            data['DQ_Technological'],
            data['DQ_DataCollection']
        ]
        prediction = model.predict([features])[0]
        return jsonify({"predicted_emission_factor": prediction})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
