import streamlit as st
import pandas as pd
import time
import plotly.express as px
from sensor_simulation import simulate_stream, preprocess_data
from ml_models import train_anomaly_model

st.set_page_config(page_title="Conveyor Belt Digital Twin - Phase 1 to 3", layout="wide")
st.title("📊 Conveyor Belt Digital Twin - Phase 1 to 3")

# Phase 1: Simulate Data
raw_data = simulate_stream(num_rows=100)
st.subheader("🔁 Simulated Sensor Data (Raw)")
st.write(raw_data)

# Phase 2: Preprocess
processed_data = preprocess_data(raw_data)
st.subheader("🧹 Preprocessed Sensor Data")
st.write(processed_data)

# Phase 3: ML Model - Anomaly Detection
st.subheader("🚨 Anomaly Detection using Isolation Forest")
preds, model, scaler = train_anomaly_model(processed_data)
processed_data['anomaly'] = preds
anomalies = processed_data[processed_data['anomaly'] == -1]

st.write("🔴 Detected Anomalies")
st.write(anomalies)

# Visualize
st.subheader("📈 Visualizations")
col1, col2 = st.columns(2)

with col1:
    fig1 = px.scatter(processed_data, x='timestamp', y='vibration_mm_s', color='anomaly', title='Vibration with Anomaly')
    st.plotly_chart(fig1, use_container_width=True)

    fig2 = px.scatter(processed_data, x='timestamp', y='temperature_C', color='anomaly', title='Temperature with Anomaly')
    st.plotly_chart(fig2, use_container_width=True)

with col2:
    fig3 = px.scatter(processed_data, x='timestamp', y='load_percent', color='anomaly', title='Load with Anomaly')
    st.plotly_chart(fig3, use_container_width=True)

    fig4 = px.scatter(processed_data, x='timestamp', y='speed_m_s', color='anomaly', title='Speed with Anomaly')
    st.plotly_chart(fig4, use_container_width=True)