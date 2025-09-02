# 2D list of scores
scores = [
    [78, 85, 90], #Student 1
    [92, 88, 76], #Student 2
    [89, 94, 91], #Student 3
    [67, 73, 70]  #Student 4
]

#1. Score of Student 2 in Subject 3
student2_subject3 = scores[1][2]
print("Student 2, Subject 3 score:", student2_subject3) 

#2. Average score of Student 3
student3_scores = scores[2]
average_student3 = sum(student3_scores) / len(student3_scores)
print("Average score for Student 3:", average_student3)

#3. Highest score across all students in Subject 1
highest_score = max(max(student) for student in scores)
print("Highest score overall:", highest_score)

#4. Average score for eaach subject
num_students = len(scores[0])
for subject in range(num_students):
    total = sum(scores[student][subject] for student in range(len(scores)))
    average = total / len(scores)
    print(f"Average score for Subject {subject + 1}:", average)