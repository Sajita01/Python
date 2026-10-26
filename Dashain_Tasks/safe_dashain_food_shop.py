# Safe Dashain Food Shop using  Exceptions, Functions, Loops, Dictionaries etc.

# 01. Create a menu dictionary with item prices.
menu = {"momo": 180,"chowmein": 150,"sel roti": 30,"tea": 40}
cart = {}

# 03. Create ask_quantity() that raises ValueError, if the quantity is zero or less.
def ask_quantity():
    quantity = int(input("Quantity: "))

    if quantity <= 0:
        raise ValueError("Quantity must be more than 0")
    return quantity


# 07. Create print_bill(cart) to print each item and the total bill.
def print_bill(cart):
    total = 0

    for item, quantity in cart.items():
        price = menu[item]
        item_total = price * quantity

        print(f"{item} x{quantity} = Rs {item_total}")

        total = total + item_total

    print(f"Total: Rs {total}")


# 02. Keep asking for items until the user types "done".
while True:
    item = input("Item (or done): ").strip().lower()

    if item == "done":
        break

    try:
        # 04. Raise KeyError if the item is not on the menu.
        price = menu[item]

        # Ask for and validate the quantity.
        quantity = ask_quantity()

    except KeyError:
        # 04. Handle items that are not on the menu.
        print(f"Sorry, no {item} on the menu.")

    except ValueError as e:
        # 05. Handle invalid numbers and invalid quantities.
        print(f"Wrong quantity: {e}")

    else:
        # 06. Add the item to the cart only if no error occurs.
        if item in cart:
            cart[item] = cart[item] + quantity
        else:
            cart[item] = quantity

        print(f"Added {quantity} x {item}")

    finally:
        # 06. Print a line of dashes after every attempt.
        print("--------------------")


# Print the final bill after the user types "done".
print_bill(cart)

"""
Output:
Item (or done): momo
Quantity: 7
Added 7 x momo
--------------------
Item (or done): chowmein
Quantity: 0
Wrong quantity: Quantity must be more than 0
--------------------
Item (or done): bread
Sorry, no bread on the menu.
--------------------
Item (or done): sel roti
Quantity: 10
Added 10 x sel roti
--------------------
Item (or done): done
momo x7 = Rs 1260
sel roti x10 = Rs 300
Total: Rs 1560

"""