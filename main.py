# wordle.py

import random
import collections
from simple_chalk import chalk

# Globals
word = ''
guessedLetters = ''
guesses = 0
gameState = False  # False = game in progress, True = guessed or exitted

# Functions -------------------------


def countLetters(letter, string):
    letterCount = 0

    for l in string:
        if l == letter:
            letterCount += 1

    return letterCount

# End Functions ----------------------


# Open the file with a handle and have it automatically
# closed after use
with open('wordle.txt', 'r') as f:
    word = random.choice(f.readlines())

# DEBUG USE ONLY
print(chalk.red(word))

# Work out number of repeated letters in the word
freq = collections.Counter(word)
repeated = {}

for key, val in freq.items():
    if val > 1:
        repeated[key] = val

# Main game loop
while not gameState:
    for guess in range(5):
        print(guessedLetters)
        guessedLetters = ''
        guess = input(f'{guesses + 1} Enter A Guess: ')
        guesses += 1

        # If the guess is equal to the word end the game
        if guess.lower() + '\n' == word.lower():
            print(chalk.green('Congratulations you solved the Wordle!'))
            gameState = True
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
                continue
            elif guess[x] in word:
                guessedLetters += chalk.yellow(guess[x].lower())
            else:
                guessedLetters += chalk.grey('-')

    print(chalk.red('Game over!'))
    gameState = True
