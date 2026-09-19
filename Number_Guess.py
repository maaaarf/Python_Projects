import random
import time

def guess_the_number():
    secret_number = random.randint(1,100)

    attempt_counter = 1

    guess_status = False

    while not guess_status:
        user_guess = int(input("Guess the number: "))
        

        if user_guess > secret_number:
            print("That number is kinda high.")
            attempt_counter += 1
        elif user_guess < secret_number:
            print("You might wanna guess higher than that.")
            attempt_counter += 1
        elif user_guess == secret_number:
            print("Congrats! you got it!"), time.sleep(2)
            guess_status = True

    print(f"The number was {secret_number}"), time.sleep(1.5)
    print(f"You guessed the number in {attempt_counter} attempt/s.")

print("=== Simple Number Guessing Game ==="), time.sleep(2)
print("You have an unlimited, but counted, number of attempts."), time.sleep(2)
print("The secret number is between 1 and 100."), time.sleep(2)
print("Good luck!"), time.sleep(2)

guess_the_number()



    



