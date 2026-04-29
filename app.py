#6_app.py
import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px
import joblib
from alerts import send_alert   # Import alert function

# Load models
cpu_model = joblib.load("models/cpu_model.pkl")
anomaly_model = joblib.load("models/anomaly_model.pkl")

st.title(" Real-Time System Monitoring")

# Connect to database
conn = sqlite3.connect("data/metrics.db")
df = pd.read_sql("SELECT * FROM metrics", conn)

# Show CPU Graph
st.subheader("Live CPU Usage")
fig = px.line(df, x="timestamp", y="cpu")
st.plotly_chart(fig)

# Get latest record
latest_cpu = df['cpu'].iloc[-1]
latest_memory = df['memory'].iloc[-1]
latest_disk = df['disk'].iloc[-1]

# CPU Prediction

predicted_cpu = cpu_model.predict([[latest_memory, latest_disk]])[0]
st.metric("Predicted CPU Usage", f"{predicted_cpu:.2f}%")

#ALERT TRIGGER

if predicted_cpu > 85:
    send_alert(" Warning: High CPU usage predicted!")
    st.error(" High CPU Alert Sent!")
else:
    st.success("System Normal")

# Anomaly Detection

anomaly = anomaly_model.predict([[latest_cpu, latest_memory, latest_disk]])[0]

if anomaly == -1:

    st.warning(" Anomaly Detected!")

