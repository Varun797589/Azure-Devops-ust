import pandas as pd
from sklearn.model_selection import train_test_split

# Function to split data into training and testing datasets
def train_test_split_data(data, target_column, test_size=0.2, random_state=42):
    try:
        X = data.drop(columns=[target_column])
        y = data[target_column]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
        print("Train-test split completed.")
        
        # Save training and testing datasets to CSV files
        X_train.to_csv('X_train.csv', index=False)
        X_test.to_csv('X_test.csv', index=False)
        y_train.to_csv('y_train.csv', index=False)
        y_test.to_csv('y_test.csv', index=False)
        print("Training and testing datasets saved as CSV files.")
        
        return X_train, X_test, y_train, y_test
    except Exception as e:
        print(f"Error during train-test split: {e}")
        return None, None, None, None

# Example usage
if __name__ == "__main__":
    # Replace with the actual path to your preprocessed logs
    preprocessed_file_path = "preprocessed_logs.csv"  # Updated to use a valid file path
    target_column = "scam_label"  # Updated to use the actual target column name
    try:
        preprocessed_logs = pd.read_csv(preprocessed_file_path)
        X_train, X_test, y_train, y_test = train_test_split_data(preprocessed_logs, target_column)
        print("Training and testing datasets are ready.")
    except Exception as e:
        print(f"Error loading preprocessed logs: {e}")