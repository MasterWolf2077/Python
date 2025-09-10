#Grades Analyser

#Ask user for an integer (1--30)
n = int(input("Enter an integer (1-30):"))

#Create an empty list
exam_scores = []

#Read exam scores from n(0--100)
for i in range(n):
    score = int(input("Enter exam score (0-100):"))
    exam_scores.append(score)
    
#Calculate average score
average_score = sum(exam_scores) / n

#Find highest and lowest scores
highest_score = max(exam_scores)
lowest_score = min(exam_scores)

#List of scores in dedscending order
exam_scores.sort(reverse=True)

#Print results
print("\nResults:")
print("Average exam score:", average_score)
print("Highest exam score: ", highest_score)
print("Lowest esaxm score: ", lowest_score)
print("Exam scores in descending order: ", exam_scores)
