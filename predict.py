#4_predict.py
import joblib

model = joblib.load("models/cpu_model.pkl")

def predict_cpu(memory, disk):
    return model.predict([[memory, disk]])[0]