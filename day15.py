# Exceptions and Exception Handling
# An exception is an error that occurs while a Python program is running and interrupts its normal execution.
age_text = "ten"
age = int(age_text)
print("Done")
 
# Traceback (most recent call last):
#   File "day-15.py", line 2, in <module>
#     age = int(age_text)
# ValueError: invalid literal for int() with base 10: 'ten'

# try and except
try:
    age = int(input("Enter your age: "))
    print("Next year you will be", age + 1)
except ValueError:
    print("Please type a number!")

print("Program continues...")

# Enter your age: 20
# Next year you will be 21
# Program continues...

# Enter your age: ten
# Please type a number!
# Program continues...

# More than one except
try:
    a = int(input("First number: "))
    b = int(input("Second number: "))
    print("Answer:", a / b)
except ValueError:
    print("Please type numbers only.")
except ZeroDivisionError:
    print("You can't divide by zero.")

# First number: 10
# Second number: 0
# You can't divide by zero.

# First number: 10
# Second number: abc
# Please type numbers only.

# See the message with as e: 
try:
    num = int("12abc")
except ValueError as e:    # as e saves the error in a variable called e
    print("Error:", e)     # e holds the error
# Error: invalid literal for int() with bas..e 10: '12abc'

# Two errors, one block: use a tuple
try:
    print(10 / 0)
except (ValueError, ZeroDivisionError) as e:
    print("Problem:", e)
# Problem: division by zero

# try, except, else, finally
def check_age(text):
    try:
        age = int(text)
    except ValueError:
        print("Not a number!")
    else:
        print("Your age is", age)
    finally:
        print("--- check done ---")

check_age("25")
# Your age is 25
# --- check done ---

check_age("abc")
# Not a number!
# --- check done ---


# Guess the output:
nums = [10, 20, 30]

try:
    print(nums[1])
    print(nums[5])
    print("A")
except IndexError:
    print("B")
else:
    print("C")
finally:
    print("D")

try:
    print(int("7.7") + 3)
except ValueError:
    print("E")
else:
    print("F")

print(10 / 0)
"""
Output:
20
B
D
E
Traceback (most recent call last):
ZeroDivisionError: division by zero

"""

# Exception handling with a loop
while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("That's not a number. Try again.")

print("Thanks! Your age is", age)

# Enter your age: twenty
# That's not a number. Try again.
# Enter your age: 2o
# That's not a number. Try again.
# Enter your age: 20
# Thanks! Your age is 20

# exception handling with a function
def get_number(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Numbers only, please!")

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Can't divide by zero"

x = get_number("First number: ")
y = get_number("Second number: ")
print(safe_divide(x, y))

# First number: 8
# Second number: zero
# Numbers only, please!
# Second number: 0
# Can't divide by zero

# raise means: make an error on purpose. We choose the error name and write our own message. 
age = 67

if age < 0:
    raise ValueError("Age can't be negative")

print("Age saved")    # never runs

# Traceback (most recent call last):
#   File "day-15.py", line 4, in <module>
#     raise ValueError("Age can't be negative")
# ValueError: Age can't be negative

# raise inside a function
def set_age(age):
    if age < 0:
        raise ValueError("Age can't be negative")
    print("Age saved:", age)

set_age(20)
# Age saved: 20

try:
    set_age(-5)
except ValueError as e:
    print("Error:", e)
# Error: Age can't be negative


#raise inside try, caught by except.
try:
    age = int(input("Enter your age: "))

    if age < 18 and age < 0:
        raise ValueError("Age must be 18 or above!")

    print("Access granted!")

except ValueError as e:
    print("Error:", e)

print("Program continues...")

# 20  → Access granted!
# 17  → Error: Age must be 18 or above!
# ten → Error: invalid literal for int() with base 10: 'ten'


def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Please type a number.")

# project time: Safe Calculator
print("=== Safe Calculator ===")

while True:
    a = get_number("First number: ")
    op = input("Choose + - * / % ** : ")
    b = get_number("Second number: ")

    try:
        if op == "+":
            print("Answer:", a + b)
        elif op == "-":
            print("Answer:", a - b)
        elif op == "*":
            print("Answer:", a * b)
        elif op == "/":
            print("Answer:", a / b)
        elif op == "%":              # add % (remainder)
            print("Answer:", a % b)    
        elif op == "**":               # ** (power)
            print("Answer:", a ** b)
        else:
            print("Unknown sign:", op)

    except ZeroDivisionError:
        print("You can't divide by zero!")

    again = input("Again? (y/n): ").lower()

    if again != "y":
        print("Calculator closed!")
        break

