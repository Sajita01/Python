# A famous interview question! Print 1 to 15. If a number divides by 3, print Fizz. By 5, print Buzz. By both, print FizzBuzz. Otherwise print the number.
count = 0 
for n in range(1, 51):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
        count += 1
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
print(f"Fizz was printed {count} times")
