"""
Factorial
Given a positive integer n.
Find the factorial of n.
Example
Input: n = 5
Output: 120
Explanation: 1 x 2 x 3 x 4 x 5 = 120 """

def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

n = int(input("Enter n : "))
print(factorial(n))