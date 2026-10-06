# make_bill() takes any number of prices with *prices, and a discount that must be sent by name. Day 07 if checks for an empty cart.

def make_bill(*prices, discount=0):
    if not prices:
        print("Cart is empty!")
        return 0
    total = sum(prices)
    saved = total * discount / 100
    print(f"Items:     {len(prices)}")
    print(f"Costliest: Rs. {max(prices)}")
    print(f"Total:     Rs. {total}")
    print(f"Discount:  Rs. {round(saved, 2)}")
    return round(total - saved, 2)

pay = make_bill(1200, 350, 140, 260, discount=10)
print(f"To pay:    Rs. {pay}")

# call make_bill() with no prices.
make_bill()

# ask the user for prices with input().split(),
price_text = input("Enter prices: ").split()

# turn each one into an int,
prices = []
for price in price_text: 
    prices.append(int(price))

# send them with make_bill(*prices)
pay = make_bill(*prices)  # pay = make_bill(*prices, discount=20) : for 20% discount
print(f"To pay: Rs. {pay}")

"""
Output:
Costliest: Rs. 1200
Total:     Rs. 1950
Discount:  Rs. 195.0
To pay:    Rs. 1755.0
Cart is empty!
Enter prices: 78 56 45 35 75
Items:     5
Costliest: Rs. 78
Total:     Rs. 289
Discount:  Rs. 0.0
To pay: Rs. 289.0

"""