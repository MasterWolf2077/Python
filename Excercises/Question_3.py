#Create tuple of student names
student_names = ("Alice", "Bob", "Charlie")

#Create dictionary where keys are student names(from the tuple) and values are scores
student_names_scores = {"Alice": 85, "Bob": 90, "Charlie": 78}

#Print each student's name with their score using loop
for name in student_names:
    print("name:", name, ", score:", student_names_scores[name])

#Finds and prints student with highest score
highest_scorer = max(student_names_scores, key=student_names_scores.get)
print("Highest scorer:", highest_scorer, "with a score of:", student_names_scores[highest_scorer])
