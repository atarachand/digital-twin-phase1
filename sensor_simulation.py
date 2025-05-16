import pandas as pd
import numpy as np
import random
from datetime import datetime

def generate_sensor_data(fault_mode=None):
    timestamp = datetime.now()

    if fault_mode == 'overheat':
        temperature = round(np.random.normal(85.0, 2.0), 1)
    else:
        temperature = round(np.random.normal(40.0, 2.0), 1)

    if fault_mode == 'overload':
        load = round(random.uniform(105, 130), 1)
    else:
        load = round(random.uniform(50, 100), 1)

    if fault_mode == 'imbalance':
        vibration = round(np.random.normal(7.0, 0.7), 2)
    else:
        vibration = round(np.random.normal(3.0, 0.5), 2)

    speed = round(np.random.normal(1.2, 0.1), 2)
    
    return {
        'timestamp': timestamp,
        'vibration_mm_s': vibration,
        'temperature_C': temperature,
        'load_percent': load,
        'speed_m_s': speed
    }

def simulate_stream(num_rows=50, fault_mode=None):
    data = [generate_sensor_data(fault_mode) for _ in range(num_rows)]
    df = pd.DataFrame(data)
    return df

def preprocess_data(df):
    df_clean = df.copy()
    df_clean = df_clean.dropna()
    df_clean['vibration_mm_s'] = df_clean['vibration_mm_s'].clip(0, 10)
    df_clean['temperature_C'] = df_clean['temperature_C'].clip(20, 120)
    df_clean['load_percent'] = df_clean['load_percent'].clip(0, 130)
    df_clean['speed_m_s'] = df_clean['speed_m_s'].clip(0, 3)
    df_clean['timestamp'] = pd.to_datetime(df_clean['timestamp'])
    return df_clean