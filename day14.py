# Decorators : Add extra behavior to a function without rewriting its original code.
# Functions are values
def greet():
    return "Namaste!"

say = greet          # no brackets: copy the function
print(say())         # Namaste!

def run_twice(func):
    func()
    func()

def hello():
    print("Hello!")

run_twice(hello)     # send hello, no brackets
# Hello!
# Hello!


# Wrap it by a hand
def my_decorator(func):
    def wrapper():
        print("----- start -----")
        func()
        print("----- end -----")
    return wrapper

def say_hello():
    print("Hello!")

say_hello = my_decorator(say_hello)
say_hello()
# ----- start -----
# Hello!
# ----- end -----

# use @ decorator as shorthand of decorator
def my_decorator(func):
    def wrapper():
        print("----- start -----")
        func()
        print("----- end -----")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

@my_decorator
def say_bye():
    print("Bye!")

say_hello()
say_bye()
# ----- start -----
# Hello!
# ----- end -----
# ----- start -----
# Bye!
# ----- end -----

# How a decorator looks

def my_decorator(func):
    def wrapper():
        func()
    return wrapper

# What happens, in order
def my_decorator(func):
    print("1. decorating", func.__name__)
    def wrapper():
        print("3. before")
        func()
        print("5. after")
    return wrapper

@my_decorator
def say_hello():
    print("4. Hello!")

print("2. now we call it")
say_hello()
# 1. decorating say_hello
# 2. now we call it
# 3. before
# 4. Hello!
# 5. after

# Decorate any function
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Calling", func.__name__)
        result = func(*args, **kwargs)
        print("Done")
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

total = add(3,4)
print(total)
# Calling add
# Done
# 7

# login check
logged_in = False

def login_required(func):
    def wrapper(*args, **kwargs):
        if not logged_in:
            print("Please log in first!")
            return
        return func(*args, **kwargs)
    return wrapper

@login_required
def see_balance():
    print("Balance: Rs. 5000")

see_balance()      # Please log in first!
logged_in = True
see_balance()      # Balance: Rs. 5000

# timer
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        taken = round(time.time() - start, 1)
        print(func.__name__, "took", taken, "sec")
        return result
    return wrapper

@timer
def slow_add(a, b):
    time.sleep(1)
    return a + b

print(slow_add(2, 3))
# slow_add took 1.0 sec
# 5

# stack decorator
def stars(func):
    def wrapper():
        print("*****")
        func()
        print("*****")
    return wrapper

def dashes(func):
    def wrapper():
        print("-----")
        func()
        print("-----")
    return wrapper

@stars
@dashes
def hello():
    print("Hello!")

hello()
# *****
# -----
# Hello!
# -----
# *****

# Guess the output

def double_it(func):
    def wrapper(n):
        return func(n) * 2
    return wrapper

def say(func):
    def wrapper():
        print("Before")
        func()
    return wrapper

@double_it
def add_ten(n):
    return n + 10

@say
def hi():
    print("Hi")

print(add_ten(5))
hi()
print(add_ten(0))
# add_ten()
"""
30
Before
Hi
20
"""
# Recursion : A function calls itself to solve a smaller version of the same problem.
# Day 08 way: a loop
def countdown_loop(n):
    while n > 0:
        print(n)
        n -= 1
    print("Go!")

# Recursion way
def countdown(n):
    if n == 0:            # base case: stop
        print("Go!")
        return
    print(n)
    countdown(n - 1)      # call itself, smaller n

countdown(3)
# 3
# 2
# 1
# Go!

# How recursion looks
def countdown(n):
    if n == 0:
        return
    countdown(n - 1)

# factorial with recursion
# 4! = 4 x 3 x 2 x 1 = 24
# 4! = 4 x 3!

def factorial(n):
    if n == 1:                      # base case
        return 1
    return n * factorial(n - 1)     # smaller step

print(factorial(4))    # 24
print(factorial(5))    # 120
print(factorial(10))   # 3628800

# More small recursion
# Add 1 + 2 + ... + n
def total(n):
    if n == 0:
        return 0
    return n + total(n - 1)

print(total(5))              # 15

# Reverse a word
def reverse(word):
    if word == "":
        return ""
    return reverse(word[1:]) + word[0]

