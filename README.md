# 🩺 AI Disease Prediction System

An AI-powered Disease Prediction System developed using **Python, Flask, and Scikit-learn** that predicts possible diseases based on symptoms selected by the user.

The application uses a **Decision Tree Machine Learning model** trained on a large medical dataset containing hundreds of symptoms and diseases. Users can select symptoms through a simple web interface, and the system predicts the most probable disease within seconds.

> **Disclaimer:** This project is intended for educational and learning purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment.

---

# Features

- Predicts diseases based on selected symptoms
- Machine Learning powered prediction using Decision Tree Classifier
- Flask-based web application
- Interactive and user-friendly interface
- Dynamic symptom loading from the trained dataset
- Real-time prediction
- Clean and responsive UI
- Easy to understand project structure
- Beginner-friendly implementation

---

# Technologies Used

## Programming Language

- Python 3

## Machine Learning

- Scikit-learn
- Decision Tree Classifier

## Backend

- Flask

## Frontend

- HTML5
- CSS3

## Data Processing

- Pandas
- NumPy

## Model Serialization

- Pickle

---

# Project Structure

```
Disease-Prediction-System/

│── app.py
│── train_model.py
│── requirements.txt
│── README.md
│
├── dataset/
│      disease_dataset.csv
│
├── model/
│      disease_model.pkl
│      label_encoder.pkl
│      symptoms.pkl
│
├── templates/
│      index.html
│      result.html
│
└── static/
       style.css
```

---

# Dataset

The project uses a large healthcare dataset containing:

- Hundreds of symptoms
- Multiple disease categories
- Binary symptom values (0 and 1)

Each row represents a disease case, while each symptom column indicates whether the symptom is present or absent.

---

# Machine Learning Workflow

1. Load the dataset using Pandas.
2. Separate features (symptoms) and target (disease).
3. Encode disease names using LabelEncoder.
4. Split the dataset into training and testing sets.
5. Train a Decision Tree Classifier.
6. Evaluate the model.
7. Save the trained model using Pickle.
8. Load the trained model in Flask for prediction.

---

# How the Prediction Works

1. User opens the web application.
2. User selects symptoms from the available list.
3. Flask receives the selected symptoms.
4. Symptoms are converted into numerical feature values.
5. The trained Machine Learning model predicts the most probable disease.
6. The prediction result is displayed on the result page.

---

# Installation

Clone the repository

```bash
git clone https://github.com/your-username/Disease-Prediction-System.git
```

Move into the project directory

```bash
cd Disease-Prediction-System
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Install the required libraries

```bash
pip install -r requirements.txt
```

Train the Machine Learning model

```bash
python train_model.py
```

Run the Flask application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

# Files Description

## app.py

Main Flask application that handles routing, user interaction, model loading, and prediction.

---

## train_model.py

Responsible for training the Decision Tree Machine Learning model and saving the trained files.

---

## disease_model.pkl

Serialized Machine Learning model used for prediction.

---

## label_encoder.pkl

Stores the encoded disease labels used during training.

---

## symptoms.pkl

Stores the list of symptoms used by the prediction system.

---

## templates/

Contains the HTML pages used by the Flask application.

- index.html
- result.html

---

## static/

Contains the CSS stylesheet used for designing the web interface.

---

# Libraries Used

- Flask
- Pandas
- NumPy
- Scikit-learn
- Pickle

---

# Model Used

Decision Tree Classifier

The Decision Tree algorithm learns relationships between symptoms and diseases from the dataset. During prediction, it compares the selected symptoms with learned patterns and predicts the most likely disease.

---

# Learning Objectives

This project demonstrates:

- Data preprocessing
- Feature engineering
- Machine Learning model training
- Model serialization
- Flask web development
- Frontend and backend integration
- User input handling
- Model deployment using Flask

---

# License

This project is developed for educational purposes.
