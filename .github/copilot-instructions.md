# Copilot Instructions for MLOps_Pipeline_Project

## Project Overview
This project is a minimal MLOps pipeline for serving a scikit-learn model via a Flask API. It includes model training, serialization, and a RESTful prediction endpoint. The project is containerized using Docker for production deployment.

## Key Components
- `train.py`: Trains a RandomForestClassifier on the Iris dataset and saves the model as `iris_model.joblib`.
- `app.py`: Flask app exposing two endpoints:
  - `/`: Health check and welcome message.
  - `/predict` (POST): Accepts JSON payload with `input` key (list of feature arrays), returns predicted class as JSON.
- `requirements.txt`: Python dependencies for both training and serving.
- `Dockerfile`: Containerizes the API using Gunicorn for production.
- `payload.json`: Example input for prediction requests.

## Developer Workflows
- **Training the Model:**
  - Run `train.py` to retrain and serialize the model: `python train.py`
- **Serving the API (local):**
  - Run `app.py` for development: `python app.py` (Flask dev server, port 5000)
- **Serving the API (Docker):**
  - Build and run the container:
    - `docker build -t iris-api .`
    - `docker run -p 8080:8080 iris-api`
- **Prediction Request Example:**
  - POST to `/predict` with JSON body from `payload.json`.

## Patterns & Conventions
- Model file path is hardcoded as `iris_model.joblib` in both training and serving scripts.
- Input payload for prediction must be a list of lists under the `input` key.
- API returns prediction as an integer class label.
- Gunicorn is used for production serving (see `Dockerfile`).
- No test suite or CI/CD scripts are present; add these if needed for your workflow.

## External Dependencies
- scikit-learn, Flask, joblib, numpy, gunicorn (see `requirements.txt`).
- Docker required for containerized deployment.

## Example Usage
- Training: `python train.py`
- Local API: `python app.py`
- Docker API: `docker build -t iris-api . && docker run -p 8080:8080 iris-api`
- Prediction: `curl -X POST -H "Content-Type: application/json" -d @payload.json http://localhost:5000/predict`

## Directory Structure
- `app.py`, `train.py`, `requirements.txt`, `Dockerfile`, `payload.json`, `iris_model.joblib` in project root.
- No custom submodules or complex service boundaries.

---
If any section is unclear or missing, please provide feedback for further refinement.
