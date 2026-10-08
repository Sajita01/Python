# Lambda Functions : A small function written in one line, with no name.

# def vs lambda: same job
def double(x):
    return x * 2

# The lambda way
double_it = lambda x: x * 2

print(double(5))       # 10
print(double_it(5))    # 10
print(double_it(7))    # 14

# Turn a def into a lambda
# Before: normal function
def add(a, b):
    return a + b

# After: lambda
add_lambda = lambda a, b: a + b

print(add(3, 4))           # 7
print(add_lambda(3, 4))    # 7
print(add_lambda(10, 20))  # 30

# Zero, one or many inputs
hello = lambda: "Namaste!"
square = lambda n: n * n
area = lambda length, width: length * width
greet = lambda name, msg="Hello": f"{msg}, {name}!"
total = lambda *nums: sum(nums)

print(hello())              # Namaste!
print(square(6))            # 36
print(area(5, 4))           # 20
print(greet("Ram"))         # Hello, Ram!
print(greet("Sita", "Hi"))  # Hi, Sita!
print(total(10, 20, 30))    # 60

#  Decisions: if ... else
mark = 55

if mark >= 40:
    result = "Pass"
else:
    result = "Fail"

# One-line way
result = "Pass" if mark >= 40 else "Fail"
print(result)       # Pass

# Inside a lambda
check = lambda m: "Pass" if m >= 40 else "Fail"
print(check(55))    # Pass
print(check(30))    # Fail

# Only one expression
# Good: one expression
square = lambda n: n * n

# Bad: return is not allowed
# lambda n: return n * n
# SyntaxError: invalid syntax

# Bad: a normal if block is not allowed
# lambda n: if n > 0: "yes"
# SyntaxError: invalid syntax

# Good: use the one-line if instead
sign = lambda n: "yes" if n > 0 else "no"
print(sign(5))      # yes

###
add = lambda a, b: a + b
shout = lambda word: word.upper() + "!"
is_even = lambda n: n % 2 == 0
bigger = lambda a, b: a if a > b else b

print(add(2, 3))
print(add("momo", "tea"))
print(shout("namaste"))
print(is_even(7))
print(bigger(10, 25))
# print(add(5)) : missing 1 required positional argument: 'b'

# Lambda + key=
words = ["banana", "kiwi", "apple", "fig","papaya"]

# Day 10: a built-in function as key
print(sorted(words, key=len))
# ['fig', 'kiwi', 'apple', 'banana', 'papaya']

# Today: your own rule with lambda
# sort by the last letter
print(sorted(words, key=lambda w: w[-1])) # It checks the last index if each word
#['banana', 'papaya', 'apple', 'fig', 'kiwi']
print(sorted(words, key=lambda w: w[1])) # chech 1st index of each words
#['banana', 'papaya', 'kiwi', 'fig', 'apple']
#

# How key= works
words = ["banana", "kiwi", "apple", "fig"]
last = lambda w: w[-1]

for w in words:
    print(w, "->", last(w))
# banana -> a
# kiwi -> i
# apple -> e
# fig -> g
 
print(sorted(words, key=last))    ###
# ['banana', 'apple', 'fig', 'kiwi']


# Sort a list of tuples
students = [("Ram", 92), ("Sita", 78), ("Hari", 65)]

print(sorted(students))
# [('Hari', 65), ('Ram', 92), ('Sita', 78)]

print(sorted(students, key=lambda s: s[1]))
# [('Hari', 65), ('Sita', 78), ('Ram', 92)]

print(sorted(students, key=lambda s: s[1], reverse=True))
# [('Ram', 92), ('Sita', 78), ('Hari', 65)]

# Find the topper
students = [("Ram", 92), ("Sita", 78), ("Hari", 65)]

top = max(students, key=lambda s: s[1])
low = min(students, key=lambda s: s[1])

print(top)     # ('Ram', 92)
print(low)     # ('Hari', 65)

name, mark = top
print(f"Topper: {name} with {mark}")
# Topper: Ram with 92

