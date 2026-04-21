def decToBinary(n):
    if n == 0:
        return "0"
    res = []
    while n > 0:
        res.append(str(n % 2))
        n = n // 2
    res.reverse()
    return "".join(res)

n = int(input("Enter N: "))
print(decToBinary(n))