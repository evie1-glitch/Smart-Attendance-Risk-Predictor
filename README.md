# Smart-Attendance-Risk-Predictor
A simple machine learning tool that predicts whether a student is at risk of low attendance based on their current attendance pattern and trends.

# 📊 Smart Attendance Risk Predictor

## 📌 Overview

This project is a simple Machine Learning-based tool that predicts whether a student is at risk of falling below the required attendance percentage. It helps students understand their attendance status early and take action before it becomes critical.

---

## 🎯 Problem

Many students only realize their attendance shortage when it’s already too late. There is no easy way to predict how current attendance trends will affect future eligibility.

---

## 💡 Solution

This project uses a Logistic Regression model (implemented from scratch) to analyze student data and classify them into different risk levels based on:

* Attendance percentage
* Study hours
* Academic performance
* Sleep patterns

---

## ⚙️ Features

* Reads dataset from a CSV file
* Trains a machine learning model from scratch
* Predicts student risk level (SAFE / WARNING / CRITICAL)
* Calculates model accuracy
* Simple and easy to run

---

## 🧠 AIML Concepts Used

* Supervised Learning
* Logistic Regression
* Sigmoid Function
* Model Training (Epochs & Weight Updates)
* Train-Test Split
* Model Evaluation (Accuracy)

---

## 🔄 Flowchart

```id="flow123"
        Start
          ↓
   Load Dataset (CSV)
          ↓
   Data Preprocessing
          ↓
   Split into Train/Test
          ↓
   Train Logistic Model
          ↓
   Calculate Accuracy
          ↓
   Take User Input
          ↓
   Predict Risk Level
          ↓
          End
```

---

## 🗂️ Project Structure

```id="cpqizn"
├── main.py
├── dataset.csv
├── README.md
├── report.pdf
```

---

## ▶️ How to Run

1. Make sure Python is installed
2. Keep `dataset.csv` in the same folder
3. Run the program:

```id="dbhol0"
python main.py
```

---

## 📈 Output

* Displays model accuracy
* Predicts student risk level based on input

Example:

```id="15faag"
Model Accuracy: 0.83
Predicted Risk Level: WARNING
```

---

## ⚠️ Note

This is a simplified implementation of logistic regression. Multi-class classification is approximated and can be further improved using advanced techniques like One-vs-Rest.

---

## 🚀 Future Improvements

* Proper multi-class classification
* Graph visualization of performance
* Web-based interface
* Real-time attendance tracking

---

## 📚 Conclusion

This project demonstrates how basic AIML concepts can be applied to solve a real-world student problem in a simple and effective way.
