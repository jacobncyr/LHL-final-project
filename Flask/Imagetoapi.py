import requests
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
import joblib

class FoodClassifier:
    def __init__(self):
        self.rf = RandomForestClassifier(n_estimators=1, random_state=42)
        self.scaler = StandardScaler()

    def load_model(self, model_filename, scaler_filename):
        # Load the RandomForestClassifier and StandardScaler from the given filenames
        self.rf = joblib.load(model_filename)
        self.scaler = joblib.load(scaler_filename)

    def predict_health_classification(self, data):
        # Remove the 'name' feature from the data
        data.pop('name', None)

        # Convert data to DataFrame
        data_df = pd.DataFrame([data])  # Wrap the data in a list

        # Handle missing values (NaN) using SimpleImputer with mean strategy
        imputer = SimpleImputer(strategy='mean')
        data_imputed = imputer.fit_transform(data_df)

        data_scaled = self.scaler.transform(data_imputed)
        prediction = self.rf.predict(data_scaled)
        return prediction

# Initialize the API caller with your API key
api_key = 'yNGmkJtBl5ELYjPvQ1lSQA==fa0rJcexFJQvUYuC'
api_url = 'https://api.calorieninjas.com/v1/imagetextnutrition'

# Prepare the API request headers
headers = {'X-Api-Key': api_key}

# File paths for images
image_paths = ['../data/salad.jpg', '../data/pizzahut.png']

for image_path in image_paths:
    with open(image_path, 'rb') as file:
        # Prepare the payload for the API POST request
        files = {'file': (image_path, file, 'image/jpeg')}
        # Make the API POST request
        response = requests.post(api_url, headers=headers, files=files)

    # Check if the API call was successful
    if response.status_code == requests.codes.ok:
        # Parse the JSON response
        data = response.json()
        nutritional_info = data['items'][0]

        # Extract the food item name
        food_item_name = nutritional_info['name']

        # Load the model and make predictions
        model_filename = 'model.joblib'
        scaler_filename = 'scaler.joblib'
        classifier = FoodClassifier()
        classifier.load_model(model_filename, scaler_filename)

        # Make the prediction using your FoodClassifier model
        prediction = classifier.predict_health_classification(nutritional_info)

        # Process the prediction result
        result_text = "Healthy" if prediction[0] == 1 else "Not Healthy"
        result = f"The food item detected in '{image_path}' is '{food_item_name}', and it is classified as '{result_text}'."
        print(result)
    else:
        print(f"Error: Could not retrieve utrition information from the image '{image_path}'.")