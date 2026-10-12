#  The @receipt decorator prints the shop name before the order and a thank-you after it. The order() function stays small and only works out the bill. *args, **kwargs pass the inputs through, and the bill is returned.

def receipt(func):
    def wrapper(*args, **kwargs):
        print("=" * 24)
        print("      MOMO HOUSE")
        print("=" * 24)

        result = func(*args, **kwargs)

        print("-" * 24)
        print("Thank you! Visit again")
        return result
    return wrapper

#  write a @discount decorator that returns,the total minus 10% (hint: result * 0.9)
def discount(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 0.9

    return wrapper

#  write pay(amount) that prints "Paid Rs. ..."and decorate it with @receipt too
@receipt
def pay(amount):
    print(f"Paid Rs. {amount}")
    return amount

@receipt
@discount
def order(item, qty, price):
    total = qty * price
    print(f"{item} x {qty} = Rs. {total}")
    return total

bill = order("Chicken momo", 5, 180)
print("Saved bill:", bill)

"""
Output:
========================
      MOMO HOUSE
========================
Chicken momo x 5 = Rs. 900
------------------------
Thank you! Visit again
Saved bill: 810.0

"""