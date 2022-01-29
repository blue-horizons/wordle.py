

guess = input("word = ")

word = "hello"
correct = ""
correctOut = ""
"""
size = min(len(guess), len(word))

for i in range(size):
    if guess[i] == word[i]:
       correct += "\033[1;40;32m {i}"
       correctOut += "\u1f7e9"  # green square
"""

for x in guess:
    if guess[x] == word[x]:
        correct += "\033[1;40;32m {x}"
        correctOut += "\u1f7e9"  # green square
    elif guess[x] in word:
        correct += "\033[1;40;33m {x}"
        correctOut += "\u1f7e8"  # yellow square
    else:
        correct += "\033[1;40;30 {x}"
        correctOut += "\u2b1c"  # Grey/White square

print(correct)
print(correctOut)
