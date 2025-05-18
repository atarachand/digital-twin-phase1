import pandas as pd
import numpy as np
import random
from datetime import datetime

def generate_sensor_data():
    timestamp = datetime.now()
    vibration = round(np.random.normal(3.0, 0.5), 2)
    temperature = round(np.random.normal(40.0, 2.0), 1)
    load = round(random.uniform(50, 100), 1)
    speed = round(np.random.normal(1.2, 0.1), 2)
    return {
        'timestamp': timestamp,
        'vibration_mm_s': vibration,
        'temperature_C': temperature,
        'load_percent': load,
        'speed_m_s': speed
    }

def simulate_stream(num_rows=50):
    data = [generate_sensor_data() for _ in range(num_rows)]
    df = pd.DataFrame(data)
    return df