import random

words = open("wordle.txt", "r")  # open words list

word = random.choice(words.readlines())  # pick random word
print("12345")
correct = ""
guesses = 0
solved = None

while solved != True and guesses <= 6:
    guess = input()  # input for guesses
    for x in guess:  # adds correct letters, removes incorrect letters
        for y in range(0, 4):
            if guess == word:  # guess == word?
                correct = word
                solved = True
                print("you solved the wordle")
            elif guess[y] == word[y]:
                correct = correct + x.upper()
                guesses += 1
            elif guess[y] in word:
                correct = correct + x.lower()
                guesses += 1
            else:
                correct = correct + "-"
                guesses += 1
