# Class and Object: A class is a blueprint for making objects. An object is an instance of a class. A class can have data (attributes) and actions (methods).
# Why Classes?When data and actions belong together.
print(type("hello"))      # <class 'str'>
print(type([1, 2, 3]))    # <class 'list'>
print(type(5))            # <class 'int'>

name = "ram"              # name is a str object
print(name.upper())       # RAM

fruits = ["apple"]        # fruits is a list object
fruits.append("mango")
print(fruits)             # ['apple', 'mango']

# Small example of a class and object:An empty blueprint. 
class Student:
    pass              # empty for now

s1 = Student()        # make an object
s2 = Student()        # make another object

print(type(s1))       # <class '__main__.Student'>

class Student:
    pass          # This tells Python: "Leave this class empty for now, don't throw an error."

s1 = Student()
s1.name = "Ram"       # s1's name
s1.age = 20           # s1's age

s2 = Student()
s2.name = "Sita"      # s2's name
s2.age = 21           # s2's age

print(s1.name)        # Ram
print(s2.name)        # Sita

# __init__ and self : self is the object itself and  It is always the first input of a method. __init__ runs automatically when an object is made.

class Student:
    def __init__(self, name, age): # runs automatically when an object is made
        self.name = name          # save data inside the object
        self.age = age

s1 = Student("Ram", 20)
s2 = Student("Sita", 21)

print(s1.name, s1.age)     # Ram 20
print(s2.name, s2.age)     # Sita 21

############
class Student:
    def __init__(self, name, age):
        self.name = name     # 3. save "Ram"
        self.age = age       # 4. save 20

s1 = Student("Ram", 20)

# 1. new empty object   -> self
# 2. __init__(self, "Ram", 20)
# 5. s1 = the finished object

print(s1.name)    # Ram
print(s1.age)     # 20

# Starting values and changing data
class Student:
    def __init__(self, name, age):
        self.name = name     # from the input
        self.age = age       # from the input
        self.marks = 0       # same start for everyone

s1 = Student("Ram", 20)
print(s1.marks)     # 0

s1.marks = 85       # change it
print(s1.marks)     # 85

# Each object has its own data
s1 = Student("Ram", 20)
s2 = Student("Sita", 21)

s1.age = 25         # change only s1

print(s1.age)       # 25
print(s2.age)       # 21   (no change)

# Guess the output
class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
        self.battery = 100

m1 = Mobile("Samsung", 30000)
m2 = Mobile("Redmi", 18000)

m1.battery = 40

print(m1.brand, m1.battery)  # Samsung 40
print(m2.brand, m2.battery)  # Redmi 100
print(m1.price + m2.price)   # # 48000

# Methods: Functions that live inside a class. They are the object's actions.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, I am {self.name}")

s1 = Student("Ram", 20)
s2 = Student("Sita", 21)

s1.greet()      # Hi, I am Ram
s2.greet()      # Hi, I am Sita

# Methods with inputs: a bank account
# A method can change the object's data, and use if/else like any function.
class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Added Rs. {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money!")
        else:
            self.balance = self.balance - amount
            print(f"Took Rs. {amount}")

acc = BankAccount("Ram")
acc.deposit(1000)      # Added Rs. 1000
acc.withdraw(300)      # Took Rs. 300
acc.withdraw(5000)     # Not enough money!
print(acc.balance)     # 700

# A method that returns a value
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def is_square(self):
        return self.length == self.width

r1 = Rectangle(5, 3)
r2 = Rectangle(4, 4)

print(r1.area())         # 15
print(r2.area())         # 16
print(r1.is_square())    # False
print(r2.is_square())    # True

# Guess the output:
class Cart:
    def __init__(self, owner):
        self.owner = owner
        self.items = []

    def add(self, item):
        self.items.append(item)

    def count(self):
        return len(self.items)

c1 = Cart("Ram")
c2 = Cart("Sita")

c1.add("momo")
c1.add("tea")
c2.add("chowmein")

print(c1.count()) # 2
print(c2.items)   # ['chowmein']
print(f"{c1.owner} has {c1.count()} items") # Ram has 2 items

# Put everything together
class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []

    def add_mark(self, mark):
        self.marks.append(mark)

    def average(self):
        return sum(self.marks) / len(self.marks)

    def report(self):
        avg = self.average()
        if avg >= 40:
            print(f"{self.name}: {avg} Pass")
        else:
            print(f"{self.name}: {avg} Fail")

s1 = Student("Ram")
s1.add_mark(80)
s1.add_mark(70)
s1.report()       # Ram: 75.0 Pass