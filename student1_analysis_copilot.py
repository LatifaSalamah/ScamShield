
def analyze_message(message):

    urgency = (
        "urgent" in message or "URGENT" in message or "Urgent" in message or
        "immediately" in message or "IMMEDIATELY" in message or "Immediately" in message or
        "act now" in message or "ACT NOW" in message or "Act now" in message or
        "today" in message or "TODAY" in message or "Today" in message
    )

    threat = (
        "suspended" in message or "SUSPENDED" in message or "Suspended" in message or
        "blocked" in message or "BLOCKED" in message or "Blocked" in message or
        "closed" in message or "CLOSED" in message or "Closed" in message or
        "terminated" in message or "TERMINATED" in message or "Terminated" in message
    )

    sensitive = (
        "password" in message or "PASSWORD" in message or "Password" in message or
        "otp" in message or "OTP" in message or "Otp" in message or
        "verification code" in message or "VERIFICATION CODE" in message or
        "Verification code" in message
    )

    link = (
        "http" in message or "HTTP" in message or "Http" in message or
        "www." in message or "WWW." in message or "Www." in message
    )

    return urgency, threat, sensitive, link
