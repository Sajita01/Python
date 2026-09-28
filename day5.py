#Tuples and set
#tuples are immutable,and similar tolist but they locked the list

#Creating a tuple
fruits = ("apple", "banana", "cherry")
print(fruits)  # Output: ('apple', 'banana', 'cherry')  
print (type(fruits))  # Output: <class 'tuple'>

info   = ("Ram", 20, True)       # mixed types are OK
empty  = ()                      # empty tuple

nums = 1, 2, 3                   # brackets are optional
print(nums)                      # (1, 2, 3)

one = ("apple",)                 # one item: add a comma!
not_tuple = ("apple")            # this is just a string
#example
tup1 = ("apple",)
tup2 = ("banana")
print(type(tup1))  # Output: <class 'tuple'>
print(type(tup2))  # Output: <class 'str'>

#Indexing and slicing: Exactly the same as lists.
days = ("Sun", "Mon", "Tue", "Wed", "Thu")

print(days[0])      # Sun   first item
print(days[-1])     # Thu   last item
print(len(days))    # 5

print(days[1:3])    # ('Mon', 'Tue')
print(days[:2])     # ('Sun', 'Mon')
print(days[::-1])   # ('Thu', 'Wed', 'Tue', 'Mon', 'Sun')
#print(days[10])     # IndexError!

# We can't change a tuple:No editing, no append, no remove. But there's a trick.
# To replace tuple items 1st change to list and to tuple
fruits = ("apple", "banana")
#fruits[0] = "kiwi"        # TypeError! can't change

temp = list(fruits)       # 1. make it a list
temp[0] = "kiwi"          # 2. change it
fruits = tuple(temp)      # 3. make it a tuple again
print(fruits)             # ('kiwi', 'banana')

print(fruits + ("mango",))   # ('kiwi', 'banana', 'mango')
print(("hi",) * 3)           # ('hi', 'hi', 'hi')
del fruits                   # delete the whole tuple

#Tuple methods and functions: Only two methods: count() and index().
marks = (70, 90, 80, 90)

print(marks.count(90))    # output: 2   how many 90s
print(marks.index(80))    # output: 2   position of 80

print(len(marks))         # 4
print(max(marks))         # 90
print(min(marks))         # 70
print(sum(marks))         # 330
print(sorted(marks))      # [70, 80, 90, 90]  a list!
print(90 in marks)        # True
print((1, 2) == (2, 1))   # False cause they're not equal.

#packing and unpacking: Put values in together, then take them out into variables.
person = ("Ram", 20, "Pokhara")   # packing

name, age, city = person           # unpacking
print(name)      # output: Ram
print(age)       # output: 20

a, b = 1, 2
a, b = b, a      # swap values
print(a, b)      # output: 2 1
first, *rest = (1, 2, 3, 4)
print(rest)      # [2, 3, 4]Put a * before a name to collect all the extra items.

#swap
a,b= 5,10
print(f"Before swap: a={a}, b={b}")  # Output: Before swap: a=5, b=10
a,b=b,a
print(f"After swap: a={a}, b={b}")  # Output: After swap: a=10, b=5


#Nested tuple: A tuple inside a tuple, it can also hold lists.
#A list inside a tuple can still change, because only the tuple is locked.
student = ("Ram", (2008, 5, 14), ["Math"])
print(student[1])        # output: (2008, 5, 14)
print(student[1][0])     # output: 2008

student[2].append("Art")    # OK! the list can change
print(student)  # output: ('Ram', (2008, 5, 14), ['Math', 'Art'])



# Set: A bag of unique items: no duplicates, no order.
# A set can hold numbers, strings and tuples, but not lists.

#Creating a set

# Two ways to create a set.
# Method 1: Create a set directly
nums = {1, 2, 2, 3, 3, 3}
print(nums)            # output: {1, 2, 3} ,  duplicates gone

# Method 2: Convert a list into a set
nums = [1, 2, 2, 3, 3, 3]
print(set(nums))   # Output: {1, 2, 3}

print(set([1, 1, 2]))  # output: {1, 2} ,  list to set
print(set("aab"))      # {'a', 'b'}  any order

empty = set()          # the right way for empty
#set1=set()

# no index,no list inside set, but works by pop
colors = {"red", "blue", "green"}
print(colors)       # order may be different!
#print(colors[0]) # TypeError: 'set' object is not subscriptable

ok  = {1, "hi", (2, 3)}    # numbers, strings, tuples
# bad = {1, [2, 3]}  # TypeError: unhashable type: 'list',cause set can't hold lists


#Adding and removing items
#[remove() gives an error if the item is missing. discard() never gives an error, so it's the safe choice. ]

colors = {"red", "blue"}
colors.add("green")              # add one item
colors.add("red")                # already there: no change
colors.update(["pink", "gold"])  # add many items:for multiple color addition

colors.remove("pink")     # remove (error if missing)
colors.discard("black")   # remove (never an error)
colors.pop()              # remove a random item
colors.clear()            # empty it: set()
del colors                # delete the whole set

#Checking a set : in, len, max, min, sum and sorted all work.
nums = {4, 9, 1, 7}

print(9 in nums)        # True
print(5 not in nums)    # True
print(len(nums))        # 4
print(max(nums))        # 9
print(min(nums))        # 1
print(sum(nums))        # 21
print(sorted(nums))     # [1, 4, 7, 9]   a list

# Set operations in code

a = {1, 2, 3, 4}
b = {3, 4, 5}

print(a | b)    # {1, 2, 3, 4, 5}   a.union(b)
print(a & b)    # {3, 4}            a.intersection(b)
print(a - b)    # {1, 2}            a.difference(b)
print(b - a)    # {5}
print(a ^ b)    # {1, 2, 5}         a.symmetric_difference()

a |= b          # a is changed now: updates ;(the same as a.update(b)).
print(a)        # {1, 2, 3, 4, 5}

# Comparing sets:[Subset: all of A is inside B. Superset: A contains all of B. Disjoint: nothing in common]
small = {1, 2}
big   = {1, 2, 3, 4}

print(small <= big)            # True   subset
print(small.issubset(big))     # True
print(big >= small)            # True   superset
print(big.issuperset(small))   # True

print({1, 2}.isdisjoint({5, 6}))   # True
print({1, 2} == {2, 1})            # True , order doesn't matter.

#copy() and frozenset
a = {1, 2}
b = a            # same set, two names
c = a.copy()     # a real copy
a.add(3)
print(b)         # output:{1, 2, 3},changed too!
print(c)         # output:{1, 2},safe

#frozenset is a locked set, the way a tuple is a locked list.
f = frozenset([1, 2])
#f.add(3)        # AttributeError: can't change

# Best way to remove duplicates [Turn a list into a set, and all duplicates are gone.]

votes = ["tea", "coffee", "tea", "tea", "milk"]
unique = set(votes)
print(unique)           # output:{'tea', 'coffee', 'milk'}
print(len(unique))      # output:3
print(sorted(unique))   # output:['coffee', 'milk', 'tea']
print(len(votes) != len(unique))   # True: had duplicates

# We can't directly replace items from tuples.(concept:convert tuple to list -->edit --> Tuple)
temp = list(student)
temp[2] = "Kathmandu"
student = tuple(temp)



