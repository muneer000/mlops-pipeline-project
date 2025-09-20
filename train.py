# train.py (Version 2 - with MLflow Integration)
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import mlflow # <-- Import MLflow

# 1. Start an MLflow run
# MLflow will automatically log to a local 'mlruns' directory.
with mlflow.start_run():
    
    print("--- Starting a new MLflow run ---")

    # 2. Load Data
    X, y = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 3. Define and log hyperparameters
    n_estimators = 150
    max_depth = 10
    mlflow.log_param("n_estimators", n_estimators)
    mlflow.log_param("max_depth", max_depth)
    
    # 4. Train the model
    model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
    model.fit(X_train, y_train)

    # 5. Evaluate the model and log metrics
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    mlflow.log_metric("accuracy", accuracy)

    print(f"\nModel Accuracy: {accuracy:.4f}")
    
    # 6. Log the trained model as an "artifact"
    model_path = 'iris_model.joblib'
    joblib.dump(model, model_path)
    mlflow.sklearn.log_model(model, "iris-random-forest-model")
    
    print(f"\n✅ Model trained and logged to MLflow with accuracy: {accuracy:.4f}")