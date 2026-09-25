
#lists for strings
fruits = ["apple", "banana", "cherry"]
print(fruits)
print(fruits[0])  # Output: apple
print(fruits[-1])  # Output: cherry
print(fruits[2])  # Output: cherry
print(fruits[1:2])

#list length
print(len(fruits))  # Output: 3 

#list for integers
numbers = [1, 2, 3, 4, 5]
print(numbers)  
print(numbers[2:4])  # Output: [3, 4]
print(numbers[1:4:2])  # Output: [2, 4]
print(numbers[::2])  # Output: [1, 3, 5]
print(numbers[::-2])  # Output: [5, 4, 3, 2, 1]

#appends
fruits.append("orange")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

#insert
fruits.insert(1, "kiwi")
print(fruits)  # Output: ['apple', 'kiwi', 'banana', 'orange']

#remove
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'kiwi', 'cherry', 'orange']

"""
#using pop to remove items
last= fruits.pop
print(last) # output: orange
print(fruits)  # Output: ['apple', 'kiwi', 'cherry']

"""

#search for an item in a list
print("kiwi" in fruits)  # Output: True

#minimum and maximum values in a list
numbers = [1, 2, 3, 4, 5]
print(numbers)  # Output: [1, 2, 3, 4, 5]
print(len(numbers))  # Output: 5
print(sum(numbers))  # Output: 15
print(min(numbers))  # Output: 1
print(max(numbers))  # Output: 5

#sorting a list
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()  # Sorts the list in ascending order
print(numbers)  # Output: [1, 2, 5, 5, 6, 9]

names = ["Charlie", "Alice", "Bob"]
names.sort() 
print(names)  # Output: ['Alice', 'Bob', 'Charlie']

#reverse sorting a list
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort(reverse=True)  # Sorts the list in descending order
print(numbers)  # Output: [9, 6, 5, 5, 2, 1]    

#names = ["Charlie", "Alice", "Bob"]
names.sort(reverse=True)  # Sorts the list in descending order
print(names)
names.sort(key=str.lower) 
print(names)  # Output: ['Alice', 'Bob', 'Charlie']

#count
print(numbers.count(5))  # Output: 2

#Nested lists
nested_lists = [[1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9]]
print(nested_lists)  # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_lists[0])  # Output: [1, 2, 3]
print(nested_lists[0][1])  # Output: 2
print(nested_lists[1][2])  # Output: 6
print(nested_lists[2][0])  # Output: 7

#for loop for lists
for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4

for i in range(1, 6):
    print(i)  # Output: 1, 2, 3, 4, 5

for row in nested_lists:
        print(row) 

#split lists
words = "My name is Sajita".split()
print(words)  # Output: ['My', 'name', 'is', 'Sajita']

#joining lists
words= ["Its", "me", "Sajita"]
line = ", ".join(words)
print(line)  #Output: Its, me, Sajita

#list append
list1 = [1, 2, 3]
print(f"list1: {list1}")

list2 = list1
list2.append(4)
print(f"list2: {list2}")  # Output: [1, 2, 3, 4]
print(f"list1 new: {list1}")  # Output: [1, 2, 3, 4]

#copying a list
list1 = [1, 2, 3]
list2 = list1.copy()
list2.append(4)
print(f"list2: {list2}")  # Output: [1, 2, 3, 4]
print(f"list1: {list1}")  # Output: [1, 2, 3]


