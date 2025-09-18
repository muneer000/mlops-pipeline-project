from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
import joblib

# Load a simple dataset
X, y = load_iris(return_X_y=True)

# Train a simple model
model = RandomForestClassifier()
model.fit(X, y)

# Save the trained model to a file
joblib.dump(model, 'iris_model.joblib')

print("✅ Model trained and saved as iris_model.joblib")