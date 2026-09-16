import json
import sys

with open("creds.json", "r") as credopen:
    acc_check = json.load(credopen)


welcome = print("Welcome to BookFace! Do you already have an acccount?")
deci1 = input("Y/N: ").upper()
if deci1 == "Y":
    print("Enter your account username and password below: ")

elif "N":
    print("Please sign-up below")
    signup = input("Enter an account name: ")
    acc_check["userdata"].append(signup)
    signuppass = input("Enter a password: ")
    acc_check["passdata"].append(signuppass)
    print("Account created!")
    print("Enter your username and password below: ")

with open("creds.json", "w") as accname:
    json.dump(acc_check, accname)

valid_creds = False
while not valid_creds:

    loginuser = input("Username: ")
    logpassword = input("Password: ")

    with open("creds.json") as useracc:
        userload = json.load(useracc)
        
        if loginuser in acc_check["userdata"]:
            index = acc_check["userdata"].index(loginuser)

            if logpassword == acc_check["passdata"][index]:
                print("woohoo congrats")
                valid_creds = True
        
        else: 
            print("Sorry, you prolly dont have an acc yet.")
            break

       