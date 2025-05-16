import streamlit as st
import pandas as pd
import plotly.express as px
from sensor_simulation import simulate_stream, preprocess_data
from ml_models import train_anomaly_model

st.set_page_config(page_title="Conveyor Belt Digital Twin - Phase 1 to 5", layout="wide")
st.title("🛰️ Conveyor Belt Digital Twin - Phase 1 to 5")

# Phase 5: Fault injection
st.sidebar.header("🧪 Fault Injection Mode")
fault_mode = st.sidebar.selectbox("Select a Fault Mode", [None, "overheat", "overload", "imbalance"])

# Phase 1
raw_data = simulate_stream(num_rows=100, fault_mode=fault_mode)
st.subheader("🔁 Simulated Sensor Data (Raw)")
st.write(raw_data)

# Phase 2
processed_data = preprocess_data(raw_data)
st.subheader("🧹 Preprocessed Sensor Data")
st.write(processed_data)

# Phase 3
st.subheader("🚨 Anomaly Detection using Isolation Forest")
preds, model, scaler = train_anomaly_model(processed_data)
processed_data['anomaly'] = preds
anomalies = processed_data[processed_data['anomaly'] == -1]
st.write("🔴 Detected Anomalies")
st.write(anomalies)

# Phase 4: Dashboard and Visualization
st.subheader("📊 Real-Time Monitoring Dashboard")
col1, col2 = st.columns(2)

with col1:
    fig1 = px.scatter(processed_data, x='timestamp', y='vibration_mm_s', color='anomaly', title='Vibration (mm/s)')
    st.plotly_chart(fig1, use_container_width=True)

    fig2 = px.scatter(processed_data, x='timestamp', y='temperature_C', color='anomaly', title='Temperature (°C)')
    st.plotly_chart(fig2, use_container_width=True)

with col2:
    fig3 = px.scatter(processed_data, x='timestamp', y='load_percent', color='anomaly', title='Load (%)')
    st.plotly_chart(fig3, use_container_width=True)

    fig4 = px.scatter(processed_data, x='timestamp', y='speed_m_s', color='anomaly', title='Speed (m/s)')
    st.plotly_chart(fig4, use_container_width=True)

# Phase 4 continued: 3D Viewer
st.subheader("🖼️ Digital Twin 3D Visualization")
st.markdown(
    '''
    <iframe src="https://3dviewer.net/embed.html#model=https://github.com/mrdoob/three.js/blob/dev/examples/models/gltf/Duck/glTF/Duck.gltf" 
            width="100%" height="480" frameborder="0" allowfullscreen></iframe>
    ''',
    unsafe_allow_html=True
)