import itertools
from faker import Faker
import time
import random

fake = Faker()

digits = "0123456789"

def BruteForce(target_password):
    attempts = 0
    found = False
    tried_guesses = set()

    print("Starting bruteforce in...")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    while not found and attempts < 10000000:
        fname = fake.first_name()
        sname = fake.first_name()
        number = random.choice(digits)

        guess = ''.join(fname + sname + number)

        if guess in tried_guesses:
            continue

        attempts += 1
        tried_guesses.add(guess)

        print(f"Attempt #{attempts} {guess}")
        

        if guess == target_password:
            found = True
            print(f"Password: {guess}")
    if not found:
        print("Password not found within 10,000,000 attempts")

target_password = "IanGabriel123"
print(f"The target password is CharlesGarcia1")

BruteForce(target_password)
