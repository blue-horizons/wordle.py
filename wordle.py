#PYTHON - WORDLESS.PY

#setup

import random

wordList = open("wordle.txt")

word = random.choice(wordList.readlines)

#\033[1;40;32m HIGHLIGHT GREEN

#\033[1;40;30m HIGHLIGHT DARK GRAY

#\033[1;40;33m HIGHLIGHT YELLOW



guess1 = input()

def guessCheck()
    for x in guess1:

        if guess1[x] in word:

            correct += f"\033[1;40;33m {x}"
            if guess1[x] == word[x]:
                correct += f"\033[1;40;32m {x}"
