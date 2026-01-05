import pandas as pd
import joblib

# Function to make predictions on fresh logs
def log_predictions(model, fresh_logs, output_path):
    try:
        # Ensure fresh logs match training features
        fresh_logs = fresh_logs.select_dtypes(include=['number'])

        predictions = model.predict(fresh_logs)
        fresh_logs['predictions'] = predictions
        fresh_logs.to_csv(output_path, index=False)
        print(f"Predictions logged successfully at {output_path}.")
    except Exception as e:
        print(f"Error during prediction logging: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with the actual paths to your fresh logs and trained model
    fresh_logs_path = "X_test.csv"
    model_path = "random_forest_model.joblib"
    output_path = "predicted_logs.csv"

    try:
        fresh_logs = pd.read_csv(fresh_logs_path)

        # Load the trained model
        model = joblib.load(model_path)

        # Log predictions
        log_predictions(model, fresh_logs, output_path)
    except Exception as e:
        print(f"Error loading fresh logs or model: {e}")