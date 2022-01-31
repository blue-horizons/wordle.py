import random

global alphabet
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

words = open("wordle.txt", "r")  # open words list

word = random.choice(words.readlines())  # pick random word
print("  12345")
correct = ""
guesses = 0
solved = None

def countLetter(letter,string):
    for x in string:
        if string[x] == letter:
            alphabet = alphabet - letter


while solved != True:  # or guesses <= 5:
    for i in range(0, 5):
        print(correct)
        correct = ""

        guess = input(str(guesses+1) + " ")  # input for guesses
        guesses += 1
        for x in range(0, len(guess)):
            if guess.lower() == word.lower():  # guess == word?
                correct = word
                print("You Solved The Wordle!!!")
                solved = True
            elif guess == "#####":
                print("DEBUG\n")
                print(word)
                guesses = 0
            else:
                if guess[x] == word[x] and guess[x] != word[x]:
                    correct = correct + guess[x].upper()
                    print(alphabet.lower())
                elif guess[x] in word:
                    correct = correct + guess[x].lower()

                else:
                    correct = correct + "-"
                    alphabet = alphabet - guess[x]
                    print[x]
