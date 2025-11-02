# Gender---1Female 0Male
# Churn---1Yes 0No
# scaler is exported as scaler.pkl
# Model is exported as model.pkl
# Order of the x is ['Age', 'Gender', 'MonthlyCharges', 'Tenure']

import numpy as np
import pandas as pd
import joblib
import streamlit as st

# Load the saved scaler and model
scaler = joblib.load('scaler.pkl')
model = joblib.load('model.pkl')

st.title('Customer Churn Prediction')

st.divider()
st.write("Please enter the values then press the button for a prediction.")

st.divider()

# Input fields
age = st.number_input('Enter Age', min_value=11, max_value=100, value=30, step=1)
gender = st.selectbox("Enter Gender", ["Male", "Female"])
tenure = st.number_input('Enter Tenure', min_value=0, max_value=111, value=12, step=1)
monthlycharges = st.number_input('Enter Monthly Charges', min_value=0.0, max_value=200.0, value=70.0, step=0.1)

st.divider()

# ✅ Only one button here
predictbutton = st.button("Predict", key="predict_button")
st.divider()   # remove the extra space

if predictbutton:
    # Convert gender to numeric
    gender_selected = 1 if gender == "Female" else 0

    # Create input array
    X = np.array([[age, gender_selected, monthlycharges, tenure]])

    # Scale inputs using your saved scaler
    X_scaled = scaler.transform(X)

    # Make prediction
    prediction = model.predict(X_scaled)[0]

    # Interpret prediction
    predicted = "Churn" if prediction == 1 else "Not Churn"
    st.balloons()

    # Display result
    st.success(f"The model predicts: {predicted}")

else:
    st.write("Please enter the values and use the Predict button.")
