import time

def birthday_greeter(name, age):
    print(f"Happy birthday to you {name.capitalize()}")
    time.sleep(1.5)
    print(f"You are {age} years old")
    time.sleep(1.5)
    print(f"Welcome to a new age, have an amazing year ahead")
    print()

b_name = input("Enter your name: ")
b_age = int(input("Enter your age: "))


birthday_greeter(name=b_name, age=b_age)
