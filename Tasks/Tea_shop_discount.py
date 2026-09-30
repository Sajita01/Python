#Show the menu dictionary. Ask for an item. If it's on the menu, ask how many and print the total. If not, say sorry. Then give a discount with if / elif / else.

menu = {"tea": 20, "coffee": 50, "momo": 150}
print("Menu:", menu)

item = input("What do you want? ").strip().lower()

if item in menu:
    qty = int(input("How many? "))
    total = menu[item] * qty
    print(f"Total: Rs. {total}")

    if total >= 500:
        discount = total * 0.10
    elif total >= 200:
        discount = total * 0.05
    else:
        discount = 0

    final_bill = total - discount
    print(f" The final bill: Rs.{final_bill}")
else:
    print("Sorry, we don't have that")

"""
Output:

Menu: {'tea': 20, 'coffee': 50, 'momo': 150}
What do you want? coffee
How many? 4
Total: Rs. 200
The final bill: Rs.190.0

when the item is unavailable
 
Menu: {'tea': 20, 'coffee': 50, 'momo': 150}
What do you want? cookies
Sorry, we don't have that

"""