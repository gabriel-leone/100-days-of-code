names = names_string.split(", ")
# The code above converts the input into an array seperating
# each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
import random

index = random.randint(0, len(names)-1)
print(f'{names[index]} is going to buy the meal today!')