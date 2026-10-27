# AI Farming Assistant

def get_ai_advice(
    crop,
    N,
    P,
    K,
    temperature,
    humidity,
    ph,
    rainfall
):
    advice = []

    # Crop advice
    advice.append(
        f"Based on the entered conditions, {crop} is the recommended crop."
    )

    # Nitrogen analysis
    if N < 50:
        advice.append(
            "Nitrogen level is low. Nitrogen management should be considered."
        )
    elif N > 120:
        advice.append(
            "Nitrogen level is high. Avoid excessive nitrogen fertilizer."
        )
    else:
        advice.append(
            "Nitrogen level is suitable."
        )

    # Phosphorus analysis
    if P < 30:
        advice.append(
            "Phosphorus level is low. Phosphorus management may be required."
        )
    elif P > 100:
        advice.append(
            "Phosphorus level is high. Avoid excessive phosphorus fertilizer."
        )
    else:
        advice.append(
            "Phosphorus level is suitable."
        )

    # Potassium analysis
    if K < 40:
        advice.append(
            "Potassium level is low. Potassium management may be required."
        )
    elif K > 150:
        advice.append(
            "Potassium level is high. Avoid excessive potassium fertilizer."
        )
    else:
        advice.append(
            "Potassium level is suitable."
        )

    # pH analysis
    if ph < 5.5:
        advice.append(
            "The soil is acidic. Soil pH management may be required."
        )
    elif ph > 7.5:
        advice.append(
            "The soil is alkaline. Soil pH management may be required."
        )
    else:
        advice.append(
            "Soil pH is within a suitable range."
        )

    # Rainfall analysis
    if rainfall < 50:
        advice.append(
            "Rainfall is low, so additional irrigation may be needed."
        )
    elif rainfall > 200:
        advice.append(
            "Rainfall is high, so avoid unnecessary irrigation and waterlogging."
        )
    else:
        advice.append(
            "Rainfall is in a moderate range."
        )

    # Humidity analysis
    if humidity > 80:
        advice.append(
            "Humidity is high. Avoid excessive irrigation and monitor the crop regularly."
        )
    elif humidity < 40:
        advice.append(
            "Humidity is low. Monitor soil moisture carefully."
        )
    else:
        advice.append(
            "Humidity level is suitable."
        )

    # Temperature analysis
    if temperature > 35:
        advice.append(
            "Temperature is high. Protect the crop from heat stress and monitor irrigation."
        )
    elif temperature < 10:
        advice.append(
            "Temperature is low. Monitor the crop for cold stress."
        )
    else:
        advice.append(
            "Temperature is within a moderate range."
        )

    return advice