import random

words = open("wordle.txt", "r")  # open words list

word = random.choice(words.readlines())  # pick random word
print("  12345")
correct = ""
guesses = 0
solved = None



while solved != True and guesses < 6:
    guess = input(str(guesses+1) + " ")  # input for guesses
    print(correct)
    if guess == word:  # guess == word?
        correct = word
        solved = True
        print("you solved the wordle")
    elif guess[guesses] == word[guesses]:
        correct = correct + guess[guesses].upper()
        guesses += 1
    elif guess[guesses] in word:
        correct = correct + guess[guesses].lower()
        guesses += 1
    else:
        correct = correct + "-"
        guesses += 1
        
    
