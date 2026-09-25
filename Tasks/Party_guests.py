# Two friends type their guest lists (names separated by commas, no spaces). Make each list a set, then print: guests on both lists, all guests, and the total number of guests. Add one guest with add(), and remove one with discard().

# Party guest list
ram = set(input("Ram's guests: ").split(","))
sita = set(input("Sita's guests: ").split(","))

print("Guests On both lists:", ram & sita)
print("All guests   :", ram | sita)

# Total number of guests
print("Total guests :", len(ram | sita))

# Guests only Ram invited
print("Only Ram invited:", ram - sita)

# Check if Hari is invited
print("Is Hari invited?", "Hari" in ram)

# Add a guest
ram.add("Hari")

# Remove a guest safely
ram.discard("Gita")

# Print Ram's list again
print("Ram's updated guests:", ram)