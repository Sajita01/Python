#  The generator never ends (while True), but it only makes a new token when next() asks. A while loop keeps asking until the user types q.


# Generator for bank tokens
def token_machine(prefix):
    n = 1
    while True:
        yield f"{prefix}-{n}"
        n += 1


# Generator for countdown
def countdown(n):
    while n >= 1:
        yield n
        n -= 1


# Create two separate token machines
normal_tokens = token_machine("A")
vip_tokens = token_machine("V")

print("=== Bank Token Machine ===")

while True:
    choice = input("Press Enter for a token (q to quit): ")

    if choice.lower() == "q":
        print("Bye!")
        break

    customer_type = input("Normal or VIP? ").strip().lower()

    if customer_type == "normal":
        print("Your token:", next(normal_tokens))
    elif customer_type == "vip":
        print("Your token:", next(vip_tokens))
    else:
        print("Invalid choice. Please enter normal or vip.")

# Countdown 

print("Next in", end=" ")

for number in countdown(3):
    print(number, end=" ")

print()

"""
=== Bank Token Machine ===
Press Enter for a token (q to quit): 1
Normal or VIP? vip
Your token: V-1
Press Enter for a token (q to quit): 667
Normal or VIP? vip
Your token: V-2
Press Enter for a token (q to quit): a
Normal or VIP? normal
Your token: A-1
Press Enter for a token (q to quit): q
Bye!
Next in 3 2 1 

"""