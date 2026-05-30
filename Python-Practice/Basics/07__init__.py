"""
__init__ is the constructor.
It runs automatically when object is created.
It sets up initial values.
"""

# SIMPLE EXAMPLE

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating object — __init__ runs automatically
s = Student("Poshan", 21)

print(s.name)  # Poshan
print(s.age)   # 21

# DEEP EXAMPLE

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.transactions = []  # empty list to start

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(amount)


# __init__ sets everything up automatically
account = BankAccount("Poshan", 5000)
print(account.owner)  # Poshan
print(account.balance)  # 5000

# DAILY LIFE EXAMPLE

# Every time a new user registers on Swiggy
class User:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.cart = []        # empty cart
        self.orders = []      # no orders yet
        self.is_active = True # account active

new_user = User("Poshan", "9530403030")
# All values set automatically!

# INDUSTRY EXAMPLE

class InstagramAccount:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.followers = 0      # starts at 0
        self.posts = []         # no posts yet
        self.is_verified = False # not verified