print(reverse("what?"))       # omom

# Add all items in a list
def list_sum(nums):
    if len(nums) == 0:
        return 0
    return nums[0] + list_sum(nums[1:])

print(list_sum([4, 5, 6]))   # 15

"""
# No base case = RecursionError

def forever(n):
    print(n)
    forever(n + 1)      # no base case!

forever(1)
# 1
# 2
# ... (about 1000 times)
# RecursionError: maximum recursion depth exceeded

import sys
print(sys.getrecursionlimit())   # 1000

# Also wrong: n + 1 never reaches 0
# def countdown(n):
#     if n == 0:
#         return
#     countdown(n + 1)

"""

# Guess the output
def power(base, n):
    if n == 0:
        return 1
    return base * power(base, n - 1)

def count_down(n):
    if n == 0:
        return "Done"
    return count_down(n - 1)

def digits(n):
    if n < 10:
        return 1
    return 1 + digits(n // 10)

print(power(2, 3))
print(power(5, 0))
print(count_down(3))
print(digits(45))
print(digits(7))

# Generators: Give values one at a time, only when asked. The keyword is yield.
# return vs yeild
# return: gives back once, then the function ends
def get_numbers():
    return [1, 2, 3]

# yield: gives one value, pauses, then continues
def gen_numbers():
    yield 1
    yield 2
    yield 3

print(get_numbers())   # [1, 2, 3]
print(gen_numbers())   # <generator object gen_numbers at 0x...>

for n in gen_numbers():
    print(n)
# 1
# 2
# 3

# Ask for one value with next()

def gen_numbers():
    yield 1
    yield 2
    yield 3

g = gen_numbers()

print(next(g))    # 1
print(next(g))    # 2
print(next(g))    # 3
#print(next(g))    # StopIteration (no more values)

# yield pauses, next() continues
def steps():
    print("Start")
    yield "A"
    print("Middle")
    yield "B"
    print("End")

g = steps()        # nothing prints yet!

print(next(g))
# Start
# A

print(next(g))
# Middle
# B

# next(g) again prints End,
# then gives StopIteration

# yield inside a loop
def count_up(limit):
    n = 1
    while n <= limit:
        yield n
        n += 1

for num in count_up(5):
    print(num, end=" ")     # 1 2 3 4 5
print()

def evens(limit):
    for n in range(limit + 1):
        if n % 2 == 0:
            yield n

print(list(evens(10)))      # [0, 2, 4, 6, 8, 10]

# Endless, and used only once
# Endless: makes a new number only when asked
def token_numbers():
    n = 1
    while True:
        yield n
        n += 1

tokens = token_numbers()
print(next(tokens))      # 1
print(next(tokens))      # 2
print(next(tokens))      # 3

# Used only once
def count_up(limit):
    for n in range(1, limit + 1):
        yield n

nums = count_up(3)
print(list(nums))        # [1, 2, 3]
print(list(nums))        # []  (already used up!)

# Generator in one line 
# Square brackets: a list, made all at once

squares_list = [n * n for n in range(5)]
print(squares_list)         # [0, 1, 4, 9, 16]

# Round brackets: a generator, one by one
squares_gen = (n * n for n in range(5))

print(squares_gen)          # <generator object <genexpr> at 0x...>
print(list(squares_gen))    # [0, 1, 4, 9, 16]

# Inside a function call, one pair of brackets is enough
print(sum(n * n for n in range(5)))   # 30

# Generators save memory : Produce values one at a time using yield, pausing between values.

import sys

big_list = list(range(1000000))
big_gen = (n for n in range(1000000))

print(sys.getsizeof(big_list))   # 8000056  (about 8 MB)
print(sys.getsizeof(big_gen))    # 200      (tiny!)

print(sum(big_list))             # 499999500000
print(sum(big_gen))              # 499999500000

# Guess the output
def letters(word):
    for ch in word:
        yield ch.upper()

def squares(n):
    for i in range(1, n + 1):
        yield i * i

g = letters("hi")
print(next(g))
print(next(g))
print(list(squares(4)))
print(sum(squares(3)))

s = squares(2)
print(list(s))
print(list(s))
# print(next(g))
"""
Output:
H
I
[1, 4, 9, 16]
14
[1, 4]
[]

"""



