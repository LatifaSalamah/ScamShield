from student1_analysis import analyze_message
from student2_scoring import calculate_score, get_risk_level
from student3_analysis import display_results

print("===== Welcome to ScamShield =====")

message = input("Enter the message you received: ")

urgency, threat, sensitive, link = analyze_message(message)

score = calculate_score(urgency, threat, sensitive, link)

level = get_risk_level(score)

display_results(score, level, urgency, threat, sensitive, link)