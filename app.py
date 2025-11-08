from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import os
import sys

app = Flask(__name__)

# Load model and scaler from model directory
model_path = os.path.join('model', 'model.pkl')
scaler_path = os.path.join('model', 'scaler.pkl')

# Check if model files exist
if not os.path.exists(model_path) or not os.path.exists(scaler_path):
    print(f"❌ Error: Model files not found!")
    print(f"   Expected: {os.path.abspath(model_path)}")
    print(f"   Expected: {os.path.abspath(scaler_path)}")
    print(f"\n📝 To create the model, run:")
    print(f"   python model/train_model.py")
    sys.exit(1)

try:
    model = pickle.load(open(model_path, 'rb'))
    scaler = pickle.load(open(scaler_path, 'rb'))
    print("✅ Model and Scaler loaded successfully!")
except Exception as e:
    print(f"❌ Error loading model files: {e}")
    sys.exit(1)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Read user input
        limit_bal = float(request.form['limit_bal'])
        age = int(request.form['age'])
        pay_0 = int(request.form['pay_0'])
        pay_2 = int(request.form['pay_2'])
        bill_amt1 = float(request.form['bill_amt1'])
        pay_amt1 = float(request.form['pay_amt1'])

        # Create feature array matching trained model features
        features = np.array([[limit_bal, age, pay_0, pay_2,
                              0, 0, 0, 0,  # PAY_3–PAY_6
                              bill_amt1, 0, 0, 0, 0, 0,  # BILL_AMT2–6
                              pay_amt1, 0, 0, 0, 0, 0]])  # PAY_AMT2–6

        # Transform features using scaler (without feature names)
        scaled = scaler.transform(features)
        
        # Make prediction
        prob = model.predict_proba(scaled)[0][1]
        
        # Determine risk level (1 = default, 0 = no default)
        pred_label = 1 if prob > 0.5 else 0

        return jsonify({
            "pred_label": pred_label,
            "pred_prob": float(prob)
        })

    except ValueError as e:
        return jsonify({"error": f"Invalid input values: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
