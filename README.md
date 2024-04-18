# Disease Prediction and Advisory System

This project is a web application built using Flask for predicting diseases based on user-input symptoms and providing comprehensive advisory information akin to a doctor's consultation.

## Features
1. Symptom Prediction: Users can input their symptoms, and the system predicts the most likely disease using a pre-trained machine learning model.
   
2. Comprehensive Advisory: Upon predicting the disease, the system provides detailed information including disease description, precautions, recommended medications, workout plans, and dietary advice.
   
3. Interactive Interface: The web application provides an interactive interface for users to input symptoms and receive personalized advisory information.
   
## Technologies Used
1. Flask: Used for building the web application backend.
   
2. Pandas and NumPy: Utilized for data manipulation and preprocessing.
   
3. LightGBM: Employed for the machine learning model for disease prediction.
   
4. HTML/CSS: Used for frontend development and styling.
   
## Usage
To run the application locally:

Install the required dependencies by running pip install -r requirements.txt.
Run the application using python app.py.
Access the application through a web browser at http://localhost:5000.

## Routes
/: Homepage of the application.
/predict: Endpoint for predicting diseases based on user-input symptoms.
/home, /about, /blog, /contact, /developer: Additional pages for information and contact details.

## Contributing
Contributions are welcome! Feel free to open issues or pull requests for any enhancements or bug fixes.

##License
This project is licensed under the MIT License.

## Techstack Used 
flask

scikit-learn==1.3.2

lightgbm==4.3.0

pandas 

numpy

## Links
    Kaggle Dataset Link : https://www.kaggle.com/datasets/noorsaeed/medicine-recommendation-system-dataset
    
    bootstrap link : https://getbootstrap.com/
