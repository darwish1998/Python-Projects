import random

print("This a Dice Game: ")
x = "y"
while x == "y":
    number = random.randint(1,6)

    if (number == 1):
        print("----------")
        print("|        |")
        print("|    O   |")
        print("|        |")
        print("----------")
    elif (number == 2):
        print("-----------")
        print("|    O    |")
        print("|         |")
        print("|    O    |")
        print("----------")
    elif (number == 3):
        print("----------")
        print("|    O    |")
        print("|    O    |")
        print("|    O    |")
        print("----------")
    elif (number == 4):
        print("-----------")
        print("| O     0 |")
        print("|         |")
        print("| 0     0 |")
        print("-----------")

    elif (number == 5):
        print("----------")
        print("| O     0 |")
        print("|    0    |")
        print("| 0     0 |")
        print("-----------")
    else:
        print("----------")
        print("| O     0 |")
        print("| O     0 |")
        print("| 0     0 |")
        print("----------")
    x = input("Roll the dice again: press y or Y ")
