# 🛡️ HealthShield AI

**HealthShield AI** is a lightweight health risk prediction web application built with **Flask** and **Logistic Regression models**. It allows users to assess their risk of **Diabetes** and **Heart Disease** based on basic health metrics.

## 💡 Key Features

- 🔍 Predicts **Diabetes** and **Heart Disease** risk
- 🧠 Uses **Logistic Regression** with dummy medical data
- 🖥️ Simple and responsive web interface (Flask + HTML)
- 📋 Gives **personalized health suggestions** based on results
- 🔐 Clean, offline, and beginner-friendly project

---

## 🚀 How It Works

1. User inputs:
   - Age
   - BMI
   - Glucose (for diabetes)
   - Blood Pressure
   - Risk Type (Diabetes or Heart)

2. Flask processes the data and loads trained `.pkl` models

3. Model predicts and returns:
   - ✅ If you're safe
   - ⚠️ If you're at high risk

4. Personalized **health tips** shown based on prediction

---

## 🛠️ Tech Stack
---------------------------------------------------
| Layer       | Technology                         |
|-------------|------------------------------------|
| Backend     | Python, Flask                      |
| ML Models   | scikit-learn (Logistic Regression) |
| Frontend    | HTML, CSS (optional Bootstrap)     |
| Model Saving | `joblib`                          |
---------------------------------------------------
## 📁 Folder Structure

HealthShield/
├── app.py # Flask app
├── train_model.py # ML model training
├── models/
│ ├── diabetes_model.pkl
│ └── heart_model.pkl
├── templates/
│ ├── index.html
│ └── result.html
└── static/ (optional for CSS)

## 📦 Installation & Run

```bash
# Clone this repo
git clone https://github.com/yourusername/HealthShieldAI
cd HealthShieldAI

# Create virtual environment (optional)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
