# The menu is a Day 06 dictionary. Sort it by price, find cheap items with filter(), raise every price with map(), and find the costliest item with max().

menu = {"momo": 150, "chowmein": 120, "tea": 30,
        "lassi": 80, "pizza": 450}

print("--- Cheapest first ---")
for item, price in sorted(menu.items(), key=lambda x: x[1]):
    print(f"{item}: Rs. {price}")

cheap = list(filter(lambda item: menu[item] < 100, menu))
print("Under Rs. 100:", cheap)

new_prices = list(map(lambda p: p + 10, menu.values()))
print("New prices:", new_prices)

costliest = max(menu, key=lambda item: menu[item])
print("Costliest:", costliest)

# print the total of all prices with sum()
total = sum(menu.values())
print("Total prices:", total)

# ask the user for a budget with int(input())
budget = int(input("Enter your budget: "))

# Show only items they can buy
affordable = list(filter(lambda item: menu[item] <= budget, menu))

print("Items you can buy:", affordable)

"""
Output:
--- Cheapest first ---
tea: Rs. 30
lassi: Rs. 80
chowmein: Rs. 120
momo: Rs. 150
pizza: Rs. 450
Under Rs. 100: ['tea', 'lassi']
New prices: [160, 130, 40, 90, 460]
Costliest: pizza
Total prices: 830
Enter your budget: 300
Items you can buy: ['momo', 'chowmein', 'tea', 'lassi']

"""