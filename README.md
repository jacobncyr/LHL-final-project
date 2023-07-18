Final Project - Food nutrition classificaiton.

**Project Description**: This project implements a Flask web application that utilizes a machine learning model to perform text recognition from images. It provides an easy-to-use API for extracting text from images and demonstrates the functionality through a web server.

## Requirements

- Python 3.x
- Flask
- scikit-learn
## Installation

1. Clone the repository to your local machine:

git clone https://github.com/your-username/project-name.git

Usage
Launch the Flask server:

python main.py

Once the server is running, you can access the web application by navigating to http://localhost:5000 in your web browser.

To test the text recognition from images functionality, run the following command:

python imagetoapi.py
This will process the specified image file and display the extracted text.

API Endpoints

/: Home page of the web application.
/imagetoapi: Accepts POST requests with an image file and returns the extracted text from the image.
Configuration
You can configure the project settings in the config.py file. This includes changing the host, port, or any other Flask configurations.

Acknowledgments
Thanks to Calorie ninjas for making this alot faster and doable. Their API was a huge help in my process.
cs
