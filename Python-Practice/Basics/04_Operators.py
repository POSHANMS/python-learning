# Operators in general are used to perform operations on values and variables.

# Arithmetic Operators

a = 15
b = 4

print("Addition: ", a+b)
print("Subtraction: ", a-b)
print("Multiplication: ", a*b)
print("Division: ", a/b)
print("Floor Division: ", a//b)
print("Modulus: ", a%b)
print("Exponentiation: ", a**b)

# Comparison Operators

print("Greater than: ", a > b)
print("Less than: ", a < b)
print("Equal to: ", a == b)
print("Not Equal to: ", a != b)
print("Greater than or equal to: ", a >= b)
print("Less than or equal to: ", a <= b)

# Logical Operators

t = True
f = False
print(t and f)
print(t or f)
print(not t)

# Bitwise Operators

print("Bitwise AND: ", a & b)
print("Bitwise OR: ", a | b)
print("Bitwise NOT(Complement): ", ~a)
print("Bitwise XOR: ", a ^ b)
print("Bitwise Right Shift: ", a >> 2)
print("Bitwise Left Shift: ", a << 2)

# Assignment Operators

x = 10
b = a
print(b)
b += a
print(b)
b -= a
print(b)
b *= a
print(b)
b /= a
print(b)


# Identity Operators
c = a
print(a is not b)
print(a is c)

# Membership Operators

numbers = [10, 15, 20, 30, 40, 50]

if (a not in numbers):
    print("x is NOT present in given list")
else:
    print("x is present in given list")

if(b in numbers):
    print("y is prsent in given list")
else:
    print("y is not present in given list")

# Ternary Operator

minimum = a if a < b else b
maximum = a if a >b else b
print(minimum, maximum)

# := Walrus Operator

num = [1, 2, 3, 4, 5]

while (n := len(num)) > 0:
    print(num.pop())
