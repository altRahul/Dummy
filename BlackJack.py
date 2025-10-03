#BlackJack
import random
import sys

def sum_of_cards(deck1,deck2):
    if sum(tuple(deck1))>sum(tuple(deck2)):
        print("*******************You WIN !*******************")
    else:
        print("*******************You LOSE !*******************")

def facecard(deck):

    for face_card in ["J","Q","K"]:
        if face_card in deck:
            deck[deck.index(face_card)]=10

    if deck==players_deck:
        if "A" in deck:
            deck[deck.index("A")]=int(input("Enter 11 or 1 to assing A: "))
            print(f"\nYour final deck: {deck}\n")
    else:
        duplicate=list(deck)
        if "A" in deck:
            duplicate.remove("A")
            if sum(tuple(duplicate))>=11:
                deck[deck.index("A")]=1
            else:
                deck[deck.index("A")]=11

def check_bust(deck):
    if sum(tuple(deck))>21:
        if deck==players_deck:
            print("*******************YOU BUST !*******************")
            sys.exit()
        else:
            print("*******************COMPUTER BUST !*******************")
            sys.exit()

def another_card(choice,deck):
    if choice=="y":
        deck.append(random.choice(cards))
        return deck
    if choice=="n":
        return deck

#intro
wanna_play=input("Do you wanna play Black Jack? Type in 'y' to play! ").lower()
cards=["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]

#randomly choosing cards for theplayer and computer
players_deck=[random.choice(cards),random.choice(cards)]
computers_deck=[random.choice(cards),random.choice(cards)]

#hiding a cand of the computers hand
hidden_c_deck=list(computers_deck)
hidden_c_deck[random.randint(0,1)]="?"

#printing decks
print(f"\nYour deck: {players_deck}\n")
print(f"Computer\'s deck: {hidden_c_deck}\n")

#adding another card for user
user_choice=input("Enter 'y' to get another card, type 'n' to pass: ").lower()
print(f"\nYour final deck: {another_card(user_choice,players_deck)}\n")

for face_Card in ["A","J","Q","K"]:
    facecard(players_deck)
check_bust(players_deck)

#adding andther card for computer
facecard(computers_deck) #changing values of face card
y_n=["y","n"]
if sum(tuple(computers_deck))>=11:
    user_choice=random.choice(y_n)
else:
    user_choice="y"
if "A" in computers_deck:
    user_choice="y"
print(f"Computer\'s final deck: {another_card(user_choice,computers_deck)}")

facecard(computers_deck) #again changing values of face card if any new face was added
check_bust(computers_deck)

sum_of_cards(players_deck,computers_deck)
