"""
Fibonacci Number

Given an integer n. Write a program to find the nth Fibonacci number.

The nth Fibonacci number is given by the forumla F(n) = F(n-1) + F(n-2). The first few fibonacci numbers are:
1 1 2 3 5... and so on.

Examples:

Input: n = 4
Output: 3
Explanation: In the series 1 1 2 3 5...... the fourth fibonacci number is 3.
Input: n = 6
Output: 8
Explanation: In the series 1 1 2 3 5 8 13...... the sixth fibonacci number is 8.
"""

def Fibonacci(n):
    if n == 1 or n == 2:
        return 1

    a = 1
    b = 1

    for i in range(3, n + 1):
        c = a + b
        a = b
        b = c
    return b

n = int(input("Enter the Number :" ))
print(Fibonacci(n))