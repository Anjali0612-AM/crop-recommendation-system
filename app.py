from flask import Flask, render_template, request
import pandas as pd
import pickle
from datetime import datetime

from fertilizer import get_fertilizer_recommendation
from irrigation import get_irrigation_recommendation
from ai_assistant import get_ai_advice
from soil_health import get_soil_health


app = Flask(__name__)


# =========================
# Load Trained ML Model
# =========================

with open("model/crop_model.pkl", "rb") as file:
    model = pickle.load(file)


# =========================
# Crop Information
# =========================

crop_info = {

    "rice": {
        "climate": "Warm and humid climate is suitable.",
        "water": "High water requirement.",
        "season": "Kharif season.",
        "soil": "Clayey and loamy soil.",
        "description": "Rice is an important cereal crop that requires sufficient water.",
        "tips": [
            "Maintain proper water availability.",
            "Use balanced fertilizers.",
            "Control weeds regularly."
        ]
    },

    "maize": {
        "climate": "Warm climate with moderate rainfall.",
        "water": "Moderate water requirement.",
        "season": "Kharif and Rabi seasons.",
        "soil": "Well-drained loamy soil.",
        "description": "Maize is an important cereal crop used for food and animal feed.",
        "tips": [
            "Provide proper irrigation.",
            "Control weeds.",
            "Use balanced fertilizers."
        ]
    },

    "chickpea": {
        "climate": "Cool and dry climate.",
        "water": "Low to moderate water requirement.",
        "season": "Rabi season.",
        "soil": "Well-drained loamy soil.",
        "description": "Chickpea is an important pulse crop rich in protein.",
        "tips": [
            "Avoid excessive irrigation.",
            "Use proper seed treatment.",
            "Maintain good soil drainage."
        ]
    },

    "kidneybeans": {
        "climate": "Moderate warm climate.",
        "water": "Moderate water requirement.",
        "season": "Kharif season.",
        "soil": "Well-drained loamy soil.",
        "description": "Kidney beans are protein-rich pulse crops.",
        "tips": [
            "Avoid waterlogging.",
            "Provide moderate irrigation.",
            "Control weeds."
        ]
    },

    "pigeonpeas": {
        "climate": "Warm and semi-arid climate.",
        "water": "Moderate water requirement.",
        "season": "Kharif season.",
        "soil": "Well-drained loamy soil.",
        "description": "Pigeon pea is an important pulse crop.",
        "tips": [
            "Avoid excessive irrigation.",
            "Control pests.",
            "Maintain proper soil drainage."
        ]
    },

    "mungbean": {
        "climate": "Warm and dry climate.",
        "water": "Low to moderate water requirement.",
        "season": "Kharif and summer seasons.",
        "soil": "Well-drained sandy loam soil.",
        "description": "Mungbean is a short-duration pulse crop.",
        "tips": [
            "Avoid waterlogging.",
            "Provide irrigation during dry periods.",
            "Control weeds."
        ]
    },

    "blackgram": {
        "climate": "Warm and humid climate.",
        "water": "Moderate water requirement.",
        "season": "Kharif season.",
        "soil": "Well-drained loamy soil.",
        "description": "Blackgram is an important pulse crop.",
        "tips": [
            "Avoid excessive irrigation.",
            "Control weeds.",
            "Use healthy seeds."
        ]
    },

    "lentil": {
        "climate": "Cool and dry climate.",
        "water": "Low water requirement.",
        "season": "Rabi season.",
        "soil": "Well-drained loamy soil.",
        "description": "Lentil is a protein-rich pulse crop.",
        "tips": [
            "Avoid waterlogging.",
            "Provide limited irrigation.",
            "Maintain good soil drainage."
        ]
    },

    "banana": {
        "climate": "Warm and humid climate.",
        "water": "High water requirement.",
        "season": "Can be grown throughout the year in suitable climates.",
        "soil": "Deep, fertile and well-drained soil.",
        "description": "Banana is a tropical fruit crop requiring sufficient moisture.",
        "tips": [
            "Provide regular irrigation.",
            "Use organic manure.",
            "Protect plants from strong winds."
        ]
    },

    "mango": {
        "climate": "Warm tropical and subtropical climate.",
        "water": "Moderate water requirement.",
        "season": "Summer fruiting season.",
        "soil": "Well-drained loamy soil.",
        "description": "Mango is an important tropical fruit crop.",
        "tips": [
            "Avoid waterlogging.",
            "Provide irrigation during dry periods.",
            "Prune unhealthy branches."
        ]
    },

    "grapes": {
        "climate": "Warm and dry climate.",
        "water": "Moderate water requirement.",
        "season": "Mainly grown in warm seasons.",
        "soil": "Well-drained sandy loam or loamy soil.",
        "description": "Grapes are an important fruit crop used for fresh consumption and processing.",
        "tips": [
            "Provide proper support to vines.",
            "Avoid excessive irrigation.",
            "Regular pruning is important."
        ]
    },

    "watermelon": {
        "climate": "Warm and sunny climate.",
        "water": "Moderate to high water requirement.",
        "season": "Summer season.",
        "soil": "Sandy loam and well-drained soil.",
        "description": "Watermelon is a warm-season fruit crop.",
        "tips": [
            "Provide regular irrigation.",
            "Avoid waterlogging.",
            "Ensure sufficient sunlight."
        ]
    },

    "muskmelon": {
        "climate": "Warm and dry climate.",
        "water": "Moderate water requirement.",
        "season": "Summer season.",
        "soil": "Sandy loam and well-drained soil.",
        "description": "Muskmelon is a warm-season fruit crop.",
        "tips": [
            "Provide proper irrigation.",
            "Avoid waterlogging.",
            "Maintain good sunlight."
        ]
    }
}


