# Remember the calculator from Day 03? Now it can't be broken. get_number() keeps asking until it gets a number, and try / except catches dividing by zero.

def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Please type a number.")


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