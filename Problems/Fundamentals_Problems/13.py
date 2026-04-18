"""
Print Even Positioned Characters

You are given a String S, you need to print its characters at even indices(index starts at 0). |
Examples:
Input: s = "Geeks"
Output: Ges
Explanation: The even indices (0, 2 & 4) characters are printed.
"""

def utility(s):
    result = ""
    for i in range(0, len(s), 2):
        result += s[i]
    return result

print(utility("Geeks"))