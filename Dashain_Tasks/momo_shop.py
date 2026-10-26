# Flexible Momo Shop

menu = [("buff momo", 180),("veg momo", 150),("chicken momo", 220),("tea", 40)]

# 01. Create total_bill(*prices, discount=0) that adds any number of prices.
def total_bill(*prices, discount=0):
    total = sum(prices)
    total = total - discount
    return total


# 02. Call it with 3 prices, with discount=40,and with *cart.
print(total_bill(180, 150, 60))
print(total_bill(180, 150, 60, discount=40))

cart = [180, 150, 70]
print(total_bill(*cart))


# 03. Create make_order(customer, *items, **extras) that prints the customer, items and extras.
def make_order(customer, *items, **extras):
    print(f"Order for {customer}:")

    for item in items:
        print(f"  - {item}")

    for key, value in extras.items():
        print(f"  {key}: {value}")

make_order("Sita", "buff momo", "jhol momo",spicy="yes", table=4)

# 04. Sort the menu by price using sorted(key=lambda ...)
sorted_menu = sorted(menu, key=lambda item: item[1])
print("Cheap to costly:", sorted_menu)


# 05. Find the costliest item using max() and lambda.
costliest = max(menu, key=lambda item: item[1])
print("Costliest:", costliest)


# 06. Add a 10% service charge to every price using map().
prices_with_service = list(
    map(lambda item: round(item[1] * 1.10), menu)
)
print("With 10% service charge to every price:", prices_with_service)


# 07. Keep only items under Rs 200 using filter().
cheap_items = list(
    filter(lambda item: item[1] < 200, menu)
)
print("Under 200:", cheap_items)

"""
Output:
390
350
400
Order for Sita:
  - buff momo
  - jhol momo
  spicy: yes
  table: 4
Cheap to costly: [('tea', 40), ('veg momo', 150), ('buff momo', 180), ('chicken momo', 220)]
Costliest: ('chicken momo', 220)
With 10% service charge to every price: [198, 165, 242, 44]
Under 200: [('buff momo', 180), ('veg momo', 150), ('tea', 40)]

"""