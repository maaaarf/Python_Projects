num1 = 0
num2 = 0
operator = ""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

print("Simple Calculator")
print("Available operations: +, -, *, /")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operation (+, -, *, /): ")

if operator == "+":
    result = add(num1, num2)
elif operator == "-":
    result = subtract(num1, num2)
elif operator == "*":
    result = multiply(num1, num2)
elif operator == "/":
    result = divide(num1, num2)
else:
    result = "Error: Invalid operation."

print("Result:", result)

resultStorage = result

print("Would you like to continue the operation? (yes/no)")
continue_operation = input().lower()
if continue_operation == "yes":
    num3 = float(input("Enter the next number: "))
    operator2 = input("Enter the next operation (+, -, *, /): ")

    if operator2 == "+":
        resultStorage = add(resultStorage, num3)
    elif operator2 == "-":
        resultStorage = subtract(resultStorage, num3)
    elif operator2 == "*":
        resultStorage = multiply(resultStorage, num3)
    elif operator2 == "/":
        resultStorage = divide(resultStorage, num3)
    else:
        print("Error: Invalid operation.")
    
    print("New Result:", resultStorage)