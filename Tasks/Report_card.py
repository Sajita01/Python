#Ask for a name and three marks. Use zip() to build a marks dictionary, then put it inside a report dictionary. Print the report card, the total, the average and the best subject.

name = input("Student name: ")

m1 = int(input("Math: "))
m2 = int(input("Science: "))
m3 = int(input("English: "))

subjects = ["math", "science", "english"]

# Build a marks dictionary using zip()
marks = dict(zip(subjects, [m1, m2, m3]))

# Put the name and marks inside a report dictionary
report = {"name": name, "marks": marks}

print("\n---------REPORT CARD ---------")
print("Name :", report["name"])
print("Marks:", report["marks"])

# Calculate and print total
total = sum(marks.values())
print("Total:", total)

# Calculate and print average
average = total / len(marks)
print("Average:", average)

# Find and print the best subject
best_subject = max(marks, key=marks.get)
print("Best subject:", best_subject)
print("Best marks:", marks[best_subject])