# Ask the shopper a few questions, then print a neat receipt.
"""
01
Ask for name, item, price and quantity with input()
02
Change price to float and quantity to int
03
Show the name in Title Case and the item in CAPITALS
04
Make an item code from the first 3 letters (slicing)
05
Print the total with 2 decimals using an f-string
06
Use // and %: how many Rs 500 notes, and what is left
07
Print True/False: is the total over Rs 1000? Then print type(price)
"""

Customer = input ("Enter your name :") .strip().title()
item = input ("Enter the items name:") .strip().capitalize()
code = item[:3].upper()

quantity = int(input("Enter quantity: "))
price = float(input("Enter the item's price: "))

total = price * quantity

notes = total // 500
left = total % 500

print("\n--- Customer Bill ---")
print("Customer:", Customer)
print(f"Item :{item} (code: {code})")
print("Quantity:", quantity)
print(f"Total : Rs {total:.2f}")
print(f"500 notes: {int(notes)}, left Rs {left:.2f}")
print("Over 1000?", total > 1000)
print("Price type:", type(price))

"""
Output:
Enter your name :Riyaa
Enter the items name:Tika Set
Enter quantity: 5
Enter the item's price: 750

--- Customer Bill ---
Customer: Riyaa
Item :Tika set (code: TIK)
Quantity: 5
Total : Rs 3750.00
500 notes: 7, left Rs 250.00
Over 1000? True
Price type: <class 'float'>

"""