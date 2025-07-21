# app.py
import streamlit as st
import joblib
import numpy as np

# Load model and columns
model = joblib.load("loan_model.pkl")
model_columns = joblib.load("model_columns.pkl")

st.title("Loan Approval Prediction App")
st.write("Enter applicant details to predict whether the loan will be approved.")

# User input
dependents = st.selectbox("Number of financially Dependent Persons in Home", ['0', '1', '2', '2+'])
education = st.selectbox("Education", ['Graduate', 'Not Graduate'])
loan_amount = st.number_input("Loan Amount (in ₹1000s)", min_value=0)
loan_term = st.selectbox("Loan Amount Term (in months)", [12, 36, 60, 120, 180, 240, 300, 360])
credit_history = st.selectbox("Credit History", ['Good', 'Not_Good'])
income = st.number_input("Combined Income (Applicant + Coapplicant)", min_value=0)

# Preprocessing user inputs
dependents = 3 if dependents == '2+' else int(dependents)
education = 1 if education == 'Graduate' else 0
credit_history = 1 if credit_history == 'Good' else 0

# Final input array
input_data = np.array([[dependents, education, loan_amount, loan_term, credit_history, income]])
input_data = input_data.reshape(1, -1)

# Prediction
if st.button("Predict Loan Approval"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Not Approved")
