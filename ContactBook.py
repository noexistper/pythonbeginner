import json
import os
os.system("cls")
def writebook():
    name= input("Enter name: ")
    number= int(input("Enter number: "))
    email= input("Enter email: ")
    Contactnumbers = {"name": name, "number": number, "Email": email}
    os.system("cls")
    
    with open("contact_list.json", "a") as f:
        for key, value in Contactnumbers.items():
        
            f.write(f"{key} :: {value}\n")
        f.write("------------------------------------ \n")   
            
    f.close()
def readbook():
    if os.stat("contact_list.json").st_size == 0:
        print("Book is empty.")
    else:
        with open("contact_list.json", "r") as f:
            content = f.read()
            print(content)

while True:
    print("1. Read")
    print("2. Write")
    choice = int(input(":: "))
    if choice == 1:
        readbook()
    elif choice == 2: 
        while True:
            writebook()
            cont = input("Want to save another? (y/n) :: ")
            if cont == "n":
                break
            else:
                os.system("cls")
    cont = input("Want to run program again? (y/n) :: ")
    if cont == "n":
        break
    else:
        os.system("cls")
