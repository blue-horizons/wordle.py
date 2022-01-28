#PYTHON - WORDLESS.PY

#setup

import random
#import pyperclip
#from datetime import datetime

#date = datetime.now("%d/%m/%Y @ %H:%M")
wordList = open("wordle.txt","r")

word = random.choice(wordList.readlines())

#ANSI Codes
#\033[1;40;32m HIGHLIGHT GREEN

#\033[1;40;30m HIGHLIGHT DARK GRAY

#\033[1;40;33m HIGHLIGHT YELLOW

ansiSupport = input("""
Do you know if your terminal supports ANSI formatting?
If it does, the text below should be highlighted green.
If you don't know, put N.
\033[1;40;32m IF I'M GREEN YOU HAVE ANSI

y/N

> """)

if ansiSupport.lower() == "y":
    ansiTrue == True
elif ansiSupport.lower() == "n":
    ansiTrue == false
def guessCheck(word, guess):
    if len(guess) == len(word):
        for x in guess:
            if guess[x] == word[x]:
                correctOut += "\u1f7e9" #green square
                print(correctOut)
            elif guess[x] in word:
                correctOut += "\u1f7e8"
                print(correctOut)
            else:
                correctOut += "\u2b1c"
                print(correctOut)
        
        print(correctOut)
        return correct
        return correctOut


def guessCheckANSI(word, guess):
    if len(guess) == len(word) and len(guess) == 5:
        for x in guess:
            if guess[x] == word[x]:
                correct += f"\033[1;40;32m {x}"
                correctOut += "\u1f7e9" #green square
            elif guess[x] in word:
                correct += f"\033[1;40;33m {x}"
                correctOut += "\u1f7e8" #yellow square
            else:
                correct += f"\033[1;40;30 {x}"
                correctOut += "\u2b1c" #Grey/White square

        return correct
        return correctOut




if ansiTrue == False:
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

else:
    guess1 = input()
    guessCheckANSI(word, guess1)
    
    guess2 = input()
    guessCheckANSI(word, guess2)

    guess3 = input()
    guessCheckANSI(word, guess3)

    guess4 = input()
    guessCheckANSI(word, guess4)

    guess5 = input()
    guessCheckANSI(word, guess5)

    guess6 = input()
    guessCheckANSI(word, guess6)



if guess6 == word:
    print("""SUCCESS!! You have solved the wordle.""")
    print(correctOut)
    
    while choice != "Q":
        print("S Share\nN New\nQ Quit")
        choice  = input("> ").lower()
        if choice == "S":
            #print("Copying to clipboard.")
            #pyperclip.copy(correctOut)
            print("\n" + correctOut)
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
        
            
    


