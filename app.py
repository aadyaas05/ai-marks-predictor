from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    hours = float(request.form['hours'])
    attendance = float(request.form['attendance'])
    sleep = float(request.form['sleep'])

    prediction = model.predict(np.array([[hours, attendance, sleep]]))
    marks = round(prediction[0], 2)

    percent = min(max(marks, 0), 100)

    # Grade system
    if marks >= 85:
        grade = "A+"
    elif marks >= 75:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "D"

    # Feedback message
    if marks >= 80:
        message = "Excellent performance! 🔥"
    elif marks >= 60:
        message = "Good job! Keep improving 👍"
    elif marks >= 40:
        message = "You can do better 📖"
    else:
        message = "Work harder and manage study time ⚠"

    return render_template(
        'index.html',
        prediction_text=f"Predicted Marks: {marks}",
        percent=percent,
        message=message,
        grade=grade
    )

if __name__ == "__main__":
    app.run(debug=True)