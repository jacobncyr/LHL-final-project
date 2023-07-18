from flask import Flask, render_template, request
from apiCaller import apiCaller
from modelMaker import FoodClassifier

app = Flask(__name__)

# model selection
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
        food_name = request.form['food_name']
        nutritional_info = api_caller.get_nutritional_info(food_name)

        if nutritional_info:
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
