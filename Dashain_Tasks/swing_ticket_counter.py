# Decide who can ride the big Dashain ping, and how much they pay.
"""
01
Ask for name, age, height (cm) and a coupon code
02
Empty name? Print Please enter your name.
03
Age under 5 or height under 110 cm: not safe to ride
04
Otherwise: 60+ rides free, under 12 pays Rs 50, everyone else Rs 100
05
Coupon dashain or tihar (any capitals or spaces) gives Rs 20 off, but not on free tickets
06
Print the final price
"""

print("=== Dashain Big Ping Ticket ===")

name = input("Name: ").strip()

if name == "":
    print("Please enter your name.")

else:
    age = int(input("Age: "))
    height = int(input("Height (cm): "))
    coupon = input("Coupon code: ").strip().lower()

    if age < 5 or height < 110:
        print(f"Sorry {name}, the big ping is not safe for you.")

    else:
        if age >= 60:
            price = 0
        elif age < 12:
            price = 50
        else:
            price = 100

        if price > 0 and coupon in ["dashain", "tihar"]:
            price = price - 20
            print("Coupon used! Rs 20 off.")

        print(f"{name}, your ping ticket is Rs {price}.")

"""
Output:
swing_ticket_counter.py
=== Dashain Big Ping Ticket ===
Name: riya
Age: 89
Height (cm): 78
Coupon code: tihar
Sorry riya, the big ping is not safe for you.

################

=== Dashain Big Ping Ticket ===
Name: 
Please enter your name.

################

=== Dashain Big Ping Ticket ===
Name: siyaa
Age: 27
Height (cm): 120
Coupon code: tihar
Coupon used! Rs 20 off.
siyaa, your ping ticket is Rs 80.

"""