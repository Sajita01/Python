# Shopping cart
cart = [
    ["chocolate", 300, 2],
    ["Milk", 120, 1],
    ["Bread", 60, 1]
]

grand_total = 0

# Loop through the cart
for item in cart:

    name, price, quantity = item

    # Calculate the total for each item
    line_total = price * quantity

    # Print each item's total
    print(f"{name}: Rs. {line_total}")

    # Add line total to grand total
    grand_total += line_total

# Print final total
print(f"Grand total: Rs. {grand_total}")