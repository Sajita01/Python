#  Two lists: items and prices. show_bill() walks them together with zip(). bill_total() uses sum() and round(), with a default discount of 0

def show_bill(items, prices):
    print("------ BILL ------")
    # number every line with enumerate(items, start=1)
    for i, (item, price) in enumerate(zip(items, prices), start=1):
        print(f"{i}. {item}: Rs. {price}")
    print("------------------")

def bill_total(prices, discount=0):
    total = sum(prices)
    return round(total - total * discount / 100, 2)

items = ["rice", "oil", "sugar", "tea"]
prices = [1200, 350, 140, 260]

show_bill(items, prices)
print(f"Items: {len(items)}")
print(f"Costliest: Rs. {max(prices)}")
print(f"Total: Rs. {bill_total(prices)}")
print(f"After 10% off: Rs. {bill_total(prices, 10)}")

# print the cheapest item's name
cheapest_item = items[prices.index(min(prices))]  # Finding the cheapest price and use its index to get the cheapest item's name
print(f"Cheapest item: {cheapest_item}")

"""
Output:
------ BILL ------
1. rice: Rs. 1200
2. oil: Rs. 350
3. sugar: Rs. 140
4. tea: Rs. 260
------------------
Items: 4
Costliest: Rs. 1200
Total: Rs. 1950.0
After 10% off: Rs. 1755.0
Cheapest item: sugar

"""