import streamlit as st
import pandas as pd
import pickle

# Set the page configuration
st.set_page_config(page_title="Loan Eligibility Checker", layout="wide")

# Header and description
st.header("Loan Eligibility Checker")
st.markdown("""
Welcome to the **Loan Eligibility Checker** app! 🌟
Find out if you're eligible for a loan by providing a few personal and financial details. 
This app uses a machine learning model for predictions.
""")

# Sidebar for inputs
st.sidebar.title("Input Loan Details")
st.sidebar.markdown("Please fill out the following details:")

# Gender input
Gender = st.sidebar.radio("Gender", options=["Male", "Female"])

# Marital Status
Married = st.sidebar.radio("Marital Status", options=["Yes", "No"])

# Dependents
Dependents = st.sidebar.selectbox("Number of Dependents", options=["0", "1", "2", "3+"])

# Education
Education = st.sidebar.radio("Education Level", options=["Graduate", "Not Graduate"])

# Self Employment
Self_Employed = st.sidebar.radio("Self Employed?", options=["Yes", "No"])

# Applicant Income
ApplicantIncome = st.sidebar.number_input("Applicant Monthly Income ($)", min_value=0, step=500, format="%d")

# Coapplicant Income
CoapplicantIncome = st.sidebar.number_input("Coapplicant Monthly Income ($)", min_value=0, step=500, format="%d")

# Loan Amount
LoanAmount = st.sidebar.slider("Loan Amount ($)", min_value=0, max_value=500000, step=5000)

# Loan Amount Term
Loan_Amount_Term = st.sidebar.selectbox("Loan Term (Months)", options=["360", "180", "240", "120", "60"])

# Credit History
Credit_History = st.sidebar.radio("Credit History", options=["1 (Good)", "0 (Bad)"])
Credit_History = Credit_History.split()[0]  # Extract the numeric value

# Property Area
Property_Area = st.sidebar.radio("Property Area", options=["Urban", "Semiurban", "Rural"])

# Submit button
if st.sidebar.button("Check Eligibility"):
    # Load the pre-trained model
    with open("models/RFmodel.pkl", "rb") as file:
        rf_model = pickle.load(file)

    # Prepare the input for prediction
    prediction_input = [[
        ApplicantIncome, CoapplicantIncome, LoanAmount, int(Loan_Amount_Term),
        int(Credit_History), Gender == "Female", Gender == "Male",
        Married == "No", Married == "Yes", Dependents == "0",
        Dependents == "1", Dependents == "2", Dependents == "3+",
        Education == "Graduate", Education == "Not Graduate",
        Self_Employed == "No", Self_Employed == "Yes",
        Property_Area == "Rural", Property_Area == "Semiurban", Property_Area == "Urban"
    ]]

    # Make prediction
    prediction = rf_model.predict(prediction_input)

    # Display prediction result
    st.subheader("Prediction Result:")
    if prediction[0] == 1:
        st.success("🎉 Congratulations! You are eligible for a loan!")
    else:
        st.error("Unfortunately, you are not eligible for a loan.")

# Footer with additional info
st.markdown("---")
st.caption("Powered by a Random Forest Model 🤖")
