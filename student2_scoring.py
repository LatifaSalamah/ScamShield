def calculate_score(urgency, threat, sensitive, link):

    score = 0

    if urgency == True:
        score = score + 25

    if threat == True:
        score = score + 20

    if sensitive == True:
        score = score + 30

    if link == True:
        score = score + 25

    return score


def get_risk_level(score):

    if score <= 20:
        level = "Low Risk"
    elif score <= 40:
        level = "Moderate Risk"
    elif score <= 70:
        level = "High Risk"
    else:
        level = "Very High Risk"

    return level