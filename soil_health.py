# Soil Health Analysis

def get_soil_health(N, P, K, ph):

    score = 0
    advice = []

    # Nitrogen
    if 50 <= N <= 120:
        score += 25
        advice.append("Nitrogen level is suitable.")
    elif N < 50:
        advice.append("Nitrogen level is low.")
    else:
        advice.append("Nitrogen level is high.")

    # Phosphorus
    if 30 <= P <= 100:
        score += 25
        advice.append("Phosphorus level is suitable.")
    elif P < 30:
        advice.append("Phosphorus level is low.")
    else:
        advice.append("Phosphorus level is high.")

    # Potassium
    if 40 <= K <= 150:
        score += 25
        advice.append("Potassium level is suitable.")
    elif K < 40:
        advice.append("Potassium level is low.")
    else:
        advice.append("Potassium level is high.")

    # Soil pH
    if 5.5 <= ph <= 7.5:
        score += 25
        advice.append("Soil pH is suitable.")
    elif ph < 5.5:
        advice.append("Soil is acidic.")
    else:
        advice.append("Soil is alkaline.")

    # Overall health
    if score >= 75:
        health = "Good Soil Health"
    elif score >= 50:
        health = "Moderate Soil Health"
    else:
        health = "Poor Soil Health"

    return health, score, advice