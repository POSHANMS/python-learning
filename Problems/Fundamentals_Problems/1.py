#Sum of N Numbers
#Given an integer n find the sum of the first n natural number.
def nSum(n):
    ans = 0
    ans=n*(n+1) // 2
    return ans

print(nSum(3))

#In-Short
def NSum(n):
    return n * (n + 1) // 2

print(NSum(5))
print(NSum(10))

