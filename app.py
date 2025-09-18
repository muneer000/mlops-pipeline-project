# app.py
from flask import Flask, request, jsonify
import joblib
import numpy as np

# Initialize the Flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load('iris_model.joblib')

@app.route('/')
def home():
    return "Welcome to the Iris Model API! Use the /predict endpoint to get predictions."
@app.route('/predict', methods=['POST'])
def predict():
    # Get data from the POST request
    data = request.get_json(force=True)
    
    # Make a prediction
    prediction = model.predict(np.array(data['input']))
    
    # Return the prediction as JSON
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(port=5000, debug=True)