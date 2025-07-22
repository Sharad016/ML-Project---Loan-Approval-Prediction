# 🏦 Loan Approval Prediction App

This is a **Loan Approval Prediction Web App** built using **Machine Learning** and deployed using **Streamlit** and **Hugging Face**. The app predicts whether a loan will be approved or not based on user inputs.

---

## Project Overview

Loan approval prediction is a common use case in banking where banks can assess an applicant’s eligibility using a variety of parameters. This app simplifies that task using a trained ML model and a simple, interactive web interface.

---

## Technology used 

* **Frontend/UI**: [Streamlit]
* **Model Training**: Scikit-learn, Pandas, NumPy
* **Dataset**: Kaggle Loan Prediction Dataset (https://www.kaggle.com/datasets/altruistdelhite04/loan-prediction-problem-dataset)
* **Deployment**: Hugging Face Spaces

---

##  Dataset

* Source: [Kaggle - Loan Prediction Dataset](https://www.kaggle.com/datasets/altruistdelhite04/loan-prediction-problem-dataset)
* File Used: `train_u6lujuX_CVtuZ9i.csv`
* Target Column: `Loan_Status`

---

##  Features

* Predicts loan approval status based on:

  * Education
  * Applicant Total Income
  * Loan Amount
  * Credit History
  * Number of financially Dependent Persons in Home
* Clean and interactive web interface
* Instant result after submitting inputs

---

## Preprossing of the Data

*  For the missig Values of the Credit_History Column of the dataset , used mode of the rest Values
*  Dropped Null Values of Dependents Column and convert 3+ to 3 and make all of the column to int32 Type
*  Label Encoded the Columns : Education and Loan_Status
*  Merged the Column ApplicantIncome and CoapplicantIncome and added them to a new column Income
*  Deleted Columns : Loan_ID , Gender , Married , Self_Employed	, Property_Area

##  Project Structure

```
loan-approval-prediction/
|
├── app.py                                  # Streamlit frontend app
├── model.pkl                               # Trained ML model
├── data/                   
│   └── train_u6lujuX_CVtuZ9i.csv           # Original Kaggle dataset
├── requirements.txt                        # List of dependencies
├── README.md                               # Project documentation
```

---


## Model Info

* Model Type: Random Forest 
* Accuracy Achieved: 81.5%
* Preprocessing: Label Encoding, Handling Missing Values , One Hot Encoding
---

## Why Random Forest

* The Random Forest Model can easily Handle categorial data. So, it became the best choice for this dataset 
* Other Models accuracy :
  
  Logistic Regression  - 76.32%
  XG Boost Classifier  - 75.44%
  Light GBM Classifier - 74.56%

##  Deployment

 Deployed it on Hugging Face
 
 * 🖥️ Try the app live: [Loan Approval Predictor App](https://huggingface.co/spaces/Sharad016/Loan_Prediction_Model)

---


##  Author

**Sharad Gupta**
[LinkedIn](https://www.linkedin.com/in/sharad-gupta-8196a4321/)
Email: [sharad2001spg@gmail.com](mailto:sharad2005guptag@gmail.com)

---
