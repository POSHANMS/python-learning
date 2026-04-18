# Jumping through While

"""
Given a positive integer x, the task is to print the numbers from 1 to x in the order as
1² 2², 3², 4², 5², ... (in increasing order).
Example:
Input: x = 10
Output: 1 4 9
Explanation:From 1 to 10, numbers in powers of 2 are, 1², 2², 3² as 1, 4 and 9.
"""

def printIncreasingPower(x):
    i = 1
    while i * i <= x:
        print(i * i, end=" ")
        i += 1

x = int(input("Enter a number: "))

printIncreasingPower(x)