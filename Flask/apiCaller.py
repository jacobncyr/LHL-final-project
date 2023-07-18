import requests

class apiCaller:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = 'https://api.calorieninjas.com/v1/nutrition?query='

    def get_nutritional_info(self, query):
        api_call_url = self.api_url + query

        # Make the API GET request
        response = requests.get(api_call_url, headers={'X-Api-Key': self.api_key})

        # Check if the API call was successful
        if response.status_code == requests.codes.ok:
            # Parse the JSON response
            data = response.json()
            return data
        else:
            return f"Error: {response.status_code}, {response.text}"
import os

api_key = os.environ.get('API_KEY')

api_caller = apiCaller(api_key)

# Test the API call with a food item query
food_item_query = 'chicken sandwich'
nutritional_info = api_caller.get_nutritional_info(food_item_query)
print(nutritional_info)
