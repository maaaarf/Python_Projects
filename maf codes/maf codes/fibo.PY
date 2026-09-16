import sys

inp = input("Are you ready to see some magic (Y/N): ").upper()

while True:
    if inp == "Y":
        break
    if inp == "N":
        sys.exit()

rng = range(0,70,1)
previous = 0
current = 1

for i in rng:
    print(current)
    current = current + previous
    previous = current - previous

    