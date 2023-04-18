# Exploring the Iris Dataset: A Classic Example of Supervised Learning and Data Visualization
The Iris dataset is a popular dataset used in machine learning and statistics. It contains measurements of the sepal length, sepal width, petal length, and petal width for three species of Iris flowers: Iris setosa, Iris versicolor, and Iris virginica. The dataset consists of 150 observations, with 50 observations for each species.

The Iris dataset is often used as a classic example of supervised learning, as the goal is to predict the species of the flower based on its measurements. It is also used for data visualization and clustering.

The Iris dataset is available in many machine learning libraries and can be easily accessed through Python or R. It is a well-studied dataset and is often used as a benchmark to evaluate the performance of new algorithms.

# Description
This project contains a logistic regression model trained on the Iris dataset, which includes measurements for the sepal length, sepal width, petal length, and petal width of three different species of iris flowers (setosa, versicolor, and virginica).

The logistic regression model is used to predict the species of an iris flower based on its measurements, with an accuracy of approximately 95%. The model was trained using scikit-learn, a popular machine learning library in Python.

The purpose of this project is to demonstrate the use of logistic regression for classification tasks, as well as provide an example of how to build a simple Flask application for deploying a machine learning model.

# Installation
## To install and run this application, follow these steps:

### Clone the repository to your local machine.
    https://github.com/actuaryhafeez/Exploring-the-Iris-Dataset.git
### Create a new virtual environment in the project directory.
    python3 -m venv venv
### Activate the virtual environment.
    source venv/bin/activate
### Install the necessary dependencies by running the command 
    pip install -r requirements.txt.
### Start the Flask server by running the command python app.py in the terminal.
    flask run
### Open a web browser and navigate to http://localhost:5000 to access the home page of the application.
### Enter the measurements for an iris flower in the form and click "Predict" to see the predicted species.
