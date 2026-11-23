# ScamShield - Main Program

from student1_analysis import analyze_message
from student2_analysis import analyze_risk
from student3_analysis import display_results


def main():

    print("===== Welcome to ScamShield =====")

    # Get message from user
    user_message = input("Enter the message you received: ")

    # Student 1: Analyze the message
    indicators = analyze_message(user_message)

    # Convert indicators into scoring flags
    flags = {
        "urgent_words": "Urgency" in indicators,
        "suspicious_link": "Link" in indicators,
        "asks_personal_info": "Sensitive Information" in indicators,
        "prize_or_money": False,
        "unknown_sender": False,
        "spelling_errors": False
    }

    # Student 2: Calculate risk score
    score, risk_level = analyze_risk(flags)

    # Student 3: Display results and advice
    display_results(score, risk_level, indicators)


# Run the program
if __name__ == "__main__":
    main()