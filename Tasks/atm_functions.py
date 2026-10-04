# Take the Day 08 ATM and split it into functions. deposit() and withdraw() get the old balance and return the new one. The while True menu at the bottom stays almost the same.

# write check_pin(pin) that returns True or False
correct_pin = "1234"

def check_pin(pin):
    return pin == correct_pin


# ask for the PIN first, only 3 tries 
tries = 0
while tries < 3:
    pin = input("Enter your PIN: ")
    tries += 1

    if check_pin(pin):
        print("PIN correct! Welcome.")
        break
    else:
        print("Incorrect PIN.")

def show_menu():
    print("1. Balance  2. Deposit  3. Withdraw  4. Exit")

def deposit(balance, amount):
    if amount <= 0:
        print("Amount must be more than 0")
        return balance
    return balance + amount

def withdraw(balance, amount):
    if amount > balance:
        print("Not enough money")
        return balance
    return balance - amount

balance = 1000

while True:
    show_menu()
    choice = input("Choose (1-4): ").strip()

    if choice == "1":
        print(f"Balance: Rs. {balance}")
    elif choice == "2":
        amount = int(input("Amount to deposit: "))
        balance = deposit(balance, amount)
    elif choice == "3":
        amount = int(input("Amount to withdraw: "))
        balance = withdraw(balance, amount)
    elif choice == "4":
        print("Thank you! Bye")
        break
    else:
        print("Please choose 1 to 4")

