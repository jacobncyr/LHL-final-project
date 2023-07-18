from flask import Flask, render_template, request
from apiCaller import apiCaller
from modelMaker import FoodClassifier

app = Flask(__name__)

# Create an instance of the FoodClassifier class
# Replace 'model.joblib' and 'scaler.joblib' with the paths to your model and scaler files
model_filename = 'model.joblib'
scaler_filename = 'scaler.joblib'
classifier = FoodClassifier()
classifier.load_model(model_filename, scaler_filename)

import os

api_key = os.environ.get('API_KEY')
api_caller = apiCaller(api_key)


# Home route
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the food name from the form
        food_name = request.form['food_name']

        # Make the API call and get nutritional information
        nutritional_info = api_caller.get_nutritional_info(food_name)

        if nutritional_info:
            # Make the prediction using your FoodClassifier model
            prediction = classifier.predict_health_classification(nutritional_info['items'][0])
            result_text = "Healthy" if prediction[0] == 1 else "Not Healthy"
            result = f"The food item '{food_name}' is classified as '{result_text}'."
        else:
            result = f"Error: No nutritional information found for '{food_name}'."

        return render_template('index.html', classification_result=result)

    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
