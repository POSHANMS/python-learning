# if-elif-else Statement

# Problem 1: Suggest a mode of transport based on distance

distance = float(input("Enter the distance to your destination (in km): "))

if distance <= 2:
    print("You can walk.")
elif distance <= 10:
    print("Use a bicycle or scooter.")
elif distance <= 50:
    print("Take a car or public transport.")
else:
    print("Consider a train or flight.")

# Problem 2: Battery status

battery = int(input("Enter the battery percentage: "))

if battery > 80:
    print("Battery Full")
elif battery > 40:
    print("Battery Half")
else:
    print("Battery Low")

# Nested if-else Statement

#Problem 3: Login with username and password
username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin":
    if password == "1234":
        print("Access granted")
    else:
        print("Incorrect password")
else:
    print("Username not found")

# Problem 4: Check exam pass and scholarship eligibility

marks = int(input("Enter your marks: "))

if marks >= 50:
    if marks >= 80:
        print("Passed with scholarship")
    else:
        print("Passed without scholarship")
else:
    print("Failed")


# Ternary Statement

# Problem 5: Check if number is even

num =int(input("Enter a number: "))
print("Even" if num % 2 == 0 else "Odd")

# Problem 6: Compare two numbers

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
print("a is greater than b" if a>b else "b is greater than a")

# Problem 7: Temperature check

temp =int(input("Enter the temperature: "))
print("Hot" if temp > 25 else "Cold")