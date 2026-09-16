import time
import sys

def slow_print(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def slower_print(text, delay=1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

while True: 
    slow_print("what's good shawty? *bites lip* ready to use me?(calculator): ")
    textenter = input().lower()
    if textenter == 'yes':
        break
    if textenter == 'no':
        slow_print("damn,")
        slower_print(" ")
        slow_print("aight")
        slower_print(" ")
        sys.exit()
    else: 
        print("nahh shawty, type in yes or no")

print()
slow_print("now, put some numbers in me...\n")
slow_print("I meant INPUT some numbers in me:\n")

while True: 
    slow_print("First number: ")
    num1 = int(input())
    
    if isinstance(num1, int):
        slow_print("Second number: ")
        num2 = int(input())
        
        if isinstance(num2, int):
            break
        else: slow_print("shawty I said numbers.\n")
    else: slow_print("shawty I said numnbers.\n")

slow_print("now... whatchu want me to do? (add, subtract, multiply, divide)\n")

while True:
    slow_print("Operation: ")
    opinput = input()
    if opinput not in ("add", "subtract", "multiply", "divide"):
        slow_print("shawty you gotta input one of the mentioned operations *bites lip*:\n")
    else: 
        break

if opinput == 'add':
    slow_print("here's your result *gigachad face* call me...: ")
    slower_print(" ")
    print(num1 + num2)
    slower_print(" ")

if opinput == 'subtract':
    slow_print("here's your result *gigachad face* call me...: ")
    slower_print(" ")
    print(num1 - num2)
    slower_print(" ")

if opinput == 'multiply':
    slow_print("here's your result *gigachad face* call me...: ")
    slower_print(" ")
    print(num1 * num2)
    slower_print(" ")

if opinput == 'divide':
    slow_print("here's your result *gigachad face* call me...: ")
    slower_print(" ")
    print(num1/num2)
    slower_print(" ")