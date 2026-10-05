# Write small functions (Day 09) that use built-ins inside: len(), set(), sorted() and max() with key=len. Then print a short report about any sentence.

def word_count(text):
    return len(text.split())

def longest_word(text):
    return max(text.split(), key=len)

def unique_words(text):
    return sorted(set(text.lower().split()))

sentence = input("Type a sentence: ")

print(f"Letters: {len(sentence)}")
print(f"Words: {word_count(sentence)}")
print(f"Longest word: {longest_word(sentence)}")

# write shortest_word(text) with min()
print(f"Shortest word: {min(sentence.split(), key=len)}")

for num, word in enumerate(unique_words(sentence), start=1):
    print(f"{num}. {word}")

# count how many times each word appears using a dictionary.
word_counts = {}
for word in sentence.lower().split():
    if word in word_counts:
        word_counts[word] = word_counts[word] + 1
    else:
        word_counts[word] = 1

print(f"Word counts= {word_counts}")

"""
Output:
Type a sentence: I love chocolate and i love coffee
Letters: 34
Words: 7
Longest word: chocolate
Shortest word: I
1. and
2. chocolate
3. coffee
4. i
5. love
Word counts= {'i': 2, 'love': 2, 'chocolate': 1, 'and': 1, 'coffee': 1}

"""
