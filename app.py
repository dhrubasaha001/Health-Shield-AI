from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)

# Load ML models
diabetes_model = joblib.load("models/diabetes_model.pkl")
heart_model = joblib.load("models/heart_model.pkl")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Safely fetch values with defaults
        age = int(request.form.get('age', 0))
        bmi = float(request.form.get('bmi', 0))
        glucose = float(request.form.get('glucose', 0))
        bp = float(request.form.get('bp', 0))
        risk_type = request.form.get('risk_type')

        result = "❌ Invalid risk type selected."
        suggestions = []

        if risk_type == 'diabetes':
            input_data = [[age, bmi, glucose, bp]]
            prediction = diabetes_model.predict(input_data)[0]

            if prediction == 1:
                result = "⚠️ High Risk of Diabetes. Please consult a doctor."
                suggestions = [
                    "Reduce sugar and refined carb intake",
                    "Exercise for at least 30 minutes daily",
                    "Drink more water and avoid sugary drinks",
                    "Ensure 7–8 hours of sleep",
                    "Get blood sugar levels checked regularly"
                ]
            else:
                result = "✅ You are likely safe from Diabetes."
                suggestions = [
                    "Maintain a healthy balanced diet",
                    "Stay active and hydrated",
                    "Monitor blood sugar occasionally"
                ]

        elif risk_type == 'heart':
            input_data = [[age, bmi, bp]]
            prediction = heart_model.predict(input_data)[0]

            if prediction == 1:
                result = "⚠️ High Risk of Heart Disease. Stay alert!"
                suggestions = [
                    "Avoid fried and high-cholesterol foods",
                    "Stay physically active and manage stress",
                    "Don’t smoke or consume alcohol",
                    "Monitor blood pressure and cholesterol levels regularly"
                ]
            else:
                result = "✅ You are likely safe from Heart Disease."
                suggestions = [
                    "Exercise regularly and eat whole foods",
                    "Limit salt intake and avoid stress",
                    "Do regular heart checkups"
                ]

        print("====== BACKEND LOG ======")
        print("Risk Type:", risk_type)
        print("Prediction:", prediction)
        print("Suggestions:", suggestions)
        print("=========================")

        return render_template(
            "result.html",
            result=result,
            suggestions=suggestions,
            age=age,
            bmi=bmi,
            glucose=glucose,
            bp=bp
        )

    except Exception as e:
        print("❌ Error:", e)
        return render_template("result.html", result=f"❌ Error: {e}", suggestions=[])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
