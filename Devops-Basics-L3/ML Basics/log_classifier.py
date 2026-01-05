"""
Log Classifier for DevOps

This script demonstrates how to build a log classifier using machine learning. The classifier categorizes logs into different categories such as INFO, WARNING, and ERROR.
"""

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib

# Step 1: Load and Prepare Data
def load_data():
    """Simulate loading log data."""
    data = {
        'log_message': [
            'System started successfully',
            'Disk space running low',
            'Error connecting to database',
            'User logged in',
            'Memory usage is high',
            'File not found error',
            'Backup completed successfully',
            'CPU temperature is critical',
            'Network latency detected',
            'Unauthorized access attempt'
        ],
        'log_category': ['INFO', 'WARNING', 'ERROR', 'INFO', 'WARNING', 'ERROR', 'INFO', 'WARNING', 'WARNING', 'ERROR']
    }
    return pd.DataFrame(data)

# Step 2: Preprocess Data
def preprocess_data(df):
    """Convert text data into numerical features."""
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df['log_message'])
    y = df['log_category']
    return X, y, vectorizer

# Step 3: Train the Model
def train_model(X, y):
    """Train a Random Forest Classifier."""
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model, X_test, y_test

# Step 4: Evaluate the Model
def evaluate_model(model, X_test, y_test):
    """Evaluate the model's performance."""
    y_pred = model.predict(X_test)
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

# Step 5: Save the Model and Vectorizer
def save_artifacts(model, vectorizer):
    """Save the trained model and vectorizer for future use."""
    joblib.dump(model, 'log_classifier_model.pkl')
    joblib.dump(vectorizer, 'log_vectorizer.pkl')

# Step 6: Load and Predict New Logs
def predict_new_logs(logs):
    """Predict categories for new log messages."""
    model = joblib.load('log_classifier_model.pkl')
    vectorizer = joblib.load('log_vectorizer.pkl')
    logs_vectorized = vectorizer.transform(logs)
    predictions = model.predict(logs_vectorized)
    return predictions

# Step 7: Load Real DevOps Logs
def load_real_logs():
    """Load real DevOps logs for classification."""
    real_logs = [
        '2026-01-02 12:00:01 INFO: Deployment started successfully.',
        '2026-01-02 12:05:23 WARNING: Disk space usage exceeded 80%.',
        '2026-01-02 12:10:45 ERROR: Failed to connect to the database.',
        '2026-01-02 12:15:12 INFO: Health check passed for all services.',
        '2026-01-02 12:20:33 WARNING: High memory usage detected.',
        '2026-01-02 12:25:50 ERROR: Application crashed due to unhandled exception.'
    ]
    return real_logs

if __name__ == "__main__":
    # Load and preprocess data
    df = load_data()
    X, y, vectorizer = preprocess_data(df)

    # Train the model
    model, X_test, y_test = train_model(X, y)

    # Evaluate the model
    evaluate_model(model, X_test, y_test)

    # Save the model and vectorizer
    save_artifacts(model, vectorizer)

    # Predict new logs
    new_logs = load_real_logs()
    predictions = predict_new_logs(new_logs)

    for log, category in zip(new_logs, predictions):
        print(f"Log: {log} => Category: {category}")