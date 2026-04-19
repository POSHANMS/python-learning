"""
Strong Numbers

Strong Numbers are the numbers whose sum of factorial of digits is equal to the original number. Given a number N, the task is to check if it is a Strong Number or not. Print 1 if the Number is Strong, else Print 0.

Example 1:

Input:
N = 145
Output:
1
Explanation:
1! + 4! + 5! = 145 So, 145 is a Strong Number and therefore the Output 1.
Example 2:

Input:
N = 14
Output:
0
Explanation:
1! + 4! = 25 So, 14 isn't a Strong Number and therefore the Output "NO".
"""

def isStrong(N):
    original = N
    total = 0

    while N > 0:
        digit = N % 10
        fact = 1

        for i in range(1, digit+1):
            fact *= i
        total += fact
        N//=10

    if total == original:
        return 1
    else:
        return 0

N = int(input("Enter N: "))
print(isStrong(N))