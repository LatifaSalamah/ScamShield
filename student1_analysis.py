# ScamShield - Student 1
# Message Analysis

def analyze_message(message):

    message = message.lower()

    urgency_words = ["urgent", "immediately", "act now", "today"]
    threat_words = ["suspended", "blocked", "closed", "terminated"]
    sensitive_words = ["password", "otp", "verification code"]

    indicators = []

    for word in urgency_words:
        if word in message:
            indicators.append("Urgency")
            break

    for word in threat_words:
        if word in message:
            indicators.append("Threat")
            break

    for word in sensitive_words:
        if word in message:
            indicators.append("Sensitive Information")
            break

    if "http" in message or "www." in message:
        indicators.append("Link")

    return indicators