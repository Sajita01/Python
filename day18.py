# Abstract Class and Encapsulation

# Abstract class:A class that is only a plan; a plan that every child must follow(We cannot make an object from it. It only says what its children must have.)
# Module abc Comes with Python. Short for Abstract Base Class.
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass                    # no work here

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

print(Square(4).area())     # 16
print(Circle(2).area())     # 12.56

# Making an abstract class
from abc import ABC, abstractmethod     # 1.Import: from abc import ABC, abstractmethod

class Fruit(ABC):                       # 2.Inherit from ABC: class Fruit(ABC):
    @abstractmethod                     # 3.Put @abstractmethod above the "must have" method
    def taste(self):
        pass                            # 4.Write only pass inside it

class Apple(Fruit):                     # 5.Make children that override that method
    def taste(self):
        print("Sweet")

class Lemon(Fruit):                     # 5.Make children that override that method
    def taste(self):
        print("Sour")

Apple().taste()     # Sweet
Lemon().taste()     # Sour

# Rule 1: No object from the plan

s = Shape()
# TypeError: Can't instantiate abstract class Shape
# without an implementation for abstract method 'area'

sq = Square(4)       # a child is fine
print(sq.area())     # 16

# Rule 2: Every child must follow the plan
class Triangle(Shape):
    pass                     # forgot area()!

t = Triangle()
# TypeError: Can't instantiate abstract class Triangle
# without an implementation for abstract method 'area'

# Fix: write area() in the child
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

print(Triangle(6, 4).area())     # 12.0

# Normal methods are allowed too
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    def eat(self):                       # normal
        print(f"{self.name} is eating")

    @abstractmethod
    def sound(self):                     # must write
        pass

class Cow(Animal):
    def sound(self):
        print(f"{self.name} says Moo!")

c1 = Cow("Gauri")
c1.eat()        # Gauri is eating
c1.sound()      # Gauri says Moo!

# Every child has it, so loop safely
shapes = [Square(4), Circle(2), Triangle(6, 4)]

for s in shapes:
    print(s.area())

# 16
# 12.56
# 12.0

# Guess the output:
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class Esewa(Payment):
    def pay(self, amount):
        print(f"Paid Rs. {amount} with eSewa")

class Khalti(Payment):
    def pay(self, amount):
        print(f"Paid Rs. {amount} with Khalti")

class Cash(Payment):
    pass

Esewa().pay(500) # Paid Rs. 500 with eSewa
Khalti().pay(200) # Paid Rs. 200 with Khalti
Cash().pay(100) # TypeError: Can't instantiate abstract class Cash
# without an implementation for abstract method 'pay'

# Encapsulation: hiding the details of how a class works from the outside world. It has Public, protected and private data.

# Anyone can change anything
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

acc = BankAccount("Ram", 1000)

acc.balance = -50000       # nobody stops this!
print(acc.balance)         # -50000

acc.balance = "hello"      # or this!
print(acc.balance)         # hello

# 3 types of encapsulation written as self.name, self._name and self.__name. The first is public, the second is protected and the third is private.
# Public: No underscore. Open for everyone.
class Student:
    def __init__(self, name):
        self.name = name           # public

s1 = Student("Ram")
print(s1.name)        # Ram    (read from outside)

s1.name = "Hari"      # change from outside
print(s1.name)        # Hari

# Protected: one underscore _
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance     # protected

acc = BankAccount("Ram", 1000)

print(acc._balance)    # 1000   (works, but you shouldn't)
acc._balance = 5       # works too. Python trusts you

# Private: two underscores __
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance    # private

    def show(self):
        print(f"{self.owner}: Rs. {self.__balance}")

acc = BankAccount("Ram", 1000)
acc.show()          # Ram: Rs. 1000   (inside: OK)

print(acc.__balance)
# AttributeError: 'BankAccount' object has no attribute '__balance'

# Getter(read the value of a variable) and setter(write/change the value of a variable):
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def get_balance(self):                 # getter
        return self.__balance

    def deposit(self, amount):             # setter
        if amount > 0:
            self.__balance = self.__balance + amount
            print(f"Added Rs. {amount}")
        else:
            print("Amount must be more than 0")

acc = BankAccount("Ram", 1000)
acc.deposit(500)            # Added Rs. 500
acc.deposit(-200)           # Amount must be more than 0
print(acc.get_balance())    # 1500

# Marks must be 0 to 100
class Student:
    def __init__(self, name):
        self.name = name
        self.__marks = 0

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):    # A setter keeps the data correct.
        if marks >= 0 and marks <= 100:
            self.__marks = marks
        else:
            print("Marks must be 0 to 100")

s1 = Student("Sita")
s1.set_marks(85)
s1.set_marks(500)          # Marks must be 0 to 100
print(s1.get_marks())      # 85

# Guess the output
class ATM:
    def __init__(self, pin):
        self.__pin = pin

    def check(self, pin):
        if pin == self.__pin:
            print("Welcome!")
        else:
            print("Wrong PIN")

acc = ATM(1234)
acc.check(1111) # Wrong PIN
acc.check(1234) # Welcome!

acc.__pin = 1111  # makes a new, separate attribute
acc.check(1111) # Wrong PIN

# Put everything together: A bank account example;
from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance          # private

    def add_interest(self):
        interest = self.__balance * self.rate() / 100
        self.__balance = self.__balance + interest

    def show(self):
        print(f"{self.owner}: Rs. {self.__balance}")

    @abstractmethod
    def rate(self):                       # must write
        pass

class Savings(Account):
    def rate(self):
        return 5

class Fixed(Account):
    def rate(self):
        return 10

s = Savings("Ram", 1000)
f = Fixed("Sita", 1000)
s.add_interest()
f.add_interest()
s.show()      # Ram: Rs. 1050.0
f.show()      # Sita: Rs. 1100.0