import streamlit as st
import pandas as pd
import joblib
import pickle

# Load model and top 20 features
model = joblib.load("house_price_model.pkl")

with open("top_20_features.pkl", "rb") as f:
    top_20_features = pickle.load(f)

# Title
st.title("🏠 House Price Prediction App")
st.markdown("Enter the house details below to predict the **Sale Price**:")

# Input dictionary to collect user inputs
input_data = {}

# Layout: group inputs in columns
col1, col2 = st.columns(2)

for idx, feature in enumerate(top_20_features):
    col = col1 if idx % 2 == 0 else col2

    # Simple numeric input for all features (you can customize based on data type if known)
    input_data[feature] = col.number_input(
        label=feature,
        min_value=0.0,
        step=1.0,
        format="%.2f"
    )

# Predict button
if st.button("Predict Sale Price"):
    # Convert input to DataFrame
    input_df = pd.DataFrame([input_data])
    
    # Make prediction
    prediction = model.predict(input_df)[0]

    # Display result
    st.success(f"🏡 Predicted Sale Price: **${prediction:,.2f}**")
