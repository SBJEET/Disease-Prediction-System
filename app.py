from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load model
model = pickle.load(open("model/disease_model.pkl", "rb"))
label_encoder = pickle.load(open("model/label_encoder.pkl", "rb"))
symptoms = pickle.load(open("model/symptoms.pkl", "rb"))


@app.route("/")
def home():
    return render_template("index.html", symptoms=symptoms)


@app.route("/predict", methods=["POST"])
def predict():

    selected = []

    for i in range(1, 6):
        symptom = request.form.get(f"symptom{i}")

        if symptom and symptom != "None":
            selected.append(symptom)

    input_data = [0] * len(symptoms)

    for symptom in selected:
        if symptom in symptoms:
            index = symptoms.index(symptom)
            input_data[index] = 1

    prediction = model.predict([input_data])[0]

    disease = label_encoder.inverse_transform([prediction])[0]

    return render_template(
        "result.html",
        disease=disease,
        selected=selected
    )


if __name__ == "__main__":
    app.run(debug=True)