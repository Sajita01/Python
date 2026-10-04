# Write two small functions that return the converted temperature. Use float(input()) so the user can type 36.6 too.

def c_to_f(c):
    return c * 9 / 5 + 32


def f_to_c(f):
    return (f - 32) * 5 / 9


# print(c_to_f(100))     # 212.0
# print(f_to_c(50))      # 10.0

# ask: C to F, or F to C? 
choice = input("C to F, or F to C? ").strip().lower()

if choice == "C to F".lower():
    temp = float(input("Temperature in Celsius: "))
    print(f"That is {c_to_f(temp)} F")

elif choice == "F to C".lower():
    temp = float(input("Temperature in Fahrenheit: "))
    print(f"That is {f_to_c(temp)} C")

else:
    print("Invalid choice")

# Returns True if temperature is above 30

def is_hot(c):
    return c > 30

"""
Output:
C to F, or F to C? c to f
Temperature in Celsius: 50
That is 122.0 F

C to F, or F to C? f to c
Temperature in Fahrenheit: 122
That is 50.0 C

"""
