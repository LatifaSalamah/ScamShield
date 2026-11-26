def analyze_message(message):

    urgency = False
    threat = False
    sensitive = False
    link = False

    if "urgent" in message or "Urgent" in message or "URGENT" in message:
        urgency = True
    if "immediately" in message or "Immediately" in message or "IMMEDIATELY" in message:
        urgency = True
    if "act now" in message or "Act now" in message or "ACT NOW" in message:
        urgency = True

    if "suspended" in message or "Suspended" in message or "SUSPENDED" in message:
        threat = True
    if "blocked" in message or "Blocked" in message or "BLOCKED" in message:
        threat = True
    if "closed" in message or "Closed" in message or "CLOSED" in message:
        threat = True
    if "terminated" in message or "Terminated" in message or "TERMINATED" in message:
        threat = True

    if "password" in message or "Password" in message or "PASSWORD" in message:
        sensitive = True
    if "otp" in message or "Otp" in message or "OTP" in message:
        sensitive = True
    if "verification code" in message or "Verification code" in message or "VERIFICATION CODE" in message:
        sensitive = True

    if "http" in message or "Http" in message or "HTTP" in message:
        link = True
    if "www." in message or "Www." in message or "WWW." in message:
        link = True

    return urgency, threat, sensitive, link