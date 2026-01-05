from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load("random_forest_model.joblib")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse input JSON data
        data = request.get_json()
        df = pd.DataFrame(data)

        # Make predictions
        predictions = model.predict(df)
        return jsonify(predictions.tolist())
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)