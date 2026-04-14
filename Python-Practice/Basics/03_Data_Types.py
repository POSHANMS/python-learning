x = 50 # int
x = 60.5 # float
x = "Hello World" # string
x = ["Hello", "World"] # list
x = ("Hello", "World") # tuple

# Numeric Data types
# Integers
a = 5
print(type(a))

# Floating-Point
b = 5.0
print(type(b))

# Complex
c = 2 + 4j
print(type(c))

# Sequence Data Types
# String
s = "Welcome to python"
print(s)

# check data type
print(type(s))

# access string with index
print(s[0])
print(s[1])
print(s[-1])

# List
#Empty
l = []

# list with int values
l = [1, 2, 3]
print(a)

# list with mixed values int and String
b = [1,2,3, "Hello", "World"]
print(b)

# Access List Items
print("Accessing element from the list")
print(l[0])
print(l[1])

print("Accessing element using negative indexing")
print(l[-2])
print(l[-1])

# Tuple
# initiate empty tuple
t = ()

t = ("Hello", "World")
print(t)

# Access Tuple Items
print(t[0])
print(t[1])
print(t[-1])
print(t[-2])

# Boolean Data Type
print(type(True))
print(type(False))

# Set Data Type
# initializing empty set
s1 = set()

s1 =  set([1,2,3])
print(s1)

s1 = set("Welcome to python")
print(s1)

s2 = set(["Hello", "World", "Hello"])
print(s2)

# Access Set Items
set1 = set(["Geeks", "For", "Geeks"])
print(set1)

# loop through set
for i in set1:
    print(i, end=" ")

# check if item exist in set
print("Geeks" in set1)

# Dictionary Data Type
# initialize empty dictionary
d = {}

d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d)

# creating dictionary using dict() constructor
d1 = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print(d1)

# Accessing Key-value in Dictionary
d = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}

# Accessing an element using key
print(d['name'])

# Accessing a element using get
print(d.get(3))

# Truthy vs Falsy Values in Python
f_name = input("Enter your first name: ")

if f_name:
    print(f"Hi, {f_name}!")
else:
    print("Bro, I said enter your name.")
    f_name = input("Enter your first name: ")