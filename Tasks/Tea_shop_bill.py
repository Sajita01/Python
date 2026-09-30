
# Make a menu dictionary of items and prices. Ask what the customer wants and how many. Use get() to find the price, then print the total bill. Then add a new item to the menu and print some menu facts.

prices = {"tea": 20, "coffee": 50, "samosa": 25}
print("Menu:", prices)

# Ask the customer
item = input("What do you want? ")
qty = int(input("How many? "))

# Find the price
price = prices.get(item, 0)

# Calculate the bill
print("Price of one:", price)
print("Total bill  :", price * qty)

# Add a new item
prices["momo"] = 150
print("\nUpdated menu:", prices)

# Print cheapest and costliest prices
print(f"Cheapest price: {min(prices.values())}")
print(f"Costliest price: {max(prices.values())}")

# Print item names in alphabetical order
print(f"Items: {sorted(prices)}")

