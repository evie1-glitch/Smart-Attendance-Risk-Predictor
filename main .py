import csv
import random
from math import exp

dataset = []
with open("dataset.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        dataset.append([float(item) for item in row])

random.shuffle(dataset)
split_index = int(0.8 * len(dataset))

train_data = dataset[:split_index]
test_data = dataset[split_index:]


def sigmoid(value):
    return 1 / (1 + exp(-value))


num_features = len(train_data[0]) - 1
weights = [0.0] * (num_features + 1)

learning_rate = 0.01
epochs = 500

for _ in range(epochs):
    for row in train_data:
        features = row[:-1]
        actual = row[-1]

        weighted_sum = weights[-1]
        for i in range(len(features)):
            weighted_sum += weights[i] * features[i]

        prediction = sigmoid(weighted_sum)
        error = actual - prediction

        for i in range(len(features)):
            weights[i] += learning_rate * error * features[i]

        weights[-1] += learning_rate * error

correct_predictions = 0

for row in test_data:
    features = row[:-1]
    actual = row[-1]

    weighted_sum = weights[-1]
    for i in range(len(features)):
        weighted_sum += weights[i] * features[i]

    prediction = round(sigmoid(weighted_sum))

    if prediction == actual:
        correct_predictions += 1

accuracy = correct_predictions / len(test_data)
print("Final Model Accuracy:", accuracy)


def predict(attendance, study_hours, marks, sleep_hours):
    features = [attendance, study_hours, marks, sleep_hours]

    weighted_sum = weights[-1]
    for i in range(len(features)):
        weighted_sum += weights[i] * features[i]

    prediction = round(sigmoid(weighted_sum))

    if prediction == 0:
        return "SAFE"
    elif prediction == 1:
        return "WARNING"
    else:
        return "CRITICAL"


print("Predicted Risk Level:", predict(65, 2, 50, 5))


