# place_order() uses all three: a normal box for the customer, *items for the food, and **options for extras. The menu is a Day 06 dictionary. enumerate() (Day 10) numbers each line.

menu = {"momo": 150, "chowmein": 120, "tea": 30, "lassi": 80}

def place_order(customer, *items, **options):
    print(f"Order for {customer}")
    total = 0
    for num, item in enumerate(items, start=1):
        if item in menu:
            print(f"{num}. {item}: Rs. {menu[item]}")
            total += menu[item]
        else:
            print(f"{num}. {item}: not on the menu")

    if options.get("delivery"):
        print("Delivery: Rs. 50")
        total += 50
    for key, value in options.items():
        if key != "delivery":
            print(f"Note: {key} = {value}")

    print(f"Total: Rs. {total}")
    return total

total= place_order("Hari", "momo", "tea", "pizza", delivery=True, spicy="extra")

# save the returned total, then add 13% VAT
vat = total * 0.13
final_total = total + vat

print(f"VAT amount: Rs. {vat:.2f}")
print(f"Final total: Rs. {final_total}")

# ask the user for items with input().split(),
items = input("\nEnter items:").split()

# then send them with place_order("You", *items)
total = place_order("Me", *items)

"""
Output:
Order for Hari
1. momo: Rs. 150
2. tea: Rs. 30
3. pizza: not on the menu
Delivery: Rs. 50
Note: spicy = extra
Total: Rs. 230
VAT amount: Rs. 29.90
Final total: Rs. 259.9

Enter items: tea donut
Order for Me
1. tea: Rs. 30
2. donut: not on the menu
Total: Rs. 30

"""