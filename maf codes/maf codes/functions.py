def add(a, b):
    return a + b

def greet(name):
    print(f"Hello, {name}!")

greet(input("What is your name?: "))

print("Please enter two numbers in succession: ")
a = int(input())
b = int(input())

print(f"I have added those two numbers, and they equal to {add(a, b)}.")

name = input("Please enter your name: ")
print(f"Hello, {name}!")

print("please enter two numbers: ")
x = int(input())
y = int(input())

print(f"Hello, {name}!, the sum of your numbers is {x + y}.")