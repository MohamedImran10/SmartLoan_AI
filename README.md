# 💳 Credit Default Prediction AI

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.2-green.svg)](https://flask.palletsprojects.com/)
[![Machine Learning](https://img.shields.io/badge/ML-scikit--learn-orange.svg)](https://scikit-learn.org/)

## 🧠 Project Overview

**Credit Default Prediction AI** is an intelligent machine learning application that assesses whether a credit card client is likely to default on their next payment. This tool helps financial institutions make data-driven decisions about credit approvals and risk management.

The application uses advanced machine learning algorithms trained on the **"Default of Credit Card Clients"** dataset from Taiwan, one of the most comprehensive credit default datasets available.

### 🎯 What This App Does

| Risk Level | Status | Meaning |
|-----------|--------|---------|
| ✅ **LOW RISK** | Green Badge | Client likely to repay on time |
| ⚠️ **MEDIUM RISK** | Yellow Badge | Client may delay repayment |
| 🚨 **HIGH RISK** | Red Badge | Client likely to default |

### 💼 Business Value

- **For Banks**: Automated risk assessment to approve/deny credit increases and loans
- **For Customers**: Real-time understanding of their credit health
- **For Businesses**: Reduce default losses through predictive analytics

---

## ✨ Features

### 🎨 Modern, Intuitive UI
- Beautiful gradient background with cyan-to-blue theme
- Responsive design that works on desktop, tablet, and mobile
- Smooth animations and real-time visual feedback
- Organized form sections with icons for easy data entry

### 🤖 Intelligent Predictions
- Trained Random Forest model for accurate default prediction
- Feature scaling for optimal model performance
- Confidence scores with animated progress meters
- Instant risk assessment

### 📊 Detailed Risk Analysis
- Risk percentage display
- Color-coded badges for quick interpretation
- Descriptive insights about prediction
- JSON-based API for easy integration

### ⚡ Fast & Reliable
- Sub-second prediction time
- Robust error handling
- Comprehensive logging
- Production-ready architecture

---

## 🛠️ Tech Stack

### Backend
- **Flask** (2.3.2) - Web framework
- **scikit-learn** (1.5.2) - Machine learning
- **pandas** (2.2.3) - Data processing
- **numpy** (1.26.4) - Numerical computing
- **joblib** (1.3.2) - Model serialization

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Modern styling with gradients and animations
- **Bootstrap 5** - Responsive grid system
- **Font Awesome 6.4** - Icon library
- **Vanilla JavaScript** - Client-side logic

---

## 📋 Input Features

The model accepts the following credit-related parameters:

| Feature | Description | Example |
|---------|-------------|---------|
| **LIMIT_BAL** | Credit Limit Amount | $50,000 |
| **AGE** | Client's Age | 30 years |
| **PAY_0** | Current Repayment Status | 0 (on time) |
| **PAY_2** | Previous Month Status | 0 (on time) |
| **BILL_AMT1** | Current Bill Amount | $10,000 |
| **PAY_AMT1** | Payment Made | $5,000 |

### 📊 Output

```json
{
  "pred_label": 0,
  "pred_prob": 0.15
}
```

- **pred_label**: 0 (No Default) or 1 (Default)
- **pred_prob**: Probability of default (0.0 - 1.0)

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
   ```bash
   cd SmartLoan_AI
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure model files exist**
   ```
   SmartLoan_AI/
   ├── model/
   │   ├── model.pkl       # Trained ML model
   │   └── scaler.pkl      # Feature scaler
   └── ...
   ```

### Running the Application

1. **Start the Flask server**
   ```bash
   python app.py
   ```

2. **Open in browser**
   ```
   http://localhost:5000
   ```

3. **Fill in the form** and click "Predict Default Risk"

---

## 📁 Project Structure

```
SmartLoan_AI/
├── app.py                          # Flask application entry point
├── requirements.txt                # Python dependencies
├── Procfile                        # Deployment configuration
├── default of credit card clients.xls # Training dataset
│
├── model/
│   ├── train_model.py              # Model training script
│   ├── model.pkl                   # Trained ML model
│   └── scaler.pkl                  # Feature scaler
│
└── templates/
    └── index.html                  # Frontend UI (HTML + CSS + JS)
```

### Key Files

| File | Purpose |
|------|---------|
| `app.py` | Main Flask application with API endpoints |
| `index.html` | Beautiful frontend with form and results display |
| `model.pkl` | Pre-trained Random Forest classifier |
| `scaler.pkl` | Fitted StandardScaler for feature normalization |
| `train_model.py` | Script to retrain the model with new data |

---

## 🔌 API Endpoints

### GET `/`
Returns the main UI page.

**Response**: HTML page with interactive form

---

### POST `/predict`
Predicts credit default risk based on input features.

**Request Body** (Form Data):
```
limit_bal: float
age: int
pay_0: int
pay_2: int
bill_amt1: float
pay_amt1: float
```

**Response** (JSON):
```json
{
  "pred_label": 0,
  "pred_prob": 0.25
}
```

**Error Response**:
```json
{
  "error": "Invalid input: message here"
}
```

---

## 🧮 How the Model Works

### Algorithm
- **Model Type**: Random Forest Classifier
- **Training Data**: Taiwan Credit Card Default Dataset
- **Classes**: 2 (Default / No Default)

### Prediction Process

1. User inputs 6 key features
2. Features are scaled using StandardScaler
3. Model generates prediction probability
4. Probability is classified as:
   - **0 (Low Risk)**: prob < 0.5
   - **1 (High Risk)**: prob ≥ 0.5
5. Results displayed with confidence percentage

### Model Performance
- Trained on real credit card client data
- Handles missing features gracefully
- Optimized for financial decision-making

---

## 📊 Prediction Logging

When predictions are made, they are automatically logged to `predictions_log.csv`:

```csv
timestamp,limit_bal,age,pay_0,pay_2,bill_amt1,pay_amt1,pred_label,pred_prob
2025-11-07T10:30:45.123456,50000,30,0,0,10000,5000,0,0.15
```

This enables:
- Model monitoring and validation
- Historical analysis
- Performance tracking
- Audit trails

**Note**: The log file is generated automatically on first prediction and stored locally.

---

## 🎨 UI Features

### Form Design
- **Organized Sections**: Personal → Financial → Loan Details
- **Icon Integration**: Font Awesome icons for visual scanning
- **Input Validation**: Real-time feedback on form fields
- **Mobile Responsive**: Optimized for all screen sizes

### Results Display
- **Animated Progress Bar**: Shows default probability
- **Color-Coded Badge**: Green (Safe) / Red (Risk)
- **Smooth Transitions**: Professional animations
- **Auto-Scroll**: Results appear below form

### Color Scheme
- **Primary**: Cyan (#0ea5e9) → Blue (#06b6d4)
- **Success**: Emerald Green (#10b981)
- **Danger**: Rose Red (#f43f5e)
- **Warning**: Amber (#f59e0b)

---

## 🚀 Deployment

### Deploy to Heroku

1. **Create Procfile** (already included)
   ```
   web: python app.py
   ```

2. **Push to Heroku**
   ```bash
   git push heroku main
   ```

3. **Access your app**
   ```
   https://your-app-name.herokuapp.com
   ```

### Deploy to AWS/Azure/GCP

The app is containerizable and works with any platform supporting Python/Flask.

---

## 📈 Usage Example

### Via Web UI
1. Navigate to `http://localhost:5000`
2. Fill in client information
3. Click "Predict Default Risk"
4. View results instantly

### Via API (cURL)
```bash
curl -X POST http://localhost:5000/predict \
  -d "limit_bal=50000" \
  -d "age=30" \
  -d "pay_0=0" \
  -d "pay_2=0" \
  -d "bill_amt1=10000" \
  -d "pay_amt1=5000"
```

### Via Python
```python
import requests

data = {
    'limit_bal': 50000,
    'age': 30,
    'pay_0': 0,
    'pay_2': 0,
    'bill_amt1': 10000,
    'pay_amt1': 5000
}

response = requests.post('http://localhost:5000/predict', data=data)
result = response.json()
print(f"Risk Level: {result['pred_label']}")
print(f"Probability: {result['pred_prob']:.2%}")
```

---

## 🔍 Troubleshooting

### Problem: "Network Error - Failed to connect to server"

**Solution**: Make sure Flask is running
```bash
python app.py
# Should show: Running on http://0.0.0.0:5000
```

### Problem: "Error: model.pkl not found"

**Solution**: Ensure model files are in the `model/` directory
```bash
ls model/
# Should show: model.pkl and scaler.pkl
```

### Problem: "Invalid input" error

**Solution**: Check that all form fields are filled with valid numbers

---

## 📚 Model Training

To retrain the model with new data:

```bash
python model/train_model.py
```

This script:
- Loads training data
- Prepares features and target
- Trains Random Forest model
- Saves model and scaler
- Generates performance metrics

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## 📄 License

This project is open source and available on GitHub. For more information about licensing, please contact the repository owner.

---

## 📞 Support

- **Documentation**: See README.md
- **Issues**: Check GitHub Issues
- **Questions**: Open a discussion

---

## 🙌 Acknowledgments

- **Dataset**: "Default of Credit Card Clients" - UCI Machine Learning Repository
- **Framework**: Flask web framework
- **ML Library**: scikit-learn
- **UI Inspiration**: Modern fintech applications

---

## 🔐 Privacy & Security

- Predictions are logged locally for audit trails
- Model runs locally on your server
- No third-party API calls required
- Data handling follows best practices

---

## 📊 Dataset Information

**Source**: UCI Machine Learning Repository  
**Samples**: 30,000 credit card clients  
**Features**: 23 behavioral variables  
**Target**: Default payment (Yes/No)  
**Time Period**: April 2005 to September 2005

---

## 🎓 Technical Details

### Feature Engineering
The model uses the following engineered features:
- Repayment status history (6 months)
- Bill amounts (6 months)
- Payment amounts (6 months)
- Age and credit limit
- Total amount of previous consumption

### Model Optimization
- Feature scaling with StandardScaler
- Hyperparameter tuning for Random Forest
- Class imbalance handling
- Cross-validation for robustness

---
<<<<<<< HEAD

**Made with ❤️ by MohamedImran10** | Last Updated: November 8, 2025
=======
>>>>>>> d5a68593c9c1fc5422e1497ca131bd479b4f703f
