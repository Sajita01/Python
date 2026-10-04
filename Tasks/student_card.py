# get_grade() uses if/elif and returns a grade. average() works on any marks dictionary. A for loop prints every student.

def get_grade(mark):
    if mark >= 80:
        return "A"
    elif mark >= 60:
        return "B"
    elif mark >= 40:
        return "C"
    else:
        return "F"

def average(marks):
    return sum(marks.values()) / len(marks)

marks = {"Ram": 78, "Sita": 92, "Hari": 35, "Gita": 64}

for name, mark in marks.items():
    print(f"{name}: {mark} -> {get_grade(mark)}")

print(f"Class average: {average(marks)}")

# write count_passed(marks): how many got 40 or more?
def count_passed(marks):
    count = 0

    for mark in marks.values():
        if mark >= 40:
            count += 1

    return count
print(f"Passed students: {count_passed(marks)}")

# write topper(marks): return the name with the top mark
def topper(marks):
    top_mark = 0

    for name, mark in marks.items():
        if mark > top_mark:
            top_mark = mark
            top_name = name

    return top_name
print(f"Topper: {topper(marks)}")

""" 
Output:
Ram: 78 -> B
Sita: 92 -> A
Hari: 35 -> F
Gita: 64 -> B
Class average: 67.25
Passed students: 3
Topper: Sita

"""