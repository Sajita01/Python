# Start with kites = ["red", "blue", "green"] and keep the stock up to date.

# 01. Start with the stock list
kites = ["red", "blue", "green"]

# Add yellow at the end and black at the start
kites.append("yellow")
kites.insert(0, "black")

# 02. Remove "green". Then pop() the last kite and print it as sold
kites.remove("green")
sold = kites.pop()
print("Sold:", sold)

# 03. Sort the list and print the first two kites with slicing
kites.sort()
print("Stock:", kites)
print("First two:", kites[:2])

# 04. Count kites and check whether blue is in stock
print("How many kites are left? ", len(kites))
print("Have blue in stock?", "blue" in kites)

# 05. Split a string into a list and add the new kites
new_kites = "pink,orange,white".split(",")

kites.extend(new_kites)

# 06. Join all kites with " | "
print(" | ".join(kites))

# 07. Make a real copy and add gold, show the original did not change
copy_kites = kites.copy()
copy_kites.append("gold")

print(len(kites), len(copy_kites))

# 08. With prices = [["small", 50], ["big", 150]], print the big kite's price
prices = [["small", 50], ["big", 150]]

print("Big kite price:", prices[1][1])

"""
Output:
Sold: yellow
Stock: ['black', 'blue', 'red']
First two: ['black', 'blue']
How many kites are left?  3
Have blue in stock? True
black | blue | red | pink | orange | white
6 7
Big kite price: 150

"""