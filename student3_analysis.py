def display_results(score, level, urgency, threat, sensitive, link):

    print("\n===== ScamShield Results =====")
    print("Risk Score:", score)
    print("Risk Level:", level)

    print("\nDetected Indicators:")

    found = False

    if urgency == True:
        print("- Urgency")
        found = True

    if threat == True:
        print("- Threat")
        found = True

    if sensitive == True:
        print("- Sensitive Information")
        found = True

    if link == True:
        print("- Suspicious Link")
        found = True

    if found == False:
        print("No suspicious indicators detected.")

    print("\nAdvice:")

    if level == "Low Risk":
        print("The message appears to have a low risk.")
        print("Still, be careful when opening links.")

    elif level == "Moderate Risk":
        print("The message has some suspicious signs.")
        print("Be careful and verify the sender.")

    elif level == "High Risk":
        print("Warning! This message has a high risk.")
        print("Do not share personal information.")

    else:
        print("Warning! This message has a very high risk.")
        print("Do not click links or share personal information.")