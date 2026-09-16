userin = input("Would you like to convert to Celsius or Farenheit? (C/F): ").lower()

if userin == "c":
    temp = "Celsius"
    numin =int(input("Enter a temperature: "))
    faren = (numin - 32)*(5/9)
    print(f"You converted from {temp}, and your temperature now is {faren:.2f} degrees F")

elif "f":
    temp2 = "Farenheit"
    numin2 = int(input("Enter a temperature: "))
    cels = (numin2*(9/5)) + 32
    print(f"You converted from {temp2}, and your temperature now is {cels:.2f} degrees C")

