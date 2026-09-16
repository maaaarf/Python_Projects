import math

while True:
    pyth1 = input("Please input number 'a': ")
    print(" ")
    if pyth1.isdigit():
        break
    else: 
        print("Please input a number!")
        print(" ")
while True:
    pyth2 = input("Please input number 'b': ")
    print(" ")
    if pyth2.isdigit():
        break
    else: 
        print("Please input a number!")
        print(" ")

pytha1 = int(pyth1)
pytha2 = int(pyth2)

hypt1 = ((pytha1)*(pytha1))
hypt2 = ((pytha2)*(pytha2))
hyptt = ((hypt1)+(hypt2))

hypo = float(hyptt)

hypc = math.sqrt(hypo)

pyth = (f"According to the Pythagorean Theorem, the values you have inputted resulted in a hypotenuse of: {hypc}")

print(pyth)