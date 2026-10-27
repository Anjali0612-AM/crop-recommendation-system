  # Irrigation Recommendation System

def get_irrigation_recommendation(rainfall, humidity):

    recommendations = []

    # Rainfall based recommendation
    if rainfall < 50:
        irrigation = "Higher irrigation may be required."
        recommendations.append("Rainfall is low, so additional irrigation may be needed.")

    elif rainfall < 100:
        irrigation = "Moderate irrigation may be required."
        recommendations.append("Rainfall is moderate, so regular irrigation may be useful.")

    else:
        irrigation = "Low irrigation may be required."
        recommendations.append("Rainfall is sufficient, so avoid unnecessary irrigation.")

    # Humidity based recommendation
    if humidity < 50:
        recommendations.append("Humidity is low, so the soil may lose moisture faster.")

    elif humidity > 80:
        recommendations.append("Humidity is high, so avoid excessive irrigation.")

    else:
        recommendations.append("Humidity level is suitable for normal irrigation.")

    return irrigation, recommendations