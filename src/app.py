from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Cargar el modelo
model = pickle.load(open('../models/ranfor_classifier_nestimators-60_42.sav', 'rb'))

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    if request.method == "POST":
        try:
            # Obtener los valores del formulario y verificar si están vacíos
            pregnancies = float(request.form.get("pregnancies") or 0)
            glucose = float(request.form.get("glucose") or 0)
            blood_pressure = float(request.form.get("blood_pressure") or 0)
            skin_thickness = float(request.form.get("skin_thickness") or 0)
            insulin = float(request.form.get("insulin") or 0)
            bmi = float(request.form.get("bmi") or 0)
            diabetes_pedigree_function = float(request.form.get("diabetes_pedigree_function") or 0)
            age = float(request.form.get("age") or 0)

            # Crear un DataFrame para la predicción
            input_data = pd.DataFrame([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]], 
                                       columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'])

            # Hacer la predicción
            prediction = model.predict(input_data)[0]  # Obtener el valor de predicción
        except ValueError as e:
            # Manejar el caso de valores no válidos
            prediction = "Por favor, introduce valores válidos en todos los campos."
    

    return render_template("index.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)
