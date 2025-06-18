import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib
import os

print("🔥 Script started...")

# Create models folder if not exists
os.makedirs("models", exist_ok=True)

print("📁 Models folder ready")

# Dummy diabetes data
print("📊 Preparing diabetes data...")
diabetes_data = pd.DataFrame({
    'Age': [25, 35, 45, 50, 60],
    'BMI': [18.5, 24.2, 30.5, 28.4, 33.2],
    'Glucose': [90, 110, 150, 140, 180],
    'BloodPressure': [70, 80, 85, 90, 88],
    'Diabetes': [0, 0, 1, 1, 1]
})

X_d = diabetes_data.drop('Diabetes', axis=1)
y_d = diabetes_data['Diabetes']

model_d = LogisticRegression()
model_d.fit(X_d, y_d)

print("✅ Diabetes model trained!")

joblib.dump(model_d, "models/diabetes_model.pkl")
print("💾 Saved diabetes_model.pkl")

# Dummy heart data
print("📊 Preparing heart data...")
heart_data = pd.DataFrame({
    'Age': [30, 40, 50, 60, 70],
    'BMI': [22.0, 26.1, 29.5, 31.0, 35.2],
    'BloodPressure': [72, 82, 88, 91, 95],
    'HeartDisease': [0, 0, 1, 1, 1]
})

X_h = heart_data.drop('HeartDisease', axis=1)
y_h = heart_data['HeartDisease']

model_h = LogisticRegression()
model_h.fit(X_h, y_h)

print("✅ Heart model trained!")

joblib.dump(model_h, "models/heart_model.pkl")
print("💾 Saved heart_model.pkl")
