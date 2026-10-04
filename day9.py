#function
# Without a function: copy, copy, copy
print("=====================")
print("Welcome to Momo House")
print("=====================")
print("=====================")
print("Welcome to Momo House")
print("=====================")

# With a function: write it once
def welcome():
    print("=====================")
    print("Welcome to Momo House")
    print("=====================")

welcome()
welcome()
welcome()
welcome()

#Define first, call later
def say_hello():
    print("Hello!")
    print("Welcome to class")

# Nothing has printed so far!

say_hello()       # call it: now it runs
say_hello()       # call it again  
# Output: # Hello!
# Welcome to class
# Hello!
# Welcome to class

#Functions and loops together
def show_stars():
    for i in range(1, 4):
        print("*" * i)

for n in range(2):
    show_stars()  # *
                  # **
                  # ***
                  # *
                  # **
                  # ***

#practise

def line():
    print("~~~~~~~~~~~~~~")

def happy():
    print("Happy Dashain!")

line()
happy()
line()

#parameters: Send values into a function
def greet(name):
    print(f"Namaste, {name}!")

greet("Ram")
greet("Sita")
greet("Hari")    # Namaste, Ram!
                 # Namaste, Sita!
                 # Namaste, Hari!

# More than one parameter: Separate them with commas also the order matters.
def introduce(name, age):
    print(f"I am {name}. I am {age} years old.")

introduce("Gita", 21)
introduce(21, "Gita")        # wrong order!
                             # I am Gita. I am 21 years old.
                            # I am 21. I am Gita years old.

# Send the right number of values
def add(a, b):
    print(a + b)

add(5, 3)        # 8

#add(5)
# TypeError: add() missing 1 required

#add(5, 3, 1)
# TypeError: add() takes 2 positional
# arguments but 3 were given

#Default values: A value to use when the caller sends nothing.
#value will override the default if the caller sends a value. 

def order_tea(name, sugar=1):
    print(f"{name}: tea with {sugar} sugar")

order_tea("Ram")          # uses the default 1
order_tea("Sita", 2)      # 2 overrides the default
order_tea("Hari", 0)

# Ram: tea with 1 sugar
# Sita: tea with 2 sugar
# Hari: tea with 0 sugar

#Call with the box name i.e. function parameter name.name=value. Now the order doesn't matter.

def introduce(name, age):
    print(f"I am {name}. I am {age} years old.")

introduce(name="Gita", age=21)
introduce(age=21, name="Gita")     # same answer

# I am Gita. I am 21 years old.
# I am Gita. I am 21 years old.

#Send a list or a dictionary
def show_menu(menu):
    print("--- MENU ---")
    for item, price in menu.items():
        print(f"{item}: Rs. {price}")

tea_shop = {"tea": 20, "coffee": 50}
momo_shop = {"veg momo": 120, "chicken momo": 150}

show_menu(tea_shop)
show_menu(momo_shop)

# --- MENU ---
# tea: Rs. 20
# coffee: Rs. 50
# --- MENU ---
# veg momo: Rs. 120
# chicken momo: Rs. 150

#practice
def box(word, symbol="#"):
    line = symbol * (len(word) + 4)
    print(line)
    print(f"{symbol} {word} {symbol}")
    print(line)

box("Nepal")
box("Hi", "*")
box(symbol="+", word="Python")

#return: Get an answer back from the function, and keep it.
def x(a, b):
    return a + b   # It send a value back to the place where we called the function,
    
result = x(2, 3)
print(result)                  # 5

total = x(100, 50) + x(10, 5)
print(total)                   # 165

print(x(7, 8) * 2)           # 30


# Forgot return? You get None
def add(a, b):
    print(a + b)      # shows it, doesn't return it

result = add(2, 3)    # prints 5
print(result)         # None

# return stops the function

def check_result(mark):
    if mark >= 40:
        return "Pass"
    return "Fail"
    print("This never prints")

print(check_result(75))     # Pass
print(check_result(30))     # Fail

status = check_result(55)
print(f"Ram: {status}")     # Ram: Pass

#Return True or False
def is_even(n):
    return n % 2 == 0

print(is_even(4))    # True
print(is_even(7))    # False

numbers = [3, 8, 10, 5, 6, 2]
count = 0
for n in numbers:
    if is_even(n):
        count += 1

print(f"{count} even numbers")    # 4 even numbers

#Return more than one value
def lowest_highest(marks):
    return min(marks), max(marks)

marks = [67, 45, 92, 78]

result = lowest_highest(marks)
print(result)               # (45, 92)

low, high = lowest_highest(marks)
print(f"Lowest: {low}")     # Lowest: 45
print(f"Highest: {high}")   # Highest: 92

# practise
def double(n):
    return n * 2

def shout(word):
    return word.upper() + "!"

x = double(5)
print(x + 1)
print(double(double(3)))

y = shout("hello")
print(y)

#What happens inside, stays inside : Local variables
def make_bill():
    bill = 500
    print(f"Inside: {bill}")

make_bill()          # Inside: 500

#print(bill)
# NameError: name 'bill' is not defined

# Same name, different boxes

x = 50
def change():
    x = 99
    print(f"Inside: {x}")
    print(f"Outside: {x}") 

change()                 # Inside: 99
print(f"Outside: {x}")   # Outside: 50

# The clean way:
def add_ten(n):
    return n + 10

x = add_ten(x)
print(x)                 # 20

# Functions that use functions

def subtotal(price, qty):
    return price * qty

def add_vat(amount):
    return amount + amount * 13 / 100

def bill_total(price, qty):
    before = subtotal(price, qty)
    return add_vat(before)

print(subtotal(150, 2))     # 300
print(add_vat(300))         # 339.0 ;here 300 = amount
print(bill_total(150, 2))   # 339.0


# Explain your function using help() or docstring. A docstring is a note for people, right under def.
def area(length, width):
    """Return the area of a room."""
    return length * width

print(area(12, 10))     # 120

help(area)

# area(length, width)
#     Return the area of a room.
#
# Press q to leave help

#practice
score = 0

def add_points(points):
    global score
    score = points
    print(f"Inside: {score}")

add_points(10)
add_points(5)
print(f"Final score: {score}")