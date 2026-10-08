# split() a sentence into words, then sort, filter and change them with lambdas. join() puts them back into one line.

sentence = input("Enter a sentence: ")    # get the sentence from the user with input()
words = sentence.split()

print(sorted(words, key=len))
print(max(words, key=len))
print(list(filter(lambda w: len(w) > 3, words)))
print(list(map(lambda w: w.capitalize(), words)))
print(" ".join(map(lambda w: w[::-1], words)))

# count the words that start with a vowel:(hint: filter + w[0] in "aeiou" + len)
vowel_words = list(filter(lambda w: w[0] in "aeiou", words))
print("Words starting with a vowel:", len(vowel_words))

"""
Output:
Enter a sentence: python is a very fun language to learn       
['a', 'is', 'to', 'fun', 'very', 'learn', 'python', 'language']
language
['python', 'very', 'language', 'learn']
['Python', 'Is', 'A', 'Very', 'Fun', 'Language', 'To', 'Learn']
nohtyp si a yrev nuf egaugnal ot nrael
Words starting with a vowel: 2

"""
