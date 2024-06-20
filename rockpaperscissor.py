import random as r
import os
def rockpaperscissor():
    data = ["rock","paper","scissor"]
    while True:
        os.system("cls")
        num = r.randint(0, 2)
        computer = data[num]
        user = input("Rock, Paper or Scissor? :: ")
        user = user.lower()
        if user == computer:
            os.system("cls")
            print(f"your choice {user} and computer chose {computer}")
            print("Draw")
        elif user == "rock" and computer == "paper":
            os.system("cls")
            print(f"your choice {user} and computer chose {computer}")
            print("Computer wins")
        elif user == "rock" and computer == "scissor":
            os.system("cls")
            print(f"your choice {user} and computer chose {computer}")
            print("You win")
        elif user == "paper" and computer == "rock":
            os.system("cls")
            print(f"your choice {user} and computer chose {computer}")
            print("You win")
        elif user == "paper" and computer == "scissor":
            os.system("cls")
            print(f"your choice {user} and computer chose {computer}")
            print("Computer wins")
        elif user == "scissor" and computer == "paper":
            os.system("cls")
            print(f"your choice {user} and computer chose {computer}")
            print("You win")
        elif user == "scissor" and computer == "rock":
            os.system("cls")
            print(f"your choice {user} and computer chose {computer}")
            print("Computer wins")
        else:
            os.system("cls")
            print("invalid input")
        cont = input("want to play again? (y/n)")
        if cont == "n":
            break
        else:
            os.system("cls")
            print("restarting")
rockpaperscissor()