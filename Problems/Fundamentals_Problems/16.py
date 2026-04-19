"""
Closest Number

Given two integers n and m (m != 0). The problem is to find the number closest to n and divisible by m. If there is more than one such number, then output the one having the maximum absolute value.

Examples :

Input: n = 13, m = 4
Output: 12
Explanation: 12 is the Closest Number to 13 which is divisible by 4.
Input: n = -15, m = 6
Output: -18
Explanation: Both -12 and -18 are closest to -15 and divisible by 6, but -18 has the maximum absolute value. So, output is -18.
"""


def closestNumber(n, m):
    lower = (n // m) * m
    higher = lower + m

    # compare distances
    if abs(n - lower) < abs(n - higher):
        return lower
    elif abs(n - lower) > abs(n - higher):
        return higher
    else:
        # tie → choose one with greater absolute value
        return lower if abs(lower) >= abs(higher) else higher

n, m = map(int, input("Enter the number: ").split())
print(closestNumber(n, m))