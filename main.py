# wordle.py

import random
import collections
import pyperclip
from simple_chalk import chalk
from os import name, system
from time import sleep
from datetime import date

# Globals
word = ''
guessedLetters = ''
guesses = 0
gameState = False  # False = game in progress, True = guessed or exitted
solvedOut = ''
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


def menu():
    menuState = False

    print("""Wordle:
    S - Share
    N - New
    Q - Quit""")

    while not menuState:
        choice = input(">> ")
        # No need to access this as an array???
        if choice.lower() == "s":
            print(solvedOut)
            clipboard = input('Copy to clipboard?\ny/N')
            if clipboard.lower() == "y":
                pyperclip.copy(solvedOut)
                print("Copied to clipboard")
                continue
            elif clipboard.lower == "n":
                print("Not Copied")
                continue
        elif choice.lower() == "n":
            print("New game starting")

            run()

            sleep(2)
        elif choice.lower() == "q":
            sure = input("Sure?\ny/N\n> ")
            if sure.lower() == "y":
                print(chalk.red("Closing..."))

                # Code here is literally useless just say closing

                # print("\b")  # Once again why the random byte string???
                # for x in range(4, 0):
                #     print("\b{x}")  # And here????
                #     x -= 1

                quit()

# Open the file with a handle and have it automatically
# closed after use


def pickWord():
    with open('wordle.txt', 'r') as f:
        return random.choice(f.readlines())

# Set Daily Word


def setDaily(todayDate):
    with open("daily.txt", "r") as g, open("wordle.txt", "r") as f:

        for line in g:
            if line != str(todayDate):
                with open('daily.txt', 'a') as daily:
                    daily.write(f'{todayDate}/n{random.choice(f.readlines())}')


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
                    solvedOut += "\b\b🟩"  # What is with these random byte strings?
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


# End Functions ----------------------


if __name__ == '__main__':
    menu()
