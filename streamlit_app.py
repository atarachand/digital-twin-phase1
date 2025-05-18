import streamlit as st
import time
from sensor_simulation import simulate_stream
import plotly.express as px

st.set_page_config(page_title="Conveyor Belt Digital Twin - Phase 1", layout="wide")
st.title("📊 Conveyor Belt Digital Twin - Phase 1: Real-Time Sensor Monitoring")

placeholder = st.empty()

for _ in range(100):
    data = simulate_stream(num_rows=1)
    with placeholder.container():
        st.subheader("🔁 Live Conveyor Belt Sensor Readings")
        st.write(data)

        col1, col2 = st.columns(2)

        with col1:
            fig1 = px.line(data, x='timestamp', y='vibration_mm_s', title='Vibration (mm/s)')
            st.plotly_chart(fig1, use_container_width=True)

            fig2 = px.line(data, x='timestamp', y='temperature_C', title='Temperature (°C)')
            st.plotly_chart(fig2, use_container_width=True)

        with col2:
            fig3 = px.line(data, x='timestamp', y='load_percent', title='Load (%)')
            st.plotly_chart(fig3, use_container_width=True)

            fig4 = px.line(data, x='timestamp', y='speed_m_s', title='Speed (m/s)')
            st.plotly_chart(fig4, use_container_width=True)

    time.sleep(1)