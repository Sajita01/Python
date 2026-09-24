name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))
current_year = 2026

# Clean and format the name
name = name.strip()
name = name.title()

age = current_year - birth_year
is_long_name = len(name) > 10

print("\n--- PROFILE CARD ---")
print(f"Name: {name.upper()}")
print(f"Age: {age}")
print(f"is_long_name: {is_long_name}")


