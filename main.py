# wordle.py

import random
import collections
from simple_chalk import chalk
import pyperclip
from os import name, system
from time import sleep, strftime
from datetime import date

# Globals
word = ''
guessedLetters = ''
guesses = 0
global gameState
gameState = False  # False = game in progress, True = guessed or exitted
global solvedOut
solvedOut = ""
todayDate = date.today()
clearLast = "\b\b\b\b\b\b"
# Functions -------------------------

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def countLetters(letter, string):
    letterCount = 0

    for l in string:
        if l == letter:
            letterCount += 1

    return letterCount

def menu():
    menuState = False
    print("""Wordle:
    S - Share
    N - New
    Q - Quit""")
    while not menuState:
        choice = input(">> ")
        if choice[0].lower() == "s":
            print(solvedOut)
            clipboard = input("""Copy to clipboard?\ny/N""")
            if clipboard[0].lower() == "y":
                pyperclip.copy(solvedOut)
                print("copied to clipboard")
                continue
            elif clipboard[0].lower == "n":
                print("Not Copied")
                continue
        elif choice[0].lower() == "n":
            print("New game starting")
            word = random.choice(f.readlines())
            sleep(2)
            if name == "nt":
                _ = "cls"
            else:
                _ = "clear"
            gameState = False
        elif choice[0].lower() == "q":
            sure = input("Sure?\ny/N\n> ")
            if sure[0].lower() == "y":
                print("Closing in ")
                print("\b")
                for x in range(4,0):
                    print("\b{x}")
                    x -= 1

                quit()
            
# End Functions ----------------------

# Set Daily Word
def setDaily(todayDate,word):
    with open("daily.txt", "w") as g, open("wordle.txt","r") as f:
    
        if g.readline(0) == todayDate:
            close(g)
        elif g.readlines != todayDate:
            word = random.choice(f.readlines())
            g.write("{todayDate}/n{word}")


# Open the file with a handle and have it automatically
# closed after use

def pickword():
    with open('wordle.txt', 'r') as f:
        word = random.choice(f.readlines())
    return word
word = pickword()
"""
# DEBUG USE ONLY
    #word = random.choice(f.readlines())

# DEBUG USE ONLY
    word = random.choice(f.readlines())

# DEBUG USE ONLY
    word = random.choice(f.readlines())
"""
print(chalk.red(word))

# Work out number of repeated letters in the word
freq = collections.Counter(word)
repeated = {}

for key, val in freq.items():
    if val > 1:
        repeated[key] = val


menu()


# Main game loop
while not gameState:
    print("|||||")
    print("\b")   
    for guess in range(5):
        print(guessedLetters)
        guessedLetters = ''
        guess = input()
        guesses += 1

        # If the guess is equal to the word end the game
        if guess.lower() + '\n' == word.lower():
            print(chalk.green('Congratulations you solved the Wordle!'))
            gameState = True
            solvedOut += "\n🟩🟩🟩🟩🟩"
            break

        hasDuplicates = False
        for x in range(len(guess)):

            # Check for repeated letters
            for i in repeated:
                if countLetters(word[x], guess) > repeated[i] and not hasDuplicates:
                    print(chalk.red(f"Too many {word[x]}'s"))
                    hasDuplicates = True
                    break
            
            # Main checks to decide how to catagorize the letters in terms of colours
            if guess[x] == word[x]:
                guessedLetters += chalk.green(guess[x].lower())
                solvedOut += "\b\b🟩"
                continue
            elif guess[x] in word:
                guessedLetters += chalk.yellow(guess[x].lower())
                solvedOut += "\b\b🟨"
                print(clearLast)
            else:
                guessedLetters += chalk.grey('-')
                solvedOut += "\b\b⬜️"
            solvedOut += "\n"


    print(chalk.red('Game over!'))
    print(solvedOut)
    gameState = True
    setDaily(todayDate,pickword())
    #menu()