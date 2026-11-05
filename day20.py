# Duck Typing, Magic Methods & File Handling
# Duck Typing: In Python, what an object can do is more important than what class it belongs to.
class Duck:
    def quack(self):
        print("Quack quack!")

class Person:
    def quack(self):
        print("I am saying quack!")

class Toy:
    def quack(self):
        print("Squeak quack!")

def make_it_quack(thing):
    thing.quack()              # no type check

make_it_quack(Duck())          # Quack quack!
make_it_quack(Person())        # I am saying quack!
make_it_quack(Toy())           # Squeak quack!

# Another example of duck typing
class Phone:
    def charge(self):
        print("Phone is charging")

class Laptop:
    def charge(self):
        print("Laptop is charging")

class Book:
    def read(self):
        print("Reading the book")

def plug_in(device):
    try:
        device.charge()
    except AttributeError:
        print("Cannot charge this!")

for d in [Phone(), Laptop(), Book()]:
    plug_in(d)

# Magic method: Special methods with double underscores

# using __init__ method
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s1 = Student("Ram", 80)

print(s1)
# <__main__.Student object at 0x104b2a0d0>
print(s1.name)       # Ram
print(s1.marks)      # 80

# using __str__ method
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"{self.name} - {self.marks} marks"

s1 = Student("Ram", 80)
s2 = Student("Sita", 92)

print(s1)            # Ram - 80 marks
print(s2)            # Sita - 92 marks

text = str(s1)       # str() also uses __str__
print(text)          # Ram - 80 marks

# using __len__ method
class Basket:
    def __init__(self, fruits):
        self.fruits = fruits             # a list

    def __len__(self):
        return len(self.fruits)

b = Basket(["apple", "mango", "banana"])

print(len(b))        # 3

#using __add__ method
class Wallet:
    def __init__(self, money):
        self.money = money

    def __add__(self, other):
        return Wallet(self.money + other.money)

    def __str__(self):
        return f"Rs. {self.money}"

w1 = Wallet(500)
w2 = Wallet(300)

w3 = w1 + w2         # Python calls w1.__add__(w2)
print(w3)            # Rs. 800

# using __eq__ and __lt__ methods
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __eq__(self, other):
        return self.marks == other.marks

    def __lt__(self, other):
        return self.marks < other.marks

ram = Student("Ram", 80)
sita = Student("Sita", 92)
hari = Student("Hari", 80)

print(ram == hari)   # True    (80 == 80)
print(ram == sita)   # False
print(ram < sita)    # True    (80 < 92)
print(sita < ram)    # False

# Another example of magic methods
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"Book: {self.title}"

    def __len__(self):
        return self.pages

    def __add__(self, other):
        return self.pages + other.pages

b1 = Book("Muna Madan", 120)
b2 = Book("Python Basics", 300)

print(b1)
print(len(b2))
print(b1 + b2)

# File Handling
# Writing to a file
f = open("notes.txt", "w")      # open for writing

f.write("Hello Nepal\n")
f.write("Python is fun\n")

f.close()                       # always close!

# notes.txt now has:
# Hello Nepal
# Python is fun
 
# Other approach in better way: with open ()
with open("notes.txt", "w") as f:
    f.write("Hello Nepal\n")
    f.write("Python is fun\n")

# the file is closed here, by itself
print("Saved!")

# writelines(): write a whole list
fruits = ["apple\n", "mango\n", "banana\n"]

with open("fruits.txt", "w") as f:
    f.writelines(fruits)

# fruits.txt now has:
# apple
# mango
# banana

# Without \n
with open("fruits.txt", "w") as f:
    f.writelines(["apple", "mango", "banana"])

# fruits.txt: applemangobanana

# 3 ways to read a file
# 1. read(): read the whole file
with open("notes.txt", "r") as f:
    text = f.read()
print(text)

# 2. readlines(): a list of lines
with open("notes.txt", "r") as f:
    lines = f.readlines()
print(lines)   # ['Hello Nepal\n', 'Python is fun\n']

# 3. for loop: one line at a time
with open("notes.txt", "r") as f:
    for line in f:
        print(line.strip())

# 4. readline(): read one line at a time  
with open("notes.txt", "r") as f:
    first = f.readline()       # 1st line
    second = f.readline()      # 2nd line
    third = f.readline()       # no more lines

print(first.strip())           # Hello Nepal
print(second.strip())          # Python is fun
print(third == "")             # True  (empty string)      

# write vs append mode
# "w" deletes the old content first.
#"a" keeps the old content and adds new lines at the end.

# "w" deletes the old content!
with open("notes.txt", "w") as f:
    f.write("New day\n")
# notes.txt: New day     (old lines are gone)

# "a" keeps the old content, adds at the end
with open("notes.txt", "a") as f:
    f.write("Momo is tasty\n")
    f.write("Dal bhat power\n")

# notes.txt now has:
# New day
# Momo is tasty
# Dal bhat power

# "r+": read and write together
# Read first, then write: the new text goes at the end.
# Write first: it writes over the start of the file! "Sun" became "SUN".

# diary.txt has:
# Sunday: went to college

with open("diary.txt", "r+") as f:
    print(f.read())                    # 1. read first
    f.write("Monday: learned files\n") # 2. then write

# diary.txt now has:
# Sunday: went to college
# Monday: learned files

# Careful: write without reading first
with open("diary.txt", "r+") as f:
    f.write("SUN")       # writes at the start!

# diary.txt: SUNday: went to college ...

# when the file is missing
with open("marks.txt", "r") as f:
    print(f.read())
# FileNotFoundError: [Errno 2] No such file or directory: 'marks.txt'

# Safe version
try:
    with open("marks.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found. Check the name!")

# File not found. Check the name!

# Deleting a file
import os

os.remove("fruits.txt")          # fruits.txt is deleted

# Safe way: check first
if os.path.exists("fruits.txt"):
    os.remove("fruits.txt")
    print("Deleted!")
else:
    print("File not found")

# File not found   (we already deleted it)

# practise
with open("shop.txt", "w") as f:
    f.write("rice\n")
    f.write("dal\n")

with open("shop.txt", "a") as f:
    f.write("oil\n")

with open("shop.txt", "w") as f:
    f.write("salt\n")

with open("shop.txt", "a") as f:
    f.write("sugar\n")

with open("shop.txt", "r") as f:
    print(f.read())   # salt
                      # sugar

# Everything putting together:
class Contact:

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"{self.name}: {self.phone}"

contacts = [Contact("Ram", "9841000001"),
            Contact("Sita", "9851000002")]

# Save: str(c) uses __str__
with open("contacts.txt", "w") as f:
    for c in contacts:
        f.write(str(c) + "\n")

# Add one more later
with open("contacts.txt", "a") as f:
    f.write(str(Contact("Hari", "9861000003")) + "\n")

# Read and show
with open("contacts.txt", "r") as f:
    for line in f:
        print(line.strip())

# Ram: 9841000001
# Sita: 9851000002
# Hari: 9861000003