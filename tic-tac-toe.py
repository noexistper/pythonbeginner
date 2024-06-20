import os
def sum(a, b, c):
    return a+b+c

def board(x, z):
    zero = 'X' if x[0] else ('Z' if z[0] else 0)
    one = 'X' if x[1] else ('Z' if z[1] else 1)
    two = 'X' if x[2] else ('Z' if z[2] else 2)
    three = 'X' if x[3] else ('Z' if z[3] else 3)
    four = 'X' if x[4] else ('Z' if z[4] else 4)
    five = 'X' if x[5] else ('Z' if z[5] else 5)
    six = 'X' if x[6] else ('Z' if z[6] else 6)
    seven = 'X' if x[7] else ('Z' if z[7] else 7)
    eight = 'X' if x[8] else ('Z' if z[8] else 8)
    print(f" {zero} | {one} | {two} ")
    print(f" --|---|-- ")
    print(f" {three} | {four} | {five} ")
    print(f" --|---|-- ")
    print(f" {six} | {seven} | {eight} ")

def checkmate(x, z):
    xwins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in xwins:
        if sum(x[win[0]], x[win[1]], x[win[2]]) == 3:
            print("X WON")
            return 1
        elif sum(z[win[0]], z[win[1]], z[win[2]]) == 3:
            print("Z WON")
            return 0
    return -1
    if sum(i) == 3:
        return 1

x = [0, 0, 0, 0, 0, 0, 0, 0, 0]
z = [0, 0, 0, 0, 0, 0, 0, 0, 0]
turn = True
while True:
    print("TIC-TAC-TOE")
    while True:
        board(x, z)
        if int(turn) == 1:
            print("Player X input")
            value = int(input("Enter a value:"))
            x[value] = 1
        else:
            print("Player Z input")
            value = int(input("Enter a value:"))
            z[value] = 1
        cmate = checkmate(x, z)
        if cmate != -1:
            print("MATCHOVER")
            break
        turn = not turn
    cont = input("Want to play again? (y/n)")
    if cont == "y":
        os.system("cls")
    else:
        break 
    