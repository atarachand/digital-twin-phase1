# Conveyor Belt Digital Twin - Phase 1 to 5

## Phase 1: Sensor Simulation
- Simulates vibration, temperature, load, and speed

## Phase 2: Preprocessing
- Data cleaning and clipping
- Time-series visualization

## Phase 3: ML Model
- Anomaly detection using Isolation Forest

## Phase 4: Dashboard + 3D Viewer
- Interactive visual dashboard with real-time plots
- Embedded 3D visualization (simulated)

## Phase 5: Simulation and Fault Injection
- Inject synthetic faults: overheat, overload, imbalance
- Observe model response and anomaly detection

## Run Locally
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Deploy Online
1. Push to GitHub
2. Deploy via https://streamlit.io/cloud
3. Use `streamlit_app.py` as the entry point