#Initial dictionary
student_scores = {"Alice": 85,
                "Bob": 90,
                 "Charlie": 78
                 }

#Print all keys
print("Student names:", student_scores.keys())

#Print all values
print("Scores:", student_scores.values())

#Update scores
student_scores["Bob"] = 95

#Add a new student
student_scores["Diana"] = 88

#Print updated dictionary
print("Upadted student scores:", student_scores)