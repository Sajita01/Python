# remove_duplicates() uses the set trick. total_price() loops using dictionary. Both return the answer, so you can use it later.

def remove_duplicates(items):
    return sorted(set(items))

def total_price(cart):
    total = 0
    for price in cart.values():
        total += price
    return total

names = ["Ram", "Sita", "Ram", "Hari", "Sita"]
print(remove_duplicates(names))   # ['Hari', 'Ram', 'Sita']

cart = {"rice": 1200, "oil": 350, "sugar": 140}
print(total_price(cart))          # 1690

# Find common items in both lists
def common(a, b):
    return set(a) & set(b)

# Find the costliest item's name
def costliest(cart):
    highest_price = 0

    for name, price in cart.items():
        if price > highest_price:
            highest_price = price
            item_name = name

    return item_name

print(f"Common names are: {common(['Ram', 'Sita', 'Hari'], ['Sita', 'Hari', 'Gita'])}")
print(f"Costliest item is: {costliest(cart)}")

"""
Output:
['Hari', 'Ram', 'Sita']
1690
Common names are: {'Hari', 'Sita'}
Costliest item is: rice

"""
