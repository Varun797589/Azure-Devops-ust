import joblib

# Function to save the trained model
def save_model(model, file_path):
    try:
        joblib.dump(model, file_path)
        print(f"Model saved successfully at {file_path}.")
    except Exception as e:
        print(f"Error saving model: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with the actual trained model and desired file path
    model_path = "random_forest_model.joblib"

    try:
        # Assuming the model is already trained and available as 'model'
        from train_random_forest import train_random_forest
        import pandas as pd

        # Example: Load training data and train the model
        X_train = pd.read_csv("path_to_X_train.csv")
        y_train = pd.read_csv("path_to_y_train.csv").squeeze()
        model = train_random_forest(X_train, y_train)

        # Save the model
        if model:
            save_model(model, model_path)
    except Exception as e:
        print(f"Error during model training or saving: {e}")