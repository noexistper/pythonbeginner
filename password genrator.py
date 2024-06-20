import random as r
import os
import string
os.system("cls")
lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)
number = list(range(10))
symbols = list(string.punctuation)
password = []
passw = []
limit = input("Length of password:: ")
limit = int(limit)
os.system("cls")
def custom():
    print("Enter any keyword of your type:: ")
    user = input()
    userlist = [char for char in user]
    for i in range(limit):
        pas = r.choice(userlist)
        password.append(pas)
        i+=1
    print("Password is -->")
    print("".join(password))

def randompass():
    print(f"lowercase, uppercase, numbers and symbols. Total:: {limit}")
    low0 = int(input("How many lowercase alphabet you want in your password:: "))
    up0 = int(input("How many uppercase alphabet you want in your password:: "))
    num0 = int(input("How many numbers you want in your password:: "))
    sym0 = int(input("How many symbols alphabet you want in your password:: "))
    sum =low0+up0+num0+sym0
    if sum > limit or sum < limit:
        print ("your calculation is wrong.")
    else:
        sample0 = r.sample(lowercase, low0)
        sample1 = r.sample(uppercase, up0)
        sample2 = r.sample(number, num0)
        sample3 = r.sample(symbols, sym0)
        randomizing = [[sample0],[sample1],[sample2],[sample3]]
        r.shuffle(randomizing)
        for pas in randomizing:
            r.shuffle(pas)
            password.append(pas)
        pas = [item for sublist in password for item in sublist]
        pa = [item for sublist in pas for item in sublist]
        r.shuffle(pa)
        string = "".join(str(x) for x in pa)
        os.system("cls")
        print(f" password include:: {low0} lowercase alphabets, {up0} uppercase alphabets, {num0} numbers and {sym0} symbols.")
        print(f"new generated password--> {string}")
    

print("1. Generate from user input.")
print("2. Generate random.")
choice = input("::")
if choice == "1":
    os.system("cls")
    custom()
elif choice == "2":
    os.system("cls")
    randompass()
else:
    os.system("cls")
    print("Invalid option")