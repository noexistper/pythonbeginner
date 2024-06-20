import random as r
import os
def game():
    animals = ["lion", "tiger", "elephant", "giraffe", "zebra", "camel"]
    stages = [
        """
         ------
         |    |
         |    O
         |   /|\\
         |   / \\
         |
         --------
        """,
        """
         ------
         |    |
         |    O
         |   /|\\
         |   / 
         |
         --------
        """,
        """
         ------
         |    |
         |    O
         |   /|\\
         |    
         |
         --------
        """,
        """
         ------
         |    |
         |    O
         |   /|
         |    
         |
         --------
        """,
        """
         ------
         |    |
         |    O
         |    |
         |    
         |
         --------
        """,
        """
         ------
         |    |
         |    O
         |    
         |    
         |
         --------
        """,
        """
         ------
         |    |
         |    
         |    
         |    
         |
         --------
        """
    ]
    attempts = 5
    int(attempts)
    while attempts >= 0:
        zoo = r.choice(animals)
        print("guess a zoo animal name, which is in my mind. ")
        answer=input("::")
        if answer == zoo:
            print("You WON")
            break
        elif answer != zoo:
            os.system("cls")
            print(f"Wrong, {attempts} remaining.")
            print(stages[attempts])
        else:
            print(f"Invalid, {attempts} remaining.")
            print(stages[attempts])
        attempts = attempts - 1

print("Game")
while True:
    game()
    cont = input("Want to play again (y/n)? ::")
    cont = cont.lower()
    if cont == "y":
        os.system("cls")
    else:
        break