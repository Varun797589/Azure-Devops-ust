import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report
import joblib

# Function to evaluate model performance
def evaluate_model(model, X_test, y_test):
    try:
        # Ensure test features match training features
        X_test = X_test.select_dtypes(include=['number'])

        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred, average='weighted')
        recall = recall_score(y_test, y_pred, average='weighted')

        print("Model Evaluation:")
        print(f"Accuracy: {accuracy:.2f}")
        print(f"Precision: {precision:.2f}")
        print(f"Recall: {recall:.2f}")
        print("\nClassification Report:\n")
        print(classification_report(y_test, y_pred))

        return accuracy, precision, recall
    except Exception as e:
        print(f"Error during model evaluation: {e}")
        return None, None, None

# Example usage
if __name__ == "__main__":
    # Replace with the actual paths to your test datasets and model
    X_test_path = "X_test.csv"
    y_test_path = "y_test.csv"
    model_path = "random_forest_model.joblib"

    try:
        X_test = pd.read_csv(X_test_path)
        y_test = pd.read_csv(y_test_path).squeeze()  # Ensure y_test is a Series

        # Ensure y_test is properly formatted as an array-like structure
        y_test = pd.Series(y_test) if not isinstance(y_test, pd.Series) else y_test

        # Load the trained model
        model = joblib.load(model_path)

        # Evaluate the model
        evaluate_model(model, X_test, y_test)
    except Exception as e:
        print(f"Error loading test data or model: {e}")