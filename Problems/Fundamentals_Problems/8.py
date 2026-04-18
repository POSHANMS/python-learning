# loops

# for loops
# Problem 1: Print each item in a shopping list

items = input("Enter shopping items separated by commas: ").split(',')

for item in items:
    print("Buy:", item.strip())

# Problem 2: Print squares of numbers from 1 to n

n = int(input("Enter a number: "))

for i in range(1, n+1):
    m = m**1
    print(f"Square of {i} is {i**2}")

# Nested for Loops

# Problem 1: Print a multiplication table

n = 3

for i in range(1, n+1):
    for j in range(1, 11):
        print(i * j, end=' ')
    print()

# Problem 2: Print Identity Matrix Pattern

n = 4

for i in range(n):
    for j in range(n):
        if i == j:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()