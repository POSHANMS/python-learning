# Control Flow Statements in Loops

# break

# Problem 1: Stop printing at a target item

items = ["apple", "banana", "cherry", "stop", "mango"]

for item in items:
    if item == "stop":
        break
    print("Item:", item)

# Problem 2: Find first even number

while True:
    num = int(input("Enter a number: "))
    if num % 2 ==0:
        print("First even number found: ", num)
        break

# continue

# Problem 1: Skip out-of-stock items

items = ["milk", "bread", "out of stock", "eggs"]

for item in items:
    if item == "out of stock":
        continue
    print("Buy:", item)

# Problem 2: Skip even numbers

n = 10

for i in range(1, n+1):
    if i % 2 == 0:
        continue
    print("Odd number:", i)

# pass

# Problem 1: Use pass for future implementation

tasks = ["email", "meeting", "call"]

for task in tasks:
    if task == "call":
        pass # Logic to be added later
    print("Do:", task)

# Problem 2: Pass in empty loop for now

for i in range(5):
    pass  # Placeholder for future logic