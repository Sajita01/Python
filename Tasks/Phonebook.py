# Start with two contacts. Ask the user for a new name and number and add them. Print all contacts and the total. Then ask for a name to search, and use get() so a missing name prints "Not found" instead of crashing.

# Creating a dictionary with two contacts
contacts = {"Ram": "9801111111", "Sita": "9802222222"}

# Adding a new contact
name = input("New contact name: ")
phone = input("Phone number: ")

contacts[name] = phone

# Printing all contacts and total
print(f"All contacts: {contacts}")
print(f"Total: {len(contacts)}")

# Searching for a contact using get()
find = input("Search a name: ")
print(f"Number: {contacts.get(find, 'Not found')}")

# Remove one contact using pop()
remove_name = input("Name to remove: ")

removed = contacts.pop(remove_name, "Not found")
print(f"Removed contact: {removed}")

# Print only the names
print(f"Contact names: {list(contacts.keys())}")

# Print updated contacts and total
print(f"Updated contacts: {contacts}")
print(f"Total contacts: {len(contacts)}")

