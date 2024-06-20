import random as r
import os
def guess():
  os.system('cls')
  number = int(r.randint(1, 10))
  loop = 0
  while loop < 3:
    answer = int(input(":::"))
    if answer > number:
      print("lower")
    elif answer < number:
      print("higher")
    elif answer == number:
      print(f"your answer is correct, {number}")
      break
    else:
      print("invalid")
    loop = loop + 1

def computer_guess(peak):
    low = 1
    feedback = ''
    while feedback != 'c':
        if low != peak:
            guess = r.randint(low, peak)
        else:
            guess = low
        feedback = input(f'Is {guess} high (H), low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            peak = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Your number is {guess}. ')
while True:
  print("1. User guess")
  print("2. Computer guess")
  choice = input("which one you want to play::")
  if choice == "1":
    guess()
  elif choice == "2":
    user = int(input("Enter a your number::"))
    computer_guess(user)
  else:
    print("Invalid")
  cont = input("want to play again? (y/n)")
  if cont == "y":
    os.system("cls")
  else:
    break
  os.system("cls")
