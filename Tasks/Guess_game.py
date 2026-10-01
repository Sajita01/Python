# Keep a secret number. The user keeps guessing until they get it right. Say Too low or Too high to help them. Count the tries.
import random

secret = random.randint(1, 100)
tries = 0

while tries < 7:
    guess = int(input("Guess (1 to 100): "))
    tries += 1

    if guess == secret:
        print(f"Correct! You took {tries} tries")
        break
    elif guess < secret:
        print("Too low")
    else:
        print("Too high")

if guess != secret:
    print(f"Game over! The secret number was {secret}")
