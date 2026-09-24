#f-strings
num1=4
num2=5
sum=num1+num2
print(sum)
print(f"{num1} + {num2} = {sum}")


#2
price=100
quantity=5
discount=10
tax=0.13

total=price*quantity-discount
tax_amount=total*tax
final_total=total+tax_amount
print(f"Total price : {total}")

"""
#3 input function
num1=input("Enter first number: ")
new_num1 = num1 + "5"
print(num1)
print(new_num1)

#4 defining datatypes
num1=int(input("Enter first number: "))  
new_num1 = num1 + 5
print(num1)
print(new_num1)
"""

#5 shorthand operators

num1 = 10
num1 += 5  # Equivalent to num1 = num1 + 5
print(num1) 

#6 match-case--python's switch

choice ="2"
match choice:
    case "1":
        print("Add")
    case "2":
        print("Subtract")
    case "3":
        print("multiply")
    case _:
        print("Invalid option")

#7 strings

name = "alice"

name=name.upper()
print(name)

name=name.lower()
print(name)

name=name.capitalize()
print(name)

name=name.title()
print(name)

length=len(name)
print(length)

#remove unnecessary gaps
name="   alice   "
name=name.strip()
print(name)

#check datatype
a=12
b=5.7
c=True
d="hello"
print(type(a))
print(type(b))
print(type(c))
print(type(d))

#Boolean operators

#sentence starts with: (python is case sensitive)

sentence = "Hello World!"
print(sentence.startswith("hi"))#case sensitive
print(sentence.startswith("Hi"))
print(sentence.endswith(" World!"))
print("z " in sentence)

#replace
sentence = sentence.replace("World", "Python")
print(sentence)

#Indexing:index always starts from 0
word = "Python"
print(word[0])  # Output: P
print(word[1])  # Output: y
print(word[-1])  # Output: t

#Slicing (start from the mentioned index and go upto -1 of the mentioned index)
word = "Python"
print(word[0:3])  # Output from index 0 to 2: Pyt

print(word[2:5])  # Output: tho
print(word[3:])  # Output: hon
print(word[:3])   # Output: Pyt
print(word[1:4])   # Output: yth
#step slicing
word = "Python"
print(word[0:4:2]) # 

#Typecasting

num1 = 10
str=str(num1)
print(str)

string = "123.11"
number = float(string)
print(type(number))  # Output: <class 'float'


#for boolean
num=3
bool_val=bool(num)
print(bool_val)

num=0
bool_val=bool(num)
print(bool_val)

#Comparision operators

num1=5
num2=10
print(num1 == num2)  # Output: False
print(num1 != num2)  # Output: True
print(num1 < num2)   # Output: True
print(num1 <= num2)  # Output: True
print(num1 > num2)   # Output: False
print(num1 >= num2)  # Output: False

#Making Calculator using match-case statements 
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Choose your operation (+, -, *, /, %): ")

match operation:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        print(num1 / num2)
    case "%":
        print(num1 % num2)
    case _:
        print(" Please enter avalid operation")


"""
#Making Calculator using if-else statements

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Choose your operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    result = "Invalid operation"

print(f"Result: {result}")
"""
