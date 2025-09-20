# MLOps Pipeline for Iris Classification

This project demonstrates a complete, end-to-end MLOps pipeline for a simple machine learning model. The primary goal is to showcase the principles of CI/CD, containerization, and automation in a machine learning context.

## 🚀 Project Overview

This pipeline trains a **Random Forest Classifier** on the classic Iris dataset, packages the prediction logic into a **Flask API**, containerizes the entire application using **Docker**, and sets up a **CI/CD workflow with GitHub Actions** to automatically build and validate the Docker image on every code change.

This project serves as a foundational template for building more complex, production-ready MLOps systems.

## ✨ Core Features

- **Model Training**: A simple script (`train.py`) to train a classifier and save it using `joblib`.
- **REST API**: A Flask application (`app.py`) that loads the trained model and exposes a `/predict` endpoint for inference.
- **Containerization**: A `Dockerfile` that packages the application, model, and all dependencies into a portable Docker image.
- **CI/CD Automation**: A GitHub Actions workflow (`.github/workflows/main.yml`) that automatically triggers on a `git push` to the `main` branch to build the Docker image, ensuring the application is always in a deployable state.

## 🛠️ Tech Stack

- **Machine Learning**: Scikit-learn, Pandas, NumPy
- **Web Framework**: Flask, Gunicorn
- **Containerization**: Docker
- **CI/CD**: GitHub Actions

## 📋 How to Run Locally

### Prerequisites

- Python 3.9+
- Docker Desktop

### Steps

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/<Your-GitHub-Username>/<Your-Repository-Name>.git
    cd <Your-Repository-Name>
    ```

2.  **Train the Model:**
    (Optional, as a pre-trained model is already included)
    ```bash
    # Create and activate a virtual environment
    python -m venv venv
    source venv/bin/activate # On Windows: .\venv\Scripts\activate
    
    # Install dependencies and train
    pip install -r requirements.txt
    python train.py
    ```

3.  **Build the Docker Image:**
    ```bash
    docker build -t iris-predictor .
    ```

4.  **Run the Docker Container:**
    ```bash
    docker run -p 8080:8080 iris-predictor
    ```
    The application will now be running and listening on `http://localhost:8080`.

## 🔬 How to Test the API

You can test the running API using `curl` from a new terminal.

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  --data '{"input": [[5.1, 3.5, 1.4, 0.2]]}' \
  http://localhost:8080/predict
```

**Expected Response:**
```json
{
  "prediction": 0
}
```

## 🔄 CI/CD Pipeline

The Continuous Integration (CI) pipeline is defined in `.github/workflows/main.yml`. It triggers on every push to the `main` branch and performs the following steps:
1.  Checks out the repository code.
2.  Sets up Docker Buildx.
3.  Builds the Docker image to ensure that all code, dependencies, and configurations are correct and the application is buildable.

You can view the status of the workflows under the "Actions" tab of this repository.
