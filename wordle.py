#PYTHON - WORDLESS.PY

#setup

import random
#import pyperclip
from datetime import datetime

date = datetime.now("%d/%m/%Y @ %H:%M")
wordList = open("wordle.txt","r")

word = random.choice(wordList.readlines())

#\033[1;40;32m HIGHLIGHT GREEN

#\033[1;40;30m HIGHLIGHT DARK GRAY

#\033[1;40;33m HIGHLIGHT YELLOW


def guessCheck(word, guess):
    if len(guess) == len(word):
        for x in guess:
            if guess[x] == word[x]:
                correct += f"\033[1;40;32m {x}"
                correctOut += "\u1f7e9" #green square
            elif guess[x] in word:
                correct += f"\033[1;40;33m {x}"
                correctOut += "\u1f7e8"
            else:
                correct += f"\033[1;40;30 {x}"
                correctOut += "\u2b1c"

        return correct
        return correctOut


guess1 = input()
guessCheck(word, guess1)

guess2 = input()
guessCheck(word, guess2)

guess3 = input()
guessCheck(word, guess3)

guess4 = input()
guessCheck(word, guess4)

guess5 = input()
guessCheck(word, guess5)

guess6 = input()
guessCheck(word, guess6)

if guess6 == word:
    print("""SUCCESS!! You have solved the wordle.""")
    print(correctOut)
    
    while choice != "Q":
        print("S Share\nN New\nQ Quit")
        choice  = input("> ").lower()
        if choice == "S":
            #print("Copying to clipboard.")
            #pyperclip.copy(correctOut)
            print(date + "\n" + correctOut)
        elif choice == "N":
            repeat = True
        elif choice == "Q":
            choice = input("""Sure?
            y/N""")
            if choice.lower() == "y":
                print("closing")
                quit()
        else:
            print("Invalid Option")
        
            
    


