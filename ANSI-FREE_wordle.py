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
    for x in range(0, len(guess)):
        if guess == word:  # guess == word?
            correct = word
            solved = True
            print("you solved the wordle")
        else:
            if guess[x] == word[x]:
                correct = correct + guess[x].upper()
            
            elif guess[x] in word:
                correct = correct + guess[x].lower()
        
            else:
                correct = correct + "-"
    guesses += 1
        
    
