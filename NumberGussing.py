import sys
import random

print("Welcome to number guessing game!")
print("Think of a number between 1 and 100")

random_number=random.randint(1,100)
level=input("\nEnter 'Hard' for hard level and 'Easy' for easy level: ").lower()
if level=="hard":
    print("\nYou have 5 chances to guess the number.")
    chance=5
    while chance!=0:
        inp=int(input("\nGuess the number: "))
        if inp==random_number:
            print("You WIN !")
            sys.exit()
        elif inp>random_number:
            print("Too high")
            chance-=1
        elif inp<random_number:
            print("Too low")
            chance-=1
    print("You lose !")

if level=="easy":
    print("\nYou have 10 chances to guess the number.")
    chance=10
    while chance!=0:
        inp=int(input("\nGuess the number: "))
        if inp==random_number:
            print("You WIN !")
            sys.exit()
        elif inp>random_number:
            print("Too high")
            chance-=1
        elif inp<random_number:
            print("Too low")
            chance-=1
    print("You lose !")   
