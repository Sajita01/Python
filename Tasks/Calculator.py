# Remember the Day 03 calculator? Now every operation gets its own function that returns the answer. A while True loop from Day 08 keeps the calculator running until the user types q.
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Can't divide by 0"
    return a / b


def power(a, b):
    return a ** b


while True:
    op = input("Choose + - * / ** (or q to quit): ")

    if op == "q":
        print("Bye!")
        break

    x = float(input("First number: "))
    y = float(input("Second number: "))

    match op:
        case "+":
            print(add(x, y))

        case "-":
            print(subtract(x, y))

        case "*":
            print(multiply(x, y))

        case "/":
            print(divide(x, y))

        case "**":
            print(power(x, y))

        case _:
            print("Unknown sign")