# Grading using Dictionary
Students_Scores = {
    "Abdul": 80,
    "Abhishek": 90,
    "Ashok": 20,
    "Marvel": 70,
    "Karthik": 98
}
student_review = {}
for student in Students_Scores:
    score = Students_Scores[student]
    if 90 < score <= 100:
        student_review[student] = "outstanding"
    elif 80 < score <= 90:
        student_review[student] = "Exceeds expectation"
    elif 70 < score <= 80:
        student_review[student] = "is acceptable"
    elif score <= 70:
        student_review[student] = "Should WorkHard"

print(student_review)
