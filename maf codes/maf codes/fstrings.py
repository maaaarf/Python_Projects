import random

price = (random.randrange(5,20))

desc = f"The price of this supercar is valued at ${price*5} million!"

print(desc)

if "90" in desc:
    print("That's a lot of money!")
else: print("I think you can afford this, unless it's over $90M hehe...")