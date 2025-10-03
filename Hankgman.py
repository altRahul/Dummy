#Hangman:

#Selecting a random word
import random
random_word_list=["WORLD","EARTH","PLANETS","GALAXY","SUN","MOON"]
random_word=random.choice(random_word_list)

#message to be shown if lost
message=["!","R","E","V","O"]

#filling random wrod with blanks
blanks="_ "*len(random_word)
blank_word_list=list("_"*len(random_word)) #the blank word shown in output
print(blanks)


life=5
end_message="" #OVER!
output_word="" 

#loop
while life!=0 and blank_word_list!=list(random_word):

    #input from user
    guess=input("\nEnter the letter: ").upper()

    if guess in random_word:
        
        if guess in blank_word_list:
             print("\nYou have already guessed it! guess an another letter!")
             continue
        
        #to find index of all recurring elements
        for index in range(len(random_word)):
            if random_word[index]==guess:
                blank_word_list[index]=guess
                
        #to print the random word in string
        for letter in blank_word_list:
            output_word+=letter+" "
        print(f"\n{output_word}")
        output_word=""
        continue
    
    else:
        life-=1
        end_message+=message[life]
        print(f"\nRemaining life: {life}\n\n********************{end_message}********************")
        if life==0:
            print("******************YOU LOSE!******************")

if blank_word_list==list(random_word):
        print("\n********************YOU WIN!********************")
