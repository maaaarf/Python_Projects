import time
import sys

def slow_print(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()  # Forces the print to happen immediately
        time.sleep(delay)  # Delay between each character

def slower_print(text, delay=0.3):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()  # Forces the print to happen immediately
        time.sleep(delay)  # Delay between each character


while True:
    slow_print("Please enter a product name: ")
    pname = input()
    
    if pname.isalpha():
        print()
        break
        
    else: 
        print()
        slow_print("Error! Enter a valid product name!\n")
        
while True:
    slow_print("Item quantity: ")
    pquanti = input()
    if pquanti.isdigit():
        print()
        break
    else:
        print()
        slow_print("bruh,")
        slower_print(" ")
        slow_print("enter a valid item quantity.\n")

while True: 
    slow_print("Item price: $")
    pprice = input()
    if pprice.isdigit():
        print()
        break
    else: 
        slow_print("a price tag with ")
        slower_print("NUMBERS ")
        slow_print("dont have letters in it, no?\n")

slow_print(f"Item name: {pname}\n")
slow_print(f"Item quantity: {pquanti}\n")
slow_print(f"Item price: {pprice}\n")

price = float(pprice)
quanti = float(pquanti)

result = price*quanti

print("Your total will be: $", result)
        
       