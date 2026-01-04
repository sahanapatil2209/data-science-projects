# Uber Fare Prediction

This project predicts Uber ride fares using linear regression and feature engineering.

## Problem Statement
Given pickup and dropoff coordinates, time of day, and passenger count, predict the fare amount.

## Feature Engineering
- Haversine distance between pickup and dropoff
- Pickup hour extraction from timestamp
- Passenger count

## Model
- Linear Regression (baseline)
- Evaluated using R² and RMSE

## How to Run

pip install -r requirements.txt
python train_linear_regression.py
