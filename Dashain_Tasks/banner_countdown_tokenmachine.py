# Banner, Countdown and Token Machine using Decorators, recursion, generators


# 01. Create a decorator dashain_banner that prints a line before and after any function.
def dashain_banner(func):
    def wrapper(*args, **kwargs):
        print("*** Happy Dashain ***")
        func(*args, **kwargs)
        print("*********************")
    return wrapper


# 02. Decorate greet(name, gift="tika") with @ and call it twice.
@dashain_banner
def greet(name, gift="tika"):
    print(f"{name} gets a {gift}!")


greet("Sita")
greet("Ram", gift="kite")


# 03. Create recursive countdown(n),Print days left, then "Tika day!" at 0.
def countdown(n):
    if n == 0:
        print("Tika day!")
        return

    print(n, "days left")
    countdown(n - 1)


countdown(5)


# 04. Create recursive sum_digits(n),sum_digits(2026) should return 10.
def sum_digits(n):
    if n == 0:
        return 0

    last_digit = n % 10
    remaining_digits = n // 10

    return last_digit + sum_digits(remaining_digits)

print("Digit sum:", sum_digits(2026))


# 05. Create a generator token_machine(start)that yields T-101, T-102, T-103 ... forever.
def token_machine(start):
    while True:
        yield f"T-{start}"
        start = start + 1


tokens = token_machine(101)

# 06. Get four tokens using next().
print(next(tokens), next(tokens), next(tokens),next(tokens))


# also Use a one-line generator to sum squares from 1 to 5.
total = sum(number ** 2 for number in range(1, 6))

print("Sum of squares:", total)

"""
Output:
*** Happy Dashain ***
Sita gets a tika!
*********************
*** Happy Dashain ***
Ram gets a kite!
*********************
5 days left
4 days left
3 days left
2 days left
1 days left
Tika day!
Digit sum: 10
T-101 T-102 T-103 T-104
Sum of squares: 55

"""