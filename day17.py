# Method Overloading and Inheritance
# Method overloading means one method name that works with different inputs: fewer inputs, more inputs, or different kinds

# Method overloading ways 1: Default Values
class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

calc = Calculator()

print(calc.add(2, 3))       # 5    (c = 0)
print(calc.add(2, 3, 4))    # 9    (c = 4)

#  Way 1 + if statement
class Student:
    def __init__(self, name):
        self.name = name

    def greet(self, time=""):
        if time == "":
            print(f"Hi, I am {self.name}")
        else:
            print(f"Good {time}, I am {self.name}")

s1 = Student("Ram")
s1.greet()               # Hi, I am Ram
s1.greet("morning")      # Good morning, I am Ram

# Way 2: *args for any number
class Calculator:
    def add(self, *numbers):
        return sum(numbers)

calc = Calculator()

print(calc.add(5))               # 5
print(calc.add(5, 10))           # 15
print(calc.add(5, 10, 15, 20))   # 50

# Example: Momo Shop 
class MomoShop:
    def order(self, item="buff momo", plates=1):
        price = 150 * plates
        print(f"{plates} plate {item}: Rs. {price}")

shop = MomoShop()

shop.order()                    # 1 plate buff momo: Rs. 150
shop.order("chicken momo")      # 1 plate chicken momo: Rs. 150
shop.order("veg momo", 3)       # 3 plate veg momo: Rs. 450

# Guess the output
class Greeter:
    def hello(self, name="friend", times=1):
        for i in range(times):
            print(f"Hello, {name}!")

g = Greeter()

g.hello()   # Hello, friend!
g.hello("Sita")   # Hello, Sita!
g.hello("Hari", 2)   # Hello, Hari! 
                     # Hello, Hari!


#Inheritance: A child class gets everything from its parent class.
"""
class Dog:
    def __init__(self, name):
        self.name = name

    def eat(self):                       # same
        print(f"{self.name} is eating")

    def bark(self):
        print("Woof!")

class Cat:
    def __init__(self, name):
        self.name = name

    def eat(self):                       # same again!
        print(f"{self.name} is eating")

    def meow(self):
        print("Meow!")
"""

# A child can also add its own methods
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} says Meow!")

d1 = Dog("Tommy")
c1 = Cat("Kitty")

d1.eat()       # Tommy is eating
d1.bark()      # Tommy says Woof!
c1.eat()       # Kitty is eating
c1.meow()      # Kitty says Meow!

a1 = Animal("Lion")
a1.eat()       # Lion is eating

#a1.bark()
# AttributeError: 'Animal' object has no attribute 'bark'

c1 = Cat("Kitty")
#c1.bark()
# AttributeError: 'Cat' object has no attribute 'bark'

d1 = Dog("Tommy")
a1 = Animal("Lion")

print(isinstance(d1, Dog))      # True
print(isinstance(d1, Animal))   # True  (a Dog is an Animal)
print(isinstance(a1, Dog))      # False (not every Animal is a Dog)

# Other names you may hear:
# parent class = base class  = super class
# child class  = derived class = sub class

# Guess the output
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        self.wheels = 4

    def start(self):
        print(f"{self.brand} started")

class Bike(Vehicle):
    def ring(self):
        print("Tring tring!")

b1 = Bike("Honda")
b1.start() # Honda started
b1.ring() # Tring tring!
print(b1.wheels) # 4

#Overriding and super(): When the child wants to do things its own way.
# Method overriding means the child writes a method with the same name as the parent's method.
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):              # override
        print("Woof!")

class Cat(Animal):
    def sound(self):              # override
        print("Meow!")

class Fish(Animal):
    pass                          # no override

Dog("Tommy").sound()     # Woof!
Cat("Kitty").sound()     # Meow!
Fish("Nemo").sound()     # Some sound

# One loop, many animals
animals = [Dog("Tommy"), Cat("Kitty"), Fish("Nemo")]

