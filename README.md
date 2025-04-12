# Loan Eligibility Prediction Model

## Project Overview

This project focuses on building a **Loan Eligibility Prediction Model** to classify whether an applicant is eligible for a loan based on various attributes. The dataset used for this project contains details of 614 loan applicants, including their income, loan amount, credit history, and other features.

### **Goal**:
- The goal of this project is to create a machine learning model that predicts whether a loan will be approved for an applicant based on various factors.
- The model will be trained using a dataset and evaluated to achieve a good level of accuracy in loan eligibility classification (target accuracy: **76%** or higher).

### **Machine Learning Task**:
- **Task Type**: Classification
- **Target Variable**: `Loan_Approved` (Yes/No)
- **Success Criteria**: Model accuracy of 76% and above.

---

## Files in the Project

1. **`preprocessing.py`**:
   - Contains functions for **data cleaning**, **handling missing values**, and **encoding categorical variables**.
   
2. **`train_model.py`**:
   - Loads the dataset, preprocesses the data, trains a **Random Forest Regressor** (or other classification models), and saves the trained model to a file (`loan_eligibility_model.pkl`).

3. **`streamlit.py`**:
   - This is a **Streamlit app** that provides an interactive user interface to predict loan eligibility. Users can input details such as income, loan amount, credit history, etc., and get predictions from the trained model.

---

## Dataset

The dataset used for this project contains the following columns:

- **Loan_ID**: Applicant ID
- **Gender**: Gender of the applicant (Male/Female)
- **Married**: Marital status of the applicant (Yes/No)
- **Dependents**: Number of dependents the applicant has
- **Education**: Highest level of education (Graduate/Not Graduate)
- **Self_Employed**: Whether self-employed (Yes/No)
- **ApplicantIncome**: Monthly income of the applicant
- **CoapplicantIncome**: Monthly income of the co-applicant
- **LoanAmount**: Loan amount requested (in 1000s)
- **Loan_Amount_Term**: Term of the loan in months
- **Credit_History**: Whether the applicant has a credit history (1 for Yes, 0 for No)
- **Property_Area**: Area where the property is located (Urban/Semiurban/Rural)
- **Loan_Approved**: Target variable (Loan approved Yes/No)

---

## Steps to Run the Project

### **1. Install Dependencies**:
Ensure you have the required Python packages installed. You can install the necessary libraries using `pip`:

```bash
pip install -r requirements.txt
