student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for alumn in student_scores:
  if student_scores[alumn] <= 70:
    student_grades[alumn] = "Fail"
  elif student_scores[alumn] > 70 and student_scores[alumn] <= 80:
    student_grades[alumn] = "Acceptable"
  elif student_scores[alumn] > 80 and student_scores[alumn] <= 90:
    student_grades[alumn] = "Exceeds Expectations"
  elif student_scores[alumn] > 90:
    student_grades[alumn] = "Outstanding"

# 🚨 Don't change the code below 👇
print(student_grades)