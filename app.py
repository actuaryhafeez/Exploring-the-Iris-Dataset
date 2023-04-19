import pickle
import pandas as pd
import numpy as np
from flask import Flask, request, jsonify, render_template

# Load the saved model from a pickle file
model_file = 'model/iris_model.pkl'
with open(model_file, 'rb') as f:
    model = pickle.load(f)

# Create a Flask app instance
app = Flask(__name__)

# Define a function that takes in input data (in the form of a dictionary) and returns a prediction
def predict_species(input_data):
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df).tolist()[0]
    return prediction


# Define a route for the home page (/). In this route, we'll display a simple form that allows the user to input values for the four features of the Iris dataset (sepal length, sepal width, petal length, and petal width)
@app.route('/')
def home():
    return render_template('home.html')

# Define a route for the prediction endpoint (/predict)
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    prediction = predict_species(data)
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
