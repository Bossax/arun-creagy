# CRI Impact Visualization App (Standalone)

This application provides an interactive dashboard for visualizing Thailand's Climate Resilience Index (CRI) impact data from B.E. 2560 to 2567.

## Structure
- `app.py`: Main Streamlit application.
- `data/`: Contains the Gold Fact CSVs and spatial boundary files (SHP).
- `assets/fonts/`: Place your `.ttf` or `.otf` font files here (e.g., `TH SarabunPSK.ttf`).
- `internal/`: Reserved for the standalone Python runtime.

## How to Run (Development)
Ensure you have the requirements installed in your environment:
```bash
pip install streamlit pandas geopandas plotly matplotlib
```
Then run the app:
```bash
streamlit run app.py
```

## How to use Custom Fonts
1. Download your preferred Thai font (e.g., TH SarabunPSK).
2. Copy the `.ttf` file into `assets/fonts/`.
3. Restart the application. The app will automatically detect and register the font for both the UI and the charts.

## Deployment
To create the standalone Windows executable, use the provided packaging scripts (Milestone 4).
