#PYTHON - WORDLESS.PY

# setup

import random
import os
import time
import sys


#import pyperclip
#from datetime import datetime

#date = datetime.now("%d/%m/%Y @ %H:%M")
wordList = open("wordle.txt", "r")
print("Words Imported")

word = random.choice(wordList.readlines())
print("Word Chosen")
# ANSI Codes
# \033[1;40;32m HIGHLIGHT GREEN

# \033[1;40;30m HIGHLIGHT DARK GRAY

# \033[1;40;33m HIGHLIGHT YELLOW
ansiTrue = None

global correctOut
global correct


ansiSupport = input("""
Do you know if your terminal supports ANSI formatting?
If it does, the text below should be highlighted green.
If you don't know, put N.
\033[1;40;32m IF I'M GREEN YOU HAVE ANSI

y/N

> """)

if ansiSupport.lower() == "y":
    ansiTrue == True
    print("\033[1;40;33m ANSI Colours Enabled")
elif ansiSupport.lower() == "n":
    ansiTrue == False
    print("ANSI Colours not Enabled")


def guessCheck(word, guess):
    correctOut = ""
    if len(guess) == len(word):
        for x in guess:
            if guess[x] == word[x]:
                correctOut += "\u1f7e9"  # green square
                print(correctOut)
            elif guess[x] in word:
                correctOut += "\u1f7e8"
                print(correctOut)
            else:
                correctOut += "\u2b1c"

                print(correctOut)

        sys.stdout.write(correctOut)

        return correctOut


def guessCheckANSI(word, guess):
    global correctOut
    correctOut = ""
    correct = ""
    if len(guess) == len(word) and len(guess) == 5:
        for x in guess:
            if guess[x] == word[x]:
                correct += f"\033[1;40;32m {x}"
                correctOut += "\u1f7e9"  # green square
            elif guess[x] in word:
                correct += f"\033[1;40;33m {x}"
                correctOut += "\u1f7e8"  # yellow square
            else:
                correct += f"\033[1;40;30 {x}"
                correctOut += "\u2b1c"  # Grey/White square

        sys.stdout.write(correct)
        return correctOut


def clearLine():
    sys.stdout.flush()
    print("\b")


if ansiTrue == False:
    print("Wordle - START")

    guess1 = input()
    # os.system('cls')
    clearLine()
    guessCheck(word, guess1)

    guess2 = input()
    # os.system('cls')
    clearLine()
    guessCheck(word, guess2)

    guess3 = input()
    # os.system('cls')
    clearLine()
    guessCheck(word, guess3)

    guess4 = input()
    # os.system('cls')
    clearLine()
    guessCheck(word, guess4)

    guess5 = input()
    # os.system('cls')
    clearLine()
    guessCheck(word, guess5)

    guess6 = input()
    # os.system('cls')
    clearLine()
    guessCheck(word, guess6)

elif ansiSupport == True:
    print("\u001b[31mWordle - START")
    guess1 = input()
    # os.system('cls')
    clearLine()
    guessCheckANSI(word, guess1)

    guess2 = input()
    # os.system('cls')
    clearLine()
    guessCheckANSI(word, guess2)

    guess3 = input()
    # os.system('cls')
    # clearLine()
    guessCheckANSI(word, guess3)

    guess4 = input()
    # os.system('cls')
    clearLine()
    guessCheckANSI(word, guess4)

    guess5 = input()
    # os.system('cls')
    clearLine()
    guessCheckANSI(word, guess5)

    guess6 = input()
    # os.system('cls')
    clearLine()
    guessCheckANSI(word, guess6)


if guess6 == word:
    print("""SUCCESS!! You have solved the wordle.""")
    print(correctOut)

    while choice != "Q":
        print("S Share\nN New\nQ Quit")
        choice = input("> ").lower()
        if choice == "S":
            #print("Copying to clipboard.")
            # pyperclip.copy(correctOut)
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
