
# ScamShield - Student 3
# Results and Advice


def display_results(score, level, indicators):

    print("\n===== ScamShield Results =====")

    print("Risk Score:", score)
    print("Risk Level:", level)

    print("\nDetected Indicators:")

    if len(indicators) == 0:
        print("No suspicious indicators detected.")

    else:
        for indicator in indicators:
            print("-", indicator)

    print("\nAdvice:")

    if score <= 20:
        print("The message appears to have a low risk.")
        print("Still, be careful when opening links.")

    elif score <= 50:
        print("The message may be suspicious.")
        print("Check the sender before responding.")

    elif score <= 80:
        print("Warning! This message has a high risk.")
        print("Do not click links or share personal information.")

    else:
        print("Very high risk! This message may be a scam.")
        print("Do not click links or share personal information.")
        print("Verify the message through the official source.")


# Test the program
if __name__ == "__main__":

    test_score = 90
    test_level = "Very High Risk"
    test_indicators = [
        "Urgency",
        "Threat",
        "Sensitive Information",
        "Link"
    ]

    display_results(test_score, test_level, test_indicators)
