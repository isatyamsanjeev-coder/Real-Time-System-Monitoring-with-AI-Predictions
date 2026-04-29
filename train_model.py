#3_train_model.py
import os
import pandas as pd
import sqlite3
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import IsolationForest
# Ensure models folder exists
os.makedirs("models", exist_ok=True)

conn = sqlite3.connect("data/metrics.db")
df = pd.read_sql("SELECT * FROM metrics", conn)

# Anomaly Detection

iso = IsolationForest(contamination=0.05, random_state=42)
df['anomaly'] = iso.fit_predict(df[['cpu', 'memory', 'disk']])

# Save anomaly model

joblib.dump(iso, "models/anomaly_model.pkl")
print("Anomaly detection model trained!")

#CPU Prediction Model

X = df[['memory', 'disk']]
y = df['cpu']

model = RandomForestRegressor(n_estimators=100)
model.fit(X, y)

joblib.dump(model, "models/cpu_model.pkl")

print("Model trained and saved successfully!")