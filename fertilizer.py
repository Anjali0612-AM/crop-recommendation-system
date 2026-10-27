# Fertilizer Recommendation System

def get_fertilizer_recommendation(N, P, K):

    recommendations = []

    # Nitrogen
    if N < 50:
        recommendations.append("Nitrogen fertilizer is recommended.")
    elif N > 120:
        recommendations.append("Avoid excessive nitrogen fertilizer.")
    else:
        recommendations.append("Nitrogen level is suitable.")

    # Phosphorus
    if P < 30:
        recommendations.append("Phosphorus fertilizer is recommended.")
    elif P > 100:
        recommendations.append("Avoid excessive phosphorus fertilizer.")
    else:
        recommendations.append("Phosphorus level is suitable.")

    # Potassium
    if K < 40:
        recommendations.append("Potassium fertilizer is recommended.")
    elif K > 150:
        recommendations.append("Avoid excessive potassium fertilizer.")
    else:
        recommendations.append("Potassium level is suitable.")

    # Overall recommendation
    if N < 50 and P < 30 and K < 40:
        fertilizer = "Balanced NPK fertilizer may be required."
    elif N < 50:
        fertilizer = "Nitrogen-rich fertilizer may be required."
    elif P < 30:
        fertilizer = "Phosphorus-rich fertilizer may be required."
    elif K < 40:
        fertilizer = "Potassium-rich fertilizer may be required."
    else:
        fertilizer = "No major NPK deficiency detected from the entered values."

    return fertilizer, recommendations