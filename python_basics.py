
# Codomax Internship 2026
# Module 01: Introduction to AI & Python

# 1. Variables and Data Types
name = "Abdulrahman"
age = 21
track = "AI & Machine Learning"

print("Name:", name)
print("Age:", age)
print("Track:", track)

# 2. Conditional Statements
score = 85

if score >= 50:
    print("Passed")
else:
    print("Failed")

# 3. Loops
print("\nNumbers from 1 to 5:")

for number in range(1, 6):
    print(number)

# 4. Lists
skills = ["Python", "Artificial Intelligence", "Machine Learning"]

print("\nMy Skills:")

for skill in skills:
    print(skill)

# 5. Functions
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

scores = [80, 90, 85]
average = calculate_average(scores)

print("\nAverage Score:", average)
