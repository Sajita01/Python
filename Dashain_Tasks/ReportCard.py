
# Report Card with Functions and Built-ins
# Report card with functions: names = ["Sita", "Ram", "Gita"] marks = [[90, 85, 78], [45, 38, 60], [70, 65, 80]]

names = ["Sita", "Ram", "Gita"]
marks = [[90, 85, 78],[45, 38, 60],[70, 65, 80]]

# 01. Create get_average(marks) that returns the average,rounded to 2 decimal places. Add a docstring.
def get_average(marks):
    average = sum(marks) / len(marks)
    return round(average, 2)

# 02. Create get_grade(avg) that returns:A (80+), B (60+), C (40+) or Fail.
def get_grade(avg):
    if avg >= 80:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "Fail"

# 03. Create report(name, marks, pass_mark=40) that prints average, grade, best, worst and whether the student passed.
def report(name, marks, pass_mark=40):
    average = get_average(marks)
    grade = get_grade(average)
    best = max(marks)
    worst = min(marks)

    # The student must pass every subject.
    passed = all(mark >= pass_mark for mark in marks)

    print(f"{name}: avg {average:.2f}, grade {grade}")
    print(f"  Best: {best} | Worst: {worst}")
    print(f"  Passed all? {passed}")

# 04 and 05. Use built-ins and zip() to loop over names and marks together.
for name, student_marks in zip(names, marks):
    report(name, student_marks)

# 06. Collect the averages, then print ranks with sorted() and enumerate()
averages = []

for student_marks in marks:
    average = get_average(student_marks)
    averages.append(average)

ranked_averages = sorted(averages, reverse=True)

for rank, average in enumerate(ranked_averages, start=1):
    print(f"Rank {rank}: {average:.2f}")

"""
Output:
Sita: avg 84.33, grade A
  Best: 90 | Worst: 78
  Passed all? True
Ram: avg 47.67, grade C
  Best: 60 | Worst: 38
  Passed all? False
Gita: avg 71.67, grade B
  Best: 80 | Worst: 65
  Passed all? True
Rank 1: 84.33
Rank 2: 71.67
Rank 3: 47.67

"""