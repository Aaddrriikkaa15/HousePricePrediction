# HousePricePrediction

Welcome to my **House Price Prediction** project!  
This project demonstrates a complete **data science pipeline** — from data preprocessing and feature engineering to model training and custom predictions.

---

## 📌 Project Overview

The goal is to predict house prices using various features like area, quality, garage size, number of baths, neighborhood, etc.

This project was built as part of my **Data Science Internship** at **Celebal Technologies**.

---

## ✅ Tasks Covered

- 📂 **Data Loading:** Load training and test datasets.
- 🧹 **Data Preprocessing:** Handle missing values, encode categorical variables (One-Hot Encoding), scale features.
- 🔍 **Exploratory Data Analysis (EDA):** Plots and correlation heatmaps to find important features.
- ⚙️ **Feature Engineering:** Drop low-correlation features and select only meaningful predictors.
- 🤖 **Model Training:** Random Forest Regressor to predict `SalePrice`.
- 🔮 **Custom Predictions:** Input your own house details and predict the price live!

---

## 📁 Dataset

The dataset is inspired by the classic **Kaggle House Prices - Advanced Regression Techniques** dataset.
link - https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques
- `train.csv`: Contains features & target (`SalePrice`).
- `test.csv`: Contains features for prediction & submission format.

---

## 🖥️ Streamlit Web App

We have added a Streamlit interface to allow interactive house price prediction.

### How to Run the Streamlit App

```bash
pip install -r requirements.txt
streamlit run app.py
yaml
Copy
Edit



## 📈 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/Aaddrriikkaa15/house-price-prediction.git
   cd house-price-prediction

2. **Git Commands to Add and Push the New Files**

Open terminal inside your repo folder and run:

```bash
git add app.py house_price_model.pkl top_20_features.pkl requirements.txt
git commit -m "Added Streamlit app for interactive house price prediction"
git push origin main
