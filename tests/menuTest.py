# Pretty sure this is redundant as its already implemented

import pyperclip
from time import sleep
import random
from datetime import date
solvedOut = """
⬜️⬜️🟨⬜️⬜️
🟩⬜️⬜🟨🟨
🟩🟩⬜️⬜️🟨
🟩🟩🟩🟩🟩
"""

global variables
variables = {}


# Set Daily Word
def setDaily(todayDate,word):
    with open("daily.txt", "w") as g, open("wordle.txt","r") as f:
    
        if g.readline(0) == todayDate:
            close(g)
        elif g.readlines != todayDate:
            word = random.choice(f.readlines())
            g.write("{todayDate}/n{word}")

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
            word = random.choice(f.readlines())
            # DEBUG USE ONLY
            variables.append("word : {word}")
            sleep(2)
            if name == "nt":
                _ = "cls"
            else:
                _ = "clear"
            gameState = False
            variables.append("gameState : ")
        elif choice[0].lower() == "q":
            sure = input("Sure?\ny/N\n> ")
            if sure[0].lower() == "y":
                print("Closing")
                print("\b")
                for x in range(4, 0):
                    print("\b{x}")
                    x -= 1

                quit()


menu()
