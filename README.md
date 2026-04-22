# Smart-Attendance-Risk-Predictor
A simple machine learning tool that predicts whether a student is at risk of low attendance based on their current attendance pattern and trends.


# Smart Attendance Risk Predictor 📊

## Overview

This project is a simple machine learning-based tool that predicts whether a student is at risk of falling below the required attendance percentage. It helps students understand their situation early and act before things get serious.

---

## Problem

A lot of students only realize their attendance shortage when it’s already too late. There’s no easy way to estimate how current attendance trends will affect future eligibility.

---

## Solution

The project uses a logistic regression model (implemented from scratch) to analyze student data and classify risk levels based on:

* attendance percentage
* study hours
* academic performance
* sleep patterns

---

## Features

* Reads dataset from a CSV file
* Trains a machine learning model from scratch
* Predicts student risk level (SAFE / WARNING / CRITICAL)
* Calculates model accuracy
* Simple CLI-based execution

---

## AIML Concepts Used 🧠

* Supervised learning
* Logistic regression
* Sigmoid function
* Model training (epochs & weight updates)
* Train-test split
* Model evaluation (accuracy)

---

## Flowchart 🔄

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

## Project Structure 📁

```id="cpqizn"
├── main.py
├── dataset.csv
├── README.md
├── report.pdf
```

---

## How to Run ▶️

1. Make sure Python is installed
2. Keep `dataset.csv` in the same folder
3. Run:

```id="dbhol0"
python main.py
```

---

## Output 📈

* Displays model accuracy
* Predicts student risk level based on input

Example:

```id="15faag"
Model Accuracy: 0.83  
Predicted Risk Level: WARNING
```

---

## Note

This is a simplified implementation of logistic regression. Multi-class classification is approximated and can be improved further using techniques like One-vs-Rest.

---

## Future Improvements 🚀

* Proper multi-class classification
* Graph-based visualization
* Web interface
* Real-time attendance tracking

---

## Conclusion

This project shows how basic AIML concepts can be applied to solve a real, everyday student problem in a simple and practical way.
