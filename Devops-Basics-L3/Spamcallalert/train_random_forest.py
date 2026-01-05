import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Function to train a Random Forest model
def train_random_forest(X_train, y_train, n_estimators=100, random_state=42):
    try:
        model = RandomForestClassifier(n_estimators=n_estimators, random_state=random_state)
        model.fit(X_train, y_train)
        print("Random Forest model training completed.")
        return model
    except Exception as e:
        print(f"Error training Random Forest model: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Replace with the actual paths to your training datasets
    X_train_path = "X_train.csv"
    y_train_path = "y_train.csv"

    try:
        X_train = pd.read_csv(X_train_path)
        y_train = pd.read_csv(y_train_path).squeeze()  # Ensure y_train is a Series

        # Ensure all features are numeric
        X_train = X_train.select_dtypes(include=['number'])

        # Train the Random Forest model
        model = train_random_forest(X_train, y_train)

        # Save the model
        if model:
            joblib.dump(model, "random_forest_model.joblib")
            print("Model saved as random_forest_model.joblib.")
    except Exception as e:
        print(f"Error loading training data: {e}")