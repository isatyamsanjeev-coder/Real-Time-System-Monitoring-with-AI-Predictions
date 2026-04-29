# 📊 Real-Time System Monitoring with AI Predictions

A smart monitoring system built with **Python, Streamlit, SQLite, and Machine Learning** that tracks real-time system metrics such as CPU, Memory, and Disk usage. The project visualizes live performance data, predicts future CPU load using AI models, detects anomalies, and triggers alerts when abnormal behavior is found.

---

## 📌 Overview

This project simulates an intelligent DevOps / IT monitoring dashboard where system performance metrics are continuously stored, analyzed, and visualized. Instead of only showing current usage, it also uses Machine Learning models to predict future CPU consumption and identify suspicious patterns.

It is useful for learning how AI can be integrated into system administration, infrastructure monitoring, and predictive maintenance solutions.

---

## ✨ Features

### 🖥️ Real-Time Monitoring

* Tracks:

  * CPU Usage
  * Memory Usage
  * Disk Usage
* Reads and stores metrics in a local SQLite database

### 📈 Live Dashboard

* Interactive dashboard built with Streamlit
* CPU usage trend chart using Plotly
* Clean and responsive UI

### 🤖 AI-Based CPU Prediction

* Uses trained ML model to predict CPU usage based on:

  * Memory usage
  * Disk usage

### 🚨 Smart Alerts

* Sends warning alerts when predicted CPU usage crosses threshold (85%)

### 🔍 Anomaly Detection

* Detects unusual system behavior using anomaly detection model
* Alerts users when abnormal metrics are found

### 💾 Database Integration

* Stores metrics history in SQLite
* Enables trend analysis and reporting

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Frontend / Dashboard

* Streamlit
* Plotly

### Backend / Data Handling

* SQLite
* Pandas

### Machine Learning

* Scikit-learn
* Joblib

---

## 📂 Project Structure

```text
Real-Time-System-Monitoring-with-AI-Predictions/
│── app.py                # Streamlit dashboard
│── database.py           # Create DB + insert metrics
│── alerts.py             # Alert sending logic
│── models/
│   ├── cpu_model.pkl
│   └── anomaly_model.pkl
│── data/
│   └── metrics.db
│── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

### Step 1: Collect Metrics

System metrics like CPU, memory, and disk usage are captured and inserted into SQLite database.

### Step 2: Visualize Data

The dashboard reads database records and displays CPU trends using graphs.

### Step 3: Predict CPU Usage

The ML model predicts future CPU usage using latest memory and disk data.

### Step 4: Trigger Alerts

If predicted CPU > 85%, warning alert is triggered.

### Step 5: Detect Anomalies

Another ML model checks if current system behavior is abnormal.

---

## 🚀 Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/isatyamsanjeev-coder/Real-Time-System-Monitoring-with-AI-Predictions.git
cd Real-Time-System-Monitoring-with-AI-Predictions
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

For Windows:

```bash
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Database Script

```bash
python database.py
```

### 5️⃣ Start Streamlit App

```bash
streamlit run app.py
```

---

## 📊 Example Dashboard Outputs

* Live CPU usage graph
* Predicted CPU usage percentage
* High CPU warning alert
* Anomaly detection warning

---

## 🎯 Learning Outcomes

This project helps in understanding:

* Real-time data pipelines
* SQLite database integration
* Streamlit dashboard development
* ML model deployment
* Predictive analytics
* Anomaly detection systems
* Alert automation

---

## ⚠️ Limitations

* Uses local SQLite database only
* Basic alerting mechanism
* Suitable for learning/demo scale
* Requires trained models (.pkl files)

---

## 🔮 Future Improvements

* Email / SMS alert system
* Cloud deployment
* Docker support
* Multi-server monitoring
* Historical reports
* User authentication
* Better anomaly explanations

---

## 👨‍💻 Author

**Satyam Sanjeev**

GitHub: https://github.com/isatyamsanjeev-coder

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
