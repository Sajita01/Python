# Three small recursive functions, each with a base case and a smaller step. n % 10 gives the last digit and n // 10 removes it. Fibonacci: each number is the sum of the two before it.

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def sum_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Power using recursion
def power(base, n):
    if n == 0:
        return 1
    return base * power(base, n - 1)


# Count vowels using recursion
def count_vowels(word):
    if word == "":
        return 0

    if word[0].lower() in "aeiou":
        return 1 + count_vowels(word[1:])

    return count_vowels(word[1:])


# Ask the user for a number
number = int(input("Enter a number: "))

print(number, "! =", factorial(number))
print("Sum of digits:", sum_digits(number))
print("2 to the power", number, "=", power(2, number))

word = input("Enter a word: ")
print("Number of vowels:", count_vowels(word))

print("Fibonacci:", end=" ")
for i in range(8):
    print(fibonacci(i), end=" ")
print()

"""
Output:
Enter a number: 27
27 ! = 10888869450418352160768000000
Sum of digits: 9
2 to the power 27 = 134217728
Enter a word: whatever
Number of vowels: 3
Fibonacci: 0 1 1 2 3 5 8 13

"""