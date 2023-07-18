import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer  # Import SimpleImputer
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
        print("Input data:", data)
        # Remove the 'name' feature from the data
        data.pop('name', None)

        # Convert data to DataFrame
        data_df = pd.DataFrame([data])  # Wrap the data in a list

        # Handle missing values (NaN) using SimpleImputer with mean strategy
        imputer = SimpleImputer(strategy='mean')
        data_imputed = imputer.fit_transform(data_df)

        data_scaled = self.scaler.transform(data_imputed)
        print("Scaled data:", data_scaled)
        prediction = self.rf.predict(data_scaled)
        print("Prediction:", prediction)
        return prediction

    def evaluate_model(self, X, y):
        X_scaled = self.scaler.transform(X)
        y_pred = self.rf.predict(X_scaled)
        print("Confusion Matrix:")
        print(confusion_matrix(y, y_pred))
        print("Accuracy:", accuracy_score(y, y_pred))
