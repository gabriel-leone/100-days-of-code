target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

even_sum = 0

# Write your code here 👇
for value in range(0, target+1, 2):
  even_sum += value

print(even_sum)