import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report

# Function to classify logs and prioritize alerts
def classify_and_prioritize_logs(model, logs, alert_column):
    try:
        # Predict classifications
        predictions = model.predict(logs)
        logs['classification'] = predictions

        # Prioritize alerts based on classification
        logs['priority'] = logs['classification'].apply(lambda x: 'High' if x == 'critical' else 'Medium' if x == 'warning' else 'Low')

        print("Log classification and prioritization completed.")
        return logs
    except Exception as e:
        print(f"Error during log classification and prioritization: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Replace with the actual paths to your logs and trained model
    logs_path = "path_to_logs.csv"
    model_path = "random_forest_model.joblib"

    try:
        logs = pd.read_csv(logs_path)

        # Load the trained model
        model = joblib.load(model_path)

        # Classify logs and prioritize alerts
        classified_logs = classify_and_prioritize_logs(model, logs, alert_column='classification')
        if classified_logs is not None:
            classified_logs.to_csv("classified_logs.csv", index=False)
            print("Classified logs saved successfully.")
    except Exception as e:
        print(f"Error loading logs or model: {e}")