import sys
import random

num = random.randrange(1,20)

while True:

    userin = input("Pick a number between 1 through 20, I'll let you know if you got it: ")
    userin = int(userin)
    number = num
    if userin == number:
        print(f"\nCongratulations! You guessed the number! It was {number}!")
        break
    elif userin > number:
        print("\nYour number is a tad higher than mine\n")
    elif userin < number:
        print("\nYou're a bit short dude...\n")
    


