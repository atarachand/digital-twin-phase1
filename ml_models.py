import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import MinMaxScaler
import pickle

def train_anomaly_model(df):
    features = ['vibration_mm_s', 'temperature_C', 'load_percent', 'speed_m_s']
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(df[features])
    model = IsolationForest(contamination=0.1)
    model.fit(X_scaled)
    preds = model.predict(X_scaled)
    return preds, model, scaler

def save_model(model, scaler, path_model='model.pkl', path_scaler='scaler.pkl'):
    with open(path_model, 'wb') as f:
        pickle.dump(model, f)
    with open(path_scaler, 'wb') as f:
        pickle.dump(scaler, f)

def load_model(path_model='model.pkl', path_scaler='scaler.pkl'):
    with open(path_model, 'rb') as f:
        model = pickle.load(f)
    with open(path_scaler, 'rb') as f:
        scaler = pickle.load(f)
    return model, scaler