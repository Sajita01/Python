# Keep asking for a password until it is strong: 8 or more letters and at least one number. Tip: "5".isdigit() is True, "a".isdigit() is False.
while True:
    password = input("New password: ")

    has_number = False  #assuming start value is False, until we find a number in the password
    has_capital = False  # haven't found a capital letter

    for ch in password:
        if ch.isdigit():
            has_number = True

        if ch.isupper():
            has_capital = True

    if len(password) < 8:
        print("Too short. Use 8 or more letters")
    elif not has_number:
        print("Add at least one number")
    elif not has_capital:
        print("Add at least one capital letter")
    else:
        print("Strong password. Saved!")
        break