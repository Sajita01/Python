# The user types marks with spaces. split() cuts the text, and a loop turns every part into an int. Then built-ins do all the hard work.
text = input("Enter marks with spaces: ")    # 67 45 92 78
marks = []
for part in text.split():
    marks.append(int(part))

print(f"Students: {len(marks)}")
print(f"Highest:  {max(marks)}")
print(f"Lowest:   {min(marks)}")
print(f"Total:    {sum(marks)}")
print(f"Average:  {round(sum(marks) / len(marks), 2)}")
print(f"Sorted:   {sorted(marks, reverse=True)}")

# print how many passed (40 or more)
passed = 0
for mark in marks:
    if mark >= 40:
        passed += 1

print(f"Passed: {passed}")

# if all() of them passed, print "Everyone passed!"
if all(mark >= 40 for mark in marks):
    print("Everyone passed!")


"""
Output:
Enter marks with spaces: 48 56 75 84 51
Students: 5
Highest:  84
Lowest:   48
Total:    314
Average:  62.8
Sorted:   [84, 75, 56, 51, 48]
Passed: 5
Everyone passed!

"""