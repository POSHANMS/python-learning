"""
self = "this object"
It keeps each object's data separate from others.
Always first parameter in every method.
"""


class Student:
    def __init__(self, name):
        self.name = name  # THIS object's name

    def introduce(self):
        print("My name is", self.name)

# SIMPLE EXAMPLE

s1 = Student("Poshan")
s2 = Student("Rahul")

s1.introduce()  # My name is Poshan
s2.introduce()  # My name is Rahul


# DEEP EXAMPLE

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount  # THIS account's balance
        print(f"{self.owner} deposited {amount}")

    def show(self):
        print(f"{self.owner} has ₹{self.balance}")


a1 = BankAccount("Poshan", 5000)
a2 = BankAccount("Rahul", 3000)

a1.deposit(1000)  # Poshan deposited 1000
a2.deposit(500)  # Rahul deposited 500

a1.show()  # Poshan has ₹6000
a2.show()  # Rahul has ₹3000


# 6. INDUSTRY EXAMPLE
# Zomato — millions of users:

class ZomatoUser:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item):
        self.cart.append(item)  # THIS user's cart only!

u1 = ZomatoUser("Poshan")
u2 = ZomatoUser("Rahul")

u1.add_to_cart("Burger")
u2.add_to_cart("Pizza")

print(u1.cart)  # ['Burger']
print(u2.cart)  # ['Pizza']
# Never mixed! self keeps them separate