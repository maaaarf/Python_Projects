import sys

misinp = + 0

xscore = 0


intro = input("Are you ready to play Osu! ? (Y/N): ").upper()

while True:
    if intro == "Y":
        break
    if intro == "N":
        sys.exit()

hits = input("Enter how many times you would like to hit: ")
hits1 = int(hits)

nohits = range(0,hits1,1)

print(("Would you like to hit 'Miss', 'Bad', 'Good', or 'Perfect'?: "))

for idk in nohits:

    hitinp = int(idk)

    if hitinp <= idk:
        userinp = input().lower()

        uinp = str(userinp)

        if userinp == "miss":
            print(misinp)
        
print(f"Your score is {xscore + misinp}")


