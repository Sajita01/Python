#  int(input()) crashes when the user types words. get_number() keeps asking until it gets real digits, then returns an int. Use it in every program from now on!
def get_number(question):
    while True:
        answer = input(question).strip()
        if answer.isdigit():
            if 1 <= int(answer) <= 120:   # only accept ages from 1 to 120
                return int(answer)

            print("Age must be between 1 and 120")
        else:
            print("Please type a number only")


age = get_number("Your age: ")
print(f"Next year you will be {age + 1}")

"""
Output:
Your age: 122
Age must be between 1 and 120
Your age: two
Please type a number only
Your age: 45
Next year you will be 46

"""