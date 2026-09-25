# Ask for name, age and city, and put them in a tuple. Unpack the tuple and print a neat ID card. Then make a tuple of 3 marks and print the highest, the lowest and the total. Finally, change the city using the list trick.

# Taking input
name = input("Name: ")
age = input("Age: ")
city = input("City: ")

# Creating a tuple (packing)
student = (name, age, city)

# Unpacking the tuple
n, a, c = student

# Printing ID card
print("===== ID CARD =====")
print("Name:", n)
print("Age :", a)
print("City:", c)

# Tuple of marks
marks = (70, 85, 90)

# Highest, lowest and total marks
print("Highest marks:", max(marks))
print("Lowest marks :", min(marks))
print("Total marks  :", sum(marks))

# Changing the city (concept:convert to list -->edit --> Tuple)
temp = list(student)
temp[2] = "Kathmandu"
student = tuple(temp)

print("Updated student tuple:", student)