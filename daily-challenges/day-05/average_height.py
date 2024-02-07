# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
total_sum = 0
for height in student_heights:
    total_sum += height
average_height = total_sum / len(student_heights)
print(f"total height = {total_sum}")
print(f"number of students = {len(student_heights)}")
print(f"average height = {round(average_height)}")