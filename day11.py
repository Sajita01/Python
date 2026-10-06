# args and kwargs 
# *args collects all positional values into a tuple i.e. collects values
# **kwargs collects all keyword arguments into a dictionary i.e. name=value pairs

def my_function(*args, **kwargs):

    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

# Without *args/**kwargs: the function has a fixed number of parameters.
def add(a, b):
    return a + b

print(add(2, 3))        # 5

# print(add(2, 3, 4))
# TypeError: add() takes 2 positional
# arguments but 3 were given

# Put a * before the name
def add(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print(add(2, 3))              # 5
print(add(2, 3, 4))           # 9
print(add(10, 20, 30, 40))    # 100
print(add())                  # 0

#  Python packs the values into a tuple.
def show(*args):
    print(args)
    print(type(args))
    print(len(args))

show("momo", "tea", "dal")
# ('momo', 'tea', 'dal')
# <class 'tuple'>
# 3

show()
# ()
# <class 'tuple'>
# 0

#
def add(*args):
    return sum(args)

def add(*numbers):
    return sum(numbers)

def add(*prices):
    return sum(prices)

print(add(100, 50, 25))    # 175

# The * is the magic part, not the name.

#  built-ins love *args
def report(*marks):
    print(f"Count:   {len(marks)}")
    print(f"Total:   {sum(marks)}")
    print(f"Highest: {max(marks)}")
    print(f"Lowest:  {min(marks)}")
    print(f"Sorted:  {sorted(marks)}")

report(67, 45, 92, 78)
# Count:   4
# Total:   282
# Highest: 92
# Lowest:  45
# Sorted:  [45, 67, 78, 92]

# Normal parameters + *args
def greet(greeting, *names):
    for name in names:
        print(f"{greeting}, {name}!")

greet("Namaste", "Ram", "Sita", "Hari")
# Namaste, Ram!
# Namaste, Sita!
# Namaste, Hari!

greet("Hello", "Gita")
# Hello, Gita!

# How Python fills the boxes
def greet(greeting, *names):
    print("greeting =", greeting)
    print("names    =", names)

greet("Namaste", "Ram", "Sita", "Hari")
# greeting = Namaste
# names    = ('Ram', 'Sita', 'Hari')

greet("Namaste")
# greeting = Namaste
# names    = ()

# print() uses *args too!

# Inside Python, print looks like this:
# def print(*values, sep=" ", end="\n"):

print("a")
print("a", "b", "c")
print("a", "b", "c", "d", "e", sep="-")

# a
# a b c
# a-b-c-d-e

# After *args, use the name
def total(*prices, discount=0):
    amount = sum(prices)
    return amount - amount * discount / 100

print(total(100, 200, 300))
# 600.0

print(total(100, 200, 300, discount=10))
# 540.0   (10% off)

print(total(100, 200, 300, 10))
# 610.0   (oops! 10 became a price)

# practise
def count(*things):
    return len(things)

def first(*things):
    return things[0]

def join_all(sep, *words):
    return sep.join(words)

print(count(1, 2, 3))
print(count())
print(first("tea", "coffee"))
print(join_all("7", "a", "b", "c"))
#print(first())

# Two Stars: **kwargs
def profile(**info):
    print(info)
    print(type(info))

profile(name="Ram", age=21, city="Pokhara")
# {'name': 'Ram', 'age': 21, 'city': 'Pokhara'}
# <class 'dict'>

profile()
# {}
# <class 'dict'>


# Loop through kwargs
def profile(**info):
    for key, value in info.items():
        print(f"{key}: {value}")
    print("----")

profile(name="Sita", age=22, city="Kathmandu")
# name: Sita
# age: 22
# city: Kathmandu
# ----

profile(name="Hari", hobby="football")
# name: Hari
# hobby: football
# ----

# Use .get() for missing options
def order_tea(**options):
    sugar = options.get("sugar", 1)
    milk = options.get("milk", "yes")
    print(f"Tea: sugar={sugar}, milk={milk}")
    print(f"Options sent: {len(options)}")

order_tea(sugar=2)
# Tea: sugar=2, milk=yes
# Options sent: 1

order_tea(sugar=0, milk="no")
# Tea: sugar=0, milk=no
# Options sent: 2

# Normal parameters + **kwargs
def student(name,**marks):
    print(f"Student: {name}")
    for subject, mark in marks.items():
        print(f"  {subject}: {mark}")
    print(f"Total: {sum(marks.values())}")

student("Gita", math=88, science=76, english=91)
# Student: Gita
#   math: 88
#   science: 76
#   english: 91
#   Total: 255

# **kwargs only takes name=value
def profile(**info):
    print(info)

profile(name="Ram")        # {'name': 'Ram'}

#profile("Ram")
# TypeError: profile() takes 0 positional
# arguments but 1 was given

#profile(first name="Ram")
# SyntaxError: invalid syntax
# (a space is not allowed in a name)

profile(first_name="Ram")  # OK

# practise
def info(**details):
    return details

def count(**details):
    return len(details)

print(info(a=1, b=2))
print(count(x=10, y=20, z=30))
print(info())      
                    # {'a': 1, 'b': 2}
                    # 3
                    # {}

def momo(plate, **extras):
    print(f"{plate} momo")
    for name, amount in extras.items():
        print(f"- {name} x{amount}")

momo("Buff", achar=2, soup=1)
                 #Buff momo
                 #- achar x2
                 #- soup x1
momo("Veg")
                 # Veg momo

# using Normal, *args and **kwargs in one function.
def demo(a, *args,b=0, **kwargs):
    print("a      =", a)
    print("args   =", args)
    print("b      =", b)
    print("kwargs =", kwargs)

demo(1, 2,7,8,9,3, x=10, y=20)
# a      = 1
# args   = (2, 7, 8, 9, 3)
# b      = 0
# kwargs = {'x': 10, 'y': 20}

demo(1)
# a      = 1
# args   = ()
# kwargs = {}

# Calling: plain values first
def demo(*args, **kwargs):
    print(args, kwargs)

demo(1, 2, x=3)      # (1, 2) {'x': 3}
demo(x=3)            # () {'x': 3}
demo(1, 2)           # (1, 2) {}

# demo(x=3, 1, 2)
# SyntaxError: positional argument
# follows keyword argument

# practise
def mix(first, *args, **kwargs):
    print(first, args, kwargs)

mix(1)
mix(1, 2, 3)
mix(1, b=2)
mix(1, 2, c=3, d=4)
# mix(a=1) : TypeError: mix() missing 1 required positional argument: 'first'
  # 1 () {}
  # 1 (2, 3) {}
  # 1 () {'b': 2}
  # 1 (2,) {'c': 3, 'd': 4}

# * opens a list
def add(a, b, c):
    return a + b + c
nums = [10, 20, 30]

# Long way
print(add(nums[0], nums[1], nums[2]))   # 60

# Short way
print(add(*nums))                        # 60
# add(*nums) is the same as add(10, 20, 30)

# print() + * = clean output
fruits = ["apple", "mango", "banana"]

print(fruits)              # ['apple', 'mango', 'banana']
print(*fruits)             # apple mango banana
print(*fruits, sep=", ")   # apple, mango, banana

print(*fruits, sep="\n")
# apple
# mango
# banana

print(*"Nepal")            # N e p a l

# ** opens a dictionary
def profile(name, age, city):
    print(f"{name}, {age}, from {city}")

ram = {"name": "Ram", "age": 21, "city": "Pokhara"}

profile(**ram)
# Ram, 21, from Pokhara

# profile(**ram) is the same as
# profile(name="Ram", age=21, city="Pokhara")

#  Unpack into *args
def total(*prices):
    return sum(prices)

cart = [120, 80, 250]
more = (50, 30)

print(total(*cart))           # 450
print(total(*cart, *more))    # 530
print(total(*cart, 100))      # 550
#print(total(cart))
# TypeError: unsupported operand type(s)
# for +: 'int' and 'list'   (forgot the *)


# practise 
marks = [92, 78, 67, 45, 30]

first, *rest = marks
print(first)      # 92
print(rest)       # [78, 67, 45, 30]

top, *middle, last = marks
print(top, last)  # 92 30
print(middle)     # [78, 67, 45]

# practise
def area(length, width):
    return length * width

size = [5, 4]
room = {"length": 3, "width": 6}
names = ["Ram", "Sita", "Hari"]

print(area(*size))  # 20
print(area(**room)) # 18
print(*names, sep=" | ") # Ram | Sita | Hari

first, *others = names
print(others)    # ['Sita', 'Hari']
print(area(*[ 2, 3]))  # 6
#print(area(*[1, 2, 3])) : TypeError: area() takes 2 positional arguments but 3 were given
