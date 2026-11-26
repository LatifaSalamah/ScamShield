from student1_analysis import analyze_message

message = input("Enter a message: ")

urgency, threat, sensitive, link = analyze_message(message)

print("Urgency:", urgency)
print("Threat:", threat)
print("Sensitive Information:", sensitive)
print("Suspicious Link:", link)