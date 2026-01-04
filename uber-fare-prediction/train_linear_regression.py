import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns
from math import radians, sin, cos, sqrt, atan2

# 1. Load and subset data (keep small for GitHub)
df = pd.read_csv(r'C:\Users\ASUS\PyCharmMiscProject\input\uber.csv')  # Or download from Kaggle
df.head()
df.shape
df.info()
df.describe()

# df = df.sample(10000, random_state=42).reset_index(drop=True)


# 2. Feature Engineering
def haversine_distance(row):
    """Calculate distance between pickup and dropoff"""
    R = 6371  # Earth radius in km

    lat1, lon1 = radians(row['pickup_latitude']), radians(row['pickup_longitude'])
    lat2, lon2 = radians(row['dropoff_latitude']), radians(row['dropoff_longitude'])

    dlat, dlon = lat2 - lat1, lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c


# Add distance feature
df['distance_km'] = df.apply(haversine_distance, axis=1)

# Extract hour from datetime
df['pickup_hour'] = pd.to_datetime(df['pickup_datetime']).dt.hour

# Remove outliers
df = df[(df['fare_amount'] > 0) & (df['fare_amount'] < 100)]
df = df[(df['distance_km'] > 0) & (df['distance_km'] < 50)]

# Features and target
features = ['distance_km', 'pickup_hour', 'passenger_count']
X = df[features]
y = df['fare_amount']

# 3. Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 5. Train Linear Regression
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# 6. Predictions and Evaluation
y_pred = model.predict(X_test_scaled)
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"R² Score: {r2:.3f}")
print(f"RMSE: ${rmse:.2f}")
print(f"Coefficients: {dict(zip(features, model.coef_))}")
print(f"Intercept: ${model.intercept_:.2f}")

# Expected output: R² ~0.65-0.75, RMSE ~$4-6

