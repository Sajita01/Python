#  Ask the user for a sentence. Loop over every letter and count how many vowels (a, e, i, o, u) it has. Use .lower() so capital letters count too.

text = input("Type a sentence: ").lower()
vowels = 0
spaces = 0
back = ""

for letter in text:
    if letter in "aeiou":
        vowels += 1

    if letter == " ":    # checks whether the current character is a space.
        spaces += 1      # increases space counter whenever a space is found.

    back = letter + back   # adds the letter at the beginning

print(f"Vowels: {vowels}")
print(f"Spaces: {spaces}")
print(f"Backwards: {back}")