# Streamlit Code for this model work as frontend"
import streamlit as st
import requests

st.set_page_config(page_title="Boston House Price Prediction", layout="centered")

st.title(" Boston Housing Price Prediction")
st.write("Enter housing details to predict the house price.")

API_URL = "http://127.0.0.1:8000/predict"

with st.form("prediction_form"):
    CRIM = st.number_input("Crime rate per capita (CRIM)", min_value=0.0, value=0.0063)
    ZN = st.number_input("Residential land zoned (ZN)", min_value=0.0, value=18.0)
    INDUS = st.number_input("Non-retail business acres (INDUS)", min_value=0.0, value=2.37)
    CHAS = st.selectbox("Bounds Charles River (CHAS)", [0, 1])
    NOX = st.number_input("Nitric oxides concentration (NOX)", min_value=0.0, value=0.538)
    RM = st.number_input("Average rooms per dwelling (RM)", min_value=0.0, value=6.575)
    AGE = st.number_input("Owner-occupied units built before 1940 (AGE)", min_value=0.0, value=65.2)
    DIS = st.number_input("Distance to employment centers (DIS)", min_value=0.0, value=4.09)
    RAD = st.number_input("Accessibility to highways (RAD)", min_value=0, step=1, value=1)
    TAX = st.number_input("Property tax rate (TAX)", min_value=0.0, value=296.0)
    PTRATIO = st.number_input("Pupil-teacher ratio (PTRATIO)", min_value=0.0, value=15.3)
    B = st.number_input("Black population index (B)", min_value=0.0, value=396.9)
    LSTAT = st.number_input("Lower status population % (LSTAT)", min_value=0.0, value=4.98)

    submit = st.form_submit_button("Predict Price")

if submit:
    payload = {
        "CRIM": CRIM,
        "ZN": ZN,
        "INDUS": INDUS,
        "CHAS": CHAS,
        "NOX": NOX,
        "RM": RM,
        "AGE": AGE,
        "DIS": DIS,
        "RAD": RAD,
        "TAX": TAX,
        "PTRATIO": PTRATIO,
        "B": B,
        "LSTAT": LSTAT
    }

    try:
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            result = response.json()
            st.success(f" Predicted House Price: ${result['predicted_price']}k")
        else:
            st.error(f"API Error: {response.text}")

    except Exception as e:
        st.error(f"Connection Error: {e}") 
