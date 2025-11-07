from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load model and scaler
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

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

        # Simplified feature subset matching trained model
        # Fill missing with zeros for simplicity
        features = np.array([[limit_bal, age, pay_0, pay_2,
                              0, 0, 0, 0,  # PAY_3–PAY_6
                              bill_amt1, 0, 0, 0, 0, 0,  # BILL_AMT2–6
                              pay_amt1, 0, 0, 0, 0, 0]])  # PAY_AMT2–6

        scaled = scaler.transform(features)
        prob = model.predict_proba(scaled)[0][1]
        
        # Determine risk level (1 = default, 0 = no default)
        pred_label = 1 if prob > 0.5 else 0

        return jsonify({
            "pred_label": pred_label,
            "pred_prob": float(prob)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
