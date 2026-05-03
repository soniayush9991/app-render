# Autonomous Reliability Platform (ARP)

A lightweight Streamlit dashboard for simulating API service health signals, predicting root causes, and recommending actions for reliability management.

## Project Overview

This app simulates the health of three API services and uses a pre-trained model to detect root causes, calculate severity, and suggest remedial actions.

### Core capabilities
- Generate synthetic health metrics for `Payment API`, `Auth API`, and `Database API`
- Predict root cause and confidence using a saved ML model
- Calculate severity and health score for selected API data
- Generate incident summaries, alerts, and explanations
- Persist analyzed events to `logs.csv`

## Repository Structure

- `app.py` - Streamlit frontend and main application workflow
- `src/logger.py` - Logging helper for event persistence and safe log loading
- `src/model.py` - Model loading and prediction logic
- `src/simulator.py` - API simulation and cascading failure modeling
- `src/decision.py` - Decision logic for action selection, severity, alerts, and scoring
- `requirements.txt` - Python dependencies
- `model.pkl` - Serialized model artifact used for root cause prediction
- `logs.csv` - Event log file generated during analysis runs

## Setup

1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the app

```bash
streamlit run app.py
```

## Usage

1. Open the Streamlit app in your browser.
2. Select one of the API services from the dropdown.
3. Adjust the sliders for latency, CPU usage, and memory usage.
4. Click **Analyze System** to run the simulation and inspection.
5. Review predictive results, recommended actions, alerts, and the system health score.

## Notes

- The application uses `model.pkl` for root cause classification.
- Log events are saved to `logs.csv` using `src/logger.py`.
- The dashboard displays a simulated system state for all services while focusing analysis on the selected API.

## Future Improvements

- Add support for real telemetry ingestion instead of synthetic simulation
- Include historical trend visualization for logs and API health
- Improve root cause classification with richer signal models
- Add user controls for toggling cascading failure scenarios

## Contact

For questions or enhancements, update the repository or open an issue.
