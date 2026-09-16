import sys
import time

def slow_print(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

agelist = [0,100]

username = ("Please input your name: ")
userage = ("Please input your age: ")
userstatus = ("Are you single, married, or widowed?: ")
usernatl = ("Are you a Filipino (Yes/No)?: ")

while True:
    print(" ")
    slow_print(username)
    uname = input().lower()
    if uname.replace(" ", "").replace(".", "").isalpha():
        break
    else: 
        print(" ")
        slow_print("Please enter your valid name.\n")

while True: 
    print(" ")
    slow_print(userage)
    uage = input().lower()
    if uage.isdigit():
        break
    else: 
        slow_print("Please enter a valid age.\n")

while True: 
    print(" ")
    slow_print(userstatus)
    ustat = input().lower()
    if ustat == str("single"):
        break
    if ustat == str("married"):
        break
    if ustat == str("widowed"):
        break
    else: 
        slow_print("Please choose a status.\n")

while True: 
    print(" ")
    slow_print(usernatl)
    unatl = input().lower()
    if unatl == ("yes"):
        break
    if unatl == ("no"):
        print(" ")
        slow_print("What is your nationality?: ")
        uothernatl = input().lower()
        break
print(" ")
slow_print(f"Name: {uname.title()}\n")
slow_print(f"Age: {uage.capitalize()}\n")
slow_print(f"Status: {ustat.capitalize()}\n")

if unatl == "yes":
    slow_print(f"Nationality: Filipino\n")
else:
    slow_print(f"Nationality: {uothernatl.capitalize()}\n")
    print(" ")

