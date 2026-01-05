import pandas as pd
import numpy as np

# Function to load logs
def load_logs(file_path):
    try:
        logs = pd.read_csv(file_path)
        print("Logs loaded successfully.")
        return logs
    except Exception as e:
        print(f"Error loading logs: {e}")
        return None

# Function to clean and preprocess data
def preprocess_data(logs):
    try:
        # Drop duplicates
        logs = logs.drop_duplicates()

        # Handle missing values
        logs = logs.fillna(method='ffill')

        # Example: Convert timestamp to datetime
        if 'timestamp' in logs.columns:
            logs['timestamp'] = pd.to_datetime(logs['timestamp'], errors='coerce')

        # Add a 'scam_label' column based on 'call_type'
        if 'call_type' in logs.columns:
            logs['scam_label'] = logs['call_type'].apply(lambda x: 1 if x == 'spam' else 0)

        # Save the preprocessed logs to a CSV file
        logs.to_csv('preprocessed_logs.csv', index=False)
        print("Preprocessed logs saved to 'preprocessed_logs.csv'.")

        print("Data preprocessing completed.")
        return logs
    except Exception as e:
        print(f"Error preprocessing data: {e}")
        return None

# Example usage
if __name__ == "__main__":
    file_path = "logs.csv"  # Updated to use a valid file path for the logs
    logs = load_logs(file_path)
    if logs is not None:
        preprocessed_logs = preprocess_data(logs)
        print(preprocessed_logs.head())