for a in animals:
    print(a.name, end=": ")
    a.sound()

# Tommy: Woof!
# Kitty: Meow!
# Nemo: Some sound

# child needs extra data
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, school):
        self.school = school       # only school is saved

s1 = Student("Ram", 20, "Skill Shikshya")
print(s1.school)    # Skill Shikshya

#print(s1.name)
# AttributeError: 'Student' object has no attribute 'name'


#super() to the rescue: super().__init__(name, age) asks the parent: "please save name and age for me".Then the child saves only its own new data. 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)   # parent saves name, age
        self.school = school          # child saves school

s1 = Student("Ram", 20, "Skill Shikshya")

print(s1.name)      # Ram
print(s1.age)       # 20
print(s1.school)    # Skill Shikshya

# Keep the parent's work, add more:super() works with normal methods too.
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hi, I am {self.name}")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def introduce(self):
        #super().introduce()                # parent's part
        print(f"I teach {self.subject}")   # child's part

t1 = Teacher("Siyaa", "Python")
t1.introduce()
# Hi, I am Siyaa
# I teach Python

# Guess the output
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        self.wheels = 4

    def info(self):
        print(f"{self.brand} has {self.wheels} wheels")

class Bike(Vehicle):
    def __init__(self, brand):
        super().__init__(brand)
        self.wheels = 2

car = Vehicle("Toyota")
bike = Bike("Honda")

car.info()  # Toyota has 4 wheels
bike.info() # Honda has 2 wheels
print(bike.brand) # Honda

# Overloading vs overriding
# Overloading is Same method name, different inputs.
# Overriding is Child re-writes a parent's method.

# Types of Inheritance
# 1.Single inheritance: One parent → one child.
class Father:
    def house(self):
        print("I have a house")

class Son(Father):
    def bike(self):
        print("I have a bike")

s = Son()
s.house()     # I have a house
s.bike()      # I have a bike

# 2.Multilevel inheritance: Grandfather → Father → Son. A chain.One parent → one child → another child.
class Grandfather:
    def land(self):
        print("Land from grandfather")

class Father(Grandfather):
    def house(self):
        print("House from father")

class Son(Father):
    def bike(self):
        print("My own bike")

s = Son()
s.land()      # Land from grandfather
s.house()     # House from father
s.bike()      # My own bike

# 3.Hierarchical inheritance: One parent → many children.
class Person:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f"{self.name} is walking")

class Student(Person):
    def study(self):
        print(f"{self.name} is studying")

class Teacher(Person):
    def teach(self):
        print(f"{self.name} is teaching")

s = Student("Ram")
t = Teacher("Sita")

s.walk()      # Ram is walking
t.walk()      # Sita is walking
s.study()     # Ram is studying
t.teach()     # Sita is teaching

# 4.Multiple inheritance: Many parents → one child.
class Father:
    def height(self):
        print("Tall like father")

class Mother:
    def eyes(self):
        print("Brown eyes like mother")

class Child(Father, Mother):
    pass

c = Child()
c.height()    # Tall like father
c.eyes()      # Brown eyes like mother

# 5. Hybrid inheritance: A mix of two or more types.
class Person:
    def breathe(self):
        print("Breathing")

class Student(Person):
    def study(self):
        print("Studying")

class Worker(Person):
    def work(self):
        print("Working")

class Intern(Student, Worker):
    pass

i = Intern()
i.breathe()   # Breathing
i.study()     # Studying
i.work()      # Working

# Puttin everything together: A bank account example;
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Added Rs. {amount}")

    def show(self):
        print(f"{self.owner}: Rs. {self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, rate=5):
        super().__init__(owner, balance)
        self.rate = rate

    def add_interest(self):
        interest = self.balance * self.rate / 100
        self.deposit(interest)

acc = SavingsAccount("Ram", 1000)
acc.deposit(500)       # Added Rs. 500
acc.add_interest()     # Added Rs. 75.0
acc.show()             # Ram: Rs. 1575.0
