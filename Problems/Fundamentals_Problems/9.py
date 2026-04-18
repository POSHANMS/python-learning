# while loop

# Problem 1: Countdown timer

seconds = int(input("Enter the countdown time in seconds: "))

while seconds > 0:
    print("Time left:", seconds)
    seconds -= 1

# Problem 2: Sum until user enters 0 without using break

total = 0
num = int(input("Enter number(0 to stop): "))
while num != 0:
    total += num
    num = int(input("Enter number(0 to stop): "))
print("Total:", total)

