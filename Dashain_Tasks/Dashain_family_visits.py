# A trip that never changes, houses we visited, and the tika money we got.

# 01. Tuple: Store trip information and unpack it
trip = ("Pokhara", 3, "bus")

place, days, transport = trip

print(f"Going to {place} for {days} days by {transport}")


# 02. Sets: Houses visited by Sita and Ram
sita = {"aamabuba", "kaka", "fupu","thulobaba","mamaghar"}
ram = {"aamabuba", "fupu","thulobaba","mamaghar"}

# 03. Print who both visited (&), everyone (|) and only Sita (-)
print("House visited by Both:", sorted(sita & ram))
print("House visited by Everyone:", sorted(sita | ram))
print("House visited by only Sita:", sorted(sita - ram))


# 04. Count unique guests
guests = ["Ram", "Sita", "Ram", "Hari", "Sita"]
unique_guests = set(guests)

print("Unique guests:", len(unique_guests))

# 05. Tika money dictionary: add a person, change a value, then update()
money = {"aamabuba": 500,"kaka": 200,"mamaghar": 1000}

# Add a person
money["fupu"] = 300

# Change a value
money["mama"] = 600

# Update dictionary with another person
money.update({"maiju": 400})

# 06. Get a missing person's money with a default
print("Maiju gave:", money.get("maiju", 0))

# Remove kaka and store the removed value
removed = money.pop("kaka")
print("Removed kaka:", removed)


# 07. Print dictionary, keys and total
print(money)
print("People:", list(money.keys()))
print("Total:", sum(money.values()))


# 08. Dictionary inside a dictionary
family = {"Sita": {"city": "Bhaktapur","age": 20},"Ram": {"city": "Pokhara","age": 22}}
print(family["Sita"]["city"])

"""
Output:
Going to Pokhara for 3 days by bus
House visited by Both: ['aamabuba', 'fupu', 'mamaghar', 'thulobaba']
House visited by Everyone: ['aamabuba', 'fupu', 'kaka', 'mamaghar', 'thulobaba']
House visited by only Sita: ['kaka']
Unique guests: 3
Maiju gave: 400
Removed kaka: 200
{'aamabuba': 500, 'mamaghar': 1000, 'fupu': 300, 'mama': 600, 'maiju': 400}
People: ['aamabuba', 'mamaghar', 'fupu', 'mama', 'maiju']
Total: 2800
Bhaktapur

"""