# Python Built-in Functions

name = "nepal"
fruits = ["mango", "apple"]

# Function: name(value)
print(len(name))          # 5
print(len(fruits))        # 2

# Method: value.name()
print(name.upper())       # NEPAL
fruits.append("banana")
print(fruits)             # ['mango', 'apple', 'banana']

# hidden settings of print()
print("Ram", "Sita", "Hari")
# Ram Sita Hari

print("Ram", "Sita", "Hari", sep=", ")
# Ram, Sita, Hari

print("2026", "10", "01", sep="-")
# 2026-10-01

for i in range(1, 6):
    print(i, end=" ")
# 1 2 3 4 5


# input() always gives text

age = input("Your age: ")      # user types 25
print(type(age))               # <class 'str'>
print(age + "1")               # 251   (text joined!)

age = int(input("Your age: "))
print(type(age))               # <class 'int'>
print(age + 1)                 # 26


# type() and isinstance()

print(type(10))          # <class 'int'>
print(type(9.5))         # <class 'float'>
print(type("hi"))        # <class 'str'>
print(type([1, 2]))      # <class 'list'>

print(isinstance(10, int))      # True
print(isinstance("10", int))    # False

# practise

print("a", "b", "c", sep="")
print(int("7") + int(3.9))
print(str(5) + str(5))
print(float(4))
print(bool(" "))
print(len(set("hello")))
print(int("10"))

# abs() and round()
print(abs(-15))            # 15
print(abs(15))             # 15

print(round(4.6))          # 5
print(round(4.4))          # 4
print(round(3.14159, 2))   # 3.14

bill = 1000 / 3
print(bill)                # 333.3333333333333
print(round(bill, 2))      # 333.33

# From 5 degrees down to -3 degrees: how big a drop?
print(abs(-3 - 5))         # 8

#pow() and divmod()
print(pow(2, 3))           # 8
print(pow(2, 3, 3))        # 2
print(divmod(10, 3))       # (3, 1)
print(5//2 , 5%2)          # (2, 1 )

# min(), max() and sum()
marks = [67, 45, 92, 78, 55]

print(min(marks))          # 45
print(max(marks))          # 92
print(sum(marks))          # 337

print(max(10, 25, 7))      # 25
prices = {"tea": 20, "momo": 150, "coffee": 50}
print(sum(prices.values()))   # 220
print(max(prices.values()))   # 150
print(max(prices))            # tea  (biggest key, A to Z)

# the long way vs the short way
marks = [67, 45, 92, 78]

# Long way (Day 08)
total = 0
biggest = marks[0]
for m in marks:
    total += m
    if m > biggest:
        biggest = m
print(total, biggest)           # 282 92

# Short way (today)
print(sum(marks), max(marks))   # 282 92

# Average in one line
def average(numbers):
    return round(sum(numbers) / len(numbers), 2)

marks = [67, 45, 92, 78, 55]
print(average(marks))           # 67.4

temps = [21.5, 24.0, 19.8]
print(average(temps))           # 21.77

# print(abs(-7) + abs(3))
print(round(9.87, 1))
print(pow(3, 2))
print(divmod(20, 6))

prices = [120, 80, 250, 50]
print(f"Cheapest: {min(prices)}")
print(f"Costliest: {max(prices)}")
print(f"Total: {sum(prices)}")

# Collection Functions : len, sorted, reversed, enumerate, zip, any and all.
print(len("Kathmandu"))              # 9
print(len("Hi there"))               # 8  (space counts)
print(len([10, 20, 30]))             # 3
print(len((1, 2)))                   # 2
print(len({"a", "b", "a"}))          # 2  (no duplicates)
print(len({"tea": 20, "momo": 150})) # 2

password = input("Password: ")
if len(password) < 8:
    print("Too short")

# sorted() vs .sort()
marks = [67, 45, 92, 78]

print(sorted(marks))                # [45, 67, 78, 92]
print(sorted(marks, reverse=True))  # [92, 78, 67, 45]
print(marks)                        # [67, 45, 92, 78]  (same)

print(sorted("python"))   # ['h', 'n', 'o', 'p', 't', 'y']
print(sorted({3, 1, 2}))  # [1, 2, 3]

prices = {"tea": 20, "momo": 150, "coffee": 50}
print(sorted(prices))     # ['coffee', 'momo', 'tea']

# reversed(): back to front
nums = [1, 2, 3, 4, 5]

print(reversed(nums))         # <list_reverseiterator object ...>
print(list(reversed(nums)))   # [5, 4, 3, 2, 1]

for n in reversed(range(1, 4)):
    print(n)
print("Go!")
# 3
# 2
# 1
# Go!
# enumerate(): number every item
fruits = ["apple", "mango", "banana"]

# Old way (Day 08 homework)
count = 1
for fruit in fruits:
    print(f"{count}. {fruit}")
    count += 1

# New way
for num, fruit in enumerate(fruits, start=1):
    print(f"{num}. {fruit}")

# Both print:
# 1. apple
# 2. mango
# 3. banana

# zip(): combine two lists
names = ["Ram", "Sita", "Hari"]
marks = [78, 92, 35]

for name, mark in zip(names, marks):
    print(f"{name} got {mark}")

# Ram got 78
# Sita got 92
# Hari got 35

report = dict(zip(names, marks))     # Day 06
print(report)
# {'Ram': 78, 'Sita': 92, 'Hari': 35}

# any() and all()
results = [True, True, False]
print(all(results))     # False: not all of them
print(any(results))     # True: at least one

marks = [78, 92, 35, 64]
passed = []
for m in marks:
    passed.append(m >= 40)

print(passed)           # [True, True, False, True]
print(all(passed))      # False: someone failed
print(any(passed))      # True: someone passed

# Sort your own way with key=
words = ["momo", "tea", "chowmein", "dal"]

print(sorted(words))
# ['chowmein', 'dal', 'momo', 'tea']   (A to Z)

print(sorted(words, key=len))
# ['tea', 'dal', 'momo', 'chowmein']   (short to long)

print(max(words, key=len))   # chowmein  (longest)
print(min(words, key=len))   # tea       (first shortest)

# Don't use built-in names for variables
sum = 0                 # bad name!
for n in [1, 2, 3]:
    sum += n
print(sum)              # 6

print(sum([4, 5]))
# TypeError: 'int' object is not callable

# Good names
total = 0
items = [1, 2, 3]
text = "hello"

names = ["Sita", "Ram", "Gita"]
ages = [21, 19, 23]

print(len(names))
print(sorted(names))
print(list(reversed(ages)))
print(max(ages) - min(ages))

for i, name in enumerate(names, start=1):
    print(i, name)

for name, age in zip(names, ages):
    print(f"{name} is {age}")

