# Dashain countdown and savings jar
"""
Part A uses a for loop. Part B is a menu that keeps running until you quit.
01
Part A: loop through days 1 to 15 with range()
02
On day 7 print Day 7: Fulpati! and continue
03
On day 10 print the tika day message and break
04
Part B: a while True menu: 1 Add, 2 Spend, 3 Balance, 4 Quit
05
Spending more than you have? Print a warning and continue
06
Wrong choice: print a message. Choice 4: say bye and break

"""

# Part A: Dashain Countdown (for loop)

for day in range(1, 16):

    if day == 7:
        print("Day 7: Fulpati!")
        continue

    if day == 10:
        print("Day 10: Vijaya Dashami, tika day!")
        break

    print("Day", day)

# Part B: Savings Jar(while loop)

balance = 0

while True:

    choice = input("1 Add  2 Spend  3 Balance  4 Quit: ")

    # Add money
    if choice == "1":
        amount = int(input("Amount: "))
        balance = balance + amount

    # Spend money
    elif choice == "2":
        amount = int(input("Amount: "))

        # Check whether enough money is available
        if amount > balance:
            print("Not enough money!")
            continue

        balance = balance - amount

    # Display the current balance
    elif choice == "3":
        print("Balance: Rs", balance)

    # Quit the program
    elif choice == "4":
        print("Bye! Happy Dashain.")
        break

    # Handle an invalid menu choice
    else:
        print("Wrong choice, try again.")

"""
Output:
Day 1
Day 2
Day 3
Day 4
Day 5
Day 6
Day 7: Fulpati!
Day 8
Day 9
Day 10: Vijaya Dashami, tika day!
1 Add  2 Spend  3 Balance  4 Quit: 2
Amount: 700
Not enough money!
1 Add  2 Spend  3 Balance  4 Quit: 3
Balance: Rs 0
1 Add  2 Spend  3 Balance  4 Quit: 1
Amount: 1000
1 Add  2 Spend  3 Balance  4 Quit: 2
Amount: 700
1 Add  2 Spend  3 Balance  4 Quit: 3
Balance: Rs 300
1 Add  2 Spend  3 Balance  4 Quit: quit
Wrong choice, try again.
1 Add  2 Spend  3 Balance  4 Quit: 4
Bye! Happy Dashain.

"""