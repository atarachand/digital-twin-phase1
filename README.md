# Conveyor Belt Digital Twin - Phase 1 & 2

This project simulates a digital twin for a conveyor belt with real-time sensor data.

## Phase 1:
- Simulates vibration, temperature, load, and speed sensors
- Live streaming in Streamlit

## Phase 2:
- Preprocessing (data cleaning, normalization)
- Time-series visualization
- Downloadable CSV of cleaned data

## Run Locally
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Deploy on Streamlit Cloud
1. Push to GitHub
2. Connect to Streamlit Cloud
3. Use `streamlit_app.py` as the entry point