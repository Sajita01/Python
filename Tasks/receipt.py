item = input("Enter the item name:")
price= float(input("Enter the price of the item:"))
quantity = int(input("Enter the quantity of the item:"))    

subtotal = price * quantity
vat = subtotal * 0.13
total = subtotal + vat

print("\n--- SHOPPING RECEIPT ---")
print(f"Item: {item}")
print(f"Price: Rs.{price:.2f}")
print(f"Quantity: {quantity}")
print(f"Subtotal: Rs.{subtotal:.2f}")
print(f"VAT: Rs.{vat:.2f}")
print(f"Total: Rs.{total:.2f}")
