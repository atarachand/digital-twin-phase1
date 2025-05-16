import streamlit as st
import time
from sensor_simulation import simulate_stream, preprocess_data
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Conveyor Belt Digital Twin - Phase 1 & 2", layout="wide")
st.title("📊 Conveyor Belt Digital Twin - Phase 1 & 2")

# Phase 1: Simulate sensor data
raw_data = simulate_stream(num_rows=50)
st.subheader("🔁 Simulated Sensor Data (Raw)")
st.write(raw_data)

# Phase 2: Preprocess data
processed_data = preprocess_data(raw_data)
st.subheader("🧹 Preprocessed Sensor Data")
st.write(processed_data)

# Phase 2: Visualizations
st.subheader("📈 Time-Series Visualizations")
col1, col2 = st.columns(2)

with col1:
    fig1 = px.line(processed_data, x='timestamp', y='vibration_mm_s', title='Vibration (mm/s)')
    st.plotly_chart(fig1, use_container_width=True)

    fig2 = px.line(processed_data, x='timestamp', y='temperature_C', title='Temperature (°C)')
    st.plotly_chart(fig2, use_container_width=True)

with col2:
    fig3 = px.line(processed_data, x='timestamp', y='load_percent', title='Load (%)')
    st.plotly_chart(fig3, use_container_width=True)

    fig4 = px.line(processed_data, x='timestamp', y='speed_m_s', title='Speed (m/s)')
    st.plotly_chart(fig4, use_container_width=True)

# Optional: Save preprocessed data to CSV
csv = processed_data.to_csv(index=False)
st.download_button("📥 Download Preprocessed Data as CSV", csv, "processed_sensor_data.csv", "text/csv")