# Conveyor Belt Digital Twin - Phase 1 to 4

This full-stack simulation includes all 4 phases of a Digital Twin implementation for a Conveyor Belt.

## Phase 1: Sensor Simulation
- Generate vibration, temperature, load, and speed values

## Phase 2: Preprocessing
- Clean, clip, normalize
- Visualize time series

## Phase 3: AI/ML Models
- Anomaly Detection with Isolation Forest

## Phase 4: Dashboard and 3D Twin
- Real-time charts with Plotly
- Embedded 3D model viewer (simulated using 3DViewer.net iframe)

## How to Run
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Deploy Online
1. Push to GitHub
2. Deploy on [Streamlit Cloud](https://streamlit.io/cloud)
3. Use `streamlit_app.py` as the entry point