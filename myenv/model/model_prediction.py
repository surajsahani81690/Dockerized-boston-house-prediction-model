import joblib
import pandas as pd
import os

# Load the model from the same folder as this script
MODEL_PATH = os.path.join(os.path.dirname(__file__), "boston_xgb_regressor_pipeline.pkl")
model = joblib.load(MODEL_PATH)

def model_prediction(user_input: dict):
    """
    Accepts a dictionary of input features,
    converts it to a DataFrame, and predicts using the loaded model.
    """
    df = pd.DataFrame([user_input])
    prediction = model.predict(df)[0]
    return round(float(prediction),2)