# =========================
# Home Route
# =========================

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    info = None
    input_values = None

    fertilizer = None
    fertilizer_details = []

    irrigation = None
    irrigation_details = []

    ai_advice = []

    soil_health = None
    soil_score = None
    soil_advice = []

    if request.method == "POST":

        try:

            # =========================
            # Get Input Values
            # =========================

            N = float(request.form["N"])
            P = float(request.form["P"])
            K = float(request.form["K"])

            temperature = float(
                request.form["temperature"]
            )

            humidity = float(
                request.form["humidity"]
            )

            ph = float(
                request.form["ph"]
            )

            rainfall = float(
                request.form["rainfall"]
            )


            # =========================
            # Store Input Values
            # =========================

            input_values = {

                "N": N,
                "P": P,
                "K": K,

                "temperature": temperature,
                "humidity": humidity,

                "ph": ph,
                "rainfall": rainfall
            }


            # =========================
            # ML Crop Prediction
            # =========================

            prediction = model.predict([[
                N,
                P,
                K,
                temperature,
                humidity,
                ph,
                rainfall
            ]])[0]


            # =========================
            # Crop Information
            # =========================

            info = crop_info.get(
                prediction.lower(),
                {}
            )


            # =========================
            # Fertilizer Recommendation
            # =========================

            fertilizer, fertilizer_details = (
                get_fertilizer_recommendation(
                    N,
                    P,
                    K
                )
            )


            # =========================
            # Irrigation Recommendation
            # =========================

            irrigation, irrigation_details = (
                get_irrigation_recommendation(
                    rainfall,
                    humidity
                )
            )


            # =========================
            # AI Farming Assistant
            # =========================

            ai_advice = get_ai_advice(

                prediction,

                N,
                P,
                K,

                temperature,
                humidity,

                ph,
                rainfall
            )


            # =========================
            # Soil Health Analysis
            # =========================

            soil_health, soil_score, soil_advice = (
                get_soil_health(
                    N,
                    P,
                    K,
                    ph
                )
            )


            # =========================
            # Save Prediction History
            # =========================

            history_file = "history.csv"

            new_record = pd.DataFrame([{

                "Date":
                    datetime.now().strftime(
                        "%Y-%m-%d"
                    ),

                "Time":
                    datetime.now().strftime(
                        "%H:%M:%S"
                    ),

                "Nitrogen": N,

                "Phosphorus": P,

                "Potassium": K,

                "Temperature":
                    temperature,

                "Humidity":
                    humidity,

                "pH":
                    ph,

                "Rainfall":
                    rainfall,

                "Predicted Crop":
                    prediction

            }])


            try:

                old_data = pd.read_csv(
                    history_file
                )

                updated_data = pd.concat(
                    [
                        old_data,
                        new_record
                    ],
                    ignore_index=True
                )

                updated_data.to_csv(
                    history_file,
                    index=False
                )

            except FileNotFoundError:

                new_record.to_csv(
                    history_file,
                    index=False
                )


        except Exception as e:

            prediction = "Error"

            info = {
                "description": str(e)
            }


    # =========================
    # Send Data to HTML
    # =========================

    return render_template(

        "index.html",

        prediction=prediction,

        info=info,

        input_values=input_values,

        fertilizer=fertilizer,

        fertilizer_details=fertilizer_details,

        irrigation=irrigation,

        irrigation_details=irrigation_details,

        ai_advice=ai_advice,

        soil_health=soil_health,

        soil_score=soil_score,

        soil_advice=soil_advice
    )


# =========================
# History Page
# =========================

@app.route("/history")
def history():

    try:

        data = pd.read_csv(
            "history.csv"
        )

        records = data.to_dict(
            orient="records"
        )

    except FileNotFoundError:

        records = []


    return render_template(
        "history.html",
        records=records
    )


# =========================
# About Page
# =========================

@app.route("/about")
def about():

    return render_template(
        "about.html"
    )


# =========================
# Contact Page
# =========================

@app.route("/contact")
def contact():

    return render_template(
        "contact.html"
    )


# =========================
# Run Flask Application
# =========================

if __name__ == "__main__":

    app.run(
        debug=True
    )