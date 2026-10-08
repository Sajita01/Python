# Each sign in the dictionary points to a lambda. operations[sign] picks the lambda, and (a, b) calls it. A while loop keeps asking until the user types q. split() and if checks handle bad input.

operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else "Can't divide by 0",
    "%": lambda a, b: a % b,  # add "%" for the remainder 
    "**": lambda a, b: a ** b,
}

print("Type like: 8 + 2   (or q to quit)")
while True:
    text = input("> ").strip()
    if text.lower() == "q":
        print("Bye!")
        break
    parts = text.split()
    if len(parts) != 3:
        print("Please type: number sign number")
        continue
    a, sign, b = parts
    if sign not in operations:
        print(f"Unknown sign: {sign}")
        continue
    result = operations[sign](float(a), float(b))
    print("=", result)


# what happens if you type: abc + 2 ?
#ValueError: could not convert string to float: 'abc'

"""
Output:
Type like: 8 + 2   (or q to quit)
> 45 / 5
= 9.0
> 32 * 98
= 3136.0
> 67 % 2
= 1.0
> q
Bye!

"""