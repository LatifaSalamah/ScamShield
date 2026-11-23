# ScamShield - Student 2
# Risk Scoring

SCORES = {
    "urgent_words": 20,        # Urgency words
    "suspicious_link": 30,     # Suspicious link
    "asks_personal_info": 30,  # Personal information
    "prize_or_money": 15,      # Prize or money
    "unknown_sender": 10,       # Unknown sender
    "spelling_errors": 5        # Spelling errors
}


def calculate_score(flags):
    """
    flags: dictionary containing detected scam indicators
    """

    total = 0

    for flag, found in flags.items():
        if found and flag in SCORES:
            total += SCORES[flag]

    return total


def get_risk_level(score):

    if score <= 20:
        return "Low Risk (خطورة منخفضة)"

    elif score <= 50:
        return "Moderate Risk (خطورة متوسطة)"

    elif score <= 80:
        return "High Risk (خطورة عالية)"

    else:
        return "Very High Risk (خطورة عالية جدًا)"


def analyze_risk(flags):

    score = calculate_score(flags)
    level = get_risk_level(score)

    return score, level


# Test the code
if __name__ == "__main__":

    detected_flags = {
        "urgent_words": True,
        "suspicious_link": True,
        "asks_personal_info": True,
        "prize_or_money": False,
        "unknown_sender": True,
        "spelling_errors": False
    }

    score, level = analyze_risk(detected_flags)

    print("Total Risk Score:", score)
    print("Risk Level:", level)