import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# -----------------------
# Load Dataset
# -----------------------

data = pd.read_csv("dataset/disease_dataset.csv")

print("Dataset Loaded Successfully")

# -----------------------
# Features and Target
# -----------------------

X = data.drop("diseases", axis=1)
y = data["diseases"]

# -----------------------
# Encode Disease Names
# -----------------------

label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# -----------------------
# Train Test Split
# -----------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.2,
    random_state=42
)

# -----------------------
# Train Model
# -----------------------

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, y_train)

# -----------------------
# Accuracy
# -----------------------

prediction = model.predict(X_test)

accuracy = accuracy_score(y_test, prediction)

print("Accuracy :", accuracy)

# -----------------------
# Save Model
# -----------------------

import os

# Create model folder if it doesn't exist
os.makedirs("model", exist_ok=True)

pickle.dump(model, open("model/disease_model.pkl", "wb"))
pickle.dump(label_encoder, open("model/label_encoder.pkl", "wb"))
pickle.dump(list(X.columns), open("model/symptoms.pkl", "wb"))

print("Model Saved Successfully")