# wordle.py

import random
import collections
import pyperclip
from simple_chalk import chalk
from os import name, system
from time import sleep
from datetime import date

# Globals
global word
word = ''
guessedLetters = ''
guesses = 0
global gameState
gameState = True  # False = game in progress, True = guessed or exitted
solvedOut = ''
global todayDate
todayDate = date.today()
clearLast = '\b\b\b\b\b\b'

# This allows chalk to work in the windows terminal
system('')

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




# Set Daily Word
def setDaily(todayDate):
    with open(".daily.txt", "w") as g, open(".wordle.txt", "r") as f:

        if g.readline(0) == todayDate:
            g.close(g)
            print("Today's wordle has already been completed")
        elif g.readlines != todayDate:
            word = random.choice(f.readlines())
            g.write("{todayDate}/n{word}")
    return word

"""# New word generator
def pickWord():
    with open(".wordle.txt", "r") as f:
        word = random.choice(f.readlines())
    return word"""

# Open the file with a handle and have it automatically
# closed after use


def pickWord():
    with open('.wordle.txt', 'r') as f:
        return random.choice(f.readlines())


def run():

    # Main game loop
    gameState = False
    word = pickWord()

    # Work out number of repeated letters in the word
    freq = collections.Counter(word)
    repeated = {}

    for key, val in freq.items():
        if val > 1:
            repeated[key] = val

    while not gameState:
        # Get globals
        global solvedOut
        global guessedLetters
        global guesses

        # DEBUG USE ONLY
        print(chalk.red(word))

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
        # print(solvedOut) # Pretty sure this is useless as it seems broken??
        gameState = True
        setDaily(todayDate)


def menu():
    menuState = False
    print("""Wordle:
    S - Share 
    N - New 
    D - Play Daily
    Q - Quit""")
    while not menuState:
        choice = input(">> ")
        if choice[0].lower() == "s":

            print(solvedOut)
            clipboard = input("""Copy to clipboard?\ny/N\n >> """)
            if clipboard[0].lower() == "y":
                pyperclip.copy(solvedOut)
                print("copied to clipboard")
                continue
            elif clipboard[0].lower == "n":
                print("Not Copied")
                continue
        elif choice[0].lower() == "n":
            print("New game starting")
            pickWord()

           
            sleep(2)
            if name == "nt":
                _ = "cls"
            else:
                _ = "clear"
            gameState = False
            menuState = True
        elif choice[0].lower() == "d":
            print("Daily game starting")
            with open(".daily.txt") as f:
                word = f.readline(2)

            sleep(2)
            if name == "nt":
                _ = "cls"
            else:
                _ = "clear"
            gameState = False
            menuState = True
        elif choice[0].lower() == "q":
            sure = input("Sure?\ny/N\n> ")
            if sure[0].lower() == "y":
                print("Closing")
                print("\b")
                for x in range(4, 0):
                    print("\b{x}")
                    x -= 1

                quit()



# Set Daily Word


menu()



# End Functions ----------------------


# Main Code --------------------------

