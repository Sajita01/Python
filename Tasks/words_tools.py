# Turn the Vowel_counter into a function. Then write is_palindrome(): a word that reads the same backwards. [::-1] 

def count_vowels(text):
    count = 0
    for letter in text.lower():
        if letter in "aeiou":
            count += 1
    return count

def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

print(count_vowels("I love Nepal"))   # 5
print(is_palindrome("Madam"))         # True
print(is_palindrome("Nepal"))         # False

# Count spaces
def count_spaces(text):
    count = 0
    for letter in text:
        if letter == " ":
            count += 1
    return count

#  Get first letter of each word
def first_letters(text):
    words = text.split() 
    result = ""

    for word in words:
        result += word[0]   # split()separates words and ignores repeated whitespace., while [0] gets the first character of each word.

    return result

print(count_spaces("I love Nepal"))    # 2
print(first_letters("I love Nepal"))   # ILN