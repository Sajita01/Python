# Polymorphism in Python(One name, many forms)

class Car:
    def move(self):
        print("Car drives on the road")

class Boat:
    def move(self):
        print("Boat sails on the water")

class Plane:
    def move(self):
        print("Plane flies in the sky")

c1 = Car()
b1 = Boat()
p1 = Plane()

c1.move()     # Car drives on the road
b1.move()     # Boat sails on the water
p1.move()     # Plane flies in the sky

# One loop for all of them
vehicles = [Car(), Boat(), Plane()]

for v in vehicles:
    v.move()

# Car drives on the road
# Boat sails on the water
# Plane flies in the sky

# One function for all of them
def start_trip(vehicle):
    print("Trip started!")
    vehicle.move()

start_trip(Car())
# Trip started!
# Car drives on the road

start_trip(Plane())
# Trip started!
# Plane flies in the sky

#  Missing method
class House:
    def rooms(self):
        print("House has 5 rooms")

start_trip(Car())
# Trip started!
# Car drives on the road

start_trip(House())
# Trip started!
# AttributeError: 'House' object has no attribute 'move'

# Guess the Output:
class Nepali:
    def greet(self):
        print("Namaste")

class English:
    def greet(self):
        print("Hello")

class Japanese:
    def greet(self):
        print("Konnichiwa")

class Robot:
    def beep(self):
        print("Beep beep")

people = [Nepali(), English(), Japanese(), Robot()]

for p in people:
    p.greet()
# Namaste
# Hello
# Konnichiwa
# AttributeError: 'Robot' object has no attribute 'greet'

# Polymorphism with Inheritance: The parent gives a method. Each child changes it in its own way.

# Overriding is polymorphism
class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f"{self.name} flies high")

class Sparrow(Bird):
    pass                           # uses parent fly()

class Penguin(Bird):
    def fly(self):                 # override
        print(f"{self.name} cannot fly, it swims")

class Kiwi(Bird):
    def fly(self):                 # override
        print(f"{self.name} cannot fly, it runs")

for b in [Sparrow("Chiri"), Penguin("Pingu"), Kiwi("Kiki")]:
    b.fly()

# Chiri flies high
# Pingu cannot fly, it swims
# Kiki cannot fly, it runs

# Example: Salary for everyone
class Employee:
    def __init__(self, name):
        self.name = name

    def salary(self):
        return 20000

class Manager(Employee):
    def salary(self):              # override
        return 80000

class Intern(Employee):
    def salary(self):              # override
        return 10000

staff = [Employee("Ram"), Manager("Sita"), Intern("Hari")]

total = 0
for s in staff:
    print(s.name, s.salary())
    total = total + s.salary()

print("Total:", total)

# Ram 20000
# Sita 80000
# Hari 10000
# Total: 110000

# polymorphism with Abstract Classes: The parent gives a method. Each child must implement it in its own way.
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

class Card(Payment):
    def pay(self, amount):
        print(f"Paid Rs. {amount} with card")

def checkout(method, amount):
    method.pay(amount)

checkout(Esewa(), 500)      # Paid Rs. 500 with eSewa
checkout(Khalti(), 200)     # Paid Rs. 200 with Khalti
checkout(Card(), 1000)      # Paid Rs. 1000 with card

# Guess the output:
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w

class Dot(Shape):
    pass

for s in [Square(3), Rectangle(4, 5), Dot()]:
    print(s.area())
# 9      Square: 3 * 3
# 20     Rectangle: 4 * 5
# 0      Dot: uses the parent's area()

#  Method Overloading: One method name. Different inputs. Different work.
class Calculator:
    def add(self, a, b, c=0):          # default value
        return a + b + c

    def total(self, *args):            # any number
        return sum(args)

calc = Calculator()
print(calc.add(2, 3))                # 5
print(calc.add(2, 3, 4))             # 9

print(calc.total(1, 2))              # 3
print(calc.total(1, 2, 3, 4, 5))     # 15

# Guess the output:
class Greet:
    def hello(self, name="Friend", times=1):
        for i in range(times):
            print(f"Hello {name}")

g = Greet()
g.hello()    # Hello Friend
g.hello("Ram")  # Hello Ram
g.hello("Sita", 2)  # Hello Sita
                      # Hello Sita

# Polymorphism : all the forms
# Buit-in polymorphism:One function works on many types.
# Classes:Different classes, same method name.
# Overriding:Children change the parent's method.
# Abstract class:Every child must write the method.
# Overloading:One method name, different inputs, different work.

# Put all together
# Momo shop bill:Abstract class + overriding + one loop, in one example.
from abc import ABC, abstractmethod

class Food(ABC):
    def __init__(self, plates):
        self.plates = plates

    @abstractmethod
    def price(self):                  # every food must have it
        pass

class Momo(Food):
    def price(self):
        return self.plates * 150

class Chowmein(Food):
    def price(self):
        return self.plates * 120

class Pizza(Food):
    def price(self):
        return self.plates * 500

order = [Momo(2), Chowmein(1), Pizza(1)]

total = 0
for f in order:
    total = total + f.price()        # each food, its own price

print(f"Total bill: Rs. {total}")    # Total bill: Rs. 920