import random

words = open("wordle.txt", "r")  # open words list

word = random.choice(words.readlines())  # pick random word
print("  12345")
correct = ""
guesses = 0
solved = None



while solved != True or guesses <= 5:
    print(correct)
    guess = input(str(guesses+1) + " ")  # input for guesses
    for x in guess:
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
        
    
