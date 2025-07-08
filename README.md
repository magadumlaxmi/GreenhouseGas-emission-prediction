# 🌱 Greenhouse Gas Emission Prediction API

This project is built as part of the Shell Edunet Internship Program to predict Greenhouse Gas (GHG) Emission Factors using machine learning.

## 📌 Project Structure

```
Greenhouse-Gas-Emission-Prediction/
├── app.py                          # Flask API to serve predictions
├── GHG_Emissions_Prediction.ipynb # Jupyter notebook for training
├── models/                         # Saved ML model & encoders
│   ├── ghg_model.pkl
│   ├── industry_encoder.pkl
│   └── substance_encoder.pkl
├── SupplyChainEmissionFactors.xlsx # Dataset
├── requirements.txt                # Python dependencies
└── README.md
```

## 🚀 How to Run

1. Clone or download this repository.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the Flask API:
   ```
   python app.py
   ```

4. Test using Postman or curl:
   - POST to: `http://127.0.0.1:5000/predict`
   - Example JSON body:
     ```json
     {
       "Industry Code": "111CA",
       "Industry Name": "111CA",
       "Substance": "carbon dioxide",
       "DQ_Reliability": 4,
       "DQ_Temporal": 2,
       "DQ_Geographical": 1,
       "DQ_Technological": 4,
       "DQ_DataCollection": 1
     }
     ```

## 🧠 Model

A linear regression model trained on industry-level emission factor data (2016) to estimate supply chain GHG emission factors based on:
- Industry and substance
- Data quality metrics

## ✨ Output

Returns a predicted GHG emission factor in JSON.

---

**Project by:** Laxmi Magadum  
**Internship Program:** Shell Edunet + AICTE  
