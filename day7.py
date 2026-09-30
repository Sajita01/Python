#Python Condition
#if condition : run it or skip it
age = int(input("Your age: "))

if age >= 18:
    print("You can vote")
    print("Bring your ID card")

print("Thank you!")

#if...else condition: Two paths. Exactly one of them runs
age = int(input("Your age: "))

if age >= 18:
    print("You can vote")
else:
    print("Too young to vote") # Your age: 25  ->  You can vote
                               # Your age: 17  ->  Too young to vote

#if...elif...else : More than two choices? Add elif
marks = int(input("Your marks: "))

if marks >= 80:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Fail")               # 90 -> Grade A      65 -> Grade B
                                # 50 -> Grade C      30 -> Fail

#Order matters :Put the hardest condition first
marks = 90

# Wrong order
if marks >= 40:
    print("Grade C")       # runs, and stops here
elif marks >= 80:
    print("Grade A")       # never checked

# Right order
if marks >= 80:
    print("Grade A")       # runs
elif marks >= 40:
    print("Grade C")

#Join conditions with and, or, not.(and: both sides must be True. or: at least one side must be True. not: flips True to False, and False to True.)
age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("Enjoy the movie")      # both True

day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("Holiday!")             # one is True

is_raining = False
if not is_raining:
    print("Let's play outside")   # not False = True

#if with in

fruits = ["apple", "mango", "banana"]
if "mango" in fruits:
    print("We have mango")

email = "ram@gmail.com"
if "@" not in email:
    print("Invalid email")
else:
    print("Email looks OK")

####
prices = {"tea": 20, "coffee": 50}
item = input("Order: ")
if item in prices:
    print(f"Price: Rs. {prices[item]}")
else:
    print("Sorry, not on the menu")

#if/else with different strings
answer = input("Do you like Python? ")

if answer.strip().lower() == "yes":
    print("Great! Me too")
else:
    print("You will soon!")

# yes, YES and " Yes " all print: Great! Me too

name = input("Your name: ")
if len(name) > 10:
    print("That is a long name")

#Empty Values ( empty value counts as False.)
name = input("Your name: ")

if name:
    print(f"Hello, {name}")
else:
    print("You didn't type anything")

cart = []
if not cart:
    print("Your cart is empty")

print(bool(0), bool(""), bool([]))       # False False False
print(bool(5), bool("hi"), bool([1]))    # True True True

# Nested if
username = input("Username: ")
password = input("Password: ")

if username == "admin":
    if password == "1234":
        print("Welcome, admin!")
    else:
        print("Wrong password")
else:
    print("User not found")

# if / elif vs match-case
day = input("Day: ")

# with if / elif
if day == "sat":
    print("Holiday")
elif day == "fri":
    print("Half day")
else:
    print("School day")

# with match-case (Use it,when there is multiples cases)
match day:
    case "sat":
        print("Holiday")
    case "fri":
        print("Half day")
    case _:
        print("School day")