# sort with dictionaries
students = [
    {"name": "Ram", "marks": 92},
    {"name": "Sita", "marks": 78},
]
best = max(students, key=lambda s: s["marks"])
print(best["name"])          # Ram
print(best) # {'name': 'Ram', 'marks': 92}

menu = {"momo": 150, "tea": 30, "lassi": 80}
cheap_first = sorted(menu.items(), key=lambda item: item[1])
print(cheap_first)
# [('tea', 30), ('lassi', 80), ('momo', 150)]

# practise
words = ["Python", "is", "very", "fun"]
nums = [-7, 3, -1, 5]
team = [("Ram", 21), ("Sita", 19), ("Hari", 25)]

print(sorted(words, key=lambda w: len(w)))
print(sorted(words, key=len))
print(sorted(nums, key=lambda n: abs(n)))
print(max(team, key=lambda p: p[1]))
print(min(team, key=lambda p: p[1])[0])
print(sorted(words, key=lambda w: w.lower()))
print(sorted(words))
"""
['is', 'fun', 'very', 'Python']
['is', 'fun', 'very', 'Python']
[-1, 3, 5, -7]
('Hari', 25)
Sita
['fun', 'is', 'Python', 'very']
['Python', 'fun', 'is', 'very']

"""
# map() and filter(): Change every item, or keep only some items.

prices = [100, 250, 80]

# Day 08 way: a loop
new_prices = []
for p in prices:
    new_prices.append(p + 20)
print(new_prices)       # [120, 270, 100]

# map + lambda way
new_prices = list(map(lambda p: p + 20, prices))
print(new_prices)       # [120, 270, 100]

# map() with any function
# A built-in function: no lambda needed
marks = "67 45 92".split()
print(marks)                    # ['67', '45', '92']
print(list(map(int, marks)))    # [67, 45, 92]

# A string method with lambda
names = ["ram", "sita", "hari"]
print(list(map(lambda n: n.title(), names)))
# ['Ram', 'Sita', 'Hari']

# Your own def function (no brackets!)
def square(n):
    return n * n
print(list(map(square, [1, 2, 3])))   # [1, 4, 9]


# Why do we need list()?
nums = [1, 2, 3]
result = map(lambda n: n * 10, nums)
#print(result)    # to print the actual result, use list()
# <map object at 0x10f3a2b90>

print(list(result))   # [10, 20, 30]
print(list(result))   # []   (already used up!)

# Tip: make the list once, use it many times
tens = list(map(lambda n: n * 10, nums))
print(tens, sum(tens))   # [10, 20, 30] 60


# filter(): keep only some items
marks = [67, 35, 92, 28, 54]

# (loop + if)logic
passed = []
for m in marks:
    if m >= 40:
        passed.append(m)
print(passed)      # [67, 92, 54]

# filter + lambda way
passed = list(filter(lambda m: m >= 40, marks))
print(passed)      # [67, 92, 54]

words = ["momo", "tea", "chowmein", "dal"]
print(list(filter(lambda w: len(w) > 3, words)))
# ['momo', 'chowmein']


# Use them together
marks = [67, 35, 92, 28, 54]

passed = filter(lambda m: m >= 40, marks)
bonus = map(lambda m: m + 5, passed)
final = list(bonus)

print(final)          # [72, 97, 59]
print(sum(final))     # 228
print(max(final))     # 97

# All in one line (harder to read!)
print(list(map(lambda m: m + 5, filter(lambda m: m >= 40, marks))))
# [72, 97, 59]

# practise
nums = [1, 2, 3, 4, 5]
names = ["ram", "sita", "gopi"]

print(list(map(lambda n: n * n, nums)))
print(list(filter(lambda n: n > 2, nums)))
print(list(map(len, names)))
print(list(map(lambda n: n.upper(), names)))
print(list(filter(lambda n: "a" in n, names)))
print(list(map(lambda n: n + 1, nums)))

"""
[1, 4, 9, 16, 25]
[3, 4, 5]
[3, 4, 4]
['RAM', 'SITA', 'GOPI']
['ram', 'sita']
[2, 3, 4, 5, 6]

"""