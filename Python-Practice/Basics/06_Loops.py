# Loops

# For Loops
n = 4
for i in range(0, n):
    print(i)

# Iterating Over List, Tuple, String and Dictionary Using for Loops in Python

li = ["geeks", "for", "geeks"]
for x in li:
    print(x)

tup = ("geeks", "for", "geeks")
for x in tup:
    print(x)

s = "abc"
for x in s:
    print(x)

d = dict({"x":123, "y":456})
for x in d:
    print("%s %d" % (x,d[x]))

set1 = {10, 20, 30}
for x in set1:
    print(x)

# Iterating by Index of Sequences

for index in range(len(li)):
    print(li[index])

# While Loop

cnt = 0
while (cnt < 3):
    cnt = cnt + 1
    print("Hello Geek")

# Infinite While Loop
""" while (True):
    print("Hello Geek") """

# Nested Loops

for i in range(1, 5):
    for j in range(i):
        print(i, end=" ")
    print()

# Loop Control Statements

# Continue Statement
for letter in "geeksforgeeks":
    if letter == "e" or letter == "s":
        continue
    print("Current Letter :", letter)
print("\n")

# Break Statement
for letter in "geeksforgeeks":
    if letter == "e" or letter == "s":
        break
print("Current Letter :", letter)

# Pass Statement
for letter in 'geeksforgeeks':
    pass
print('Last Letter :', letter)

# Using Else with Loops

for i in range(1, 4):
    print(i)
else:  # Executed because no break in for
    print("No Break")

count = 0
while (count < 1):
    count = count+1
    print(count)
    break
else:
    print("No Break")