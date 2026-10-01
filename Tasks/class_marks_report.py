# Keep student marks in a dictionary. Loop with .items() and print Pass or Fail for each student. Then print the class average.
marks = {"Ram": 78, "Sita": 92, "Hari": 35, "Gita": 64}

total = 0
top = 0

for name, mark in marks.items():
    if mark >= 40:
        print(f"{name}: {mark} Pass")
    else:
        print(f"{name}: {mark} Fail")
# Calculate total
    total += mark

    # Grades
    if mark >= 80:
        grade = "A"
    elif mark >= 60:
        grade = "B"
    else:
        grade = "C"

    print(f"{name}'s grade: {grade}")

    # Find topper
    if mark > top:
        top = mark
        topper = name

# Class average
average = total / len(marks)
print(f"\nClass average: {average}")

# Print topper
print(f"Topper: {topper} with {top} marks")