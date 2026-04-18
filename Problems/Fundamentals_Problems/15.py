"""
Print square
Given an integer n.
Write a program to print the square of size n using "*" character.
Example
Input: n = 4
Output:
* * * *
*     *
*     *
* * * *
Explanation: It's a square Each side contains N4
"""

n = int(input("Enter n : "))

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()