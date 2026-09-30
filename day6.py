#Dictionaries : Store data as key and value pairs.
#Creating a dictionary
student = {"name": "Ram", "age": 20}
empty = {}                     # empty dictionary
print(type(empty))             # <class 'dict'>

d1 = dict(name="Sita", age=19)
print(d1)                      # output: {'name': 'Sita', 'age': 19}

d2 = dict([("a", 1), ("b", 2)])
print(d2)                      # output: {'a': 1, 'b': 2}

print(len(student))            # 2   two pairs

#Rules for keys:(key can't duplicate but value can)
d = {"a": 1, "b": 2, "a": 99}
print(d)             # {'a': 99, 'b': 2}   last one wins

ok = {1: "one", "two": 2, (3, 4): "tuple key"}

#bad = {[1, 2]: "list key"}
# TypeError: unhashable type: 'list'

info = {"marks": [70, 80], "pass": True}   # any value

print({"a": 1, "b": 2} == {"b": 2, "a": 1})   # True

#Reading a value
student = {"name": "Ram", "age": 20}

print(student["name"])          # Ram
#print(student["phone"])         # KeyError: 'phone'

print(student.get("name"))      # Ram
print(student.get("phone"))     # None   no error
print(student.get("phone", "N/A"))   # Not availble default

#print(student[0])               # KeyError: 0;cause it only looks for key not index

#Adding and Updating
student = {"name": "Ram"}

student["age"] = 20          # new key: added
student["name"] = "Hari"     # old key: change;if key exit update otherwise add
print(student)               # {'name': 'Hari', 'age': 20}

student.update({"city": "Pokhara", "age": 21})
print(student) # Output: {'name': 'Hari', 'age': 21, 'city': 'Pokhara'}

#Removing items (pop, popitem, del and clear.)
student= {"name": "Ram", "age": 20, "city": "Pokhara", "grade": "A"}

age = student.pop("age")       # remove, and get the value
print(age)               # 20
print(student.pop("phone", "not found"))   # not found

last = student.popitem()       # remove the last pair
print(last)              # ('grade', 'A')

del student["city"]            # delete one key
print(student)                 # {'name': 'Ram'}
student.clear()                # empty it: {}
del student                  # delete the whole dictionary

"""
student.clear()
print(student)

del student
print(student) #delete with variables

#practise
d = {"a": 1, "b": 2}
d["c"] = 3
d["a"] = 10

print(d)
print(len(d))
print(d.get("z", 0))
print(d.pop("b"))
print(d)
# print(d["z"]) #keyerror
print(d.get["z"]) #output: None

"""
#keys(), values() and items()
prices = {"tea": 20, "coffee": 50, "milk": 30}

print(prices.keys()) # dict_keys(['tea', 'coffee', 'milk'])
print(prices.values()) # dict_values([20, 50, 30])
print(prices.items()) # dict_items([('tea', 20), ('coffee', 50), ('milk', 30)])

print(list(prices))            # ['tea', 'coffee', 'milk']
print(list(prices.values()))   # [20, 50, 30]

#Checking a dictionary
prices = {"tea": 20, "coffee": 50, "milk": 30}

print("tea" in prices)           # True   it's a key
print(20 in prices)              # False cause dict looks for key; 20 is a value
print(20 in prices.values())     # True

print(len(prices))               # 3
print(sum(prices.values()))      # 100
print(max(prices.values()))      # 50
print(sorted(prices))            # ['coffee', 'milk', 'tea']
print(max(prices, key=prices.get))   # coffee

#Joining two dictionaries
a = {"tea": 20, "milk": 30}
b = {"milk": 35, "juice": 60}

print(a | b)
# {'tea': 20, 'milk': 35, 'juice': 60}   milk from b

print({**a, **b})      # same result, older way

a |= b                 # change a (same as a.update(b))
print(a) # {'tea': 20, 'milk': 35, 'juice': 60}

#setdefault() and fromkeys()
c = {"name": "Ram"}

print(c.setdefault("age", 18))      # 18    missing: added
print(c.setdefault("name", "Hari")) #output: Ram  set default ignore new value if existing: already there
print(c)          # {'name': 'Ram', 'age': 18}

marks = dict.fromkeys(["math", "science", "english"], 0)
print(marks) # output: {'math': 0, 'science': 0, 'english': 0}

print(dict.fromkeys(["a", "b"]))    # {'a': None, 'b': None}

#zip() and converting: Join two lists into one dictionary.

names = ["Ram", "Sita", "Hari"]
marks = [85, 92, 78]

result = dict(zip(names, marks))
print(result)    # {'Ram': 85, 'Sita': 92, 'Hari': 78}

print(list(result.items()))
# [('Ram', 85), ('Sita', 92), ('Hari', 78)]
print(tuple(result))    # ('Ram', 'Sita', 'Hari')

#copy trap (Use .copy() or dict(a) to make a real copy.)

a = {"x": 1}
b = a            # same dictionary, two names
c = a.copy()     # a real copy
d = dict(a)      # also a real copy

a["y"] = 2
print(b)         # {'x': 1, 'y': 2}   changed too!
print(c)         # {'x': 1}           safe
print(d)         # {'x': 1}           safe

#A dictionary inside a dictionary :Great for storing many students, each with their own details.
school = {
    "ram":  {"age": 20, "city": "Pokhara"},
    "sita": {"age": 19, "city": "Kathmandu"}
}

print(school["sita"])           # {'age': 19, 'city': 'Kathmandu'}
print(school["sita"]["city"])   # Kathmandu

school["ram"]["age"] = 21       # change inside
school["hari"] = {"age": 22, "city": "Butwal"}   # add one
print(len(school))              # 3

#Lists and dictionaries together
student = {"name": "Ram", "marks": [70, 85, 90]}

print(student["marks"])        # [70, 85, 90]
print(student["marks"][0])     # 70
student["marks"].append(95)
print(sum(student["marks"]))   # 340
print(max(student["marks"]))   # 95

people = [{"name": "Ram"}, {"name": "Sita"}]
print(people[1]["name"])       # Sita

#practise
p = {"pen": 10, "book": 50}
q = {"book": 60, "bag": 500}

print("pen" in p)
print(50 in p)
print(list(p.keys()))
print(p | q)
print(sum(q.values()))

r = p
r["pen"] = 15
print(p["pen"])

#print(p.items()[0])