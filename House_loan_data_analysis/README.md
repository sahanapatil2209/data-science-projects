Loan Default Prediction using ANN and XGBoost
Overview

This project focuses on predicting whether a loan applicant will default using historical financial and demographic data. The goal is to build and evaluate machine learning models that can accurately identify high risk applicants, helping financial institutions minimize credit risk and make better lending decisions.

The dataset contains a large number of features including income, credit amount, employment details, and applicant characteristics. Due to the imbalanced nature of the data, special attention is given to preprocessing and evaluation metrics that prioritize detecting defaulters.

Problem Statement

The objective of this project is to develop a predictive model that determines whether a loan applicant will default on a loan.

TARGET = 0 → Loan repaid (safe applicant)
TARGET = 1 → Loan defaulted (risky applicant)

This is a supervised binary classification problem.

A key challenge in this dataset is class imbalance, where defaulters represent a much smaller portion of the data. As a result, accuracy alone is not sufficient, and evaluation focuses on metrics such as sensitivity and ROC AUC.

Business Objective
Identify high risk applicants before loan approval
Reduce financial losses due to defaults
Improve credit risk assessment
Support data driven lending decisions
Dataset

The dataset includes the following types of features:

Demographic information (gender, family status, housing type)
Financial information (income, credit, annuity)
Behavioral indicators (employment duration, phone usage, etc.)
External risk scores (EXT_SOURCE variables)

Target variable:

TARGET: Loan repayment status
Data Preprocessing

The following preprocessing steps were applied:

Removed identifier column (SK_ID_CURR)
Checked and handled missing values
Split features into numerical and categorical
Imputed missing values:
Numerical → median
Categorical → most frequent
Applied One Hot Encoding for categorical features
Performed train test split with stratification
Addressed class imbalance using:
Class weights (ANN)
scale_pos_weight (XGBoost)
Models Implemented
1. Artificial Neural Network (ANN)
Multiple dense layers with ReLU activation
Dropout and batch normalization for regularization
Sigmoid activation for binary classification
Binary cross entropy loss
Early stopping to prevent overfitting
2. XGBoost
Gradient boosting based tree model
Handles non linear relationships effectively
Robust to tabular structured data
Uses scale_pos_weight to handle imbalance
Evaluation Metrics

Due to class imbalance, the following metrics were used:

Sensitivity (Recall): Measures how many actual defaulters were correctly identified
ROC AUC: Measures model’s ability to distinguish between classes
Confusion Matrix
Classification Report
Results
Model	Sensitivity	ROC AUC
ANN	0.7041	0.7483
XGBoost	0.7041	0.7600
Model Selection

XGBoost was selected as the final model because:

It achieved a higher ROC AUC compared to ANN
Both models had equal sensitivity, but XGBoost showed better overall class separation
Tree based models generally perform strongly on structured tabular data
Key Insights
Class imbalance significantly affects model performance
Sensitivity is critical in this problem because missing defaulters is costly
XGBoost outperforms ANN for this tabular dataset
Proper preprocessing and feature handling are crucial
Technologies Used
Python
Pandas
NumPy
Scikit learn
TensorFlow / Keras
XGBoost
Matplotlib
How to Run
Clone the repository
Install required libraries
Run the notebook step by step
Future Improvements
Feature selection and importance analysis
Hyperparameter tuning using GridSearch or Optuna
Threshold tuning to improve sensitivity
Use advanced models such as LightGBM or CatBoost
Deploy model using Streamlit or FastAPI
Key Takeaway

This project demonstrates how machine learning can be applied to credit risk prediction by handling imbalanced data, building robust models, and focusing on metrics that align with business objectives.
