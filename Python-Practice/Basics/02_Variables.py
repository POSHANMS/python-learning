#Basic Assignment
x=5
y=3.14
z="Hi"
print(x,y,z)

#Dynamic Typing
x=10
x="It's a string"
print(x)

'''
Multiple Assignments
Assigning Same Value
'''
a=b=c=100
print(a,b,c)

#Assigning Different Values
x, y, z = 1, 3.18, "Python"
print(x,y,z)

#Swapping two variables
a, b = 5, 10
a, b = b, a
print(a, b)

#Counting Characters in a String
word = "Python"
length = len(word)
print("length of word:", length)

#Insert a Variable into a String
#Using f-strings
a="Python"
res= f"This is {a} programming language"
print(res)

#Using format()
a="Hello"
b="World"
res = "{} {}".format(a, b)
print(res)

#Using + Operator
res=a + " " + b
print(res)

#Using % formatting
a="Python"
res="This is %s programming language" %a
print(res)
