# Classroom seating chart

chart = [
    ["empty", "empty", "empty", "empty"],
    ["empty", "empty", "empty", "empty"],
    ["empty", "empty", "empty", "empty"]
]

# Get student's name and seat position
name = input("Enter student name: ")
row = int(input("Enter row number (0-2): "))
column = int(input("Enter column number (0-3): "))

# Seat the student
chart[row][column] = name


# Print the seating chart
print("\nSeating Chart:")

for row in chart:
    print(row)


# Count empty seats
empty_seats = 0

for row in chart:
    empty_seats += row.count("empty")

print("Empty seats:", empty_seats)