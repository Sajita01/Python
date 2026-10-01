#  Start with Rs. 1000 in the account. Show the menu again and again with while True. The user can check the balance, deposit, withdraw (only if there is enough money) or exit with break.

balance = 1000
correct_pin = "1234"
tries = 0

# PIN verification
while tries < 3:
    pin = input("Enter your PIN: ")
    tries += 1

    if pin == correct_pin:
        print("PIN correct! Welcome.")
        break
    else:
        print("Incorrect PIN.")

if pin != correct_pin:
    print("Too many incorrect attempts. Account locked.")
else:
    while True:
        print("1. Balance  2. Deposit  3. Withdraw  4. Exit")
        choice = input("Choose (1-4): ").strip()

        if choice == "1":
            print(f"Balance: Rs. {balance}")

        elif choice == "2":
            amount = int(input("Amount to deposit: "))

            if amount <= 0:
                print("Deposit must be greater than 0")
            else:
                balance += amount
                print(f"New balance: Rs. {balance}")

        elif choice == "3":
            amount = int(input("Amount to withdraw: "))

            if amount > balance:
                print("Not enough money")
            else:
                balance -= amount
                print(f"Take your cash. Left: Rs. {balance}")

        elif choice == "4":
            print("Thank you! Bye")
            break

        else:
            print("Please choose 1 to 4")