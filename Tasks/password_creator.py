# The tasks of password_checker, now split into small functions.

def has_number(password):
    for ch in password:
        if ch.isdigit():
            return True
    return False

def has_capital(password):
    for ch in password:
        if ch.isupper():
            return True
    return False

def is_strong(password):
    return len(password) >= 8 and has_number(password) and has_capital(password)

while True:
    password = input("New password: ")
    if is_strong(password):
        print("Strong password. Saved!")
        break
    print("Use 8 or more letters and at least one number")


while True:
    password = input("New password: ")

    if is_strong(password):
        print("Strong password. Saved!")
        break

    print("Use 8 or more letters, at least one number, and one capital letter")

"""
Output:
New password: what?
Use 8 or more letters and at least one number
New password: what12345
Use 8 or more letters and at least one number
New password: What12345
Strong password. Saved!

"""
