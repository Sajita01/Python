#LOOPS
# for loop : run one item per round. When the items finish, the loop ends

fruits = ["apple", "mango", "banana"]
for fruit in fruits:
    print(fruit)

print("Done!")        # after the loop: runs once

#Indentation matters here
names = ["Ram", "Sita", "Hari"]

for name in names:
    print(f"Hello, {name}")    # inside: runs 3 times
print("Class started")         # outside: runs 1 time


#Loop over a string
word = "Nepal"
for letter in word:
    print(letter)

#Range ()
for i in range(5):
    print(i)      # 0
                  # 1
                  # 2
                  # 3
                  # 4
print(list(range(5)))    # [0, 1, 2, 3, 4]

#range() in different ways :start, stop, step
for i in range(10,1,-1):
    print(i)

#Adding up with a loop (Start with 0, then add one by one)
total = 0
for num in range(1, 6):
    total += num          # same as total = total + num
    print(f"Added {num}, total is {total}")

print(f"Final total: {total}")

# Added 1, total is 1
# Added 2, total is 3
# Added 3, total is 6
# Added 4, total is 10
# Added 5, total is 15
# Final total: 15

#Loop over tuples and dictionaries
colors = ("red", "green", "blue")     # tuple
for c in colors:
    print(c)

##
prices = {"tea": 20, "coffee": 50, "momo": 150}
for item in prices:                   # keys only
    print(item)

for item, price in prices.items():     # for k, v in prices.items():	key in k, value in v
    print(f"{item}: Rs. {price}")      # tea: Rs. 20
                                       # coffee: Rs. 50
                                       # momo: Rs. 150

#Loop and if together

marks = [45, 80, 32, 67, 25]
passed = 0
for m in marks:
    if m >= 40:
        print(f"{m}: Pass")
        passed += 1
    else:
        print(f"{m}: Fail")

print(f"{passed} students passed") # 45: Pass
                                   # 80: Pass
                                   # 32: Fail
                                   # 67: Pass
                                   # 25: Fail
                                   # 3 students passed

#practise
for n in range(1, 4):
    print(n * 10)
print("---")

##
total = 0
for price in [20, 50, 30]:
    total += price
print("Total:", total)

##
for letter in "Hi":
    print(letter)

#while Loop :Keep repeating while a condition is True.
#It Check, run, check again. False? Stop.

count = 1
while count <= 5:
    print(count)
    count += 1
print("Done!")  # 1
                # 2
                # 3
                # 4
                # 5
                # Done!

#while Loop With input()

tasks = []
task = input("Add a task (or 'quit'): ")

while task != "quit":
    tasks.append(task)
    task = input("Add a task (or 'quit'): ")

print("Your tasks:", tasks)

#for vs while
# for: Python counts for you
for i in range(1, 6):
    print(i)

# while ConditionHIHI: you do the counting
i = 1
while i <= 5:
    print(i)
    i += 1     # Both print 1 2 3 4 5

#practise
n = 10
while n > 0:
    print(n)
    n -= 1
print("Liftoff!")

# Break and Continue : Break stops the loop. continue skips one round.
#break
numbers = [4, 9, 10, 7, 15]

for n in numbers:
    if n >= 10:
        print(f"Found a big one: {n}")
        break
    print(f"{n} is small")
print("Loop over")    # 4 is small
                      # 9 is small
                      # Found a big one: 10
                      # Loop over

# Continue
for n in range(1, 8):
    if n == 4:
        continue        # skip 4
    print(n)            # output: 1 2 3 5 6 7

# while True: loop until break
while True:
    choice = input("Type 'hi' or 'exit': ").strip().title()

    if choice == "Exit":
        print("Bye!")
        break
    elif choice == "hi":
        print("Hello there!")
    else:
        print("I don't know that one")

# Nested Loops

for row in range(1, 4):
    for col in range(1, 6):
        if col == 2 and row == 1:
            continue
        print(f"{row} x {col} = {row * col}")
    print("---")        # 1 x 1 = 1
                        # 1 x 3 = 3
                        # 1 x 4 = 4
                        # 1 x 5 = 5
                        #------                        # 2 x 1 = 2  #2 x 2 = 4
                        # ... and so on until 3 x 5 = 15

#practise
for n in range(1, 10):
    if n % 2 != 0:
        continue
    if n > 7: 
        break
    print(n)


for i in range(1, 4):
    print("*" * i)
